# MCM-Rolennetzwerk: Bedingungsdiagnose

## Zweck

Diese Datei prueft passiv, welche gemeinsamen Bedingungen hinter den Netzwerkzustaenden der `dio_net_*` Feldkarte liegen.
Sie beschreibt keine Handlung, kein Gate und keine Strategie.

## Sicherheitsgrenze

- passive Diagnose
- keine Entry-Wirkung
- keine Richtungsvorgabe
- keine Motorik

## Bedingungsmatrix

| Zustand | Knoten | Durchschnitt Nachbarn | Durchschnitt Rekopplung | Durchschnitt Strain | Top Bewegung | Top Stabilitaet | Top Drift | Lesung |
|---|---:|---:|---:|---:|---|---|---|---|
| `netz_offen_verbunden` | 37 | 1.837838 | -0.03861 | 0.046825 | `role_condensing:32 | -:4 | maturation_reifung:1` | `gaining_weight:32 | -:4 | kurze_mehrweltspur:1` | `surface_role_movement:32 | -:4 | feld_jung_instabiler_austritt:1` | Offene Verbindung zeigt Anschluss ohne klare Zentrums- oder Rekopplungsbindung. |
| `netz_rekoppelnd_verbunden` | 32 | 1.6875 | 0.026703 | -0.020958 | `role_condensing:25 | -:4 | role_releasing:2 | maturation_jung_gehalten:1` | `gaining_weight:25 | -:4 | losing_role_weight:2 | segment_nicht_gelesen:1` | `surface_role_movement:25 | -:4 | role_releasing_or_fading:2 | feld_unguelesen:1` | Rekopplung entsteht, wenn Feldanschluss und Entlastung gemeinsam staerker wirken als Strain. |
| `netz_fragmentiert_belastet` | 28 | 3.392857 | -0.058689 | 0.062391 | `role_drifting:12 | role_stable:10 | role_core_near_retained:6` | `stable_surface:10 | variable_but_carried:8 | stable_core:6 | gaining_weight:4` | `low_drift:16 | explicit_role_drift:12` | Fragmentierung wird belastet, wenn Strain und Aussen-/Brueckenriss trotz sichtbarer Kernnaehe hoch bleiben. |
| `netz_driftend_getragen` | 22 | 2.181818 | 0.02395 | -0.014202 | `role_stable:13 | role_drifting:7 | role_core_near_retained:2` | `stable_surface:13 | variable_but_carried:6 | stable_core:2 | gaining_weight:1` | `low_drift:15 | explicit_role_drift:7` | Drift bleibt getragen, wenn Rollenbewegung sichtbar ist, aber Rekopplung Strain nicht klar unterliegt. |
| `netz_rekoppelnd_einzeln` | 16 | 0.0 | 0.0 | 0.0 | `role_releasing:16` | `losing_role_weight:16` | `role_releasing_or_fading:16` | Einzelrekopplung zeigt Entlastung ohne tragendes Nachbarschaftsnetz. |
| `netz_zentrum_mit_anschluss` | 8 | 5.625 | 0.00183 | 0.005805 | `role_condensing:4 | role_core_near_retained:3 | role_releasing:1` | `core_near_retained:7 | losing_role_weight:1` | `core_boundary_movement:7 | role_releasing_or_fading:1` | Zentrumsnaehe entsteht, wenn Kern-/Zentrumsqualitaet mit Anschlussnachbarschaft zusammen sichtbar wird. |

## Interpretation

Die Netzwerkzustaende wirken nicht zufaellig gleichartig.
Sie unterscheiden sich durch Kombinationen aus Nachbarschaft, Rekopplung, Strain, Rollenbewegung, Stabilitaet und Drift.

Damit wird die naechste MCM-Arbeitsfrage konkreter:

```text
Welche Feldbedingungen lassen eine Bedeutung stabil bleiben, wandern, rekoppeln oder fragmentieren?
```

## Grenze

Diese Diagnose bleibt beschreibend.
Sie darf keine harte Regel und keine Handlungsnaehe erzeugen.

## Wie es weitergeht

Als naechstes sollte eine einzelne Klasse, vorzugsweise `netz_fragmentiert_belastet`, gegen ihre Weltsegmente zurueckgelegt werden.
Dann wird sichtbar, ob Fragmentierung durch Weltbruch, Nachbarschaftsriss oder innere Strain-Lage getragen wird.
