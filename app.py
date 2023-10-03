# Version 1.2 9/13/23
import requests, os, io, yaml, functions
from flask import Flask, send_file
app = Flask(__name__)


@app.route('/')
def get_random_image():
    if not os.path.isfile('conf.yaml'):
        print("template.yaml not found! Please Read the README!")
        exit(1)
    else:
        with open('conf.yaml', 'r') as f:
            data = yaml.safe_load(f)
            IMMICH_API_URL = functions.cleanurl(data['url'])
            IMMICH_API_KEY = data['api-key']
    imagedata = functions.get_photo_data(IMMICH_API_KEY,IMMICH_API_URL)
    image = functions.getfile(IMMICH_API_KEY,IMMICH_API_URL,imagedata['id'])
    return send_file(io.BytesIO(image), mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
