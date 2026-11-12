# security-lab

Central repository of a cybersecurity tool ecosystem with a **Purple Team** approach: Blue Team tools that detect attacks, and Red Team attacks in my own lab to check that those detections work.

This repository does not contain tools. It contains what connects them: the plan, the architecture, the common data format and the lab documentation.

## What is here

| File | Content |
| --- | --- |
| [ROADMAP.md](ROADMAP.md) | What will be built and in what order |
| [PROJECT_STATUS.md](PROJECT_STATUS.md) | Current status of each part |
| [ARCHITECTURE.md](ARCHITECTURE.md) | How the tools fit together and why it is organised this way |
| [LEARNING_PATH.md](LEARNING_PATH.md) | Knowledge practised and pending |
| [schema/](schema/) | Common findings schema `o2.finding` |
| [CHANGELOG.md](CHANGELOG.md) | Important changes |

## The ecosystem

| Repository | Area | Status |
| --- | --- | --- |
| security-lab | Organisation and common schema | Published |
| authwatch | Blue Team · Linux log analysis | In development |
| phish-triage | Blue Team · suspicious email triage | Planned |
| ad-hygiene | Blue Team · Active Directory audit | Planned |
| detections | Blue Team · Sigma rules with tests | Planned |
| ctf-writeups | Red Team · documented legal challenges | Planned |
| purple-validator | Purple Team · detection validation | Planned |

## Principles

- **Always synthetic data.** The examples simulate a fictional hospital (`hosp.lab`). Real data is never used.
- **Attacks only in my own or authorised environments:** the local lab and legal practice platforms.
- **One common format.** All the tools produce findings with the same JSON schema, so any tool can read what another one creates.
- **Quality over quantity.** Each tool has tests, CI, documentation and clear limitations.

## Licence

[MIT](LICENSE)
