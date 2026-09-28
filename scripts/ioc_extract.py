#!/usr/bin/env python3
"""Extract common network indicators from Suricata alert events."""

import json
from collections import Counter

LOG_FILE = "/var/log/suricata/eve.json"


def main() -> None:
    src_ips = Counter()
    dst_ips = Counter()
    dst_ports = Counter()

    with open(LOG_FILE, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            if event.get("event_type") != "alert":
                continue

            if event.get("src_ip"):
                src_ips[event["src_ip"]] += 1
            if event.get("dest_ip"):
                dst_ips[event["dest_ip"]] += 1
            if event.get("dest_port"):
                dst_ports[event["dest_port"]] += 1

    print("\nSource IPs:")
    for ip, count in src_ips.most_common():
        print(ip, count)

    print("\nDestination IPs:")
    for ip, count in dst_ips.most_common():
        print(ip, count)

    print("\nDestination Ports:")
    for port, count in dst_ports.most_common():
        print(port, count)


if __name__ == "__main__":
    main()
