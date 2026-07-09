# 1795 - `dio_104t` Nachbarn: Rollen-Differenzierung

## Grundfrage

Die Prüfung liest, ob die stärksten Nachbarn von `dio_104t` eigene Rollen tragen oder nur dieselbe Feldphase wiederholen.

Verglichen wird jeweils nur dort, wo Zielknoten und Nachbar in derselben Achsen-Memory aktiv sind.

## Kurzbefund

- gelesene Nachbarn: `80`
- Rollenprofil: `asymmetrie_plus:22; kohaerenz_hoeher:17; sehen_schaerfer:15; asymmetrie_minus:9; hoeren_staerker:8; hoeren_leiser:5; zielnahe_mitrolle:3; kohaerenz_niedriger:1`

## Stärkste Nachbarn nach gemeinsamer Präsenz

| Nachbar | Memories | Cosinus | Abstand | Rollenlesung | stärkste Abweichung | Quellenprofil |
|---|---:|---:|---:|---|---|---|
| `dio_1fll` | 163 | 0.9646 | 0.2108 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1367` | `btc:46;sonstige:32;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_13o0` | 163 | 0.9680 | 0.2013 | `asymmetrie_minus` | `mcm_asymmetrie:-0.1151` | `btc:46;sonstige:32;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_1492` | 163 | 0.9800 | 0.1769 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1157` | `btc:46;sonstige:32;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0kx9` | 163 | 0.9681 | 0.1734 | `asymmetrie_plus` | `mcm_asymmetrie:0.1173` | `btc:46;sonstige:32;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_06er` | 163 | 0.9800 | 0.1731 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1362` | `btc:46;sonstige:32;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_14wj` | 163 | 0.9844 | 0.1228 | `hoeren_leiser` | `hoeren_stimulation:-0.1024` | `btc:46;sonstige:32;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0nlj` | 162 | 0.9764 | 0.1887 | `asymmetrie_plus` | `mcm_asymmetrie:0.1283` | `btc:46;sonstige:32;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_0n0i` | 161 | 0.9642 | 0.2113 | `asymmetrie_plus` | `mcm_asymmetrie:0.1313` | `btc:45;sonstige:32;doge:25;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0pz6` | 161 | 0.9869 | 0.1709 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1215` | `btc:46;sonstige:30;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_1kpz` | 161 | 0.9788 | 0.1435 | `asymmetrie_plus` | `mcm_asymmetrie:0.1217` | `btc:46;sonstige:31;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_04q7` | 160 | 0.9521 | 0.2717 | `asymmetrie_plus` | `mcm_asymmetrie:0.2295` | `btc:45;sonstige:32;doge:26;xrp:24;paxg:24;expansion:3;sideways:3;stress:3` |
| `dio_1ygx` | 160 | 0.9644 | 0.2163 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1370` | `btc:45;sonstige:32;doge:25;xrp:24;paxg:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0ly7` | 160 | 0.9730 | 0.2106 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1568` | `btc:46;sonstige:30;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_1350` | 160 | 0.9899 | 0.1297 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1071` | `btc:46;sonstige:30;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_087m` | 159 | 0.9576 | 0.2785 | `asymmetrie_plus` | `mcm_asymmetrie:0.2386` | `btc:46;sonstige:29;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_05ap` | 159 | 0.9765 | 0.1952 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1477` | `btc:46;sonstige:29;doge:26;xrp:24;paxg:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_06s7` | 159 | 0.9835 | 0.1251 | `asymmetrie_minus` | `mcm_asymmetrie:-0.1008` | `btc:46;sonstige:28;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0l7p` | 159 | 0.9947 | 0.0707 | `zielnahe_mitrolle` | `hoeren_stimulation:-0.0567` | `btc:46;sonstige:28;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_1rqi` | 157 | 0.9665 | 0.2592 | `asymmetrie_minus` | `mcm_asymmetrie:-0.2134` | `btc:46;sonstige:28;doge:25;xrp:24;paxg:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_17ct` | 157 | 0.9844 | 0.2014 | `asymmetrie_minus` | `mcm_asymmetrie:-0.1221` | `btc:46;doge:26;sonstige:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0tay` | 157 | 0.9966 | 0.1159 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1105` | `btc:46;sonstige:27;doge:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_09bn` | 156 | 0.9843 | 0.1784 | `asymmetrie_plus` | `mcm_asymmetrie:0.1276` | `btc:46;doge:26;sonstige:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_0dd2` | 156 | 0.9882 | 0.1541 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1325` | `btc:46;doge:26;sonstige:26;paxg:25;xrp:24;expansion:3;sideways:3;stress:3` |
| `dio_00ly` | 156 | 0.9852 | 0.1210 | `asymmetrie_plus` | `mcm_asymmetrie:0.1182` | `btc:46;doge:26;paxg:25;sonstige:25;xrp:24;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_1u5i` | 154 | 0.9824 | 0.1398 | `hoeren_leiser` | `hoeren_stimulation:-0.1052` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:24;expansion:3;sideways:3;stress:3` |
| `dio_19pg` | 154 | 0.9871 | 0.1161 | `sehen_schaerfer` | `sehen_form_salience:0.1109` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:23;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0h9h` | 154 | 0.9908 | 0.0971 | `zielnahe_mitrolle` | `mcm_asymmetrie:-0.0931` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:23;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0g3b` | 153 | 0.9626 | 0.2238 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1434` | `btc:45;sonstige:32;paxg:24;doge:22;xrp:20;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_1s2n` | 153 | 0.9678 | 0.1855 | `asymmetrie_plus` | `mcm_asymmetrie:0.1304` | `btc:42;sonstige:30;doge:26;xrp:23;paxg:23;expansion:3;sideways:3;stress:3` |
| `dio_1q85` | 153 | 0.9935 | 0.1541 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1109` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:23;expansion:3;sideways:3;stress:3` |
| `dio_02xf` | 152 | 0.9673 | 0.1729 | `sehen_schaerfer` | `sehen_form_salience:0.1285` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:21;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_1uof` | 151 | 0.9564 | 0.1992 | `sehen_schaerfer` | `sehen_form_salience:0.1278` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:20;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_07uk` | 150 | 0.9533 | 0.3108 | `asymmetrie_plus` | `mcm_asymmetrie:0.2483` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:20;expansion:3;sideways:3;stress:3` |
| `dio_1qyl` | 150 | 0.9289 | 0.2816 | `asymmetrie_plus` | `mcm_asymmetrie:0.2471` | `btc:43;sonstige:29;doge:25;xrp:23;paxg:21;expansion:3;sideways:3;stress:3` |
| `dio_10dv` | 150 | 0.9749 | 0.2187 | `kohaerenz_hoeher` | `mcm_kohaerenz:0.1309` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:20;expansion:3;sideways:3;stress:3` |
| `dio_00pl` | 150 | 0.9512 | 0.2102 | `asymmetrie_plus` | `mcm_asymmetrie:0.1289` | `btc:46;doge:26;paxg:25;xrp:23;sonstige:20;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_00ja` | 150 | 0.9729 | 0.1571 | `sehen_schaerfer` | `sehen_form_salience:0.1287` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:19;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_155c` | 150 | 0.9790 | 0.1546 | `asymmetrie_minus` | `mcm_asymmetrie:-0.1011` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:19;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_0u1o` | 149 | 0.9452 | 0.2920 | `hoeren_staerker` | `hoeren_stimulation:0.2079` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:18;expansion:3;sideways:3;stress:3;synth:1` |
| `dio_1mwv` | 149 | 0.9648 | 0.2856 | `asymmetrie_minus` | `mcm_asymmetrie:-0.2147` | `btc:46;doge:26;paxg:25;xrp:24;sonstige:18;expansion:3;sideways:3;stress:3;synth:1` |

## Interpretation

Die Nachbarschaft von `dio_104t` ist kein homogener Block.
Ein Teil liegt sehr nah am Zielknoten, ein anderer Teil trägt klare Abweichungen über Kohärenz, Hören, Sehen, Asymmetrie oder Feldkontakt.

Fachliche Lesung:

```text
Mitläufer = ähnliche Achsenlage im selben Bedeutungsraum.
Eigenrolle = wiederkehrende Nachbarschaft mit stabiler Achsenabweichung.
```

Damit wirkt der Bedeutungsraum wie ein differenziertes Feldnetz, nicht wie eine einzige breite Sammelfamilie.

## Wie es weitergeht

Als nächstes sollte eine Teilnetz-Prüfung die Rollen `asymmetrie_plus, kohaerenz_hoeher, sehen_schaerfer, asymmetrie_minus` getrennt lesen: Welche Rolle bindet Zentrum, Brücke, Rand oder Nachhall?
