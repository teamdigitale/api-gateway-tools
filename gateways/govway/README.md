# GovWay

[GovWay](https://github.com/link-it/govway) è un API gateway open source (licenza GPL-v3) prodotto da link.it.

Di seguito alcune delle funzionalità indicate nella documentazione di Govway a supporto del ModI.

## Funzionalità REST implementate
* API REST
  - Interfacce: [caricamento](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/definizioneApi.html) di API OpenAPI 3.0.
  - Error Handling: conforme alle specifiche del RFC 7807 (Problem Details for HTTP APIs).

* Throttling
  - Policy di [RateLimiting](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/rateLimiting/index.html) con gestione degli header di throttling:
    - X-RateLimit-Limit: limite massimo di richieste;
    - X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo reset;
    - X-RateLimit-Reset: il numero di secondi mancanti al momento in cui il limite verrà reimpostato
  - In caso di [violazione](https://govway.readthedocs.io/it/latest/console/handling-errors/index.html) viene generato un response code HTTP 429 (con Problem Details RFC 7807)
  - Possibilità di [sospendere](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/sospensioneApi.html) l’accesso a una API o di limitare l’accesso ad API temporaneamente non disponibili (es. read timeout), generando un response code http 503, con header ‘Retry-After’ valorizzato al numero di secondi di attesa richiesti al client.

* Tracciamento
  - Ogni richiesta viene [tracciata](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/tracciamento.html#), indipendentemente dal livello di logging o dall’esito della richiesta
  - Campi tracciati:
    - identificazione della richiesta: data e ora della richiesta, dell’erogatore e dell’API richiesta (url invocazione, http method per REST, soap action per SOAP).
    - esito della chiamata: http status code, eventuali fault (SOAPFault per SOAP,  Problem Details per REST), esito della transazione.
    - identificazione del richiedente: identificazione del soggetto fruitore, Identificativo dell’applicativo chiamante se disponibile, indirizzo IP del Chiamante.
    - correlazione alla transazione applicativa: possibilità di estrarre dai contenuti della richiesta ed associare alla traccia un identificativo applicativo univoco. Possibilità di correlare le tracce di chiamate diverse tramite un identificativo unico di correlazione.

* Sicurezza Messaggio
  - Implementazione dei pattern [ID_AUTH_01](https://govway.readthedocs.io/it/latest/console/profiloModIPA/messaggio/idar01.html), [ID_AUTH_02](https://govway.readthedocs.io/it/latest/console/profiloModIPA/messaggio/idar02.html) e [INTEGRITY_01](https://govway.readthedocs.io/it/latest/console/profiloModIPA/messaggio/idar03.html)
  - Implementazione del profilo [PROFILE_NON_REPUDIATION_01](https://govway.readthedocs.io/it/latest/console/profiloModIPA/messaggio/requestDigest.html)

* OAuth2
  - Gestione di token di autenticazione conformi agli standard JWT, OAuth2 e OIDC.
  - Funzionalità di [authorization server](https://govway.readthedocs.io/it/latest/console/configurazione/tokenPolicy/tokenValidazione.html) per le API erogate: supporto della validazione dei token e dell'acquisizione dei claim interni al token per le successive fasi di [autenticazione](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/controlloAccessi/gestioneToken.html) e [autorizzazione](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/controlloAccessi/tokenClaims.html) (audience, [scope](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/controlloAccessi/scope.html), ...), anche interagendo con Authorization Server esterni tramite funzionalità di Introspection e UserInfo.
  - Funzionalità di negoziazione token per le API fruite tramite le modalità:
	- Client Credentials: negoziazione “Client Credentials Grant” descritta nel [RFC 6749, page-40](https://tools.ietf.org/html/rfc6749#page-40);
	- Resource Owner Password Credentials: negoziazione “Resource Owner Password Credentials Grant” descritta nel [RFC 6749, page 37](https://tools.ietf.org/html/rfc6749#page-37);
	- Signed JWT: negoziazione “Client Credentials Grant” descritta nella [sezione 2.2 del RFC 7523](https://datatracker.ietf.org/doc/html/rfc7523#section-2.2) che prevede lo scambio di un’asserzione JWT firmata tramite certificato x.509 con l’authorization server;
	- Signed JWT with Client Secret: modalità di negoziazione identica alla precedente dove però l’asserzione JWT viene firmata tramite una chiave simmetrica.

* [API](https://govway.readthedocs.io/it/latest/api/index.html) di configurazione e monitoraggio del gateway OpenAPI 3.0
  - [API di Configurazione](https://generator.swagger.io/?url=https://raw.githubusercontent.com/link-it/govway/master/tools/rs/config/server/src/schemi/merge/govway_rs-api_config.yaml)
  - [API di Monitoraggio](https://generator.swagger.io/?url=https://raw.githubusercontent.com/link-it/govway/master/tools/rs/monitor/server/src/schemi/merge/govway_rs-api_monitor.yaml)

* Possibilità di realizzare API REST per i servizi SOAP preesistenti in accordo a template di conversione attraverso [engine di trasformazione](https://govway.readthedocs.io/it/latest/console/profiloApiGateway/trasformazioni/index.html)

## Immagine Docker

Viene fornito un ambiente di prova GovWay funzionante, containerizzato tramite Docker Compose e preinizializzato con degli esempi di scenari OAuth2 e ModI 'INTEGRITY_01'.
Gli scenari preconfigurati vengono descritti nella Guida '[GovWay Docker](DOCKER.md)'.

## Da implementare / Work In Progress

  - Supporto ‘Alternative Schema’ per effettuare validazione tramite OpenAPI 3.0 utilizzando schemi differenti come XSD Schema o JSON Schema.
    - https://github.com/teamdigitale/api-openapi-samples/blob/alternativeSchema/openapi-v3/external-schema.yaml
    - https://github.com/OAI/OpenAPI-Specification/pull/1736/files#r248600075
