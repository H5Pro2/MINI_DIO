# 836 - Marktmelodie WAV Debug

## Zweck

Dieser Bericht erzeugt eine hoerbare WAV-Datei aus der passiven Marktmelodie.
Die WAV-Datei ist ein Debug-Artefakt fuer menschliches Anhoeren, keine Handlung, kein Gate und keine direkte MCM-Feldwirkung.

Kette:

1. Welt wurde bereits in eine Marktmelodie uebersetzt.
2. Die Melodie wird als Mono-WAV gerendert.
3. Tonhoehe, Lautstaerke, Rauigkeit und Klangrolle werden hoerbar gemacht.

## Quelle

- Melodie-CSV: `C:\Users\TV\Desktop\MINI_DIO\docs\befunde\834_MARKTMELODIE_STRESS2024_TONFOLGE.csv`
- WAV: `C:\Users\TV\Desktop\MINI_DIO\docs\audio\836_MARKTMELODIE_STRESS2024.wav`

## Audio-Daten

| Wert | Ergebnis |
|---|---:|
| Frames | 10000 |
| Sample Rate | 22050 Hz |
| Sekunden pro Frame | 0.0250 |
| Dauer | 249.89 s |
| Peak | 0.5766 |

## Klangrollen

| Rolle | Anzahl |
|---|---:|
| aufhellungston | 2189 |
| abdunklungston | 2168 |
| trageton | 2033 |
| bruchton | 1543 |
| ruheton | 1500 |
| spannungston | 567 |

## Dominante Klangtokens

| Token | Anzahl |
|---|---:|
| `dio_snd_e0b633` | 830 |
| `dio_snd_81f8fd` | 655 |
| `dio_snd_6d50e5` | 506 |
| `dio_snd_83bf3c` | 441 |
| `dio_snd_41399f` | 440 |
| `dio_snd_7caa8e` | 414 |
| `dio_snd_c7c2a7` | 403 |
| `dio_snd_a1b960` | 399 |
| `dio_snd_219ecb` | 390 |
| `dio_snd_aa59b3` | 376 |
| `dio_snd_41484d` | 370 |
| `dio_snd_0f4138` | 368 |

## Befund

Die WAV-Ausgabe macht die energetische Weltspur auditiv pruefbar.
Sie ersetzt nicht die CSV-Diagnose, sondern hilft zu hoeren, ob die Welt eher ruhig, bruechig, gespannt oder tragend wirkt.

## Wie es weitergeht

Als naechstes sollte eine zweite Welt als WAV gerendert werden. Dann kann geprueft werden, ob sich unterschiedliche Welten auch akustisch klar unterscheiden.
