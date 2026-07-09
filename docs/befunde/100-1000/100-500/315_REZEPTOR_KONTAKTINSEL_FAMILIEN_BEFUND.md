# 315 - Semantik der Rezeptor-Kontaktinseln

## Grundfrage

Wer traegt lokale Rezeptor-Kontaktinseln wiederholt?

Geprueft wurde, ob Kontaktinseln eher durch rohe `symbol_family`-Spuren oder durch verdichtete `mcm_field_episode_preview_symbol`-Familien stabil lesbar werden.

## Datengrundlage

Ausgangspunkt:

- `312_REZEPTOR_KONTAKTINSELN_EVENTS.csv`
- `312_REZEPTOR_KONTAKTINSELN_SUMMARY.csv`

Neu erzeugt:

- `314_REZEPTOR_KONTAKTINSEL_SYMBOL_FAMILIEN.csv`
- `314_REZEPTOR_KONTAKTINSEL_MCM_PREVIEW_FAMILIEN.csv`
- `314_REZEPTOR_KONTAKTINSEL_FAMILIEN_PAARE.csv`

## Befund

Die rohe Symbolseite ist stark fragmentiert:

```text
symbol_family-Familien: 998
```

Die MCM-Preview-Ebene ist deutlich verdichteter:

```text
mcm_field_episode_preview-Familien: 91
```

Das ist fachlich relevant:

```text
Die lokale Sinnes-/Formvarianz zerstreut sich in viele feine Zeichen.
Die MCM-Feld-Episodensprache verdichtet diese Kontaktinseln in deutlich weniger Familien.
```

## Staerkste MCM-Preview-Familien

| MCM-Preview-Familie | Count | Welten | Rekoppelt | Offen getragen | Kippnah | Lesung |
|---|---:|---:|---:|---:|---:|---|
| `dio_mcm_episode_1t5bcxp` | 449 | 4 | 0.579 | 0.408 | 0.013 | gemischt |
| `dio_mcm_episode_183drjy` | 307 | 4 | 0.792 | 0.208 | 0.000 | rekoppelnde Kontaktinsel-Familie |
| `dio_mcm_episode_02xikfk` | 87 | 4 | 0.414 | 0.586 | 0.000 | offen getragene Kontaktinsel-Familie |
| `dio_mcm_episode_0y50lf3` | 25 | 4 | 0.360 | 0.600 | 0.040 | offen getragene Kontaktinsel-Familie |
| `dio_mcm_episode_19m9z8d` | 13 | 4 | 0.538 | 0.462 | 0.000 | gemischt |
| `dio_mcm_episode_1927mcg` | 13 | 3 | 0.154 | 0.769 | 0.077 | offen getragene Kontaktinsel-Familie |
| `dio_mcm_episode_0l5wut9` | 12 | 4 | 0.917 | 0.083 | 0.000 | rekoppelnde Kontaktinsel-Familie |

## Semantische Deutung

Die Kontaktinseln sind nicht nur einzelne Druckereignisse.

Sie tragen wiederkehrende MCM-Preview-Familien:

- `dio_mcm_episode_183drjy` wirkt aktuell wie eine stark rekoppelnde Kontaktinsel-Familie.
- `dio_mcm_episode_02xikfk` wirkt eher wie offen getragene Kontaktnaehe.
- `dio_mcm_episode_1t5bcxp` ist breit und gemischt: sie erscheint haeufig, aber nicht eindeutig nur rekoppelnd oder nur offen.
- echte kippnahe Familien sind selten und bisher duenn.

Damit entsteht eine wichtige Trennung:

```text
symbol_family = feine, lokale Wahrnehmungs-/Formvarianz
mcm_field_episode_preview_symbol = verdichtete Feld-Episodensprache
```

## Ergebnis

Rekoppelnde und offen getragene Kontaktinseln sind semantisch unterscheidbar.

Nicht perfekt, nicht absolut, aber sichtbar:

```text
Einige MCM-Preview-Familien tragen Kontaktinseln eher zur Rekopplung.
Andere tragen Kontaktinseln eher offen weiter.
Kippnahe Inseln bleiben selten und weniger stabil verdichtet.
```

Das ist ein Hinweis auf eine entstehende innere Semantik:

```text
Die Welt beruehrt Rezeptoren.
Das Feld reagiert.
Lokale Kontaktinseln entstehen.
Wiederkehrende Inseln verdichten sich in MCM-Feld-Episodenfamilien.
Diese Familien tragen unterschiedliche Nachlaufqualitaet.
```

## Grenze

Diese Familien duerfen nicht als Handlungssignale gelesen werden.

Sie beschreiben passive Innenfeld-Semantik:

- Kontakt,
- Druck,
- Passung,
- Rekopplung,
- offene Fortsetzung,
- seltene Kippnaehe.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob `dio_mcm_episode_183drjy`, `dio_mcm_episode_02xikfk` und `dio_mcm_episode_1t5bcxp` in neuen Welten wieder dieselbe Kontaktqualitaet tragen. Das waere ein wichtiger Reproduktionstest fuer die entstehende MCM-Feld-Episodensprache.
