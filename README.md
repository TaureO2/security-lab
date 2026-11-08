# security-lab

Repositorio central de un ecosistema de herramientas de ciberseguridad con enfoque **Purple Team**: herramientas Blue Team que detectan ataques, y ataques Red Team en un laboratorio propio para comprobar si esas detecciones funcionan.

Este repositorio no contiene herramientas. Contiene lo que las une: el plan, la arquitectura, el formato común de datos y la documentación del laboratorio.

## El ecosistema

| Repositorio | Área | Estado |
| --- | --- | --- |
| security-lab | Organización y esquema común | Publicado |
| authwatch | Blue Team · análisis de logs de Linux | En desarrollo |
| phish-triage | Blue Team · triaje de correos sospechosos | Planificado |
| ad-hygiene | Blue Team · auditoría de Active Directory | Planificado |
| detections | Blue Team · reglas Sigma con tests | Planificado |
| ctf-writeups | Red Team · retos legales documentados | Planificado |
| purple-validator | Purple Team · validación de detecciones | Planificado |

## Principios

- **Datos sintéticos siempre.** Los ejemplos simulan un hospital ficticio (`hosp.lab`). Nunca se usan datos reales.
- **Ataques solo en entornos propios o autorizados:** el laboratorio local y plataformas legales de práctica.
- **Un formato común.** Todas las herramientas producen hallazgos con el mismo esquema JSON, así cualquiera puede leer lo que genera otra.
- **Calidad antes que cantidad.** Cada herramienta tiene tests, CI, documentación y limitaciones explícitas.

## Licencia

[MIT](LICENSE)
