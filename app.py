# Version 1.2 9/13/23
import requests, os, io, yaml, functions
from flask import Flask, send_file
app = Flask(__name__)


IMMICH_API_URL = functions.cleanurl(os.environ.get('IMMICH_API_URL', 'default_api_url'))
IMMICH_API_KEY = os.environ.get('IMMICH_API_KEY', 'default_api_key')

@app.route('/')
def get_random_image():
    imagedata = functions.get_photo_data(IMMICH_API_KEY,IMMICH_API_URL)
    image = functions.getfile(IMMICH_API_KEY,IMMICH_API_URL,imagedata['id'])
    return send_file(io.BytesIO(image), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
