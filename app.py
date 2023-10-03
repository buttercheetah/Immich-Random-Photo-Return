# Version 1.2 9/13/23
import requests, os, io, yaml, functions, urllib.request
from flask import Flask, send_file
app = Flask(__name__)


IMMICH_API_URL = functions.cleanurl(os.environ.get('IMMICH_API_URL', 'default_api_url'))
IMMICH_API_KEY = os.environ.get('IMMICH_API_KEY', 'default_api_key')

@app.route('/')
def get_random_image(run=0,error=False):
    if run==10:
        return error
    try:
        imagedata = functions.get_photo_data(IMMICH_API_KEY,IMMICH_API_URL)
        image = functions.getfile(IMMICH_API_KEY,IMMICH_API_URL,imagedata['id'])
        return send_file(functions.AddDate(image,imagedata['fileCreatedAt']), mimetype='image/jpeg')
    except Exception as e:
        return get_random_image(run+1,e)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
