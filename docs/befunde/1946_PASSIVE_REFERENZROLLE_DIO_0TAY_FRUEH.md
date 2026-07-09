# 1946 - Passive Referenzrolle für dio_0tay/frueh

## Grundfrage

Kann `dio_0tay/frueh` nach der Generalisierungsprüfung als passive Referenzrolle geführt werden, ohne daraus eine Steuerlogik zu machen?

## Umsetzung

`tools/update_mcm_field_role_memory.py` liest jetzt zusätzlich:

`docs/befunde/1945_DIO_0TAY_FRUEH_GENERALISIERUNG.csv`

Daraus wird im bestehenden Block `passive_mcm_field_role_memory` ein neuer Unterblock geschrieben:

`reference_roles`

Dieser Unterblock bleibt passiv:

- keine Handlung
- kein Gate
- keine Richtung
- kein Entry-Signal
- keine Motorik

## Inhalt der Referenzrolle

Die Rolle wird als:

`fruehe_nullnahe_brueckenberuhigung`

geführt.

Sie beschreibt keine Entscheidung, sondern eine wiedererkennbare Feldqualität:

> Eine frühe, nullnahe Brückenberuhigung, die in mehreren Welten wiederkehrt und als Vergleichsanker für passive Rücklesung dienen kann.

## Geschriebene Referenzprofile

Das Update-Tool schreibt 7 Profile:

| Scope | nicht-fehlende Rücklesungen | Nullnähe-Anteil |
| --- | ---: | ---: |
| gesamt | 65 | 0.846154 |
| BTC | 18 | 1.0 |
| SOL | 18 | 1.0 |
| DOGE | 10 | 0.7 |
| XRP | 8 | 0.625 |
| PAXG | 11 | 0.636364 |
| B_Fokus_SOL_BTC | 14 | 1.0 |

## Einordnung

Das ist eine organische Erweiterung der passiven Memory.

Mini-DIO bekommt dadurch keinen neuen Befehl, sondern eine sauberere Rückleseform:

- Wenn eine ähnliche frühe Nullnähe wieder auftaucht, kann sie gegen diese Referenzrolle verglichen werden.
- Wenn sie fehlt, wird nichts blockiert.
- Wenn sie driftet, öffnet oder nachhallnah wird, bleibt das eine passive Weltpassungsinformation.

Damit wird die Memory nicht haerter, sondern lesbarer.

## Wie es weitergeht

Als nächstes sollte geprüft werden, ob weitere stabile Rollen denselben Status verdienen: nicht viele neue Namen, sondern nur Rollen, die über mehrere Welten reproduzierbar genug sind und trotzdem Weltvarianz zulassen.
