# 1852 - Passive Familien-Anschlusskarte im Memory

## Grundfrage

Kann die familiengenaue Anschlussqualität aus `1851` passiv in die Feldrollen-Memory übernommen werden, ohne daraus Steuerung, Handlung oder Richtung zu machen?

## Umsetzung

`tools/update_mcm_field_role_memory.py` schreibt nun zusätzlich zur bisherigen Feldrollen-Memory eine passive `family_attachment_quality`.

Diese Karte enthält:

- Familienprofile aus `1851_FAMILIEN_ANSCHLUSSQUALITAET.csv`,
- Asset/Familien-Profile,
- dominante Anschlussqualität,
- Profilzustand,
- Anschlussprofil,
- mittleren Nachhall,
- mittlere Feldzeit,
- mittleren Feldvorsprung.

Die Karte ist ausdrücklich passiv:

- kein Gate,
- keine Handlung,
- keine Richtung,
- kein Entry-Signal,
- keine Motorik.

## Laufbefund

Der Updater meldet:

```text
top_roles=48
states={'feldrolle_anschlussfaehig': 107, 'feldrolle_reift_verdichtend': 37}
attachment_quality={'offen_gemischt': 8, 'kernnah': 5, 'kernnah_ohne_feldzeit': 3, 'nullnah': 2, 'nachhallnah_ohne_kern': 1, 'anschlussnah': 1}
family_attachment_quality={'familienanschluss_deutlich': 36, 'familienanschluss_leicht': 8, 'familienanschluss_offen_gemischt': 8, 'einzelbeleg': 1}
```

## Einordnung

Das ist eine organische Erweiterung der Reifungsbahn:

Die bisherige Memory konnte tragen, dass eine Familie über Phasen anschlussfähig oder verdichtend wirkt. Die neue Karte ergänzt, in welchem Weltkontext diese Familie wiederkehrt: eher kernnah, nachhallnah, offen, nullnah oder gemischt.

Damit entsteht keine feste Wortbedeutung. Es entsteht eine passive Bedeutungslage:

```text
Familie
+ Weltkontext
+ Anschlussqualität
+ Nachhall
+ Feldzeit
= passives Bedeutungsprofil
```

Der Befund bleibt vorsichtig zu lesen. Die Karte zeigt nicht, dass eine Familie immer dasselbe bedeutet. Sie zeigt eher, dass Bedeutung im MCM-Feld kontextabhängig reift.
