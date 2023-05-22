import requests
import json
import spotipy
import urllib

#to return access token using client id and secret
def get_access_token(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url,headers=headers,data=data)
    response_data = response.json()
    access_token = response_data.get("access_token")
    return access_token

#to return the json of playlists
def get_users_playlists(user_id):
    url=f"https://api.spotify.com/v1/users/{user_id}/playlists?limit=50&offset=0"
    headers={"Authorization" : "Bearer " +access_token}
    response = requests.get(url,headers=headers)
    json_result=json.loads(response.content)
    print(json_result)
    """with open("dump.json", "w") as f:
        json.dump(json_result, f, indent=4)
    #need to find and return the playlist id of the "discover weekly"
    for item in json_result['items']:
        if item['name'] == 'bleh':
           return item['tracks']['href']
    return None"""
    #lets for fuckssake asssume it returns discover weekly's correct href
    return "https://api.spotify.com/v1/playlists/37i9dQZEVXcCbIePFh3j16/tracks"

def create_playlsit(user_id,access_token):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {
        "Authorization" :"Bearer "+ access_token,
        "Content-Type": "application/json" 
        }
    data = {
    "name": "weeks weekly",
    "description": "Weeks wwwWEKEELY",
    "public": True
    }
    response = requests.post(url,headers=headers,data=data)
    #response_data = response.json()
    print(response)
    
    



#credentials
client_id = "38a9e35cd6f944dfafcbf6a815877867"
client_secret = "74c9bc87a40241b3a9b2fa7b248a597b"
user_id = "48aw7a7h3k01lmk9xu1c95v2t"

access_token = get_access_token(client_id, client_secret)
print(access_token)

href_of_playlist=get_users_playlists(user_id)

parsed_url = urllib.parse.urlparse(href_of_playlist)
playlist_id = parsed_url.path.split("/")[-2]



create_playlsit(user_id,access_token)
