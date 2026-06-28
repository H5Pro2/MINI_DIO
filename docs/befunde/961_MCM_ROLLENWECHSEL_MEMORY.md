# MCM-Rollenwechsel-Memory

## Zweck

Diese Datei speichert passiv, wenn ein bekanntes MCM-Zeichen seine Rolle wechselt.
Sie beschreibt keine Handlung, kein Gate und keine Richtung.

## Sicherheitsgrenze

- passiv only
- keine Entry-Wirkung
- keine Motorik
- keine Richtungsvorgabe
- keine harte Regel

## Profil

- Records: `8`

### Wechselqualitaeten

- `shift_verschwinden_zu_zentrum`: 2
- `shift_belastete_reifung_zu_zentrum`: 1
- `shift_nicht_sichtbar`: 1
- `shift_oberflaeche_zu_offen`: 1
- `shift_bruecke_zu_zentrum_getragen`: 1
- `shift_verlust_zu_randspur`: 1
- `shift_weltabhaengig_zu_rekopplung`: 1

### Zielrollen

- `nichtbruecke_zentrum_getragen`: 3
- `-`: 1
- `nichtbruecke_offen`: 1
- `nichtbruecke_randspannung`: 1
- `nichtbruecke_zentrum_schwach`: 1
- `nichtbruecke_rekopplungsfeld`: 1

## Records

| Shift | Token | Von | Nach | Beobachtungen | Welten | Note |
|---|---|---|---|---:|---:|---|
| `dio_shift_0ght6xc` | `1hdpu9s` | `langfristig_belastet_getragen` / `schwacher_anschluss` | `nichtbruecke_zentrum_getragen` / `rekopplungszone` | 4345 | 4 | Belastete Reifung bleibt sichtbar, verliert aber die Brueckenrolle. |
| `dio_shift_074qo7f` | `00nzcuc` | `kurzfristige_oberflaeche` / `schwacher_anschluss` | `-` / `-` | 0 | 0 | Zeichen bleibt in dieser Lesung unsichtbar. |
| `dio_shift_1v47ku0` | `00dz86x` | `kurzfristige_oberflaeche` / `schwacher_anschluss` | `nichtbruecke_offen` / `hoeherer_cluster_uebergang` | 10 | 3 | Kurzfristige Oberflaeche bleibt als offene Form sichtbar. |
| `dio_shift_01i725o` | `0z748ck` | `langfristig_getragen` / `lokaler_anschlussanker` | `nichtbruecke_zentrum_getragen` / `rekopplungszone` | 93 | 4 | Brueckenreifung bleibt als zentrumsnahe Feldform sichtbar. |
| `dio_shift_13ofdj9` | `00yl137` | `abgeschwaecht_oder_verloren` / `brueckenkern` | `nichtbruecke_randspannung` / `driftzone` | 3 | 2 | Vorher verlorene Reifung taucht als Randspannung wieder auf. |
| `dio_shift_0s2o4zp` | `0db07p4` | `verschwunden_bestaetigt` / `-` | `nichtbruecke_zentrum_schwach` / `stabile_bedeutungsinsel` | 64 | 1 | Verschwinden in Brueckenlogik war kein vollstaendiger Feldverlust. |
| `dio_shift_0lmqn9z` | `1ahj81f` | `verschwunden_bestaetigt` / `-` | `nichtbruecke_zentrum_getragen` / `stabile_bedeutungsinsel` | 240 | 3 | Verschwinden in Brueckenlogik war kein vollstaendiger Feldverlust. |
| `dio_shift_1dj11m9` | `0om13wf` | `weltabhaengig_getragen` / `brueckenkern` | `nichtbruecke_rekopplungsfeld` / `hoeherer_cluster_uebergang` | 19 | 4 | Weltabhaengige Reifung koppelt als Rekopplungsfeld wieder an. |

## Interpretation

Die Rollenwechsel-Memory trennt Bedeutungsverlust von Rollenverlust.
Ein Zeichen kann als Bruecke verschwinden und trotzdem als Zentrum, Rand, Rekopplungsfeld oder offene Oberflaeche erhalten bleiben.

## Wie es weitergeht

Als naechstes sollte diese `dio_shift_*` Memory gegen eine weitere Welt gelesen werden.
Dann wird sichtbar, ob Rollenwechsel selbst wiederkehrend sind oder nur eine einmalige Umlagerung der siebten Welt darstellen.