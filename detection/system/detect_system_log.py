import re
import json

log_file = "system.log"

patterns = {
    "sudo_misuse": r"sudo:.*authentication failure",
    "service_failure": r"Failed to start",
    "privilege_issue": r"permission denied",
    "suspicious_activity": r"segfault|core dumped"
}

def detect_threats():
    alerts = []

    with open(log_file, "r") as f:
        for line in f:
            for threat, pattern in patterns.items():
                if re.search(pattern, line, re.IGNORECASE):
                    alerts.append({
                        "type": threat,
                        "log": line.strip()
                    })

    return alerts

if __name__ == "__main__":
    results = detect_threats()
    print(json.dumps(results, indent=4))
