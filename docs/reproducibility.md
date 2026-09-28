# Reproducibility Guide

## 1. VirtualBox Network

Configure both VMs with a shared Host-only Adapter.

Ubuntu:

```text
Host-only: 192.168.56.104/24
NAT:       10.0.3.15/24 (for Internet/package access)
```

Kali:

```text
Host-only: 192.168.56.103/24
NAT:       10.0.3.15/24 on its NAT interface as assigned by VirtualBox
```

Do not depend on the exact NAT address; VirtualBox may assign a different address.

## 2. Validate Connectivity

From Kali:

```bash
ping -c 10 192.168.56.104
```

## 3. Suricata Validation

On Ubuntu:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

Then check the service:

```bash
sudo systemctl status suricata --no-pager
```

## 4. Capture Reconnaissance

On Ubuntu:

```bash
sudo tcpdump -i enp0s3 -nn -w ~/soc-nsm-lab/pcaps/reconnaissance.pcap
```

From Kali, run the controlled scan:

```bash
nmap -sS 192.168.56.104
nmap -sV 192.168.56.104
```

Stop tcpdump with `Ctrl+C`.

Open the capture in Wireshark:

```bash
wireshark ~/soc-nsm-lab/pcaps/reconnaissance.pcap
```

Useful display filter:

```text
ip.src == 192.168.56.103 && ip.dst == 192.168.56.104
```

## 5. HTTP Detection

On Ubuntu:

```bash
python3 -m http.server 8080 --bind 192.168.56.104
```

In another Ubuntu terminal, capture:

```bash
sudo tcpdump -i enp0s3 -nn -w ~/soc-nsm-lab/pcaps/http-test.pcap host 192.168.56.103 and host 192.168.56.104 and port 8080
```

From Kali:

```bash
curl http://192.168.56.104:8080/
```

Stop tcpdump after the request completes.

Check the Suricata EVE log:

```bash
sudo grep 'SOC LAB - HTTP Test Service Access' /var/log/suricata/eve.json
```

## 6. Validate EVE JSON

For a clean EVE file:

```bash
jq -c . /var/log/suricata/eve.json > /dev/null
```

If a historical copy contains NUL bytes, preserve the original first and create a separate analysis copy:

```bash
sudo cp /var/log/suricata/eve.json ~/soc-nsm-lab/eve-original-backup.json
sudo tr -d '\000' < /var/log/suricata/eve.json > ~/soc-nsm-lab/eve-clean.json
jq -c . ~/soc-nsm-lab/eve-clean.json > /dev/null
```

Do not commit either telemetry file to GitHub.

## 7. Python Analysis

```bash
python3 scripts/alerts.py
python3 scripts/ioc_extract.py
```

If using a cleaned historical file, change `LOG_FILE` in the scripts to:

```text
/home/vboxuser/soc-nsm-lab/eve-clean.json
```

## 8. Evidence Preservation

For the HTTP PCAP, the lab recorded this SHA-256:

```text
a35cc9bf5726f5d7a8935001ae5a0406cc0b936b738b8a69aa1c6652f7cf
```

Use `sha256sum` to verify a copy:

```bash
sha256sum ~/soc-nsm-lab/pcaps/http-test.pcap
```
