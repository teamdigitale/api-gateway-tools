# WSO2

WSO2 è un api gateway con un motore opensource. La sua pagina
github è: https://github.com/wso2

Per ulteriori informazioni si veda il repository del progetto.

## Implementati

 * In caso di superamento della quota, è possibile ritornare:

HTTP 429 (too many requests) se il rate limit viene superato

Regione Lombardia [ha condiviso una sequence](https://github.com/teamdigitale/api-gateway-tools/blob/master/gateways/wso2/handlers/_throttle_out_handler.xml) che permette di ritornare `Retry-After` in caso di 429.

WSO2 ha implementato il ritorno dell'header `Retry-After` in formato `HTTP-date` dalla versione APIM 3.0.0

Vedi anche:

  - https://github.com/wso2/product-apim/issues/1654
  - https://github.com/wso2/carbon-apimgt/pull/7059

## Vanno implementati

* Gli status che evidenziano un sovraccarico devono essere ritornati quanto prima:

HTTP 503 (service unavailable) in caso di servizio indisponibile (eg. in manutenzione) o di sovraccarico


* Gli header di throttling da implementare [vedi ticket 4295](https://github.com/wso2/product-apim/issues/4295)

  - X-RateLimit-Limit 	        maximum requests limit configured for the API endpoint
  - X-RateLimit-Remaining	remaining requests for the API endpoint until next counter reset
  - X-RateLimit-Reset 	        remaining seconds until next counter reset
