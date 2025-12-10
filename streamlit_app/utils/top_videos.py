import streamlit as st
import pandas as pd

@st.cache_data()
def get_top_videos(df):    
    df['Engagement %'] = (df['engagement_score'] * 100).round(2)
    df['Video URL'] = df['video_id'].apply(lambda x: f"https://www.youtube.com/watch?v={x}")

    top_views = df.sort_values("views", ascending=False).head(10).set_index(pd.Series(range(1,11)), drop=True)
    top_views = top_views[['title', 'channel_title', 'category_name', 'views', 'Video URL']]
    top_views.columns = ['Title', 'Channel', 'Category', 'Views', 'Video URL']

    top_likes = df.sort_values("likes", ascending=False).head(10).set_index(pd.Series(range(1,11)), drop=True)
    top_likes = top_likes[['title', 'channel_title', 'category_name', 'likes', 'Video URL']]
    top_likes.columns = ['Title', 'Channel', 'Category', 'Likes', 'Video URL']
    
    top_comments = df.sort_values("comments", ascending=False).head(10).set_index(pd.Series(range(1,11)), drop=True)
    top_comments = top_comments[['title', 'channel_title', 'category_name', 'comments', 'Video URL']]
    top_comments.columns = ['Title', 'Channel', 'Category', 'Comments', 'Video URL']
    
    top_engagement = df.sort_values("Engagement %", ascending=False).head(10).set_index(pd.Series(range(1,11)), drop=True)
    top_engagement = top_engagement[['title', 'channel_title', 'category_name', 'Engagement %', 'Video URL']]
    top_engagement.columns = ['Title', 'Channel', 'Category', 'Engagement %', 'Video URL']

    return top_views, top_likes, top_comments, top_engagement