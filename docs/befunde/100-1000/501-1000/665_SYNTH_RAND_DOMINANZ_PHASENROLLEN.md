# Synthetische Randdominanz - Phasenrollen

Passive Diagnose: synthetische Weltphase gegen entstehende MCM-Rolle. Die Phasen sind nur Auswertungshilfe, keine Runtime-Regel.

## Phasenmatrix

| Phase | Episoden | Zentrum | Offen | Rand/Kipp | Rekopplungsnähe | Rekopplung | Carry | Strain | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| ruhig_basis | 600 | 0.9817 | 0.0067 | 0.0017 | 0.0100 | 0.7584 | 0.6175 | 0.1206 | 0.0179 | 0.0247 | 0.8384 |
| druckaufbau | 600 | 0.9783 | 0.0117 | 0.0017 | 0.0083 | 0.7569 | 0.6155 | 0.1212 | 0.0213 | 0.0284 | 0.8345 |
| laute_randphase | 800 | 0.0762 | 0.7113 | 0.0600 | 0.1525 | 0.6716 | 0.4859 | 0.1857 | 0.1644 | 0.2779 | 0.5375 |
| asymmetrischer_bruch | 700 | 0.8357 | 0.0871 | 0.0000 | 0.0771 | 0.7286 | 0.5660 | 0.1320 | 0.0751 | 0.1235 | 0.8051 |
| gegenzerrung | 700 | 0.9457 | 0.0229 | 0.0000 | 0.0314 | 0.7481 | 0.5990 | 0.1207 | 0.0334 | 0.0463 | 0.8247 |
| ueberreizter_nachhall | 700 | 0.9029 | 0.0414 | 0.0014 | 0.0543 | 0.7354 | 0.5772 | 0.1277 | 0.0553 | 0.0890 | 0.7771 |
| rekopplungsversuch | 700 | 0.9914 | 0.0043 | 0.0014 | 0.0029 | 0.7594 | 0.6216 | 0.1212 | 0.0196 | 0.0263 | 0.8381 |
| ruhe_restspannung | 600 | 0.9933 | 0.0033 | 0.0017 | 0.0017 | 0.7596 | 0.6207 | 0.1209 | 0.0191 | 0.0267 | 0.8387 |
| zweiter_randstoss | 600 | 0.9383 | 0.0283 | 0.0033 | 0.0300 | 0.7363 | 0.5857 | 0.1330 | 0.0738 | 0.1192 | 0.7990 |
| schluss_rekopplung | 994 | 0.9970 | 0.0030 | 0.0000 | 0.0000 | 0.7599 | 0.6222 | 0.1206 | 0.0176 | 0.0230 | 0.8369 |

## Rollenverteilung
- `ruhig_basis`: zentrum_stabil=589, rekopplungsnaehe=6, offene_variante=4, spannungsrand_kippnaehe=1
- `druckaufbau`: zentrum_stabil=587, offene_variante=7, rekopplungsnaehe=5, spannungsrand_kippnaehe=1
- `laute_randphase`: offene_variante=569, rekopplungsnaehe=122, zentrum_stabil=61, spannungsrand_kippnaehe=48
- `asymmetrischer_bruch`: zentrum_stabil=585, offene_variante=61, rekopplungsnaehe=54
- `gegenzerrung`: zentrum_stabil=662, rekopplungsnaehe=22, offene_variante=16
- `ueberreizter_nachhall`: zentrum_stabil=632, rekopplungsnaehe=38, offene_variante=29, spannungsrand_kippnaehe=1
- `rekopplungsversuch`: zentrum_stabil=694, offene_variante=3, rekopplungsnaehe=2, spannungsrand_kippnaehe=1
- `ruhe_restspannung`: zentrum_stabil=596, offene_variante=2, rekopplungsnaehe=1, spannungsrand_kippnaehe=1
- `zweiter_randstoss`: zentrum_stabil=563, rekopplungsnaehe=18, offene_variante=17, spannungsrand_kippnaehe=2
- `schluss_rekopplung`: zentrum_stabil=991, offene_variante=3

## Befund
Die Diagnose zeigt, ob die synthetisch gesetzten Weltphasen unterschiedliche Innenfeldrollen auslösen oder ob das Feld sie trotz Bruchstruktur zentrumsnah integriert.

Wie es weitergeht: Die Phasenmatrix sollte gegen harmonische und Bruch-/Randwelt verglichen werden, um zu prüfen, ob die Rollenverschiebung wirklich phasengebunden ist.
