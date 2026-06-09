import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

url = "http://127.0.0.1:8088/api/transactions"
response = requests.get(url)

print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))

response.raise_for_status()

data = response.json()

print("\nRaw JSON type:", type(data))
print("Raw JSON preview:")
print(data if isinstance(data, list) else data.keys())

# Handle beberapa kemungkinan bentuk response
if isinstance(data, list):
    records = data

elif isinstance(data, dict):
    if "data" in data and isinstance(data["data"], list):
        records = data["data"]
    elif "transactions" in data and isinstance(data["transactions"], list):
        records = data["transactions"]
    elif "results" in data and isinstance(data["results"], list):
        records = data["results"]
    else:
        # fallback: flatten dict satu baris
        records = [data]

else:
    raise ValueError("Format response tidak dikenali")

df = pd.json_normalize(records)

print("\nPreview DataFrame:")
print(df.head())

print("\nDataFrame Info:")
print(df.info())

output_path = OUTPUT_DIR / "parsed_result.csv"
df.to_csv(output_path, index=False)

print(f"\nFile saved to: {output_path}")