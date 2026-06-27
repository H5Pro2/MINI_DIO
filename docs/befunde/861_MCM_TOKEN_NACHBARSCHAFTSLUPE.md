# MCM-Token Nachbarschaftslupe

## Zweck

Diese Diagnose prueft, welche MCM-Episodentokens vor und nach den Ziel-Tokens auftreten.
Damit wird unterschieden, ob ein Zonenwechsel am Token selbst haengt oder an veraenderter Nachbarschaft im Feld.

## Uebersicht

| Token | Kontakte | Welten | Dominant davor | Dominant danach | Dominantes Paar | Selbstbindung vorher/nachher | Nachbarrollen |
|---|---:|---:|---|---|---|---|---|
| dio_mcm_episode_0v5p8er | 2013 | 4 | dio_mcm_episode_0v5p8er (1997) | dio_mcm_episode_0v5p8er (1997) | dio_mcm_episode_0v5p8er->dio_mcm_episode_0v5p8er (1984) | 0.9921/0.9921 | zentrum_stabil:3400; offene_variante:615; spannungsrand_kippnaehe:11 |
| dio_mcm_episode_14l8khu | 906 | 3 | dio_mcm_episode_14l8khu (888) | dio_mcm_episode_14l8khu (888) | dio_mcm_episode_14l8khu->dio_mcm_episode_14l8khu (873) | 0.9801/0.9801 | zentrum_stabil:1390; offene_variante:418; spannungsrand_kippnaehe:4 |
| dio_mcm_episode_1q3us3f | 1763 | 6 | dio_mcm_episode_1q3us3f (1737) | dio_mcm_episode_1q3us3f (1737) | dio_mcm_episode_1q3us3f->dio_mcm_episode_1q3us3f (1721) | 0.9853/0.9853 | zentrum_stabil:3125; offene_variante:394; spannungsrand_kippnaehe:7 |
| dio_mcm_episode_1xx3u1e | 3060 | 4 | dio_mcm_episode_1xx3u1e (3037) | dio_mcm_episode_1xx3u1e (3037) | dio_mcm_episode_1xx3u1e->dio_mcm_episode_1xx3u1e (3018) | 0.9925/0.9925 | zentrum_stabil:5201; offene_variante:904; spannungsrand_kippnaehe:15 |

## Bewegungsachsen Zum Nachfolger

| Token | Rekopplung | Strain | Lautheit | Unschaerfe | Spannung |
|---|---:|---:|---:|---:|---:|
| dio_mcm_episode_0v5p8er | -0.0001 | 0.0001 | -0.0005 | 0.0008 | -0.0002 |
| dio_mcm_episode_14l8khu | -0.0005 | 0.0004 | 0.0027 | 0.0002 | 0.0012 |
| dio_mcm_episode_1q3us3f | -0.0005 | 0.0007 | 0.0027 | 0.0010 | 0.0012 |
| dio_mcm_episode_1xx3u1e | -0.0003 | 0.0002 | 0.0013 | 0.0002 | 0.0006 |

## Befund

- `dio_mcm_episode_0v5p8er`: starke Selbstnachbarschaft; dominanter Nachfolger `dio_mcm_episode_0v5p8er`.
- `dio_mcm_episode_14l8khu`: starke Selbstnachbarschaft; dominanter Nachfolger `dio_mcm_episode_14l8khu`.
- `dio_mcm_episode_1q3us3f`: starke Selbstnachbarschaft; dominanter Nachfolger `dio_mcm_episode_1q3us3f`.
- `dio_mcm_episode_1xx3u1e`: starke Selbstnachbarschaft; dominanter Nachfolger `dio_mcm_episode_1xx3u1e`.

## Gesamtlesart

Wenn ein Token in eine stabile oder rekoppelnde Nachbarschaft eingebettet ist, wirkt sein Zonenwechsel weniger wie isolierter Kontakt und mehr wie Feldbewegung.
Wenn die Nachbarschaft wechselhaft wird oder die Selbstbindung sinkt, ist Drift eher als Veraenderung des lokalen Feldraums zu lesen.

## Wie es weitergeht

Als naechstes sollten die Nachbarschaftsmuster gegen die Verdichtungszonen klassifiziert werden: stabile Insel, rekoppelnder Pfad, offene Drift oder Randpfad.
