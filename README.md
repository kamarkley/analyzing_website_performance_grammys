# Data Infrastructure & Analytics: Evaluating Domain Split Performance for The Recording Academy

## Executive Business Overview
In 2022, the Recording Academy's VP of Digital Strategy initiated a structural partition of their digital presence, separating the consumer-oriented **Grammy.com** from the professional institutional platform **RecordingAcademy.com**. This strategic initiative aimed to optimize distinct target user behaviors, mitigate resource contention during global high-traffic events (such as Awards Night), and refine target content mapping.

This project builds a data pipeline to parse historical tracking telemetry, compute interactive engagement metrics, and isolate user behavior patterns across both platforms during standard baselines and critical event-driven marketing spikes.

## Tech Stack & Analytical Toolkit
* **Core Languages & Processing Frameworks:** Python, Pandas (Vectorized Feature Engineering), NumPy
* **Visualization Layer:** Plotly Express (Interactive Time-Series Telemetry & Density Profiling)
* **Execution Paradigms:** Modular object-oriented scripting alongside Jupyter Notebook prototypes.

## Core Performance Metrics Engineered
To evaluate true audience retention beyond vanity traffic metrics, the pipeline engineers specialized behavioral engagement KPIs:
* **Bounce Rate ($\%$):** $\frac{\text{Bounced Sessions}}{\text{Total Sessions}} \times 100$ (Measures single-page landing drops).
* **Pages per Session:** $\frac{\text{Pageviews}}{\text{Total Sessions}}$ (Evaluates continuous navigation depth and programmatic user journeys).

## Installation & Project Reproducibility

> **Data Privacy Notice:** The underlying granular web analytics datasets (`grammy_live_web_analytics.csv` and `ra_live_web_analytics.csv`) contain proprietary internal tracking telemetry from The Recording Academy. To respect institutional data privacy boundaries, the raw data files are omitted from public version control. 

To review the structural pipeline, feature engineering logic, or runtime environment architecture, you can execute the data processing script using simulated mock telemetry framework placeholders.

## Strategic Analytics Summary & Insights

* **The High-Traffic Spike Problem:** Consumer traffic on Grammy.com scales exponentially during awards_week, presenting deep right-skewed count structures that require isolated load handling.

* **Audience Retention Stabilization:** By shifting business/membership operations to recordingacademy.com, internal operational user flows maintain predictable engagement levels and stay protected from user drops during consumer traffic surges.
