# tof-bridge-planning-method

> Deutsch ist die Spiegelversion dieses Repositories. Der englische Primärtext liegt in `README.md`.

Öffentliche Bridge-Planning-Baseline, um vorbereitete Bausteine in Skizzen und Zielkandidaten weiterzuführen, ohne Runtime-Wahrheit zu behaupten.

## Kurzüberblick

- startet mit vorbereiteten Bausteinen
- erzeugt grobe Skizzen und Candidate-Sets
- hält Unsicherheit sichtbar
- markiert Zielkandidaten als Planungsobjekte, nicht als Implementierungswahrheit
- vermeidet stille Freigabe von Planung in Runtime

## Warum dieses Repo existiert

Dieses Repository ist eine öffentliche sichere Baseline für ein Brückenplanungs-Muster:

- vorbereitete Bausteine weiterführen
- mehrere Richtungen offen halten, wo nötig
- grobe Skizzen bilden
- Zielkandidaten erzeugen
- die Grenze zwischen Planung und aktiver Runtime-Wahrheit bewahren

## Was dieses Repo ist

- eine reduzierte technische Methoden-Baseline
- eine lauffähige Demo-Pipeline
- ein öffentlich sicheres Beispiel für Planungsdisziplin zwischen Vorbereitung und späterer Umsetzung

## Was dieses Repo nicht ist

- keine Runtime-Wahrheit
- nicht der private interne Planungsraum
- kein Implementierungs-Generator
- kein versteckter Release-Pfad

## Planungskette

1. `00_prepared_blocks/` – vorbereitete Bausteine
2. `01_sketches/` – grobe Skizzen pro Baustein
3. `02_candidate_sets/` – Zielkandidaten-Bündel
4. `03_reports/` – Summary und Acceptance

## Schnellstart

### Lokal

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-bridge-plan run
```

### Docker

```bash
docker compose up --build bridge_planning
```

## Demo-Input

Das Repository enthält nur öffentlich sichere fiktive Bausteine.

Sie zeigen absichtlich klein, wie vorbereitete Substanz weitergeführt werden kann in:
- Discord-Strukturkandidaten
- Bot-Interaktionskandidaten
- Repo-/Runtime-Servicekandidaten
- review-pflichtige offene Kandidaten

## Wichtige Regeln

- Planung ist nicht Runtime-Wahrheit
- Zielkandidaten sind nicht Implementierung
- Unsicherheit bleibt sichtbar
- Richtung darf offen bleiben
- der Default-Lauf materialisiert keinen Runtime-Code

## Verwandte öffentliche Repos

- [`tof-legacy-recovery-workbench`](https://github.com/IMaugrenI/tof-legacy-recovery-workbench) — Recovery- und Trenn-Baseline
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — lokaler Builder-Stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem lokales Wissenssystem
