# 1989 - PEPE-C Ruecklesung der Rolle 1yxc2ug

## Grundfrage

PEPE-C hat `dio_mcm_episode_0hiolzy` nicht erneut aktiviert. Stattdessen wurde `dio_mcm_episode_1yxc2ug` deutlich gestaerkt. Diese Ruecklesung prueft:

Ist `1yxc2ug` eine Ersatzrolle fuer `0hiolzy`, oder handelt es sich um eine andere Art von Rekopplung?

## Datenbasis

- Welt: `FOLLOW_EQ10K_PEPE_C_2024_5M`
- Debuglauf: `debug/1988_equal10k_pepe_c_2024_5m/dio_mini_lauf_49/episodes.csv`
- Rohwelt: `data/kontrolliert_pepe_2024_5m_10k_c_PEPEUSDT.csv`
- Zielrolle: `dio_mcm_episode_1yxc2ug`
- Segmenttabelle: `docs/befunde/1001-2000/1751-2000/1989_MCM_PEPE_C_1YXC2UG_SEGMENTE.csv`

## Grobbefund

`1yxc2ug` trat in PEPE-C 304-mal direkt auf. Die Treffer verteilen sich auf 26 Segmente. Anders als `0hiolzy` bildet diese Rolle kein langes dominantes Hauptsegment.

Die laengsten Segmente:

| Start | Ende | Laenge | Feldwirkung | dominante Zeitlage |
|---:|---:|---:|---|---|
| 3938 | 3968 | 31 | ueberwiegend `field_carried` | `temporal_far_return` |
| 3849 | 3878 | 30 | gemischt, aber getragen | `temporal_far_return` |
| 3670 | 3697 | 28 | ueberwiegend `field_carried` | `temporal_far_return` |
| 6607 | 6634 | 28 | ueberwiegend `field_carried` | `temporal_far_return` |
| 3632 | 3651 | 20 | ueberwiegend `field_carried` | `temporal_far_return` |

## Feldprofil gegenueber dem Rest der PEPE-C-Welt

`1yxc2ug` zeigt gegenueber dem Rest der PEPE-C-Welt:

- weniger Tragqualitaet: `mcm_carry_quality` ca. 0.544 statt 0.553
- leicht mehr Feldspannung: `mcm_strain_quality` ca. 0.174 statt 0.172
- weniger Rekopplung: `mcm_rekopplung_quality` ca. 0.700 statt 0.706
- weniger Sinneskopplung: `mcm_sensory_coupling` ca. 0.826 statt 0.838
- deutlich mehr visuelle Feldluecke: `mcm_visual_field_gap` ca. 0.232 statt 0.185
- etwas weniger Hoer-Feld-Luecke: `mcm_hearing_field_gap` ca. 0.089 statt 0.104
- weniger Nachhall: `mini_afterimage` ca. 0.617 statt 0.668
- weniger Wiederkehr: `mini_recurrence_strength` ca. 0.666 statt 0.726
- mehr visueller Rezeptorkontakt: `rezeptor_visual_contact` ca. 0.352 statt 0.291
- weniger visuelle Schaerfe: `perception_visual_sharpness` ca. 0.605 statt 0.649
- deutlich negativerer Energieton: `hoeren_energy_tone` ca. -0.045 statt -0.005

Damit ist `1yxc2ug` keine ruhige, nachhallstarke Milieuinsel wie `0hiolzy`.

## Rohweltprofil

Gegenueber dem Rest der PEPE-C-Welt liegt `1yxc2ug` in einer deutlich aktiveren Rohweltlage:

- hoehere durchschnittliche Range: ca. 0.01042 statt 0.00694
- deutlich hoeheres Volumen: ca. 300 Mrd. statt 166 Mrd.
- leicht positivere Kerzenrendite
- breitere Preiszone als bei der spaeten `0hiolzy`-Phase

Die Rolle liest also eher aktive, rauere, visuell staerker beanspruchende Weltbereiche.

## Vergleich zu 0hiolzy

`0hiolzy` in PEPE-A:

- ein dominantes langes Hauptsegment
- hoher Nachhall
- hohe Wiederkehr
- geringe Hoer-Luecke
- geringere Kontaktspannung
- eher ruhige Rekopplung

`1yxc2ug` in PEPE-C:

- viele kuerzere Segmente
- weniger Nachhall und Wiederkehr
- mehr visuelle Luecke
- mehr visueller Kontakt
- hoehere Rohweltaktivitaet
- rauerer Energieton

## Interpretation

`1yxc2ug` ist keine Ersatzrolle fuer `0hiolzy`. Es handelt sich eher um eine breite Grundrollen-Rekopplung in aktiveren PEPE-C-Bereichen.

Die Rolle wirkt wie:

> Eine aktive, mehrfach auftretende Rekopplungsform, die visuell staerker beansprucht, weniger nachhallgetragen ist und in dynamischeren Weltabschnitten erscheint.

Damit zeigt PEPE-C nicht die Wiederkehr der PEPE-A-Milieuinsel, sondern eine andere Art von Feldnaehe.

## Schlussfolgerung

Die PEPE-Fenster bilden keine starre Symbolfamilie. PEPE-A erzeugt eine situative Milieuinsel (`0hiolzy`), PEPE-C staerkt eine breitere, aktivere Grundrollen-Rekopplung (`1yxc2ug`). Das unterstuetzt die Arbeitshypothese, dass MINI_DIO Bedeutungen aus konkreten Feldphasen bildet und nicht aus oberflaechlichen Asset-Labels.

## Wie es weitergeht

Als naechstes sollte ein direkter Profilvergleich zwischen `0hiolzy` und `1yxc2ug` als kompakte Tabelle erzeugt werden. Danach kann geprueft werden, ob andere Assets aehnliche aktive Grundrollen-Rekopplungen bilden.
