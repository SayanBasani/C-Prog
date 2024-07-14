url = 'https://www.googleapis.com/youtube/v3/videos'
apikey = 'AIzaSyCxuEP8qFmJzhzmOpa9XdqwmYJbh19C-40'
import requests,json
a=requests.get('https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id=HpUcMGmZbko&key=AIzaSyCxuEP8qFmJzhzmOpa9XdqwmYJbh19C-40').text

b=json.loads(a)
print(b)
