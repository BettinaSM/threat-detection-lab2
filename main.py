from detection.log_parser import parse_file
from detection.detection_engine import detect
from detection.correlation_engine import correlate
import json

all_events = []

all_events += parse_file("data/linux/system.log", "linux")
all_events += parse_file("data/aix/aix_audit.log", "aix")
all_events += parse_file("data/unix/messages.log", "unix")
all_events += parse_file("data/cloud/cloudtrail.json", "cloud")

alerts = detect(all_events)
correlated = correlate(alerts)

final_output = {
    "alerts": alerts,
    "correlated": correlated
}

with open("output/alerts.json", "w") as f:
    json.dump(final_output, f, indent=4)

print("Detection pipeline executed successfully.")
