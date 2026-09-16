# Correzioni applicate a nucleapp.html

Data: 2026-08-02 — fonte di riferimento: World Nuclear Association Reactor
Database (derivato da IAEA PRIS). Dettaglio e citazioni testuali in
`affermazioni/reattori.yaml` e `affermazioni/sizewell-b.yaml`.

Per annullare una correzione basta rimettere il valore della colonna "prima".

## Errori di fatto

| # | impianto | voce | prima | dopo | perché |
|---|---|---|---|---|---|
| 1 | Olkiluoto 3 | nota sulla potenza | "Il reattore più potente in esercizio al mondo" | "Uno dei reattori più potenti al mondo" | Taishan 1 e 2 hanno 1660 MWe netti contro 1575, e sono in esercizio dal 2018 |
| 2 | Chernobyl | avvio costruzione | 1972 (unità 1) | 1970 (unità 1) | fonte: 1 marzo 1970 |
| 3 | Darlington | avvio costruzione | 1981 | 1982 | fonte: 1 aprile 1982 |
| 4 | Sanmen 1 | potenza netta | ≈ 1 100 MW | ≈ 1 150 MW | fonte: 1157 MWe (scarto 5 %) |
| 5 | Olkiluoto 3 | potenza netta | 1 600 MW | ≈ 1 575 MW | era dichiarata come valore esatto |
| 6 | Sizewell B | fattore di capacità | ≈ 85–90 % | ≈ 84 % | lifetime load factor ≈ 84 %; aggiunta la definizione, che mancava |

Correzione 4: aggiornato anche il paragone, da "1,8 milioni di persone" a
"1,9 milioni".
Correzione 6: aggiornato anche il paragone, da "produce nove giorni su dieci"
a "l'equivalente di oltre otto giorni su dieci".

## Rendimenti ricalcolati

Il rendimento non è dichiarato dalle fonti: si ricava come
`potenza netta / potenza termica`. Nessuno era stato ricalcolato.

| impianto | prima | dopo | calcolo |
|---|---|---|---|
| Calder Hall | ≈ 20 % | ≈ 18 % | 49 / 268 |
| Sizewell B | ≈ 33 % | ≈ 35 % | 1198 / 3425 |
| Leibstadt | ≈ 33 % | ≈ 34 % | 1233 / 3600 |
| Darlington | ≈ 30 % | ≈ 32 % | 878 / 2776 |
| Sanmen 1 | ≈ 33 % | ≈ 34 % | 1157 / 3400 |

Aggiornati anche i due testi che contavano le unità di calore
(Calder Hall "solo 20 → 18", Sizewell B "33 e 67 → 35 e 65").

Confermati senza modifica: Chernobyl ≈ 31 % (coerente col valore lordo che il
sito dichiara), Olkiluoto 3 ≈ 37 %, Beloyarsk 4 ≈ 39 % (esatto),
HTR-PM ≈ 40 % (calcolo 42 %, lasciato perché "circa" regge e servirebbe una
fonte di progetto).

## Non toccato di proposito

- **Darlington, "In esercizio dal 1990"** — 1990 è il primo collegamento alla
  rete, l'esercizio commerciale è del 1992. Lasciato perché con 1990 il tempo
  di costruzione dichiarato resta coerente. Serve una decisione redazionale:
  quale delle due date usare in tutto il sito.
- **Chernobyl, scheda intitolata "unità 3–4" con le date dell'unità 1** —
  è una scelta narrativa, non un errore di dato.
- **Beloyarsk 4** — scheda confermata per intero, nessuna correzione.
