import json

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

# Load the JSON data from the file
with open('query.json', 'r') as file:
    portals = json.load(file)

# Prepare a list of endpoints using the loaded JSON data
endpoints = [
    {"name": portal["portalLabel"], "url": truncate_url(portal["hasApiEndpoint"])}
    for portal in portals if "hasApiEndpoint" in portal
]

# Create an API file for each endpoint
for endpoint in endpoints:
    create_api_file(endpoint)

print("All API files created.")
