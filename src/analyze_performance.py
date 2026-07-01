"""
Recording Academy & Grammy Awards Web Analytics Pipeline
Author: Kenzie Markley
Description: Ingests, processes, and evaluates baseline KPI metrics 
             to measure the digital strategy impact of splitting 
             grammy.com and recordingacademy.com.
"""

import os
import pandas as pd


def load_datasets(data_dir="data"):
    """Reads raw web analytics tracking frames from storage."""
    grammy_path = os.path.join(data_dir, "grammy_live_web_analytics.csv")
    ra_path = os.path.join(data_dir, "ra_live_web_analytics.csv")

    if not os.path.exists(grammy_path) or not os.path.exists(ra_path):
        raise FileNotFoundError(
            "Missing critical web analytics tracking frames inside data folder."
        )

    full_df = pd.read_csv(grammy_path)
    rec_academy = pd.read_csv(ra_path)
    return full_df, rec_academy


def preprocess_traffic_data(df):
    """Parses date indices and builds engineered behavioral interaction metrics."""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])

    # Feature Engineering: Interactive Performance Ratios
    df["bounce_rate"] = (df["bounced_sessions"] / df["sessions"]) * 100
    df["pages_per_session"] = df["pageviews"] / df["sessions"]

    return df


def generate_strategic_aggregates(grammy_df, ra_df):
    """Computes critical high-level tracking summaries across core operational states."""
    metrics = ["visitors", "pageviews", "sessions", "bounce_rate", "pages_per_session"]

    # Evaluate Grammy Performance during regular periods vs. Awards milestones
    grammy_summary = (
        grammy_df.groupby("awards_week")[metrics].mean().reset_index()
    )
    grammy_summary["platform"] = "Grammy.com (Consumer-Facing)"

    # Evaluate Recording Academy platform metrics
    ra_summary = ra_df[metrics].mean().to_frame().T
    ra_summary["platform"] = "RecordingAcademy.com (B2B/Institutional)"

    return grammy_summary, ra_summary


def run_pipeline():
    """Executes the operational analytical sequence."""
    print("Initializing Ingestion Framework...")
    grammy_raw, ra_raw = load_datasets()

    print("Executing Feature Extraction and Metric Calculations...")
    grammy_clean = preprocess_traffic_data(grammy_raw)
    ra_clean = preprocess_traffic_data(ra_raw)

    print("\n--- Platform Metrics Analysis Completed Successfully ---")

    # Display core snapshot insights for verifying baseline validity
    print("\nGrammy.com Event-Driven Ingestion Summary:")
    print(
        grammy_clean.groupby("awards_week")[["visitors", "bounce_rate"]].mean()
    )

    print("\nRecordingAcademy.com Static Baseline Summary:")
    print(ra_clean[["visitors", "bounce_rate"]].mean().to_frame().T)


if __name__ == "__main__":
    run_pipeline()
