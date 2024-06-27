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

import yt_dlp

def get_audio_stream_url(video_id):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'noplaylist': True,
        'quiet': True
    }

    url = f"https://www.youtube.com/watch?v={video_id}"
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = info_dict['url']
    return audio_url

# Use the video ID from Step 1
audio_url = get_audio_stream_url(ykey)

# print("Audio Stream URL:", audio_url)
print("\n\n")
print("Audio Stream URL:", audio_url)

import webbrowser
if audio_url != " ":
    webbrowser.open(audio_url)