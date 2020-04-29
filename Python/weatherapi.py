import requests
import json
import sys
from Naked.toolshed.shell import muterun_js
response = muterun_js('api.js')

r=requests.get('http://localhost:3000')
#r=requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=8939acbb7ed793678ee860bbb5087b73' % (zip))
data=r.json()
data_str = json.dumps(data)
widget1 = (data_str [11:18])
widget2 = (data_str [49:56])
widget3 = (data_str [88:95])
widget4 = (data_str [127:134])
color1 = (data_str [31:35])
color2 = (data_str [69:74])
color3 = (data_str [108:113])
color4 = (data_str [147:151])
print(type(data_str))

print(widget1 , color1)
print(widget2 , color2)
print(widget3 , color3)
print(widget4 , color4)