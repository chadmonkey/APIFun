from googleapiclient.discovery import build

import configparser

config = configparser.ConfigParser()
config.read("config.properties")

api_key = config.get("API_KEYS", "YOUTUBE_API_KEY")

youtube = build('youtube', 'v3', developerKey=api_key)

# Get trending videos in the US
request = youtube.videos().list(
    part="snippet,statistics",
    chart="mostPopular",
    regionCode="US",
    maxResults=10
)
response = request.execute()

# Print titles and views
for video in response["items"]:
    title = video["snippet"]["title"]
    #views = video["statistics"].get("viewCount", "N/A")
    #print(f"{title} - {views} views")
    print(f"{title}")
