# Unabhaengige 2025-2k-Weltgruppe Synthese

Stand: 2026-06-21

## Zweck

Diese Gegenprobe prueft MINI_DIO auf einer neuen kompakten Weltgruppe:

- BTC 2025 5m, 2000 Kerzen
- BTC 2025 1h, 2000 Kerzen
- SOL 2025 5m, 2000 Kerzen
- SOL 2025 1h, 2000 Kerzen

Die Pruefung bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Strategie.

## Hierarchie

1. Grundfrage: Bleibt die MCM-Feldordnung bei einer neuen Weltgruppe erhalten?
2. Unterpruefung: Bilden sich bekannte Bewegungsqualitaeten oder neue junge Bewegungsraeume?
3. Folgeschritt: Wenn Topologie stabil bleibt, aber neue Anker entstehen, ist die naechste Frage: Welche Weltmerkmale faerben die Anker?

## Forschungsketten

Alle vier Welten wurden mit zwei Laeufen und gleicher Memory zwischen Lauf 1 und Lauf 2 geprueft.

Ergebnis:

- Top-Syntax-Ueberlappung in allen vier Welten: `1.0`
- Top-Familien-Ueberlappung in allen vier Welten: `1.0`
- Trades: `0`
- Episoden je Lauf: `1994`

Das bedeutet: Die passive Innenfeld-/Syntaxbildung reproduziert sich innerhalb derselben Welt sehr stabil.

## Weltrelative Topologie

Die Topologie-Matrix liest:

| Welt | Topologiezustand | Zentrum | Offen | Rand/Kipp |
|---|---|---:|---:|---:|
| BTC2025_5M_2K | `stark_zentriert_wenig_rand` | 0.8205 | 0.1660 | 0.0135 |
| BTC2025_1H_2K | `stark_zentriert_wenig_rand` | 0.8305 | 0.1525 | 0.0171 |
| SOL2025_5M_2K | `gemischte_rollenordnung` | 0.7844 | 0.2046 | 0.0110 |
| SOL2025_1H_2K | `stark_zentriert_wenig_rand` | 0.8109 | 0.1710 | 0.0181 |

Die Rollenordnung bleibt erhalten:

```text
Zentrum + offene Variante + kleine Rand-/Kippnaehe
```

Auffaellig ist, dass alle vier Welten denselben dominanten Preview-Anker tragen:

```text
dio_mcm_episode_0e7qvj1
```

Das ist nicht derselbe dominante Anker wie in den langen 10k-Welten. Damit bestaetigt sich eine wichtige Trennung:

```text
Topologie kann stabil bleiben,
waehrend konkrete Anker und Syntax weltabhaengig wechseln.
```

## Feldbewegungs-Memory

Die unabhängige 2025-2k-Gruppe erzeugt 120 Bewegungsraeume.

Verteilung:

| Feldmemory-Qualitaet | Anzahl |
|---|---:|
| `young` | 63 |
| `recurrently_reconnecting` | 27 |
| `recurrently_opening_strain` | 23 |
| `world_specific` | 7 |

Das ist ein sauberer Befund: Die Memory reift nicht alles kuenstlich. Mehr als die Haelfte bleibt jung. Gleichzeitig entstehen gerichtete Bewegungsqualitaeten.

Staerkste Bewegungen:

| Bewegung | Ereignisse | Welten | Qualitaet | Wirkung | Druck | Rekopplung | Lautheit |
|---|---:|---:|---|---|---:|---:|---:|
| `0e7qvj1 -> 1hdpu9s` | 22 | 4 | `recurrently_reconnecting` | `rekoppelnd_entlastend` | -0.025126 | 0.015887 | -0.068608 |
| `1hdpu9s -> 0e7qvj1` | 21 | 4 | `recurrently_opening_strain` | `oeffnend_belastend` | 0.043475 | -0.034820 | 0.103628 |
| `0z748ck -> 0e7qvj1` | 15 | 4 | `recurrently_opening_strain` | `oeffnend_belastend` | 0.025639 | -0.019443 | 0.093388 |
| `0qzjuvj -> 0z748ck` | 13 | 4 | `recurrently_reconnecting` | `rekoppelnd_entlastend` | -0.005660 | 0.003098 | -0.023023 |

## Befund

Die neue Weltgruppe reproduziert nicht einfach die alten Hauptnamen `1t5bcxp` und `183drjy`.

Stattdessen bildet sie eine eigene lokale Bewegungsfamilie um `0e7qvj1`.

Fachlich ist das gut:

- die Topologie bleibt stabil,
- die konkrete Syntax bleibt weltbezogen,
- die Feldbewegungs-Memory trennt junge Spuren von wiederkehrenden Bewegungen,
- gerichtete Asymmetrie erscheint erneut: Hin- und Rueckweg sind nicht identisch.

Damit stuetzt diese Gegenprobe die bisherige Lesart:

```text
MINI_DIO bildet keine starre Namensliste.
MINI_DIO bildet eine Rollenordnung,
in der konkrete Bedeutungsanker weltabhaengig entstehen.
```

## Grenze

Die Gruppe umfasst vier kompakte 2k-Welten. Sie ist unabhaengiger als die vorherige 10k-After/Repro-Pruefung, aber noch keine Langwelt- oder Volljahrespruefung.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob `0e7qvj1` in laengeren 2025-Welten stabil bleibt oder ob es nur ein kompakter Abschnittsanker ist. Dafuer bietet sich eine 10k- oder 4k-Folgewelt aus BTC/SOL 2025 an.
