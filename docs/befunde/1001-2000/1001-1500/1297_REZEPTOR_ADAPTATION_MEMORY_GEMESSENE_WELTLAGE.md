# Rezeptor Adaptation Memory

Passive Verdichtung der A/B-Folgen einer Sinneshaltung.

Diese Memory speichert keine Regel. Sie speichert, ob eine gelesene Rezeptorhaltung in beobachteten Welten das MCM-Feld eher beruhigt, neutral laesst oder verschiebt.

## Verdichtung

| Haltung | Welten | bekannte Ticks | angewendet | Folge | Qualitaet | dZentrum | dRand | dRekopplung | dStrain | dRohfeld | dTon | dSicht |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| achsenweise_rezeptorhaltung_normale_weltspannung | 16 | 64825 | 64825 | beruhigend | 1.0000 | 0.0072 | -0.0040 | 0.0010 | -0.0014 | -0.0048 | -0.0055 | 0.0051 |
| achsenweise_rezeptorhaltung_offen_suchend | 5 | 9451 | 9451 | beruhigend | 1.0000 | 0.0115 | -0.0037 | 0.0011 | -0.0016 | -0.0054 | -0.0063 | 0.0062 |
| achsenweise_rezeptorhaltung_ruhig_zentrumsnah | 1 | 1160 | 1160 | neutral | 0.3500 | 0.0050 | -0.0010 | 0.0006 | -0.0009 | -0.0037 | -0.0042 | 0.0028 |
| achsenweise_rezeptorhaltung_ueberstabil_mit_randreiz | 2 | 11305 | 11305 | neutral | 0.5250 | 0.0000 | -0.0121 | 0.0005 | -0.0007 | -0.0030 | -0.0026 | 0.0002 |
| achsenweise_rezeptorhaltung_ueberstabil_sinnesdominant | 5 | 31680 | 31680 | neutral | 0.3500 | 0.0008 | -0.0019 | 0.0002 | -0.0002 | -0.0008 | -0.0008 | 0.0008 |

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
