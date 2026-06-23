# Synthetische Sequenz Rekopplung vor Rand Phasenrollen

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig_vorlast | 700 | 0.9857 | 0.0057 | 0.0014 | 0.0071 | 0.7587 | 0.6188 | 0.1202 | 0.0173 | 0.0227 | 0.8387 |
| oeffnung | 700 | 0.9743 | 0.0114 | 0.0014 | 0.0129 | 0.7560 | 0.6145 | 0.1204 | 0.0221 | 0.0287 | 0.8336 |
| bruch_impuls | 700 | 0.8857 | 0.0514 | 0.0014 | 0.0614 | 0.7378 | 0.5808 | 0.1234 | 0.0483 | 0.0692 | 0.8077 |
| rekopplung | 700 | 0.9943 | 0.0043 | 0.0014 | 0.0000 | 0.7585 | 0.6202 | 0.1207 | 0.0210 | 0.0275 | 0.8359 |
| randflackern | 700 | 0.2329 | 0.5486 | 0.0043 | 0.2143 | 0.6946 | 0.5133 | 0.1513 | 0.0945 | 0.1467 | 0.6229 |
| gegenpol | 700 | 0.9643 | 0.0086 | 0.0014 | 0.0257 | 0.7475 | 0.5994 | 0.1201 | 0.0365 | 0.0503 | 0.8200 |
| ruhe_nachhall | 700 | 0.9914 | 0.0057 | 0.0014 | 0.0014 | 0.7595 | 0.6213 | 0.1210 | 0.0191 | 0.0259 | 0.8375 |
| zweiter_kippimpuls | 500 | 0.9820 | 0.0100 | 0.0020 | 0.0060 | 0.7425 | 0.5948 | 0.1264 | 0.0539 | 0.0825 | 0.8024 |
| zweite_rekopplung | 694 | 0.9928 | 0.0058 | 0.0000 | 0.0014 | 0.7583 | 0.6196 | 0.1204 | 0.0210 | 0.0287 | 0.8358 |

## Rollenverteilung
- `ruhig_vorlast`: zentrum_stabil=690, rekopplungsnaehe=5, offene_variante=4, spannungsrand_kippnaehe=1
- `oeffnung`: zentrum_stabil=682, rekopplungsnaehe=9, offene_variante=8, spannungsrand_kippnaehe=1
- `bruch_impuls`: zentrum_stabil=620, rekopplungsnaehe=43, offene_variante=36, spannungsrand_kippnaehe=1
- `rekopplung`: zentrum_stabil=696, offene_variante=3, spannungsrand_kippnaehe=1
- `randflackern`: offene_variante=384, zentrum_stabil=163, rekopplungsnaehe=150, spannungsrand_kippnaehe=3
- `gegenpol`: zentrum_stabil=675, rekopplungsnaehe=18, offene_variante=6, spannungsrand_kippnaehe=1
- `ruhe_nachhall`: zentrum_stabil=694, offene_variante=4, rekopplungsnaehe=1, spannungsrand_kippnaehe=1
- `zweiter_kippimpuls`: zentrum_stabil=491, offene_variante=5, rekopplungsnaehe=3, spannungsrand_kippnaehe=1
- `zweite_rekopplung`: zentrum_stabil=689, offene_variante=4, rekopplungsnaehe=1

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
