# Synthetische Bruch/Rand-Welt - Phasenrollen nach adaptierter Feldkopplung

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig_vorlast | 700 | 0.9857 | 0.0057 | 0.0014 | 0.0071 | 0.7587 | 0.6188 | 0.1202 | 0.0173 | 0.0227 | 0.8387 |
| oeffnung | 700 | 0.9757 | 0.0114 | 0.0014 | 0.0114 | 0.7560 | 0.6146 | 0.1204 | 0.0221 | 0.0287 | 0.8337 |
| bruch_impuls | 700 | 0.8857 | 0.0529 | 0.0000 | 0.0614 | 0.7378 | 0.5809 | 0.1233 | 0.0478 | 0.0684 | 0.8077 |
| randflackern | 700 | 0.2729 | 0.5157 | 0.0014 | 0.2100 | 0.6957 | 0.5155 | 0.1511 | 0.0938 | 0.1454 | 0.6242 |
| gegenpol | 700 | 0.9700 | 0.0114 | 0.0014 | 0.0171 | 0.7477 | 0.6000 | 0.1206 | 0.0368 | 0.0510 | 0.8210 |
| rekopplung | 700 | 0.9914 | 0.0057 | 0.0014 | 0.0014 | 0.7581 | 0.6198 | 0.1207 | 0.0212 | 0.0279 | 0.8355 |
| ruhe_nachhall | 700 | 0.9929 | 0.0029 | 0.0014 | 0.0029 | 0.7598 | 0.6217 | 0.1207 | 0.0187 | 0.0252 | 0.8375 |
| zweiter_kippimpuls | 500 | 0.9820 | 0.0080 | 0.0020 | 0.0080 | 0.7427 | 0.5951 | 0.1264 | 0.0538 | 0.0825 | 0.8027 |
| zweite_rekopplung | 594 | 0.9899 | 0.0051 | 0.0000 | 0.0051 | 0.7578 | 0.6190 | 0.1208 | 0.0225 | 0.0315 | 0.8349 |

## Rollenverteilung
- `ruhig_vorlast`: zentrum_stabil=690, rekopplungsnaehe=5, offene_variante=4, spannungsrand_kippnaehe=1
- `oeffnung`: zentrum_stabil=683, offene_variante=8, rekopplungsnaehe=8, spannungsrand_kippnaehe=1
- `bruch_impuls`: zentrum_stabil=620, rekopplungsnaehe=43, offene_variante=37
- `randflackern`: offene_variante=361, zentrum_stabil=191, rekopplungsnaehe=147, spannungsrand_kippnaehe=1
- `gegenpol`: zentrum_stabil=679, rekopplungsnaehe=12, offene_variante=8, spannungsrand_kippnaehe=1
- `rekopplung`: zentrum_stabil=694, offene_variante=4, rekopplungsnaehe=1, spannungsrand_kippnaehe=1
- `ruhe_nachhall`: zentrum_stabil=695, offene_variante=2, rekopplungsnaehe=2, spannungsrand_kippnaehe=1
- `zweiter_kippimpuls`: zentrum_stabil=491, offene_variante=4, rekopplungsnaehe=4, spannungsrand_kippnaehe=1
- `zweite_rekopplung`: zentrum_stabil=588, offene_variante=3, rekopplungsnaehe=3

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
