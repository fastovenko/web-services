import requests

# Make a Request

r = requests.get('http://httpbin.org/get')
print(r.text)
