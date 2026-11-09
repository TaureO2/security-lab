# Roadmap

Plan hasta junio de 2027, con unas 6-7 horas de trabajo semanales. Se revisa cada mes: si cambian las prioridades o el mercado laboral, se ajusta aquí.

## Etapas

| Etapa | Periodo | Entregables |
| --- | --- | --- |
| 1. Fundación | Noviembre 2026 | Perfil de GitHub, este repositorio, esquema común v0 |
| 2. AuthWatch | Noviembre-diciembre 2026 | Analizador de logs de autenticación en Bash |
| 3. phish-triage | Diciembre 2026-enero 2027 | Analizador de correos sospechosos en Python |
| 4. Laboratorio | Febrero-marzo 2027 | SIEM, dominio de Active Directory, Windows, Linux y máquina atacante |
| 5. ad-hygiene | Febrero-marzo 2027 | Auditor de cuentas de Active Directory en PowerShell |
| 6. detections | Abril-mayo 2027 | Reglas Sigma con tests y mapeo a MITRE ATT&CK |
| 7. Ejercicios Purple | Mayo-junio 2027 | Ataques simulados en el laboratorio y su detección, documentados |
| 8. purple-validator | Desde junio 2027 | Validación automática de detecciones y cobertura ATT&CK |

En paralelo, desde enero: **ctf-writeups**, 1-2 horas semanales de práctica ofensiva en plataformas legales.

## Por qué este orden

1. **Bash primero:** es el lenguaje que ya conozco y da un primer resultado rápido.
2. **Python después:** el análisis de correos sospechosos es la tarea más repetida en un SOC y conecta con mi experiencia en soporte técnico.
3. **PowerShell con el laboratorio:** el auditor de Active Directory necesita un dominio donde probarse.
4. **Detecciones y Purple Team al final:** necesitan el laboratorio, datos reales de ataques simulados y las herramientas anteriores.

## Hitos

- **Enero 2027:** perfil presentable con dos herramientas terminadas.
- **Marzo 2027:** laboratorio operativo.
- **Junio 2027:** 3-4 herramientas, reglas de detección propias y primeros ejercicios Purple Team documentados.
