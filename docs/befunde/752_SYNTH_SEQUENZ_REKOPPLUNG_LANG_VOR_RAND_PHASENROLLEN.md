# Synthetische Sequenz lange Rekopplung vor Rand Phasenrollen

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig_vorlast | 700 | 0.9857 | 0.0057 | 0.0014 | 0.0071 | 0.7587 | 0.6188 | 0.1202 | 0.0173 | 0.0227 | 0.8386 |
| oeffnung | 700 | 0.9657 | 0.0143 | 0.0014 | 0.0186 | 0.7553 | 0.6133 | 0.1203 | 0.0223 | 0.0287 | 0.8331 |
| bruch_impuls | 700 | 0.8700 | 0.0614 | 0.0014 | 0.0671 | 0.7364 | 0.5781 | 0.1235 | 0.0488 | 0.0692 | 0.8042 |
| rekopplung | 2100 | 0.9981 | 0.0014 | 0.0005 | 0.0000 | 0.7596 | 0.6225 | 0.1198 | 0.0177 | 0.0207 | 0.8373 |
| randflackern | 700 | 0.2557 | 0.5371 | 0.0043 | 0.2029 | 0.6931 | 0.5137 | 0.1537 | 0.0968 | 0.1488 | 0.6053 |
| gegenpol | 700 | 0.9700 | 0.0114 | 0.0014 | 0.0171 | 0.7479 | 0.6006 | 0.1205 | 0.0355 | 0.0476 | 0.8183 |
| ruhe_nachhall | 700 | 0.9943 | 0.0043 | 0.0014 | 0.0000 | 0.7597 | 0.6219 | 0.1209 | 0.0191 | 0.0259 | 0.8380 |
| zweiter_kippimpuls | 500 | 0.9860 | 0.0060 | 0.0020 | 0.0060 | 0.7429 | 0.5959 | 0.1264 | 0.0527 | 0.0790 | 0.7994 |
| zweite_rekopplung | 694 | 0.9914 | 0.0058 | 0.0000 | 0.0029 | 0.7590 | 0.6209 | 0.1198 | 0.0189 | 0.0242 | 0.8365 |

## Rollenverteilung
- `ruhig_vorlast`: zentrum_stabil=690, rekopplungsnaehe=5, offene_variante=4, spannungsrand_kippnaehe=1
- `oeffnung`: zentrum_stabil=676, rekopplungsnaehe=13, offene_variante=10, spannungsrand_kippnaehe=1
- `bruch_impuls`: zentrum_stabil=609, rekopplungsnaehe=47, offene_variante=43, spannungsrand_kippnaehe=1
- `rekopplung`: zentrum_stabil=2096, offene_variante=3, spannungsrand_kippnaehe=1
- `randflackern`: offene_variante=376, zentrum_stabil=179, rekopplungsnaehe=142, spannungsrand_kippnaehe=3
- `gegenpol`: zentrum_stabil=679, rekopplungsnaehe=12, offene_variante=8, spannungsrand_kippnaehe=1
- `ruhe_nachhall`: zentrum_stabil=696, offene_variante=3, spannungsrand_kippnaehe=1
- `zweiter_kippimpuls`: zentrum_stabil=493, offene_variante=3, rekopplungsnaehe=3, spannungsrand_kippnaehe=1
- `zweite_rekopplung`: zentrum_stabil=688, offene_variante=4, rekopplungsnaehe=2

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
