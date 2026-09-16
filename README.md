# NucleApp

Sito di divulgazione scientifica sull'energia nucleare. Si esplorano i principali
tipi di reattore, i depositi di scorie e gli incidenti più noti, con dati
verificati su fonti citate.

> Progetto in sviluppo.

## Struttura

| Percorso | Contenuto |
|---|---|
| `index.html` | Il sito: HTML, CSS e JavaScript in un unico file. È il file da modificare. Pubblicato con GitHub Pages |
| `img/` | Fotografie degli impianti e relativi crediti (`crediti.json`, `crediti.js`) |
| `pubblica/index.html` | Versione in un solo file, con immagini, font e crediti incorporati |
| `verifica/` | Verifica delle fonti: metodo, registro fonti, affermazioni controllate, correzioni e stato del lavoro |
| `prepara-immagini.ps1` | Scarica le foto da Wikimedia Commons e genera i crediti (`prepara-immagini.py` è la versione Python originale) |

## Vedere il sito

Online: https://pozzif00-prog.github.io/NucleApp/

In locale: aprire `index.html` con un browser. Le foto vengono lette dalla
cartella `img/`, i font da Google Fonts.

## Fonti

Ogni dato del sito deve essere tracciabile a una fonte, con citazione testuale.
Il metodo è descritto in [`verifica/README.md`](verifica/README.md), l'avanzamento
in [`verifica/PROGRESS.md`](verifica/PROGRESS.md).

## Immagini e licenze

Le fotografie provengono da Wikimedia Commons e restano soggette alle rispettive
licenze (pubblico dominio, CC BY, CC BY-SA). Autore, licenza e pagina di origine
di ciascuna sono in `img/crediti.json` e compaiono nelle didascalie del sito.
