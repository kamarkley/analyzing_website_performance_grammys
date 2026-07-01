"""
Recording Academy & Grammy Awards Web Analytics Pipeline
Author: Kenzie Markley
Description: Ingests, processes, and evaluates baseline KPI metrics. Falls back 
             on synthetically generated tracking structures if production files are omitted.
"""

import os
import pandas as pd
import numpy as np

def load_datasets(data_dir="data"):
    """Reads raw telemetry files, falling back gracefully to a synthetic simulator if missing."""
    grammy_path = os.path.join(data_dir, "grammy_live_web_analytics.csv")
    ra_path = os.path.join(data_dir, "ra_live_web_analytics.csv")

    # If the user doesn't have the files, simulate them to show the pipeline works!
    if not os.path.exists(grammy_path) or not os.path.exists(ra_path):
        print("⚠️ Production tracking logs not found. Initializing Synthetic Mock Data Engine for demonstration...")
        return generate_mock_data()

    full_df = pd.read_csv(grammy_path)
    rec_academy = pd.read_csv(ra_path)
    return full_df, rec_academy

def generate_mock_data():
    """Generates a randomized synthetic dataframe matching the production schema constraints."""
    np.random.seed(42)
    dates = pd.date_range(start="2022-01-01", periods=100, freq="D")
    
    # Simulate Grammy.com Event Traffic
    grammy_mock = pd.DataFrame({
        "date": dates,
        "sessions": np.random.randint(1000, 50000, size=100),
        "bounced_sessions": np.random.randint(400, 20000, size=100),
        "pageviews": np.random.randint(3000, 150000, size=100),
        "visitors": np.random.randint(800, 40000, size=100),
        "awards_week": np.random.choice([0, 1], size=100, p=[0.85, 0.15])
    })
    
    # Simulate RecordingAcademy.com B2B Traffic
    ra_mock = pd.DataFrame({
        "date": dates,
        "sessions": np.random.randint(500, 5000, size=100),
        "bounced_sessions": np.random.randint(200, 2500, size=100),
        "pageviews": np.random.randint(1000, 15000, size=100),
        "visitors": np.random.randint(400, 4000, size=100)
    })
    
    return grammy_mock, ra_mock

def preprocess_traffic_data(df):
    """Parses date indices and builds engineered behavioral interaction metrics."""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    # Vectorized Feature Engineering Engine
    df["bounce_rate"] = (df["bounced_sessions"] / df["sessions"]) * 100
    df["pages_per_session"] = df["pageviews"] / df["sessions"]
    return df

def run_pipeline():
    print("Initializing Ingestion Framework...")
    grammy_raw, ra_raw = load_datasets()

    print("Executing Feature Extraction and Metric Calculations...")
    grammy_clean = preprocess_traffic_data(grammy_raw)
    ra_clean = preprocess_traffic_data(ra_raw)

    print("\n--- Pipeline Run Completed Successfully ---")
    print("\nGrammy.com Event-Driven Ingestion Summary:")
    print(grammy_clean.groupby("awards_week")[["visitors", "bounce_rate"]].mean())

    print("\nRecordingAcademy.com Static Baseline Summary:")
    print(ra_clean[["visitors", "bounce_rate"]].mean().to_frame().T)

if __name__ == "__main__":
    run_pipeline()
