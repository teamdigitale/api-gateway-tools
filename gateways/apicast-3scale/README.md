# apicast / 3scale

Apicast è un api gateway opensource. La sua pagina
github è: https://github.com/3scale/apicast

Per ulteriori informazioni si veda il repository del progetto.

## Implementati

 * In caso di superamento della quota, è possibile ritornare:
 
HTTP 429 (too many requests) se il rate limit viene superato.

Vedi anche:

  - https://github.com/3scale/apicast/pull/929

* Gli header di throttling sono stati implementati via [PR 1166](https://github.com/3scale/APIcast/pull/1166) nel [ticket 953](https://github.com/3scale/apicast/issues/953)

  - X-RateLimit-Limit 	        maximum requests limit configured for the API endpoint
  - X-RateLimit-Remaining	remaining requests for the API endpoint until next counter reset
  - X-RateLimit-Reset 	        remaining seconds until next counter reset


## Vanno implementati

* Gli status che evidenziano un sovraccarico devono essere ritornati quanto prima:

HTTP 503 (service unavailable) in caso di servizio indisponibile (eg. in manutenzione) o di sovraccarico

Per differire le richieste, si usa l'header

- Retry-After: numero di secondi dopo i quali ripresentarsi

anche implementando meccanismi di exponential back-off.



