import json

def parse_file(filepath, source):
    events = []

    with open(filepath, "r") as f:
        for line in f:
            if source == "cloud":
                try:
                    events.append(json.loads(line))
                except:
                    continue
            else:
                events.append({
                    "platform": source,
                    "event": line.strip()
                })

    return events
