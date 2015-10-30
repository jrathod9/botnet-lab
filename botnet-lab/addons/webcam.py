import base64
import json
import requests
from base64 import b64encode
import pygame
import pygame.camera
import os

def webcam():
    client_id = "2ed32bb280dd0b8"
    pygame.camera.init()
    #pygame.camera.list_camera() #Camera detected or not
    if  os.name=="nt":
        cam = pygame.camera.Camera(0,(640,480))
    else:
        cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam.start()
    img = cam.get_image()
    pygame.image.save(img,"im.png")
	
    headers = {"Authorization": "Client-ID 2ed32bb280dd0b8"}
    api_key = 'eb215a75b4e3b0e3604c42b98f3ab7b41656ddfb'
    url = "https://api.imgur.com/3/upload.json"
    j1 = requests.post(
        url, 
        headers = headers,
        data = {
            'key': api_key, 
            'image': b64encode(open('im.png', 'rb').read()),
            'type': 'base64',
            'name': 'im.png',
            'title': 'screen'
        }
    )
    return json.loads(j1.text)["data"]["link"]