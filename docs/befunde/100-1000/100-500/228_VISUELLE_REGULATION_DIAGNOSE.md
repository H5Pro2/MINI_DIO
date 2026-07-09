# Visuelle Regulation - Diagnose

Stand: 2026-06-19 06:36:42

## Zweck

Diese Diagnose liest die Sehspur von MINI_DIO als passive visuelle Regulation.
Sie prueft, ob Formfluss, Formstabilitaet, Formwechsel und visueller Feldabstand getrennt lesbar sind.

Wichtig: Das ist keine Handlung, kein Gate und kein Entry-Signal.

Hierarchie der Pruefung:

1. Grundfrage: Kann MINI_DIO Form sehen, ohne sie direkt als Feldwirkung oder Handlung zu behandeln?
2. Unterpruefung: visuelles Rauschen, genaueres Ansehen, Hintergrund, stabile Form, Alarmform und Abklingen lesen.
3. Folgeschritt: visuelle Zustaende gegen MCM-Feldlast und Rekopplung legen.

## Einzelwerte

| Welt | Gruppe | Rolle | dominanter Sehzustand | Bewegung | Wechsel | Stabilitaet | Visueller Gap | Fokus | Rauschen | Alarm | Hintergrund | Nachbild | Rekopplung | Feldlast |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | referenz | reiz_aktiv_rekoppelnd | visuelles_rauschen_filtern | 0.2854 | 0.3380 | 0.3725 | 0.0900 | 0.2521 | 0.4604 | 0.2916 | 0.6597 | 0.0005 | 0.622776 | 0.0527 |
| SOL_2025_5M | referenz | reiz_aktiv_rekoppelnd | form_hintergrund_halten | 0.1382 | 0.1652 | 0.3523 | 0.0852 | 0.1637 | 0.4483 | 0.2109 | 0.7431 | 0.0019 | 0.636504 | 0.0140 |
| STRESS_2023_TEST4 | stress | last_memory_bindend | visuelles_rauschen_filtern | 0.5143 | 0.6349 | 0.3493 | 0.0938 | 0.3861 | 0.5055 | 0.4342 | 0.5093 | 0.0000 | 0.596927 | 0.2660 |
| STRESS_2024_REAL | stress | uebergang_bindend | visuelles_rauschen_filtern | 0.5317 | 0.5751 | 0.4450 | 0.1105 | 0.3955 | 0.4557 | 0.4070 | 0.5424 | 0.0016 | 0.601652 | 0.2340 |
| STRESS_2025_STRESS | stress | last_memory_bindend | visuelles_rauschen_filtern | 0.4996 | 0.5879 | 0.3067 | 0.1008 | 0.3620 | 0.5127 | 0.4250 | 0.5152 | 0.0000 | 0.594327 | 0.2872 |
| SOL_2024_1H | vergleich | last_memory_bindend | visuelles_rauschen_filtern | 0.6140 | 0.6764 | 0.3419 | 0.1085 | 0.4226 | 0.5039 | 0.4704 | 0.4679 | 0.0006 | 0.587027 | 0.3159 |
| SOL_2024_30M | vergleich | uebergang_bindend | visuelles_rauschen_filtern | 0.4819 | 0.5601 | 0.3522 | 0.1029 | 0.3595 | 0.4927 | 0.4062 | 0.5382 | 0.0004 | 0.600205 | 0.1830 |
| SOL_2025_1H | vergleich | last_memory_bindend | visuelles_rauschen_filtern | 0.6033 | 0.6522 | 0.3500 | 0.1088 | 0.4149 | 0.4968 | 0.4593 | 0.4796 | 0.0007 | 0.589067 | 0.2944 |
| SOL_2025_30M | vergleich | uebergang_bindend | visuelles_rauschen_filtern | 0.4932 | 0.5474 | 0.3613 | 0.0985 | 0.3597 | 0.4832 | 0.4007 | 0.5425 | 0.0003 | 0.600912 | 0.2016 |

## Sehzustandsanteile

| Welt | genauer ansehen | Alarmform | stabil tragen | Hintergrund | Rauschen filtern | Form abklingen |
|---|---:|---:|---:|---:|---:|---:|
| SOL_2024_5M | 0.0110 | 0.0150 | 0.0973 | 0.3932 | 0.4835 | 0.0000 |
| SOL_2025_5M | 0.0015 | 0.0000 | 0.1008 | 0.6505 | 0.2472 | 0.0000 |
| STRESS_2023_TEST4 | 0.1277 | 0.1277 | 0.0426 | 0.1489 | 0.5532 | 0.0000 |
| STRESS_2024_REAL | 0.0745 | 0.1170 | 0.0957 | 0.1809 | 0.5319 | 0.0000 |
| STRESS_2025_STRESS | 0.1064 | 0.1596 | 0.0319 | 0.1915 | 0.5106 | 0.0000 |
| SOL_2024_1H | 0.1259 | 0.1906 | 0.0466 | 0.0938 | 0.5431 | 0.0000 |
| SOL_2024_30M | 0.0843 | 0.0938 | 0.0537 | 0.1725 | 0.5958 | 0.0000 |
| SOL_2025_1H | 0.1194 | 0.1740 | 0.0451 | 0.1048 | 0.5567 | 0.0000 |
| SOL_2025_30M | 0.0757 | 0.1013 | 0.0687 | 0.1830 | 0.5712 | 0.0000 |

## Lesart

- `form_genauer_ansehen`: Formwechsel, Bewegung oder Gap brauchen feinere visuelle Betrachtung.
- `visuelle_alarmform`: Formwechsel und Feldabstand liegen nahe an Kippnaehe.
- `form_stabil_tragen`: Form bleibt stabil und nah am Feld.
- `form_hintergrund_halten`: Form bleibt sichtbar, ohne Vordergrund zu werden.
- `visuelles_rauschen_filtern`: visuelle Unruhe wird nicht strukturtragend gemacht.
- `form_abklingen_lassen`: ein visuelles Nachbild darf auslaufen.

## Vorlaeufiger Befund

Sehen sollte als eigene Sinnesregulation gelesen werden.
Form darf sichtbar sein, ohne sofort Feldbedeutung oder Handlung zu werden.

## Wie es weitergeht

Als naechstes wird der Befund geschrieben.
Dort wird geprueft, ob SOL 5m visuell anders getragen wird als SOL 30m/1h und Stresssegmente.
