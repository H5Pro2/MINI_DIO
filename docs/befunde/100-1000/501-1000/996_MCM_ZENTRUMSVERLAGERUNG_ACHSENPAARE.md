# MCM-Zentrumsverlagerung: Achsenpaare

## Zweck

Diese Datei prueft, ob neue Zentrumskandidaten nur Einzelknoten sind oder reziproke Achsen bilden.

## Sicherheitsgrenze

- passive Diagnose
- keine Handlung
- kein Gate
- keine Strategie

## Achsen

| Achse | Welten | Zeilen | Reziproke Links | Beob. | Belege | Rekopplung | Strain | Sensorik | Lesung |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| `183drjy <-> 1t5bcxp` | `NEUNTE_WELT | ZEHNTE_STRESSWELT` | 4 | 4 | 17599 | 212 | 0.653732 | 0.176928 | 0.866839 | `reziproke_verlegte_zentrumsachse` |
| `0vkdfwc <-> 1y00xwb` | `NEUNTE_WELT | ZEHNTE_STRESSWELT` | 3 | 3 | 99 | 42 | 0.65137 | 0.175572 | 0.868575 | `reziproke_verlegte_zentrumsachse` |
| `183drjy <-> 1hjbx8p` | `NEUNTE_WELT | ZEHNTE_STRESSWELT` | 2 | 2 | 492 | 28 | 0.666108 | 0.155728 | 0.874054 | `reziproke_verlegte_zentrumsachse` |
| `02xikfk <-> 1t5bcxp` | `NEUNTE_WELT | ZEHNTE_STRESSWELT` | 2 | 2 | 223 | 28 | 0.646792 | 0.188623 | 0.861762 | `reziproke_verlegte_zentrumsachse` |
| `0vkdfwc <-> 1t5bcxp` | `NEUNTE_WELT | ZEHNTE_STRESSWELT` | 2 | 2 | 72 | 20 | 0.648253 | 0.182335 | 0.867466 | `reziproke_verlegte_zentrumsachse` |
| `1ashesa <-> 1hjbx8p` | `NEUNTE_WELT` | 1 | 1 | 61 | 10 | 0.672084 | 0.143898 | 0.870457 | `duenne_zentrumsachse` |
| `02xikfk <-> 037i64j` | `ZEHNTE_STRESSWELT` | 1 | 1 | 68 | 12 | 0.643684 | 0.200237 | 0.856918 | `duenne_zentrumsachse` |
| `0y50lf3 <-> 17i4j9o` | `ZEHNTE_STRESSWELT` | 1 | 1 | 54 | 15 | 0.653394 | 0.162591 | 0.877537 | `duenne_zentrumsachse` |

## Befund

Eine verlegte Mitte wird staerker, wenn sie nicht nur als einzelner Knoten erscheint,
sondern als gegenseitige Achse mit wiederkehrender Rueckbindung.

Arbeitsableitung:

```text
Mitte kann im MCM-Feld als Achse entstehen:
zwei Knoten tragen sich gegenseitig und bleiben ueber Weltwechsel als Zentrumsnaehe lesbar.
```

## Wie es weitergeht

Als naechstes sollte die staerkste Achse gegen Rohweltsegmente gelesen werden.
Dann wird sichtbar, welche Weltform diese reziproke Mitte ausloest oder traegt.