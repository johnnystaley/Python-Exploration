
#This script is used to scrape data from a YouTube video using the video id.
#Before using, make sure you obtain a client secret from the google API.

import csv
import os
import google_auth_oauthlib.flow
import googleapiclient.errors
from googleapiclient.discovery import build


# Set up the YouTube API client
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "D:\client_secret_727926435662-s0pua65i5jbnc84kd79r76gbpk6sks1l.apps.googleusercontent.com.json"

flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_local_server()
youtube = build(api_service_name, api_version, credentials=credentials)

# Get the comments from a video and write them to a CSV file
video_id = "c7LrqSxjJQQ"
comments = []

# Get the first page of comments
request = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText",
    maxResults=100
)
response = request.execute()
comments_list_response = response
nextPageToken = None
while response:
    # Extract the comments from the response
    for comment in comments_list_response["items"]:
        comment_id = comment["id"]
        author = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        like_count = comment["snippet"]["topLevelComment"]["snippet"]["likeCount"]
        reply_count = comment["snippet"]["totalReplyCount"]
        #print(comment_id, author, text, like_count, reply_count)

        # Append the comment to the comments list
        comments.append(text)

    # Check if there are more pages of comments
    if "nextPageToken" in response:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            textFormat="plainText",
            pageToken=response["nextPageToken"],
            maxResults=100
        )
        response = request.execute()
    else:
        break

# Write the comments to a CSV file
filename = f"{video_id}_comments.csv"
if not os.path.exists(filename):
    with open(filename, mode="w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        for comment in comments:
            writer.writerow([comment])
else:
    with open(filename, mode="a", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

    for comment in comments:
        writer.writerow([comment])