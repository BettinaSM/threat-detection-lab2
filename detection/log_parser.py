import json

def parse_file(filepath, source):
    events = []

    with open(filepath, "r") as f:
        for line in f:
            if source == "cloud":
                try:
                    data = json.loads(line)
                    data["platform"] = source
                    events.append(data)
                except:
                    continue
            else:
                events.append({
                    "platform": source,
                    "event": line.strip()
                })

    return events