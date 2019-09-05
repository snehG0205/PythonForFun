
import json
import urllib.request
import turtle
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])

people = result['people']

for p in people:
  print(p['name'], ' in ', p['craft'])


url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.register_shape('iss.png')

# image source: 
# map.jpg: http://visibleearth.nasa.gov/view.php?id=57752 Credit: NASA
screen.bgpic('map.jpg')

iss = turtle.Turtle()
iss.shape('iss.png')
iss.setheading(90)
iss.penup()

iss.goto(lon, lat)

# When Does ISS next pass over me?
#london
#lat = 51.5072
#lon = 0.1275

# Tokyo
#lat = 35.689487
#lon = 139.691706

# Space Center, Houston
lat = 29.5502
lon = -95.097

# # Mumbai
# lat = 19.0860
# lon = 72.8888

location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url = 'http://api.open-notify.org/iss-pass.json?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#print result
over = result['response'][1]['risetime']
location.write(time.ctime(over))
