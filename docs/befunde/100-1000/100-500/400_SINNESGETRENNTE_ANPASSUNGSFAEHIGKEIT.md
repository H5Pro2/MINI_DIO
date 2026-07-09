# Sinnesgetrennte Anpassungsfaehigkeit

Stand: 2026-06-20

## Grundfrage

Wie kann MINI_DIO Weltkontakt frei aufnehmen, ohne dass das MCM-Feld durch eine globale Dämpfung oder harte Vorsteuerung verfälscht wird?

## Kernsatz

```text
DIO bekommt Fähigkeiten zur Wahrnehmungsanpassung.
Wie stark er diese Fähigkeiten nutzt, muss über Feldrückmeldung und Erfahrung entstehen.
```

Das bedeutet:

- Sehen darf stärker oder schwächer fokussiert werden.
- Hören darf lauter oder leiser ankommen.
- Fühlen/Spüren darf bei Kontakt mehr Druck oder mehr Abstand tragen.
- Diese Achsen dürfen getrennt wirken.
- Keine Achse darf global alle anderen mitdämpfen.

## Fachliche Trennung

```text
Rezeptorische Übersetzung = biologische Aufnahmegrenze
Sinnesgetrennte Anpassung = Fähigkeit des Organismus
MCM-Feldwirkung = direkte Feldrückmeldung
Episodisches Lernen = spätere Verdichtung, was getragen hat
```

Die Rezeptorschicht darf Rohdaten in eine aufnehmbare Sinneswirkung übersetzen.
Sie darf aber nicht heimlich entscheiden, wie das Feld zu reagieren hat.

## Warum keine globale Dämpfung

Eine globale Dämpfung würde bedeuten:

```text
Wenn Welt stark wirkt, wird alles leiser.
```

Das ist zu grob.
Organisch plausibler ist:

```text
Bei dieser Lage höre ich gedämpfter, sehe aber genauer.
Bei jener Lage halte ich Abstand zum Gefühl, lasse aber die Tonspur stärker wirken.
Bei einer anderen Lage reicht Sehen, ohne starken Feldkontakt.
```

Damit entsteht keine mechanische Regel, sondern eine differenzierte Wahrnehmungsfähigkeit.

## Aktueller Codezustand

`mini_dio/mini_world.py` trennt jetzt:

```text
field_intake_pressure
```

von:

```text
adaptation_potential
adapted_field_intake_pressure
regulation_damping
```

`field_intake_pressure` ist die tatsächliche Rezeptorwirkung, die in `mcm_tension` eingeht.

`adaptation_potential`, `adapted_field_intake_pressure` und `regulation_damping` sind Diagnose- und Fähigkeitswerte. Sie zeigen, welche Anpassung möglich wäre, steuern aber das MCM-Feld nicht direkt.

Zusätzlich werden die getrennten Tendenzen sichtbar:

```text
visual_focus_tendency
visual_distance_tendency
auditory_listen_tendency
auditory_softening_tendency
felt_contact_tendency
felt_distance_tendency
```

## Verbindliche Grenze

Diese Werte sind keine Handlung, kein Gate und keine Strategie.

Sie beantworten nur:

```text
Wie könnte DIO diese Weltlage aufnehmen?
```

Nicht:

```text
Was soll DIO jetzt tun?
```

## Konsequenz für MINI_DIO

Die direkte Rückmeldung kommt aus dem MCM-Feld:

- trägt die Aufnahme?
- kippt sie?
- entsteht Überlagerung?
- rekoppelt sie?
- bleibt sie als Nachhall?
- bildet sie wiederkehrende Bedeutung?

Daraus kann später gelernt werden, welche sensorische Anpassung für welche Weltlage tragfähig war.

## Wie es weitergeht

Als nächstes wird mit kurzen Kontrollläufen geprüft, ob `field_intake_pressure` und `adapted_field_intake_pressure` sauber auseinanderfallen: Das Feld soll echte Rezeptorwirkung erleben, während die Anpassungswerte nur als beobachtbare Fähigkeit danebenstehen.
