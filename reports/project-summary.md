# SOC NSM Project Summary

## Executive Summary

This project demonstrates an end-to-end Network Security Monitoring workflow in an isolated VirtualBox environment using Suricata, Wireshark, tcpdump, Python and jq.

Two controlled scenarios were investigated:

1. TCP network reconnaissance generated with Nmap.
2. HTTP service access generated with curl against a Python test server.

The reconnaissance scenario was validated through Nmap output and packet-level Wireshark analysis. The HTTP scenario additionally validated a custom Suricata detection signature and correlated the resulting alert with PCAP evidence.

## Key Findings

### Finding 1 — Network reconnaissance

Kali `192.168.56.103` generated repeated TCP SYN probes toward Ubuntu `192.168.56.104` across multiple ports. The behavior is documented as T1046 Network Service Scanning. It was authorized lab activity and did not establish compromise.

### Finding 2 — HTTP service access

Kali accessed Ubuntu TCP/8080. Suricata generated the custom signature `SOC LAB - HTTP Test Service Access`. Wireshark confirmed the HTTP GET and `200 OK` response.

## Analyst Workflow Demonstrated

```text
Traffic Generation
      ↓
Packet Capture
      ↓
Suricata Detection
      ↓
Alert Parsing
      ↓
IOC Extraction
      ↓
Wireshark Correlation
      ↓
MITRE ATT&CK Mapping
      ↓
Incident Documentation
```

## Limitations

- DNS analysis was not completed because Kali's DNS resolver was outside the monitored host-only interface.
- TShark execution encountered a local permission problem even after file-permission checks; Wireshark was therefore used for packet analysis.
- The lab demonstrates controlled behavior and does not claim production-scale detection performance.

## Portfolio Outcome

The repository emphasizes practical SOC analyst tasks: telemetry validation, detection engineering, packet investigation, IOC extraction, evidence correlation, and incident reporting.
