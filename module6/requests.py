import requests
response = requests.get('https://www.google.com')
print(response.text[:300])

#headers 
response.request.headers['Accept-Encoding']