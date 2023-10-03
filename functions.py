import requests, io, re
from flask import Flask, send_file


def get_photo_data(api,url):
    # Make a request to Immich API to get a random image URL
    headers = {'x-api-key': api, 'Accept': 'application/json'}
    params = {'count': 1}  # Set count to 1 to get a single random image
    response = requests.get(f"{url}/asset/random", headers=headers, params=params)

    if response.status_code == 200:
        assets = response.json()
        if assets == []:
            return get_photo_data(api,url)
        else:
            return assets[0]
    else:
        raise Exception('Response error')

def getfile(api,url,id):
    # Make a request to Immich API to get a random image URL
    headers = {'x-api-key': api, 'Accept': 'application/octet-stream'}
    response = requests.post(f"{url}/asset/download/{id}", headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"{url}/asset/download/{id}")
        print(response)
        raise EnvironmentError

def cleanurl(url):
    if url[-1] == '/':
        url = url[:-1]
    match = re.match('^.*\/\/', url)
    if match == None:
        url = f'https://{url}'
    elif match.string[match.end()-4] == 's':
        pass
    else:
        print("https is recommended")
    match = re.match('\/api$', url)
    if match:
        url = url[:-4]
    url = f'{url}/api'
    return url