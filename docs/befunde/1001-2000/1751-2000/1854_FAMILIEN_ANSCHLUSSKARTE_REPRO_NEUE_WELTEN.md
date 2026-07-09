# 1854 - Familien-Anschlusskarte gegen neue Welten

## Grundfrage

Taucht die passive Familien-Anschlusskarte aus `1851/1852` in neuen Weltfenstern wieder auf, oder driftet sie?

## Methode

- Baseline: Asset/Familien-Anschlussprofile aus `1851`.
- Folge: neue Fenster aus `1853`.
- Verglichen wird pro Asset/Familie die dominante Anschlussqualität.
- Keine Handlung, kein Gate, keine Richtung.

## Kurzbefund

- Asset/Familien-Paare: `206`
- Reproduktionszustände: `anschlussqualitaet_driftet_offen:149; anschlussqualitaet_driftet:38; neu_ohne_baseline:10; anschlussqualitaet_reproduziert:9`
- Folge-Qualitäten: `kernnah:120; offen_gemischt:43; nullnah:36; kernnah_ohne_feldzeit:7`

## Wiederkehrende Profile

| Asset | Familie | Baseline | Folge | Profil | Zustand |
|---|---|---|---|---|---|
| PAXG | `dio_0fe7` | `kernnah` | `kernnah` | `kernnah:1; offen_gemischt:1` | `anschlussqualitaet_reproduziert` |
| PAXG | `dio_09bn` | `kernnah` | `kernnah` | `kernnah:1` | `anschlussqualitaet_reproduziert` |
| PAXG | `dio_0nlj` | `offen_gemischt` | `offen_gemischt` | `offen_gemischt:1` | `anschlussqualitaet_reproduziert` |
| PAXG | `dio_12fw` | `offen_gemischt` | `offen_gemischt` | `offen_gemischt:1` | `anschlussqualitaet_reproduziert` |
| PAXG | `dio_19pg` | `kernnah` | `kernnah` | `kernnah:1` | `anschlussqualitaet_reproduziert` |
| PAXG | `dio_1gp2` | `offen_gemischt` | `offen_gemischt` | `offen_gemischt:1` | `anschlussqualitaet_reproduziert` |
| PAXG | `dio_1xrt` | `kernnah` | `kernnah` | `kernnah:1` | `anschlussqualitaet_reproduziert` |
| XRP | `dio_06jk` | `kernnah_ohne_feldzeit` | `kernnah_ohne_feldzeit` | `kernnah_ohne_feldzeit:1` | `anschlussqualitaet_reproduziert` |
| XRP | `dio_1tiu` | `kernnah_ohne_feldzeit` | `kernnah_ohne_feldzeit` | `kernnah_ohne_feldzeit:1` | `anschlussqualitaet_reproduziert` |

## Driftende Profile

| Asset | Familie | Baseline | Folge | Profil | Zustand |
|---|---|---|---|---|---|
| BTC | `dio_00ja` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_00ly` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_04uf` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_06er` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_06jk` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_06s7` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_09bn` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0dd2` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0g2r` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0h9h` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0l7p` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0m9z` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0nlj` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0obq` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0oc3` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0pz6` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_0tay` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_104t` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_1492` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |
| BTC | `dio_14wj` | `nachhallnah_ohne_kern` | `kernnah` | `kernnah:2` | `anschlussqualitaet_driftet` |

## Einordnung

Die passive Familien-Anschlusskarte zeigt Wiederkehr, aber keine starre Kopie.
Ein Teil der Asset/Familien-Paare reproduziert seine Anschlussqualität, ein größerer Teil driftet offen.
Das ist methodisch sinnvoll: Das Feld speichert keinen festen Symbolwert, sondern eine kontextabhängige Anschlusslage.

Damit bleibt die bisherige Linie erhalten:
`Familie + Weltkontext + Anschlussqualität` ist tragfähiger als eine isolierte Familienbedeutung.
