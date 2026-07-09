# Synthetische Randdominanz-Zeitdehnung kompakt Phasenrollen

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig_basis | 300 | 0.9567 | 0.0167 | 0.0033 | 0.0233 | 0.7545 | 0.6068 | 0.1195 | 0.0223 | 0.0339 | 0.8389 |
| druckaufbau | 300 | 0.9367 | 0.0267 | 0.0033 | 0.0333 | 0.7532 | 0.6068 | 0.1213 | 0.0264 | 0.0382 | 0.8307 |
| laute_randphase | 400 | 0.0275 | 0.8325 | 0.0375 | 0.1025 | 0.6664 | 0.4716 | 0.1809 | 0.1663 | 0.2816 | 0.5414 |
| asymmetrischer_bruch | 350 | 0.6143 | 0.2200 | 0.0000 | 0.1657 | 0.7151 | 0.5394 | 0.1358 | 0.0961 | 0.1653 | 0.7934 |
| gegenzerrung | 350 | 0.8686 | 0.0486 | 0.0000 | 0.0829 | 0.7415 | 0.5837 | 0.1202 | 0.0400 | 0.0599 | 0.8182 |
| ueberreizter_nachhall | 350 | 0.8743 | 0.0457 | 0.0029 | 0.0771 | 0.7338 | 0.5735 | 0.1271 | 0.0563 | 0.0912 | 0.7768 |
| rekopplungsversuch | 350 | 0.9886 | 0.0086 | 0.0029 | 0.0000 | 0.7562 | 0.6150 | 0.1215 | 0.0260 | 0.0387 | 0.8330 |
| ruhe_restspannung | 300 | 0.9867 | 0.0067 | 0.0033 | 0.0033 | 0.7574 | 0.6158 | 0.1214 | 0.0252 | 0.0387 | 0.8368 |
| zweiter_randstoss | 300 | 0.8400 | 0.1100 | 0.0100 | 0.0400 | 0.7248 | 0.5653 | 0.1383 | 0.0969 | 0.1639 | 0.7826 |
| schluss_rekopplung | 294 | 0.9898 | 0.0102 | 0.0000 | 0.0000 | 0.7562 | 0.6146 | 0.1209 | 0.0270 | 0.0413 | 0.8334 |

## Rollenverteilung
- `ruhig_basis`: zentrum_stabil=287, rekopplungsnaehe=7, offene_variante=5, spannungsrand_kippnaehe=1
- `druckaufbau`: zentrum_stabil=281, rekopplungsnaehe=10, offene_variante=8, spannungsrand_kippnaehe=1
- `laute_randphase`: offene_variante=333, rekopplungsnaehe=41, spannungsrand_kippnaehe=15, zentrum_stabil=11
- `asymmetrischer_bruch`: zentrum_stabil=215, offene_variante=77, rekopplungsnaehe=58
- `gegenzerrung`: zentrum_stabil=304, rekopplungsnaehe=29, offene_variante=17
- `ueberreizter_nachhall`: zentrum_stabil=306, rekopplungsnaehe=27, offene_variante=16, spannungsrand_kippnaehe=1
- `rekopplungsversuch`: zentrum_stabil=346, offene_variante=3, spannungsrand_kippnaehe=1
- `ruhe_restspannung`: zentrum_stabil=296, offene_variante=2, rekopplungsnaehe=1, spannungsrand_kippnaehe=1
- `zweiter_randstoss`: zentrum_stabil=252, offene_variante=33, rekopplungsnaehe=12, spannungsrand_kippnaehe=3
- `schluss_rekopplung`: zentrum_stabil=291, offene_variante=3

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
