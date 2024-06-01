import requests

url = "https://youtube-v2.p.rapidapi.com/search/"
surl=input("Enter your serch quary :- ")
surl = surl + " song best for mood"
querystring = {"query":surl}

headers = {
	"X-RapidAPI-Key": "67512a51a5msh77cb1f629731743p1fd608jsne6f95d1f415b",
	"X-RapidAPI-Host": "youtube-v2.p.rapidapi.com",
  "content-type": "application/json",
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
ydata = data['videos'][0]
ykey = data['videos'][0]['video_id']
vlink = "https://www.youtube.com/watch?v="+ykey
print(vlink)

url = "https://youtube-to-mp315.p.rapidapi.com/download"

headers = {
	"X-RapidAPI-Key": "67512a51a5msh77cb1f629731743p1fd608jsne6f95d1f415b",
	"X-RapidAPI-Host": "youtube-to-mp315.p.rapidapi.com",
}

querystring = {"url":vlink,"format":"mp3"}
response = requests.post(url, json={}, headers=headers, params=querystring)

dlink = response.json()
print(dlink)
slink = dlink['downloadUrl']
print(slink)