# Approfondimenti — contenuto, criteri, verifica

Data: 2026-08-02

## Cosa sono

Un blocco a tendina ("Approfondisci") in coda ai parametri che, spiegati in due
righe, restano superficiali. Dentro si usa il lessico tecnico per esteso, e in
fondo c'è una riga "Per saperne di più:" con i link.

**41 approfondimenti** definiti, agganciati a 90 punti del sito
(reattori, depositi, passi degli incidenti).

## Come sono agganciati

Non sono scritti dentro i dati. Stanno in una libreria (`APPRO`) e vengono
associati per **etichetta del parametro**, con la possibilità di specializzare
per impianto (`APPRO_MAP`). Vantaggi: un concetto ricorrente — moderatore,
rendimento, contenimento — si scrive una volta sola, e i dati restano puliti.

Per gli incidenti la chiave è `<id incidente>.<numero passo>` (`APPRO_INC`).

Per aggiungerne uno: si scrive la voce in `APPRO`, si aggiunge il link in `L`,
e si mappa l'etichetta in `APPRO_MAP`. Nessuna modifica ai dati.

## Criterio di selezione

Solo dove l'approfondimento aggiunge qualcosa. Non sono stati messi su:
- parametri autoesplicativi (Posizione, Avvio costruzione, In esercizio dal);
- valori già spiegati adeguatamente dalla riga di paragone esistente.

## Link: come sono stati verificati

**Tutti i 67 URL di approfondimento sono stati interrogati uno per uno e
rispondono 200.** Verifica ripetuta a fine lavoro sul file finale.

Fonti scelte, in ordine di preferenza:
1. enti (UNSCEAR, Posiva, Sogin/Deposito Nazionale, ISIN, OECD-NEA, IAEA PRIS);
2. World Nuclear Association, information library;
3. Wikipedia italiana, per i concetti dove esiste una voce solida;
4. Wikipedia inglese, dove quella italiana manca o è troppo scarna
   (TRISO, letto di sfere, core catcher, KBS-3, sicurezza passiva).

**Non sono stati usati** i link al glossario della NRC e alle pagine tematiche
della IAEA: rispondono 403 a qualunque accesso programmatico, quindi non ho
potuto verificarli. Regola applicata: nessun link non verificato in pagina.

Attenzione per il futuro: i titoli di Wikipedia cambiano con i redirect. Le
voci usate sono state risolte via API alla data di oggi — per esempio
"Moderatore di neutroni" reindirizza a "Moderatore (fisica)", "Barre di
controllo" a "Barre di moderazione". In pagina sono stati messi i titoli finali.

## Verifiche di merito fatte sul testo scritto

| affermazione | esito |
|---|---|
| WIPP 2014: assorbente organico, reazione esotermica, americio e plutonio | confermato |
| WIPP 2014: numero di lavoratori contaminati | **corretto da 22 a 21**, e precisato che fu contaminazione *interna*, nessuna esterna |
| WIPP: riapertura gennaio 2017 | confermato |
| Fukushima: UNSCEAR non documenta effetti sanitari da radiazioni sui residenti | confermato (Rapporto 2020/2021) |
| Fukushima: decessi legati all'evacuazione, soprattutto anziani e ospedalizzati | confermato; in pagina è scritto "oltre un migliaio", conservativo rispetto alle stime correnti |
| Chernobyl: 134 casi di sindrome acuta, 28 decessi | confermato (UNSCEAR 2008, Annex D) |
| Fattore di capacità in Italia: fotovoltaico ed eolico | **corretto**: da 15 % e 25 % a 12 % e 20 %, con la ragione (vento italiano meno costante) |
| Confronto eolico nella scheda di Sizewell B | **corretto**: da "tre su dieci" a "circa due su dieci in Italia", per coerenza col dato sopra |
| Acqua pesante: assorbimento del deuterio "oltre due ordini di grandezza" inferiore | confermato (rapporto ≈ 640) |
| PWR: a 155 bar l'acqua bolle oltre i 340 °C | confermato (≈ 345 °C) |
| BWR: emivita dell'azoto-16 ≈ 7 secondi | confermato |
| Calore residuo: 6–7 % subito dopo l'arresto, ≈ 1 % dopo un'ora | confermato |
| TRISO: tenuta del carburo di silicio ≈ 1 600 °C | confermato |

## Punti dichiarati come contesi, non risolti

Nell'approfondimento sugli effetti sanitari è scritto esplicitamente che le
stime a dosi basse dipendono dal modello lineare senza soglia, che è
prudenziale e discusso, e che **è questa la ragione per cui i bilanci di
Chernobyl divergono di ordini di grandezza fra fonti tutte tecnicamente serie**.
È la rappresentazione del dissenso prevista dall'architettura: ventaglio più
ragione metodologica, non un numero unico.

## Fonti in pagina (aggiunta successiva)

Ogni approfondimento porta ora, sotto il testo e sopra i link, una riga
**"Fonte:"** con la provenienza del contenuto (`APPRO_FONTI`). Stessa forma
discreta della riga fonte già presente negli incidenti.

Anche gli elenchi di dati hanno la loro riga di provenienza:

| blocco | fonte dichiarata |
|---|---|
| Scheda dell'impianto | IAEA PRIS tramite World Nuclear Association, consultato il 2026-08-02; rendimento calcolato come netto/termico |
| La tecnologia in breve | documentazione tecnica di filiera e voci richiamate negli approfondimenti |
| Scheda del sito (depositi) | Posiva, DOE, Sogin/ISIN secondo il sito |
| Le barriere | documentazione Posiva e istruttoria svedese; DOE per il WIPP |
| Requisiti del sito | OECD-NEA e IAEA; ISIN per l'Italia |

**Onestà della provenienza.** Dove il testo espone fisica e ingegneria di base
— moderazione, termodinamica, contenimento — la riga dice che la fonte è la
letteratura tecnica corrente e le voci enciclopediche collegate. Non è stato
attribuito a un documento preciso ciò che da quel documento non è stato
ricavato. Le attribuzioni puntuali (UNSCEAR 2008 Annex D, UNSCEAR 2020/2021
Annex B, Kemeny Commission 1979, Accident Investigation Board del DOE per il
WIPP 2014) compaiono solo dove il contenuto viene davvero da lì.

## Controllo di leggibilità (testi tagliati o coperti)

Rilevazione automatica su tutte e tre le sezioni, con le tendine aperte.
Trovati e corretti:

- `.eyebrow` — "Dove finisce il combustibile esaurito" e "Un impianto per ogni
  tecnologia" erano tagliati: `white-space:nowrap` dentro un `aside` con
  `overflow:hidden` e larghezza fissa di 262 px.
- `.r-sub` — i sottotitoli lunghi degli elenchi laterali erano troncati fino a
  54 px ("Chernobyl, unità 3–4 · URSS (oggi Ucraina)", "Finlandia · Isola di
  Olkiluoto, Eurajoki", "Stati Uniti · Carlsbad, Nuovo Messico").
- `.r-nome` — stesso rischio, corretto in via preventiva.

Correzione: rimosso `nowrap`, aggiunto `overflow-wrap:anywhere` e interlinea.

**Falso allarme da non ripetere.** Una prima rilevazione segnalava l'etichetta
"100 km" delle mini-mappe come fuori tela. Era un errore del metodo di misura:
`getBBox()` restituisce coordinate locali e ignora la trasformazione del gruppo
contenitore. Rimisurando con `getBoundingClientRect()` — che tiene conto di
tutte le trasformazioni — nessuna etichetta SVG esce dalla tela, su nessuna
mappa, scena o passo di incidente. Verificata anche l'assenza di
sovrapposizioni fra etichette: zero su tutte le scene.

## Da fare

- Rivedere i link quando la NRC tornerà accessibile: il suo glossario sarebbe
  una fonte migliore di Wikipedia per una decina di voci.
- Estendere gli approfondimenti ai parametri `tech` non ancora coperti.
- Ricontrollo periodico dei 67 URL (link rot).
