#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NUCLEAPP — preparazione delle immagini degli impianti
=====================================================

Cosa fa, in un solo comando:
  1. cerca su Wikimedia Commons una fotografia adatta per ogni impianto
  2. scarta automaticamente diagrammi, mappe, loghi e immagini troppo piccole
  3. scarica la migliore in  img/<id>.jpg
  4. legge dai metadati AUTORE e LICENZA reali e li scrive in img/crediti.js

Il sito legge crediti.json da solo: le didascalie si compilano da sole,
con l'attribuzione corretta richiesta dalle licenze Creative Commons.

USO
---
    python3 prepara-immagini.py

    python3 prepara-immagini.py --solo htrpm italia   (solo alcuni impianti)
    python3 prepara-immagini.py --lista               (mostra i candidati senza scaricare)

Serve solo Python 3 (già presente su macOS e Linux; su Windows si installa
da python.org spuntando "Add Python to PATH"). Nessuna libreria esterna.
"""

import json, os, re, sys, urllib.parse, urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA  = "NUCLEAPP/1.0 (divulgazione scientifica; contatto: comitato)"
DIR = "img"

# Per ogni impianto: il file già individuato (se c'è) e le chiavi di ricerca
# di riserva. 'analogo' indica che l'impianto ritratto non è quello descritto.
IMPIANTI = {
 "magnox": dict(nome="Calder Hall",
    file="Calder Hall nuclear power station (11823864155).jpg",
    query=["Calder Hall nuclear power station", "Sellafield Calder Hall"]),
 "rbmk": dict(nome="Chernobyl",
    file="Reactor bloc of the Chernobyl Nuclear Power Plant.JPG",
    query=["Chernobyl Nuclear Power Plant reactor", "Chornobyl nuclear power plant"]),
 "pwr": dict(nome="Sizewell B",
    file="Nuclear power station at Sizewell - geograph.org.uk - 210830 retouched.jpg",
    query=["Sizewell B nuclear power station", "Sizewell nuclear power station"]),
 "bwr": dict(nome="Leibstadt",
    file="Leibstadt Kernkraftwerk Leibstadt AG.jpg",
    query=["Kernkraftwerk Leibstadt", "Leibstadt nuclear power plant"]),
 "candu": dict(nome="Darlington",
    file="Darlington Nuclear Generating Station panorama2.jpg",
    query=["Darlington Nuclear Generating Station", "Darlington nuclear Ontario"]),
 "epr": dict(nome="Olkiluoto 3",
    file="Olkiluoto Nuclear Power Plant 2015-07-21 001.jpg",
    query=["Olkiluoto Nuclear Power Plant", "Olkiluoto 3 EPR"]),
 "ap1000": dict(nome="Sanmen",
    file="Sanmen Nuclear Power Station.jpg",
    query=["Sanmen Nuclear Power Station", "Sanmen nuclear China AP1000"]),
 "bn800": dict(nome="Beloyarsk",
    file="RIAN archive 895485 Beloyarsk nuclear power plant in Sverdlovsk Region.jpg",
    query=["Beloyarsk Nuclear Power Plant", "Belojarsk nuclear power station"]),
 "htrpm": dict(nome="Shidaowan (HTR-PM)",
    file=None,
    query=["Shidao Bay Nuclear Power Plant", "HTR-10 Tsinghua reactor",
           "high temperature gas cooled reactor China"],
    analogo="Impianto analogo: dell'HTR-PM di Shidaowan non esistono fotografie con licenza libera"),
 "onkalo": dict(nome="Onkalo",
    file="Olkiluoto Nuclear Power Plant 2015-07-21 001.jpg",
    query=["Onkalo spent nuclear fuel repository", "Olkiluoto island Posiva"]),
 "wipp": dict(nome="WIPP",
    file="WIPP-04.jpeg",
    query=["Waste Isolation Pilot Plant", "WIPP Carlsbad New Mexico"]),
 "italia": dict(nome="Deposito Nazionale",
    file=None,
    query=["El Cabril radioactive waste disposal", "Centre de stockage de l'Aube ANDRA",
           "low level radioactive waste disposal facility"],
    analogo="Impianto analogo: il Deposito Nazionale italiano non è ancora stato costruito"),
}

# scarto tutto ciò che non è una fotografia dell'impianto
ESCLUDI = re.compile(r"(logo|map|karte|mapa|diagram|schema|schéma|chart|graph|seal|"
                     r"icon|flag|coat of arms|locator|plan |layout|sign|banner|"
                     r"protest|poster|portrait|\.svg$)", re.I)
LIBERE  = re.compile(r"(public domain|cc[ -]?by|cc0|pd-|attribution)", re.I)
# In ricerca il titolo DEVE parlare del soggetto giusto: senza questo controllo
# una parola somigliante basta a far vincere una foto di tutt'altro (la ricerca
# "El Cabril" restituiva una chiesa di Cabrils, in Catalogna).
TOPICO  = re.compile(r"(nuclear|nucleare|nucléaire|kernkraft|atom|reactor|reattore|"
                     r"réacteur|power (plant|station)|repository|radioactive|radiactivo|"
                     r"radioactif|waste|residuos|déchets|stockage|storage|disposal|"
                     r"\bcabril\b|andra|posiva|onkalo)", re.I)
LARGH_MIN = 700          # sotto questa larghezza la foto esce sgranata


def api(params):
    params = dict(params, format="json", formatversion="2")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.load(r)


def pulisci(html):
    if not html:
        return ""
    t = re.sub(r"<[^>]+>", "", str(html))
    t = t.replace("&amp;", "&").replace("&quot;", '"').replace("&#039;", "'")
    return " ".join(t.split())[:160]


def info_file(titolo):
    """Metadati di un file preciso su Commons."""
    d = api(dict(action="query", titles="File:" + titolo, prop="imageinfo",
                 iiprop="url|size|extmetadata", iiurlwidth=1400))
    pagine = d.get("query", {}).get("pages", [])
    if not pagine or pagine[0].get("missing"):
        return None
    ii = pagine[0].get("imageinfo")
    return ii[0] if ii else None


def cerca(query, n=12):
    """Candidati per una ricerca testuale, solo file immagine."""
    d = api(dict(action="query", generator="search",
                 gsrsearch="filetype:bitmap " + query, gsrnamespace=6, gsrlimit=n,
                 prop="imageinfo", iiprop="url|size|extmetadata", iiurlwidth=1400))
    out = []
    for p in d.get("query", {}).get("pages", []):
        ii = p.get("imageinfo")
        if ii:
            out.append((p["title"], ii[0]))
    return out


def valuta(titolo, ii):
    """Punteggio: fotografia grande e con licenza libera vince."""
    if ESCLUDI.search(titolo):
        return -1
    if not TOPICO.search(titolo):
        return -1
    if ii.get("width", 0) < LARGH_MIN:
        return -1
    meta = ii.get("extmetadata", {})
    lic = pulisci(meta.get("LicenseShortName", {}).get("value", ""))
    if not LIBERE.search(lic):
        return -1
    p = min(ii.get("width", 0), 4000) / 100.0
    if "aerial" in titolo.lower() or "panorama" in titolo.lower():
        p += 12
    if re.search(r"(nuclear|kernkraft|power (plant|station)|repository)", titolo, re.I):
        p += 18
    return p


def crediti(ii):
    m = ii.get("extmetadata", {})
    autore = pulisci(m.get("Artist", {}).get("value", "")) or "autore non indicato"
    lic = pulisci(m.get("LicenseShortName", {}).get("value", "")) or "licenza da verificare"
    return autore, lic


def scarica(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as r, open(dest, "wb") as f:
        f.write(r.read())
    return os.path.getsize(dest)


def main():
    args = sys.argv[1:]
    solo = []
    if "--solo" in args:
        solo = args[args.index("--solo") + 1:]
    elenca = "--lista" in args

    os.makedirs(DIR, exist_ok=True)
    reg_path = os.path.join(DIR, "crediti.json")
    registro = {}
    if os.path.exists(reg_path):
        try:
            registro = json.load(open(reg_path, encoding="utf-8"))
        except Exception:
            registro = {}

    ok = falliti = 0
    for pid, cfg in IMPIANTI.items():
        if solo and pid not in solo:
            continue
        print(f"\n=== {pid}  ({cfg['nome']})")

        scelto = ripiego = None
        # 1) il file già individuato, se ancora esiste ed è abbastanza grande
        if cfg.get("file"):
            ii = info_file(cfg["file"])
            if not ii:
                print("    file noto non più disponibile, passo alla ricerca")
            elif ii.get("width", 0) < LARGH_MIN:
                # anche il file già indicato a mano deve reggere la larghezza di
                # visualizzazione; se la ricerca non trova di meglio si torna qui
                print(f"    file noto troppo piccolo ({ii.get('width')} px), cerco di meglio")
                ripiego = (cfg["file"], ii)
            else:
                scelto = (cfg["file"], ii)
                print("    file noto trovato")
        # 2) altrimenti cerco
        if not scelto:
            for q in cfg["query"]:
                cand = [(valuta(t, ii), t, ii) for t, ii in cerca(q)]
                cand = [c for c in cand if c[0] > 0]
                cand.sort(reverse=True, key=lambda c: c[0])
                if cand:
                    _, t, ii = cand[0]
                    scelto = (t.replace("File:", ""), ii)
                    print(f"    trovato cercando «{q}»")
                    if elenca:
                        for s, tt, _ in cand[:5]:
                            print(f"       {s:6.0f}  {tt}")
                    break
        if not scelto and ripiego:
            scelto = ripiego
            print("    niente di meglio: tengo il file noto")
        if not scelto:
            print("    NESSUNA immagine libera trovata")
            falliti += 1
            continue

        titolo, ii = scelto
        autore, lic = crediti(ii)
        print(f"    {titolo}")
        print(f"    {autore} — {lic}")

        if elenca:
            continue

        # Special:FilePath restituisce sempre un JPEG (converte anche i TIFF, che
        # il browser non mostrerebbe) e non viene limitato con 429 come l'URL
        # diretto delle miniature su upload.wikimedia.org
        url = ("https://commons.wikimedia.org/wiki/Special:FilePath/" +
               urllib.parse.quote(titolo.replace(" ", "_")) + "?width=1400")
        dest = os.path.join(DIR, pid + ".jpg")
        try:
            kb = scarica(url, dest) // 1024
            print(f"    salvato in {dest}  ({kb} KB)")
        except Exception as e:
            print(f"    ERRORE nel download: {e}")
            falliti += 1
            continue

        registro[pid] = {
            "autore": autore,
            "licenza": lic,
            "scheda": "https://commons.wikimedia.org/wiki/File:" +
                      urllib.parse.quote(titolo.replace(" ", "_")),
            "analogo": cfg.get("analogo", ""),
        }
        ok += 1

    if not elenca:
        json.dump(registro, open(reg_path, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        # versione .js: il sito la legge anche aperto con un doppio clic
        with open(os.path.join(DIR, "crediti.js"), "w", encoding="utf-8") as f:
            f.write("window.CREDITI_LOCALI = " +
                    json.dumps(registro, ensure_ascii=False, indent=1) + ";\n")
        print(f"\n---------------------------------------------")
        print(f"immagini pronte: {ok}    non riuscite: {falliti}")
        print(f"crediti scritti in {reg_path} e in {DIR}/crediti.js")
        print("Apri nucleapp.html: le didascalie si compilano da sole.")


if __name__ == "__main__":
    main()
