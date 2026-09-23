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
| 7 | HTR-PM | fumetto del nocciolo | "Non ci sono barre né assemblaggi: 400 000 sfere di grafite …" e "Ogni sfera contiene 12 000 granelli" | "Niente assemblaggi di combustibile: un cilindro alto circa 11 m e largo 3 m riempito di sfere …" e "circa 12 000 granelli" | le barre di regolazione ci sono: scorrono nei canali del riflettore laterale (24), non tra le sfere; il numero dei granelli varia da sfera a sfera (10 000–20 000 secondo GRS, 12 000 secondo POWER) |
| 8 | Beloyarsk 4 | disegno e fumetto del sito | torre di raffreddamento (da 95 m), fumetto: "Qui una torre di raffreddamento disperde nell'aria il calore dei condensatori" | raffreddamento a circuito aperto sul bacino (presa e scarico, senza torre) | nessuna fonte descrive una torre per il BN-600 o il BN-800 in esercizio: entrambi usano il bacino di Beloyarsk; la pagina Wikipedia sul BN-1200 (futuro, non costruito) presenta le torri evaporative come una novità rispetto a quei due impianti |
| 9 | Shidaowan | `worst.precedente` | "Nel 2024 il test è stato fatto sul serio: … su entrambi i reattori in funzione" | "Nel 2023 … ad agosto sul primo reattore e a settembre sul secondo … a un modulo alla volta" | il test (Joule, luglio 2024; POWER) fu eseguito nel 2023, in due prove separate, una per modulo, non insieme |
| 10 | WIPP | barriera "Isolamento idrogeologico" | "Nessuna falda sfruttabile sopra il deposito e nessun percorso rapido verso la superficie" | cita la Culebra per nome e la definisce non potabile (10 000–200 000 mg/l di sali), invece di negare l'esistenza di una falda | la Culebra è una falda reale, riconosciuta dallo stesso WIPP come possibile via di trasporto in caso di intrusione umana; è la sua salinità, non la sua assenza, a escluderla come fonte d'acqua |
| 11 | Deposito Nazionale | scheda "Cosa contiene" | "≈ 78 000 m³ di rifiuti" — "ma il 99 % è materiale a bassa attività" (non fontato) | "≈ 84 000 m³" (Sogin, 2024), con la scomposizione 49 000 + 35 000 m³ per origine | Sogin ha aggiornato la stima; il vecchio 78 000 m³ era quella del progetto preliminare del 2021 (ora citata come tale); il "99 %" non aveva una fonte e non tornava con la definizione stessa dell'84 000 m³ (già "sola bassa e bassissima attività") |
| 12 | Deposito Nazionale | scheda "Alta attività" | "Non va qui" | "In un'area separata, non nel deposito" | il Parco Tecnologico ha un complesso di stoccaggio (CSA, ≈ 14 000 m³) per i rifiuti a media e alta attività: non è vero che quei rifiuti non hanno alcun posto nel Parco, solo che non vanno nel deposito di superficie |
| 13 | Chernobyl | passo 5 del racconto | "la potenza supera di decine di volte il valore nominale" | "la potenza supera di molte volte il valore nominale — le stime vanno da circa dieci volte a molto di più" | 30 000 MW stimati su 3 200 nominali è circa 10×, non "decine di volte" (che implica ≥ 20×); le ricostruzioni disponibili divergono, e il fumetto del pulsante AZ-5 lo dice già |
| 14 | Fukushima | passo 4 del racconto | "guaine di zirconio, esposte al vapore a oltre 1 000 °C" | "oltre 1 200 °C" | Wikipedia (e la scheda tecnica dell'HTR-PM nello stesso sito) danno 1 200 °C come soglia della reazione zirconio-vapore |
| 15 | Fukushima | passo 6 del racconto | "Oltre 150 000 persone vengono allontanate" | "Oltre 100 000 persone … fino a circa 164 000 al picco" | World Nuclear Association dà "oltre 100 000", Wikipedia "164 000 al picco"; nessuna fonte trovata dà 150 000 |

Correzione 7 (2026-09-19, sessione 13, con il ridisegno di Shidaowan): il testo
precedente stava nella riga `fumetti:{nocciolo:…}` della scheda `htrpm` in
`index.html`; ora c'è anche un fumetto proprio per le barre.

Correzioni 8–15 (2026-09-24, sessione 16): richieste esplicitamente
dall'utente, una alla volta, a partire dai punti lasciati aperti nelle
sessioni precedenti (12–15). Dettaglio:
- **Beloyarsk (8)** è l'unica che tocca il disegno, non solo il testo: nel
  sito la torre è stata tolta e sostituita da una presa e uno scarico nel
  bacino, sullo stesso modello già usato per Darlington (lago Ontario). È
  cambiato anche il campo `scena.raffreddamento` di `bn800`, da `'torre'` a
  `'lago'`: comandava anche il contenuto dell'approfondimento "doppio click"
  sul pallino del raffreddamento, che prima descriveva ancora una torre
  evaporativa inesistente.
- **WIPP (10)**: aggiornato anche il fumetto `culebra` del disegno del sito,
  che già nominava la Culebra ma non ne diceva la salinità.
- **Deposito Nazionale (11, 12)**: la scheda ora riporta due numeri (84 000 e
  78 000) con l'anno di ciascuno, invece di un solo numero senza data —
  come richiesto dalla regola sui dati numerici in `CLAUDE.md`.
- Beloyarsk (8) e Shidaowan (9) erano già segnalate come indicative/da
  riverificare in `verifica/PROGRESS.md` (sessioni 12 e 13); WIPP, Deposito
  Nazionale, Chernobyl e Fukushima (10–15) in sessioni 14–15.

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
