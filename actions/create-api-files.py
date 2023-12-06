import json

# List of endpoints with names
endpoints = [
    {"name": "OpenData_HRO", "url": "https://www.opendata-hro.de/api/3/"},
    {"name": "Offene_Daten_Moers", "url": "https://www.offenesdatenportal.de/api/3/"},
    {"name": "Open_Data_Koeln", "url": "https://www.offenedaten-koeln.de/api/3/"},
    # ... include all other endpoints with their names here ...
]

# Function to create the API structure with dynamic description
def create_api_structure(url):
    return {
        "openapi": "3.0.2",
        "info": {
            "title": "CKAN API",
            "description": f"The CKAN API for accessing and managing datasets from {url}. Use a limit:50 as a parameter for queries to avoid too long responses!",
            "version": "1.0.0"
        },
        # ... include other necessary fields here ...
        "servers": [{"url": url}]
    }

# Function to create an API file for a single endpoint
def create_api_file(endpoint_info):
    api_structure = create_api_structure(endpoint_info["url"])

    file_name = endpoint_info["name"] + '.json'
    with open(file_name, 'w') as file:
        json.dump(api_structure, file, indent=4)
    print(f"Created file: {file_name}")

# Create an API file for each endpoint
for endpoint in endpoints:
    create_api_file(endpoint)

print("All API files created.")
