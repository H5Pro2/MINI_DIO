# Weltrelative Topologie-Matrix

Stand: 2026-06-22 17:15:07

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
| HARMONIE_ZEIT_KOMPAKT | 2694 | stark_zentriert_wenig_rand | 0.9978 | 0.0019 | 0.0004 | 0.2502 | 0.7535 | 0.6098 | 0.1201 | 0.9152 |
| HARMONIE_ZEIT_GEDEHNT | 10794 | stark_zentriert_wenig_rand | 0.9995 | 0.0004 | 0.0001 | 0.2502 | 0.7581 | 0.6198 | 0.1193 | 0.9173 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| HARMONIE_ZEIT_KOMPAKT | zentrum_stabil | 0.9978 | 0.7538 | 0.6103 | 0.1198 | 0.9155 | 0.2507 | 0.2485 | dio_mcm_episode_1v8o9kh | dio_1fll |
| HARMONIE_ZEIT_KOMPAKT | offene_variante | 0.0019 | 0.6195 | 0.3880 | 0.2319 | 0.7797 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_1r19 |
| HARMONIE_ZEIT_KOMPAKT | spannungsrand_kippnaehe | 0.0004 | 0.5742 | 0.3420 | 0.2961 | 0.6858 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_13i5 |
| HARMONIE_ZEIT_GEDEHNT | zentrum_stabil | 0.9995 | 0.7582 | 0.6199 | 0.1192 | 0.9173 | 0.2503 | 0.2499 | dio_mcm_episode_0qvodoj | dio_1fll |
| HARMONIE_ZEIT_GEDEHNT | offene_variante | 0.0004 | 0.6126 | 0.3803 | 0.2424 | 0.7697 | 0.0000 | 1.0000 | dio_mcm_episode_0qvodoj | dio_13h3 |
| HARMONIE_ZEIT_GEDEHNT | spannungsrand_kippnaehe | 0.0001 | 0.5750 | 0.3437 | 0.2955 | 0.6876 | 0.0000 | 1.0000 | dio_mcm_episode_1v8o9kh | dio_13i5 |

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
