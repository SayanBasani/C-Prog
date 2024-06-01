import requests
import json
auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
           'grant_type': 'client_credentials',
           'client_id': 'ad2c9eac11164c1daedfb242259eac63',
           'client_secret': '09449177104a4e2d8229d930f5780613',
        })
auth_data = auth_response.json()
access_token = auth_data['access_token']

# Make the search request
search_url = 'https://api.spotify.com/v1/search'
headers = {
    'Authorization': f'Bearer {access_token}'
}
params = {
    'q': 'sad song',
    'type': 'album',
    'limit': 5
}

response = requests.get(search_url, headers=headers, params=params)

# Check the response status
if response.status_code == 200:
    data = response.json()
    
    # Print the structure of the JSON response
    print(json.dumps(data, indent=4))

    # Example: Extracting specific values from the JSON
    albums = data.get('albums', {}).get('items', [])

    for album in albums:
        album_name = album.get('name')
        artist_name = album.get('artists', [])[0].get('name')
        release_date = album.get('release_date')

        print(f"Album: {album_name}, Artist: {artist_name}, Release Date: {release_date}")
else:
    print("Failed to retrieve data:", response.status_code, response.text)
