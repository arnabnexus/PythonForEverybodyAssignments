import urllib.request, urllib.parse, urllib.error
import json


url = input('Enter - ')
if len(url) < 1:
    #url = "http://py4e-data.dr-chuck.net/comments_42.json"
    url = "http://py4e-data.dr-chuck.net/comments_2454927.json"


json_data = urllib.request.urlopen(url).read()
print("Retrieved", len(json_data), "characters")
data = json.loads(json_data)
counts = data["comments"]
print("Count:", len(counts))
total = sum(int(comment["count"]) for comment in counts)
print("Sum:", total)