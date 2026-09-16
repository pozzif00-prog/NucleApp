# Stato del lavoro

> Questo file è la memoria del progetto. Va aggiornato a ogni sessione, prima
> che il contesto si accorci. Se riparti da zero, leggi README.md e poi questo.

Ultimo aggiornamento: 2026-08-02 (seconda sessione)

## Fatto — sessione 2

- **Approfondimenti**: 41 schede tecniche a tendina, agganciate a 90 punti del
  sito, ciascuna con la riga "Per saperne di più" e link verificati.
  Dettaglio, criteri e verifiche di merito → `approfondimenti.md`
- **67 link controllati uno per uno**: tutti rispondono 200
- **Layout incidenti rifatto**: disegno e racconto affiancati su una schermata,
  "Conseguenze e cambiamenti" spostate in una fascia sotto, che si raggiunge
  scorrendo
- 3 correzioni di merito emerse dalla riverifica (WIPP 21 lavoratori non 22;
  fattori di capacità italiani; confronto eolico) → `approfondimenti.md`

## Fatto — sessione 3

- **Testi tagliati corretti**: `.eyebrow`, `.r-sub`, `.r-nome` andavano a capo
  mai, dentro una barra laterale a larghezza fissa con `overflow:hidden`
- **Controllo completo** su tagli e sovrapposizioni in tutte e tre le sezioni:
  ora zero. Nessuna etichetta SVG fuori tela, nessuna sovrapposizione
- **Conseguenze e cambiamenti** (incidenti): da elenco a colonna singola a
  griglia di schede affiancate, che riempie la fascia invece di lasciarla vuota
- **Fonte in ogni approfondimento** (395 tendine) e sotto ogni elenco di dati
  → dettaglio e criterio di onestà in `approfondimenti.md`

## Fatto — sessione 4

- **Avviso dello scram**: era un riquadro sovrapposto al centro della scena e
  copriva l'impianto. Ora la scena è a due colonne (`.scena-conavviso`):
  il disegno a sinistra in `.scena-wrap`, l'avviso nella colonna accanto.
  Affiancare invece di sovrapporre è l'unico modo per garantire che non copra
  mai nulla **anche con zoom e spostamento attivi**, dove qualunque posizione
  fissa prima o poi finisce sopra l'impianto.
- Il fumetto è stato spostato dentro `.scena-wrap`, perché `mostraFumetto`
  calcola le coordinate da `scena.parentElement`. Se si tocca quella struttura,
  ricordarsi di questo accoppiamento.
- Sotto i 900 px la colonna passa sotto il disegno invece che accanto.

## Fatto — sessione 1

- Architettura definita → `README.md`
- Registro fonti → `fonti.yaml` (6 fonti)
- **Tutti e 9 i reattori verificati** sulle voci di "SCHEDA DELL'IMPIANTO"
  - `affermazioni/sizewell-b.yaml` (primo prototipo, formato esteso)
  - `affermazioni/reattori.yaml` (gli altri 8)
  - **63 affermazioni controllate: 48 confermate, 9 corrette, 6 lasciate con riserva**
- **11 correzioni applicate a nucleapp.html** → registrate in `CORREZIONI.md`
  con il valore precedente, per poterle annullare
- Sito riverificato dopo le modifiche: 9 reattori, depositi e incidenti
  funzionano, nessun errore in console

## Da fare, in ordine

1. **Depositi** (onkalo, wipp, italia) — 6 voci ciascuno: profondità, roccia,
   capacità, date, orizzonte di progetto. Fonti: Posiva (Onkalo), DOE/WIPP,
   ISIN/Sogin (Deposito Nazionale).
2. **Incidenti** — le fonti ci sono già (UNSCEAR, IAEA, Kemeny). Serve
   scomporre le affermazioni e agganciare locator + citazione testuale.
   Attenzione: il bilancio di Chernobyl è `conteso`, va rappresentato come
   ventaglio con la ragione metodologica, non come numero unico.
3. **Scheda "tech"** di ogni reattore (refrigerante, moderatore, combustibile,
   contenimento) — sono affermazioni qualitative da manuale, rischio basso,
   priorità bassa.
4. **Riagganciare IAEA PRIS (T1)** e alzare il livello delle fonti.
5. Solo dopo: espansione con letteratura peer-reviewed sui punti contesi.

## Aperto / bloccato

- **IAEA PRIS (T1) non raggiungibile**: `ReactorDetails.aspx` fa 302 verso
  `pris-stats.iaea.org`, che non espone le schede per reattore. Tutti i dati
  di targa poggiano quindi su World Nuclear Association (T2, derivata da PRIS).
- **Fattori di capacità**: verificato solo Sizewell B, e su fonte T4
  (associazione di categoria). Gli altri 8 impianti non espongono il dato
  nella scheda, quindi non è un problema aperto sul sito — lo diventerebbe
  se lo si volesse aggiungere.
- **Darlington, definizione di "in esercizio dal"**: decisione redazionale
  in sospeso, vedi `CORREZIONI.md`.

## Trappole già incontrate

- Nel database WNA la voce **"Shidaowan 1" NON è l'HTR-PM**: è un Hualong One
  in costruzione dal 2024 sullo stesso sito. Per l'HTR-PM serve World Nuclear News.
- Il **rendimento** non è mai un dato di fonte: si ricava da netto/termico.
  Va confrontato con la potenza che il sito stesso dichiara — se il sito
  espone la potenza lorda, il rendimento va calcolato sul lordo (caso Chernobyl).
- I **superlativi** ("il più potente al mondo") sono il tipo di affermazione
  che invecchia peggio e va sempre ricontrollato contro un concorrente.

## Convenzioni da non dimenticare

- Nessuna citazione testuale → nessuna pubblicazione.
- Un'affermazione `numerico` senza **definizione** non è verificabile.
- Le fonti T4 non confermano mai un fatto da sole.
