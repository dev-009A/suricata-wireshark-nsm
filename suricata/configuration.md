# Suricata Configuration Notes

## Environment

- Ubuntu: 26.04 LTS
- Suricata: 8.0.3
- Monitoring interface: `enp0s3`
- Host-only IP: `192.168.56.104/24`
- Lab network: `192.168.56.0/24`
- Rule directory: `/var/lib/suricata/rules`

## Interface

The Suricata AF_PACKET interface was configured for the Ubuntu host-only interface:

```yaml
af-packet:
  - interface: enp0s3
```

The NAT interface `enp0s8` was not selected as the lab monitoring interface.

## HOME_NET

The lab network is:

```yaml
HOME_NET: "[192.168.56.0/24]"
```

Use the exact value present in the installed `/etc/suricata/suricata.yaml` when reproducing the lab.

## Rule loading

The system's `default-rule-path` was:

```text
/var/lib/suricata/rules
```

The custom rule was therefore copied to:

```text
/var/lib/suricata/rules/local.rules
```

The configuration test reported the rule set loaded successfully, including the custom rule.

## Validation

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

Expected success message:

```text
Configuration provided was successfully loaded. Exiting.
```

## Service check

```bash
sudo systemctl status suricata --no-pager
```

## EVE JSON

The primary telemetry file used during the lab was:

```text
/var/log/suricata/eve.json
```

For historical analysis, a cleaned copy was created after a NUL-byte parsing issue was observed. Raw logs are excluded from Git.
