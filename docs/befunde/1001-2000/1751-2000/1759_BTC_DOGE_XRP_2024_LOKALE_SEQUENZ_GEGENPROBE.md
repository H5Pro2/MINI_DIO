# BTC/DOGE/XRP 2024: lokale Sequenz-Gegenprobe

Stand: 2026-07-08

## Grundfrage

Nach der 2025-Sequenzmatrix war die nächste Frage:

```text
Bleibt die Trennung zwischen `verteilt_offen` und `verteilt_rekoppelnd`
auch in einem anderen Jahr sichtbar?
```

## Unterprüfung

Geprüft wurden vorhandene 1000er-Fenster aus 2024:

```text
BTC 2024 5m
DOGE 2024 5m
XRP 2024 5m
```

Fenster:

```text
5000-6000 -> 6000-7000
6000-7000 -> 7000-8000
7000-8000 -> 8000-9000
8000-9000 -> 9000-10000
```

Reports:

```text
reports/btc_doge_xrp_2024_lokale_realsleepreal_sequenz.md
reports/btc_doge_xrp_2024_lokale_realsleepreal_sequenz.csv
reports/btc_doge_xrp_2024_sequence_rawworld_contrast.md
reports/btc_doge_xrp_2024_sequence_rawworld_contrast_groups.csv
```

## Sequenzmatrix

| Anschluss | BTC | DOGE | XRP |
|---|---|---|---|
| 5000-6000 -> 6000-7000 | verteilt_offen | verteilt_offen | mittlere_uebergangsphase |
| 6000-7000 -> 7000-8000 | verteilt_offen | mittlere_uebergangsphase | verteilt_offen |
| 7000-8000 -> 8000-9000 | verteilt_offen | verteilt_offen | verteilt_offen |
| 8000-9000 -> 9000-10000 | verteilt_offen | verteilt_offen | verteilt_offen |

## Klassenmittel

| Klasse | n | Rollen | Kombis | Rekopplung | Nachhall | Basis-Energie | Folge-Energie | Delta Energie |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| mittlere_uebergangsphase | 2 | 3.50 | 4.50 | 0.6890 | 0.2934 | 2.7319 | 2.1861 | -0.5458 |
| verteilt_offen | 10 | 6.40 | 15.40 | 0.6905 | 0.3002 | 2.2472 | 2.0477 | -0.1994 |

## Befund

In dieser 2024-Gegenprobe tritt `verteilt_rekoppelnd` nicht auf. Die lokale Sequenz besteht fast vollständig aus `verteilt_offen`, mit zwei mittleren Übergangsphasen.

Das schärft den 2025-Befund:

```text
Rollenbreite allein erzeugt nicht automatisch `verteilt_rekoppelnd`.
```

2024 zeigt breite Rollenöffnung ohne die starke rekoppelnde Breite, die PAXG 2025 mehrfach zeigte.

## Deutung

`verteilt_rekoppelnd` wird damit vorerst als besondere Milieubindung lesbar:

```text
Breite Rollenbildung + höhere Rekopplung + stärkerer Nachhall
```

`verteilt_offen` bleibt die häufigere offene Rollenbreite:

```text
Breite Rollenbildung + normale Rekopplung + schwächerer Nachhall
```

Damit gewinnt die Unterscheidung methodisch an Wert. Sie ist nicht nur ein anderes Wort für viele Rollen.

## Grenze

Diese Gegenprobe enthält BTC, DOGE und XRP 2024, aber kein PAXG 2024. Die PAXG-Frage bleibt offen:

```text
Ist PAXG 2025 rekoppelnd besonders,
oder zeigt PAXG 2024 eine ähnliche rekoppelnde Breite?
```

## Folgeschritt

Als nächstes sollte PAXG 2024 mit derselben Vier-Fenster-Logik ergänzt werden. Das ist die direkte Kontrolle für die PAXG-2025-Rekopplungslesung.
