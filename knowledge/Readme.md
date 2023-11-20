# Create Portal List

* Wikidata query: https://query.wikidata.org/#SELECT%20%3Fportal%20%3FportalLabel%20%3FhasApiEndpoint%20%3Fwebsite%0AWHERE%20%7B%0A%20%20%3Fportal%20wdt%3AP31%20wd%3AQ27031827%3B%20%20%20%20%20%20%23%20Sucht%20nach%20Instanzen%20von%20Open%20Data%20Portalen%0A%20%20%20%20%20%20%20%20%20%20wdt%3AP17%20wd%3AQ183%3B%20%20%20%20%20%20%20%20%20%20%20%23%20Begrenzt%20auf%20Deutschland%0A%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fportal%20wdt%3AP6269%20%3FhasApiEndpoint%20%7D%20%20%20%23%20Sucht%20nach%20API-Endpunkt-Eigenschaften%20%28falls%20vorhanden%29%0A%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fportal%20wdt%3AP856%20%3Fwebsite%20%7D%20%20%20%20%20%20%20%20%20%20%20%23%20Sucht%20nach%20der%20offiziellen%20Webseite%20%28falls%20vorhanden%29%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%7D%0AORDER%20BY%20DESC%28%3FhasApiEndpoint%29%0A%0A
* Convert to marktdown

```SELECT ?portal ?portalLabel ?hasApiEndpoint ?website
WHERE {
  ?portal wdt:P31 wd:Q27031827;      # Sucht nach Instanzen von Open Data Portalen
          wdt:P17 wd:Q183;           # Begrenzt auf Deutschland
          OPTIONAL { ?portal wdt:P6269 ?hasApiEndpoint }   # Sucht nach API-Endpunkt-Eigenschaften (falls vorhanden)
          OPTIONAL { ?portal wdt:P856 ?website }           # Sucht nach der offiziellen Webseite (falls vorhanden)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY DESC(?hasApiEndpoint)```
