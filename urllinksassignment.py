import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
if len(url) < 1:
    #url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    url = "http://py4e-data.dr-chuck.net/known_by_Sabrina.html"

count = input('Enter count: ')
if len(count) < 1:
    #count = 4
    count = 7
position = input('Enter position: ')
if len(position) < 1:
    #position = 3
    position =18

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
tags = soup('a')

str = url.split('/')[len(url.split('/'))-1].split('.')[0].split('_')[2]
for i in range(int(count)):
    url = tags[int(position)-1].get('href', None)

    str = str + " " + tags[int(position)-1].text
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

print(str.lstrip())



