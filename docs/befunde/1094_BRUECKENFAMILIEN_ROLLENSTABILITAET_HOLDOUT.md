# 1094 - Brueckenfamilien-Rollenstabilitaet im Holdout

Diese Synthese ist passiv. Sie erzeugt keine Handlung, kein Gate, kein Entry-Signal und keine Richtungslogik.

## Grundlage

- `1092_BRUECKENFAMILIEN_QUALITAETSKARTE.md`
- `1093_BRUECKENFAMILIEN_QUALITAETSKARTE_HOLDOUT.md`
- `1093_BRUECKENFAMILIEN_QUALITAETSKARTE_HOLDOUT.csv`

## Frage

Bleibt die passive Qualitaetskarte der Brueckenfamilien in neuen Welten stabil?

Geprueft wurden getrennte Holdout-Welten aus unabhaengigen, langen und post-clean Sequenzen. Synthetische Welten wurden hier ausgelassen.

## Holdout-Befund

Im Holdout bleiben die Grundrollen sichtbar:

| Familie | Tragende Events | Kippnahe Events | Tragende Rekopplung | Kippnahe Rekopplung | Tragender Strain | Kippnaher Strain | Lesart |
|---|---:|---:|---:|---:|---:|---:|---|
| `dio_0g2r` | 38 | 38 | 0.7222 | 0.6719 | 0.1320 | 0.1729 | offene Bruecke bleibt stabil trennbar |
| `dio_155c` | 35 | 28 | 0.7307 | 0.6965 | 0.1349 | 0.1764 | spannungsnaher Brueckenanker bestaetigt |
| `dio_17ct` | 52 | 26 | 0.7272 | 0.6990 | 0.1343 | 0.1652 | feldfolgenabhaengiger Anker bestaetigt |
| `dio_1ewh` | 112 | 22 | 0.7239 | 0.6761 | 0.1346 | 0.1679 | tragende Vorpraegung bleibt stark |
| `dio_1gp2` | 27 | 26 | 0.7223 | 0.6898 | 0.1301 | 0.1646 | balancierter Umschlag bleibt sichtbar |

## Gemeinsame Stabilitaet

Bei allen fuenf Familien gilt im Holdout:

```text
tragende Lesart = hoehere Rekopplung + niedrigerer Strain
kippnahe Lesart = niedrigere Rekopplung + hoeherer Strain
```

Damit bleibt die Grundregel aus 1082 auch ausserhalb der urspruenglichen adapted-Welten erhalten.

## Rollenstabilitaet

### Stabil

- `dio_1ewh` bleibt deutlich tragend vorgepraegt.
- `dio_1gp2` bleibt nahezu balanciert.
- `dio_155c` bleibt spannungsnaher als die ruhigeren Brueckenanker.

### Verschoben, aber nicht gebrochen

- `dio_0g2r` erscheint im Holdout exakt ausgeglichen nach Eventzahl, bleibt aber durch Rekopplung und Strain sauber unterscheidbar.
- `dio_17ct` bleibt feldfolgenabhaengig, zeigt im Holdout aber mehr tragende Ereignisse als kippnahe.

## Schluss

Die Qualitaetskarte aus 1092 wird durch den Holdout nicht widerlegt.

Sie wird im Gegenteil stabiler:

```text
Familienrolle bleibt erkennbar.
Aktuelle Lesart bleibt feldfolgenabhaengig.
Rekopplung und Strain trennen tragend von kippnah.
```

Wichtig: Die Rollen sind keine absoluten Klassen. Sie bleiben dynamische Feldrollen. Ein Anker kann tragend oder kippnah erscheinen, aber seine Tendenz bleibt im Holdout lesbar.

## Bedeutung fuer MINI_DIO

MINI_DIO bildet hier ein wiederholbares Bedeutungsnetz:

- Familien sind nicht nur Namen.
- Familien tragen Rollenqualitaeten.
- Rollenqualitaeten bleiben in neuen Welten teilweise stabil.
- Die aktuelle Bedeutung entsteht trotzdem aus der Feldfolge.

Das ist ein staerkerer Befund als reine Wiederkehr. Es ist eine beginnende rollenbasierte Innenfeld-Semantik.

## Grenze

Diese Lesart bleibt diagnostisch. Sie darf nicht in Handlung, Richtung, Strategie oder Vorhersage uebersetzt werden.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob in den Holdout-Welten neue Brueckenfamilien entstehen, die nicht in der bisherigen Karte liegen. Das trennt bekannte stabile Rollen von neuer emergenter Rollenbildung.
