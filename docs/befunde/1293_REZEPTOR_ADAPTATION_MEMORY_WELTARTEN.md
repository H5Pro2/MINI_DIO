# Rezeptor Adaptation Memory

Passive Verdichtung der A/B-Folgen einer Sinneshaltung.

Diese Memory speichert keine Regel. Sie speichert, ob eine gelesene Rezeptorhaltung in beobachteten Welten das MCM-Feld eher beruhigt, neutral laesst oder verschiebt.

## Verdichtung

| Haltung | Welten | bekannte Ticks | angewendet | Folge | Qualitaet | dZentrum | dRand | dRekopplung | dStrain | dRohfeld | dTon | dSicht |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| achsenweise_rezeptorhaltung_gold_kontrast | 3 | 11657 | 11657 | beruhigend | 0.7833 | 0.0066 | -0.0016 | 0.0008 | -0.0012 | -0.0044 | -0.0050 | 0.0040 |
| achsenweise_rezeptorhaltung_leise_assetnaehe | 2 | 2096 | 2096 | beruhigend | 1.0000 | 0.0143 | -0.0037 | 0.0011 | -0.0016 | -0.0055 | -0.0063 | 0.0063 |
| achsenweise_rezeptorhaltung_markt_weltspur | 13 | 40895 | 40895 | beruhigend | 1.0000 | 0.0073 | -0.0042 | 0.0010 | -0.0014 | -0.0049 | -0.0056 | 0.0053 |
| achsenweise_rezeptorhaltung_ruhig_stabil | 2 | 10473 | 10473 | beruhigend | 1.0000 | 0.0085 | -0.0039 | 0.0011 | -0.0015 | -0.0051 | -0.0058 | 0.0054 |
| achsenweise_rezeptorhaltung_sinneswiderspruch | 7 | 42985 | 42985 | neutral | 0.4000 | 0.0006 | -0.0048 | 0.0003 | -0.0004 | -0.0014 | -0.0014 | 0.0006 |
| achsenweise_rezeptorhaltung_stress_last | 2 | 10315 | 10315 | beruhigend | 1.0000 | 0.0086 | -0.0040 | 0.0010 | -0.0014 | -0.0049 | -0.0056 | 0.0053 |

## Befund

Die bisher getestete Rezeptorhaltung zeigt eine beruhigende Folge: Rand/Kipp und Strain sinken leicht, Zentrum und Rekopplung bleiben erhalten oder steigen minimal.

Das ist fachlich wichtig, weil die Anpassung nicht als harte Normalisierung erscheint. Sie wirkt eher wie eine gelernte Aufnahmehaltung vor dem Feld.

## Grenze

Die Memory ist passiv. Sie steuert Mini-DIO noch nicht aktiv.

Sie beantwortet nur:

```text
Welche Sinneshaltung hatte in welchen Welten welche Feldfolge?
```

Wie es weitergeht: Als naechstes kann diese Memory mit neuen Welten gefuettert werden. Wenn die Folge stabil bleibt, kann daraus spaeter eine selbst lernende Rezeptorschicht entstehen.
