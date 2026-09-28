# Security Policy

## Scope

This repository contains documentation and code for an isolated defensive security lab.

## Safe Use

Use the traffic-generation commands only against systems you own or are explicitly authorized to test.

Do not use the reconnaissance examples against public hosts or third-party infrastructure without permission.

## Sensitive Data

Do not commit:

- Passwords
- API keys
- Access tokens
- Private certificates
- Personal logs
- Unnecessary raw PCAPs
- Production telemetry

The `.gitignore` file excludes common telemetry and capture artifacts.
