import pandas as pd
import datetime
import os
import time
import json
from fetch_youtube_trend import get_trending_videos

BASE_DIR = os.getcwd()

# Load list of YouTube-supported countries
with open(os.path.join(BASE_DIR, "..", "countries.json"), "r") as f:
    countries = json.load(f)

def run():
    """
    Main workflow:
    - Create folder structure for the current year
    - Fetch trending videos for every country
    - Save country-level CSV files
    - Combine all into latest.csv
    """
    today = datetime.datetime.today()
    data_dir = os.path.join(BASE_DIR, "..", "data")
    year_dir = os.path.join(data_dir, str(today.year))

    # Ensure year directory exists
    if not os.path.exists(year_dir):
        os.makedirs(year_dir)

    latest_df = pd.DataFrame()

    for country in countries:
        print(f"\nFetching trending videos for {country}...")

        try:
            df = get_trending_videos(country)

            # Skip empty results
            if df.empty:
                print(f"No trending data for {country}, skipping.")
                continue

            # Folder for the specific country
            country_dir = os.path.join(year_dir, country)
            os.makedirs(country_dir, exist_ok=True)

            # Save daily file
            file_path = os.path.join(
                country_dir,
                f"trending_{country}_{today.year}-{today.month}-{today.day}.csv"
            )

            df.to_csv(file_path, index=False)
            print(f"Saved → {file_path}")

            # Add country tag and append to combined file
            df.insert(0, 'country_code', country)
            latest_df = pd.concat([latest_df, df], axis=0, ignore_index=True)

            time.sleep(0.3)  # Avoid API quota bursts

        except Exception as e:
            print(f"Error fetching {country}: {e}")

    # Save combined global file
    latest_path = os.path.join(data_dir, "latest.csv")
    latest_df.to_csv(latest_path, index=False)
    print(f"\nSaved combined latest file → {latest_path}")

# Execute workflow when script is run
if __name__ == "__main__":
    run()
