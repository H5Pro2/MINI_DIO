# Befund 241 - Lokale Feld-Episoden-Vorschau und Syntax

Stand: 2026-06-19

## Ausgangspunkt

Die vorherige lokale Syntaxdiagnose zeigte wiederkehrende `symbol_family`-Muster in lokalen Kipp- und Rekopplungsfenstern.
Die eigentliche `mcm_field_episode_symbol`-Spur blieb dort aber weitgehend leer, weil sie nur beim Abschluss einer passiven Feld-Episode geschrieben wurde.

Darum wurde eine passive Vorschau-Spur ergänzt:

```text
mcm_field_episode_preview_symbol
```

Diese Spur benennt die gerade entstehende Feld-Episode pro Tick, ohne sie in Memory zu schreiben und ohne Handlung, Gate, Entry oder Motorik zu beeinflussen.

## Frischer Prüflauf

Es wurden zwei frische passive Läufe auf derselben kontrollierten Welt erzeugt:

```text
data/kontrolliert_2023_real_test1_1000_5m_SOLUSDT.csv
debug/preview_syntax_chain_01/
```

Beide Läufe blieben passiv:

```text
trades=0
reward=0
symbols=947
```

Damit ist der Befund weiterhin rein diagnostisch.

## Ergebnis

Die erneute lokale Syntaxdiagnose zeigt jetzt eine klare Feld-Episoden-Vorschau.

Lokale Rekopplungsfenster tragen stark wiederkehrende Vorschau-Feldsymbole:

```text
dio_mcm_episode_02xikfk
dio_mcm_episode_1r7e52w
dio_mcm_episode_1eik02d
```

Das stärkste Beispiel:

```text
Ticks 561-640
Rolle: lokal_rekoppelnd
Feldsymbol: dio_mcm_episode_02xikfk
Anteil Lauf 1: 0.8375
Anteil Lauf 2: 0.8500
Effekt: stabil
Awareness: inner_effect_stable
```

Lokale Kippfenster tragen ebenfalls wiederkehrende Feldsymbole, aber mit anderer Wirkung:

```text
dio_mcm_episode_037i64j
dio_mcm_episode_0e9ekzq
dio_mcm_episode_0eje6op
dio_mcm_episode_182yyt2
```

Das auffälligste Kippbeispiel:

```text
Ticks 881-960
Rolle: lokale_multisensorische_kippnaehe
Feldsymbol: dio_mcm_episode_037i64j
Anteil Lauf 1: 0.4625
Anteil Lauf 2: 0.4625
Effekt: tragend_unruhig
Awareness: inner_effect_carried_unrest
```

## Lesart

Die neue Preview-Spur bestätigt nicht einfach nur einzelne Zeichen.
Sie zeigt, dass lokale multisensorische Innenlagen bereits entstehende Feld-Episoden-Familien tragen können.

Wichtig ist die Trennung:

- `symbol_family` liest lokale Zeichen- und Formnähe.
- `mcm_field_episode_preview_symbol` liest die gerade entstehende Feld-Episoden-Lage.
- `passive_mcm_effect_class` und `passive_inner_effect_awareness_state` lesen die Innenfeldwirkung.

Damit wird sichtbar:

```text
Lokale Wahrnehmung
  -> lokale Symbolfamilie
  -> entstehende Feld-Episode
  -> Innenfeldwirkung
```

Das ist näher an einer lokalen Bedeutungsinsel als die vorherige Diagnose, aber noch kein Beweis für gereifte semantische Feld-Episoden.
Es zeigt zunächst eine reproduzierbare Vorschau-Struktur.

## Forschungswert

Der Befund ist wichtig, weil er eine technische Lücke geschlossen hat:

Vorher waren lokale Fenster kürzer als abgeschlossene Feld-Episoden.
Dadurch wirkte es, als ob lokale Kipp- und Rekopplungsfenster keine Feld-Episodensprache tragen.

Jetzt ist sichtbar:

```text
Auch noch nicht abgeschlossene Feldlagen haben bereits eine eigene passive Syntax.
```

Das passt zur bisherigen MINI_DIO-Arbeit:

- Bedeutung entsteht nicht erst nach Abschluss.
- Feldlage bildet sich während des Weltkontakts.
- Wiederkehr kann lokal sichtbar werden.
- Rekopplung und Kippnähe tragen unterschiedliche Vorschau-Syntax.

## Grenze

Dieser Befund bleibt passiv.

`mcm_field_episode_preview_symbol` darf nicht genutzt werden als:

- Handlungssignal,
- Entry-Signal,
- Gate,
- Motorik,
- Memory-Schreibauslöser,
- Beweis einer fertigen Bedeutung.

Es ist eine Diagnose der entstehenden Innenfeldlage.

## Wie es weitergeht

Als nächstes wird dieselbe Preview-Diagnose über mehrere Welten gelegt.
Die Grundfrage lautet:

```text
Bleiben lokale Vorschau-Feldsymbole weltbezogen stabil,
oder entstehen je Welt eigene lokale Feld-Episoden-Sprachen?
```

Unterprüfung:

```text
Rekopplungsfenster, Kippfenster und ruhige Fenster getrennt vergleichen.
```

Folgeschritt:

```text
Wenn Preview-Symbole in ähnlichen lokalen Feldlagen wiederkehren,
kann daraus eine passive Karte entstehender lokaler Bedeutungsinseln gebaut werden.
```
