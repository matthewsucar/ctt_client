import getpass
import json
import pymunge
import requests
import datetime

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
from graphql.utilities import print_schema

login_request = {
    "user": getpass.getuser(),
    "timestamp": datetime.datetime.now(datetime.UTC).replace(tzinfo=None).isoformat(),
    }

json_str = json.dumps(login_request)
cred = pymunge.encode(json_str.encode())

auth_request = {
    "Munge" : cred.decode()
}

url = "https://localhost:8000"
login_url = url + "/login"
api_url = url + "/api"

resp = requests.post(login_url, json=auth_request, verify=False)

print(resp.json())

token = resp.json()["token"]

transport = RequestsHTTPTransport(
    url=api_url,
    verify=False,
    retries=3,
    headers={"Authorization": f"Bearer {token}"}
)
client = Client(transport=transport, fetch_schema_from_transport=True,
    introspection_args={
        "input_value_deprecation": False,
    },
)

with client as session:
    graphql_schema = client.schema
    print(print_schema(graphql_schema))
