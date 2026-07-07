# 006 - Adaptive passive Rekopplung

## Begriff

Adaptive passive Rekopplung bezeichnet eine zweite, erfahrungsgewichtete Lesung der MCM-Rueckfuehrung.

Die bisherige `mcm_rekopplung_quality` bleibt als stabile Referenz erhalten. Daneben wird `mcm_adaptive_rekopplung_quality` geschrieben.

## Warum zwei Werte

Die statische Rekopplung beantwortet:

```text
Wie rekoppelt diese Lage nach der Grundformel?
```

Die adaptive Rekopplung beantwortet:

```text
Wie rekoppelt diese Lage, wenn fruehere passive Episoden mitsprechen?
```

Damit wird die Rueckfuehrung nicht mehr nur durch feste Gewichte gelesen. Wiederkehrende Erfahrung kann verschieben, ob Tragen, Alignment, Strain-Entlastung oder Sinneskopplung staerker in die aktuelle Feldlesung eingehen.

## Funktion

Die adaptive Rekopplung ist passiv.

Sie ist:

- keine Handlung,
- kein Gate,
- keine Richtungsvorgabe,
- keine Strategie,
- kein Ersatz fuer die statische Referenz.

Sie dient nur dazu, erfahrungsnahe Feldrueckfuehrung sichtbar zu machen.

## Mechanik

Pro Lage werden vier Anteile gelesen:

- `mcm_carry_quality`: tragende Feldnaehe,
- `reflection_alignment`: innere Ausrichtung,
- `1 - mcm_strain_quality`: Entlastung von Feldspannung,
- `sensory_coupling`: Sinnes-MCM-Kopplung.

Ohne Erfahrung nutzt MINI_DIO die statische Gewichtung:

```text
carry 0.42
alignment 0.24
strain_relief 0.20
sensory 0.14
```

Mit Erfahrung werden Episoden aus `episode_memory` gelesen. Wenn eine passende Symbolfamilie vorhanden ist, wird zuerst diese Familie genutzt. Sonst wird die gesamte Episodenerfahrung verwendet.

Seit der Rollen-/Pfaderweiterung wird diese Erfahrung nicht mehr nur als Familienmittel gelesen. Zusaetzlich werden zwei passive Naehen gebildet:

- `mcm_adaptive_role_experience`: wie stark die aktuelle Feldrolle bereits getragen ist,
- `mcm_adaptive_path_experience`: wie stark der aktuelle Zustandsuebergang bereits getragen ist.

Daraus entsteht ein Milieu:

- `milieu_offen`: allgemeine Erfahrung vorhanden, aber Rolle und Pfad noch nicht tragend,
- `milieu_rollennah`: die Feldrolle ist erfahrungsnah,
- `milieu_pfadnah`: der Uebergangspfad ist erfahrungsnah,
- `milieu_rolle_und_pfad_getragen`: Rolle und Pfad tragen gemeinsam.

Diese Milieus sind passive Lesungen. Sie sind keine Handlungsanweisung.

Aus dieser Erfahrung entstehen dynamische Gewichte:

```text
carry_weight
alignment_weight
strain_relief_weight
sensory_weight
```

Diese Gewichte werden normalisiert und als Debugfelder ausgegeben.

## Zustandslesung

Die adaptive Schicht schreibt:

- `adaptive_untrained`: keine passende Erfahrung vorhanden,
- `adaptive_jung`: Erfahrung vorhanden, aber noch jung,
- `adaptive_rekopplung_angehoben`: adaptive Lesung liegt klar ueber der statischen Referenz,
- `adaptive_rekopplung_gedaempft`: adaptive Lesung liegt klar unter der statischen Referenz,
- `adaptive_rekopplung_nahe_statisch`: adaptive und statische Lesung liegen nahe beieinander.

## Erster Smoke-Befund

Ein erster Smoke-Lauf mit BTC 2024 5m, 1000 Zeilen und frischer Memory zeigte:

```text
avg_mcm_rekopplung_quality          0.683874
avg_mcm_adaptive_rekopplung_quality 0.728393
max_mcm_adaptive_rekopplung_quality 0.793495
avg_mcm_adaptive_rekopplung_experience 0.613291
```

Die adaptive Schicht wurde im Lauf sichtbar:

```text
adaptive_untrained 5
adaptive_jung 300
adaptive_rekopplung_angehoben 689
```

Das ist noch kein abschliessender Befund. Es zeigt aber, dass die adaptive Rekopplung technisch greift und nicht nur als leerer Platzhalter geschrieben wird.

## Erster Mehrwelt-Befund

Eine erste Mehrweltpruefung ueber BTC, DOGE, XRP, Seitwaerts, Stress und Expansion zeigte:

```text
Adaptive Rekopplung ist in allen Welten aktiv.
Die Anhebung gegenueber der statischen Referenz ist aber noch relativ gleichfoermig.
```

Das bedeutet:

```text
Die Rueckfuehrung ist lernbar gemacht.
Die Feinselektion nach Symbolfamilie und Weltmilieu muss noch staerker untersucht werden.
```

Der zugehoerige Befund liegt in [1680_ADAPTIVE_REKOPPLUNG_MEHRWELT_ACHSENREPORT.md](../befunde/1680_ADAPTIVE_REKOPPLUNG_MEHRWELT_ACHSENREPORT.md).

Die Gewichtsstreuung war in dieser ersten Pruefung noch sehr gering:

```text
carry         Spanne 0.0022
alignment     Spanne 0.0006
strain_relief Spanne 0.0016
sensory       Spanne 0.0007
```

Das ist fachlich wichtig: Die Schicht funktioniert, aber sie differenziert noch nicht ausreichend nach Feldrolle.

## Rollen-/Pfad-Befund

Die Rollen-/Familienpruefung ueber BTC, XRP und DOGE zeigte:

```text
BTC  beginnende Differenzierung
DOGE beginnende Differenzierung
XRP  flachere Differenzierung
```

Der anschliessende BTC-Kontrolllauf mit Rollen- und Pfaderfahrung zeigte:

```text
milieu_untrained                   5
milieu_offen                     403
milieu_pfadnah                    34
milieu_rolle_und_pfad_getragen   306
milieu_rollennah                 246
```

Damit wird die adaptive Rekopplung nicht mehr nur global angehoben. MINI_DIO kann jetzt passiv unterscheiden, ob eine Rueckfuehrung allgemein erfahrungsnah, rollennah, pfadnah oder gemeinsam getragen ist.

Die zugehoerigen Befunde liegen in:

- [1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN_BTC.md](../befunde/1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN_BTC.md)
- [1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN_DOGE.md](../befunde/1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN_DOGE.md)
- [1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN_XRP.md](../befunde/1681_ADAPTIVE_REKOPPLUNG_ROLLEN_FAMILIEN_XRP.md)
- [1682_ADAPTIVE_REKOPPLUNG_MILIEU_BTC_KONTROLLLAUF.md](../befunde/1682_ADAPTIVE_REKOPPLUNG_MILIEU_BTC_KONTROLLLAUF.md)

## Erweiterter Mehrwelt-Befund

Eine Folgepruefung ueber DOGE, XRP, PAXG und eine Stress-Gegenwelt bestaetigt, dass die Milieu-Lesung nicht auf BTC beschraenkt ist.

Kompakt:

```text
DOGE   statisch 0.685038 -> adaptiv 0.729084
XRP    statisch 0.676695 -> adaptiv 0.721852
PAXG   statisch 0.700467 -> adaptiv 0.743298
Stress statisch 0.686648 -> adaptiv 0.731231
```

Die gleichen Symbolfamilien koennen dabei je nach Weltmilieu anders gelesen werden. Eine Familie kann in einer Welt rollennah, in einer anderen offen oder pfadnah erscheinen.

Damit ist die adaptive Rekopplung nicht nur eine globale Anhebung. Sie wird als passive Milieulesung lesbar:

```text
Feldrolle
  -> Uebergangspfad
  -> Erfahrungsnaehe
  -> Milieu
  -> adaptive Rekopplungsqualitaet
```

Der Befund liegt in [1683_ADAPTIVE_MILIEU_MEHRWELT_VERGLEICH.md](../befunde/1683_ADAPTIVE_MILIEU_MEHRWELT_VERGLEICH.md).

## Langfenster-Befund

Eine laengere Pruefung ueber DOGE, XRP, PAXG und Stress zeigt:

```text
Mehr Feldzeit macht offene Milieus nicht automatisch geschlossen.
```

In allen Langfenstern bleibt `milieu_offen` deutlich vorhanden. Gleichzeitig wachsen rollennahe und gemeinsam getragene Milieus mit.

Damit wird Reifung nicht als Verschwinden von Offenheit gelesen, sondern als Koexistenz:

```text
offene Varianz
  + rollennahe Erfahrung
  + pfadnahe Teilspur
  + gemeinsam getragene Rekopplungsnaehe
```

Der Befund liegt in [1684_ADAPTIVE_MILIEU_LANGFENSTER_VERGLEICH.md](../befunde/1684_ADAPTIVE_MILIEU_LANGFENSTER_VERGLEICH.md).

## Familienlagen-Befund

Eine weitere Pruefung trennt die Milieus nicht nur nach Tick-Anteilen, sondern nach Symbolfamilien.

Die Grundfrage war:

```text
Ist `milieu_offen` eine getrennte Schicht oder ein Vorraum gereifter Familien?
```

Der Befund ueber DOGE, XRP, PAXG und Stress:

```text
DOGE   226 von 621 Familien beruehren offen und gereift
XRP    256 von 700 Familien beruehren offen und gereift
PAXG   197 von 496 Familien beruehren offen und gereift
Stress 114 von 411 Familien beruehren offen und gereift
```

Damit ist Offenheit nicht einfach ein unreifer Restbereich. Ein relevanter Teil der Familien taucht sowohl offen als auch gereift auf. Besonders PAXG zeigt eine hohe Familienueberlappung, waehrend die Stresswelt staerker trennt.

Fachlich wird `milieu_offen` deshalb vorerst so gelesen:

```text
offene Varianzschicht
  -> kann getrennt bleiben
  -> kann dieselbe Familie spaeter gereift beruehren
  -> ist nicht automatisch Fehler, Rauschen oder fehlende Reifung
```

Der Befund liegt in [1685_ADAPTIVE_MILIEU_FAMILIENSCHICHTEN.md](../befunde/1685_ADAPTIVE_MILIEU_FAMILIENSCHICHTEN.md).

## Folgewelt-Befund

Eine Folgeweltpruefung mit spaeteren Segmenten derselben Weltquellen zeigt:

```text
DOGE   Familienueberlappung 0.5120, Offen+Gereift -0.0559
XRP    Familienueberlappung 0.4356, Offen+Gereift -0.0339
PAXG   Familienueberlappung 0.5702, Offen+Gereift -0.0083
Stress Familienueberlappung 0.4901, Offen+Gereift +0.0135
```

Damit bleibt ein gemeinsamer Familienkern sichtbar, aber die Milieu-Relationen verschieben sich.

Die Lesung:

```text
Familie bleibt erkennbar
  -> Milieu kann sich verschieben
  -> Offenheit ist dynamische Varianzschicht
  -> Reifung ist keine starre Endform
```

Besonders wichtig ist der Unterschied zwischen PAXG und Stress. PAXG haelt die Offen/Gereift-Ueberlappung fast stabil, waehrend Stress trotz kuerzerem Fenster leicht mehr gemeinsame Offen/Gereift-Familien bildet. Das spricht dafuer, dass Weltkontakt nicht nur Familien erzeugt, sondern auch ihre Milieu-Lage verschiebt.

Die Befunde liegen in:

- [1686_ADAPTIVE_MILIEU_FAMILIENSCHICHTEN_FOLGEWELT.md](../befunde/1686_ADAPTIVE_MILIEU_FAMILIENSCHICHTEN_FOLGEWELT.md)
- [1687_ADAPTIVE_MILIEU_FOLGEWELT_VERGLEICH.md](../befunde/1687_ADAPTIVE_MILIEU_FOLGEWELT_VERGLEICH.md)

## Relationswechsel und Rohweltphasen

Die naechste Pruefung liest starke Milieu-Relationswechsel gegen konkrete Rohweltphasen zurueck.

Geprueft wurden DOGE, XRP, PAXG und Stress. Der staerkste Wechsel ist:

```text
offen_und_gereift -> nur_gereift
```

Das bedeutet:

```text
Eine Familie bleibt in der Folgewelt sichtbar.
Die offene Schicht nimmt ab.
Die gereifte Lesung bleibt oder wird enger.
```

Kompakt:

```text
offen_und_gereift -> nur_gereift       215
nur_gereift -> offen_und_gereift       108
offen_und_gereift -> nur_offen          33
nur_offen -> offen_und_gereift          26
```

Die Rohweltspalten zeigen Nettoverlauf, Range, Hoer-Gap und Feldspannung der jeweiligen Episodenphase.

Wichtig:

```text
Das ist Ruecklesung, kein Ursachebeweis.
```

Der Befund liegt in [1688_ADAPTIVE_MILIEU_RELATIONSWECHSEL_ROHWELT.md](../befunde/1688_ADAPTIVE_MILIEU_RELATIONSWECHSEL_ROHWELT.md).

## Jahresvergleich

Ein 2025-Gegenlauf mit DOGE, XRP, PAXG und Stress zeigt dieselben vier Relationswechsel:

```text
offen_und_gereift -> nur_gereift
nur_gereift -> offen_und_gereift
offen_und_gereift -> nur_offen
nur_offen -> offen_und_gereift
```

Die Gewichtung verschiebt sich:

```text
2024: offen_und_gereift -> nur_gereift dominiert staerker.
2025: nur_gereift -> offen_und_gereift waechst deutlich mit.
```

Zwischen beiden Jahren ueberlappen `155` Wechsel-Familien.

Lesung:

```text
Die Wechselarchitektur bleibt sichtbar.
Die einzelne Milieu-Lage bleibt beweglich.
MINI_DIO bildet keine starre Symboltabelle.
```

Der Befund liegt in [1691_ADAPTIVE_MILIEU_2024_2025_VERGLEICH.md](../befunde/1691_ADAPTIVE_MILIEU_2024_2025_VERGLEICH.md).

## Wiederkehrende Einzelfamilien

Die naechste Ruecklesung verfolgt gleiche Familie plus gleiche Wechselrichtung ueber 2024 und 2025.

Der Befund:

```text
gleiche Familie plus gleicher Wechsel: 111
```

Die Hauptspuren liegen wieder in:

```text
offen_und_gereift -> nur_gereift
nur_gereift -> offen_und_gereift
```

Das ist wichtig, weil hier nicht nur eine Gesamtverteilung wiederkehrt. Einzelne Familien geraten in unterschiedlichen Weltjahren erneut in dieselbe Milieu-Bewegung.

Lesung:

```text
Familie ist wiedererkennbar.
Milieu bleibt beweglich.
Wechselrichtung kann wiederkehren.
Rohweltnaehe muss weiter geprueft werden.
```

Der Befund liegt in [1692_ADAPTIVE_MILIEU_WIEDERKEHRFAMILIEN_2024_2025.md](../befunde/1692_ADAPTIVE_MILIEU_WIEDERKEHRFAMILIEN_2024_2025.md).

## Drittperiodenpruefung

Die 2024/2025-Kandidaten wurden danach gegen eine dritte Periode gelesen.

Geprueft wurden vier 2023-Welten:

```text
NEG_STRESS_2023
EXPANSION_2023
MOD_NEG_2023
ALTSEQ_2023
```

Die Relationswechsel bleiben sichtbar:

```text
nur_gereift -> offen_und_gereift       155
offen_und_gereift -> nur_gereift       138
nur_offen -> offen_und_gereift          34
offen_und_gereift -> nur_offen          34
```

Von den `111` Wiederkehr-Kandidaten aus 2024/2025 tauchen `55` in 2023 erneut mit gleicher Familie und gleicher Wechselrichtung auf.

Lesung:

```text
Die Milieu-Bewegung ist nicht nur eine 2024/2025-Einzelerscheinung.
Etwa die Haelfte der isolierten Kandidaten findet eine Drittperioden-Entsprechung.
Die Bewegung bleibt aber weltgefaerbt und nicht deterministisch.
```

Die wichtigsten Berichte:

- [1693_ADAPTIVE_MILIEU_FAMILIENSCHICHTEN_2023.md](../befunde/1693_ADAPTIVE_MILIEU_FAMILIENSCHICHTEN_2023.md)
- [1694_ADAPTIVE_MILIEU_RELATIONSWECHSEL_ROHWELT_2023.md](../befunde/1694_ADAPTIVE_MILIEU_RELATIONSWECHSEL_ROHWELT_2023.md)
- [1695_ADAPTIVE_MILIEU_DRITTPERIODE_TREFFER.md](../befunde/1695_ADAPTIVE_MILIEU_DRITTPERIODE_TREFFER.md)

## Rohwelt-Lupe der Treffer

Die rohweltnaechsten Treffer aus 1695 wurden anschliessend in ihren Episodenabschnitten gelesen.

Die Top-20-Treffer teilen sich relativ zum eigenen Datensatz in:

```text
rangegetriebene_umgebung  9
hoerprofil_entlastet      5
milieu_umlagert_nahe      5
hoerprofil_springt_hoch   1
```

Die wichtigste Arbeitsklasse ist `milieu_umlagert_nahe`.

Lesung:

```text
Familie und Wechselrichtung wiederholen sich.
Vorfenster und Folgephase bleiben in Hoeren und Spannung relativ nah.
Die Milieuschicht verschiebt sich, ohne dass ein komplett neuer Rohreiz sichtbar sein muss.
```

Das trennt zwei weitere Prueffragen:

```text
Innerfeldnahe Umlagerung:
  aehnliche Welt-/Feldlage, andere Milieuschicht.

Weltgetriebene Umfaerbung:
  Range, Hoeren oder Feldspannung veraendern die Familienlage sichtbar.
```

Die Berichte:

- [1696_ADAPTIVE_MILIEU_DRITTPERIODE_ROHWELT_LUPE.md](../befunde/1696_ADAPTIVE_MILIEU_DRITTPERIODE_ROHWELT_LUPE.md)
- [1697_ADAPTIVE_MILIEU_LUPENPROFILE.md](../befunde/1697_ADAPTIVE_MILIEU_LUPENPROFILE.md)

## Ziel-Familien gegen Assetfenster

Die `milieu_umlagert_nahe`-Familien aus 1697 wurden danach gegen BTC, DOGE, XRP und PAXG gelesen.

Der Befund:

```text
Zielzeilen aus 1697:                         5
Exakte Treffer in anderen Assetfenstern:     3
Ziel-Familien mit irgendeinem Relationswechsel: 4
Asset-Relationswechsel gesamt:             399
```

Besonders relevant:

```text
dio_0ly7  nur_gereift -> offen_und_gereift
dio_01hu  nur_gereift -> offen_und_gereift
```

Beide zeigen dieselbe Bewegungsrichtung ausserhalb der 2023-Pruefung erneut.

Lesung:

```text
Das spricht fuer wiederkehrende innere Milieu-Bewegung.
Es beweist noch keine feste Bedeutung.
Es trennt robuste Kandidaten von nur lokalen Drittperioden-Erscheinungen.
```

Der Befund liegt in [1700_ADAPTIVE_MILIEU_ZIELFAMILIEN_ASSET_GEGENPROBE.md](../befunde/1700_ADAPTIVE_MILIEU_ZIELFAMILIEN_ASSET_GEGENPROBE.md).

## Oeffnungs-Vorform

`dio_0ly7` und `dio_01hu` wurden in ihren Asset-Folgefenstern tiefer gelesen.

Aggregiert ueber fuenf Treffer:

```text
Vorfenster:
  Range      0.1100
  Hoeren     0.0958
  Spannung   0.0995

Oeffnungsfamilie:
  Range      0.0974
  Hoeren     0.0556
  Spannung   0.0594
```

Damit faellt in der Oeffnungsfamilie vor allem Hoeren-Gap und Feldspannung ab.

Vorlaeufige Arbeitslesung:

```text
milieu_oeffnet_nach_entlastung
```

Gemeint ist:

```text
moderate Vorlast
  -> geringerer Hoer-Gap
  -> geringere Feldspannung
  -> gleiche Familienbewegung in mehreren Welten
```

Das spricht eher fuer eine Rekopplungs-/Entlastungsbewegung als fuer ein reines Stress- oder Rangeereignis.

Grenze:

```text
Die Stichprobe ist klein.
Die Kandidaten sind robust, aber noch keine feste Bedeutungsdefinition.
```

Die Berichte:

- [1701_ADAPTIVE_MILIEU_ZIELFAMILIEN_ROHWELTFENSTER.md](../befunde/1701_ADAPTIVE_MILIEU_ZIELFAMILIEN_ROHWELTFENSTER.md)
- [1702_ADAPTIVE_MILIEU_OEFFNUNGS_VORFORM.md](../befunde/1702_ADAPTIVE_MILIEU_OEFFNUNGS_VORFORM.md)

## 10k-Pruefung der Oeffnungs-Vorform

Die gleiche Arbeitsform wurde danach in frischen durchlaufenden 10k-Welten gelesen.

Geprueft:

```text
BTC 2024 5m 10k
DOGE 2024 5m 10k
XRP 2024 5m 10k
PAXG 2024 5m 10k
```

Aggregat ueber 304 Vorkommen:

```text
Vorfenster Hoeren     0.0985
Zielzeichen Hoeren    0.0570
Delta Hoeren         -0.0415

Vorfenster Spannung   0.1016
Zielzeichen Spannung  0.0607
Delta Spannung       -0.0409
```

Damit bleibt die Entlastungsbewegung auch ohne reine 5000er Basis/Folge-Splittung sichtbar.

Familiengetrennt:

```text
dio_01hu: Delta Hoeren -0.0302, Delta Spannung -0.0307
dio_0ly7: Delta Hoeren -0.0500, Delta Spannung -0.0485
```

Lesung:

```text
milieu_oeffnet_nach_entlastung
  bleibt als passive Arbeitsform tragfaehig
  ist aber noch keine feste Bedeutungsdefinition
```

Der Bericht liegt in [1703_ADAPTIVE_MILIEU_OEFFNUNGS_VORFORM_10K.md](../befunde/1703_ADAPTIVE_MILIEU_OEFFNUNGS_VORFORM_10K.md).

## Forschungsgrenze

Aus dieser Mechanik folgt noch nicht:

```text
Das Feld entscheidet besser.
Das Feld handelt.
Das Feld beweist adaptive Intelligenz.
```

Sauberer ist:

```text
MINI_DIO kann passive Rueckfuehrung erfahrungsgewichtet sichtbar machen.
```

## Wie es weitergeht

Als naechstes werden die haeufigsten Wechsel-Familien ueber weitere Folgewelten verfolgt. Entscheidend ist, ob dieselbe Familie wiederholt unter aehnlicher Rohweltspannung reift, oeffnet oder ihre Milieu-Lage verschiebt.
