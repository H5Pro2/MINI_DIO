# Synthetische Randdominanz - Phasenrollen nach adaptierter Feldkopplung

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig_basis | 600 | 0.9783 | 0.0083 | 0.0017 | 0.0117 | 0.7585 | 0.6174 | 0.1202 | 0.0179 | 0.0247 | 0.8384 |
| druckaufbau | 600 | 0.9767 | 0.0117 | 0.0017 | 0.0100 | 0.7571 | 0.6157 | 0.1207 | 0.0213 | 0.0284 | 0.8345 |
| laute_randphase | 800 | 0.0650 | 0.7612 | 0.0288 | 0.1450 | 0.6729 | 0.4874 | 0.1792 | 0.1644 | 0.2779 | 0.5375 |
| asymmetrischer_bruch | 700 | 0.8429 | 0.0786 | 0.0000 | 0.0786 | 0.7294 | 0.5673 | 0.1298 | 0.0751 | 0.1235 | 0.8051 |
| gegenzerrung | 700 | 0.9471 | 0.0214 | 0.0000 | 0.0314 | 0.7484 | 0.5996 | 0.1199 | 0.0334 | 0.0463 | 0.8247 |
| ueberreizter_nachhall | 700 | 0.9100 | 0.0357 | 0.0014 | 0.0529 | 0.7362 | 0.5792 | 0.1268 | 0.0553 | 0.0890 | 0.7771 |
| rekopplungsversuch | 700 | 0.9929 | 0.0043 | 0.0014 | 0.0014 | 0.7595 | 0.6217 | 0.1208 | 0.0196 | 0.0263 | 0.8381 |
| ruhe_restspannung | 600 | 0.9950 | 0.0033 | 0.0017 | 0.0000 | 0.7597 | 0.6209 | 0.1205 | 0.0191 | 0.0267 | 0.8387 |
| zweiter_randstoss | 600 | 0.9500 | 0.0233 | 0.0033 | 0.0233 | 0.7370 | 0.5870 | 0.1311 | 0.0738 | 0.1192 | 0.7990 |
| schluss_rekopplung | 994 | 0.9970 | 0.0030 | 0.0000 | 0.0000 | 0.7600 | 0.6224 | 0.1202 | 0.0176 | 0.0230 | 0.8369 |

## Rollenverteilung
- `ruhig_basis`: zentrum_stabil=587, rekopplungsnaehe=7, offene_variante=5, spannungsrand_kippnaehe=1
- `druckaufbau`: zentrum_stabil=586, offene_variante=7, rekopplungsnaehe=6, spannungsrand_kippnaehe=1
- `laute_randphase`: offene_variante=609, rekopplungsnaehe=116, zentrum_stabil=52, spannungsrand_kippnaehe=23
- `asymmetrischer_bruch`: zentrum_stabil=590, offene_variante=55, rekopplungsnaehe=55
- `gegenzerrung`: zentrum_stabil=663, rekopplungsnaehe=22, offene_variante=15
- `ueberreizter_nachhall`: zentrum_stabil=637, rekopplungsnaehe=37, offene_variante=25, spannungsrand_kippnaehe=1
- `rekopplungsversuch`: zentrum_stabil=695, offene_variante=3, rekopplungsnaehe=1, spannungsrand_kippnaehe=1
- `ruhe_restspannung`: zentrum_stabil=597, offene_variante=2, spannungsrand_kippnaehe=1
- `zweiter_randstoss`: zentrum_stabil=570, offene_variante=14, rekopplungsnaehe=14, spannungsrand_kippnaehe=2
- `schluss_rekopplung`: zentrum_stabil=991, offene_variante=3

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
