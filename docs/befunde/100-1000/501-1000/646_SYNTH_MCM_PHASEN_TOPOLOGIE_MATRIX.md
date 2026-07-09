# Weltrelative Topologie-Matrix

Stand: 2026-06-22 10:10:12

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
| SYNTH_A | 5394 | stark_zentriert_wenig_rand | 0.9991 | 0.0007 | 0.0002 | 0.2501 | 0.7568 | 0.6170 | 0.1196 | 0.9168 |
| SYNTH_B | 5394 | stark_zentriert_wenig_rand | 0.9991 | 0.0007 | 0.0002 | 0.2501 | 0.7568 | 0.6170 | 0.1196 | 0.9168 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| SYNTH_A | zentrum_stabil | 0.9991 | 0.7569 | 0.6172 | 0.1194 | 0.9169 | 0.2503 | 0.2496 | dio_mcm_episode_0qvodoj | dio_1fll |
| SYNTH_A | offene_variante | 0.0007 | 0.6120 | 0.3771 | 0.2529 | 0.7908 | 0.0000 | 1.0000 | dio_mcm_episode_0qvodoj | dio_0ef6 |
| SYNTH_A | spannungsrand_kippnaehe | 0.0002 | 0.5737 | 0.3328 | 0.3095 | 0.7112 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_15wa |
| SYNTH_B | zentrum_stabil | 0.9991 | 0.7569 | 0.6172 | 0.1194 | 0.9169 | 0.2503 | 0.2496 | dio_mcm_episode_0qvodoj | dio_1fll |
| SYNTH_B | offene_variante | 0.0007 | 0.6120 | 0.3771 | 0.2529 | 0.7908 | 0.0000 | 1.0000 | dio_mcm_episode_0qvodoj | dio_0ef6 |
| SYNTH_B | spannungsrand_kippnaehe | 0.0002 | 0.5737 | 0.3328 | 0.3095 | 0.7112 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_15wa |

## Lesart

Zentrumsnahe Welten: 2
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
