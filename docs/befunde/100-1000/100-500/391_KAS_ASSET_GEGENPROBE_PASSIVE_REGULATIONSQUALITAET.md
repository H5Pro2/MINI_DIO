# Passive Regulationsqualitaet Reproduktion

Stand: 2026-06-20 08:38:22

## Zweck

Diese Diagnose prueft, ob die in 343 formulierten passiven Regulationsqualitaeten in den vorhandenen Milieu- und Driftbefunden wieder auftauchen.
Sie bleibt passiv: keine Handlung, kein Gate, keine Strategie und keine harte Runtime-Regel.

## Hierarchie

1. Grundfrage: Bleiben passive Regulationsqualitaeten ueber Weltgruppen lesbar?
2. Unterpruefung: Milieuqualitaeten aus 341 und Weltkopplung aus 342 in vier Innenfeldqualitaeten uebersetzen.
3. Folgeschritt: pruefen, ob neue Welten dieselben Qualitaeten erweitern, verschieben oder fragmentieren.

## Reproduktionsmatrix

| Paar | Welten | Passive Qualitaeten | Top-Qualitaet | Anteil | Events | Profil |
|---|---:|---:|---|---:|---:|---|
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 2 | 2 | fragmentiert | 0.8889 | 9 | fragmentiert:8; breit_driftend:1 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 2 | 2 | eng_getragen | 0.7143 | 7 | eng_getragen:5; breit_driftend:2 |

## Gesamtlesung

| Paar | Events | Driftqualitaet | Top-Milieu | Anteil | Passive Regulationsqualitaet |
|---|---:|---|---|---:|---|
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | 9 | breit_driftend | druckuebergang | 0.3333 | fragmentiert |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | 7 | eng_getragen | rekoppelnd_stabil | 0.7143 | eng_getragen |

## Weltlesung

| Paar | Welt | Events | Milieu | Anteil | Passive Qualitaet | Druck | Alignment | Rekopplung |
|---|---|---:|---|---:|---|---:|---:|---:|
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | KAS2024_15M_ASSET_PROBE | 1 | druckbruch | 0.5000 | fragmentiert | 0.2127 | 0.8666 | 0.6443 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | KAS2024_15M_ASSET_PROBE | 1 | druckuebergang | 0.5000 | fragmentiert | 0.2127 | 0.8666 | 0.6443 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | KAS2024_1H_ASSET_PROBE | 2 | druckuebergang | 0.2857 | fragmentiert | 0.2137 | 0.8648 | 0.6434 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | KAS2024_1H_ASSET_PROBE | 2 | bruchuebergang | 0.2857 | fragmentiert | 0.2137 | 0.8648 | 0.6434 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | KAS2024_1H_ASSET_PROBE | 1 | rekoppelnd_offen | 0.1429 | breit_driftend | 0.2137 | 0.8648 | 0.6434 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | KAS2024_1H_ASSET_PROBE | 1 | bruchdominant | 0.1429 | fragmentiert | 0.2137 | 0.8648 | 0.6434 |
| dio_mcm_episode_183drjy->dio_mcm_episode_1t5bcxp | KAS2024_1H_ASSET_PROBE | 1 | druckbruch | 0.1429 | fragmentiert | 0.2137 | 0.8648 | 0.6434 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | KAS2024_15M_ASSET_PROBE | 1 | rekoppelnd_stabil | 1.0000 | eng_getragen | 0.2127 | 0.8666 | 0.6443 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | KAS2024_1H_ASSET_PROBE | 4 | rekoppelnd_stabil | 0.6667 | eng_getragen | 0.2137 | 0.8648 | 0.6434 |
| dio_mcm_episode_1t5bcxp->dio_mcm_episode_183drjy | KAS2024_1H_ASSET_PROBE | 2 | rekoppelnd_offen | 0.3333 | breit_driftend | 0.2137 | 0.8648 | 0.6434 |

## Befund

Die KAS-Gegenprobe bestaetigt die Richtung, aber nur mit begrenzter Ereignisbasis.
Die vorhandenen KAS-Daten sind 2000er Kontrollwelten, keine 4000er Stress/Ruhe-Jahresfenster wie bei SOL/BTC.
Zudem liefern in dieser Zielbewegung nur 1h und 15m belastbare Events; 5m bleibt fuer diese konkrete Paarpruefung praktisch leer.

Innerhalb dieser Grenze bleibt die Asymmetrie sichtbar:

```text
1t5bcxp -> 183drjy: dominant eng_getragen, 7 Events, Top-Anteil 0.7143
183drjy -> 1t5bcxp: dominant fragmentiert, 9 Events, Top-Anteil 0.8889
```

KAS liest den Rueckweg sogar sehr deutlich fragmentiert, aber die geringe Eventzahl verhindert eine harte Aussage.
Der Befund ist deshalb eine Asset-Gegenprobe, keine vollstaendige Asset-Reproduktion.

Fachliche Lesart:

```text
Auch KAS zeigt: Die Feldbewegung hat eine gerichtete Tragart.
Die Richtung passt zur SOL/BTC-Matrix, aber die Datentiefe ist noch zu klein.
Sie bleibt passive Innenfeldwahrnehmung und darf nicht direkt in Handlung uebersetzt werden.
```

## Wie es weitergeht

Als naechstes braucht KAS laengere oder gezielter extrahierte Welten.
Ziel ist zu pruefen, ob die geringe Eventzahl eine Eigenschaft der KAS-Welt oder nur Folge der kurzen 2000er Kontrollfenster ist.
