# Projektstatus

Stand: 2026-06-19

MINI_DIO wurde aus dem grossen `MCM_Trading_Brain`-Projekt als eigenstaendiges Forschungsprojekt angelegt.

## Entkopplungsstand

Fachlich:

- Mini-DIO besitzt eigenen Kern.
- Mini-DIO nutzt eigene MCM-Neuronen, eigene Weltlesung, eigene Semantik und eigene passive Reports.
- Keine direkte Runtime-Abhaengigkeit auf `bot.py`, `MCM_Brain_Modell.py`, `core/` oder `trading/`.

Technisch:

- Kernpaket liegt unter `mini_dio/`.
- Forschungsskripte liegen unter `reports/`.
- Befunde liegen unter `docs/befunde/`.
- Lokale Daten, Memory und Debug-Ausgaben sind getrennt.

## Offene Aufraeumarbeiten

- Historische Reports weiter kuratieren.
- Einheitliche CLI-Kommandos fuer die aktuelle Forschungskette bauen.
- Kleine Testdaten dauerhaft eincheckbar halten.
- Grosse Daten und Debug-Ausgaben nicht in Git aufnehmen.
- Tests fuer Kernfunktionen ergaenzen.
- Organische Reizadaptation weiter passiv pruefen, bevor sie in den Kern wandert.
- Feldhistorie gegen Weltstruktur weiter pruefen: aktuelle Naeherung nutzt Feldlast, Memorylast und Rekopplungsverlust.
- SOL 5m als harmonisches Referenzprofil weiter verwenden, aber nicht als feste Regel oder bevorzugte Zeitaufloesung.
- Organische Adaptionsachsen weiter passiv pruefen: Feldabstand, Memory-Last, Rekopplung, Dauerlast, Nachhall und Reizbasis.
- Auditive Regulation als passive Sinnesachse weiter pruefen: Hinhoeren, Rauschen filtern, Reiz abklingen lassen, genauer Anhoeren, Alarm, Hintergrund und Beruhigung.
- Auditive Feldkopplung weiter passiv pruefen: Hoerzustand gegen Feldlast, Memorylast und Rekopplung legen.
- Visuelle Regulation als passive Sinnesachse weiter pruefen: Formfluss, Formwechsel, Formstabilitaet, visueller Feldabstand, Hintergrund, Rauschen, Alarmform und Fokus.
- Visuelle Feldkopplung weiter passiv pruefen: Sehzustand gegen Feldlast, Memorylast und Rekopplung legen.
- Hoeren, Sehen und Fuehlen als getrennte Sinnesachsen halten und erst danach multisensorisch vergleichen.
- Multisensorische Kopplung weiter passiv pruefen: gemeinsame Sinnesinnenlage zuerst auf Gesamtwelt lesen, danach lokale Kippzonen innerhalb einzelner Welten suchen.
- Lokale multisensorische Kopplung weiter passiv pruefen: Top-Kippfenster und Top-Rekopplungsfenster gegen eigene Syntax/Familien legen.
- Lokale multisensorische Syntax weiter passiv pruefen: wiederkehrende Symbolfamilien von echter MCM-Feld-Episodenverdichtung trennen.
- Frische Laeufe mit `mcm_field_episode_preview_symbol` erzeugen und danach lokale Feld-Episoden-Vorschau gegen Kipp-/Rekopplungsfenster pruefen.
- Die frischen Preview-Laeufe `debug/preview_syntax_chain_01/` zeigen: lokale Rekopplungsfenster tragen reproduzierbar starke `dio_mcm_episode_*`-Vorschau-Familien, lokale Kippfenster tragen andere Vorschau-Familien mit unruhigerer Innenfeldwirkung.
- Die Mehrwelt-Preview-Pruefung zeigt eine gemeinsame lokale Vorschau-Grundsprache: `dio_mcm_episode_02xikfk` tritt weltuebergreifend stark in Rekopplungsfenstern auf. Kippnaehe bleibt variantenreicher und weltabhaengiger.
- Die passive Preview-Regulationskarte zeigt: Feldsymbole tragen keine eindimensionale Bedeutung. `dio_mcm_episode_02xikfk` wirkt in Rekopplung stabilisierend, in Kippnaehe dagegen tragend-unruhiger.
- Die Kippvarianten `dio_mcm_episode_037i64j`, `dio_mcm_episode_0e9ekzq`, `dio_mcm_episode_0eje6op` und `dio_mcm_episode_182yyt2` bilden bisher eine erkennbare Rand-/Spannungsgruppe, aber noch keine mehrweltstabile Familie. Sie reproduzieren sich in `PREVIEW_REAL_2023` ueber beide Laeufe.
- Die Folgewelt `PREVIEW_REAL2_2023` stuetzt erstmals ein Kippzeichen ueber eine zweite Realwelt: `dio_mcm_episode_182yyt2`. Damit ist Randspannung nicht mehr nur Einzelzeichen, aber weiterhin noch keine stabile MCM-Familie.
- Die weiteren Folgewelten `PREVIEW_REAL3_2023` und `PREVIEW_MODNEG_2023` bestaetigen `182yyt2` nicht als breit stabiles Einzelzeichen. Die Randspannungsgruppe bleibt aber erkennbar: `037i64j` tritt zusaetzlich in Real3 auf, waehrend die Kippvarianten insgesamt hoeheren Felddruck und geringere Rekopplung als die Rekopplungsfamilie tragen.
- Die passive Symbolgruppen-Rollenkarte trennt die aktuelle Preview-Syntax in `rekopplungsnaehe`, `randspannung` und `offene_variante`. `dio_mcm_episode_1eik02d` ist derzeit die offene Variante: haeufig genug fuer Beobachtung, aber noch nicht sauber als Rekopplung oder Randspannung zu benennen.
- Die neue Realwelt `PREVIEW_2024_REAL1` erweitert vor allem die `rekopplungsnaehe`: `dio_mcm_episode_02xikfk` und `dio_mcm_episode_1t5bcxp` treten dort erneut auf. Die Gruppenrelation bleibt erhalten; `dio_mcm_episode_0044zlp` erscheint nur schwach als offene Variante und wird nicht als neue Familie gelesen.
- Die Symbolgruppen-Stabilitaetsmatrix zeigt nach `PREVIEW_2024_REAL1`: `rekopplungsnaehe`, `randspannung` und `offene_variante` bleiben in ihren Rollenrelationen stabil. Die neue Welt wirkt bisher nicht als Ordnungsbruch.
- Die Pruefung der weltuebergreifenden Informationsaufnahme zeigt ein klares Wahrnehmungsproblem: feste Teiler und harte Skalierung koennen Sinnesachsen uebersteuern. Eine einfache weltrelative Skalierung war nicht ausreichend; erst eine weiche weltrelative Sinneskompression reduzierte die Auffaelligkeiten deutlich.
- `run_mini` besitzt jetzt den expliziten Forschungsmodus `--sense-mode world_relative`. Der Standard bleibt `fixed`, bis die Rollenmatrix ueber mehrere Welten im neuen Modus geprueft ist.
- Der Befund `266_WELTRELATIVER_MEHRWELT_LAUFBEFUND.md` zeigt: `world_relative` vereinheitlicht die Aufnahme ueber SOL/BTC, 5m/1h und Stresswelten stark. Das reduziert Rohdatenlast, kann aber echte Weltspannung zu stark beruhigen. Der Modus bleibt daher Forschungsmodus.
- Die Diagnose `267_WELTRELATIVER_BRUCHERHALT_DIAGNOSE.md` entlastet diesen Punkt teilweise: rohe Bruchfenster bleiben unter `world_relative` in allen geprueften Welten sensorisch sichtbar und zeigen lokal erhoehte Kippnaehe. Eine zweite Bruchspur ist aktuell noch nicht noetig.
- Die Laufpruefung `268_SOL_BTC_5M_1H_WELTRELATIVER_BRUCHERHALT.md` bestaetigt den Befund auf frischen Reset-Memory-Laeufen fuer SOL 5m, SOL 1h, BTC 5m und BTC 1h: `world_relative` bleibt passiv, vergleichbar und erhaelt Bruchfenster.
- Die Topologie-Matrix `269_WELTRELATIVE_TOPOLOGIE_MATRIX.md` liest Rollenqualitaet statt feste `dio_*`-Namen. In den geprueften SOL/BTC- und 5m/1h-Welten bleibt eine stabile Rollenordnung sichtbar: zentrumsnahe Stabilitaet, offene Variante und Rand-/Kippnaehe. Die Einteilung bleibt Diagnose, keine Regel und kein Beweis einer universellen Geometrie.

## Arbeitsregel

MINI_DIO bleibt auf Forschungsebene.

Passive Reports duerfen keine Handlung, kein Gate und kein Entry-Signal erzeugen.

Neue Diagnosewerkzeuge wie `report_sensory_adaptation.py` bleiben ebenfalls passiv.
Sie duerfen Reizwirkung, Habituation, Sensitivierung und allostatische Feldlast beschreiben, aber keine Handlung ableiten.

Die Diagnosen `218_FELDHISTORIE_GEGEN_WELTSTRUKTUR_DIAGNOSE.md` und `219_FELDHISTORIE_GEGEN_WELTSTRUKTUR_BEFUND.md` lesen Feldhistorie nur als passive Naeherung.
Sie duerfen nicht als Regel, Schwelle oder Handlungsausloeser verwendet werden.

Die Diagnosen `220_SOL5M_HARMONISCHE_REFERENZ_DIAGNOSE.md` und `221_SOL5M_HARMONISCHE_REFERENZ_BEFUND.md` lesen SOL 5m nur als bisher harmonisches Referenzprofil.
Sie duerfen nicht als mechanische Bevorzugung einer Zeitaufloesung verwendet werden.

Die Diagnosen `222_ORGANISCHER_ADAPTIONSWEG_DIAGNOSE.md` und `223_ORGANISCHER_ADAPTIONSWEG_BEFUND.md` lesen Anpassungsfaehigkeit nur als passive Feldwahrnehmung.
Sie duerfen nicht als Limiter, Gate oder Handlungsvorgabe verwendet werden.

Die Diagnosen `224_AUDITIVE_REGULATION_DIAGNOSE.md` und `225_AUDITIVE_REGULATION_BEFUND.md` lesen Hoeren nur als passive Sinnesregulation.
Sie duerfen nicht als Lautstaerke-Limiter, Entry-Signal oder Handlungsausloeser verwendet werden.

Die Diagnosen `226_AUDITIVE_FELDKOPPLUNG_DIAGNOSE.md` und `227_AUDITIVE_FELDKOPPLUNG_BEFUND.md` lesen Hoeren gegen MCM-Feldwirkung.
Sie duerfen nicht als Handelslogik oder Feldsteuerung verwendet werden.

Die Diagnosen `228_VISUELLE_REGULATION_DIAGNOSE.md` und `229_VISUELLE_REGULATION_BEFUND.md` lesen Sehen nur als passive Sinnesregulation.
Sie duerfen nicht als Form-Gate, Entry-Signal oder Handlungsausloeser verwendet werden.

Die Diagnosen `230_VISUELLE_FELDKOPPLUNG_DIAGNOSE.md` und `231_VISUELLE_FELDKOPPLUNG_BEFUND.md` lesen Sehen gegen MCM-Feldwirkung.
Sie duerfen nicht als Handelslogik oder Feldsteuerung verwendet werden.

Die Diagnosen `232_MULTISENSORISCHE_KOPPLUNG_DIAGNOSE.md` und `233_MULTISENSORISCHE_KOPPLUNG_BEFUND.md` lesen Hoeren, Sehen und Fuehlen gemeinsam.
Sie duerfen nicht als Handlungsreife, Gate, Entry-Signal oder Feldsteuerung verwendet werden.

Die Diagnosen `234_LOKALE_MULTISENSORISCHE_KOPPLUNG_DIAGNOSE.md` und `235_LOKALE_MULTISENSORISCHE_KOPPLUNG_BEFUND.md` lesen lokale Sinnesinnenlagen innerhalb einzelner Welten.
Sie duerfen nicht als lokale Handelszone, Signal oder Eingriffspunkt verwendet werden.

Die Diagnosen `236_LOKALE_MULTISENSORISCHE_SYNTAX_DIAGNOSE.md` und `237_LOKALE_MULTISENSORISCHE_SYNTAX_BEFUND.md` lesen lokale Kipp- und Rekopplungsfenster gegen MINI_DIOs eigene Syntax.
Sie duerfen nicht als Beweis fuer gereifte lokale Bedeutungsinseln verwendet werden, solange die Feld-Episodenspur nicht stabil mittraegt.

Der Befund `238_LOKALE_FELD_EPISODEN_VORSCHAU_BEFUND.md` dokumentiert die Trennung zwischen abgeschlossener Feld-Episode und lokaler Feld-Episoden-Vorschau.
`mcm_field_episode_preview_symbol` ist nur Diagnose und darf keine Handlung, kein Gate und keine Memory-Schreibung ausloesen.

Die Diagnosen `239_LOKALE_MULTISENSORISCHE_KOPPLUNG_PREVIEW_DIAGNOSE.md`, `240_LOKALE_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.md` und der Befund `241_LOKALE_FELD_EPISODEN_PREVIEW_SYNTAX_BEFUND.md` lesen lokale Kipp- und Rekopplungsfenster mit der neuen Feld-Episoden-Vorschau.
Sie zeigen entstehende lokale Feld-Episoden-Syntax, bleiben aber passiv und duerfen nicht als gereifte Bedeutung, Handlung, Gate oder Entry-Signal verwendet werden.

Die Diagnosen `242_MEHRWELT_LOKALE_MULTISENSORISCHE_KOPPLUNG_PREVIEW_DIAGNOSE.md`, `243_MEHRWELT_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.md` und der Befund `244_MEHRWELT_FELD_EPISODEN_PREVIEW_SYNTAX_BEFUND.md` vergleichen lokale Vorschau-Syntax ueber mehrere Welten.
Sie lesen gemeinsame Grundsprache und weltbezogene Varianten passiv; sie duerfen nicht als feste Topologie, Handlung oder universeller Beweis verwendet werden.

Die Diagnose `245_PASSIVE_PREVIEW_REGULATIONSKARTE.md` und `246_PREVIEW_SYMBOL_02XIKFK_ROLLENKONTRAST.md` lesen Regulation als passive Kopplung aus Feldsymbol, lokaler Rolle und Innenfeldwirkung.
Sie duerfen nicht als aktives Regulationsmodul oder Steuerlogik verwendet werden.

Die Diagnose `247_PREVIEW_KIPPVARIANTEN_GEGEN_REKOPPLUNGSFAMILIE.md` vergleicht Rand-/Spannungsvarianten gegen die Rekopplungsfamilie.
Sie darf nur als passiver Kontrast gelesen werden; die Kippvarianten sind noch nicht als stabile MCM-Familie zu benennen.

Die Diagnosen `248_FOLGEWELT_LOKALE_MULTISENSORISCHE_KOPPLUNG_PREVIEW_DIAGNOSE.md`, `249_FOLGEWELT_FELD_EPISODEN_PREVIEW_SYNTAX_DIAGNOSE.md`, `250_FOLGEWELT_KIPPVARIANTEN_GEGEN_REKOPPLUNGSFAMILIE.md` und der Befund `251_FOLGEWELT_RANDSPANNUNG_BEFUND.md` pruefen Randspannung mit einer weiteren Realwelt.
Sie zeigen eine erste Folgewelt-Stuetze fuer `dio_mcm_episode_182yyt2`, bleiben aber passiv.

Die Diagnosen `252_182Y_FOLGEWELTEN_LOKALE_KOPPLUNG_PREVIEW_DIAGNOSE.md`, `253_182Y_FOLGEWELTEN_PREVIEW_SYNTAX_DIAGNOSE.md`, `254_182Y_FOLGEWELTEN_KIPPVARIANTEN_KONTRAST.md` und der Befund `255_182Y_FOLGEWELTEN_RANDSPANNUNG_GRUPPENBEFUND.md` erweitern diese Pruefung um weitere Folgewelten.
Sie lesen Randspannung aktuell als Variantenfamilie, nicht als breit stabiles Einzelzeichen.

Die Diagnose `256_PASSIVE_SYMBOLGRUPPEN_ROLLENKARTE.md` fasst Preview-Zeichen zu passiven Rollenfamilien zusammen.
Sie dient dazu, neue Zeichen zuerst hierarchisch einzuordnen, statt jede Einzelvariante als eigene Forschungsrichtung zu behandeln.

Die Diagnosen `257_SYMBOLGRUPPEN_NEUE_WELT_LOKALE_KOPPLUNG_PREVIEW_DIAGNOSE.md`, `258_SYMBOLGRUPPEN_NEUE_WELT_PREVIEW_SYNTAX_DIAGNOSE.md`, `259_SYMBOLGRUPPEN_NEUE_WELT_ROLLENKARTE.md` und der Befund `260_SYMBOLGRUPPEN_NEUE_WELT_BEFUND.md` pruefen die Rollenkarte gegen `PREVIEW_2024_REAL1`.
Sie zeigen, dass die Gruppenrelation unter der neuen Realwelt erhalten bleibt.

Die Diagnose `261_SYMBOLGRUPPEN_STABILITAETSMATRIX.md` vergleicht Rollenkarte vor und nach `PREVIEW_2024_REAL1`.
Sie zeigt alle drei Gruppen als stabil und dient als Grundlage fuer weitere Weltspannungspruefungen.

Die Diagnosen `262_WELTUEBERGREIFENDE_INFORMATIONSAUFNAHME_DIAGNOSE.md`, `263_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.md`, `264_WEICHER_WELTRELATIVER_WAHRNEHMUNGSADAPTER_VERGLEICH.md`, `267_WELTRELATIVER_BRUCHERHALT_DIAGNOSE.md`, `268_SOL_BTC_5M_1H_WELTRELATIVER_BRUCHERHALT.md` sowie die Befunde `265_WAHRNEHMUNGSADAPTER_LAUFVERGLEICH.md` und `266_WELTRELATIVER_MEHRWELT_LAUFBEFUND.md` pruefen die Sinnesaufnahme selbst.
Sie zeigen: Berechnung und Umsetzung der Wahrnehmung beeinflussen die MCM-Feldwirkung stark. Die weiche weltrelative Aufnahme ist viel einheitlicher und erhaelt in den geprueften Welten bisher Brueche, Rhythmuswechsel und Kippnaehe.

Die Diagnose `269_WELTRELATIVE_TOPOLOGIE_MATRIX.md` prueft danach die Rollen-Topologie im weltrelativen Modus.
Sie darf nur als passive Rollenmatrix gelesen werden: Zentrum, offene Variante, Rand/Kippnaehe und Rekopplungsnaehe sind Diagnosebegriffe, keine Zielstruktur und keine Ausfuehrungslogik.
