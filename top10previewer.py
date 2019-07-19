import spotipy
import spotify_token as st

#Get the Access Token (just needed for authentification purposes in order to use the Spotify API)
username = ""
password = ""
data = st.start_session(username, password)
access_token = data[0]

spotify = spotipy.Spotify()

token = data[0]
spotify = spotipy.Spotify(auth=token)

#Get Artist's URI from Spotify
artist_uri = 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

artist = spotify.artist_top_tracks(artist_uri)

for track in artist['tracks'][:10]:
  print('Song Name: ' + track['name'])
  print('Song Preview: ' + track['preview_url'])
  print('Song Cover Art: ' + track['album']['images'][0]['url'] + "\n")



