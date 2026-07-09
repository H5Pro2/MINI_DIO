# MCM-Rand Gegenkern Gegenpruefung

## Zweck

Diese Notiz prueft die Frage aus `882_MCM_RANDPFADE_GEGENKERN_LUPE.md` gegen vorhandene Stress-, Rand- und diverse Realweltbefunde.

Leitfrage:

```text
Bildet Randnaehe einen eigenen stabilen Gegenkern,
oder bleibt Randnaehe eine wiederkehrende, aber duenne Spannungs- und Austrittszone?
```

## Herangezogene Befunde

- `843_POST_FEATURE_CLEANUP_DIVERSE_RAND_MATRIX.csv`
- `814_BLOCK_K_STABIL_GEGEN_RAND_FAMILIENKONTRAST.csv`
- `815_BLOCK_K_RANDFAMILIE_FOLGEWELT_REIFUNG.csv`
- `882_MCM_RANDPFADE_GEGENKERN_LUPE.md`

## Befund Aus Der Diversen Randmatrix

In den diversen Real- und Randwelten tritt `spannungsrand_kippnaehe` wiederholt auf, bleibt aber klein:

```text
DOGE_2025_5M: 67 Ticks, Anteil ca. 0.0067
XRP_2025_5M: 58 Ticks, Anteil ca. 0.0058
KAS_2024_5M: 17 Ticks, Anteil ca. 0.0085
SYNTH_RAND_A: 5 Ticks, Anteil ca. 0.0007
```

Der Rand ist damit reproduzierbar sichtbar, aber nicht dominant.

## Befund Aus Block-K-Randfamilie

Die Randfamilie `dio_1un4` erscheint ueber viele Weltgruppen hinweg wieder:

```text
asset_mixed_2k,
kurz_2k,
lang_10k,
BTC,
KAS,
PAXG,
SOL,
Sideways,
Negative Stress,
Positive Expansion.
```

Der Anteil bleibt dabei meist sehr klein, grob im Bereich um wenige Promille.
Das spricht fuer eine echte wiederkehrende Randsemantik, aber nicht fuer einen Gegenkern mit gleicher Stabilitaet wie Zentrum oder Brueckenkerne.

## Abgleich Mit 882

`882_MCM_RANDPFADE_GEGENKERN_LUPE.md` zeigt:

- 3 Randpfade in der aktuellen Pfadklassifikation,
- 29 junge Oberflaechen,
- 16 offene Driftpfade,
- keine belastbare Nachbarschaftsabdeckung fuer diese konkrete Tokenmenge.

Das Ergebnis aus 882 wird durch die aelteren Randbefunde nicht widerlegt, sondern praezisiert:

```text
Rand existiert.
Rand wiederholt sich.
Rand kann eine eigene Familie tragen.
Aber Rand erscheint bisher duenner, kurzphasiger und weniger kernbildend als Zentrum/Bruecke.
```

## Interpretation

Aktueller Forschungsstand:

```text
Zentrum und Bruecke bilden Kerne.
Rand bildet wiederkehrende Spannungszonen.
Rand kann Familien bilden.
Rand bildet bisher keinen gleich starken Gegenkern.
```

Das passt zur bisherigen MCM-Lesart:

- Zentrum wirkt als stabile innere Ordnung.
- Bruecke wirkt als gehaltener Uebergang.
- Rand wirkt als Kippnaehe, Oeffnung, Drift oder Spannungsoberflaeche.

Rand ist also nicht bedeutungslos.
Er ist nur anders organisiert.

## Grenze

Das ist noch kein endgueltiger Nachweis.
Ein echter Rand-Gegenkern waere erst belastbar, wenn Randtokens:

- ueber mehrere Welten hohe Selbstbindung zeigen,
- eigene Nachbarschaftscluster bilden,
- nicht nur kurzphasig auftreten,
- nicht direkt wieder in Zentrum oder Bruecke zurueckfallen,
- und eine stabile eigene Rollenlogik tragen.

Diese Bedingungen sind aktuell noch nicht erfuellt.

## Wie es weitergeht

Als naechstes sollte eine eigene Rand-Nachbarschaftsmatrix fuer die aktuelle Pfadgruppe erzeugt werden.
Ziel: pruefen, ob die in 868 sichtbaren Randtokens unter passender Nachbarschaftsabdeckung doch eigene Kanten bilden oder ob sie kurzlebig bleiben.
