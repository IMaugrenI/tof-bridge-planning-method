# tof-bridge-planning-method

> Die englische Hauptfassung liegt in `README.md`.

Oeffentliche bridge_planning Baseline, um vorbereitete Bausteine in Skizzen und Zielkandidaten weiterzufuehren, ohne Runtime_Wahrheit zu behaupten.

Ich nutze dieses Repo, um zu zeigen, wie vorbereitete Materialien in einem strukturierten Planungsraum weitergehen koennen, ohne dass Planung versehentlich zu Implementierung wird.

## start_here

### local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
tof-bridge-plan run
```

### docker

```bash
docker compose up --build bridge_planning
```

## was_dieses_repo_macht

1. es startet von vorbereiteten Bausteinen
2. es erzeugt Skizzen und Kandidatenmengen
3. es haelt Unsicherheit sichtbar
4. es markiert Zielkandidaten als Planungsobjekte, nicht als Implementierungswahrheit
5. es verhindert stillen Uebergang von Planung in Runtime

## warum_das_wichtig_ist

1. Planung und Runtime_Wahrheit sind nicht dasselbe
2. vorbereitete Materialien brauchen oft mehrere offene Richtungen
3. Zielkandidaten brauchen Review vor der Implementierung
4. Planungsdisziplin verhindert versteckte Release_Pfade

## planning_chain

1. `00_prepared_blocks/` = vorbereitete Bausteine
2. `01_sketches/` = grobe Skizzen pro Baustein
3. `02_candidate_sets/` = Zielkandidaten_Buendel
4. `03_reports/` = Zusammenfassung und Annahme

## fuer_arbeitgeber

Dieses Repo ist nuetzlich, wenn du sehen willst, wie ich mit folgenden Dingen umgehe:

1. strukturierter Fortsetzung von Vorbereitung in Planung
2. sichtbarer Unsicherheit statt falscher Sicherheit
3. disziplinierten Grenzen zwischen Planung und Implementierung
4. Methodendesign fuer spaetere Ausbauarbeit

## verwandte_oeffentliche_repos

- [`tof_legacy_recovery_workbench`](https://github.com/IMaugrenI/tof-legacy-recovery-workbench) — Recovery_ und Trennungs_Baseline
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — lokaler Builder_Stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on_prem lokales Wissenssystem
