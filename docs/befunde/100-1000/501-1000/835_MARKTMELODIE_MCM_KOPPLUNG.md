# 835 - Marktmelodie MCM-Kopplung

## Zweck

Diese Diagnose prueft passiv, ob Klangrollen, Melodiephrasen und DIO-Klangtokens wiederkehrend mit MCM-Innenfeldlagen zusammenfallen.
Sie erzeugt keine Handlung, kein Gate und keine Vorhersage.

Hierarchie:

1. Die Aussenwelt wird als Tonfolge gelesen.
2. Die gleiche Welt wird ueber MINI_DIO als Innenfeldspur gelesen.
3. Beide Spuren werden zeitlich gekoppelt.
4. Geprueft wird nur, ob Klangformen und Innenfeldqualitaeten gemeinsam wiederkehren.

## Quellen

- Melodie: `C:\Users\TV\Desktop\MINI_DIO\docs\befunde\834_MARKTMELODIE_STRESS2024_TONFOLGE.csv`
- Episoden: `C:\Users\TV\Desktop\MINI_DIO\debug\adapted_state_negative_stress_2024_5m_10k\dio_mini_lauf_1\episodes.csv`
- CSV: `C:\Users\TV\Desktop\MINI_DIO\docs\befunde\835_MARKTMELODIE_MCM_KOPPLUNG.csv`
- gekoppelte Frames: `9994`

## Kopplungsrollen

| Rolle | Anzahl |
|---|---:|
| offene_klangkopplung | 550 |
| tragende_klangkopplung | 277 |
| einzelkontakt | 155 |

## Dominante Melodiephrasen

| Phrase | Anzahl | Rolle | MCM-Klasse | Innenlage | Carry | Strain | Rekopplung |
|---|---:|---|---|---|---:|---:|---:|
| `dio_mel_72fe5716` | 67 | tragende_klangkopplung | stabil | inner_effect_stable | 0.5546 | 0.1419 | 0.7171 |
| `dio_mel_3f785ec2` | 47 | offene_klangkopplung | stabil | inner_effect_stable | 0.5341 | 0.1600 | 0.6986 |
| `dio_mel_575716ce` | 42 | offene_klangkopplung | stabil | inner_effect_stable | 0.5334 | 0.1511 | 0.7037 |
| `dio_mel_91af20c6` | 42 | tragende_klangkopplung | stabil | inner_effect_stable | 0.5641 | 0.1314 | 0.7255 |
| `dio_mel_8de7b18c` | 40 | tragende_klangkopplung | stabil | inner_effect_stable | 0.5510 | 0.1418 | 0.7154 |
| `dio_mel_b081f6f1` | 40 | offene_klangkopplung | tragend_unruhig | inner_effect_carried_unrest | 0.5054 | 0.1713 | 0.6800 |
| `dio_mel_30e37a57` | 38 | offene_klangkopplung | stabil | inner_effect_stable | 0.5301 | 0.1452 | 0.7064 |
| `dio_mel_81cba106` | 36 | tragende_klangkopplung | stabil | inner_effect_stable | 0.5573 | 0.1387 | 0.7197 |
| `dio_mel_89120746` | 36 | offene_klangkopplung | stabil | inner_effect_stable | 0.5393 | 0.1547 | 0.7034 |
| `dio_mel_c301dee2` | 36 | offene_klangkopplung | stabil | inner_effect_stable | 0.5300 | 0.1577 | 0.6974 |
| `dio_mel_1442f058` | 35 | offene_klangkopplung | stabil | inner_effect_stable | 0.5300 | 0.1321 | 0.7117 |
| `dio_mel_2c8f7028` | 35 | offene_klangkopplung | stabil | inner_effect_stable | 0.5156 | 0.1675 | 0.6926 |

## Dominante DIO-Klangtokens

| Token | Anzahl | Rolle | Tonrolle | MCM-Klasse | Carry | Strain |
|---|---:|---|---|---|---:|---:|
| `dio_snd_e0b633` | 829 | tragende_klangkopplung | ruheton | stabil | 0.5522 | 0.1422 |
| `dio_snd_81f8fd` | 655 | offene_klangkopplung | bruchton | stabil | 0.5192 | 0.1646 |
| `dio_snd_6d50e5` | 506 | offene_klangkopplung | abdunklungston | stabil | 0.5289 | 0.1561 |
| `dio_snd_41399f` | 440 | offene_klangkopplung | spannungston | stabil | 0.5212 | 0.1606 |
| `dio_snd_83bf3c` | 440 | offene_klangkopplung | aufhellungston | stabil | 0.5323 | 0.1517 |
| `dio_snd_7caa8e` | 414 | offene_klangkopplung | bruchton | tragend_unruhig | 0.4619 | 0.2099 |
| `dio_snd_c7c2a7` | 403 | offene_klangkopplung | ruheton | stabil | 0.5479 | 0.1450 |
| `dio_snd_a1b960` | 398 | offene_klangkopplung | abdunklungston | stabil | 0.5461 | 0.1454 |
| `dio_snd_219ecb` | 390 | offene_klangkopplung | aufhellungston | stabil | 0.5467 | 0.1462 |
| `dio_snd_aa59b3` | 376 | tragende_klangkopplung | trageton | stabil | 0.5536 | 0.1460 |
| `dio_snd_41484d` | 370 | offene_klangkopplung | aufhellungston | stabil | 0.5369 | 0.1465 |
| `dio_snd_0f4138` | 368 | offene_klangkopplung | abdunklungston | stabil | 0.5398 | 0.1511 |

## Klangrollen gegen MCM-Feld

| Klangrolle | Anzahl | Rolle | MCM-Klasse | Innenlage | Carry | Strain | Rekopplung |
|---|---:|---|---|---|---:|---:|---:|
| aufhellungston | 2188 | offene_klangkopplung | stabil | inner_effect_stable | 0.5384 | 0.1484 | 0.7073 |
| abdunklungston | 2166 | offene_klangkopplung | stabil | inner_effect_stable | 0.5383 | 0.1510 | 0.7059 |
| trageton | 2031 | tragende_klangkopplung | stabil | inner_effect_stable | 0.5529 | 0.1458 | 0.7158 |
| bruchton | 1543 | offene_klangkopplung | stabil | inner_effect_stable | 0.5049 | 0.1764 | 0.6833 |
| ruheton | 1499 | tragende_klangkopplung | stabil | inner_effect_stable | 0.5524 | 0.1421 | 0.7163 |
| spannungston | 567 | offene_klangkopplung | stabil | inner_effect_stable | 0.5175 | 0.1635 | 0.6934 |

## Befund

Die Marktmelodie koppelt in dieser Diagnose nicht direkt in das MCM-Feld, sondern wird neben die bereits entstandene Innenfeldspur gelegt.
Damit wird sichtbar, ob ein Klangmuster nur akustische Oberflaeche bleibt oder wiederholt in aehnlicher Feldwirkung erscheint.

Wenn eine Melodiephrase wiederkehrend mit hoher Carry-Qualitaet und Rekopplung erscheint, ist das ein Hinweis auf eine tragende Klangnaehe.
Wenn sie mit erhoehter Strain-Qualitaet erscheint, ist das ein Hinweis auf belastete Klangnaehe.
Offene Kopplungen bleiben beobachtbar, ohne sofort Bedeutung zu erzwingen.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese Klangkopplungen in einer anderen Welt wieder auftauchen oder ob sie nur situationsgebundene Klang-Innenfeld-Inseln dieser Stresswelt sind.
