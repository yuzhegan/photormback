# encoding='utf-8

# @Time: 2021-12-30
# @File: %
#!/usr/bin/env
from icecream import ic
import requests
import urllib
res=urllib.request.urlopen("https://img.ltwebstatic.com/images3_pi/2021/12/09/1639057784093d76c5e04c39cdb1a83001f06e1587.webp")
url_img = res.read()
response = requests.post(
    'https://sdk.photoroom.com/v1/segment',
    headers={'x-api-key': '4778a0136fd750be7ba3d41939d92d3230706061'},
    files={'image_file': url_img }, 
    # files={'image_file': open('a.jpg', 'rb') }, 
    data= {'bg_color':'#FFFFFF'}, 
)

response.raise_for_status()
with open('main.png', 'wb') as f:
	f.write(response.content)
