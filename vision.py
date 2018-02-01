# !/usr/bin/python
# coding: utf-8

from googleapiclient.discovery import build
import base64

APIKEY = "AIzaSyCmzfVk2AsSHEWmt7N5hSmKEvJzg3kpKF8"

def launch():

    IMAGE_PATH = "picture.png"

    image_file = open(IMAGE_PATH, "rb")
    encoded_string = base64.b64encode(image_file.read())

    vservice = build('vision', 'v1', developerKey=APIKEY)
    request = vservice.images().annotate(body={
            'requests':[{
                    'image':{
                        'content': encoded_string
                    },
                    'features':[{
                            'type':"TEXT_DETECTION",
                            'max_results':1
                    }]
                }]
            })
    responses = request.execute(num_retries=3)

    text = responses['responses'][0]['textAnnotations'][0]['description']
    norm_text = text.lower()
    text_file = open("picture.txt", "w")
    text_file.write(norm_text)
    text_file.close()
