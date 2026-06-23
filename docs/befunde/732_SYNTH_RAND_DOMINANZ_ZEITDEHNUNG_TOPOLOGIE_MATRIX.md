# Weltrelative Topologie-Matrix

Stand: 2026-06-22 17:17:57

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
| RAND_ZEIT_KOMPAKT | 3294 | stark_zentriert_wenig_rand | 0.9174 | 0.0808 | 0.0018 | 0.2505 | 0.7338 | 0.5758 | 0.1320 | 0.8924 |
| RAND_ZEIT_GEDEHNT | 13194 | stark_zentriert_wenig_rand | 0.9276 | 0.0719 | 0.0005 | 0.2322 | 0.7436 | 0.5957 | 0.1296 | 0.8964 |

## Rollenmatrix

| Welt | Rolle | Anteil | Rekopplung | Carry | Strain | Sinneskopplung | Rekopplung Top | Strain Top | Vorschau-Symbol | Symbolfamilie |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| RAND_ZEIT_KOMPAKT | zentrum_stabil | 0.9174 | 0.7408 | 0.5858 | 0.1261 | 0.9032 | 0.2730 | 0.1827 | dio_mcm_episode_1hs3jsa | dio_1fll |
| RAND_ZEIT_KOMPAKT | offene_variante | 0.0808 | 0.6578 | 0.4678 | 0.1953 | 0.7743 | 0.0000 | 1.0000 | dio_mcm_episode_1hdpu9s | dio_1v2w |
| RAND_ZEIT_KOMPAKT | spannungsrand_kippnaehe | 0.0018 | 0.5776 | 0.3359 | 0.3030 | 0.6840 | 0.0000 | 1.0000 | dio_mcm_episode_19dxnmz | dio_03rd |
| RAND_ZEIT_GEDEHNT | zentrum_stabil | 0.9276 | 0.7494 | 0.6034 | 0.1245 | 0.9066 | 0.2697 | 0.1915 | dio_mcm_episode_0qvodoj | dio_1fll |
| RAND_ZEIT_GEDEHNT | offene_variante | 0.0719 | 0.6690 | 0.4974 | 0.1939 | 0.7672 | 0.0000 | 1.0000 | dio_mcm_episode_01s42m6 | dio_1v2w |
| RAND_ZEIT_GEDEHNT | spannungsrand_kippnaehe | 0.0005 | 0.5811 | 0.3329 | 0.3074 | 0.6762 | 0.0000 | 1.0000 | dio_mcm_episode_1engxbn | dio_0owd |

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
