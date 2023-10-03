import requests, io, re, os
from flask import Flask, send_file
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

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
            if assets[0]['type'] != 'IMAGE':
                return get_photo_data(api,url)
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

def AddDate(ioimage,datetimevar):
    datetime_obj = datetime.fromisoformat(datetimevar[:-1])  # Removing 'Z' from the string

    # Format the datetime object to a pretty day, month, year format
    pretty_date_format = datetime_obj.strftime("%B %d, %Y")

    #print(pretty_date_format)

    original_image = Image.open(io.BytesIO(ioimage))

    # Create a drawing object
    draw = ImageDraw.Draw(original_image)

    # Calculate the position to place the text at the bottom right
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.30

    font = ImageFont.truetype("./Roboto-Light.ttf", fontsize)
    while font.getsize(pretty_date_format)[0] < img_fraction*original_image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("./Roboto-Light.ttf", fontsize)

    text_width, text_height = draw.textsize(pretty_date_format, font=font)
    image_width, image_height = original_image.size
    x = image_width - text_width - 10  # 10 pixels from the right edge
    y = image_height - text_height - 10  # 10 pixels from the bottom edge

    # Add the text to the image
    draw.text((x, y), pretty_date_format, font=font, fill="white")  # You can change the text color

    #------------------------------------------------------------------------------------------------------------
    now = datetime.now()
    pretty_time_format = now.strftime('%H:%M %p')
        # Calculate the position to place the text at the bottom right
    fontsize = 1  # starting font size

    # portion of image width you want text width to be
    img_fraction = 0.60

    font = ImageFont.truetype("./Roboto-Light.ttf", fontsize)
    while font.getsize(pretty_time_format)[0] < img_fraction*original_image.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("./Roboto-Light.ttf", fontsize)

    text_width, text_height = draw.textsize(pretty_time_format, font=font)
    image_width, image_height = original_image.size
    x = 10  # 10 pixels from the right edge
    y = 10  # 10 pixels from the bottom edge

    # Add the text to the image
    draw.text((x, y), pretty_time_format, font=font, fill="white")  # You can change the text color
    # Save the modified image
    
    byteIO = io.BytesIO()
    original_image.save(byteIO, format='JPEG')
    byteIO.seek(0)
    return byteIO

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