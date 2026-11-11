# Roadmap

Plan until June 2027, with about 6-7 hours of work per week. It is reviewed every month and changes are recorded here.

## Stages

| Stage | Period | Deliverables |
| --- | --- | --- |
| 1. Foundation | November 2026 | GitHub profile, this repository, common schema v0 |
| 2. AuthWatch | November-December 2026 | Authentication log analyser in Bash |
| 3. phish-triage | December 2026-January 2027 | Suspicious email analyser in Python |
| 4. Lab | February-March 2027 | SIEM, Active Directory domain, Windows, Linux and attacker machine |
| 5. ad-hygiene | February-March 2027 | Active Directory account auditor in PowerShell |
| 6. detections | April-May 2027 | Sigma rules with tests and MITRE ATT&CK mapping |
| 7. Purple exercises | May-June 2027 | Simulated attacks in the lab and their detection, documented |
| 8. purple-validator | From June 2027 | Automatic detection validation and ATT&CK coverage |

In parallel, from January: **ctf-writeups**, 1-2 hours a week of offensive practice on legal platforms.

## Why this order

1. **Bash first:** it is the language I already know, and it gives a quick first result.
2. **Python next:** analysing suspicious emails is one of the most common tasks in a SOC, and it connects with my experience in technical support.
3. **PowerShell with the lab:** the Active Directory auditor needs a domain to test on.
4. **Detections and Purple Team at the end:** they need the lab, real data from simulated attacks and the previous tools.

## Milestones

- **January 2027:** a presentable profile with two finished tools.
- **March 2027:** a working lab.
- **June 2027:** 3-4 tools, my own detection rules and the first documented Purple Team exercises.
