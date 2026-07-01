# Weltrelative Topologie-Matrix

Stand: 2026-07-01 05:20:59

## Zweck

Diese Diagnose prueft, ob MINI_DIO unter `world_relative` weiterhin eine passive Topologie ausbildet.
Die Topologie wird nicht ueber feste `dio_*`-Namen gelesen.
Gelesen werden Rollenqualitaeten aus Innenfeldwirkung, Rekopplung, Carry, Strain und Sinnes-MCM-Kopplung.

Die Diagnose erzeugt keine Handlung, kein Gate und kein Entry-Signal.

## Hierarchie

1. Grundfrage: Bleibt eine Rollen-Topologie sichtbar, wenn die Sinnesaufnahme weltrelativ wird?
2. Unterpruefung: Welche Rollenanteile tragen Zentrum, Rand/Kippnaehe, offene Variante und Rekopplungsnaehe?
3. Folgeschritt: Vergleich gegen ruhigere, laengere und staerker gespannte Welten.

## Kurzbefund

| Welt | Episoden | Topologiezustand | Zentrum | Offen | Rand/Kipp | Rekopplungsnaehe | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|
| SYNTH_DESYNC_AXES | 8494 | stark_zentriert_wenig_rand | 0.9803 | 0.0105 | 0.0092 | 0.2352 | 0.7527 | 0.6061 | 0.1260 | 0.9108 |
| SYNTH_RAND_KIPP_GEGENPROBE | 8994 | stark_zentriert_wenig_rand | 0.9033 | 0.0961 | 0.0007 | 0.2357 | 0.7377 | 0.5860 | 0.1326 | 0.8885 |
| SYNTH_RAND_DOMINANZ_ALT | 6994 | stark_zentriert_wenig_rand | 0.9312 | 0.0681 | 0.0007 | 0.2501 | 0.7410 | 0.5906 | 0.1296 | 0.8971 |
| SYNTH_HARMONIE_ALT | 5394 | stark_zentriert_wenig_rand | 0.9993 | 0.0006 | 0.0002 | 0.2501 | 0.7570 | 0.6173 | 0.1191 | 0.9169 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_DESYNC_AXES | zentrum_stabil | 0.9803 | 0.7553 | 0.6093 | 0.1231 | 0.9152 | 0.2551 | 0.2350 | dio_mcm_episode_0v5p8er | dio_1fll |
| SYNTH_DESYNC_AXES | offene_variante | 0.0105 | 0.6470 | 0.4707 | 0.2458 | 0.7332 | 0.0000 | 1.0000 | dio_mcm_episode_0v5p8er | dio_03yj |
| SYNTH_DESYNC_AXES | spannungsrand_kippnaehe | 0.0092 | 0.6006 | 0.4204 | 0.3016 | 0.6475 | 0.0000 | 1.0000 | dio_mcm_episode_0v5p8er | dio_0kcg |
| SYNTH_RAND_KIPP_GEGENPROBE | zentrum_stabil | 0.9033 | 0.7444 | 0.5944 | 0.1266 | 0.9007 | 0.2768 | 0.1699 | dio_mcm_episode_0qvodoj | dio_1fll |
| SYNTH_RAND_KIPP_GEGENPROBE | offene_variante | 0.0961 | 0.6762 | 0.5085 | 0.1882 | 0.7751 | 0.0000 | 1.0000 | dio_mcm_episode_01s42m6 | dio_1v2w |
| SYNTH_RAND_KIPP_GEGENPROBE | spannungsrand_kippnaehe | 0.0007 | 0.5763 | 0.3309 | 0.3064 | 0.6823 | 0.0000 | 1.0000 | dio_mcm_episode_1engxbn | dio_03rd |
| SYNTH_RAND_DOMINANZ_ALT | zentrum_stabil | 0.9312 | 0.7468 | 0.5987 | 0.1247 | 0.9066 | 0.2685 | 0.1947 | dio_mcm_episode_08lp0ua | dio_1fll |
| SYNTH_RAND_DOMINANZ_ALT | offene_variante | 0.0681 | 0.6632 | 0.4828 | 0.1946 | 0.7693 | 0.0000 | 1.0000 | dio_mcm_episode_14l8khu | dio_1v2w |
| SYNTH_RAND_DOMINANZ_ALT | spannungsrand_kippnaehe | 0.0007 | 0.5885 | 0.3400 | 0.2996 | 0.6825 | 0.0000 | 1.0000 | dio_mcm_episode_0r9ht2p | dio_11v0 |
| SYNTH_HARMONIE_ALT | zentrum_stabil | 0.9993 | 0.7571 | 0.6175 | 0.1190 | 0.9170 | 0.2503 | 0.2495 | dio_mcm_episode_0qvodoj | dio_1fll |
| SYNTH_HARMONIE_ALT | offene_variante | 0.0006 | 0.6112 | 0.3802 | 0.2449 | 0.7668 | 0.0000 | 1.0000 | dio_mcm_episode_0qvodoj | dio_0trm |
| SYNTH_HARMONIE_ALT | spannungsrand_kippnaehe | 0.0002 | 0.5792 | 0.3456 | 0.2866 | 0.6948 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_13i5 |

## Lesart

Zentrumsnahe Welten: 4
Gemischte Rollenordnung: 0
Randlastige Welten: 0

Die aktuelle Matrix spricht fuer eine Rollen-Topologie, nicht fuer eine starre geometrische Form.

```text
Zentrum      = stabile Innenfeldwirkung
Rand/Kipp    = lokale Spannung und Bruchnaehe
Offen        = tragende, aber noch nicht fest gereifte Variante
Rekopplung   = Qualitaet, die Zentrum und Uebergang stabilisiert
```

Wichtig: Die numerischen Einteilungen sind Diagnosehilfen.
Sie sind keine Regeln fuer MINI_DIO und keine universellen MCM-Grenzen.

## Wie es weitergeht

Als naechstes sollte dieselbe Matrix auf lange ruhige Welten, Stresswelten und Expansionswelten gelegt werden.
Ziel ist zu pruefen, ob `zentrum_mit_rand_und_uebergang` stabil bleibt, ob Randspannung bei Stress sichtbar zunimmt oder ob neue Mischklassen entstehen.
