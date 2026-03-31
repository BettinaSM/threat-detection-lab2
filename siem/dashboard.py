import json

def show_dashboard():
    with open("output/alerts.json", "r") as f:
        data = json.load(f)

    alerts = data["alerts"]
    correlated = data["correlated"]

    print("\n=== SIEM DASHBOARD ===\n")

    print(f"Total alerts: {len(alerts)}")
    print(f"Correlated threats: {len(correlated)}")

    print("\nTop alert types:")

    types = {}
    for alert in alerts:
        t = alert["type"]
        types[t] = types.get(t, 0) + 1

    for t, count in types.items():
        print(f"- {t}: {count}")
