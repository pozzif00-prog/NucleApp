# Stato del lavoro

> Questo file è la memoria del progetto. Va aggiornato a ogni sessione, prima
> che il contesto si accorci. Se riparti da zero, leggi README.md e poi questo.

Ultimo aggiornamento: 2026-09-24 (sessione 18: scorrimento contro zoom + verifica
depositi/incidenti a tre larghezze, vedi sotto)

## Fatto — sessione 18b (verifica di depositi e incidenti a tre larghezze)

Richiesta dell'utente: ricontrollare depositi e incidenti (non solo centrali)
alle tre larghezze (telefono 375 px, tablet 768 px, desktop 1200 px), dopo la
correzione scorrimento/zoom della sessione 18. Nel farlo, trovato e corretto
un difetto piccolo ma reale:

- **`#lato-sfondo`** (lo sfondo scuro dietro al pannello a comparsa
  dell'elenco) non aveva un `display:none` di base **fuori** dal media query
  sotto i 900 px: sopra i 900 px restava `display:block` di default (nessuna
  regola CSS lo copriva a quella larghezza), invece di `none`. Nella pratica
  non si vedeva — l'elemento è vuoto e senza `position:fixed` fuori dal media
  query, quindi occupa zero spazio — ma non era dichiarato invisibile "per
  davvero", solo per un caso fortunato. Aggiunta la regola di base
  `#lato-sfondo{display:none}` fuori dal media query, e tolto il `display:none`
  ormai ridondante dentro.

**Verificato** (depositi e incidenti, non solo centrali) a tutte e tre le
larghezze: `touch-action:pan-y`, rotellina senza/con Ctrl, pizzico a due dita,
tocco a un dito che non sposta nulla, fumetti, cambio passo (solo incidenti),
apertura/chiusura del pannello con chiusura automatica alla scelta (solo
depositi, che ha l'aside — incidenti non ne ha e il tasto ☰ lì resta senza
effetto, come previsto). Nessun errore in console in nessun caso. Confermato
anche con screenshot reali a 768 e 375 px (pannello che si apre sopra il
contenuto con lo sfondo scuro; disegni di depositi e incidenti leggibili e
ben impaginati).

**Trappola aggiuntiva, stessa famiglia di quelle di sessione 17–18**:
`getBoundingClientRect().left`, letto da JavaScript subito dopo aver aperto
il pannello a comparsa, può dare la posizione VECCHIA (fuori schermo) anche
a transizione conclusa — lo stesso difetto già visto con `getComputedStyle`
+ `transform`, dato che `getBoundingClientRect` lo usa internamente. Confermato
con uno screenshot reale, nello stesso istante: il pannello era aperto
correttamente. Vale la stessa regola di sessione 17: per lo stato visivo di
un cambio legato a `transform`, fidarsi dello screenshot, non della lettura
JavaScript della posizione.

## Fatto — sessione 18 (distinguere lo scorrimento dal tentativo di zoom)

Richiesta dell'utente, di seguito alla sessione 17: lo scorrimento della
pagina si interrompeva scorrendo sulle parti interattive (i disegni), perché
il sito lo interpretava come un tentativo di zoom. Causa, per due percorsi
distinti:
- **Al tocco**: le tre scene avevano `touch-action:none`, che blocca ogni
  gesto nativo del browser (incluso lo scorrimento verticale) appena un dito
  tocca il disegno; il trascinamento con un dito veniva sempre interpretato
  come "sposta il disegno", senza distinzione da "scorri la pagina".
- **A rotellina/trackpad**: il gestore dell'evento `wheel` chiamava sempre
  `e.preventDefault()` e zoomava, qualunque fosse la sorgente — anche un
  normale scorrimento a due dita sul trackpad, senza alcun pizzico.

Corretto per tutte e tre le scene (centrali, depositi, incidenti):
- `touch-action:none` → `touch-action:pan-y`: un dito che scorre in
  verticale ora scorre la pagina, nativamente, senza passare dal
  JavaScript — non può più "restare intrappolato" nel disegno.
- Il trascinamento con un dito (nel gestore `pointerdown` di ciascuna scena)
  ora è riservato al mouse (`e.pointerType==='touch'` esce subito): il tocco
  a un dito solo non sposta più il disegno.
- Nuova funzione condivisa **`attaccaPizzico`**: pizzicare con due dita
  ingrandisce (o rimpicciolisce) il disegno, centrato sul punto medio delle
  due dita, e muovendo insieme le due dita lo si sposta — lo stesso gesto di
  Google Maps o di qualunque visualizzatore di mappe. Due dita non si
  confondono mai con lo scorrimento a un dito, per definizione.
- Il gestore della rotellina (`wheel`) ora zooma solo se `e.ctrlKey` è vero:
  è lo stesso segnale che ogni browser manda per un vero pizzico sul
  trackpad (anche senza che l'utente tocchi il tasto Ctrl), e lo stesso
  trucco usato da Google Maps ("usa Ctrl + rotellina per ingrandire") per
  risolvere esattamente questo problema. Senza Ctrl, l'evento non viene più
  intercettato: lo scorrimento passa alla pagina.
- I tasti +/− e "vista intera" restano invariati: chi non conosce il
  pizzico o il Ctrl+rotellina ha sempre un modo visibile per zoomare.

**Verificato**, non con eventi finti generici ma con veri `TouchEvent`
(pizzico che allontana le dita → ingrandisce; che le avvicina → rimpicciolisce;
due dita che si spostano insieme, a distanza costante → sposta il disegno) e
`WheelEvent` con e senza `ctrlKey`, su tutte le 9 centrali, i 3 depositi e i
3 incidenti: nessun errore in console, il trascinamento col mouse (desktop)
resta identico a prima, il tocco a un dito non muove più nulla.

**Trappole incontrate in questa sessione, per non riscoprirle**:
- Il messaggio di console `<svg> attribute viewBox: Expected number, "NaN
  NaN …"` è un artefatto: il log della console resta legato alla SCHEDA del
  browser attraverso più `navigate()`, non alla pagina. Su una scheda
  **nuova**, appena aperta, non compare. Non è un errore del sito (già
  annotato in sessione 16, riconfermato qui).
- `requestAnimationFrame` — usato dall'animazione dei pulsanti di zoom
  (incluso "vista intera") — **non parte affatto** in questo ambiente di
  test quando la scheda non è quella attiva agli occhi del sistema
  operativo, anche se lo strumento la segna come "in primo piano". Per
  testare un cambio di VIEW dopo un pulsante che anima, o si aspetta molto
  più a lungo del dovuto, o (meglio) si impone lo stato finale a mano
  (`VIEW.x=...; applicaView();`) e si verifica quello, ignorando
  l'animazione in sé. Non è un problema del sito: gli utenti reali vedono
  l'animazione normalmente.
- Testare un pizzico a due dita con `elementFromPoint`/coordinate calcolate
  a mano è inutile: le coordinate riportate dagli screenshot di questo
  strumento non corrispondono in modo affidabile ai pixel CSS della pagina
  (visto già in sessione 17). Per il pizzico, meglio costruire `Touch` e
  `TouchEvent` veri e leggere lo stato risultante (`zoom`, `VIEW`) via
  JavaScript, senza passare da coordinate sullo schermo.

## Fatto — sessione 17 (sito utilizzabile da mobile)

Richiesta dell'utente, lasciata in lavorazione durante la notte (non
disponibile per rispondere a domande: nessuna necessaria, i due problemi
avevano una causa individuabile dal codice). Due problemi segnalati:

1. **Il doppio click/tocco per approfondire non funzionava da telefono.**
   Causa reale, trovata testando con tocchi veri (non con eventi simulati
   via JS, che l'avevano nascosta): il doppio click nativo (`dblclick`) non
   è affidabile al tocco, ed era l'UNICO meccanismo usato (oltre ai tasti
   freccia da tastiera). Risolto sostituendolo con un riconoscimento manuale
   di due "click" ravvicinati (funziona identico con mouse e dito, perché
   ogni tocco reale genera comunque un evento "click"). **Ma c'è una seconda
   causa, più subdola**: appena il primo tocco apre il fumetto, questo spesso
   **copre proprio il pallino** (confermato con `elementFromPoint`) — quindi
   il secondo tocco nello stesso punto arriva al fumetto, non al pallino
   sottostante, e andrebbe perso. Per questo il riconoscimento del doppio
   tocco è stato spostato dentro `mostraFumetto()` stesso (punto d'ingresso
   comune), con un tocco sul corpo del fumetto già aperto che vale come
   secondo tocco sul pallino che l'ha aperto. Riguarda solo le centrali
   (`apriMicro`/`MICRO_CHIAVI`): depositi e incidenti non hanno questo
   secondo livello di approfondimento.
   - Verificato rigorosamente: non bastava un test con eventi simulati
     (bypassano il vero posizionamento sullo schermo, dando un falso
     positivo). Verificato invece componendo due prove indipendenti ma
     concrete — (a) `elementFromPoint` nel punto esatto del pallino, dopo il
     primo tocco, per vedere davvero cosa ci sta sopra; (b) l'evento
     dispatchato su QUELL'elemento vero (pallino o fumetto, a seconda del
     caso) per vedere se apre l'approfondimento. Su tutte le 9 centrali e
     tutti i loro pallini "doppio tocco", nessun errore in console.
2. **Sotto i 900 px (mobile, tablet, finestra del browser stretta) l'elenco
   laterale (aside) compariva incollato in cima alla pagina, sopra la scheda
   dell'impianto**, invece di stare in un menu. Causa: `.griglia{grid-
   template-columns:1fr}` sotto i 900 px faceva impilare aside e main in
   ordine di documento (aside prima), invece di nascondere l'aside per
   davvero. Risolto trasformando l'aside, sotto i 900 px, in un **pannello a
   comparsa** (`position:fixed`, nascosto di default con `transform:
   translateX(-100%)`), con uno sfondo scuro dietro (`#lato-sfondo`, nuovo
   elemento nell'HTML, subito dopo l'header) che si tocca per chiudere. È
   lo stesso tasto ☰ (`#toggle-lato`) di sempre: la classe che comandava già
   la colonna laterale su desktop (`lato-chiuso`) ora, sotto i 900 px,
   comanda il pannello a comparsa — con il significato pratico invertito
   (assente = chiuso anche sotto i 900 px, comportamento di partenza; con la
   classe = aperto). Il pannello si chiude anche da solo scegliendo una
   centrale, un deposito, o cambiando scheda dalla barra in alto
   (`chiudiLatoMobile()`, richiamata da `selezionaReattore`,
   `selezionaDeposito` e dal click sulla barra di navigazione).
   - Verificato con screenshot reali (non solo con letture di stato via
     JavaScript: vedi la trappola qui sotto) a 375 px (telefono), 768 px
     (tablet), 850 px (finestra desktop stretta) e 1200 px (desktop pieno):
     pannello chiuso di default sotto i 900 px, si apre sopra il contenuto
     con lo sfondo scuro, si chiude toccando lo sfondo o scegliendo una voce;
     sopra i 900 px il comportamento di prima (colonna fissa, comprimibile
     col tasto ☰) è rimasto identico. Nessun errore in console su tutte le
     9 centrali, i 3 depositi e i 3 incidenti.
   - **Non toccato**: la sezione Incidenti non ha un `aside`/`griglia` (ha
     una lista orizzontale in alto, `.inc-lista`): il tasto ☰ lì non ha
     nessun effetto visibile, come già prima. Non è uno dei problemi
     segnalati e non l'ho cambiato.

**Trappola per la prossima sessione**: in questo ambiente di test,
`getComputedStyle(...).transform`, letto da JavaScript subito dopo aver
cambiato una classe che attiva una `transition` su `transform`, può
restituire il valore VECCHIO anche a transizione ampiamente conclusa (anche
con un valore forzato via `style.setProperty(...,'important')`, che
dovrebbe vincere su qualunque regola del foglio di stile) — mentre uno
screenshot reale, nello stesso istante, mostra il risultato GIUSTO. Non è un
bug del sito: è una particolarità di come questo strumento legge lo stile
calcolato tramite l'automazione del browser. **Per verificare l'effetto
visivo di un cambio di classe legato a `transform`/`transition`, fidarsi
dello screenshot, non di `getComputedStyle` letto da JavaScript.**

## Fatto — sessione 16 (licenza e correzioni segnalate nelle sessioni 12–15)

Richiesta esplicita dell'utente: "fai sia la licenza che le correzioni tutte
in fila". Fatto tutto in `index.html`, verificato nel browser (nessun errore
in console, tutte le centrali/depositi/incidenti si disegnano), poi
registrato in `CORREZIONI.md` (correzioni 8–15) e qui.

- **Licenza aggiunta**: `LICENSE.md` — MIT per il codice, CC BY 4.0 per testi
  e disegni, le foto in `img/` restano con le loro licenze originali
  (rimando a `crediti.json`). Il nome del titolare del copyright nel testo
  MIT è generico ("Autrici e autori del progetto NucleApp"): da sostituire
  con un nome vero o quello del comitato, se si vuole. README aggiornato con
  un rimando.
- **Beloyarsk 4 (correzione 8, l'unica che tocca un disegno)**: cercata una
  fonte sulla torre di raffreddamento del sito e non trovata; trovato invece,
  cercando il BN-1200 futuro, che le torri evaporative sono presentate come
  una *novità* rispetto al BN-600 e al BN-800 in esercizio, che usano il
  bacino. Tolta la torre dal disegno del sito, sostituita con una presa e
  uno scarico nel bacino (circuito aperto, come Darlington sul lago
  Ontario); aggiornati il fumetto del raffreddamento e il campo
  `scena.raffreddamento` (da `'torre'` a `'lago'`, usato anche
  dall'approfondimento "doppio click"). *In compenso*, la potenza netta
  (820 MW) è risultata confermata: il database di World Nuclear Association,
  oggi, dà proprio 820 MW netti — il valore di 789 MW che avevo segnalato
  come discrepante veniva da POWER (T4) e sembra superato. Nessuna modifica
  alla scheda.
- **Shidaowan (correzione 9)**: il test di sicurezza è del 2023 (non 2024),
  e sono state due prove separate, una per modulo (agosto e settembre),
  non una prova unica su entrambi insieme. Corretto `worst.precedente`.
- **WIPP (correzione 10)**: la barriera "Isolamento idrogeologico" negava
  l'esistenza di una falda sopra il deposito; la falda (Culebra) esiste
  davvero ed è riconosciuta dallo stesso WIPP come possibile via di
  trasporto — è la sua salinità (10 000–200 000 mg/l) a escluderla come
  fonte d'acqua, non la sua assenza. Corretti il testo della barriera e il
  fumetto `culebra` del disegno.
- **Deposito Nazionale (correzioni 11 e 12)**: il volume è stato aggiornato
  a ≈ 84 000 m³ (Sogin, 2024; era ≈ 78 000 m³ nel progetto preliminare del
  2021 — ora citato con la sua data, invece di un numero solo), con la
  scomposizione per origine (49 000 dalle centrali, 35 000 da ricerca e
  medicina); tolto il "99 % bassa attività" senza fonte. La riga "Alta
  attività: Non va qui" diceva una mezza verità: il Parco ha un complesso
  di stoccaggio temporaneo (CSA, ≈ 14 000 m³) per quei rifiuti — diventata
  "In un'area separata, non nel deposito".
- **Chernobyl (correzione 13)**: "la potenza supera di decine di volte il
  valore nominale" (passo 5) implicava ≥ 20×; il rapporto tra la stima
  (≈ 30 000 MW) e il nominale (3 200 MW) è ≈ 10×. Ammorbidito a "molte
  volte", con la nota che le stime vanno da circa dieci volte in su.
- **Fukushima (correzioni 14 e 15)**: la temperatura della reazione
  zirconio-vapore era "oltre 1 000 °C" nel passo 4, corretta a 1 200 °C
  (coerente con la fonte usata altrove nello stesso sito, per l'HTR-PM);
  gli evacuati erano "oltre 150 000" nel passo 6, valore che non trovo in
  nessuna fonte — corretto a "oltre 100 000 … fino a circa 164 000 al
  picco" (World Nuclear Association e Wikipedia).
- **Non toccato**: il fumetto generico dell'incidente (`disegnaIncidente`,
  ramo `if(s.evacuazione)`) ha ancora "150 000" in una riga di testo, ma è
  codice morto — nessuno dei tre incidenti lo usa più (hanno tutti un
  disegno dedicato). Segnalato di nuovo qui sotto tra il codice da rimuovere.
  L'"incidente 2014" del WIPP dice "restò chiuso tre anni": dal 14 febbraio
  2014 a gennaio 2017 sono quasi tre anni (2 anni e 11 mesi): arrotondamento
  ragionevole, non l'ho toccato.

## Fatto — sessione 14 (depositi e incidenti: grafica come per le centrali)

Nuova richiesta dell'utente: ridisegnare anche la grafica dei **depositi**
(Onkalo, WIPP, Deposito Nazionale) e degli **incidenti** (TMI, Chernobyl,
Fukushima) nello stesso modo delle centrali: un disegno dedicato e fedele per
ciascuno, elementi appoggiati e non sospesi, ogni elemento spiegato da un
pallino numerato con fumetto o da un suggerimento al passaggio del mouse.
Si procede un elemento alla volta, mostrando il risultato.

- **Infrastruttura dei depositi** (una volta per tutte): la scena ha ora
  l'altezza che le serve (aspect-ratio dal disegno), zoom e trascinamento con
  pulsanti sotto il disegno, livelli di dettaglio come nelle centrali, e ogni
  deposito può avere una propria funzione di disegno registrata in
  `DEP_DISEGNI`; chi non ce l'ha usa `disegnaDepositoGenerico` (il vecchio
  disegno). I pallini delle barriere si chiamano `b0`…`b4` e prendono il testo
  da `barriere` della scheda, così il testo resta uno solo; gli altri pallini
  prendono il testo da `fumetti` del deposito. I numeri dei pallini delle
  barriere coincidono con "Barriera n" nella tendina sotto il disegno.
- **Onkalo: fatto.** Tre fasce. (1) la superficie in scala reale (2,6 px/m):
  impianto di incapsulamento, testa del pozzo dei contenitori, pozzo del
  personale, camini di ventilazione, ingresso della rampa, mare e conifere
  solo sulla terra; (2) la sezione in scala (0,72 px/m) con la profondità vera
  e la **rampa a spirale con pendenza 1:10 alla sua lunghezza vera** (22 tratti
  in fila, ≈ 4 km), quattro pozzi verticali, il livello del deposito a
  400–430 m, scala di profondità con la Torre Eiffel a 330 m, zone di frattura
  evitate; (3) dentro una galleria di deposito in scala (30 px/m): tre buche
  (8 m, Ø 1,75 m) con contenitore e bentonite, galleria riempita di blocchi,
  tappo, quote, e il contenitore in sezione trasversale (12 canali). 11 pallini.
  - Fonti: Posiva ("How ONKALO works", "Disposal canister", "Deposition
    holes"); INIS/OSTI ("ONKALO – Main drawings in 2007"); Tunnels &
    Tunnelling; Wikipedia ("Onkalo…", "KBS-3"). Quattro pozzi (personale,
    contenitori, due di ventilazione), 6 500 tU in ≈ 3 250 contenitori, rampa
    1:10, deposito a 400–430 m, buca ≈ 8 m e Ø 1,75 m, contenitore Ø 1,05 m,
    4,75 m, 24,5 t, rame 5 cm, 12 elementi, > 20 t di bentonite per buca,
    30–40 buche per galleria, prima galleria ≈ 330 m.
  - **Indicativi**: dimensioni e posizioni degli edifici di superficie;
    posizione della rampa rispetto ai pozzi; la disposizione delle gallerie di
    deposito (disegnate di taglio); le zone di frattura (d'esempio); il
    tappo di calcestruzzo e il riempimento a blocchi; la disposizione dei 12
    canali; la lunghezza della rampa (fonti: da 4,2 km nelle prime fasi a
    5,6 km).
  - **Da allineare nella scheda**: la profondità "≈ 430 m" è coerente con
    Posiva (deposito a 400–430 m, livello di caratterizzazione a 420 m), ma
    Wikipedia dà 520 m come profondità finale del complesso (livello
    inferiore). Va scelta la definizione e indicata. "Gneiss granitico" è una
    semplificazione (Posiva parla di gneiss migmatitico).
  - Verificato nel browser: nessun errore in console, 11 pallini con fumetto
    giusto, zoom e trascinamento, WIPP e Italia funzionano ancora col disegno
    generico.
- **WIPP: fatto.** Stessa struttura di Onkalo. (1) La superficie nel deserto
  in scala reale: camion con i contenitori di trasporto, edificio di
  movimentazione, torre del pozzo dei rifiuti, pozzi dell'aria e del sale,
  cumulo del sale scavato, segnali permanenti, arbusti (niente alberi in
  acqua né acqua). (2) La sezione in scala (0,72 px/m), a 950 m: coperture,
  Rustler con la Culebra, Salado (sale) con i suoi strati di anidrite, Castile
  con le sacche di salamoia, quattro pozzi, il livello a 655 m con due sale
  viste per il lungo, scala di profondità e "due Torri Eiffel". (3) Dentro una
  sala in scala (18 px/m): a sinistra appena riempita (pile di confezioni da
  sette fusti in tre strati, scatole standard, sacchi di ossido di magnesio),
  a destra dopo decenni, con il sale che si è chiuso attorno ai fusti; riquadro
  con il fusto in sezione e la confezione da sette vista dall'alto. 12 pallini.
  - Fonti: DOE e EPA (655 m = 2 150 piedi, quattro pozzi, pozzo grande da 20
    piedi con ascensore da 45 t, otto pannelli da sette sale di 13 x 33 x 300
    piedi, tredici siti di provenienza); Wikipedia ("Waste Isolation Pilot
    Plant"); appendice MgO della domanda di certificazione del DOE (sacchi da
    3 000–4 200 libbre sopra i contenitori); NRC e Beauheim/Holt (Culebra
    spessa 7–8 m, sopra il deposito; Castile con sacche di salamoia circa 200
    m sotto il livello del deposito); rapporti sull'incidente del 14 febbraio
    2014 (sala 7 del pannello 7, fusto con nitrati, assorbente organico e
    agente neutralizzante; nessun superamento dei limiti di dose).
  - **Indicativi**: le quote delle formazioni sopra i 655 m e sotto (Rustler
    100–235 m, Culebra a 200 m, Salado fino a 855 m) — le ho ricavate da
    memoria e da un solo dato di fonte ("Castile 200 m sotto il deposito"); la
    posizione dei pozzi tra loro; edifici, cumulo, camion e segnali; la
    disposizione dei fusti, delle confezioni da sette e delle scatole; **i
    tempi e il grado di chiusura della sala** ("dopo decenni" viene dalla
    scheda, non da una fonte); il numero di segnali permanenti (non
    specificato).
  - **Da verificare nella scheda**: la barriera "Isolamento idrogeologico"
    dice "nessuna falda sfruttabile sopra il deposito", ma sopra c'è la
    Culebra, che è una falda; serve una fonte sulla qualità dell'acqua o
    una riformulazione. La scheda dice "Il deposito restò chiuso tre anni":
    il rilascio è del 14 febbraio 2014 e la riapertura di gennaio 2017 (quasi
    tre anni).
  - Verificato nel browser: nessun errore in console, 12 pallini con fumetto
    giusto, zoom e trascinamento.
- **Deposito Nazionale: fatto.** Due fasce (il sito non c'è ancora: il
  paesaggio è d'esempio e lo dichiara). (1) In scala reale (2,6 px/m): una fila
  di sette delle 90 celle dentro la collina artificiale con i suoi strati, la
  platea, il terreno (suolo, argille compatte) e la falda molto più in basso;
  edificio di ricezione e controllo, complesso di stoccaggio ad alta attività,
  Parco Tecnologico, centro abitato lontano, cipressi. (2) Dentro una cella in
  scala (18 px/m): 27 x 10 m con 32 moduli di 3 x 1,7 m, quote, persona di
  1,8 m; riquadri del modulo e del manufatto (contenitore metallico con i
  rifiuti nel cemento). 9 pallini: 5 barriere, cella, complesso ad alta
  attività, Parco Tecnologico, sito da scegliere.
  - Fonti: Sogin e Ministero, tramite Wikipedia ("Deposito nazionale dei
    rifiuti radioattivi") e ANSA Verified (marzo 2023): 90 celle in
    calcestruzzo armato di 27 x 15,5 x 10 m, moduli di calcestruzzo di
    3 x 2 x 1,7 m con i manufatti, matrice cementizia, coperchio del modulo,
    collina artificiale con vegetazione, oltre 300 anni, 150 ettari (110 il
    deposito, 40 il Parco Tecnologico), complesso di stoccaggio ad alta
    attività temporaneo; MASE (localizzazione, D.Lgs. 31/2010, Sogin).
    Le pagine di Sogin e di depositonazionale.it non si aprono da qui (errore
    di certificato): niente è stato letto direttamente dal progetto
    preliminare.
  - **Indicativi**: la disposizione delle celle nella collina (una fila di
    sette), gli **strati della copertura e i loro spessori** (vegetazione e
    terreno, drenante, impermeabile: inventati sul modello di una discarica,
    la fonte dice solo "inerti e impermeabili"), lo spessore di pareti e
    soletta (1 m), il numero di manufatti per modulo, la platea, gli edifici,
    il paesaggio, la profondità della falda.
  - **Discrepanze da sistemare nella scheda**: i volumi. La scheda dice
    "≈ 78 000 m³" (come ANSA e il progetto preliminare del 2021), ma Sogin ora
    scrive circa 84 000 m³ di rifiuti a bassissima e bassa attività e circa
    14 000 m³ di media e alta attività nel complesso di stoccaggio (contro
    17 000 m³ prima); Wikipedia riporta 75 000 e 15 000. Va scelta una fonte e
    una data. La scheda dice anche "il 99 % è materiale a bassa attività" senza
    fonte, e "alta attività: non va qui", che è vero per il deposito ma
    non per il complesso di stoccaggio temporaneo dello stesso parco: nella
    riga "Alta attività" conviene spiegare la differenza. Non toccato.
  - Verificato nel browser: nessun errore in console, 9 pallini con fumetto
    giusto, zoom e trascinamento.
- **Depositi: finiti tutti e 3.** `disegnaDepositoGenerico` non è più usato
  da nessuno (codice morto, come le funzioni generiche delle centrali).
- **Infrastruttura degli incidenti** (una volta per tutte): ogni incidente può
  avere il suo disegno, registrato in `INC_DISEGNI` con la sua vista e una
  funzione `disegna(g,s,passo,inc)` che restituisce i pallini; i testi dei
  pallini stanno in `fumetti` dell'incidente, mostrati nel fumetto dentro la
  scena (`#fumetto-inc`); ogni passo può avere un campo `ora` con l'orario.
  Chi non ha un disegno proprio usa il vecchio disegno generico (Chernobyl e
  Fukushima, per ora).
- **Three Mile Island: fatto.** Sezione del contenimento di un reattore ad
  acqua in pressione con un solo circuito (il disegno lo dichiara): recipiente
  con nocciolo, barre, coperchio e meccanismi; generatore di vapore;
  pressurizzatore con valvola di blocco e valvola di sfogo (PORV); pompa di
  circolazione; serbatoio di scarico con il disco che si rompe; pozzetto e
  acqua sul pavimento; iniezione di emergenza (serbatoio d'acqua borata fuori
  dal contenimento, pompa, tubo); alimento principale fermo e alimento di
  emergenza con le valvole chiuse; sala turbine; pannello **"sala di
  controllo: cosa vedono gli operatori"** con la spia (spenta, ma la valvola è
  aperta), il livello alto nel pressurizzatore e il livello nel recipiente
  che nessuno strumento misura. I sei passi cambiano: livello dell'acqua nel
  recipiente e nel pressurizzatore, stato del nocciolo (intatto, scoperto,
  fuso sul fondo), barre, valvole, pompe ferme o in moto, iniezione in
  funzione o ridotta, acqua sul pavimento, contenimento evidenziato all'ultimo
  passo. 10 pallini con fumetto.
  - Fonti: World Nuclear Association ("Three Mile Island Accident"); Wikipedia
    ("Three Mile Island accident"): 4:00 del 28 marzo 1979, arresto del
    reattore, PORV aperta a 2 255 psi che non si richiude, spia che segue il
    comando, due valvole dell'alimento di emergenza chiuse, ≈ 32 000 galloni
    (≈ 120 m³) di refrigerante persi, livello del pressurizzatore che sale,
    disco del serbatoio di scarico rotto alle 4:15, pompe che vibrano dopo
    ≈ 80 minuti, valvola di blocco chiusa alle 6:22, almeno il 45 % del nocciolo
    fuso (≈ 62 t) e ≈ 19 t sul fondo, combustione di idrogeno verso le 13:50
    con + 28 psi, contenimento integro; PORV già guasta 11 volte in altri
    impianti e caso simile a Davis-Besse 18 mesi prima (risolto in 20
    minuti). La pagina dell'NRC dava 403.
  - **Da riverificare**: il tipo dei generatori di vapore (a passaggio unico,
    Babcock & Wilcox) e "quattro pompe, due per generatore" sono dalla mia
    memoria, non da una fonte letta; le valvole dell'alimento di emergenza
    chiuse "per i primi minuti" (la fonte dice solo che erano chiuse; dalla
    memoria: circa 8 minuti); l'arresto "dopo 8 secondi" (Wikipedia) contro
    "circa un secondo" (WNA): nel disegno e nel fumetto ho scritto "pochi
    secondi"; che l'acqua del serbatoio di scarico sia stata poi pompata in
    un edificio ausiliario (dalla memoria: non scritto); la dose media
    (0,08 mSv entro 16 km per WNA, 1,4 mrem = 0,014 mSv per Wikipedia).
  - **Indicativi**: forma e quote di tutti i componenti, posizione dei tubi,
    livelli dell'acqua nei sei passi, tempi dei passi intermedi.
  - **Da sistemare nella scheda**: `esiti` dice "Nessun effetto sanitario ...
    rilevato": coerente con WNA; le tre fonti danno dosi diverse, va scelta
    una definizione.
  - Verificato nel browser: nessun errore in console, sei passi, 10 fumetti,
    Chernobyl e Fukushima funzionano ancora col disegno generico.
- **Chernobyl: fatto.** Di notte, come nella realtà. Sezione dell'edificio
  dell'unità 4: nocciolo di grafite con 16 canali disegnati (ne ha 1 661) e
  combustibile, barre con la punta di grafite in chiaro e il tratto d'acqua
  sotto, piastra superiore, sala del reattore con la macchina di carico,
  separatori di vapore ai lati, pompe, vasche di soppressione sotto il piano
  di campagna, sala turbine con la turbina che gira per inerzia fino al passo
  4, e il pannello **"sala di controllo"** con la potenza, le barre in campo,
  il test e il pulsante **AZ-5** (che si abbassa al passo 4). I sei passi
  cambiano: barre estratte o in ingresso, bolle di vapore nei canali,
  bagliore blu e poi arancio, all'esplosione la piastra sollevata e inclinata,
  la sala squarciata, il nocciolo sventrato, il fuoco, i detriti a terra, e
  all'ultimo passo il pennacchio con la piastra ricaduta di sbieco. 9 pallini
  con fumetto.
  - Fonti: World Nuclear Association ("Chernobyl Accident": 3 200 MW termici,
    1 000 MW elettrici, nocciolo ≈ 7 x 12 m, 211 barre, piastra da 1 000 t,
    coefficiente di vuoto positivo, punte di grafite, 28 morti per sindrome
    acuta) e Wikipedia ("Chernobyl disaster": 1 661 canali, test della turbina
    con 5,5 MW per ≈ 45 s, cronologia dal 25 aprile 01:06 al 26 aprile 01:23:40,
    ≈ 30 MW alle 00:05, 160 MW alle 00:39, due pompe in più alle 01:05, minimo
    di 15 barre, oltre 530 MW, ≈ 30 000 MW, seconda esplosione 2–3 s dopo,
    incendio fino al 10 maggio, sarcofago dicembre 1986, New Safe
    Confinement 2016–2018).
  - **Da riverificare**: la piastra "ricaduta di sbieco sopra il reattore
    aperto" (dalla memoria); le vasche di soppressione come protezione
    parziale contro la rottura di tubi (dalla memoria); la macchina di carico
    nella sala; la "seconda esplosione" come esplosione di idrogeno o di
    altra natura (le fonti divergono: WNA dice "probabilmente idrogeno",
    Wikipedia non decide).
  - **Indicativi**: forma e quote dell'edificio, disposizione di separatori,
    pompe, tubi e vasche, quanti canali e barre si disegnano, il tetto, la
    posizione dei detriti.
  - **Discrepanze da sistemare nella scheda**: il passo 5 dice "la potenza
    supera di decine di volte il valore nominale"; con ≈ 30 000 MW su
    3 200 MW nominali si tratta di circa dieci volte (Wikipedia). Le stime
    variano (il fumetto lo dice) e il testo del passo va reso coerente:
    proposta "di molte volte". Non toccato. La grafite di WNA (1 200 t) e la
    piastra (1 000 t) contro altre fonti (grafite ≈ 1 700 t, piastra ≈ 2 000
    t) non entrano nel disegno.
  - Verificato nel browser: nessun errore in console, sei passi, 9 pallini con
    fumetto giusto; TMI e Fukushima funzionano.
- **Fukushima Daiichi: fatto.** Sezione di un'unità con contenimento Mark I:
  a sinistra il mare con la diga, le altezze di riferimento (5,7 m di progetto,
  10 m di quota del sito, 15 m dell'onda) e le pompe dell'acqua di mare sulla
  riva; l'edificio turbina con nel seminterrato diesel, quadri e batterie;
  l'edificio del reattore con recipiente, nocciolo, barre inserite dal basso,
  bolla d'acciaio (drywell), camera di soppressione ad anello, piscina del
  combustibile esaurito e piano di servizio con telaio e copertura leggeri; un
  pannello "alimentazione e raffreddamento" con quattro spie (rete, diesel,
  batterie, pompe). I sei passi cambiano: l'onda che sale a 15 m e allaga il
  sito e i seminterrati (che restano allagati dopo), il livello dell'acqua nel
  recipiente, il nocciolo (intatto, caldo, scoperto e fuso), la piscina che
  bolle, l'idrogeno che sale dal contenimento al piano di servizio, poi
  l'esplosione con macerie e fumo e infine una mappa dell'evacuazione con gli
  ordini a 2, 3, 10 e 20 km. 8 pallini con fumetto.
  - Fonti: World Nuclear Association ("Fukushima Daiichi Accident") e
    Wikipedia ("Fukushima Daiichi nuclear disaster"): sei BWR General Electric
    con Mark I, unità 1–3 in funzione; 14:46, magnitudo 9,0; onda tra 15:27 e
    15:35 (≈ 41 minuti), ≈ 15 m contro 5,7 m di progetto, sito a 10 m;
    diesel, quadri e batterie nei seminterrati degli edifici turbina;
    12 generatori su 13 fuori uso (WNA; Wikipedia dice "10 su 13 sistemi di
    raffreddamento dei diesel"); batterie da ≈ 8 ore; unità 1: acqua alla
    sommità del combustibile dopo ≈ 3 h, danni dopo ≈ 4 h; unità 3 e 2: ≈ 42
    e ≈ 74 h; esplosioni: unità 1 alle 15:36 del 12 marzo, unità 3 alle 11:01
    del 14, unità 4 il 15 con idrogeno dall'unità 3; piscina dell'unità 4
    con 1 331 + 548 elementi, combustibile tolto a dicembre 2014; ordini di
    evacuazione a 2 km (20:50), 3 (21:23), 10 (05:44 del 12), 20 (18:25); oltre
    100 000 persone e fino a 164 000 al picco; 51 morti per l'evacuazione e
    2 313 "correlati al disastro" (90 % oltre i 66 anni); nessun morto acuto
    da radiazioni.
  - **Da riverificare**: le pompe dell'acqua di mare "sulla riva, più in basso
    del sito" (dalla memoria); la diga alta come l'onda di progetto; "molti
    sistemi non comandabili senza corrente" (Wikipedia dice solo che il
    condensatore di isolamento dell'unità 1 si guastò per le valvole
    chiuse alla perdita della corrente continua).
  - **Indicativi**: forma e quote dei componenti, posizione di diga e prese,
    livelli dell'acqua nei sei passi, tempi intermedi, un solo edificio.
  - **Discrepanze da sistemare nella scheda**: il passo 4 dice "a oltre
    1 000 °C" mentre Wikipedia dà "oltre 1 200 °C" per la reazione
    zirconio-vapore (non riportato nel fumetto); il passo 6 dice "oltre
    150 000 persone", la WNA "oltre 100 000", Wikipedia "164 000 al picco";
    lo "screening" della tiroide e "oltre cinquanta pazienti" (Wikipedia: 51
    morti per l'evacuazione, in generale) vanno ricondotti a una fonte e a una
    definizione.
  - Verificato nel browser: nessun errore in console, sei passi, 8 pallini
    con fumetto (l'ottavo, l'evacuazione, compare all'ultimo passo);
    TMI e Chernobyl funzionano.
- **Incidenti: finiti tutti e 3.** Il disegno generico degli incidenti (in
  `disegnaIncidente`, dopo l'`if(D)`) non è più usato da nessuno: codice
  morto, come `sitoGenerico`, `isolaGenerica` e `disegnaDepositoGenerico`. Si
  possono togliere tutti insieme, ma serve un giro di verifica.
- **La richiesta "depositi e incidenti come le centrali" è completa.**

## Fatto — sessione 13

- **Shidaowan (HTR-PM): nono e ultimo disegno dedicato.** Con questo tutte le
  9 centrali hanno sito e spaccato propri; `sitoGenerico` e `isolaGenerica`
  restano in `index.html` come ripiego ma nessuna centrale li usa più (codice
  morto: si possono togliere).
  - La foto `img/htrpm.jpg` è un'**immagine radar satellitare** del sito
    (Umbra, giugno 2023, cantiere di Shidaowan), vista dall'alto: mostra costa,
    dighe di massi, terreno pianeggiante, ma non l'aspetto degli edifici.
  - Sito: vista dal mare (Mar Giallo) con la diga frangiflutti, i **due
    edifici reattore affiancati** ("reattore 1" e "reattore 2", il primo
    evidenziato e collegato allo spaccato), il deposito del combustibile
    esaurito, la sala turbine (una sola per i due moduli), trasformatore e
    traliccio, e sullo sfondo, schiarito, il cantiere di un'unità Hualong One
    con la gru. Presa d'acqua di mare a sinistra dietro la diga, scarico a
    destra: nessun albero in acqua, nessun traliccio in acqua.
  - Spaccato di un modulo: **due recipienti separati e affiancati** — reattore
    (alto ≈ 25 m) e generatore di vapore — uniti dal **condotto coassiale**,
    con la **soffiante sopra il generatore**. Il nocciolo è disegnato alle
    misure vere (Ø 3 m, alto 11 m: lungo e stretto) con le sfere ingrandite,
    cono di scarico in basso, riflettore di grafite attorno, camera dell'elio
    caldo sotto. Le **barre di regolazione stanno nel riflettore laterale**, non
    nel letto (SCRAM verificato: le barre scendono e finiscono sull'altezza del
    nocciolo). Elio freddo in oro, caldo in arancio, con il giro completo.
    Sotto il recipiente: scarico e misura delle sfere, ricircolo pneumatico in
    cima, uscita verso il deposito. Ai lati della cavità del reattore i
    **pannelli d'acqua del raffreddamento passivo**, collegati a una torre ad
    aria sul tetto. Niente cupola: l'edificio è a parete di cemento, come
    "contenimento funzionale" (la barriera è il granello TRISO).
  - 4 pallini nuovi con fumetto (sfere, condotto coassiale, soffiante,
    raffreddamento passivo) più testi propri per nocciolo, barre, generatore
    di vapore e acqua di mare: **11 pallini in tutto**.
  - Fonti: 2 moduli da 250 MW termici e una turbina da 210 MW elettrici
    (Wikipedia, "HTR-PM"; World Nuclear News); elio 250/750 °C; generatore di
    vapore a tubi elicoidali, vapore ≈ 13 MPa e 566 °C (POWER "Nuclear
    Milestone: China's HTR-PM"; articoli tecnici); recipiente ≈ 25 m e ≈ 700 t
    (WNN, "Key components of second HTR-PM reactor connected"); reattore e
    generatore in due recipienti separati, condotto concentrico, soffiante
    sulla sommità del generatore, "contenimento funzionale" invece di un
    edificio a tenuta (GRS, "The pebble bed reactor at the Shidaowan nuclear
    power plant"); scarico dal fondo, ricircolo, un deposito per i due
    reattori, ≈ 15 passaggi per sfera (articoli tecnici, POWER); raffreddamento
    dal Mar Giallo (Wikipedia, "Shidao Bay Nuclear Power Plant"); RCCS passivo
    a pannelli d'acqua con "torre ad aria" (articoli tecnici sull'RCCS
    dell'HTR-PM).
  - **Da riverificare sul testo originale** (arrivano da sintesi di ricerca,
    non da una lettura diretta): nocciolo Ø 3 m e alto 11 m, **24 barre di
    regolazione nel riflettore laterale** e sistema di arresto a sferette
    assorbenti (sei canali), elio a ≈ 7 MPa. Le due pagine con più dettagli
    (Engineering 2016, MDPI RCCS) davano 403 e non le ho lette.
  - **Indicativi**: tutte le quote interne (altezze e posizioni di recipienti,
    cavità, camera calda, pannelli, gru); l'altezza dell'edificio (33 m), la sua
    larghezza (38 m) e l'assenza di cupola, non trovate su una fonte; **il
    percorso interno dell'elio nel generatore** (caldo su nel tubo centrale e
    giù sul fascio, freddo su nell'intercapedine, discesa dalla soffiante
    sull'altro lato); **l'elio caldo al centro del condotto e il freddo
    nell'intercapedine** (disposizione consueta, non verificata); la
    **posizione della torre ad aria sul tetto** e del deposito del combustibile
    esaurito; la diga; il cantiere Hualong One (cilindro basso e gru).
  - **Discrepanza da sistemare nella scheda**: `worst.precedente` dice "Nel 2024
    il test è stato fatto sul serio"; POWER data il test a metà 2023 (annunciato
    e pubblicato nel 2024). Va scelta la data giusta e indicata. Non toccato.
  - Corretto il fumetto del nocciolo, che diceva "Non ci sono barre": vedi
    correzione 7 in `CORREZIONI.md`.
  - Verificato nel browser: nessun errore in console, 9 centrali su 9 si
    disegnano, SCRAM e tutti gli 11 fumetti funzionano, doppio click su un
    pallino nuovo non dà errori.

## Fatto — sessione 12

- **Beloyarsk 4 (BN-800): ottavo disegno dedicato**, stesso metodo. La foto
  `img/bn800.jpg` è la **sala di controllo** (con la mappa circolare del
  nocciolo sul pannello): nessun dettaglio esterno, quindi sito e
  spaccato vengono dai dati dell'impianto.
  - Sito: bacino di Beloyarsk in primo piano, conifere della taiga (solo
    sulla terra), il BN-600 schiarito a sinistra, l'edificio del reattore
    con accanto l'**edificio dei generatori di vapore e sul tetto i tre
    camini degli scambiatori aria-sodio**, sala turbine, torre di
    raffreddamento a destra (in scala), presa di reintegro dal bacino.
  - Spaccato: la **vasca di sodio** di un reattore a piscina — recipiente
    principale e recipiente di sicurezza attorno, argon sopra il livello del
    sodio, sodio freddo e barile del sodio caldo, nocciolo in basso,
    raccoglitore del nocciolo fuso sotto, colonna delle barre con **barre che
    scendono lungo guide fisse** (verificato: le barre coprono l'altezza del
    nocciolo), scambiatori intermedi e pompe primarie immersi nella vasca
    con il motore sul coperchio a tappi girevoli — e fuori, in due edifici
    laterali, il **sodio intermedio non radioattivo** che porta il calore ai
    generatori di vapore, con il ramo verso gli scambiatori aria-sodio sul
    tetto. Tre circuiti visibili in fila: sodio primario, sodio
    intermedio, acqua e vapore.
  - 3 pallini nuovi con fumetto (scambiatore intermedio, pompa primaria,
    scambiatori aria-sodio nel sito) e testi specifici per generatore di
    vapore, nocciolo, barre e raffreddamento.
  - Fonti: potenza 2 100 MW termici; tre circuiti (sodio primario e
    secondario, acqua e vapore); ogni circuito con una pompa primaria, due
    scambiatori intermedi, una pompa secondaria e un generatore; tre barre
    assorbenti sospese idraulicamente nel flusso; scambiatori aria-sodio su
    ogni circuito secondario; raccoglitore del nocciolo fuso (POWER, "Top
    Plant: Beloyarsk Unit 4"; Wikipedia, "BN-800 reactor"); tipo a
    piscina, recipiente a pressione appena sopra quella atmosferica; circa
    565 elementi di combustibile (World Nuclear News); bacino di Beloyarsk
    creato nel 1959–1963 (Wikipedia, "Beloyarsk Nuclear Power Station").
  - **Indicativi, non verificati**: il diametro e l'altezza del recipiente e
    del recipiente di sicurezza (non trovati); la posizione del raccoglitore
    del nocciolo fuso dentro il recipiente; le dimensioni del nocciolo,
    riprese dal BN-600 "molto simile" (≈ 1 m x 2 m) e disegnate
    **ingrandite** per leggibilità — il titolo del pannello lo dichiara;
    la disposizione di scambiatori e pompe (uno per lato, non due
    scambiatori per circuito); le altezze degli edifici. **La torre di
    raffreddamento** viene dalla scheda originale ("torre" nella
    configurazione della scena), non verificata su una fonte: il fumetto
    "Acqua del bacino di Beloyarsk" (riga ~842 di `index.html`) dice
    però che "qui una torre di raffreddamento disperde nell'aria il calore
    dei condensatori", cioè lo afferma — da controllare prima di
    pubblicare, o da attenuare.
  - **Da allineare nella scheda**: la potenza netta dichiarata è ≈ 820 MW
    (Wikipedia); POWER dà 789 MW netti e 864 lordi. Il numero giusto dipende
    dalla definizione: va scelta una fonte di riferimento e indicata.
  - Una ricerca diceva che "la stazione non ha un edificio di
    contenimento": non ho trovato conferma su una fonte migliore e non
    l'ho scritto né disegnato come tale; il disegno mostra un edificio
    reattore in cemento senza specificarne la funzione di contenimento.
    `scena.contenimento:true` nella scheda originale resta com'è.

## Fatto — sessione 11

- **Sanmen 1 (AP1000): settimo disegno dedicato**, stesso metodo. La foto
  `img/ap1000.jpg` mostra il **cantiere** (edifici bianchi e grigi, gru a
  torre, il contenimento dell'unità 1 in costruzione sullo sfondo), non
  l'impianto finito: la forma viene dal progetto AP1000, dalla foto solo
  il colore della sala turbine (bianca con una fascia scura).
  - Sito: lo schermo in cemento con il tetto conico, il **grande serbatoio
    d'acqua ad anello con il camino centrale dell'aria in cima**, le prese
    d'aria, l'edificio ausiliario addossato, la sala turbine, Sanmen 2
    schiarito a destra, mare con presa e scarico. Nessuna torre di
    raffreddamento.
  - Spaccato: schermo in cemento e guscio d'acciaio con **cupola ellittica**,
    l'intercapedine con il **flusso d'aria** che sale per tiraggio naturale
    (dalle prese, giù lungo la parete, su lungo il guscio, fino al camino),
    la pellicola d'acqua sulla cupola con i tubi di scarico dal serbatoio,
    la **vasca d'acqua in contenimento (IRWST)** con lo scambiatore
    passivo a fascio di tubi a C, due serbatoi di compensazione e due
    accumulatori con azoto, due generatori di vapore con le pompe
    agganciate al fondo, recipiente con meccanismi delle barre sul
    coperchio, barre che scendono lungo guide fisse (verificato: le barre
    coprono l'altezza del nocciolo), gru polare.
  - 3 pallini nuovi con fumetto (scambiatore passivo, guscio d'acciaio,
    serbatoio in quota — quest'ultimo nel sito, con `extra`) più testi
    specifici per nocciolo, generatore, pompa, raffreddamento.
  - Fonti: guscio d'acciaio Ø 39,6 m, alto 65,6 m, parete di 4,5 cm; schermo
    in cemento Ø 44,2 m, alto 83,4 m, parete di 0,9 m; 157 elementi di
    combustibile da 264 barrette, altezza attiva 4,27 m (Westinghouse, AP1000
    Design Control Document; NRC). Acqua di mare in passaggio unico dal
    canale di Shefan (Wikipedia, "Sanmen Nuclear Power Station"). Sistemi
    passivi: due CMT, due accumulatori, scambiatore passivo nella vasca
    interna (NRC). **Indicativi, non verificati**: il serbatoio in quota
    "circa 3 000 m³, per 72 ore" (da uno studio di ricerca, non dal DCD);
    la disposizione interna di IRWST, CMT, accumulatori e scambiatore; il
    diametro e l'altezza del recipiente; la forma del tetto conico e
    dell'anello del serbatoio; le altezze di edificio ausiliario e sala
    turbine; il ritorno dello scambiatore passivo al circuito primario,
    non disegnato; il tipo di turbina (una di alta e due di bassa
    pressione, generico).

## Fatto — sessione 10

- **Olkiluoto 3 (EPR): sesto disegno dedicato**, stesso metodo. Vista dalla
  baia, foto `img/epr.jpg` come riferimento.
  - Sito: cupola grigia di OL3 con gli edifici in mattone rosso e bianco
    davanti, camino di OL3, sala turbine lunga con **una turbina di alta
    pressione e tre di bassa** e alternatore, OL1 e OL2 schiariti a destra
    con i camini a spirale, acqua di mare in una sola passata con presa a
    destra e scarico a sinistra (nessuna torre di raffreddamento), massi
    lungo la sponda, canneti in primo piano.
  - Spaccato: **doppio guscio** con intercapedine (esterno in cemento armato,
    interno precompresso con rivestimento in acciaio), recipiente con i
    meccanismi delle barre sul coperchio, **barre che scendono dall'alto
    lungo guide fisse** (verificato: le barre coprono esattamente
    l'altezza del nocciolo), due dei quattro circuiti, pozzo del reattore e
    **core catcher** — canale di scarico con tappo sacrificale, camera di
    spargimento laterale con fondo raffreddato — vasca di ricarica IRWST,
    quattro edifici di salvaguardia ai lati, gru polare.
  - 2 pallini nuovi con fumetto (core catcher, doppio contenimento) più
    pompa e generatore con testo specifico; testo specifico anche per
    nocciolo, barre e raffreddamento.
  - Fonti: contenimento interno Ø 46,8 m, alto 57,5 m, parete di 1,3 m,
    doppio guscio con intercapedine in depressione, core catcher da 170 m²
    con elementi di raffreddamento in ghisa (Wikipedia, "EPR (nuclear
    reactor)" e letteratura sul contenimento EPR); 241 elementi di
    combustibile da 265 barrette, 89 meccanismi delle barre sul coperchio
    (NRC, U.S. EPR FSAR — è il progetto americano, uguale per questi dati);
    una turbina di alta e tre di bassa pressione (TVO, tvo.fi); acqua di
    mare ≈ 57 m³/s (TVO, via ricerca). **Indicativi, non verificati**: il
    diametro e l'altezza del recipiente (≈ 5 x 12 m), lo spessore
    dell'intercapedine (1,4 m, da cui il Ø esterno ≈ 55 m), la sala turbine
    (lunga ≈ 100 m e alta ≈ 33 m: una fonte diceva 60 m di altezza e
    larghezza, non convincente), le altezze di OL1, OL2, degli edifici in
    mattone e dei camini, dedotte dalla foto.
  - **Da allineare**: la scheda "tech" dice che il core catcher è "una vasca
    ceramica sotto il reattore"; nel disegno è una camera laterale di 170 m²
    raggiunta da un canale sotto il recipiente, come nel progetto reale. Il
    testo è vago più che sbagliato, ma vale la pena rivederlo.

## Fatto — sessione 9

- **Darlington (CANDU): quinto disegno dedicato**, stesso metodo. Vista dal
  lago Ontario, foto `img/candu.jpg` come riferimento.
  - **Verifica di merito prima di disegnare**: nei CANDU multi-unità come
    Darlington il **serbatoio di spruzzo (dousing) sta nell'edificio a
    vuoto**, non nell'edificio reattore. La prima idea del disegno lo metteva
    in cima al reattore: sbagliato, corretto prima di scrivere il codice
    (fonte: OPG, CNSC, IAEA). Lo spaccato mostra solo il condotto di sfogo
    che porta all'edificio a vuoto.
  - Sito: sala turbine bassa e lunga, edificio reattore in dettaglio (una
    sola unità gemella schiarita dietro), **edificio a vuoto** — cilindro
    con cupola bassa e antenna rossa e bianca — collegato dal condotto di
    sfogo, camini scuri, scogliera di massi lungo la riva, gallerie
    sotterranee della presa e dello scarico con diffusori, lago in primo
    piano. Nessuna torre di raffreddamento (coerente con la foto e con il
    testo già presente).
  - Spaccato: sezione longitudinale — calandria orizzontale con canali e
    fasci di combustibile (12 fasci per canale disegnati, 13 nella realtà),
    piastre tubiere, vasca di acqua leggera, **barre di arresto che cadono
    dall'alto lungo guide fisse** (verificato), circuito primario a otto con
    collettori caldo e freddo a ogni estremità, generatori di vapore e pompe
    a entrambi i lati, **macchine di ricarica agganciate ai due lati**,
    condotto di sfogo verso l'edificio a vuoto. Etichette in colonna a destra
    con linee guida, come Leibstadt.
  - 3 pallini nuovi con fumetto (pompa primaria, macchine di ricarica,
    edificio a vuoto) e testi specifici per calandria, barre, generatore di
    vapore e raffreddamento.
  - **Estensione al motore**: un sito può dichiarare pallini propri con
    `extra:{chiave:[x,y]}` nel valore restituito; `disegnaScena` li aggiunge.
    Serve per l'edificio a vuoto, che sta nel sito e non nello spaccato.
  - Fonti: 480 canali, 6 240 fasci, pareti degli edifici reattore in
    calcestruzzo di 1,8 m, un reattore e quattro generatori di vapore per
    edificio, edificio a vuoto alto 71 m e collegato da un condotto di sfogo
    (OPG, opg.com; CNSC, cnsc-ccsn.gc.ca; IAEA-INIS su Pickering A →
    Darlington). Calandria di un CANDU 6 ≈ 6,0 x 7,6 m con 380 canali
    (Wikipedia, "CANDU reactor"). **Indicativi, non verificati**: il
    diametro dell'edificio a vuoto (≈ 60 m) e l'altezza degli edifici
    reattore (≈ 50 m), dedotti dalla foto in proporzione ai 71 m; le
    dimensioni della calandria di Darlington (più grande di quella del
    CANDU 6); il numero di generatori e pompe disegnati (uno per lato,
    nella realtà i generatori sono quattro per edificio).

## Fatto — sessione 8

- **Leibstadt (BWR): quarto disegno dedicato**, stesso metodo. Vista dal
  Reno, foto `img/bwr.jpg` come riferimento.
  - **Correzione di merito**: il disegno generico rappresentava Leibstadt
    con raffreddamento a fiume; la centrale ha invece una **grande torre di
    raffreddamento** (144 m, Ø 120 m alla base), con il Reno usato solo per
    il reintegro (≈ 1 000 L/s, un millesimo della portata). `scena.raffreddamento`
    passa da `'fiume'` a `'torre'`. Nessuna affermazione del sito diceva il
    contrario (la scheda dice solo "sul Reno"), ma il disegno sì.
  - Sito: torre, cupola bianca con basamento basso, camino rosso e bianco
    di 99 m, sala macchine con turbogruppo, gallerie sotterranee dell'acqua
    verso la torre e presa di reintegro dal Reno, Reno in primo piano.
  - Spaccato: edificio in calcestruzzo (pareti 1,2 m) con cupola; dentro,
    il contenimento in acciaio (guscio 3,8 cm), il drywell in cemento, la
    **piscina di soppressione** attorno, recipiente in pressione con
    separatori e asciugatori sopra il nocciolo, **barre di controllo che
    partono a riposo sotto il nocciolo e lo SCRAM spinge in su** (verificato:
    `translateY(-33.3px)`, le barre attraversano il nocciolo), pompa di
    ricircolo, cavità e ponte di ricarica, gru polare, piscina del
    combustibile nell'edificio ausiliario. Etichette in una colonna a destra
    con linee guida — necessario perché dentro il drywell non c'è spazio.
  - 3 pallini nuovi con fumetto (pompa di ricircolo, piscina di
    soppressione, separatori e asciugatori) più nocciolo/barre; il fumetto
    delle barre e quello del raffreddamento hanno testo specifico.
  - Fonti: KKL (kkl.ch): torre 144 m e Ø 120 m, camino 99 m, pareti 1,2 m,
    recipiente 600 t con acciaio da 15 cm, 648 elementi di combustibile,
    prelievo dal Reno. Altezza dell'edificio 58,6 m: Wikipedia. **Da
    riverificare su fonte migliore**: recipiente ≈ 6 m x 22 m e piscina di
    soppressione ≈ 4 000 m³ (fonte secondaria, non l'operatore) — il
    diametro della cupola è dedotto dalla foto. Segnati come indicativi
    nel disegno.
  - Il PDF "Technical Description" di KKL contiene con ogni probabilità le
    quote ufficiali del contenimento, ma non si riesce a leggere da qui:
    manca poppler. Un controllo a mano vale la pena.
- **Bug corretto in Calder Hall**: le torri di raffreddamento erano
  asimmetriche (punto di controllo sbagliato sul lato destro del profilo).
  Ora c'è una funzione condivisa `profiloTorre()`, usata anche da Leibstadt.
- **Verificato che il sito online non esiste ancora**: l'indirizzo GitHub
  Pages risponde 404 (Pages non attivo). `pubblica/index.html` è obsoleto:
  non contiene nessuno dei disegni nuovi. Da sistemare prima della
  pubblicazione — vedi "Da fare".

## Fatto — sessione 7

- **Chernobyl (RBMK-1000): terzo disegno dedicato**, stesso metodo delle due
  centrali precedenti. La scheda rappresenta le unità 3–4 (scelta
  redazionale già presente, vedi `CORREZIONI.md`): il disegno mostra
  l'impianto come operava, non l'incidente — quello resta nella sezione
  "Incidenti", non toccata.
  - Sito in scala: fila di 4 edifici reattore (uno in dettaglio, gli altri
    tre schiariti), la ciminiera di ventilazione condivisa dalle unità 3-4
    — 150 m dal suolo, la struttura più alta di tutto il sito — sala
    turbine lunga condivisa da 4 reattori, bacino di raffreddamento
    artificiale alimentato dal fiume Pripyat, canneti sulla riva, pini al
    posto degli alberi delle altre centrali.
  - Isola nucleare: capannone in cemento (nessuna seconda barriera sopra il
    nocciolo — coerente con la scheda "tech"), cavità in cemento al posto
    di un recipiente unico, catasta di grafite con 14 canali verticali
    rappresentativi, **piano di manovra con i tappi dei canali** — il
    dettaglio più riconoscibile di un RBMK dall'interno, aggiunto dopo la
    prima bozza perché lo spazio sopra il nocciolo risultava troppo vuoto
    — due separatori di vapore (ciclo diretto, non uno scambiatore),
    macchina di ricarica su binari in alto.
  - 2 pallini con fumetto (separatore di vapore, macchina di ricarica) più
    nocciolo/barre. La scheda delle **barre di controllo ha un testo
    specifico per questo reattore**: spiega l'effetto delle punte in
    grafite (accelerano la reazione nei primi secondi) con un rimando al
    "Worst case" — lo stesso fatto già raccontato lì, solo riproposto nel
    punto dell'interfaccia dove un visitatore se lo chiederebbe. 8
    spiegazioni al passaggio del mouse sugli elementi strutturali.
  - Misure verificate: catasta di grafite Ø 11,8 m, alta 7 m, nocciolo
    attivo ≈ 12 x 7 m (World Nuclear Association, "RBMK Reactors"); camino
    di ventilazione condiviso 3-4, alto 75,5 m, cima a 150 m dal suolo
    (World Nuclear News, "Chernobyl ventilation stack removed"). Il bacino
    di raffreddamento (22,9 km², 11 x 2 km) viene da letteratura sulla sua
    dismissione, non da una fonte T1/T2 sola: valore indicativo delle
    dimensioni, non del sito nel suo insieme — da segnare come punto da
    riverificare se si vuole innalzare il livello della fonte. Le quote
    interne dello spaccato e la disposizione del circuito restano
    indicative, dichiarate nel titolo del pannello.
  - **Falso allarme durante la verifica**: un errore "viewBox NaN" nella
    console era un residuo della scheda del browser usata per i test
    precedenti (chiusa e riaperta una scheda pulita per controllare) — non
    un bug del codice. Utile da ricordare: un errore di rendering
    apparente può derivare dallo strumento di test, non dal sito; prima di
    correggere, riprodurlo in una scheda del browser nuova.
- Verificato dopo ogni modifica: le 9 centrali si disegnano senza errori in
  console (controllato anche su scheda pulita), lo SCRAM abbassa le barre
  su tutte e tre le centrali ridisegnate, i fumetti si aprono coi testi
  giusti.

## Fatto — sessione 6

- **Calder Hall: secondo disegno dedicato**, con lo stesso metodo usato per
  Sizewell B. Vista dalla campagna, foto `img/magnox.jpg` come riferimento.
  - Sito in scala: fila di 4 edifici reattore (il selezionato in dettaglio,
    gli altri tre schiariti, come Sizewell A per Sizewell B), due ciminiere
    di ventilazione coi filtri (il dettaglio che fermò l'incendio di
    Windscale nel 1957 — collegato al "worst case" già presente nella
    scheda), due torri di raffreddamento in coppia, fabbricato del
    combustibile, sala turbine piccola (macchina da ≈ 50 MW).
  - Isola nucleare: capannone industriale (non un contenimento a tenuta —
    coerente con la scheda "tech" che già lo diceva), schermo biologico in
    cemento, recipiente in acciaio saldato col nocciolo di grafite a canali
    verticali, due scambiatori di calore esterni (non annegati come nei
    PWR) con soffianti alla base, piano di carica con macchina di carica su
    binari, carroponte.
  - 2 pallini con fumetto (scambiatore di calore, soffiante) più i soliti
    nocciolo/barre. Tooltip al passaggio del mouse su: edificio reattore,
    schermo biologico, recipiente, piano di carica, carroponte, fabbricato
    del combustibile, camino di ventilazione.
  - Misure verificate: involucro in acciaio Ø 11 m, alto 21,5 m; nocciolo
    (prisma a 24 lati) ≈ 11 x 8 m; torri di raffreddamento ≈ 88-90 m, base
    di 60 m (ICE, scheda "Calder Hall"; Wikipedia, "Calder Hall nuclear
    power station"). Le quote interne dello spaccato e la disposizione del
    circuito del gas sono indicative, non verificate su fonte — il titolo
    del pannello lo dichiara, come per Sizewell.
  - **Bug trovato e corretto prima del commit**: le barre di controllo
    partivano già inserite nel nocciolo, invece di scendere allo SCRAM.
    Verificato che ora scendono correttamente (controllato lo stile
    `transform` e con uno zoom sul nocciolo dopo il clic).
- **Refactor**: il ciclo che crea i pallini in `disegnaScena` ora scorre
  `Object.entries(I.punti)` invece di elencare le chiavi a mano. Ogni nuova
  centrale può aggiungere i propri pallini (es. `soffiante` per Calder
  Hall) senza toccare `disegnaScena`.
- Verificato dopo ogni modifica: le 9 centrali si disegnano senza errori in
  console, lo SCRAM abbassa le barre sia per Sizewell sia per Calder Hall,
  i fumetti si aprono con i testi giusti.

## Fatto — sessione 5

- **Sizewell B: primo disegno dedicato**, non più lo schema generico condiviso
  da tutte le centrali. Vista da sud, foto `img/pwr.jpg` come riferimento.
  - Sito in scala: cupola e edifici come in foto, Sizewell A sullo sfondo
    schiarita, dune, spiaggia di ciottoli, Mare del Nord. Gallerie dell'acqua
    di mare (presa e scarico) sotto spiaggia e fondale, non più tralicci o
    alberi in acqua.
  - Sala turbine con spaccato: turbogruppo, condensatore e pompa di alimento
    appoggiati su tavola, piano interrato e piano terra come una sala vera,
    non elementi fluttuanti.
  - Isola nucleare: sezione verticale sotto il sito (prima era un taglio ×5
    slegato, in cima). Ogni componente appoggiato dove sta davvero — recipiente
    appeso ai bocchelli sullo schermo biologico, generatori di vapore su
    colonne, pompe primarie sul pavimento, pressurizzatore su gonna d'appoggio,
    gru polare sulle mensole — con le strutture (cemento, solette) in grigio
    tenue e i componenti in evidenza.
  - 2 nuovi pallini cliccabili con fumetto: pressurizzatore, pompa primaria.
    5 spiegazioni al passaggio del mouse per gli elementi strutturali:
    recipiente in pressione, schermo biologico, piano operativo, gru polare,
    edifici ausiliari.
  - Misure verificate: edificio reattore Ø 45 m, alto 65 m (ICE); presa
    dell'acqua di mare a ≈ 600 m dalla riva (Granta, "On Sizewell C"). Le
    quote interne dello spaccato sono indicative, non verificate su fonte:
    il titolo del pannello lo dichiara.
  - Colori: componenti in azzurro chiaro (`--ghiaccio`, riuso della palette
    del sito) invece di bianco — prima si confondevano con lo sfondo, quasi
    dello stesso bianco. Sfondo del pannello e "vuoto" interno del
    contenimento unificati in grigio chiarissimo (`#F1F2F4`), non più bianco.
  - Impaginazione cambiata per tutte le centrali: prima il sito intero, sotto
    lo spaccato dell'isola nucleare (prima erano invertiti). L'altezza del
    disegno ora dipende dalla centrale (`disegnaScena` imposta `BASE.h`), non
    più fissa a 700.
- **Le altre 8 centrali** usano ancora lo spaccato e il sito generici
  (`isolaGenerica`, `sitoGenerico`), con la sola correzione della posizione
  dell'etichetta "nocciolo". Da ridisegnare una per una con lo stesso metodo:
  foto reale → misure verificate → sito in scala → spaccato con componenti
  appoggiati, non fluttuanti.
- Verificato dopo ogni modifica: le 9 centrali si disegnano senza errori in
  console, lo SCRAM abbassa ancora le barre, i fumetti si aprono.

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

0. **Pubblicazione** (verificato il 2026-09-20): **il sito è online** su
   https://pozzif00-prog.github.io/NucleApp/ — GitHub Pages attivato
   dall'utente (`has_pages: true`), pagina e file (`og-image.png`,
   `favicon.svg`, foto in `img/`) rispondono 200, il file online è identico a
   quello del repository, nessun errore in console, disegni e fumetti
   funzionano. Fatti: tolto `pubblica/index.html`; aggiunti `meta
   description`, Open Graph e Twitter card, `favicon.svg`,
   `apple-touch-icon.png`, `og-image.png` (generati con PowerShell, script
   non conservato: si rifà con `System.Drawing`). **Licenza aggiunta**
   (sessione 16, `LICENSE.md`): MIT + CC BY 4.0, vedi sotto. **Tutto fatto.**
   Trappola: le foto hanno `loading="lazy"`, quindi nel browser di prova non
   risultano caricate finché non scorrono davvero in vista: non è un errore
   del sito.
1. **Interfaccia grafica delle centrali**: FATTO per tutte e 9 le centrali →
   dettaglio in `sessione 5`–`13` qui sopra. Restano solo i punti "da
   riverificare" e "indicativi" elencati in ogni sessione. Le due cose sulle
   schede segnalate qui (potenza netta di Beloyarsk 4, data del test di
   Shidaowan) sono state chiuse in sessione 16, vedi sopra e
   `CORREZIONI.md` (correzioni 8 e 9).
2. **Depositi** (onkalo, wipp, italia) — 6 voci ciascuno: profondità, roccia,
   capacità, date, orizzonte di progetto. Fonti: Posiva (Onkalo), DOE/WIPP,
   ISIN/Sogin (Deposito Nazionale).
3. **Incidenti** — le fonti ci sono già (UNSCEAR, IAEA, Kemeny). Serve
   scomporre le affermazioni e agganciare locator + citazione testuale.
   Attenzione: il bilancio di Chernobyl è `conteso`, va rappresentato come
   ventaglio con la ragione metodologica, non come numero unico.
4. **Scheda "tech"** di ogni reattore (refrigerante, moderatore, combustibile,
   contenimento) — sono affermazioni qualitative da manuale, rischio basso,
   priorità bassa.
5. **Riagganciare IAEA PRIS (T1)** e alzare il livello delle fonti.
6. Solo dopo: espansione con letteratura peer-reviewed sui punti contesi.

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
