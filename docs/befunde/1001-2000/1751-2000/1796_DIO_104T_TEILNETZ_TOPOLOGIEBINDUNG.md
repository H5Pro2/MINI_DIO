# 1796 - `dio_104t` Teilnetz-Rollen und Topologiebindung

## Grundfrage

Die Prüfung liest die in 1795 gefundenen Nachbarrollen als Teilnetze.

Ziel ist nicht, neue Topologie zu erzwingen, sondern die vorhandenen Achsenabweichungen vorsichtig auf Zentrum, Brücke, Rand und Nachhall zu beziehen.

Quelle: `reports/dio_104t_neighbor_role_differentiation.csv`

## Rollenkarte

| Rollenklasse | Familien | Memories | Cosinus | Abstand | Topologie-Lesung | Delta-Profil | Stärkste Familien |
|---|---:|---:|---:|---:|---|---|---|
| `asymmetrie_plus` | 22 | 151.9091 | 0.958366 | 0.227805 | `rand_polarisierend` | `kohaerenz:0.032853; hoeren:0.003982; sehen:0.045157; asym:0.168627; feld:0.001879` | `dio_0kx9;dio_0nlj;dio_0n0i;dio_1kpz;dio_04q7;dio_087m;dio_00ly;dio_09bn` |
| `kohaerenz_hoeher` | 17 | 155.4118 | 0.979158 | 0.190965 | `zentrum_stabilisierend` | `kohaerenz:0.137025; hoeren:-0.009079; sehen:-0.049898; asym:-0.028336; feld:-0.009418` | `dio_1fll;dio_06er;dio_1492;dio_0pz6;dio_1ygx;dio_0ly7;dio_1350;dio_05ap` |
| `sehen_schaerfer` | 15 | 147.4667 | 0.965864 | 0.183878 | `sehen_formbindend` | `kohaerenz:-0.053678; hoeren:-0.00124; sehen:0.128821; asym:-0.01998; feld:0.003383` | `dio_19pg;dio_02xf;dio_1uof;dio_00ja;dio_1gp2;dio_0ein;dio_1j37;dio_1o4z` |
| `asymmetrie_minus` | 9 | 152.4444 | 0.972406 | 0.21336 | `rand_polarisierend` | `kohaerenz:0.078849; hoeren:0.021032; sehen:0.028266; asym:-0.154912; feld:0.00744` | `dio_13o0;dio_06s7;dio_17ct;dio_1rqi;dio_155c;dio_1mwv;dio_1xrt;dio_1jsj` |
| `hoeren_staerker` | 8 | 146.375 | 0.939149 | 0.248009 | `nachhall_aktivierend` | `kohaerenz:-0.046533; hoeren:0.176373; sehen:0.007399; asym:-0.069676; feld:0.077092` | `dio_0m9z;dio_0u1o;dio_169a;dio_0obq;dio_1r55;dio_1oye;dio_0oc3;dio_1pij` |
| `hoeren_leiser` | 5 | 150.4 | 0.976407 | 0.150021 | `nachhall_daempfend` | `kohaerenz:-0.020588; hoeren:-0.104593; sehen:0.00282; asym:0.004941; feld:-0.043794` | `dio_14wj;dio_1u5i;dio_1jc2;dio_1wdi;dio_02n3` |
| `zielnahe_mitrolle` | 3 | 154.0 | 0.9935 | 0.083028 | `bruecke_zielnah` | `kohaerenz:-0.019199; hoeren:-0.019976; sehen:0.014065; asym:-0.027901; feld:-0.007156` | `dio_0l7p;dio_0h9h;dio_1ewh` |
| `kohaerenz_niedriger` | 1 | 147.0 | 0.991665 | 0.104414 | `bruecke_zielnah` | `kohaerenz:-0.065627; hoeren:-0.065529; sehen:0.03071; asym:0.006495; feld:-0.022039` | `dio_1cic` |

## Befund

- Topologie-Lesungen: `rand_polarisierend:2;bruecke_zielnah:2;zentrum_stabilisierend:1;sehen_formbindend:1;nachhall_aktivierend:1;nachhall_daempfend:1`
- Die `dio_104t`-Nachbarschaft zeigt eine innere Staffelung: zielnahe Mitrollen, stabilisierende Kohärenzrollen, polarisierende Randrollen, Sehen-/Hören-Varianten und Übergangsrollen.
- Damit wird das Feldnetz nicht als eine einzelne Fläche gelesen, sondern als mehrere Teilnetze um denselben Anschlussknoten.

## Vorsicht

Diese Lesung ist eine passive Diagnose aus vorhandenen Achsenwerten. Sie ist kein Gate, keine Handlung und keine fest programmierte Topologie.
