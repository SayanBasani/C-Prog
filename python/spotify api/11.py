from ytmusicapi import YTMusic
import pafy
import vlc
import time

# Your API key details
apikey = {
    "scope": "https://www.googleapis.com/auth/youtube",
    "token_type": "Bearer",
    "access_token": "ya29.a0AXooCguDSK0mBX5UJVW8tbtzt5oUsLCorE-skWN_w2sLH97NVf5oReXZFRze_cojECFytBrlvaafgEu3H42-SSEZ0LY0XeMLkfeQhLtrDvrlz_r7FyqOIRvA53-HJ1bND4DPukRSMK-MWpU5upaOHIJo7CtG9EsFB2m0hBOtId2aixI5aCgYKAVcSARISFQHGX2MizWDf_RWevUAUJ7s5i8Du2A0183",
    "refresh_token": "1//0g6t2xKIAOoNgCgYIARAAGBASNwF-L9Ir1rpUaD6VjVaJsTul32I2zbFJvoFaisgvLUZ2DahmzEahXbEEOS0EW3pb5qpmi5U3CIM",
    "expires_at": 1717304183,
    "expires_in": 63272
}
ytmusic = YTMusic(apikey)

# Ask the user for a search query
search_query = input("Enter your search query: ")

# Search for the song
search_results = ytmusic.search(search_query)
if not search_results:
    print("No results found.")
    exit()

# Filter for songs or videos and get the first result's video ID
video_id = None
for result in search_results:
    if result['resultType'] in ['song', 'video']:
        video_id = result['videoId']
        break

if not video_id:
    print("No suitable video found.")
    exit()

video_url = f"https://www.youtube.com/watch?v={video_id}"
print(video_url)

# Get the video stream
try:
    video = pafy.new(video_url)
    best_audio = video.getbestaudio()
except Exception as e:
    print(f"Error occurred: {e}")
    exit()

# Play the audio stream
player = vlc.MediaPlayer(best_audio.url)
player.play()

# Keep the script running while the audio plays
while player.is_playing():
    time.sleep(1)
