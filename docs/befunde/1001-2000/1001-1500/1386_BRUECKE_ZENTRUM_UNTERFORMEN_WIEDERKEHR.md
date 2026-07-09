# 1386 - Bruecke/Zentrum-Unterformen: Wiederkehr

## Zweck

Diese Diagnose prueft, ob die Unterformen aus `1385` nur in der isolierten Mischrolle vorkommen oder auch in anderen Rollenfenstern wieder auftauchen.

Die Referenz bleibt die Mischrolle:

```text
mischrolle_brueckennaehe_zentrumsnaehe + gemischte_rohwelt
```

Die Einteilung wird aus der Referenz gelernt und anschliessend passiv auf alle Rollenfenster aus `1382` angewendet.

## Befund

- Referenzfenster: `48`
- Referenzsignaturen gesamt: `42`
- Referenzsignaturen mit mindestens 2 Treffern: `5`
- gepruefte Fenster ausserhalb der Referenz: `121`
- Wiederkehr irgendeiner Referenzsignatur ausserhalb: `48`
- Wiederkehr starker Referenzsignaturen ausserhalb: `12`
- Rollen bei Wiederkehr: `brueckennaehe:27, zentrumsnaehe:8, mischrolle_brueckennaehe_zentrumsnaehe:7, randdrucknaehe:4, mischrolle_brueckennaehe_entlastungsnaehe:2`
- Rollen bei starker Wiederkehr: `brueckennaehe:6, randdrucknaehe:2, mischrolle_brueckennaehe_zentrumsnaehe:2, zentrumsnaehe:2`
- Welten bei Wiederkehr: `DOGE_2024_5M:19, XRP_2024_5M:13, SOL_2024_5M:8, PAXG_2024_5M:5, BTC_2024_5M:3`

## Wiederkehr nach Rollen

- `brueckennaehe`: leise+ruhiger_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:6, mittlerer_ton+ruhiger_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:4, laut+starker_tonwechsel|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:4, leise+bewegter_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:3
- `mischrolle_brueckennaehe_entlastungsnaehe`: laut+starker_tonwechsel|bewegte_form|enge_range+wenig_wechsel+hohe_persistenz|mittlere_aufnahme+mittlere_feldspannung:1, leise+bewegter_ton|stabile_form|weite_range+mittlerer_wechsel+mittlere_persistenz|starke_aufnahme+hohe_feldspannung:1
- `mischrolle_brueckennaehe_zentrumsnaehe`: laut+starker_tonwechsel|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:2, mittlerer_ton+ruhiger_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:1, leise+starker_tonwechsel|stabile_form|enge_range+wenig_wechsel+hohe_persistenz|starke_aufnahme+hohe_feldspannung:1, laut+starker_tonwechsel|stabile_form|weite_range+mittlerer_wechsel+mittlere_persistenz|mittlere_aufnahme+mittlere_feldspannung:1
- `randdrucknaehe`: leise+ruhiger_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:2, leise+ruhiger_ton|stabile_form|mittlere_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:1, leise+ruhiger_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|starke_aufnahme+hohe_feldspannung:1
- `zentrumsnaehe`: leise+ruhiger_ton|stabile_form|mittlere_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:2, leise+ruhiger_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung:2, leise+ruhiger_ton|bewegte_form|weite_range+viel_wechsel+geringe_persistenz|mittlere_aufnahme+mittlere_feldspannung:1, mittlerer_ton+bewegter_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|starke_aufnahme+hohe_feldspannung:1

## Dominante wiederkehrende Signaturen

- `leise+ruhiger_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung`: `10`
- `laut+starker_tonwechsel|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung`: `7`
- `mittlerer_ton+ruhiger_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung`: `5`
- `leise+ruhiger_ton|stabile_form|mittlere_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung`: `4`
- `leise+bewegter_ton|stabile_form|weite_range+viel_wechsel+geringe_persistenz|starke_aufnahme+hohe_feldspannung`: `4`
- `leise+ruhiger_ton|stabile_form|mittlere_range+mittlerer_wechsel+mittlere_persistenz|starke_aufnahme+hohe_feldspannung`: `3`
- `laut+starker_tonwechsel|bewegte_form|enge_range+wenig_wechsel+hohe_persistenz|mittlere_aufnahme+mittlere_feldspannung`: `2`
- `leise+starker_tonwechsel|stabile_form|enge_range+wenig_wechsel+hohe_persistenz|starke_aufnahme+hohe_feldspannung`: `2`

## Lesung

Wenn Referenzsignaturen ausserhalb der Mischrolle wieder auftauchen, ist die Unterform nicht nur an eine einzelne Rollenbezeichnung gebunden.
Wenn starke Referenzsignaturen ausserhalb kaum auftauchen, bleibt die Mischrolle dagegen spezifischer.

Der Befund trennt damit Oberflaechenwiederkehr von Rollenwiederkehr.
Das ist wichtig, weil MINI_DIO dadurch nicht nur Namen, sondern Feldfunktionsnaehen lesen kann.

## Grenze

Die Signaturen sind aus einer Referenzprobe abgeleitet.
Sie sind kein abgeschlossenes Lexikon, sondern eine passive Vergleichsschicht.
