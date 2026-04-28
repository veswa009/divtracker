import requests
import json

res = requests.get("https://www.google.com")
print(res.status_code)

url = "https://docs.google.com/spreadsheets/d/17B4IEGfyIwoWGwEsdadqFzwXvn5LNW5-8E8ZeGvZKrE/gviz/tq?tqx=out:json"

res = requests.get(url)
data = res.text

# remove wrapper
json_data = json.loads(data[47:-2])

rows = json_data['table']['rows']

result = []

for row in rows:
    cols = row['c']
    
    company_name = cols[4]['v']
    symbol = cols[5]['v']
    cmp_price = cols[6]['v']
    shares = cols[7]['v']
    distribution_per_share = cols[8]['v']
    
    expected_distribution = shares * distribution_per_share
    
    result.append({
        "symbol": symbol,
        "company_name": company_name,
        "cmp": cmp_price,
        "shares": shares,
        "distribution_per_share": distribution_per_share,
        "expected_distribution": expected_distribution
    })

print(result)
