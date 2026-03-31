import json

def load_rules():
    with open("rules/detection_rules.json", "r") as f:
        return json.load(f)

def detect(events):
    alerts = []
    rules = load_rules()

    for event in events:
        log = str(event).lower()

        for rule in rules:
            if any(keyword in log for keyword in rule["keywords"]):
                alerts.append({
                    "type": rule["name"],
                    "severity": rule["severity"],
                    "event": log
                })

    return alerts