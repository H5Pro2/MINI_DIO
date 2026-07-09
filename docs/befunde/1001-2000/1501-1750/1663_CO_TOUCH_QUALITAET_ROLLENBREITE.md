# Co-Touch-Qualität und Rollenbreite

Stand: 2026-07-06

## Zweck

Nach der lokalen Umschaltanalyse wurde geprüft, ob breite Rollenräume stärkere gemeinsame Rollenbindung besitzen als enge Rollenräume.

Die Leitfrage:

```text
Entsteht Rollenbreite durch höhere Co-Touch-Qualität,
oder durch mehr verteilte Rollenanschlüsse?
```

Verglichen wurden wieder breite gegen enge Segmente:

```text
sideways Start 0 gegen Start 4000
negative_stress Start 2000 gegen Start 4000
positive_expansion Start 4000 gegen Start 8000
```

## Ergebnis

| Fall | Rollen | Kombis | avg CoTouch | min CoTouch | avg Resonanz | avg DeltaSum | cross | same | Top Pair |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| sideways breit | 7/7 | 19/19 | 0.4926 | 0.0133 | 0.1881 | 32.84 | 11 | 8 | `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit` co=1.000 res=0.258 delta=48 |
| sideways eng | 2/2 | 1/1 | 0.9200 | 0.9200 | 0.5000 | 83.00 | 0 | 1 | `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit` co=0.920 res=0.500 delta=83 |
| stress breit | 4/4 | 6/6 | 0.6067 | 0.3600 | 0.2707 | 46.50 | 3 | 3 | `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit` co=0.920 res=0.366 delta=60 |
| stress eng | 2/2 | 1/1 | 1.0000 | 1.0000 | 0.5000 | 55.00 | 0 | 1 | `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit` co=1.000 res=0.500 delta=55 |
| expansion breit | 5/5 | 10/10 | 0.2627 | 0.0533 | 0.2477 | 71.60 | 6 | 4 | `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit` co=0.820 res=0.408 delta=99 |
| expansion eng | 3/3 | 3/3 | 0.5378 | 0.3067 | 0.3568 | 70.00 | 0 | 3 | `dio_mcm_episode_02ktejt|dio_mcm_episode_1t06mit` co=1.000 res=0.469 delta=87 |

## Befund

Breite Rollenräume haben nicht automatisch höhere durchschnittliche Co-Touch-Qualität.

Im Gegenteil:

```text
enge Rollenräume = wenige, starke Paarbindungen
breite Rollenräume = mehrere, verteilte Paarbindungen
```

Beispiele:

- `sideways_eng` hat nur 1 Kombination, aber sehr hohe Co-Touch-Qualität.
- `stress_eng` hat ebenfalls nur 1 Kombination, aber maximale Co-Touch-Qualität.
- `sideways_breit` und `expansion_breit` haben viele Kombinationen, aber niedrigere durchschnittliche Co-Touch-Werte.

Damit ist Rollenbreite nicht einfach stärkere Bindung.
Sie ist eher Verteilungsbreite.

## Netzwerklesung

Die aktuelle MCM-Lesung wird dadurch präziser:

```text
enge Feldlage
= starke lokale Bindung zwischen wenigen Rollen

breite Feldlage
= verteiltes Netzwerk aus mehreren anschlussfähigen Rollen
```

Das passt zur bisherigen Beobachtung:

```text
Rollenbreite entsteht nicht aus Wechselhäufigkeit,
sondern aus gemeinsamer Anschlussfähigkeit.
```

Jetzt wird diese Anschlussfähigkeit differenzierter:

```text
enge Anschlussfähigkeit = kompakte Bindung
breite Anschlussfähigkeit = verteiltes Rollenfeld
```

## Bedeutung für MINI_DIO

MINI_DIO bildet in diesen Prüfungen zwei unterschiedliche passive Ordnungsformen:

1. **Kompakte Rollenbindung**
   - wenige Rollen,
   - hohe Co-Touch-Qualität,
   - starke Einzelrekopplung.

2. **Verteiltes Rollennetz**
   - mehrere Rollen,
   - mehrere cross-state Kombinationen,
   - schwächere Einzelbindung, aber größerer Bedeutungsraum.

Das ist wichtig für die MCM-Forschung:

```text
Nicht jede starke Ordnung ist breit.
Nicht jede breite Ordnung ist stark pro Paar.
```

## Grenze

Diese Diagnose bleibt passiv.
Sie zeigt keine Handlung und keine Strategie.
Sie zeigt aber, dass das MCM-Feld unterschiedliche Ordnungsformen trägt:

```text
kompakt gebunden
oder
verteilt vernetzt
```

## Nächster Prüfpunkt

Als nächstes sollte geprüft werden, ob verteilte Rollennetze später stabilere Bedeutungsräume bilden als kompakte Einzelbindungen.
Die direkte Frage:

```text
Welche Form reift besser über weitere Weltkontakte:
kompakte Bindung oder verteiltes Rollennetz?
```
