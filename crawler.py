import requests
import sys

try:
    url = sys.argv[1]
except:
     print("Error. Please supply a url as the first argument")
     quit()

try:
    data = requests.get("http://" + url)
except:
    print("Error. Malformed url")
    quit()

print ('+*+*' * 25)
print (data.text)
print ('+*+*' * 25)