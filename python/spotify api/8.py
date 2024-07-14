import requests

# Replace these values with your own
VIDEO_TITLE = "sad song"
API_KEY = "AIzaSyCxuEP8qFmJzhzmOpa9XdqwmYJbh19C-40"

# Search for the video
# search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={VIDEO_TITLE}&key={API_KEY}"
search_url = f"https://www.googleapis.com/youtube/v3/kind={API_KEY}"
response = requests.get(search_url)
response=response.json()
print(response)
# video_id = response.json()["items"][0]["id"]["videoId"]

# Get the audio stream URL
video_url = f"https://www.googleapis.com/youtube/v3/"