# 1183 - Brueckennetz Biasfamilien: Feldrollen

## Grundfrage

Die vorherige Pruefung zeigte ein gemeinsames Brueckennetz mit richtungsabhaengiger Drift.
Diese Diagnose prueft, ob die Biasfamilien im Brueckennetz eigene Feldrollen tragen oder nur Oberflaechen-Nachbarn sind.

Die Pruefung bleibt passiv. Es wird keine Handlung, kein Gate und keine Strategie abgeleitet.

## Rollenuebersicht

| Feldrollen-Lesung | Familien | Ereignisse | Rekopplung | Carry | Strain | Tension |
|---|---:|---:|---:|---:|---:|---:|
| gemischte_nachbarschaft | 3 | 106 | 0.6995 | 0.5293 | 0.1528 | 0.0823 |
| stabilisierende_rueckbindung | 2 | 74 | 0.7217 | 0.5464 | 0.1220 | 0.0527 |
| spannungsnahe_belastung | 1 | 60 | 0.6962 | 0.5284 | 0.1692 | 0.1703 |
| kohaerente_bruecke | 2 | 58 | 0.7126 | 0.5400 | 0.1394 | 0.0930 |
| uebergang_oeffnung | 1 | 42 | 0.7090 | 0.5350 | 0.1494 | 0.1343 |

## Familien

| Familie | Bias | Ereignisse | Welten | Rolle | Segmentprofil | Phasenprofil |
|---|---|---:|---:|---|---|---|
| dio_00ja | staerker_00ly_zu_104t | 36 | 3 | gemischte_nachbarschaft | form_ton_wechsel:16;tonaler_wechsel_in_stabilitaet:12;tieferer_tonraum:8 | before:20;after:10;between:6 |
| dio_1uof | staerker_00ly_zu_104t | 36 | 3 | gemischte_nachbarschaft | tieferer_tonraum:14;ruhige_rekopplung:12;offene_stabile_lage:6;tonaler_wechsel_in_stabilitaet:2 | before:14;between:12;after:10 |
| dio_1lsu | staerker_00ly_zu_104t | 34 | 3 | gemischte_nachbarschaft | form_ton_wechsel:18;tonaler_wechsel_in_stabilitaet:12;hoehere_feldspannung:4 | before:14;after:10;between:10 |
| dio_17ct | staerker_00ly_zu_104t | 34 | 3 | kohaerente_bruecke | tonaler_wechsel_in_stabilitaet:19;form_ton_wechsel:5;hoehere_feldspannung:4;tieferer_tonraum:4 | before:18;between:14;after:2 |
| dio_0tay | staerker_104t_zu_00ly | 24 | 2 | kohaerente_bruecke | tieferer_tonraum:14;ruhige_rekopplung:6;hellerer_tonraum:2;tonaler_wechsel_in_stabilitaet:2 | between:14;after:8;before:2 |
| dio_0oc3 | staerker_104t_zu_00ly | 60 | 3 | spannungsnahe_belastung | form_ton_wechsel:50;tonaler_wechsel_in_stabilitaet:8;hoehere_feldspannung:2 | before:22;after:22;between:16 |
| dio_06s7 | staerker_00ly_zu_104t | 46 | 3 | stabilisierende_rueckbindung | ruhige_rekopplung:24;tonaler_wechsel_in_stabilitaet:14;form_ton_wechsel:6;hellerer_tonraum:2 | after:28;before:10;between:8 |
| dio_1kpz | staerker_104t_zu_00ly | 28 | 3 | stabilisierende_rueckbindung | ruhige_rekopplung:14;tonaler_wechsel_in_stabilitaet:10;form_ton_wechsel:2;tieferer_tonraum:2 | after:16;between:6;before:6 |
| dio_1r55 | staerker_00ly_zu_104t | 42 | 2 | uebergang_oeffnung | tonaler_wechsel_in_stabilitaet:28;hoehere_feldspannung:8;form_ton_wechsel:6 | between:18;before:14;after:10 |

## Befund

Die Biasfamilien sind nicht gleichfoermig verteilt.
Sie fallen in mehrere Feldrollen:

- `gemischte_nachbarschaft`: dio_00ja, dio_1uof, dio_1lsu
- `kohaerente_bruecke`: dio_17ct, dio_0tay
- `spannungsnahe_belastung`: dio_0oc3
- `stabilisierende_rueckbindung`: dio_06s7, dio_1kpz
- `uebergang_oeffnung`: dio_1r55

Damit spricht die aktuelle Datenlage nicht fuer reine Oberflaechen-Nachbarschaft.
Die Familien tragen unterschiedliche lokale Feldqualitaeten innerhalb desselben Brueckennetzes.

## Grenze

Die Rollen sind diagnostische Lesungen aus passiven Fenstern.
Sie beweisen noch keine autonome Bedeutungsentscheidung von MINI_DIO.
Stark ist aber: Die gleichen Biasfamilien lassen sich nicht nur zaehlen, sondern auch feldqualitativ unterscheiden.

## Wie es weitergeht

Als naechstes sollte geprueft werden, ob diese Feldrollen in einer neuen Welt erneut auftreten oder ob sie unter anderer Weltspannung in andere Rollen kippen.
