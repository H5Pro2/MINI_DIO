# Synthetische Zeitdehnung kompakt Phasenrollen

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig_vorlast | 350 | 0.9514 | 0.0171 | 0.0029 | 0.0286 | 0.7550 | 0.6096 | 0.1204 | 0.0214 | 0.0308 | 0.8361 |
| oeffnung | 350 | 0.9657 | 0.0171 | 0.0029 | 0.0143 | 0.7525 | 0.6067 | 0.1209 | 0.0272 | 0.0386 | 0.8302 |
| bruch_impuls | 350 | 0.7114 | 0.1543 | 0.0000 | 0.1343 | 0.7257 | 0.5555 | 0.1262 | 0.0603 | 0.0930 | 0.7950 |
| randflackern | 350 | 0.1857 | 0.6571 | 0.0000 | 0.1571 | 0.6889 | 0.4999 | 0.1535 | 0.0957 | 0.1493 | 0.6235 |
| gegenpol | 350 | 0.8886 | 0.0457 | 0.0029 | 0.0629 | 0.7397 | 0.5818 | 0.1206 | 0.0452 | 0.0676 | 0.8150 |
| rekopplung | 350 | 0.9829 | 0.0114 | 0.0029 | 0.0029 | 0.7558 | 0.6154 | 0.1218 | 0.0261 | 0.0376 | 0.8335 |
| ruhe_nachhall | 350 | 0.9886 | 0.0057 | 0.0029 | 0.0029 | 0.7581 | 0.6179 | 0.1216 | 0.0234 | 0.0347 | 0.8364 |
| zweiter_kippimpuls | 250 | 0.9200 | 0.0480 | 0.0040 | 0.0280 | 0.7327 | 0.5774 | 0.1314 | 0.0708 | 0.1148 | 0.7844 |
| zweite_rekopplung | 294 | 0.9830 | 0.0102 | 0.0000 | 0.0068 | 0.7554 | 0.6140 | 0.1210 | 0.0268 | 0.0398 | 0.8304 |

## Rollenverteilung
- `ruhig_vorlast`: zentrum_stabil=333, rekopplungsnaehe=10, offene_variante=6, spannungsrand_kippnaehe=1
- `oeffnung`: zentrum_stabil=338, offene_variante=6, rekopplungsnaehe=5, spannungsrand_kippnaehe=1
- `bruch_impuls`: zentrum_stabil=249, offene_variante=54, rekopplungsnaehe=47
- `randflackern`: offene_variante=230, zentrum_stabil=65, rekopplungsnaehe=55
- `gegenpol`: zentrum_stabil=311, rekopplungsnaehe=22, offene_variante=16, spannungsrand_kippnaehe=1
- `rekopplung`: zentrum_stabil=344, offene_variante=4, rekopplungsnaehe=1, spannungsrand_kippnaehe=1
- `ruhe_nachhall`: zentrum_stabil=346, offene_variante=2, rekopplungsnaehe=1, spannungsrand_kippnaehe=1
- `zweiter_kippimpuls`: zentrum_stabil=230, offene_variante=12, rekopplungsnaehe=7, spannungsrand_kippnaehe=1
- `zweite_rekopplung`: zentrum_stabil=289, offene_variante=3, rekopplungsnaehe=2

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
