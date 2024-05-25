import json

import requests


def getAPIData(url, opHeader=None, params=None):
    response = requests.get(url, verify=True, headers=opHeader, params=params)
    print("Request URL: ", url)
    print("Request Header: ", response.request.headers)
    print("Response Header: ", response.headers)
    return response


def postAPIData(url, body):
    headers = {'Content-Type': 'application/json'}
    print("\nReqURL: ", url)
    print("ReqBody: ", json.dumps(body))
    return requests.post(url, verify=False, json=body, headers=headers) # El varify = False sirve para que se desactive la verficacion SSL
