import requests
a = requests.get("https://www.googleapis.com/auth/datastore").json
print(a)