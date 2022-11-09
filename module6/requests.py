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

response = requests.get(url)
response.raise_for_status()

#more stuff
p = {
      "search": "grey kitten",
      "max_results": 15
    }
response = requests.get("https://example.com/path/to/api", params=p)
response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'

###more
p = {"description": "white kitten",
     "name": "Snowball",
     "age_months": 6}
response = requests.post("https://example.com/path/to/api", data=p)

