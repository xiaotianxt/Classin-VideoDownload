import requests
import json

def aria2_download(durl, name, dir):
    url = 'http://127.0.0.1:6800/jsonrpc'
    download_url = durl
    json_rpc = json.dumps({
        'id': '',
        'jsonrpc': '2.0',
        'method': 'aria2.addUri',
        'params': [[download_url], {'dir': dir, 'out': name}]
    })
    response = requests.post(url=url, data=json_rpc)
    print(response.text)