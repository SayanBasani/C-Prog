import requests

url = "https://youtube-to-mp315.p.rapidapi.com/download"

s='https://www.youtube.com/results?search_query=sunsathia'

querystring = {"url":s,"format":"mp3"}
# querystring = {"url":"https://www.youtube.com/watch?v=arijit","format":"mp3"}

payload = {}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "67512a51a5msh77cb1f629731743p1fd608jsne6f95d1f415b",
	"X-RapidAPI-Host": "youtube-to-mp315.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers, params=querystring)

print(response.json())