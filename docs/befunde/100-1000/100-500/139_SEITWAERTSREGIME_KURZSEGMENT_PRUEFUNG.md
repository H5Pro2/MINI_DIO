# Seitwärtsregime: Kurzsegment-Prüfung

Stand: 2026-06-18

## Zweck

Diese Diagnose prüft ein anderes Regime als Stress: eine moderate Seitwärtswelt.

Geprüft wurde:

- ein automatisch extrahiertes aktiveres Seitwärtsfenster aus `kontrolliert_2024_moderate_sideways_10k_5m_SOLUSDT.csv`
- ein automatisch extrahiertes ruhiges Seitwärtsfenster aus derselben Welt

Die Diagnose ist passiv: keine Runtime-Regel, kein Gate, keine Handlungsvorgabe.

## Hierarchie Der Prüfung

1. Grundfrage: Bleiben die vier Kurzsegment-Arbeitsformen in einem Seitwärtsregime stabil?
2. Unterprüfung: Wird das aktivste lokale Seitwärtsfenster als Last, Ruhe oder Mischform gelesen?
3. Folgeschritt: Prüfen, ob Expansionswelten eine neue Klasse oder dieselben vier Formen erzeugen.

## Rohwelt-Extraktion

Aktiveres Seitwärtsfenster:

- Quelle: `kontrolliert_2024_moderate_sideways_10k_5m_SOLUSDT.csv`
- Bereich: Zeile 1075 bis 1175
- `stress_score`: 0.913881
- `avg_abs_return`: 0.002264
- `avg_range`: 0.004247
- `max_abs_return`: 0.031413
- `max_drawdown`: 0.069951
- `drift`: -0.025267

Ruhiges Seitwärtsfenster:

- Quelle: `kontrolliert_2024_moderate_sideways_10k_5m_SOLUSDT.csv`
- Bereich: Zeile 4325 bis 4425
- `quiet_score`: 0.294118
- `avg_abs_return`: 0.000559
- `avg_range`: 0.000980
- `max_abs_return`: 0.002619
- `max_drawdown`: 0.010518
- `drift`: -0.009294

## Segmentvergleich

| Segment | Lesung | Episoden | Memory | Strain | Rekopplung | Carry | Feldwechsel | Wiederkehr | Nachhall |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| sideways_2024_active | ruhig_feldzeitnah | 94 | 4 (0.043) | 0.202000 | 0.629551 | 0.369655 | 0.436 | 0.001773 | 0.000701 |
| sideways_2024_quiet | ruhig_feldzeitnah | 94 | 4 (0.043) | 0.160006 | 0.639653 | 0.365178 | 0.415 | 0.005319 | 0.001010 |

## Befund

Beide Seitwärtsfenster werden `ruhig_feldzeitnah` gelesen.

Das ist fachlich relevant:

- Das aktivere Seitwärtsfenster wird nicht `lastnah`.
- Es hat zwar mehr Strain als das ruhige Seitwärtsfenster.
- Trotzdem bleibt Rekopplung hoch.
- Memorylast bleibt niedrig.
- Wiederkehr/Nachhall ist sichtbar.

Damit entsteht keine neue Lastklasse.
Das Seitwärtsregime wirkt im MCM-Feld eher als ruhige Feldzeitnähe.

## Interpretation

Die bisherige Viererordnung bleibt erhalten:

```text
lastnah
last_feldzeitnah
ruhenah
ruhig_feldzeitnah
```

Die Seitwärtswelt zeigt:

```text
Seitwärts-Aktivität ist nicht automatisch Last.
Moderate Bewegung kann feldzeitnah bleiben, wenn Rekopplung und Carry getragen bleiben.
```

Das spricht für eine wichtige Trennung:

- Rohweltbewegung alleine definiert keine MCM-Last.
- Last entsteht erst, wenn Bewegung mit höherem Strain, Memorylast und Rekopplungsverlust gekoppelt ist.
- Feldzeit kann in ruhigen und aktiveren Seitwärtsbereichen auftreten.

## Bedeutung Für MINI_DIO

Für MINI_DIO bedeutet das:

- Die passive Feldlesung unterscheidet Bewegung von Belastung.
- Seitwärts kann als stabilisierende Feldzeitnähe auftreten.
- Die vier Arbeitsformen werden durch ein neues Regime nicht widerlegt.
- Eine mögliche neue Mischklasse ist derzeit nicht nötig.

Das ist ein sauberer Befund gegen Überinterpretation: Nicht jede aktivere Rohweltregion wird als Stress gelesen.

## Grenze

Diese Diagnose ist kein Beweis einer universellen Feldordnung.
Sie zeigt aber, dass ein Seitwärtsregime die bisherigen Klassen nicht auflöst.

Die Werte sind Arbeitsbefunde, keine Schwellwerte.

## Wie es weitergeht

Als nächstes sollte eine Expansionswelt geprüft werden.
Die Hierarchie bleibt:

1. Grundpol: Last, Ruhe oder ruhige Feldzeitnähe?
2. Unterform: entsteht Nachhall/Wiederkehr ohne Belastung?
3. Folgeschritt: nur wenn die bestehenden vier Formen nicht reichen, wird eine neue Mischklasse dokumentiert.
