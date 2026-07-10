# 2077 - Rollenfamilien unter Komponenten-Phasenprofilen

## Zweck

Befund 2076 fand bei `rf_05` keine allgemeine notwendige OHLCV-Kopplung, aber ein asymmetrisches Phasenprofil. Dieser Lauf prüft dieselben Welten mit allen acht Rollenfamilien, um familienspezifische Reaktion von einer allgemeinen Eigenschaft des Feldlesers zu trennen.

## Vorab Festgelegtes Design

- dieselben zwölf Realfenster und `144` Phasenkontrollen aus 2076
- keine neue Kontrollwelt und kein zusätzliches Weltarchiv
- wiederverwendetes Archiv: `data/2076_rf05_component_phase_controls.zip`
- acht unveränderte Rollenfamilien mit zusammen 29 Mitgliedern
- Komponenten: Körpervorzeichen, absolute Körpergröße, Dochtpaar und Volumen
- feste zirkuläre Offsets: `17`, `83` und `251` Beobachtungen
- Primärachsen: Kontinuität, Ereignisanteil und Mitgliederabdeckung
- direkte Paarprüfung je Familie, Fenster, Komponente und Offset
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

Eine Komponente gilt im gebündelten Profil nur dann als verstärkt oder abgeschwächt, wenn alle drei Primärachsen gleichgerichtet über beziehungsweise unter Real liegen. Gemischte Achsen bleiben ausdrücklich offen.

## Gebündelte Komponentenprofile

Differenzen sind Kontrolle minus Real. Jede Zeile bündelt `36` Kontrollwelten und `36` direkte Paare.

| Familie | Komponente | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Profil | gemeinsam Real höher |
|---|---|---:|---:|---:|---|---:|
| `rf_05` | `sign` | -0.027 | -0.0016 | -0.024 | `abgeschwaecht` | 8/36 |
| `rf_05` | `magnitude` | 0.043 | 0.0004 | 0.042 | `verstaerkt` | 6/36 |
| `rf_05` | `wick` | 0.029 | 0.0043 | 0.021 | `verstaerkt` | 3/36 |
| `rf_05` | `volume` | 0.033 | 0.0048 | 0.045 | `verstaerkt` | 1/36 |
| `rf_06` | `sign` | -0.038 | -0.0006 | -0.059 | `abgeschwaecht` | 18/36 |
| `rf_06` | `magnitude` | -0.006 | 0.0001 | -0.028 | `gemischt` | 12/36 |
| `rf_06` | `wick` | -0.041 | 0.0000 | -0.042 | `gemischt` | 11/36 |
| `rf_06` | `volume` | -0.106 | -0.0011 | -0.125 | `abgeschwaecht` | 23/36 |
| `rf_07` | `sign` | -0.006 | -0.0008 | 0.000 | `gemischt` | 0/36 |
| `rf_07` | `magnitude` | 0.007 | -0.0025 | 0.000 | `gemischt` | 0/36 |
| `rf_07` | `wick` | -0.004 | 0.0005 | 0.000 | `gemischt` | 0/36 |
| `rf_07` | `volume` | -0.009 | 0.0040 | 0.000 | `gemischt` | 0/36 |
| `rf_08` | `sign` | 0.099 | 0.0005 | 0.111 | `verstaerkt` | 5/36 |
| `rf_08` | `magnitude` | 0.142 | 0.0020 | 0.153 | `verstaerkt` | 1/36 |
| `rf_08` | `wick` | 0.064 | 0.0005 | 0.056 | `verstaerkt` | 6/36 |
| `rf_08` | `volume` | 0.070 | 0.0007 | 0.069 | `verstaerkt` | 7/36 |
| `rf_10` | `sign` | -0.083 | -0.0004 | -0.083 | `abgeschwaecht` | 12/36 |
| `rf_10` | `magnitude` | -0.121 | -0.0004 | -0.125 | `abgeschwaecht` | 12/36 |
| `rf_10` | `wick` | -0.137 | -0.0006 | -0.139 | `abgeschwaecht` | 15/36 |
| `rf_10` | `volume` | -0.198 | -0.0006 | -0.194 | `abgeschwaecht` | 17/36 |
| `rf_13` | `sign` | 0.014 | -0.0002 | 0.009 | `gemischt` | 8/36 |
| `rf_13` | `magnitude` | -0.069 | -0.0011 | -0.102 | `abgeschwaecht` | 15/36 |
| `rf_13` | `wick` | -0.003 | -0.0002 | 0.019 | `gemischt` | 8/36 |
| `rf_13` | `volume` | -0.033 | -0.0004 | -0.083 | `abgeschwaecht` | 13/36 |
| `rf_17` | `sign` | -0.221 | -0.0008 | -0.236 | `abgeschwaecht` | 20/36 |
| `rf_17` | `magnitude` | -0.075 | -0.0004 | -0.069 | `abgeschwaecht` | 14/36 |
| `rf_17` | `wick` | -0.024 | -0.0002 | -0.028 | `abgeschwaecht` | 9/36 |
| `rf_17` | `volume` | -0.267 | -0.0009 | -0.292 | `abgeschwaecht` | 18/36 |
| `rf_21` | `sign` | -0.103 | -0.0018 | -0.125 | `abgeschwaecht` | 7/36 |
| `rf_21` | `magnitude` | 0.000 | -0.0008 | 0.000 | `gemischt` | 2/36 |
| `rf_21` | `wick` | -0.039 | -0.0014 | -0.042 | `abgeschwaecht` | 3/36 |
| `rf_21` | `volume` | -0.076 | -0.0010 | -0.069 | `abgeschwaecht` | 6/36 |

## Familienprofile

| Familie | sign | magnitude | wick | volume | Einzelbedingungen verstärkt/abgeschwächt |
|---|---|---|---|---|---:|
| `rf_05` | `abgeschwaecht` | `verstaerkt` | `verstaerkt` | `verstaerkt` | 7/2 |
| `rf_06` | `abgeschwaecht` | `gemischt` | `gemischt` | `abgeschwaecht` | 1/9 |
| `rf_07` | `gemischt` | `gemischt` | `gemischt` | `gemischt` | 0/0 |
| `rf_08` | `verstaerkt` | `verstaerkt` | `verstaerkt` | `verstaerkt` | 11/0 |
| `rf_10` | `abgeschwaecht` | `abgeschwaecht` | `abgeschwaecht` | `abgeschwaecht` | 0/12 |
| `rf_13` | `gemischt` | `abgeschwaecht` | `gemischt` | `abgeschwaecht` | 2/6 |
| `rf_17` | `abgeschwaecht` | `abgeschwaecht` | `abgeschwaecht` | `abgeschwaecht` | 1/9 |
| `rf_21` | `abgeschwaecht` | `gemischt` | `abgeschwaecht` | `abgeschwaecht` | 0/7 |

## Befund

Das gebündelte Profil von `rf_05` lautet `abgeschwaecht;verstaerkt;verstaerkt;verstaerkt`. Dasselbe vollständige Vier-Komponenten-Profil tragen weitere Familien: `-`.

Dieselbe Kombination aus Vorzeichen- und Volumenreaktion wie `rf_05` tragen: `-`.

Damit ist die 2076-Asymmetrie innerhalb dieses Kontrollraums nicht als allgemeine Eigenschaft des Feldlesers reproduziert. `rf_05` zeigt eine selektive Antwortform mit `7` verstärkten und `2` abgeschwächten Einzelbedingungen. Der schwächere Vorzeichenpol bleibt jedoch schmal: Real liegt dort nur in `8/36` Paaren gleichzeitig bei Ereignisanteil und Abdeckung vorn.

Die übrigen Familien bilden deutlich andere Antwortformen. `rf_08` wird gebündelt bei allen vier Komponenten verstärkt und in `11/12` Einzelbedingungen gleichgerichtet verstärkt. `rf_10` wird bei allen vier Komponenten und in `12/12` Einzelbedingungen abgeschwächt. `rf_17` teilt das gebündelte Abschwächungsprofil, trägt es aber nur in `9/12` Einzelbedingungen; `rf_07` bleibt mit `gemischt;gemischt;gemischt;gemischt` vollständig achsengemischt.

Der tragfähige Befund ist daher keine Komponentenbedeutung, sondern eine familienabhängige Phasen-Antworttopologie: Rollenfamilien reagieren verschieden darauf, dass Eigenzeit erhalten und relative Kopplung gelöst wird. Diese Antwortformen sind passive Forschungsevidenz. Sie werden weder als Bedeutungsetikett noch als neue Runtime-Regel gespeichert.

Eine organische Erweiterung ist noch nicht begründet. Dafür müsste dieselbe Familienindividualität in unabhängigen Welten wiederkehren und gegenüber gemeinsamer Messgeometrie bestehen.

## Grenze

Alle Familien werden auf denselben Marktfenstern und denselben rekonstruierten Phasenkontrollen gelesen. Gemeinsame Profile können daher sowohl aus geteilter Feldorganisation als auch aus gemeinsamer Messgeometrie entstehen. Der Lauf prüft Spezifität innerhalb dieses Kontrollraums, nicht Kausalität, feste Semantik oder Übertragbarkeit auf andere Sinnesmodalitäten.
