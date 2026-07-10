# 2078 - Rollenfamilien-Phasenprofile im unabhängigen 2025-Holdout

## Zweck

Befund 2077 zeigte in 2024-Welten unterscheidbare Phasen-Antwortprofile der Rollenfamilien. Dieser Lauf prüft vorab festgelegte Profile in getrennten 2025-Fenstern und erweitert die 1h-Ebene um einen bisher ungenutzten 15m-Holdout.

## Vorab Festgelegtes Design

- ausschließlich Datenjahr `2025`
- Assets: `BTC` und `SOL`
- Zeitebenen: `1h` und `15m`
- drei nicht überlappende Fenster je Asset und Zeitebene
- 1h-Startpunkte `0`, `2000`, `4000`; keine Überschneidung mit den früheren Rollenfamilienfenstern `5000`, `6000`, `7000`
- 15m-Startpunkte `0`, `12000`, `24000`; diese Zeitebene war in der Rollenfamilienkette noch ungenutzt
- zwölf Realwelten und `144` Phasenkontrollen
- feste Offsets `17`, `83`, `251` und unveränderte 29 Familienmitglieder
- Weltarchiv: `data/2078_role_family_phase_profile_holdout.zip`
- keine neue Klasse, keine Handlung, kein Gate und keine Richtung

Vor dem Lauf festgelegte Signaturen:

| Familie | sign | magnitude | wick | volume |
|---|---|---|---|---|
| `rf_05` | abgeschwächt | verstärkt | verstärkt | verstärkt |
| `rf_08` | verstärkt | verstärkt | verstärkt | verstärkt |
| `rf_10` | abgeschwächt | abgeschwächt | abgeschwächt | abgeschwächt |
| `rf_07` | gemischt | gemischt | gemischt | gemischt |

Die Übereinstimmung wird komponentenweise ausgegeben. Es gibt kein nachträglich gesetztes binäres Bestätigungsgate. Die übrigen vier Familien werden explorativ gegen ihre 2077-Profile verglichen.

## Holdout-Komponentenprofile

Differenzen sind Kontrolle minus Real. Jede Zeile bündelt `36` Kontrollwelten.

| Familie | Komponente | Δ Kontinuität | Δ Ereignisanteil | Δ Abdeckung | Profil | gemeinsam Real höher |
|---|---|---:|---:|---:|---|---:|
| `rf_05` | `sign` | -0.038 | -0.0034 | -0.049 | `abgeschwaecht` | 16/36 |
| `rf_05` | `magnitude` | -0.009 | -0.0019 | 0.003 | `gemischt` | 7/36 |
| `rf_05` | `wick` | -0.028 | 0.0008 | -0.010 | `gemischt` | 9/36 |
| `rf_05` | `volume` | 0.006 | 0.0041 | 0.010 | `verstaerkt` | 4/36 |
| `rf_06` | `sign` | -0.005 | -0.0007 | -0.017 | `abgeschwaecht` | 11/36 |
| `rf_06` | `magnitude` | 0.012 | 0.0001 | 0.010 | `verstaerkt` | 9/36 |
| `rf_06` | `wick` | -0.018 | -0.0004 | -0.007 | `abgeschwaecht` | 12/36 |
| `rf_06` | `volume` | -0.057 | -0.0012 | -0.062 | `abgeschwaecht` | 19/36 |
| `rf_07` | `sign` | -0.006 | -0.0028 | 0.000 | `gemischt` | 0/36 |
| `rf_07` | `magnitude` | -0.001 | -0.0018 | 0.000 | `gemischt` | 0/36 |
| `rf_07` | `wick` | -0.007 | -0.0003 | 0.000 | `gemischt` | 0/36 |
| `rf_07` | `volume` | -0.006 | 0.0025 | 0.000 | `gemischt` | 0/36 |
| `rf_08` | `sign` | 0.072 | 0.0004 | 0.083 | `verstaerkt` | 4/36 |
| `rf_08` | `magnitude` | 0.103 | 0.0015 | 0.125 | `verstaerkt` | 3/36 |
| `rf_08` | `wick` | 0.024 | 0.0000 | 0.028 | `verstaerkt` | 6/36 |
| `rf_08` | `volume` | 0.069 | 0.0001 | 0.097 | `verstaerkt` | 4/36 |
| `rf_10` | `sign` | -0.075 | -0.0003 | -0.097 | `abgeschwaecht` | 10/36 |
| `rf_10` | `magnitude` | -0.065 | -0.0004 | -0.111 | `abgeschwaecht` | 11/36 |
| `rf_10` | `wick` | -0.018 | -0.0002 | -0.028 | `abgeschwaecht` | 9/36 |
| `rf_10` | `volume` | -0.006 | 0.0001 | -0.014 | `gemischt` | 11/36 |
| `rf_13` | `sign` | 0.008 | 0.0006 | 0.028 | `verstaerkt` | 7/36 |
| `rf_13` | `magnitude` | -0.124 | -0.0002 | -0.139 | `abgeschwaecht` | 14/36 |
| `rf_13` | `wick` | -0.072 | -0.0001 | -0.083 | `abgeschwaecht` | 9/36 |
| `rf_13` | `volume` | -0.004 | 0.0005 | -0.009 | `gemischt` | 6/36 |
| `rf_17` | `sign` | -0.282 | -0.0011 | -0.333 | `abgeschwaecht` | 17/36 |
| `rf_17` | `magnitude` | -0.135 | -0.0006 | -0.167 | `abgeschwaecht` | 15/36 |
| `rf_17` | `wick` | -0.103 | -0.0004 | -0.111 | `abgeschwaecht` | 12/36 |
| `rf_17` | `volume` | -0.229 | -0.0011 | -0.264 | `abgeschwaecht` | 18/36 |
| `rf_21` | `sign` | -0.010 | -0.0003 | 0.014 | `gemischt` | 2/36 |
| `rf_21` | `magnitude` | 0.025 | -0.0003 | 0.042 | `gemischt` | 2/36 |
| `rf_21` | `wick` | -0.013 | 0.0004 | 0.014 | `gemischt` | 2/36 |
| `rf_21` | `volume` | -0.059 | 0.0005 | -0.042 | `gemischt` | 3/36 |

## Profil-Replikation

| Familie | vorab festgelegt | 2077-Profil | 2025-Holdout | Treffer | vollständig |
|---|---|---|---|---:|---:|
| `rf_05` | ja | `abgeschwaecht;verstaerkt;verstaerkt;verstaerkt` | `abgeschwaecht;gemischt;gemischt;verstaerkt` | 2/4 | 0 |
| `rf_06` | explorativ | `abgeschwaecht;gemischt;gemischt;abgeschwaecht` | `abgeschwaecht;verstaerkt;abgeschwaecht;abgeschwaecht` | 2/4 | 0 |
| `rf_07` | ja | `gemischt;gemischt;gemischt;gemischt` | `gemischt;gemischt;gemischt;gemischt` | 4/4 | 1 |
| `rf_08` | ja | `verstaerkt;verstaerkt;verstaerkt;verstaerkt` | `verstaerkt;verstaerkt;verstaerkt;verstaerkt` | 4/4 | 1 |
| `rf_10` | ja | `abgeschwaecht;abgeschwaecht;abgeschwaecht;abgeschwaecht` | `abgeschwaecht;abgeschwaecht;abgeschwaecht;gemischt` | 3/4 | 0 |
| `rf_13` | explorativ | `gemischt;abgeschwaecht;gemischt;abgeschwaecht` | `verstaerkt;abgeschwaecht;abgeschwaecht;gemischt` | 1/4 | 0 |
| `rf_17` | explorativ | `abgeschwaecht;abgeschwaecht;abgeschwaecht;abgeschwaecht` | `abgeschwaecht;abgeschwaecht;abgeschwaecht;abgeschwaecht` | 4/4 | 1 |
| `rf_21` | explorativ | `abgeschwaecht;gemischt;abgeschwaecht;abgeschwaecht` | `gemischt;gemischt;gemischt;gemischt` | 1/4 | 0 |

## Zeitebenen-Tragung

Die Signaturen werden zusätzlich getrennt gelesen. Ein Gesamtprofil kann gegenläufige 1h- und 15m-Reaktionen verdecken.

| Familie | 1h | 15m |
|---|---|---|
| `rf_05` | `gemischt;verstaerkt;verstaerkt;verstaerkt` | `abgeschwaecht;abgeschwaecht;abgeschwaecht;gemischt` |
| `rf_06` | `abgeschwaecht;gemischt;abgeschwaecht;abgeschwaecht` | `gemischt;gemischt;gemischt;abgeschwaecht` |
| `rf_07` | `gemischt;gemischt;gemischt;gemischt` | `gemischt;gemischt;gemischt;gemischt` |
| `rf_08` | `verstaerkt;gemischt;gemischt;verstaerkt` | `verstaerkt;verstaerkt;gemischt;gemischt` |
| `rf_10` | `abgeschwaecht;abgeschwaecht;abgeschwaecht;gemischt` | `abgeschwaecht;abgeschwaecht;gemischt;gemischt` |
| `rf_13` | `verstaerkt;gemischt;verstaerkt;verstaerkt` | `gemischt;abgeschwaecht;abgeschwaecht;gemischt` |
| `rf_17` | `abgeschwaecht;verstaerkt;gemischt;abgeschwaecht` | `abgeschwaecht;abgeschwaecht;abgeschwaecht;abgeschwaecht` |
| `rf_21` | `gemischt;gemischt;verstaerkt;gemischt` | `gemischt;gemischt;gemischt;gemischt` |

## Befund

Von den vier vorab festgelegten vollständigen Familienprofilen replizieren: `rf_07;rf_08`.

Komponentenweise stimmen `13/16` Vorhersagen. Unter den gerichteten Vorhersagen ohne die vier gemischten `rf_07`-Komponenten stimmen `9/12`.

Getrennt auf beiden Zeitebenen und im Gesamtprofil gleichgerichtet tragen von diesen gerichteten Vorhersagen nur `3/12`: `rf_08:sign;rf_10:sign;rf_10:magnitude`. Kein gerichtetes vollständiges Vier-Komponenten-Profil bleibt damit zugleich auf `1h` und `15m` geschlossen.

`rf_08` repliziert als einzige gerichtete Vorhersage das vollständige Gesamtprofil und wird in `9/12` Einzelbedingungen verstärkt. Die Verstärkung verteilt sich jedoch verschieden auf die Zeitebenen. `rf_10` repliziert Vorzeichen, Größe und Docht, während Volumen gemischt bleibt. `rf_05` repliziert nur den schwächeren Vorzeichenpol und den stärkeren Volumenpol; Größe und Docht wechseln ins Mischprofil.

Das vollständige Mischprofil von `rf_07` repliziert formal, ist aber diagnostisch schwächer: Seine Mitgliederabdeckung bleibt über alle vier gebündelten Komponenten unverändert (`ja`). Das Mischprofil kann daher Sättigung beziehungsweise geringe Differenzierbarkeit widerspiegeln und wird nicht mit einer gerichteten Replikation gleichgesetzt.

Explorativ repliziert `rf_17` sein vollständiges Gesamt-Abschwächungsprofil und `10/12` abgeschwächte Einzelbedingungen. Auch dieses Profil ist zeitebenenabhängig: Auf 15m ist es geschlossen, auf 1h nicht.

Der Holdout stützt damit einzelne familienabhängige Phasenachsen, aber keine bereits stabile vollständige Familienindividualität über Zeitebenen. Die Auswertung speichert passive Forschungsevidenz; sie begründet noch keine organische Erweiterung, feste Familienbedeutung oder Runtime-Regel.

## Grenze

Der Holdout wechselt Jahr, Fenster und teilweise Zeitebene, bleibt aber bei BTC/SOL, Marktzeitreihen, `1000` Beobachtungen und derselben Phasenoperation. Er trennt zeitliche Wiederkehr von vollständiger Modalitäts- und Messunabhängigkeit, beweist aber weder Kausalität noch allgemeine Feldintelligenz.
