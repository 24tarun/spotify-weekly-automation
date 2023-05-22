import spotipy

# Get your Spotify authorization token from https://developer.spotify.com/console/get-authentication-tokens/
auth_token = "BQCh1xgHPxcVDCQVH-jhxf-L4j0duJhCjq5DF_JIdj1DxzPSqEjeA0l_PpSU713INKn9crRmySCked0W19vfrtzmHtzOvO14dA4O6TfG16UBqx77F2eA"

# Create a Spotify client
client = spotipy.Spotify(auth=auth_token)

# Create a new playlist
playlist_name = "My New Playlist"
public = False
description = "This is my new playlist."

playlist = client.user_playlist_create(user="48aw7a7h3k01lmk9xu1c95v2t", name=playlist_name, public=public, description=description)

# Print the playlist ID
print(playlist["id"])


