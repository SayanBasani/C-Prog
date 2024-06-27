import requests

url = "https://youtube-v2.p.rapidapi.com/search/"
surl=input("Enter your serch quary :- ")
surl = surl + " song best for mood"
querystring = {"query":surl}

headers = {
	"X-RapidAPI-Key": "67512a51a5msh77cb1f629731743p1fd608jsne6f95d1f415b",
	"X-RapidAPI-Host": "youtube-v2.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
print("\n")
print(data)
print("\n\n\n")
print(data)
print("\n\n\n")
ydata = data['videos'][0]
ykey = data['videos'][0]['video_id']
print("https://www.youtube.com/watch?v="+ykey)