# 1751 - XRP/DOGE 2025 lokale Real-Sleep-Real-Gegenprüfung

Stand: 2026-07-08

## Zweck

Nach der Teilfensterprüfung aus [1750_XRP_DOGE_2025_TEILFENSTER_MEHRROLLEN.md](../1501-1750/1750_XRP_DOGE_2025_TEILFENSTER_MEHRROLLEN.md) wurde die nächste Frage geprüft:

```text
Bildet XRP lokal mehr Cross-State-Reaktivierung
oder entsteht die frühere Übergangsphase erst aus dem 5000er-Gesamtkontext?
```

Verglichen wurden zwei starke lokale Kandidaten mit natürlichem Folgefenster:

- `XRP_2025_FOLLOW 0-1000`
- `DOGE_2025_FOLLOW 0-1000`

Der absolut stärkste DOGE-Kandidat lag bei `4000-5000`, hatte innerhalb der 10k-Datei aber kein natürliches Folgefenster mehr. Deshalb wurde für die saubere Real-Sleep-Real-Prüfung der stärkste DOGE-Kandidat mit direkter Folgewelt gewählt.

## Ergebnis

| Welt | Achsenklasse | Breite | Rollen | Kombinationen | Cross-State | Same-State | Reaktivierung | Kombinationsquote | Nachhall |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| XRP 2025 lokal | `verteilt_offen` | verteilt | 6 | 15 | 9 | 6 | 0.6667 | 0.4000 | 0.3101 |
| DOGE 2025 lokal | `mittlere_uebergangsphase` | mittel | 4 | 6 | 4 | 2 | 0.5000 | 0.1667 | 0.3039 |

## Befund

XRP 2025 bildet im geprüften lokalen Kandidaten mehr:

- Rollen,
- Kombinationen,
- Cross-State-Verbindungen,
- voll reaktivierte Kombinationsqualität,
- adaptive Erfahrung.

DOGE 2025 bleibt nicht einrollig. Auch DOGE bildet lokal eine mittlere Übergangsphase. XRP geht in diesem lokalen Vergleich aber eine Stufe weiter: `verteilt_offen`.

## Lesung

Die vorherige 5000er-Lesung wird dadurch geschärft:

```text
DOGE:
  lokal mehrrollenfähig,
  aber im längeren Kontext kompakter gebunden.

XRP:
  lokal stärker verteilt,
  mit mehr Cross-State-Kombinationen,
  dadurch mehr offene Rollenvernetzung.
```

Damit ist die XRP-Übergangsbreite nicht nur ein Artefakt des 5000er-Gesamtkontexts. Sie kann auch lokal sichtbar werden, wenn die Teilwelt als eigene Real-Sleep-Real-Kette gelesen wird.

## Bedeutung für die MCM-Lesung

Die MCM-Topologie bleibt weiterhin zentrumsnah stabil. Was sich ändert, ist die Art der Rollenvernetzung:

```text
Zentrum bleibt erhalten.
Rollenbreite nimmt zu.
Cross-State-Verbindungen nehmen zu.
Nachhall und Erfahrung tragen die Verteilung mit.
```

Das passt zur bisherigen Lesung:

- Topologie ist robuster als lokale Weltfärbung.
- Übergangsphasen sind keine Kollapsform.
- Verteilte Offenheit kann aus lokaler Weltphase plus Offline-/Folgewelt-Reaktivierung entstehen.

## Zugehörige Prüfdateien

Daten:

- `data/xrp_2025_follow_candidate_5000_6000.csv`
- `data/xrp_2025_follow_candidate_6000_7000.csv`
- `data/doge_2025_follow_candidate_5000_6000.csv`
- `data/doge_2025_follow_candidate_6000_7000.csv`

Reports:

- [xrp_doge_2025_lokale_realsleepreal_achsen.md](../../../../reports/xrp_doge_2025_lokale_realsleepreal_achsen.md)

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob ein zweites XRP-Teilfenster ebenfalls `verteilt_offen` wird oder ob diese lokale Offenverteilung nur an `XRP_2025_FOLLOW 0-1000` hängt.
