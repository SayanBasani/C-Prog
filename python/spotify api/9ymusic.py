from ytmusicapi import YTMusic
apikey = {
 "scope": "https://www.googleapis.com/auth/youtube",
 "token_type": "Bearer",
 "access_token": "ya29.a0AXooCguDSK0mBX5UJVW8tbtzt5oUsLCorE-skWN_w2sLH97NVf5oReXZFRze_cojECFytBrlvaafgEu3H42-SSEZ0LY0XeMLkfeQhLtrDvrlz_r7FyqOIRvA53-HJ1bND4DPukRSMK-MWpU5upaOHIJo7CtG9EsFB2m0hBOtId2aixI5aCgYKAVcSARISFQHGX2MizWDf_RWevUAUJ7s5i8Du2A0183",
 "refresh_token": "1//0g6t2xKIAOoNgCgYIARAAGBASNwF-L9Ir1rpUaD6VjVaJsTul32I2zbFJvoFaisgvLUZ2DahmzEahXbEEOS0EW3pb5qpmi5U3CIM",
 "expires_at": 1717304183,
 "expires_in": 63272
}
ytmusic = YTMusic(apikey)
playlistId = ytmusic.create_playlist("test", "test description")
search_results = ytmusic.search("Oasis Wonderwall")
ytmusic.add_playlist_items(playlistId, [search_results[0]['videoId']])