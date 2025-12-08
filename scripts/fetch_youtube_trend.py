from googleapiclient.discovery import build
import pandas as pd
from dotenv import load_dotenv
import json
import os
from convert_duration import duration_to_seconds

# Load API Key
load_dotenv()

API_KEY = os.getenv('YOUTUBE_API_KEY')
YOUTUBE = build("youtube", "v3", developerKey=API_KEY)

# Load category mapping
with open("../categories.json", "r") as f:
    cat_map = json.load(f)

def get_trending_videos(region):
    """
    Fetch top 50 trending videos for a given region.

    Parameters:
        region (str): Country code (e.g., 'IN', 'US')

    Returns:
        pd.DataFrame: Cleaned table of trending videos and metadata
    """
    request = YOUTUBE.videos().list(
        part="snippet,statistics,contentDetails",
        chart="mostPopular",
        regionCode=region,
        maxResults=50
    )
    response = request.execute()

    rows = []
    for v in response.get("items", []):
        snippet = v["snippet"]
        stats = v.get("statistics", {})
        content = v.get("contentDetails", {})
        cid = snippet.get("categoryId")

        rows.append({
            "video_id": v["id"],
            "published_at": snippet['publishedAt'],
            "title": snippet["title"],
            "channel_title": snippet["channelTitle"],
            "category_name": cat_map.get(cid, "Unknown"),
            "tags": ", ".join(snippet.get("tags", [])),
            "duration": duration_to_seconds(content.get("duration")),
            "definition": content.get("definition"),
            "caption_available": content.get("caption"),
            "licensed_content": content.get("licensedContent"),
            "views": stats.get("viewCount"),
            "likes": stats.get("likeCount"),
            "comments": stats.get("commentCount")
        })

        df = pd.DataFrame(rows)
        df['published_at'] = pd.to_datetime(df['published_at'])

    return df
