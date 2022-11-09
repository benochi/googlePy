import requests
response = requests.get('https://www.google.com')
print(response.text[:300])

#headers 
response.request.headers['Accept-Encoding']

#boolen res
response.ok

#status code
response.status_code

#ex
url = 'https://www.google.com'
response = requests.get(url)
if not response.ok:
    raise Exception("GET failed with status code {}".format(response.status_code))