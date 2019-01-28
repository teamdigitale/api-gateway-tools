# GovWay

[GovWay](https://github.com/link-it/govway) è un API gateway open source (licenza GPL-v3) basato su [OpenSPCoop](https://www.openspcoop.org/openspcoop/) - implementazione della Porta di Dominio italiana.


## Conformità al Modello di Interoperabilità 2018
* API REST
  - Interfacce: supporto per il caricamento di API OpenAPI 3.0.
  - Validazione: supporto per la validazione dei contenuti in formato JSON ed XML
  - Sicurezza: supporto del formato JOSE per la firma e la crittografia in ambito JSON e XmlSignature/XmlEncrypt in ambito XML.
  - Error Handling: conforme alle specifiche del RFC 7807 (Problem Details for HTTP APIs).
* Web Services SOAP
  - Interfacce: supporto per il caricamento di interfacce WSDL.
  - Validazione: supporto per la validazione dei contenuti in formato SOAP 1.1 e 1.2. 
  - Sicurezza: supportate tutte le funzionalità del protocollo WSSecurity (Encrypt, Signature, Timestamp, SAML, UsernameToken, ...).
  - MTOM: supportato sia in maniera trasparente dal Gateway che con la possibilità di delegargli le fasi di imbustamento o sbustamento.
  - Error Handling: generazione di SOAPFault, con detail mutuato da RFC 7807.
* Autenticazione ed Autorizzazione
  - Protocollo HTTPS: supporto della mutua autenticazione su HTTPS, autorizzazione basata sui dati del certificato X509 del mittente.
  - Protocollo OAuth2/OIDC: supporto della validazione dei token OAuth2 ricevuti (anche tramite Introspection), autorizzazione basata sui claims estratti dal token (es. Scope).
  - Protocollo SAML: supporto della validazione di Asserzioni SAML (v1 e v2).
  - Protocollo XACML: supporto di XACML per realizzare policy di autorizzazione complesse.
* Throttling
  - Rate Limiting: possibilità di attuare politiche di Rate Limiting basate su soglie relative al numero di richieste, ai tempi di risposta e all'occupazione di banda
  - Gestione degli header HTTP:
    - X-RateLimit-Limit: limite massimo di richieste;
    - X-RateLimit-Remaining: numero di richieste rimanenti fino al prossimo reset;
    - X-RateLimit-Reset: il numero di secondi mancanti al momento in cui il limite verrà reimpostato
  - Error Handling: in caso di violazione viene generato un response code http 429 (con Problem Details RFC 7807)
  - Sospensione di una API: possibilità di sospendere l’accesso a una API o di limitare l’accesso ad API temporaneamente non disponibili (es. read timeout), generando un response code http 503, con header ‘Retry-After’ valorizzato al numero di secondi di attesa richiesti al client.
* Tracciamento
  - Ogni richiesta viene tracciata, indipendentemente dal livello di logging o dall’esito della richiesta
  - Per ogni richiesta vengono tracciate tutte le informazioni richieste dal ModI2018:
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
