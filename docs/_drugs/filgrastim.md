---
layout: default
title: Filgrastim
parent: Kun modelforudsigelse (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Filgrastim: forudsagt ny indikation Primær frigivelsesforstyrrelse af blodplader (evidensniveau L5). Oprindelig indikation: Konstitutionel neutropeni, svær kongenit neutropeni…"
monitor_inn: "Filgrastim"
predicted_indications: ["primary release disorder of platelets", "primary release disorder of platelets", "pseudo-von Willebrand disease", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Glanzmann thrombasthenia", "Scott syndrome", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "hemorrhagic disorder due to a constitutional thrombocytopenia"]
---

# Filgrastim
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

# Filgrastim: Fra svær kongenit neutropeni til primær frigivelsesforstyrrelse af blodplader

## Resumé i én sætning

Filgrastim er en rekombinant G-CSF-analog (granulocytkolonistimulerende faktor), som oprindeligt anvendes til behandling af kronisk og kongenit neutropeni, herunder svær kongenit neutropeni og cyklisk hæmatopoiese.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **primær frigivelsesforstyrrelse af blodplader**,
men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter denne forudsigelse. Forudsigelsen bygger udelukkende på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Konstitutionel neutropeni, svær kongenit neutropeni, cyklisk hæmatopoiese, kronisk familiær neutropeni (fra TxGNN-vidensgrafen; indikationsteksten i den danske godkendelse er ikke tilgængelig) |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN-forudsigelsesscore | 99,998 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Filgrastim er dog en rekombinant G-CSF-analog, som virker via G-CSF-receptoren på myeloide celler, især neutrofile progenitorer, og derved øger produktionen af neutrofile granulocytter. Det er grundlaget for den dokumenterede effekt ved neutropeni.

Primær frigivelsesforstyrrelse af blodplader er en kvalitativ defekt i blodpladernes funktion (sekretion fra granula) og ikke en følge af nedsat neutrofilproduktion. Der er derfor ikke noget kendt biologisk led mellem G-CSF-receptorsignalering og denne sygdom. Den høje modelscore afspejler sandsynligvis nærhed mellem noder i vidensgrafen (hæmatologiske sygdomme) frem for en reel biologisk begrundelse.

Det samme gælder de øvrige forudsigelser i datasættet, som alle er på evidensniveau L5:
- **Pseudo-von Willebrands sygdom** (score 99,997 %): skyldes gain-of-function-varianter i GP1BA, som øger blodpladernes GPIb-affinitet for VWF. G-CSF-signalering har ingen kendt effekt på denne mekanisme.
- **Glanzmanns trombasteni** (score 99,996 %): skyldes mangel på eller dysfunktion af integrin αIIbβ3 (GPIIb/IIIa). Filgrastim genopretter ikke denne receptors funktion.
- **Scotts syndrom** (score 99,956 %): skyldes defekt fosfatidylserineksponering på aktiverede blodplader (ANO6/TMEM16F). Filgrastim har ingen kendt rolle her.
- **Hæmoragisk lidelse som følge af konstitutionel trombocytopeni** (score 99,911 %): involverer defekter i megakaryopoiese eller blodpladeproduktion. Filgrastim virker primært på den granulocytære linje, så en sammenhæng er spekulativ.

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106573220 | Accofil (Accord Healthcare S.L.U.) | Injektions-/infusionsvæske, opløsning, fyldt injektionssprøjte | Indikationstekst ikke tilgængelig |

Tilladelsen er gyldig og omfatter et enkeltstofpræparat. Administrationsvejen er injektion.

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Interaktionssøgningen er gennemført og har identificeret 100 registrerede interaktioner. De fremhævede er alle klassificeret som **moderate** (kilde: DDInter). Eksempler på de interagerende stoffer:
- Radioaktive lægemidler og diagnostika: iobenguan (I-131), fludeoxyglucose (18F), ibritumomab tiuxetan, tositumomab (med og uden I-131)
- Cytostatika og immunmodulerende stoffer: paclitaxel, mercaptopurin, trimetrexat, azacitidin, bendamustin, altretamin, arsentrioxid, asparaginase (E. coli), aldesleukin, alemtuzumab, levamisol
- Målrettede stoffer og andre: abemaciclib, acalabrutinib, avapritinib, belantamab mafodotin

For oplysninger om advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (evidensniveau L5) uden kliniske forsøg eller litteratur. Der er ikke noget plausibelt mekanistisk grundlag, da filgrastim virker på den granulocytære linje, mens de forudsagte sygdomme skyldes defekter i blodpladernes funktion eller produktion.

**For at komme videre kræves følgende:**
- Gennemgang af produktresuméet for Accofil med henblik på advarsler, kontraindikationer og godkendt indikation (mangler i de nuværende data og blokerer en egentlig sikkerhedsvurdering)
- Data om virkningsmekanismen (MOA) fra DrugBank
- Systematisk litteratur- og forsøgssøgning for at afklare, om der findes præklinisk eller klinisk støtte for en effekt på blodpladefunktion
- Et biologisk rationale for, hvorfor G-CSF-receptorsignalering skulle påvirke blodpladernes sekretion, før der overvejes yderligere undersøgelser
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

