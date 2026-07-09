# Befund 251 - Folgewelt-Stuetze der Randspannung

Stand: 2026-06-19

## Ausgangspunkt

Die vorherige Diagnose zeigte mehrere seltene Kippvarianten:

```text
dio_mcm_episode_037i64j
dio_mcm_episode_0e9ekzq
dio_mcm_episode_0eje6op
dio_mcm_episode_182yyt2
```

Diese Varianten wirkten rand- und spannungsnah, waren aber zunaechst nur in `PREVIEW_REAL_2023` sichtbar.

Die Grundfrage war:

```text
Tauchen diese Rand-/Spannungszeichen in einer weiteren Realwelt wieder auf,
oder bleiben sie situative Einzelzeichen?
```

## Folgewelt

Als Folgewelt wurde erzeugt:

```text
PREVIEW_REAL2_2023
data/kontrolliert_2023_real_test2_1000_5m_SOLUSDT.csv
```

Die Laeufe blieben passiv:

```text
trades=0
reward=0
```

## Ergebnis

Die Rand-/Spannungsgruppe bleibt deutlich vom Rekopplungsraum getrennt.

Vergleich:

```text
Rekopplungsfamilie:
72 Fenster
4 Welten
meist lokal_rekoppelnd
meist stabil / inner_effect_stable

Kippvarianten:
10 Fenster
2 Welten
immer lokale_multisensorische_kippnaehe
immer tragend_unruhig / inner_effect_carried_unrest
```

Wichtigster neuer Punkt:

```text
dio_mcm_episode_182yyt2
```

Dieses Kippzeichen erscheint jetzt in zwei Realwelten:

```text
PREVIEW_REAL_2023
PREVIEW_REAL2_2023
```

Damit ist es nicht mehr nur ein einzelnes isoliertes Randzeichen.
Es besitzt eine erste Folgewelt-Stuetze.

## Lesart

`dio_mcm_episode_182yyt2` ist aktuell der interessanteste Kandidat fuer eine entstehende Randspannungsfamilie.

Die Gruppe zeigt gegenueber Rekopplung:

- hoeheren Felddruck,
- hoehere Kippnaehe,
- geringere Rekopplung,
- geringere Entlastung,
- stabile Kopplung an `tragend_unruhig`.

Das spricht fuer:

```text
Randspannung ist nicht nur Stoerung.
Sie kann als wiederkehrende Innenfeldlage auftreten.
```

Die Grenze bleibt:

```text
Eine Folgewelt-Stuetze ist ein Hinweis,
aber noch keine stabile MCM-Familie.
```

## Bedeutung fuer Regulation

Die Anspannung ist damit nicht beseitigt.
Sie wird aber differenzierter:

```text
allgemeine Rekopplung
  -> haeufig, stabil, mehrwelttragend

Randspannung
  -> seltener, kippnah, unruhig, erste Folgewelt-Stuetze
```

Das ist fuer MINI_DIO wichtig, weil Regulation nicht als Wegdruecken von Spannung gelesen wird.
Regulation bedeutet hier:

```text
Das Feld erkennt, ob Spannung rekoppelt, driftet oder als Randlage wiederkehrt.
```

## Wie es weitergeht

Als naechstes wird `dio_mcm_episode_182yyt2` gezielt gegen weitere Real- und Stresswelten gelegt.

Grundfrage:

```text
Bleibt 182yyt2 eine Realwelt-Randspannung,
oder taucht es auch unter Stresswelt-Bedingungen auf?
```

Unterpruefung:

```text
182yyt2 gegen Kippdruck, Felddruck, Rekopplung und Entlastung in mehreren Welten vergleichen.
```

Folgeschritt:

```text
Nur wenn 182yyt2 ueber mehrere Weltfamilien wiederkehrt,
kann es als Kandidat einer stabileren passiven Spannungsfamilie gelten.
```
