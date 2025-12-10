import streamlit as st
import pandas as pd

@st.cache_data()
def get_doughnut_data(df):    
    category_stats = df.groupby('category_name').agg(
        video_count = ('video_id', 'count'),
        avg_views = ('views', 'mean'),
        avg_likes = ('likes', 'mean'),
        avg_comments = ('comments', 'mean'),
        avg_duration = ('duration', 'mean'),
        avg_engagement = ('engagement_score', 'mean'),
    ).reset_index()

    audio_language_stats = df.groupby('audio_language').agg(
        video_count = ('video_id', 'count'),
        avg_views = ('views', 'mean'),
        avg_likes = ('likes', 'mean'),
        avg_comments = ('comments', 'mean'),
        avg_duration = ('duration', 'mean'),
        avg_engagement = ('engagement_score', 'mean'),
    ).reset_index()

    default_language_stats = df.groupby('default_language').agg(
        video_count = ('video_id', 'count'),
        avg_views = ('views', 'mean'),
        avg_likes = ('likes', 'mean'),
        avg_comments = ('comments', 'mean'),
        avg_duration = ('duration', 'mean'),
        avg_engagement = ('engagement_score', 'mean'),
    ).reset_index()
    
    definition_stats = df.groupby('definition').agg(
        video_count = ('video_id', 'count'),
        avg_views = ('views', 'mean'),
        avg_likes = ('likes', 'mean'),
        avg_comments = ('comments', 'mean'),
        avg_duration = ('duration', 'mean'),
        avg_engagement = ('engagement_score', 'mean')
    ).reset_index()

    caption_stats = df.groupby('caption_available').agg(
        video_count = ('video_id', 'count'),
        avg_views = ('views', 'mean'),
        avg_likes = ('likes', 'mean'),
        avg_comments = ('comments', 'mean'),
        avg_duration = ('duration', 'mean'),
        avg_engagement = ('engagement_score', 'mean')
    ).reset_index()

    license_stats = df.groupby('licensed_content').agg(
        video_count = ('video_id', 'count'),
        avg_views = ('views', 'mean'),
        avg_likes = ('likes', 'mean'),
        avg_comments = ('comments', 'mean'),
        avg_duration = ('duration', 'mean'),
        avg_engagement = ('engagement_score', 'mean')
    ).reset_index()

    return category_stats, audio_language_stats, default_language_stats, definition_stats, caption_stats, license_stats
    