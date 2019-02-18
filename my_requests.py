import requests

# Make a Request

r = requests.get('http://httpbin.org/get')
print(r.text)

r = requests.post('http://httpbin.org/post')
print(r.text)

# Passing Parameters
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.text)

r = requests.put('http://httpbin.org/put', data = {'key':'value'})
print(r.text)


import json
url = 'http://httpbin.org/post'
r = requests.post(url, data=json.dumps({'key':'value'}))
r = requests.post(url, json={'key':'value'})
print(r.text)

# POST a Multipart-Encoded File
url = 'http://httpbin.org/post'
files = {'file':
         ('test.txt',
          open('/Users/alexander/Desktop/test.txt',
               'rb'))}

# r = requests.post(url, files=files)
print(r.text)

# Headers
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
print(r.text)

# Response Content
r = requests.get('http://httpbin.org/get')
print(type(r.text), r.text)
print(type(r.content), r.content)
print(type(r.json()), r.json())

# Response Status Codes
print(r.status_code)
print(r.status_code == requests.codes.ok)

bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()

# Response Headers
print(r.headers)

# Redirection and History
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)

r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)

# Cookies

url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

# Session Objects
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(s.cookies)
print(r.text)

s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)

