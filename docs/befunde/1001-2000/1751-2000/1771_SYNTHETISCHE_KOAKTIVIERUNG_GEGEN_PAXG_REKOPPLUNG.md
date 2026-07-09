# Synthetische Koaktivierung gegen PAXG-Rekopplung

Stand: 2026-07-08

## Grundfrage

Nach Befund 1770 war sichtbar:

```text
Koaktivierung kann lokal Rollenöffnung erzeugen.
```

Die nächste Frage war:

```text
Ist diese synthetische Rollenöffnung nahe an realer PAXG-Rekopplung,
oder zeigt PAXG eine andere Milieuqualität?
```

## Unterprüfung

Verglichen wurden:

- synthetische Koaktivierung 1770, lokale 1000er-Fenster,
- synthetische Koaktivierung 1770, breitere 2000er-Fenster,
- reale PAXG-2024-Sequenz mit `mittlere_uebergangsphase`,
- reale PAXG-2024-Sequenz mit `verteilt_rekoppelnd`.

Report:

```text
reports/1770_synth_koaktiv_vs_paxg_rekoppelnd.csv
```

## Vergleich

| Quelle | Klasse | Rollen | Kombinationen | Rekopplung | Adaptiv | Nachhall | Delta Energie | Delta Drift | Delta Range |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| synthetisch 1770 1000 | mittlere_uebergangsphase | 3 | 3 | 0.7456 | 0.7677 | 0.6744 | +1.4018 | -0.7951 | +0.004215 |
| synthetisch 1770 2000 | mittlere_uebergangsphase | 3 | 3 | 0.7515 | 0.7622 | 0.7769 | +2.7821 | -1.7582 | +0.007238 |
| PAXG 2024 real | mittlere_uebergangsphase | 3 | 3 | 0.7027 | 0.7142 | 0.3323 | -0.0862 | -0.0023 | -0.000079 |
| PAXG 2024 real | verteilt_rekoppelnd | 5 | 10 | 0.7070 | 0.7422 | 0.3770 | +0.0893 | +0.0090 | +0.000045 |

## Befund

Die synthetische Koaktivierung und PAXG bilden nicht dieselbe Milieuform.

Synthetische Koaktivierung öffnet lokal über:

- starke Folgeenergie,
- deutliche Range-Aufweitung,
- fallende Drift,
- hohen Nachhall,
- hohe adaptive Rekopplung.

PAXG `verteilt_rekoppelnd` bildet dagegen breitere Rollen bei:

- viel niedrigerer Weltenergie,
- sehr kleiner Range,
- nur leicht steigender Folgeenergie,
- höherer Rollen- und Kombinationsbreite,
- klarer adaptiver Erfahrungskopplung.

Kurz:

```text
1770 erzeugt Rollenöffnung durch starke koaktive Weltbewegung.
PAXG erzeugt rekoppelnde Rollenbreite aus ruhigerer, feinerer Milieubindung.
```

## Deutung

Die synthetische Koaktivierung ist eine Vorform, aber noch kein Modell der realen PAXG-Rekopplung.

Sie zeigt:

```text
Mehrere Rollen können lokal gemeinsam geöffnet werden.
```

PAXG zeigt zusätzlich:

```text
Mehrere Rollen können bei geringer äußerer Lautheit getragen und rekoppelt werden.
```

Damit wird der Unterschied präziser:

- `mittlere_uebergangsphase` kann durch starke Koaktivierung entstehen,
- `verteilt_rekoppelnd` braucht wahrscheinlich feinere Milieubindung,
- reale rekoppelnde Breite ist nicht einfach synthetische Übersteuerung.

## Bedeutung für MINI_DIO

MINI_DIO trennt dadurch weiter:

- laute koaktive Öffnung,
- ruhige rekoppelnde Breite,
- Syntaxvarianz,
- Rollenvarianz,
- adaptive Erfahrungsbindung.

Das ist methodisch wichtig, weil es gegen die einfache Erklärung spricht:

```text
Mehr Energie = mehr Rollen = mehr Bedeutung.
```

Der aktuelle Befund lautet eher:

```text
Rollenbreite braucht ein passendes Feldmilieu.
Dieses Milieu kann laut öffnen oder ruhig rekoppeln.
Beides ist nicht dasselbe.
```

## Grenze

Der Vergleich nutzt vorhandene PAXG-2024-Sequenzdaten und die neue 1770-Koaktivierungswelt.

Er beweist nicht, welche Ursache PAXG-Rekopplung vollständig erzeugt. Er zeigt aber, dass die synthetische Koaktivierung bisher nur eine lokale Übergangsform nachbildet, nicht die volle reale rekoppelnde Breite.
