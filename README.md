# ScrabblePointsCalculator
Questo programma scritto in *Python* crea un semplice server locale che ci permette di accedere, tramite l'indirizzo 
> 127.0.0.1:5000 
alla pagina web. In questa pagina è possibile inserire delle parole, ed il programma calcolerà il punteggio di *Scarabeo* associato.

E' possibile anche aggiungere le parole ad una lista, in modo da poterne tenere traccia.

# Problemi
La versione corrente è accessibile al [link](https://follen.pythonanywhere.com/), ma purtroppo *PythonAnyWhere* non permette di eseguire più istanze della stessa
applicazione, quindi, in poche parole, non è possibile avere una sessione per ogni utente. Ho provato a risolvere il problema tramite python, andando a rilevare l'ip
da cui ogni utente si connette, inserirlo in una lista e poi controllare quale utente (differenziato dal suo ip) avesse fatto la richiesta, per poter restituire le 
parole da lui inserite, ma purtroppo non riesco a capire dove è presente l'errore.
