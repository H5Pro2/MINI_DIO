# Jahres- und Zeitaufloesungs-Matrix gerichtete Feldbewegung

Stand: 2026-06-20

## Zweck

Diese Diagnose erweitert die Zeitaufloesungs-Matrix auf zwei Jahreswelten:

- 2024
- 2025

Geprueft werden jeweils SOL/BTC, Stress/Ruhe-Fenster und die Zeitaufloesungen:

- 1h
- 15m
- 5m

Die Diagnose bleibt passiv:

```text
keine Handlung
kein Gate
keine Strategie
keine Runtime-Regel
```

## Hierarchie

1. Grundfrage: Ist die gerichtete passive Feldbewegung jahres- und aufloesungsuebergreifend lesbar?
2. Unterpruefung: `1t5bcxp -> 183drjy` und `183drjy -> 1t5bcxp` ueber 2024/2025 und 1h/15m/5m vergleichen.
3. Folgeschritt: pruefen, ob die Stabilitaet auf Weltmerkmalen, Rezeptorkontakt oder MCM-Feldlage beruht.

## Matrix

| Jahr | Aufloesung | Paar | Events | Top-Qualitaet | Anteil | Top-Signatur | Signaturanteil | Driftlabel |
|---|---|---|---:|---|---:|---|---:|---|
| 2024 | 1h | `1t5bcxp -> 183drjy` | 106 | `eng_getragen` | 0.6132 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.6132 | `wiederkehrend_variabel` |
| 2024 | 1h | `183drjy -> 1t5bcxp` | 94 | `fragmentiert` | 0.5532 | `rekoppelnde_lage -> druck_lage -> rekoppelnde_lage` | 0.1277 | `lokal_offen` |
| 2024 | 15m | `1t5bcxp -> 183drjy` | 74 | `eng_getragen` | 0.5405 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.5405 | `wiederkehrend_variabel` |
| 2024 | 15m | `183drjy -> 1t5bcxp` | 67 | `fragmentiert` | 0.5224 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.1642 | `lokal_offen` |
| 2024 | 5m | `1t5bcxp -> 183drjy` | 77 | `eng_getragen` | 0.5195 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.5195 | `wiederkehrend_variabel` |
| 2024 | 5m | `183drjy -> 1t5bcxp` | 64 | `fragmentiert` | 0.5000 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.2031 | `lokal_offen` |
| 2025 | 1h | `1t5bcxp -> 183drjy` | 103 | `eng_getragen` | 0.5534 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.5534 | `wiederkehrend_variabel` |
| 2025 | 1h | `183drjy -> 1t5bcxp` | 97 | `fragmentiert` | 0.6392 | `rekoppelnde_lage -> bewegungsbruch -> rekoppelnde_lage` | 0.1340 | `lokal_offen` |
| 2025 | 15m | `1t5bcxp -> 183drjy` | 91 | `eng_getragen` | 0.6374 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.6374 | `wiederkehrend_stabil` |
| 2025 | 15m | `183drjy -> 1t5bcxp` | 80 | `fragmentiert` | 0.4750 | `rekoppelnde_lage -> offene_lage -> rekoppelnde_lage` | 0.1500 | `lokal_offen` |
| 2025 | 5m | `1t5bcxp -> 183drjy` | 79 | `eng_getragen` | 0.6076 | `rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage` | 0.6076 | `wiederkehrend_stabil` |
| 2025 | 5m | `183drjy -> 1t5bcxp` | 69 | `fragmentiert` | 0.5362 | `rekoppelnde_lage -> druck_lage -> bewegungsbruch` | 0.1304 | `lokal_offen` |

## Befund

Die Richtung bleibt in allen geprueften Kombinationen erhalten:

```text
1t5bcxp -> 183drjy = dominant eng_getragen
183drjy -> 1t5bcxp = dominant fragmentiert
```

Der Hinweg traegt in allen sechs Kombinationen dieselbe Top-Signatur:

```text
rekoppelnde_lage -> rekoppelnde_lage -> rekoppelnde_lage
```

Der Rueckweg ist anders:

- Er bleibt ebenfalls oft an rekoppelnde Lagen gekoppelt.
- Aber sein Signaturanteil ist deutlich niedriger.
- Seine passive Qualitaet bleibt fragmentiert.
- In 2025 erscheinen staerker offene, drucknahe oder bruchnahe Zwischenlagen.

Damit zeigt sich:

```text
Nicht jede rekoppelnde Lage traegt gleich.
Die Richtung und die Feldbewegung entscheiden mit.
```

## Jahreslesung

2024 bestaetigt die Richtung, aber weicher.
Der Rueckweg ist fragmentiert, aber weniger klar bruchnah.

2025 bestaetigt die Richtung schaerfer.
Der Hinweg wird in 15m und 5m `wiederkehrend_stabil`, der Rueckweg bleibt `lokal_offen` und fragmentiert.

## Fachliche Lesart

Dieser Befund spricht gegen eine simple Einzelzeichen-Deutung.
`1t5bcxp` oder `183drjy` sind nicht allein die Bedeutung.

Die Bedeutung entsteht aus:

```text
Feldlage
Richtung
Wiederkehr
Tragart
Weltkontakt
```

Damit liegt ein weiterer Hinweis auf passive MCM-Bedeutungsbildung vor:

```text
Eine Feldbewegung kann tragend oder fragmentierend sein,
auch wenn ihre beteiligten Feldfamilien gleich bleiben.
```

## Grenze

Der Befund ist stark innerhalb der geprueften SOL/BTC-Jahreswelten.
Er ist noch kein Beweis fuer eine allgemeine MCM-Gesetzmaessigkeit.

## Wie es weitergeht

Als naechstes sollte diese Matrix auf ein anderes Asset gelegt werden, zum Beispiel KAS.
Ziel ist zu pruefen, ob die gerichtete Feldbewegung assetuebergreifend erhalten bleibt oder ob SOL/BTC eine eigene Weltfamilie bilden.
