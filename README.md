# ⚡ EV Industry Analytics Dashboard

An interactive dashboard analysing the electric vehicle market: sales, manufacturers, battery technologies, driving range, customer satisfaction and manufacturing distribution.

## Personas / Scenarios
| Persona | Role | Focus | Dashboard tab |
|---|---|---|---|
| Emily Johnson | EV Market Strategy Director | Sales by category, leading manufacturers, satisfaction, growth segments | Strategy |
| David Chen | Automotive BI Manager | Market share, battery distribution, manufacturing country, ratings | Competitive Intel |
| Dr. Sarah Williams | Sustainable Mobility Researcher | Battery comparison, range trends, production distribution | Research |

## Features
- KPI cards: total sales, avg range, avg battery capacity, avg rating
- Sidebar filters: year, category, manufacturer
- 12 interactive Plotly charts across three persona tabs

## Project Structure
```
├── app.py                 # Streamlit dashboard
├── data/
│   ├── ev_dataset.csv     # Synthetic sample data
│   └── generate_data.py   # Regenerates the sample data
├── requirements.txt
└── LICENSE
```

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Dataset Columns
`Year, Manufacturer, Model, Category, Battery_Type, Battery_Capacity_kWh, Range_km, Price_USD, Annual_Sales, Customer_Rating, Manufacturing_Country`

> ⚠️ The included data is **synthetic** for demonstration. Replace `data/ev_dataset.csv` with real data (same columns) for real insights.

## Deploy Free
Push to GitHub, then deploy at [share.streamlit.io](https://share.streamlit.io) with `app.py` as the entry file.

## Tech Stack
Python · Streamlit · Pandas · Plotly
