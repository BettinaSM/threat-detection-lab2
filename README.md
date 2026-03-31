# Threat Detection Lab 2 - Multi-Platform SIEM Simulation

## Overview

This project simulates a real-world Security Operations Center (SOC) pipeline, including log ingestion, detection engineering, correlation, and a lightweight SIEM interface.

It demonstrates how security events from multiple platforms can be processed, analyzed, and investigated.

---

## Architecture
data → parser → detection engine → correlation → output → SIEM


---

## Supported Platforms

- Linux (system logs)
- AIX (audit logs)
- Unix (messages logs)
- Cloud (CloudTrail-like JSON logs)

---

## Features

- Multi-source log ingestion
- Log normalization layer
- Rule-based detection engine (Detection as Code)
- Threat correlation engine
- Severity classification
- SIEM simulation with:
  - Dashboard view
  - Alert search functionality

---

## Project Structure

---

## Supported Platforms

- Linux (system logs)
- AIX (audit logs)
- Unix (messages logs)
- Cloud (CloudTrail-like JSON logs)

---

## Features

- Multi-source log ingestion
- Log normalization layer
- Rule-based detection engine (Detection as Code)
- Threat correlation engine
- Severity classification
- SIEM simulation with:
  - Dashboard view
  - Alert search functionality

---

## Project Structure
threat-detection-lab2/
├── data/
├── detection/
├── rules/
├── siem/
├── output/
├── main.py


---

## Detection Engine

Detection is implemented using externalized rules:

- Rules are defined in `rules/detection_rules.json`
- Each rule includes:
  - name
  - keywords
  - severity

This approach follows modern Detection Engineering practices.

---

## Correlation Engine

The correlation engine identifies patterns across alerts.

Example:
- Multiple authentication failures → potential brute force attack

---

## SIEM Simulation

The project includes a lightweight SIEM interface:

### Dashboard

Displays:
- Total alerts
- Correlated threats
- Alert distribution by type

### Search

Allows keyword-based investigation across alerts.

---

## How to Run

### 1. Execute detection pipeline
python3 main.py


### 2. Launch SIEM interface
python3 siem/app.py


---

## Example Output

Generated file:
output/alerts.json


Contains:
- Alerts
- Correlations
- Severity summary
- Timestamp

---

## Use Cases

- Security monitoring simulation
- Detection engineering practice
- SOC workflow demonstration
- SIEM fundamentals learning

---

## Future Improvements

- MITRE ATT&CK mapping
- Sigma rule support
- Real-time log ingestion
- Integration with cloud-native logs (AWS, GCP, Azure)
- Visualization dashboards (Grafana / Kibana)

---

## Skills Demonstrated

- Detection Engineering
- Log Analysis
- Security Automation
- Python for Security
- SIEM Concepts
- Multi-platform Security Monitoring

---

## Author

Developed as part of a DevSecOps & Cloud Security learning roadmap.