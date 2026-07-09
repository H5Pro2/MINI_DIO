# 1014 - MCM-Achsentypen Wiederkehrpruefung

Passive Gegenprobe, ob die in 1012 gelesenen Chart-/MCM-Typen in weiteren Welten wiederkehren.

## Kurzbefund

- Referenztypen aus 1012: 8
- Gepruefte Achsenfenster: 3
- Bekannte Referenztypen: 1
- Neue oder erweiterte Typen: 2

## Typen

| Typ | Status | Anzahl | Quellen | Welten | Bewegung | Return % | Range % | Druck | Rekopplung | Deutung |
|---|---|---:|---|---|---|---:|---:|---:|---:|---|
| konsolidierung_mit_bruchnaehe | known_reference_type | 1 | KAS_GEGENPROBE:1 | KAS2024_15M_ASSET_PROBE:1 | bewegungsbruch_zone:1 | 0.289687 | 1.602935 | 0.043764 | 0.002671 | Konsolidierung zeigt Bruchnaehe oder gespannte Struktur. |
| rekopplung_nach_abverkauf | new_or_extended_type | 2 | KAS_GEGENPROBE:2 | KAS2024_1H_ASSET_PROBE:2 | bewegungsbruch_zone:1 <br> rekopplungs_uebergang:1 | 47.580748 | 96.986538 | 0.085577 | 0.022225 | Nach einem Abverkauf entsteht ein lokales Rekopplungsfenster. |

## Einzelzuordnung

| Status | Typ | Quelle | Welt | Paar | Ticks | Chartzone | MCM-Bewegung | Fenster % | Range % |
|---|---|---|---|---|---|---|---|---:|---:|
| known_reference_type | konsolidierung_mit_bruchnaehe | KAS_GEGENPROBE | KAS2024_15M_ASSET_PROBE | `183drjy->1t5bcxp` | 1970-1982 | `ruhige_konsolidierung` | `bewegungsbruch_zone` | 0.289687 | 1.602935 |
| new_or_extended_type | rekopplung_nach_abverkauf | KAS_GEGENPROBE | KAS2024_1H_ASSET_PROBE | `183drjy->1t5bcxp` | 447-1665 | `rekopplung_nach_abverkauf` | `bewegungsbruch_zone` | 48.426102 | 97.841511 |
| new_or_extended_type | rekopplung_nach_abverkauf | KAS_GEGENPROBE | KAS2024_1H_ASSET_PROBE | `1t5bcxp->183drjy` | 444-1656 | `rekopplung_nach_abverkauf` | `rekopplungs_uebergang` | 46.735395 | 96.131566 |

## Befund

Die Pruefung trennt bekannte Referenztypen von neu entstehenden oder erweiterten Typen. Bekannte Typen sprechen fuer Wiederkehr der Feld-/Chart-Lesung. Neue Typen sind nicht automatisch Fehler; sie koennen echte Erweiterungen durch andere Weltspannung, Assetklasse oder Zeitebene sein.

## Wie es weitergeht

Als naechstes sollten die neuen oder erweiterten Typen getrennt gelesen werden: Welche entstehen durch andere Assetspannung, welche durch Zeitebene, und welche durch echte neue MCM-Uebergangsqualitaet.
