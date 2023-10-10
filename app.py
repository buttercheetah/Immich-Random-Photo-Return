# Version 1.2 9/13/23
import requests, os, io, yaml, functions, urllib.request, random
from flask import Flask, send_file
app = Flask(__name__)


IMMICH_API_URL = functions.cleanurl(os.environ.get('IMMICH_API_URL', 'default_api_url'))
IMMICH_API_KEY = os.environ.get('IMMICH_API_KEY', 'default_api_key')
TIMEZONE = os.environ.get('TIMEZONE', 'UTC')
IMMICH_ALBUM = os.environ.get('IMMICH_ALBUM', 'all')

if IMMICH_ALBUM != 'all':
    albumdata = functions.get_all_phots_in_album(IMMICH_API_KEY, IMMICH_API_URL, IMMICH_ALBUM)
def getimg():
    if IMMICH_ALBUM == 'all':
        imagedata = functions.get_random_photo_data(IMMICH_API_KEY,IMMICH_API_URL)
    else:
        imagedata = random.choice(albumdata)
    return functions.getfile(IMMICH_API_KEY,IMMICH_API_URL,imagedata['id']), imagedata

@app.route('/')
def get_random_image(run=0,error=False):
    if run==10:
        return str(error)
    try:
        image, imagedata = getimg()
        return send_file(functions.AddDate(image,imagedata['fileCreatedAt'],TIMEZONE), mimetype='image/jpeg')
    except Exception as e:
        return get_random_image(run+1,f'{error}\n{str(e)}')

@app.route('/plain')
def get_random_image_plain(run=0,error=False):
    if run==10:
        return str(error)
    try:
        image, imagedata = getimg()
        return send_file(image, mimetype='image/jpeg')
    except Exception as e:
        return get_random_image(run+1,f'{error}\n{str(e)}')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
