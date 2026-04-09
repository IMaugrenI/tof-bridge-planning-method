# tof-bridge-planning-method

> Die englische Hauptfassung liegt in `README.md`.

Öffentliche Planungs-Baseline, um vorbereitete Bausteine in Skizzen und Zielkandidaten weiterzuführen, ohne Runtime-Wahrheit zu behaupten.

Ich nutze dieses Repo, um zu zeigen, wie vorbereitete Materialien in einem strukturierten Planungsraum weitergeführt werden können, ohne dass Planung aus Versehen zu Implementierung wird.

## Warum dieses Repo öffentlich ist

Ich habe dieses Repo öffentlich gemacht, weil zwischen Recovery und Umsetzung ein eigener, disziplinierter Brückenraum gehört.

Ich will nicht direkt von altem Material in neue Runtime springen. Ich will eine echte Zwischenebene, in der klar wird, was übernommen, übersetzt oder verworfen wird.

Dieses Repo ist kein Hauptprodukt-Repo. Es ist ein Method-Repo, das zeigt, wie ich über Architektur und Übergänge nachdenke.

## Einstieg

### lokal

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

## Was dieses Repo macht

1. startet mit vorbereiteten Bausteinen
2. erzeugt Skizzen und Kandidatensets
3. hält Unsicherheit sichtbar
4. markiert Zielkandidaten als Planungsobjekte, nicht als Umsetzungswahrheit
5. verhindert stillschweigende Freigabe von Planung in Runtime

## Warum das wichtig ist

1. Planung und Runtime-Wahrheit sind nicht dasselbe
2. vorbereitete Materialien brauchen oft mehrere offene Richtungen
3. Zielkandidaten brauchen Review vor der Umsetzung
4. Planungsdisziplin verhindert versteckte Freigabepfade

## Planungskette

1. `00_prepared_blocks/` = vorbereitete Bausteine
2. `01_sketches/` = grobe Skizzen pro Baustein
3. `02_candidate_sets/` = Zielkandidaten-Bündel
4. `03_reports/` = Zusammenfassung und Abnahme

## Für Arbeitgeber

Dieses Repo ist nützlich, wenn du sehen willst, wie ich mit Folgendem umgehe:

1. strukturierter Fortführung von Vorbereitung in Planung
2. sichtbarer Unsicherheit statt falscher Sicherheit
3. disziplinierten Grenzen zwischen Planung und Umsetzung
4. Methodik-Design für späteren Ausbau

## Verwandte öffentliche Repos

- [`tof-legacy-recovery-workbench`](https://github.com/IMaugrenI/tof-legacy-recovery-workbench) — Recovery- und Trennungs-Baseline
- [`tof_local_builder`](https://github.com/IMaugrenI/tof_local_builder) — lokaler Builder-Stack
- [`tof_local_knowledge`](https://github.com/IMaugrenI/tof_local_knowledge) — on-prem lokales Wissenssystem
