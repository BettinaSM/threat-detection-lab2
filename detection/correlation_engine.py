def correlate(alerts):
    correlated = []

    auth_failures = [a for a in alerts if a["type"] == "auth_failure"]

    if len(auth_failures) >= 3:
        correlated.append({
            "type": "bruteforce_detected",
            "severity": "high",
            "count": len(auth_failures)
        })

    return correlated
