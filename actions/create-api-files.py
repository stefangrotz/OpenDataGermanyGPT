import requests
import json

# SPARQL query to fetch data from Wikidata
sparql_query = """
SELECT ?portal ?portalLabel ?countryLabel ?hasApiEndpoint ?website ("CKAN" AS ?protocol)  # Adding CKAN as a static value for protocol
WHERE {
  ?portal wdt:P31 wd:Q27031827;                        # Searching for instances of Open Data Portals
          wdt:P17 ?country.                            # Restricting to a country, variable ?country
          VALUES ?country { wd:Q183 wd:Q40 wd:Q39 }    # Germany (Q183), Austria (Q40), Switzerland (Q39)
          OPTIONAL { ?portal wdt:P6269 ?hasApiEndpoint }   # Searching for API Endpoint properties (if available)
          OPTIONAL { ?portal wdt:P6269 ?apiEndpoint.    # Searching for API Endpoint properties (if available)
                     ?apiEndpoint wdt:P2700 wd:Q105592698;   # Ensuring the API uses the CKAN protocol
                     BIND(CONCAT(STR(?apiEndpoint)) AS ?hasApiEndpoint) }
          OPTIONAL { ?portal wdt:P856 ?website }           # Searching for the official website (if available)
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". 
                           ?portal rdfs:label ?portalLabel .
                           ?country rdfs:label ?countryLabel . }
}
ORDER BY DESC(?hasApiEndpoint)
"""

# Wikidata SPARQL endpoint
endpoint_url = "https://query.wikidata.org/sparql"

# Make the request to Wikidata
response = requests.get(endpoint_url, params={'query': sparql_query, 'format': 'json'})
data = response.json()
# Print a small part of the data to inspect its structure
print(data['results']['bindings'][:2])  # Print the first two items for inspection


# Process the data (assuming it's in the format you expect)
portals = [item for item in data['results']['bindings']]



# Function to create the API structure with dynamic description
def create_api_structure(url,name):
    return {
        "openapi": "3.0.2",
        "info": {
            "title": "CKAN API",
            "description": f"The CKAN API for accessing and managing datasets from {name}. Use a limit:50 as a parameter for queries to avoid too long responses!",
            "version": "1.0.0"
        },
        "servers": [{"url": url}],
    "paths": {
        "/action/package_search": {
            "get": {
                "summary": "Search for datasets",
                "operationId": "package_search",
                "parameters": [
                    {
                        "in": "query",
                        "name": "q",
                        "schema": {
                            "type": "string"
                        },
                        "required": False,
                        "description": "Search query"
                    },
                    {
                        "in": "query",
                        "name": "fq",
                        "schema": {
                            "type": "string"
                        },
                        "required": False,
                        "description": "Filter query"
                    },
                    {
                        "in": "query",
                        "name": "sort",
                        "schema": {
                            "type": "string"
                        },
                        "required": False,
                        "description": "Sorting options"
                    },
                    {
                        "in": "query",
                        "name": "limit",
                        "schema": {
                            "type": "integer"
                        },
                        "required": False,
                        "description": "Limit the number of results, use 50 as default value!"
                    },
                    {
                        "in": "query",
                        "name": "offset",
                        "schema": {
                            "type": "integer"
                        },
                        "required": False,
                        "description": "Offset for the results"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful search",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {
                                            "type": "boolean"
                                        },
                                        "result": {
                                            "type": "object",
                                            "properties": {
                                                "count": {
                                                    "type": "integer"
                                                },
                                                "results": {
                                                    "type": "array",
                                                    "items": {
                                                        "type": "object",
                                                        "additionalProperties": True
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Bad request",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {
                                            "type": "boolean"
                                        },
                                        "error": {
                                            "type": "object",
                                            "additionalProperties": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/action/package_show": {
            "get": {
                "summary": "Retrieve a dataset by ID",
                "operationId": "package_show",
                "parameters": [
                    {
                        "in": "query",
                        "name": "id",
                        "schema": {
                            "type": "string"
                        },
                        "required": True,
                        "description": "Dataset ID"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful retrieval",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {
                                            "type": "boolean"
                                        },
                                        "result": {
                                            "type": "object",
                                            "additionalProperties": True
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "404": {
                        "description": "Dataset not found",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {
                                            "type": "boolean"
                                        },
                                        "error": {
                                            "type": "object",
                                            "additionalProperties": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/action/package_list": {
            "get": {
                "summary": "List all packages with pagination",
                "operationId": "package_list",
                "parameters": [
                    {
                        "in": "query",
                        "name": "limit",
                        "schema": {
                            "type": "integer"
                        },
                        "required": False,
                        "description": "Limit the number of results, use 50 as default value!"
                    },
                    {
                        "in": "query",
                        "name": "offset",
                        "schema": {
                            "type": "integer"
                        },
                        "required": False,
                        "description": "Offset for the results"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful retrieval of package list",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {
                                            "type": "boolean"
                                        },
                                        "result": {
                                            "type": "array",
                                            "items": {
                                                "type": "string"
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "400": {
                        "description": "Bad request",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "success": {
                                            "type": "boolean"
                                        },
                                        "error": {
                                            "type": "object",
                                            "additionalProperties": True
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Function to create an API file for a single endpoint
def create_api_file(endpoint_info):
    api_structure = create_api_structure(endpoint_info["url"],endpoint_info["name"])

    file_name = endpoint_info["name"] + '.json'
    with open(file_name, 'w') as file:
        json.dump(api_structure, file, indent=4)
    print(f"Created file: {file_name}")

# Function to truncate URL to 'api/3/'
def truncate_url(url):
    index = url.find('api/3/')
    return url[:index + 6] if index != -1 else url

# Process the data (assuming it's in the format you expect)
portals = [item for item in data['results']['bindings']]

# Try to create endpoints with additional checks and debugging prints
endpoints = []
for portal in portals:
    # Check if necessary keys are present
    if "portalLabel" in portal and "value" in portal["portalLabel"] and "hasApiEndpoint" in portal and "value" in portal["hasApiEndpoint"]:
        endpoint = {
            "name": portal["portalLabel"]["value"], 
            "url": truncate_url(portal["hasApiEndpoint"]["value"])
        }
        endpoints.append(endpoint)
    else:
        print(f"Skipping portal due to missing data: {portal}")

# Debug print to check the endpoints list
print(endpoints)

# Create an API file for each endpoint
for endpoint in endpoints:
    create_api_file(endpoint)

print("All API files created.")
