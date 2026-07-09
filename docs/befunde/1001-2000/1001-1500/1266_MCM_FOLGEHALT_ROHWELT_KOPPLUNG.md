# MCM Folgehalt Rohwelt-Kopplung

Stand: 2026-07-02

## Grundfrage

Welche Rohweltspannung steht vor Folgehalt oder Rueckfall nach Randkontakt?

## Unterpruefung

Diese Diagnose koppelt `1264_MCM_FOLGEHALT_NACH_RANDKONTAKT.csv` mit eindeutig zuordenbaren Rohweltfenstern.

## Eingabe

- Folgehalt: `docs\befunde\1264_MCM_FOLGEHALT_NACH_RANDKONTAKT.csv`
- Rohwelt: gemappte CSV-Dateien aus `data/`

## Profil

- gekoppelte Fenster: `1021`
- ausgelassen: `{'keine_eindeutige_rohwelt': 1941}`
- Folgehalt-Arten: `{'offene_variante_entlastend_gehalten': 740, 'rekopplungsnaehe_entlastend_gehalten': 113, 'zentrum_stabil_entlastend_gehalten': 83, 'offenheit_kurz_getragen_dann_rueckfall': 75, 'zentrum_kurz_getragen_dann_rueckfall': 7, 'offene_variante_gemischt_gehalten': 2, 'rekopplung_kurz_getragen_dann_rueckfall': 1}`
- Rohbewegungen: `{'bewegungsbruch': 1011, 'gemischte_rohwelt': 9, 'bruch_koerperlast': 1}`
- Rohform-Buckets: `{'bewegungsbruch': 699, 'starker_bruchimpuls': 312, 'gemischte_rohwelt': 9, 'koerperlast': 1}`
- Welten: `{'XRP_5M_10K': 162, 'POS_EXPANSION_10K': 157, 'NEG_STRESS_10K': 152, 'DOGE_5M_10K': 139, 'SIDEWAYS_10K': 128, 'PAXG_5M_10K': 87, 'BTC_1H_2K': 46, 'SOL_1H_2K': 45, 'KAS_5M_2K': 37, 'BTC_5M_2K': 34, 'SOL_5M_2K': 34}`

## Folgehalt nach Rohweltprofil

| Folgehalt | Anzahl | Rohbewegung | Rohform | Return | Range | Expansion | Richtung | Delta Rekopplung | Delta Strain |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|
| offene_variante_entlastend_gehalten | 740 | {'bewegungsbruch': 733, 'gemischte_rohwelt': 6, 'bruch_koerperlast': 1} | {'bewegungsbruch': 513, 'starker_bruchimpuls': 220, 'gemischte_rohwelt': 7} | 0.0021 | 0.0473 | 3.8308 | 0.0859 | 0.0748 | -0.0936 |
| rekopplungsnaehe_entlastend_gehalten | 113 | {'bewegungsbruch': 111, 'gemischte_rohwelt': 2} | {'bewegungsbruch': 87, 'starker_bruchimpuls': 24, 'gemischte_rohwelt': 1} | -0.0040 | 0.0323 | 3.6080 | 0.0884 | 0.1063 | -0.1115 |
| zentrum_stabil_entlastend_gehalten | 83 | {'bewegungsbruch': 82, 'gemischte_rohwelt': 1} | {'bewegungsbruch': 57, 'starker_bruchimpuls': 25, 'gemischte_rohwelt': 1} | 0.0013 | 0.0330 | 3.6242 | 0.0871 | 0.1213 | -0.1254 |
| offenheit_kurz_getragen_dann_rueckfall | 75 | {'bewegungsbruch': 75} | {'starker_bruchimpuls': 40, 'bewegungsbruch': 35} | -0.0106 | 0.0792 | 5.5111 | 0.0825 | 0.0704 | -0.0945 |
| zentrum_kurz_getragen_dann_rueckfall | 7 | {'bewegungsbruch': 7} | {'bewegungsbruch': 5, 'starker_bruchimpuls': 2} | 0.0003 | 0.0265 | 3.9900 | 0.0746 | 0.1183 | -0.1247 |
| offene_variante_gemischt_gehalten | 2 | {'bewegungsbruch': 2} | {'bewegungsbruch': 2} | -0.0118 | 0.0172 | 3.5080 | 0.1328 | -0.0134 | -0.0228 |
| rekopplung_kurz_getragen_dann_rueckfall | 1 | {'bewegungsbruch': 1} | {'starker_bruchimpuls': 1} | -0.0081 | 0.0273 | 4.0353 | 0.0462 | 0.1133 | -0.1357 |

## Rohform nach Folgequalitaet

| Rohform | Anzahl | Folgehalt | Return | Range | Expansion | Richtung | Delta Rekopplung | Delta Strain |
|---|---:|---|---:|---:|---:|---:|---:|---:|
| bewegungsbruch | 699 | {'offene_variante_entlastend_gehalten': 513, 'rekopplungsnaehe_entlastend_gehalten': 87, 'zentrum_stabil_entlastend_gehalten': 57, 'offenheit_kurz_getragen_dann_rueckfall': 35} | 0.0025 | 0.0418 | 3.0435 | 0.0858 | 0.0820 | -0.0979 |
| starker_bruchimpuls | 312 | {'offene_variante_entlastend_gehalten': 220, 'offenheit_kurz_getragen_dann_rueckfall': 40, 'zentrum_stabil_entlastend_gehalten': 25, 'rekopplungsnaehe_entlastend_gehalten': 24} | -0.0044 | 0.0572 | 5.9262 | 0.0867 | 0.0819 | -0.0994 |
| gemischte_rohwelt | 9 | {'offene_variante_entlastend_gehalten': 7, 'rekopplungsnaehe_entlastend_gehalten': 1, 'zentrum_stabil_entlastend_gehalten': 1} | 0.0108 | 0.0366 | 1.9138 | 0.0809 | 0.0785 | -0.0942 |
| koerperlast | 1 | {'rekopplungsnaehe_entlastend_gehalten': 1} | -0.0939 | 0.1789 | 1.9994 | 0.0571 | 0.1098 | -0.0999 |

## Befund

Die Rohwelt liefert nicht allein die Bedeutung. Der gleiche Bewegungsbruch kann unterschiedliche Feldfolgen tragen.

Entscheidend ist die Kopplung:

```text
Rohweltspannung -> Randkontakt -> Folgehalt oder Rueckfall
```

Damit wird Folgehalt als Feldantwort auf Weltspannung lesbar, nicht als isolierte Rolle.

## Wie es weitergeht

Als naechstes sollte diese Kopplung nach Asset/Weltart getrennt werden: Bleibt die Feldantwort gleich, wenn sich die Weltmelodie stark unterscheidet?
