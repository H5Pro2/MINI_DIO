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
| `netz_driftend_getragen` | 33 | 0.666667 | 0.047962 | 0.006937 | `role_stable:16 | role_drifting:14 | role_core_near_retained:3` | `stable_surface:16 | variable_but_carried:10 | gaining_weight:4 | stable_core:3` | `low_drift:19 | explicit_role_drift:14` | Drift bleibt getragen, wenn Rollenbewegung sichtbar ist, aber Rekopplung Strain nicht klar unterliegt. |
| `netz_rekoppelnd_verbunden` | 30 | 1.833333 | 0.029334 | -0.016203 | `role_condensing:22 | -:4 | role_releasing:2 | maturation_reifung:1` | `gaining_weight:22 | -:4 | losing_role_weight:2 | kurze_mehrweltspur:1` | `surface_role_movement:22 | -:4 | role_releasing_or_fading:2 | feld_jung_instabiler_austritt:1` | Rekopplung entsteht, wenn Feldanschluss und Entlastung gemeinsam staerker wirken als Strain. |
| `netz_offen_verbunden` | 29 | 1.827586 | -0.043888 | 0.048462 | `role_condensing:25 | -:4` | `gaining_weight:25 | -:4` | `surface_role_movement:25 | -:4` | Offene Verbindung zeigt Anschluss ohne klare Zentrums- oder Rekopplungsbindung. |
| `netz_rekoppelnd_einzeln` | 26 | 0.0 | 0.0 | 0.0 | `role_releasing:16 | role_condensing:10` | `losing_role_weight:16 | gaining_weight:10` | `role_releasing_or_fading:16 | surface_role_movement:10` | Einzelrekopplung zeigt Entlastung ohne tragendes Nachbarschaftsnetz. |
| `netz_fragmentiert_belastet` | 17 | 3.764706 | -0.061817 | 0.065432 | `role_stable:7 | role_core_near_retained:5 | role_drifting:5` | `stable_surface:7 | stable_core:5 | variable_but_carried:4 | gaining_weight:1` | `low_drift:12 | explicit_role_drift:5` | Fragmentierung wird belastet, wenn Strain und Aussen-/Brueckenriss trotz sichtbarer Kernnaehe hoch bleiben. |
| `netz_zentrum_mit_anschluss` | 6 | 5.0 | 0.023122 | 0.007736 | `role_condensing:4 | role_releasing:1 | role_core_near_retained:1` | `core_near_retained:5 | losing_role_weight:1` | `core_boundary_movement:5 | role_releasing_or_fading:1` | Zentrumsnaehe entsteht, wenn Kern-/Zentrumsqualitaet mit Anschlussnachbarschaft zusammen sichtbar wird. |
| `netz_zentrum_getragen` | 2 | 0.0 | 0.0 | 0.0 | `role_core_near_retained:2` | `core_near_retained:2` | `core_boundary_movement:2` | Bedingung wirkt allgemein zentrumsnah. |

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