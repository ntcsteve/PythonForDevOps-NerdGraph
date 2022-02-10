import requests
import json
from license import user_key

def nerdgraph_createkey(key):
  # GraphQL query to NerdGraph
  query = """
  mutation {
    apiAccessCreateKeys(keys: {user: {accountId: XXX, userId: XXX, name: "XXX", notes: "XXX" } }) {
      createdKeys {
        id
        key
        name
        notes
        type
      }
      errors {
        message
        type
        ... on ApiAccessIngestKeyError {
          accountId
          errorType
          ingestType
        }
      }
    }
  }"""
  
  # NerdGraph endpoint
  endpoint = "https://api.newrelic.com/graphql"
  headers = {'API-Key': f'{key}'}
  response = requests.post(endpoint, headers=headers, json={"query": query})

  if response.status_code == 200:
    # convert a JSON into an equivalent python dictionary
    json_dictionary = json.loads(response.content)
    print(json_dictionary['data']['apiAccessCreateKeys']['createdKeys'])

    # optional - serialize object as a JSON formatted stream
    # json_response = json.dumps(response.json()["data"]["dashboardCreateSnapshotUrl"], indent=2)
    # print(json_response)

  else:
      # raise an error with a HTTP response code
      raise Exception(f'Nerdgraph query failed with a {response.status_code}.')

nerdgraph_createkey(user_key)