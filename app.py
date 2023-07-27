from flask import Flask, redirect, url_for, request, render_template, send_file
app = Flask(__name__)
import os
import random
import time
import platform
import glob
import functions
# Change this value to change where it looks for images
imgdir = "/images"

@app.route('/')
def maint():
   return render_template('wrong-page.html')

#This only returns .png
@app.route('/img.png',methods = ['POST', 'GET'])
def png():
    rphoto = functions.getoneimages(imgdir,'png')
    return send_file(str(imgdir + "/" + rphoto), mimetype='image/gif')

#This only returns .jpg
@app.route('/img.jpg',methods = ['POST', 'GET'])
def jpg():
    rphoto = functions.getoneimages(imgdir,'jpg')
    return send_file(str(imgdir + "/" + rphoto), mimetype='image/gif')

#This returns both jpg and png
@app.route('/img',methods = ['POST', 'GET'])
def both():
    rphoto = functions.getoneimages(imgdir,['png','jpg'])
    return send_file(str(imgdir + "/" + rphoto), mimetype='image/gif')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug = True)
