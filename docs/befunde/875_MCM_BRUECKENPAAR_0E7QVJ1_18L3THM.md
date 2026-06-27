# MCM-Brueckenpaar Lupe

## Zweck

Diese Diagnose liest das staerkste stabile Brueckenpaar `dio_mcm_episode_0e7qvj1` und `dio_mcm_episode_18l3thm`.
Sie prueft, ob das Paar nur gemeinsam haeufig erscheint oder ob gerichtete Rueckbezuege zwischen beiden Tokens bestehen.

## Tokenprofil

| Token | Segmente | Welten | Dauer | Paar-Eintritte | Paar-Austritte | Rekopplung innen | Rekopplung Austritt | Strain innen | Strain Austritt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| dio_mcm_episode_0e7qvj1 | 54 | 6 | 259.30 | 19 | 23 | +0.0410 | -0.0395 | -0.0415 | +0.0063 |
| dio_mcm_episode_18l3thm | 34 | 5 | 45.26 | 23 | 19 | +0.0018 | -0.0277 | +0.0039 | +0.0315 |

## Gerichtete Paarkanten

| Quelle | Ziel | Anzahl | Welten |
|---|---|---:|---:|
| dio_mcm_episode_0e7qvj1 | dio_mcm_episode_18l3thm | 46 | 5 |
| dio_mcm_episode_18l3thm | dio_mcm_episode_0e7qvj1 | 38 | 5 |

## Austrittsphasen Im Paar

| Phase | Anzahl |
|---|---:|
| gemischt | 19 |
| oeffnend_belastend | 43 |
| rekoppelnd | 22 |

## Befund

`dio_mcm_episode_0e7qvj1` -> `dio_mcm_episode_18l3thm` tritt `46` mal in `5` Welten auf.
`dio_mcm_episode_18l3thm` -> `dio_mcm_episode_0e7qvj1` tritt `38` mal in `5` Welten auf.

Das Paar ist gegenseitig gerichtet. Es ist damit kein einfacher einseitiger Uebergang, sondern ein Rueckbezugsbereich im Brueckennetz.
Die Gegenseitigkeit erscheint ueber mehrere Welten. Das spricht gegen eine zufaellige Einzelwelt-Kopplung.

## Bedeutung

Das Paar wirkt wie ein zentraler Uebergangsknoten im MCM-Feld:

```text
Aussenwelt aktiviert Bruecke A/B
Bruecke A fuehrt zu Bruecke B
Bruecke B fuehrt wieder zu Bruecke A
danach erfolgt ein Austritt in weitere Feldzustaende
```

Damit entsteht eine kleine Rueckbezugsstruktur, nicht nur eine isolierte Bedeutung.

## Wie es weitergeht

Als naechstes sollte dieses Paar gegen andere Brueckenpaare verglichen werden: Ist `0e7qvj1`/`18l3thm` der zentrale Brueckenkern, oder gibt es mehrere getrennte Brueckenkerne im Feld?
