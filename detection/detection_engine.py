def detect(events):
    alerts = []

    for event in events:
        log = str(event)

        if "failed" in log.lower():
            alerts.append({"type": "auth_failure", "event": log})

        if "root" in log:
            alerts.append({"type": "privilege_usage", "event": log})

        if "0.0.0.0/0" in log:
            alerts.append({"type": "insecure_exposure", "event": log})

    return alerts
