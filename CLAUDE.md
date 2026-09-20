# NucleApp — istruzioni per Claude

Sito di divulgazione scientifica sull'energia nucleare, in italiano. Rispondi in italiano.

## A inizio e fine sessione

- Prima di lavorare leggi `verifica/PROGRESS.md` (stato, cose da fare, trappole già
  incontrate) e `verifica/README.md` (regole sulle fonti).
- A fine sessione aggiorna `verifica/PROGRESS.md`, data compresa.

## File

- `index.html` è il sorgente: le modifiche si fanno qui. Pubblicato con GitHub
  Pages (branch `main`, cartella `/`): ogni push su `main` aggiorna il sito
  online in circa un minuto.
- Non esiste più una versione derivata (`pubblica/index.html` è stata tolta il
  2026-09-20: era obsoleta, senza i nuovi disegni): il sito online è
  `index.html` così com'è, con le foto lette da `img/`.
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
