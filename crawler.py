import requests
import sys

data = requests.get("http://wikipedia.com")
print ('+*+' * 20)
print (data.text)