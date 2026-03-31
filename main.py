from detection.log_parser import parse_file
from detection.detection_engine import detect
from detection.correlation_engine import correlate
import json
from datetime import datetime

all_events = []

all_events += parse_file("data/linux/system.log", "linux")
all_events += parse_file("data/aix/aix_audit.log", "aix")
all_events += parse_file("data/unix/messages.log", "unix")
all_events += parse_file("data/cloud/cloudtrail.json", "cloud")

alerts = detect(all_events)
correlated = correlate(alerts)

# resumo de severidade
severity_summary = {}
for alert in alerts:
    sev = alert["severity"]
    severity_summary[sev] = severity_summary.get(sev, 0) + 1

final_output = {
    "timestamp": str(datetime.now()),
    "source": "multi-platform",
    "alerts": alerts,
    "correlations": correlated,
    "severity_summary": severity_summary
}

with open("output/alerts.json", "w") as f:
    json.dump(final_output, f, indent=4)

print("Detection pipeline executed successfully.")