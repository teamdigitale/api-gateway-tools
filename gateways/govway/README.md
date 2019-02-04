# GovWay

[GovWay](https://github.com/link-it/govway) è un API gateway open source (licenza GPL-v3) prodotto da link.it e basato sull'implementazione della Porta di Dominio [OpenSPCoop](https://www.openspcoop.org/openspcoop/).

Di seguito alcune delle funzionalità indicate nella documentazione di Govway a supporto del ModI2018.

## Funzionalità REST implementate
* API REST
  - Interfacce: caricamento di API OpenAPI 3.0.
  - Error Handling: conforme alle specifiche del RFC 7807 (Problem Details for HTTP APIs).

* Throttling
  - Gestione degli header di throttling:
    - X-RateLimit-Limit: limite massimo di richieste;
    - X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo reset;
    - X-RateLimit-Reset: il numero di secondi mancanti al momento in cui il limite verrà reimpostato
  - In caso di violazione viene generato un response code HTTP 429 (con Problem Details RFC 7807)
  - Sospensione di una API: possibilità di sospendere l’accesso a una API o di limitare l’accesso ad API temporaneamente non disponibili (es. read timeout), generando un response code http 503, con header ‘Retry-After’ valorizzato al numero di secondi di attesa richiesti al client.
  
* Tracciamento
  - Ogni richiesta viene tracciata, indipendentemente dal livello di logging o dall’esito della richiesta
  - Campi tracciati:
    - identificazione della richiesta: data e ora della richiesta, dell’erogatore e dell’API richiesta (url invocazione, http method per REST, soap action per SOAP).
    - esito della chiamata: http status code, eventuali fault (SOAPFault per SOAP,  Problem Details per REST), esito della transazione.
    - identificazione del richiedente: identificazione del soggetto fruitore, Identificativo dell’applicativo chiamante se disponibile, indirizzo IP del Chiamante.
    - correlazione alla transazione applicativa: possibilità di estrarre dai contenuti della richiesta ed associare alla traccia un identificativo applicativo univoco. Possibilità di correlare le tracce di chiamate diverse tramite un identificativo unico di correlazione.


## Da implementare / Work In Progress

  - API di configurazione e monitoraggio del gateway OpenAPI 3.0, conformi alle linee guida del ModI 2018, riusando i componenti definiti in: 
    - https://github.com/teamdigitale/openapi/blob/master/docs/definitions.yaml
  - Supporto ‘Alternative Schema’ per effettuare validazione tramite OpenAPI 3.0 utilizzando schemi differenti come XSD Schema o JSON Schema.  
    - https://github.com/teamdigitale/api-openapi-samples/blob/alternativeSchema/openapi-v3/external-schema.yaml
    - https://github.com/OAI/OpenAPI-Specification/pull/1736/files#r248600075
  - API REST per i servizi SOAP preesistenti in accordo a template di conversione.
