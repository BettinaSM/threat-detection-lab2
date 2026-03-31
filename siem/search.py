import json

def search(keyword):
    with open("output/alerts.json", "r") as f:
        data = json.load(f)

    results = []

    for alert in data["alerts"]:
        if keyword.lower() in str(alert).lower():
            results.append(alert)

    return results
