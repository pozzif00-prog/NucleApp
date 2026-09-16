# Verifica delle fonti — architettura

Scopo: rendere ogni affermazione del sito tracciabile a una fonte, con citazione
testuale verificabile, e rappresentare onestamente i punti contesi.

## Principio guida

Non massimizzare il numero di citazioni. Assegnare a ogni affermazione **la classe
di fonte giusta**. Per i dati operativi un database istituzionale batte un paper;
i paper servono sui punti contesi o di frontiera.

## Livelli delle fonti

| livello | cosa | esempi |
|---|---|---|
| T1 | dati operativi primari | IAEA PRIS, atti del regolatore (ONR, NRC, ASN), bilanci del gestore |
| T2 | sintesi istituzionali | UNSCEAR, IAEA, OECD-NEA, OMS, World Nuclear Association |
| T3 | letteratura peer-reviewed | via DOI |
| T4 | divulgazione, stampa, associazioni di categoria | mai da solo per un fatto |

Regole dure:
- un'affermazione `numerico` non può poggiare su T3 se esiste un T1;
- un'affermazione `consenso-scientifico` **deve** ancorarsi a T2, i T3 sono supplemento;
- **nessuna citazione testuale, nessuna pubblicazione**: il campo `citazione` è
  obbligatorio e serve a permettere l'audit umano in dieci secondi.

## Tipi di affermazione

Il tipo decide cosa significa "verificata".

- `numerico` — valore + unità + **definizione** + anno di riferimento
- `evento` — data o fatto storico
- `derivato` — calcolato da altre affermazioni (va registrata la formula)
- `causale` — nesso causa/effetto
- `consenso-scientifico` — ciò che gli enti di riferimento concordano
- `interpretativo` — non si verifica, si **attribuisce**

## Stati di verifica

`sostenuta` · `parziale` · `contraddetta` · `insufficiente` · `contesa` · `da_verificare`

Una affermazione `contesa` non va risolta scegliendo un numero: va pubblicata
come ventaglio, **con la ragione metodologica** del disaccordo.

## Struttura dei file

```
verifica/
  README.md                  questo file
  PROGRESS.md                stato del lavoro e prossimi passi
  fonti.yaml                 registro fonti
  affermazioni/<entita>.yaml affermazioni + evidenza
```

## Pipeline

`harvest → retrieve → locate → adjudicate → reconcile`

Sull'adjudicate: un agente sostiene che la fonte supporta l'affermazione, un
secondo prova a **confutarlo**; il disaccordo scala all'umano invece di essere
risolto a maggioranza.

API aperte utili: OpenAlex, Crossref (anche per i ritiri), Semantic Scholar,
Europe PMC (epidemiologia da radiazioni), OSTI (DOE), INIS (IAEA).

## Sorveglianza

Ricontrollo periodico: DOI che non risolvono, link morti, articoli ritirati,
dataset aggiornati. Il fattore di capacità cambia ogni anno: le affermazioni
`numerico` hanno una data di scadenza.
