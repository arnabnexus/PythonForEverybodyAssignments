import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter - ')
if len(url) < 1:
    #url = "http://py4e-data.dr-chuck.net/comments_42.xml"
    url = "http://py4e-data.dr-chuck.net/comments_2454926.xml"


xml = urllib.request.urlopen(url).read()
print("Retrieved", len(xml), "characters")
tree = ET.fromstring(xml)
counts = tree.findall('comments/comment/count')
print("Count:", len(counts))
total = sum(int(count.text) for count in counts)
print("Sum:", total)