# Rezeptor Adaptation Memory

Passive Verdichtung der A/B-Folgen einer Sinneshaltung.

Diese Memory speichert keine Regel. Sie speichert, ob eine gelesene Rezeptorhaltung in beobachteten Welten das MCM-Feld eher beruhigt, neutral laesst oder verschiebt.

## Verdichtung

| Haltung | Welten | bekannte Ticks | angewendet | Folge | Qualitaet | dZentrum | dRand | dRekopplung | dStrain | dRohfeld | dTon | dSicht |
|---|---:|---:|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| achsenweise_rezeptorhaltung_normale_weltspannung | 16 | 64825 | 64825 | beruhigend | 1.0000 | 0.0072 | -0.0040 | 0.0010 | -0.0014 | -0.0048 | -0.0055 | 0.0051 |
| achsenweise_rezeptorhaltung_offen_suchend | 5 | 9451 | 9451 | beruhigend | 1.0000 | 0.0115 | -0.0037 | 0.0011 | -0.0016 | -0.0054 | -0.0063 | 0.0062 |
| achsenweise_rezeptorhaltung_ruhig_zentrumsnah | 1 | 1160 | 1160 | neutral | 0.3500 | 0.0050 | -0.0010 | 0.0006 | -0.0009 | -0.0037 | -0.0042 | 0.0028 |
| achsenweise_rezeptorhaltung_ueberstabil_extrem_leise_scharf | 1 | 6392 | 6392 | neutral | 0.3500 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | -0.0000 | -0.0000 | 0.0001 |
| achsenweise_rezeptorhaltung_ueberstabil_gemischt | 1 | 3181 | 3181 | neutral | 0.3500 | 0.0002 | -0.0003 | 0.0000 | -0.0000 | -0.0001 | -0.0001 | 0.0001 |
| achsenweise_rezeptorhaltung_ueberstabil_leise_scharf | 2 | 14178 | 14178 | neutral | 0.3500 | 0.0000 | -0.0044 | 0.0002 | -0.0002 | -0.0010 | -0.0009 | 0.0001 |
| achsenweise_rezeptorhaltung_ueberstabil_mit_randreiz | 2 | 11305 | 11305 | neutral | 0.5250 | 0.0000 | -0.0121 | 0.0005 | -0.0007 | -0.0030 | -0.0026 | 0.0002 |
| achsenweise_rezeptorhaltung_ueberstabil_visuell_weicher | 1 | 7929 | 7929 | neutral | 0.3500 | 0.0038 | -0.0004 | 0.0005 | -0.0006 | -0.0019 | -0.0023 | 0.0033 |

## Befund

Die bisher getestete Rezeptorhaltung zeigt eine beruhigende Folge: Rand/Kipp und Strain sinken leicht, Zentrum und Rekopplung bleiben erhalten oder steigen minimal.

Das ist fachlich wichtig, weil die Anpassung nicht als harte Normalisierung erscheint. Sie wirkt eher wie eine gelernte Aufnahmehaltung vor dem Feld.

## Grenze

Die Memory ist passiv. Sie steuert Mini-DIO noch nicht aktiv.

Sie beantwortet nur:

```text
Welche Sinneshaltung hatte in welchen Welten welche Feldfolge?
```
