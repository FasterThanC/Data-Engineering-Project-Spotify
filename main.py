import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3

DATABASE_LOCATION = "sqlite:///my_played_tracks.sqlite"
USER_ID = "vadimceremisinov"
TOKEN = "BQA9BU03j3QUeGfxjSFUZ6YfCA41CbG3TV1ZzWtSx9JavaU8WKZaw86-1AblzwOVSWEoHYDEuHbVhrpWIYnZ1jbqWz6_PcBd8d6d3LmJKVkAUp_RJ013eB1Ko8VLERK5SrNnzwGPpnJSTncAvTSwba5D__18B2EY93v1Q0qNYGYpACCCsRLpIdCj4EjnYVVdGzck"

if __name__ == "__main__":

    headers = {
        "Accept" : "application/json",
        "Content-Type" : "application/json",
        "authorization" : "Bearer {token}".format(token=TOKEN)
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after{time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()

    print(data)

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in data ["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][10:10])

    song_dict = {
        "song_name" : song_names,
        "artist_name" : artist_names,
        "played_at" : played_at_list,
        "timestamp" : timestamps
    }

    song_df = pd.DateFrame(song_dict, columns = ["song_name", "artist_name", "played_at", "timestamp"])

    print(song_df)