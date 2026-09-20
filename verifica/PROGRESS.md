# Stato del lavoro

> Questo file è la memoria del progetto. Va aggiornato a ogni sessione, prima
> che il contesto si accorci. Se riparti da zero, leggi README.md e poi questo.

Ultimo aggiornamento: 2026-09-19 (sessione 14)

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
- **Da fare in questa richiesta**: gli incidenti (TMI, Chernobyl,
  Fukushima).

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

0. **Prima di pubblicare** (verificato il 2026-09-19): attivare GitHub Pages
   (Settings → Pages → `main`, `/`) — l'indirizzo dà 404; togliere
   `pubblica/index.html`, obsoleto; aggiungere descrizione per i motori di
   ricerca, anteprima social, icona, licenza. Nessuno è ancora fatto.
1. **Interfaccia grafica delle centrali**: FATTO per tutte e 9 le centrali →
   dettaglio in `sessione 5`–`13` qui sopra. Restano solo i punti "da
   riverificare" e "indicativi" elencati in ogni sessione, e due
   cose sulle schede: potenza netta di Beloyarsk 4 (820 contro 789 MW) e data
   del test di perdita del raffreddamento di Shidaowan (2023 o 2024).
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
