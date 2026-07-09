# 1957 - Holdout-Scan der späten Driftrollenprofile

## Hierarchie der Prüfung

- Grundfrage: Tauchen die Rohweltprofile der späten Driftrollen auch in anderen Welten auf?
- Unterprüfung: Die aus 1956 gewonnenen starken Profile werden gegen Anschlusswelten gescannt.
- Folgeschritt: Nur wenn ein Profil wiederkehrt, wird später geprüft, ob daraus auch eine Rolle entsteht.

## Datengrundlage

- Profilquelle: `docs\befunde\1956_SPAETE_DRIFTROLLEN_ROHWELT_RUECKLESUNG.csv`
- starke Zielprofile: 5
- Ergebnis-Tabelle: `docs\befunde\1957_SPAETE_DRIFTROLLEN_PROFILE_HOLDOUT_SCAN.csv`

## Ergebnis

| Welt | Zeilen | Zielprofil-Treffer | Anteil | Profilbreite | dominantes Profil |
|---|---:|---:|---:|---:|---|
| SIDEWAYS | 1994 | 316 | 0.158475 | 56 | offene_formaufnahme / gedaempfte_energie / rekoppelnd_entlastet |
| EXPANSION10K_AFTER | 9994 | 1366 | 0.136682 | 70 | offene_formaufnahme / gedaempfte_energie / rekoppelnd_entlastet |
| STABLE10K_AFTER | 9994 | 1330 | 0.133080 | 70 | offene_formaufnahme / gedaempfte_energie / rekoppelnd_entlastet |
| STRESS10K_AFTER | 9994 | 1341 | 0.134181 | 70 | offene_formaufnahme / gedaempfte_energie / rekoppelnd_entlastet |
| EXPANSION10K_REPRO | 9994 | 1366 | 0.136682 | 70 | offene_formaufnahme / gedaempfte_energie / rekoppelnd_entlastet |

## Arbeitsdeutung

Die Zielprofile aus den späten Driftrollen sind nicht nur in den ursprünglichen Rücklese-Welten sichtbar. Sie tauchen auch in Anschlusswelten auf, allerdings mit unterschiedlicher Dichte. Damit ist das Profil selbst breiter als eine einzelne Symbolfamilie.

Das spricht für eine Feldlage, die Mini-DIO wiederholt lesen kann. Es sagt noch nicht, dass daraus zwingend dieselbe Rolle entsteht. Genau diese Trennung ist wichtig: Profilnähe ist Vorbedingung, Rollenbildung ist spätere Verdichtung.

## Wie es weitergeht

Als nächstes sollte eine Welt mit hoher Zielprofil-Dichte gegen die spätere Rollenbildung geprüft werden: Entsteht dort erneut eine bekannte Driftrolle, eine neue Nachbarschaft oder nur eine offene Vorform?
