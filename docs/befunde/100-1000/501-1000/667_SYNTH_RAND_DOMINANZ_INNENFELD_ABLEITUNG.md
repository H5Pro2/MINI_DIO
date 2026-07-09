# Synthetische Randdominanz - Innenfeldableitung

Stand: 2026-06-22

## Zweck

Diese Synthese prüft, ob MINI_DIO bei gezielt stärkerer künstlicher Randlast einen klaren Spannungsrand ausbildet oder ob Randlast überwiegend in offene Variante und Rekopplungsnähe übersetzt wird.

Die Auswertung bleibt passiv. Die synthetischen Phasen sind nur Diagnosehilfe.

## Hierarchie

1. Grundfrage: Kann eine synthetische Welt echte Randdominanz im MCM-Feld auslösen?
2. Unterprüfung: Welche Phase trägt den stärksten Rand-/Kippanteil?
3. Unterprüfung: Bleibt der Effekt lokal oder kippt die ganze Welt in Randlast?
4. Folgeschritt: Entscheiden, ob der Rezeptor-/Feldaufbau Randlast schützt oder ob die Randwelt noch stärker getrennt werden muss.

## Gesamtbefund

| Welt | Zentrum | Offen | Rand/Kipp | Rekopplung | Carry | Strain | Sinneskopplung |
|---|---:|---:|---:|---:|---:|---:|---:|
| SYNTH_RAND_A | 0.9375 | 0.0603 | 0.0021 | 0.7405 | 0.5898 | 0.1311 | 0.8979 |
| SYNTH_RAND_B | 0.9375 | 0.0603 | 0.0021 | 0.7405 | 0.5898 | 0.1311 | 0.8979 |

Die Randdominanz-Welt bleibt reproduzierbar und weiter `stark_zentriert_wenig_rand`.

Gegenüber den vorherigen synthetischen Welten nimmt die Belastung aber zu:

| Diagnose | Harmonie | Bruch/Rand | Randdominanz |
|---|---:|---:|---:|
| Unique Syntax | 42 | 166 | 222 |
| Zentrum | 0.9991 | 0.9563 | 0.9375 |
| Offen | 0.0007 | 0.0430 | 0.0603 |
| Rand/Kipp | 0.0002 | 0.0007 | 0.0021 |
| Tragend unruhig | 4 | 258 | 422 |
| Kippend | 1 | 1 | 13 |

## Phasenbefund

Die stärkste Phase ist `laute_randphase`:

| Phase | Zentrum | Offen | Rand/Kipp | Rekopplung | Feldinput | Lautheit | Schärfe |
|---|---:|---:|---:|---:|---:|---:|---:|
| laute_randphase | 0.0762 | 0.7113 | 0.0600 | 0.6716 | 0.1644 | 0.2779 | 0.5375 |

Das ist der bisher deutlichste lokale Rand-/Öffnungsbefund.

Trotzdem wird kein globaler Randkollaps erzeugt:

- `rekopplungsversuch` geht zurück auf Zentrum `0.9914`,
- `ruhe_restspannung` bleibt Zentrum `0.9933`,
- `schluss_rekopplung` steigt auf Zentrum `0.9970`.

## Arbeitslesart

MINI_DIO bildet bei Randdominanz keinen dauerhaften Spannungsrand als globale Feldlage.

Stattdessen passiert bisher:

```text
starke Randphase -> offene Variante dominiert lokal
Rand/Kipp wird sichtbar, aber bleibt begrenzt
danach rekoppelt das Feld zurück ins Zentrum
```

Das spricht dafür, dass die Rezeptorschicht und das MCM-Feld gemeinsam Randlast nicht einfach roh übernehmen. Randlast wird in offene Variante, Rekopplungsnähe und lokale Rand/Kipp-Anteile übersetzt.

## Bedeutung

Der Befund ist wichtig, weil er die bisherige MCM-Lesart präzisiert:

```text
Das Feld ist nicht randunfähig.
Es bildet Rand/Kipp lokal aus.
Aber es bevorzugt bisher Rückbindung statt globalem Kollaps.
```

Das passt zur bisherigen passiven Eigenregulations-Lesart des Feldes.

## Grenze

Dieser Befund zeigt keine universelle Schutzfunktion.

Er zeigt nur:

- innerhalb dieser synthetischen Welt,
- mit aktueller Rezeptorschicht,
- in passiver MINI_DIO-Lesung,
- bleibt Randdominanz lokal begrenzt und wird nicht zur globalen Topologie.

## Wie es weitergeht

Als nächstes sollte kein noch härteres Rauschen gebaut werden. Sinnvoller ist eine Differenzdiagnose: Welche Rezeptorachsen begrenzen den Rand? Also getrennt prüfen, ob Hören, Sehen, Feldinput oder Adaptation die `laute_randphase` zurück in offene Variante/Rekopplung übersetzen.
