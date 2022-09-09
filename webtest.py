from flask import Flask, redirect, url_for, request, render_template, send_file
app = Flask(__name__)
import os
import random
import time
import platform
import glob

# Change this value to change where it looks for images
imgdir = "/config/workspace/Random-img-web/img"

@app.route('/')
def maint():
   return render_template('wrong-page.html')

#This only returns .png
@app.route('/img.png',methods = ['POST', 'GET'])
def png():
    os.chdir(imgdir)
    ls = glob.glob("*.png")
    print(ls)
    rphoto = ls[random.randrange(0,len(ls))]
    return send_file(str(imgdir + "/" + rphoto), mimetype='image/gif')

#This only returns .jpg
@app.route('/img.jpg',methods = ['POST', 'GET'])
def jpg():
    os.chdir(imgdir)
    ls = glob.glob("*.jpg")
    print(ls)
    rphoto = ls[random.randrange(0,len(ls))]
    return send_file(str(imgdir + "/" + rphoto), mimetype='image/gif')

#This returns both jpg and png
@app.route('/img.jpg',methods = ['POST', 'GET'])
def both():
    os.chdir(imgdir)
    ls = glob.glob("*.jpg")
    ls += glob.glob("*.png")
    print(ls)
    rphoto = ls[random.randrange(0,len(ls))]
    return send_file(str(imgdir + "/" + rphoto), mimetype='image/gif')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)