# Kong

[Kong](https://github.com/Kong/kong) è un API gateway open source (licenza GPL-v3) prodotto da Kong Inc.

Per ulteriori informazioni si veda il repository del progetto.

## Implementati (nella versione in sviluppo 2.0.0)

 * In caso di superamento della quota, è possibile ritornare:

HTTP 429 (too many requests) se il rate limit viene superato

Kong ha implementato il ritorno dell'header `Retry-After` in formato `delta-seconds`

 * Gli header di throttling implementati https://github.com/Kong/kong/pull/5335/files sono quelli
   indicati nel lavoro di standardizzazione degli header (quindi senza il prefisso `X-`).

  - X-RateLimit-Limit 	        maximum requests limit configured for the API endpoint
  - X-RateLimit-Remaining	remaining requests for the API endpoint until next counter reset
  - X-RateLimit-Reset 	        remaining seconds until next counter reset

## Vanno implementati

* Gli status che evidenziano un sovraccarico devono essere ritornati quanto prima:

HTTP 503 (service unavailable) in caso di servizio indisponibile (eg. in manutenzione) o di sovraccarico
