# Hier starten

`tof-bridge-planning-method` ist ein kleines **Planungswerkzeug** und kein Runtime-Deployment-System.

> English version: [START_HERE.md](START_HERE.md)

## Wofür es gedacht ist

Bereits vorbereitete Bausteine werden durch eine kontrollierte Planungskette geführt:

```text
00_prepared_blocks/
  → 01_sketches/
  → 02_candidate_sets/
  → 03_reports/
```

Die Ausgabe ist Planungsmaterial. Ein Kandidat ist nicht automatisch angenommen, implementiert oder veröffentlicht.

## Voraussetzungen

- Python 3.11+
- optional Docker mit Docker Compose

## Erster lokaler Lauf

```bash
git clone https://github.com/IMaugrenI/tof-bridge-planning-method.git
cd tof-bridge-planning-method

python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-bridge-plan run
```

Unter Windows aktivierst du die virtuelle Umgebung vorher mit dem normalen PowerShell-/Command-Prompt-Befehl.

## Docker-Alternative

```bash
docker compose up --build bridge_planning
```

## Was in den Eingabeordner gehört

Nutze `00_prepared_blocks/` nur für Material, das bereits ausreichend vorbereitet ist, um in Planung zu gehen.

Gemischtes Altmaterial gehört zuerst in [tof-legacy-recovery-workbench](https://github.com/IMaugrenI/tof-legacy-recovery-workbench).

## Erfolgszustand

Ein erfolgreicher Lauf erzeugt strukturierte Planungsartefakte und hält offene Fragen sowie Unsicherheit sichtbar.

Es soll erkennbar bleiben:

- aus welchem Quellblock ein Kandidat stammt
- welche Alternativen betrachtet wurden
- was noch unsicher ist
- dass kein Kandidat automatisch zu Runtime-Wahrheit wurde

## Sicherheit / öffentliche Nutzung

Keine Geheimnisse, privaten Hostnamen, Produktions-IDs, Kundendaten oder internen Service-Maps in vorbereitete Blöcke committen.

Siehe [SECURITY.md](SECURITY.md).
