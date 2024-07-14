def cho():
    inst = "1. Happiness                2. Sadness                3. Fear                   \n4. Anger                    5. Disgust                6. Depression             \n7. Joy                      8. Love                   9. Enjoyment              \n10. Sympathy                11. Surprise              12. Irritability \n                 13. Empty mood      14. multiple mood\n         15. Search according need"
    print(inst)

    emotions = [
        "Happiness",      # 1
        "Sadness",        # 2
        "Fear",           # 3
        "Anger",          # 4
        "Disgust",        # 5
        "Depression",     # 6
        "Joy",            # 7
        "Love",           # 8
        "Enjoyment",      # 9
        "Sympathy",       # 10
        "Surprise",       # 11
        "Irritability",   # 12
        "Empty mood",     # 13
        "Multiple mood",  # 14
        "Search according to need"  # 15
    ]

    choise = int(input("Enter according our choise :- "))
    
    if choise != 15:
        print(f'Your choose is {emotions[choise-1]}')
        return emotions[choise-1]
    else:
        search = input("enter your search :- ")
        return search
# print()

import requests

url = "https://youtube-v2.p.rapidapi.com/search/"
# surl=input("Enter your serch quary :- ")
surl=cho()
surl = surl + " song hindi"
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