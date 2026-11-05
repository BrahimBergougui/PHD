"""Build a balanced country-year panel of World Bank WDI indicators.

Indicators: GDP (current US$), trade (% of GDP), total population, 2000-2024.
The panel keeps every country x year combination, so missing observations
remain as empty cells rather than being dropped.

Usage:
    pip install -r requirements-wdi.txt
    python scripts/fetch_wdi.py
"""

from pathlib import Path

import pandas as pd
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://api.worldbank.org/v2"
YEARS = "2000:2024"
OUTPUT = (
    Path(__file__).resolve().parents[1]
    / "wdi_gdp_trade_population_2000_2024.csv"
)

indicators = {
    "gdp_current_usd": "NY.GDP.MKTP.CD",
    "trade_pct_gdp": "NE.TRD.GNFS.ZS",
    "population": "SP.POP.TOTL",
}

# The API occasionally returns 429/5xx on a large multi-page pull; retry
# transient failures instead of aborting the whole dataset.
SESSION = requests.Session()
SESSION.mount(
    "https://",
    HTTPAdapter(
        max_retries=Retry(
            total=5,
            backoff_factor=1.0,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
        )
    ),
)


def fetch_all(url, params=None):
    """Retrieve all pages of a World Bank API response."""
    params = {**(params or {}), "format": "json", "per_page": 1000}
    records = []
    page = 1

    while True:
        response = SESSION.get(
            url, params={**params, "page": page}, timeout=60
        )
        response.raise_for_status()
        payload = response.json()

        if not isinstance(payload, list) or len(payload) < 2:
            raise ValueError(f"Unexpected API response: {payload}")

        metadata, data = payload
        records.extend(data or [])

        if page >= int(metadata["pages"]):
            break
        page += 1

    return records


# Country metadata distinguishes countries and territories from aggregates.
country_data = fetch_all(f"{BASE_URL}/country")
countries = pd.DataFrame([
    {
        "country_code": item["id"],
        "country_name": item["name"],
    }
    for item in country_data
    if item["region"]["id"] != "NA"
])

# Create a complete country-year panel, retaining missing observations.
years = pd.DataFrame({"year": range(2000, 2025)})
panel = countries.merge(years, how="cross")

for variable, indicator_code in indicators.items():
    records = fetch_all(
        f"{BASE_URL}/country/all/indicator/{indicator_code}",
        {"date": YEARS},
    )

    indicator_data = pd.DataFrame([
        {
            "country_code": item["countryiso3code"],
            "year": int(item["date"]),
            variable: item["value"],
        }
        for item in records
        if item.get("countryiso3code")
    ])

    panel = panel.merge(
        indicator_data,
        on=["country_code", "year"],
        how="left",
        validate="one_to_one",
    )

panel = panel.sort_values(["country_name", "year"]).reset_index(drop=True)
panel.to_csv(OUTPUT, index=False)

print(f"Saved {len(panel):,} country-year rows to {OUTPUT}.")
print(panel.head())
print("\nMissing observations:")
print(panel[list(indicators)].isna().sum())
