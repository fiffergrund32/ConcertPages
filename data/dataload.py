from algoliasearch.search_client import SearchClient

# Algolia client credentials
ALGOLIA_APP_ID = '4P0IPJPNC7'
ALGOLIA_API_KEY = '4f0b697d5afa71eafc15cb816490bce3'
ALGOLIA_INDEX_NAME = 'casey_rainmaker'

# Initialize the client
# https://www.algolia.com/doc/api-client/getting-started/instantiate-client-index/?client=python
client = SearchClient.create(ALGOLIA_APP_ID, ALGOLIA_API_KEY)

# Initialize an index
# https://www.algolia.com/doc/api-client/getting-started/instantiate-client-index/#initialize-an-index
index = client.init_index(ALGOLIA_INDEX_NAME)

# Open the json file and load the records
import json

with open('concerts2.json', encoding='utf-8') as file:
    records = json.load(file)
    
index.save_objects(records, {'autoGenerateObjectIDIfNotExist': True})

# set the searchable attributes (note, this is explicitly set to prioritize name before location equally)
index.set_settings({
    'searchableAttributes': ['name','unordered(location)','date'],
    'attributesForFaceting': ['searchable(location)'],
    'ranking': [
        'typo',
        'geo',
        'desc(date)',
        'filters',
        'words',
        'proximity',
        'attribute',
        'exact',
        'custom'
    ]
})    
