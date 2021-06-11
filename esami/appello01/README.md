# Esercizio 1

* Implementare e testare un modulo di multiplexing su file da più sorgenti di rete
* Le sorgenti inviano messaggi codificati attraverso stringhe JSON
* Il multiplexer deve tenere traccia della sorgente e dell'ordine dei messaggi
* Il formato del file di salvataggio deve essere il seguente

sorgente;numero\_di\_sequenza;messaggio

192.168.0.1;1;Messaggio\_inviato\_dal\_pc\_di\_claudio

.....;.....;.....

# Esercizio 2

* Implementare e testare un modulo di demultiplexing da file su più destinazioni
* Il file ha la struttura dell'esercizio 1
* Si assuma disponibile una tabella di mapping tra sorgenti e destinazioni che si può implementare in modo statico
* L'invio dei messaggi è fatto per ordine di destinazione
