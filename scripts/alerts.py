#!/usr/bin/env python3
"""Print Suricata alert events in a SOC-friendly format."""

import json

LOG_FILE = "/var/log/suricata/eve.json"


def main() -> None:
    with open(LOG_FILE, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            if event.get("event_type") != "alert":
                continue

            alert = event.get("alert", {})

            print("=" * 60)
            print("SURICATA ALERT")
            print("=" * 60)
            print("Timestamp   :", event.get("timestamp"))
            print("Source IP   :", event.get("src_ip"))
            print("Source Port :", event.get("src_port"))
            print("Destination :", event.get("dest_ip"))
            print("Dest Port   :", event.get("dest_port"))
            print("Protocol    :", event.get("proto"))
            print("Signature   :", alert.get("signature"))
            print("Severity    :", alert.get("severity"))
            print("Category    :", alert.get("category"))


if __name__ == "__main__":
    main()
