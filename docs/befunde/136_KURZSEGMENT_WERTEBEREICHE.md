# Kurzsegment-Wertebereiche

Stand: 2026-06-18 19:11:21

## Zweck

Diese Datei verdichtet die bisherigen Kurzsegment-Befunde.
Sie ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.

Die Wertebereiche sind Arbeitsbefunde aus den bisher geprüften Segmenten.
Sie dürfen nicht als harte Schwellwerte gelesen werden.

## Hierarchie Der Prüfung

1. Grundfrage: Trennen sich lokale Last und lokale Ruhe im MCM-Feld reproduzierbar?
2. Unterprüfung: Welche Wertebereiche zeigen die bisherigen Segmenttypen?
3. Folgeschritt: Weitere Jahre/Welten gegen diese Arbeitsbereiche prüfen.

## Einzelsegmente

| Segment | Lesung | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| stress_segment5 | lastnah | 20 (0.215) | 0.250055 | 0.607085 | 0.351929 | 0.484 | 0.000000 | 0.000000 |
| stress_segment6 | lastnah | 22 (0.237) | 0.241203 | 0.606419 | 0.339007 | 0.538 | 0.000000 | 0.000000 |
| stress_2023_test4 | lastnah | 22 (0.234) | 0.269079 | 0.596927 | 0.338154 | 0.468 | 0.000000 | 0.000000 |
| stress_2024_real1 | last_feldzeitnah | 22 (0.234) | 0.270193 | 0.601652 | 0.356035 | 0.617 | 0.003546 | 0.001599 |
| stress_2025_stress | lastnah | 20 (0.213) | 0.262183 | 0.594327 | 0.329181 | 0.447 | 0.000000 | 0.000000 |
| stress_segment5_6 | last_feldzeitnah | 44 (0.229) | 0.246979 | 0.606201 | 0.345029 | 0.521 | 0.001736 | 0.000194 |
| quiet_2025_core | ruhig_feldzeitnah | 2 (0.021) | 0.175145 | 0.628376 | 0.345272 | 0.436 | 0.001773 | 0.000662 |
| quiet_2026_anchor | ruhig_feldzeitnah | 4 (0.043) | 0.166449 | 0.639974 | 0.370294 | 0.415 | 0.001773 | 0.000518 |
| quiet_2024_real1 | ruhenah | 4 (0.043) | 0.189680 | 0.630744 | 0.362024 | 0.500 | 0.000000 | 0.000000 |
| quiet_2025_stress | ruhenah | 0 (0.000) | 0.176916 | 0.639352 | 0.378478 | 0.500 | 0.000000 | 0.000000 |

## Verdichtete Wertebereiche

| Lesung | Segmente | Memory-Quote | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| last_feldzeitnah | 2 | 0.229167 - 0.234043 | 0.246979 - 0.270193 | 0.601652 - 0.606201 | 0.345029 - 0.356035 | 0.520833 - 0.617021 | 0.001736 - 0.003546 | 0.000194 - 0.001599 |
| lastnah | 4 | 0.212766 - 0.236559 | 0.241203 - 0.269079 | 0.594327 - 0.607085 | 0.329181 - 0.351929 | 0.446809 - 0.537634 | 0.000000 - 0.000000 | 0.000000 - 0.000000 |
| ruhenah | 2 | 0.000000 - 0.042553 | 0.176916 - 0.189680 | 0.630744 - 0.639352 | 0.362024 - 0.378478 | 0.500000 - 0.500000 | 0.000000 - 0.000000 | 0.000000 - 0.000000 |
| ruhig_feldzeitnah | 2 | 0.021277 - 0.042553 | 0.166449 - 0.175145 | 0.628376 - 0.639974 | 0.345272 - 0.370294 | 0.414894 - 0.436170 | 0.001773 - 0.001773 | 0.000518 - 0.000662 |

## Mittelwerte Nach Lesung

| Lesung | Memory-Quote | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |
|---|---:|---:|---:|---:|---:|---:|---:|
| last_feldzeitnah | 0.231605 | 0.258586 | 0.603927 | 0.350532 | 0.568927 | 0.002641 | 0.000897 |
| lastnah | 0.224605 | 0.255630 | 0.601189 | 0.339568 | 0.484100 | 0.000000 | 0.000000 |
| ruhenah | 0.021277 | 0.183298 | 0.635048 | 0.370251 | 0.500000 | 0.000000 | 0.000000 |
| ruhig_feldzeitnah | 0.031915 | 0.170797 | 0.634175 | 0.357783 | 0.425532 | 0.001773 | 0.000590 |

## Befund

Die bisherigen Kurzsegmente trennen sich in vier Arbeitsformen:

- `lastnah`: hohe Memorylast, hoher Strain, schwächere Rekopplung.
- `last_feldzeitnah`: Last bleibt dominant, aber erste Wiederkehr/Nachhall-Spuren treten hinzu.
- `ruhenah`: niedrige Memorylast, niedriger Strain, stärkere Rekopplung ohne deutliche Feldzeitspur.
- `ruhig_feldzeitnah`: niedrige Memorylast, niedriger Strain, stärkere Rekopplung und leichte Feldzeitspur.

Damit wird die passive MCM-Lesung präziser:

```text
Lokale Last ist nicht einfach Bewegung.
Lokale Ruhe ist nicht einfach Stillstand.
Feldzeit ist nicht automatisch Ruhe.
```

## Interpretation

Die bisherige Trennung spricht dafür, dass MINI_DIO lokale Feldreaktionen ausbildet, die nicht direkt aus dem Dateinamen oder einer Einzelmetrik folgen.
Die Lastseite zeigt eine belastete Innenfeldreaktion.
Die Ruheseite zeigt eine tragfähigere Innenfeldreaktion.
Feldzeit kann in beiden Richtungen eingebettet sein.

Das stützt die Arbeitsthese, dass das MCM-Feld Gegenpole nicht als Modul braucht.
Stress, Ruhe, Entlastung und Last werden als Feldwirkung lesbar.

## Begrenzung

Die Datenbasis ist noch klein.
Die Wertebereiche sind keine Schwellwerte.
Neue Segmente können die Bereiche bestätigen, verschieben oder neue Mischformen zeigen.

## Wie es weitergeht

Als nächstes sollte ein weiteres Regime getestet werden.
Ziel: Prüfen, ob `lastnah`, `last_feldzeitnah`, `ruhenah` und `ruhig_feldzeitnah` auch in Seitwärts- oder Expansionswelten getrennt entstehen.
Wenn neue Mischformen auftreten, müssen sie hierarchisch eingeordnet werden: Grundpol, Unterform, danach mögliche Folgeschritte.
