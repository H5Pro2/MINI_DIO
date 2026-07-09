# SYNTH Sequenz zufallsnah Phasenrollen

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| zweiter_kippimpuls | 500 | 0.8260 | 0.0660 | 0.0020 | 0.1060 | 0.7337 | 0.5690 | 0.1247 | 0.0521 | 0.0792 | 0.8042 |
| ruhe_nachhall | 700 | 0.9857 | 0.0071 | 0.0014 | 0.0057 | 0.7587 | 0.6199 | 0.1209 | 0.0190 | 0.0259 | 0.8379 |
| oeffnung | 700 | 0.9871 | 0.0086 | 0.0000 | 0.0043 | 0.7567 | 0.6167 | 0.1200 | 0.0209 | 0.0265 | 0.8344 |
| rekopplung | 700 | 0.9986 | 0.0000 | 0.0014 | 0.0000 | 0.7590 | 0.6215 | 0.1204 | 0.0200 | 0.0257 | 0.8367 |
| randflackern | 700 | 0.2643 | 0.5129 | 0.0043 | 0.2186 | 0.6960 | 0.5135 | 0.1513 | 0.0949 | 0.1482 | 0.6283 |
| ruhig_vorlast | 700 | 0.9943 | 0.0043 | 0.0014 | 0.0000 | 0.7598 | 0.6221 | 0.1206 | 0.0183 | 0.0246 | 0.8380 |
| gegenpol | 700 | 0.9600 | 0.0114 | 0.0014 | 0.0271 | 0.7476 | 0.5990 | 0.1202 | 0.0363 | 0.0501 | 0.8220 |
| bruch_impuls | 700 | 0.9829 | 0.0057 | 0.0014 | 0.0100 | 0.7447 | 0.5979 | 0.1243 | 0.0479 | 0.0686 | 0.8076 |
| zweite_rekopplung | 394 | 0.9873 | 0.0076 | 0.0000 | 0.0051 | 0.7559 | 0.6154 | 0.1214 | 0.0269 | 0.0397 | 0.8320 |

## Rollenverteilung
- `zweiter_kippimpuls`: zentrum_stabil=413, rekopplungsnaehe=53, offene_variante=33, spannungsrand_kippnaehe=1
- `ruhe_nachhall`: zentrum_stabil=690, offene_variante=5, rekopplungsnaehe=4, spannungsrand_kippnaehe=1
- `oeffnung`: zentrum_stabil=691, offene_variante=6, rekopplungsnaehe=3
- `rekopplung`: zentrum_stabil=699, spannungsrand_kippnaehe=1
- `randflackern`: offene_variante=359, zentrum_stabil=185, rekopplungsnaehe=153, spannungsrand_kippnaehe=3
- `ruhig_vorlast`: zentrum_stabil=696, offene_variante=3, spannungsrand_kippnaehe=1
- `gegenpol`: zentrum_stabil=672, rekopplungsnaehe=19, offene_variante=8, spannungsrand_kippnaehe=1
- `bruch_impuls`: zentrum_stabil=688, rekopplungsnaehe=7, offene_variante=4, spannungsrand_kippnaehe=1
- `zweite_rekopplung`: zentrum_stabil=389, offene_variante=3, rekopplungsnaehe=2

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
