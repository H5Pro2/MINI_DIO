# SOL 2025 Feldruhe - Methodik-Synthese

Stand: 2026-06-23

## Zweck

Diese Notiz verdichtet die methodische Korrektur der Quiet-Auswahl.

Ausgangspunkt war der Befund:

```text
Rohweltlich ruhiger Abschnitt ist nicht automatisch innenfeldruhiger Abschnitt.
```

Deshalb wurde ein neues Diagnosewerkzeug eingefuehrt:

```text
tools/select_field_quiet_windows.py
```

Es trennt:

1. rohweltliche Ruhe,
2. MCM-Feldruhe.

## Warum die Korrektur noetig war

Die erste Quiet-Extraktion suchte nur nach geringerer Rohbewegung:

- geringere Volatilitaet,
- geringerer Drawdown,
- geringerer Drift,
- geringere Range.

Der MINI_DIO-Lauf zeigte aber:

```text
Rohruhe kann innenfeldlich trotzdem offen, unruhig oder randnah wirken.
```

Damit ist klar:

```text
Quiet darf nicht nur aus der Aussenwelt bestimmt werden.
Quiet muss nach der Feldreaktion gegengeprueft werden.
```

## Neue Methode

Das neue Verfahren:

```text
Quelle
  -> mehrere rohweltlich ruhige Kandidaten
  -> MINI_DIO-Lauf pro Kandidat
  -> Topologie-Lesung pro Kandidat
  -> relative Sortierung nach Feldruhe
```

Diese Sortierung ist Diagnose.
Sie ist keine Runtime-Regel und kein Gate.

## Ergebnis der SOL-2025-Pruefung

Es wurden fuenf rohweltlich ruhige, nicht stark ueberlappende Kandidaten getestet.

Der feldruhigste Kandidat war nicht der rohweltlich ruhigste Kandidat:

```text
Rohquiet-Rang 1: SOL2025_FIELD_QUIET_01
Feldquiet-Rang 1: SOL2025_FIELD_QUIET_02
```

Der beste Feldruhe-Kandidat:

```text
SOL2025_FIELD_QUIET_02
Start: 103120
Ende: 105120
Topologie: stark_zentriert_wenig_rand
Zentrum: 0.8029
Offen:   0.1881
Rand:    0.0090
```

## Vergleich gegen Bruchfenster

Der direkte Topologievergleich:

| Welt | Topologie | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain |
|---|---|---:|---:|---:|---:|---:|---:|
| Bruch | stark_zentriert_wenig_rand | 0.8144 | 0.1745 | 0.0110 | 0.6958 | 0.5118 | 0.1545 |
| Feldruhe | stark_zentriert_wenig_rand | 0.8029 | 0.1881 | 0.0090 | 0.6959 | 0.5120 | 0.1549 |

Die Feldruhe-Welt ist topologisch minimal randarmer, aber nicht dramatisch ruhiger.

Das ist wichtig:

```text
Feldruhe ist keine simple Gegenklasse zu Bruch.
Feldruhe ist eine relative Innenfeldqualitaet.
```

## Rezeptorischer Gegenbefund

Der Rezeptorachsenvergleich zeigt:

```text
Bruch und Feldruhe bleiben rezeptorisch sehr nah beieinander.
```

Die Hochlastfenster bleiben in beiden Welten offen/randnah.

Damit entsteht eine saubere Trennung:

```text
rezeptorische Aufnahmequalitaet
ist nicht dasselbe wie
topologische Feldruhe.
```

Das ist kein Widerspruch.
Es zeigt, dass MINI_DIO mehrere Ebenen liest:

- Rohwelt,
- Rezeptoraufnahme,
- MCM-Feldwirkung,
- Topologie,
- Nachhall/Feldzeit.

## Fachliche Ableitung

Die wichtigste methodische Korrektur lautet:

```text
Ruhige Aussenwelt suchen reicht nicht.
Feldruhige Innenreaktion muss nach dem Lauf gelesen werden.
```

Damit wird die Forschung sauberer:

- Rohweltlabel beschreiben die Aussenwelt.
- Rezeptorachsen beschreiben Aufnahme und Kontakt.
- Topologie beschreibt die MCM-Innenordnung.
- Feldzeit/Nachhall beschreiben Einbettung und Uebergang.

Diese Ebenen duerfen nicht zusammenfallen.

## Bedeutung fuer MINI_DIO

MINI_DIO zeigt hier keine triviale Reizkopie.

Das System reagiert nicht:

```text
wenig Bewegung = ruhig
viel Bewegung = Stress
```

Sondern eher:

```text
Weltstruktur
+ Rezeptoraufnahme
+ Feldwirkung
+ Nachhall/Feldzeit
= passive Innenordnung
```

Das ist MCM-kompatibel, weil Innenfeldwirkung als eigene Ordnungsebene erhalten bleibt.

## Vorlaeufige Schlussfolgerung

Die Methode ist verbessert:

```text
Quiet-Extraktion wird zweistufig.
Erst Rohweltkandidat.
Dann MCM-Feldruhe-Pruefung.
```

Der aktuelle Befund zeigt:

```text
Feldruhe ist relativ und topologisch lesbar,
aber nicht identisch mit rezeptorischer Leisheit.
```

## Wie es weitergeht

Als naechstes sollte dieselbe feldruhige Kandidatenauswahl auf BTC 2025 oder SOL 2024 laufen. Ziel: pruefen, ob Feldruhe auch dort nicht mit Rohruhe zusammenfaellt und ob dieselbe robuste Topologie erhalten bleibt.
