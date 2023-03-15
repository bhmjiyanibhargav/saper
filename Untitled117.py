#!/usr/bin/env python
# coding: utf-8

# # question 01

# In[1]:


import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/@PW-Foundation/videos"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
videos = soup.findAll("a", {"class": "yt-simple-endpoint style-scope ytd-grid-video-renderer"})

for i in range(5):
    video_url = "https://www.youtube.com" + videos[i]["href"]
    print(video_url)

    


# # question 02

# In[2]:


import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/@PW-Foundation/videos"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
thumbnails = soup.findAll("a", {"class": "yt-simple-endpoint style-scope ytd-grid-video-renderer"})

for i in range(5):
    thumbnail = thumbnails[i].find("img")["src"]
    print(thumbnail)


# # question 03

# In[3]:


import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/@PW-Foundation/videos"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
videos = soup.findAll("a", {"class": "yt-simple-endpoint style-scope ytd-grid-video-renderer"})

for i in range(5):
    title = videos[i].find("yt-formatted-string").text
    print(title)


# # question 04

# In[4]:


import google.auth
from googleapiclient.discovery import build

# Set up the YouTube Data API client
credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.readonly'])
youtube = build('youtube', 'v3', credentials=credentials)

# Define the channel ID for the PW-Foundation YouTube channel
channel_id = 'UCU6ZwvQCIW8zqZzuhJmPKgg'

# Call the YouTube Data API to get the first five videos of the channel
videos_response = youtube.search().list(
    part='id,snippet',
    channelId=channel_id,
    order='date',
    type='video',
    maxResults=5
).execute()

# Extract the video IDs and call the YouTube Data API to get the video statistics
for video in videos_response['items']:
    video_id = video['id']['videoId']
    video_response = youtube.videos().list(
        part='statistics',
        id=video_id
    ).execute()
    view_count = video_response['items'][0]['statistics']['viewCount']
    print(f'Video ID: {video_id}, Views: {view_count}')


# # question 05

# In[ ]:


import google.auth
from googleapiclient.discovery import build

# Set up the YouTube Data API client
credentials, project = google.auth.default(scopes=['https://www.googleapis.com/auth/youtube.readonly'])
youtube = build('youtube', 'v3', credentials=credentials)

# Define the channel ID for the PW-Foundation YouTube channel
channel_id = 'UCU6ZwvQCIW8zqZzuhJmPKgg'

# Call the YouTube Data API to get the first five videos of the channel
videos_response = youtube.search().list(
    part='id,snippet',
    channelId=channel_id,
    order='date',
    type='video',
    maxResults=5
).execute()

# Extract the video IDs and call the YouTube Data API to get the video statistics
for video in videos_response['items']:
    video_id = video['id']['videoId']
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()
    time_posted = video_response['items'][0]['snippet']['publishedAt']
    print(f'Video ID: {video_id}, Time Posted: {time_posted}')

