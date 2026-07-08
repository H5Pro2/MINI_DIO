# 1817 - `dio_1fll` Randnähe und Rekopplung Recheck

## Grundfrage

`dio_1fll` wurde in 1807 aggregiert als randnaher Sammelknoten gelesen.

Die Tickfensterprüfung aus 1816 zeigte aber eine durchgehend starke Rekopplung. Diese Prüfung klärt, ob `dio_1fll` eher Randknoten oder gehaltener Sammelknoten ist.

Die Diagnose bleibt passiv. Sie erzeugt keine Handlung, kein Gate und keine Richtung.

## Quellen

- `reports/core_family_bridge_character.csv`
- `reports/core_family_role_taxonomy.csv`
- `reports/dio_1fll_bridge_tick_windows.csv`
- `reports/dio_1fll_bridge_tick_window_signature.csv`

## Aggregierte Nachbarschaft

`dio_1fll` besitzt in der Brückencharakter-Prüfung:

- `bridge_score`: 0.465
- `avg_distance`: 0.264148
- `role_diversity`: 6
- `roles`: `asymmetrie_plus`, `asymmetrie_minus`, `hoeren_staerker`, `kohaerenz_niedriger`, `sehen_schaerfer`, `zielnahe_mitrolle`
- `topology_bindings`: stark `rand_polarisierend`, dazu `nachhall_aktivierend`, `gemischte_uebergangsrolle`, `sehen_formbindend`, `bruecke_zielnah`

Das spricht für ein breites, polarisiertes Umfeld.

## Konkretes Tickfenster

In den geprüften Tickfenstern erscheint `dio_1fll` nur als `tragende_verarbeitung`.

Die Feldfolge:

| Phase | Feld | Spannung | Rekopplung | Strain | Ton |
|---|---|---:|---:|---:|---|
| Vorlauf | `rekoppelt` | 0.062283 | 0.743598 | 0.123714 | `geordnetes_hinhoeren` |
| Ereignis | `rekoppelt` | 0.009432 | 0.779410 | 0.107528 | `geordnetes_hinhoeren` |
| Nachlauf | `rekoppelt` | 0.108537 | 0.734161 | 0.147561 | `geordnetes_hinhoeren` |

Die Rohzählung der Fenster zeigt:

- 46 Zeilen `rekoppelt`
- 14 Zeilen `belastet_kippnah`
- 8 Zeilen `offen`

## Befund

`dio_1fll` ist wahrscheinlich nicht einfach ein Randknoten.

Sauberer ist:

`dio_1fll` wirkt wie ein gehaltener Sammelknoten mit randnaher Umgebung.

Das bedeutet:

- Die Nachbarschaft ist breit, distanziert und polarisiert.
- Der konkrete Ereigniskern bleibt aber stark rekoppelt.
- Randnähe beschreibt hier eher das Umfeld, nicht den Kern der Feldfolge.

Damit wird die Rollentaxonomie präziser: Eine Familie kann aggregiert randnah wirken und trotzdem im konkreten Ereignis rekoppelnd halten.

## Schluss

Für MINI_DIO ist das wichtig, weil Bedeutungsrollen nicht nur über Summenwerte gelesen werden dürfen.

Eine Rolle braucht mindestens drei Ebenen:

- Nachbarschaft: Welche Familien liegen im selben Feldraum?
- Feldfolge: Was passiert vor, im und nach dem Ereignis?
- Weltphase: In welchem Sinnes- und MCM-Milieu tritt die Familie auf?

## Wie es weitergeht

Als nächstes sollte `dio_1fll` gegen weitere Weltfenster geprüft werden. Entscheidend ist, ob die gehaltene Rekopplung auch außerhalb der aktuellen PAXG-5m-Fenster sichtbar bleibt.
