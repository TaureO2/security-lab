# Architecture

## Overview

The tools in the ecosystem are connected through a **common findings format** in JSON. Each tool reads a data source and produces findings with the same schema, so another tool (a SIEM, a report or the validator) can use them without changes.

```text
┌──────────────────────┐
│ 1. Data sources      │◄─────────────┐
└───────────┬──────────┘              │ creates data
            ▼               ┌─────────┴───────────┐
┌──────────────────────┐    │ Attacker in the lab │
│ 2. Analysers         │    └─────────▲───────────┘
└───────────┬──────────┘              │
            ▼                         │
┌──────────────────────┐              │
│ 3. Common schema     │              │
└───────────┬──────────┘              │
            ▼                         │ was it detected?
┌──────────────────────┐              │
│ 4. Detection         │              │
└───────────┬──────────┘              │
            ▼                         │
┌──────────────────────┐              │
│ 5. Validation        ├──────────────┘
└──────────────────────┘
```

| Layer | Content |
| --- | --- |
| 1. Data sources | Linux and Windows logs, emails, Active Directory |
| 2. Analysers | authwatch, phish-triage, ad-hygiene |
| 3. Common schema | JSON findings with the `o2.finding` format |
| 4. Detection | Sigma rules and the Wazuh SIEM in the lab |
| 5. Validation | purple-validator: which attacks were detected and which were not |
| Attacker in the lab | Kali machine that simulates MITRE ATT&CK techniques |

The loop on the right is the Purple Team part: an attack technique is simulated in the lab, the data it creates goes through the tools, and the validator checks whether any detection saw it.

## Decisions

### 1. Hybrid repository architecture

- **Decision:** this central repository explains the whole ecosystem; each important tool has its own repository.
- **Rejected alternatives:**
  - One repository for everything: easy to maintain, but the work is hidden in folders, and it mixes languages and versions in the same cycle.
  - Only separate repositories: each tool is independent, but there is no overview and no place for the common schema.
- **Accepted cost:** more repositories to maintain, and the schema must be kept in sync.

### 2. Common findings schema

- **Decision:** all the tools can produce JSON with the `o2.finding` schema, versioned in the `schema/` folder of this repository.
- **Reason:** it makes it possible to chain tools, send findings to a SIEM and measure coverage in the same way.
- **Accepted cost:** changing the schema means checking every tool. That is why it is versioned (`v0`, `v1`...) and a published version does not change.

### 3. Synthetic data

- **Decision:** all examples and tests use invented data from a fictional hospital (`hosp.lab`, machines like `HOSP-WS-xxx`, documentation IP addresses like `203.0.113.0/24`).
- **Reason:** real data from any organisation is confidential. Documentation IP addresses (RFC 5737) belong to nobody.

### 4. Local lab

- **Decision:** a VirtualBox lab with an isolated internal network.
- **Planned machines:** SIEM (Ubuntu + Wazuh), domain controller (Windows Server 2022), Windows 11 workstation with Sysmon, Linux server, and Kali as the attacker machine.
- **Reason:** it allows practising attacks and detection without touching other people's networks. Snapshots make it possible to go back to a clean state in seconds.
