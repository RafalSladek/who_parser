import urllib.request, json

response = urllib.request.urlopen("http://apps.who.int/gho/athena/api/?format=json").read().decode('utf8')
print(response)
obj = json.loads(response)
print(obj)
json.dump(obj, open('dimensions.json', 'w'))