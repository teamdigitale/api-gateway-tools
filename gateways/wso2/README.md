# WSO2

WSO2 è un api gateway con un motore opensource. La sua pagina
github è: https://github.com/wso2

## Vanno implementati

* Gli status che evidenziano un sovraccarico devono essere ritornati quanto prima:

HTTP 429 (too many requests) se il rate limit viene superato
HTTP 503 (service unavailable) in caso di servizio indisponibile (eg. in manutenzione) o di sovraccarico

Per differire le richieste, si usa l'header

- Retry-After: numero di secondi dopo i quali ripresentarsi

anche implementando meccanismi di exponential back-off.

* Gli header di throttling sono

  - X-RateLimit-Limit 	        maximum requests limit configured for the API endpoint
  - X-RateLimit-Remaining	remaining requests for the API endpoint until next counter reset
  - X-RateLimit-Reset 	        remaining seconds until next counter reset
