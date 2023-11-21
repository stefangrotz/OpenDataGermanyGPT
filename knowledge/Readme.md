# Create Portal List

* [Wikidata query](https://query.wikidata.org/#SELECT%20%3Fportal%20%3FportalLabel%20%3FhasApiEndpoint%20%3Fwebsite%0AWHERE%20%7B%0A%20%20%3Fportal%20wdt%3AP31%20wd%3AQ27031827%3B%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20Searching%20for%20instances%20of%20Open%20Data%20Portals%0A%20%20%20%20%20%20%20%20%20%20wdt%3AP17%20%3Fcountry.%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20Restricting%20to%20a%20country%2C%20variable%20%3Fcountry%0A%20%20%20%20%20%20%20%20%20%20VALUES%20%3Fcountry%20%7B%20wd%3AQ183%20wd%3AQ40%20wd%3AQ39%20%7D%20%20%20%20%23%20Germany%20%28Q183%29%2C%20Austria%20%28Q40%29%2C%20Switzerland%20%28Q39%29%0A%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fportal%20wdt%3AP6269%20%3FhasApiEndpoint%20%7D%20%20%20%23%20Searching%20for%20API%20Endpoint%20properties%20%28if%20available%29%0A%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fportal%20wdt%3AP856%20%3Fwebsite%20%7D%20%20%20%20%20%20%20%20%20%20%20%23%20Searching%20for%20the%20official%20website%20%28if%20available%29%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%7D%0AORDER%20BY%20DESC%28%3FhasApiEndpoint%29%0A%0A)https://query.wikidata.org/#SELECT%20%3Fportal%20%3FportalLabel%20%3FhasApiEndpoint%20%3Fwebsite%0AWHERE%20%7B%0A%20%20%3Fportal%20wdt%3AP31%20wd%3AQ27031827%3B%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20Searching%20for%20instances%20of%20Open%20Data%20Portals%0A%20%20%20%20%20%20%20%20%20%20wdt%3AP17%20%3Fcountry.%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20Restricting%20to%20a%20country%2C%20variable%20%3Fcountry%0A%20%20%20%20%20%20%20%20%20%20VALUES%20%3Fcountry%20%7B%20wd%3AQ183%20wd%3AQ40%20wd%3AQ39%20%7D%20%20%20%20%23%20Germany%20%28Q183%29%2C%20Austria%20%28Q40%29%2C%20Switzerland%20%28Q39%29%0A%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fportal%20wdt%3AP6269%20%3FhasApiEndpoint%20%7D%20%20%20%23%20Searching%20for%20API%20Endpoint%20properties%20%28if%20available%29%0A%20%20%20%20%20%20%20%20%20%20OPTIONAL%20%7B%20%3Fportal%20wdt%3AP856%20%3Fwebsite%20%7D%20%20%20%20%20%20%20%20%20%20%20%23%20Searching%20for%20the%20official%20website%20%28if%20available%29%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%7D%0AORDER%20BY%20DESC%28%3FhasApiEndpoint%29%0A%0A
* Convert to marktdown

```
SELECT ?portal ?portalLabel ?hasApiEndpoint ?website
WHERE {
  ?portal wdt:P31 wd:Q27031827;                        # Searching for instances of Open Data Portals
          wdt:P17 ?country.                            # Restricting to a country, variable ?country
          VALUES ?country { wd:Q183 wd:Q40 wd:Q39 }    # Germany (Q183), Austria (Q40), Switzerland (Q39)
          OPTIONAL { ?portal wdt:P6269 ?hasApiEndpoint }   # Searching for API Endpoint properties (if available)
          OPTIONAL { ?portal wdt:P856 ?website }           # Searching for the official website (if available)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
ORDER BY DESC(?hasApiEndpoint)
```
