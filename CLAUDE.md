# NucleApp — istruzioni per Claude

Sito di divulgazione scientifica sull'energia nucleare, in italiano. Rispondi in italiano.

## A inizio e fine sessione

- Prima di lavorare leggi `verifica/PROGRESS.md` (stato, cose da fare, trappole già
  incontrate) e `verifica/README.md` (regole sulle fonti).
- A fine sessione aggiorna `verifica/PROGRESS.md`, data compresa.

## File

- `nucleapp.html` è il sorgente: le modifiche si fanno qui.
- `pubblica/index.html` è una versione derivata, con immagini, font e crediti
  incorporati. Non va modificata a mano ma rigenerata dal sorgente. Non esiste
  ancora uno script che lo faccia: dopo ogni modifica a `nucleapp.html` va
  rifatta a mano (o lo script va scritto).
- Foto in `img/` e crediti si generano con `prepara-immagini.ps1`.

## Regole sui contenuti

- Nessuna citazione testuale della fonte, nessuna pubblicazione del dato.
- Un dato numerico senza definizione e anno di riferimento non è verificabile.
- Le fonti T4 (stampa, associazioni di categoria) non confermano mai un fatto da sole.
- I punti contesi si mostrano come intervallo di stime, con la ragione del
  disaccordo, non con un numero solo.
- Ogni correzione di un dato va registrata in `verifica/CORREZIONI.md` con il
  valore precedente.

## Ambiente

- Windows e PowerShell. Python e Node.js non sono installati: gli script si
  scrivono in PowerShell.
- La cartella resta su OneDrive per scelta.
- La repository GitHub è pubblica: commit e push solo quando richiesti, e niente
  dati personali o file locali nei commit.
