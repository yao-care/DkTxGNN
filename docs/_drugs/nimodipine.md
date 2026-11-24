---
layout: default
title: Nimodipine
parent: Kun modelforudsigelse (L5)
nav_order: 585
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-24
description: "Nimodipine: forudsagt ny indikation Homozygot familiær hyperkolesterolæmi (evidensniveau L5). Oprindelig indikation: Subaraknoidal blødning (aneurysmal subaraknoidal blødning)"
monitor_inn: "nimodipine"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Nimodipine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Nimodipin: Fra subaraknoidal blødning til homozygot familiær hyperkolesterolæmi
{: .text-alpha }

## Resumé i én sætning

Nimodipin er en calciumkanalblokker, der oprindeligt anvendes til behandling af subaraknoidal blødning (aneurysmal). TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **homozygot familiær hyperkolesterolæmi**, men der er **ingen kliniske forsøg** og **ingen publikationer** i de indsamlede data, der understøtter denne retning. Forudsigelsen er udelukkende modelbaseret.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Subaraknoidal blødning (aneurysmal subaraknoidal blødning); der er ikke registreret en godkendt indikationstekst i den danske tilladelse |
| Forudsagt ny indikation | Homozygot familiær hyperkolesterolæmi |
| TxGNN-forudsigelsesscore | 0,9929 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 6 af 6) |
| Antal markedsføringstilladelser | 6 (gyldige: 6) |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse rimelig?

Nimodipin er en dihydropyridin og en blokker af L-type calciumkanaler. Den kendte lægemiddelklasse er derfor lagt til grund. Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Nimodipine (uofficiel oversættelse): »Nimodipin er en calciumkanalblokker af dihydropyridintypen. Glatte muskelcellers kontraktile processer er afhængige af calciumioner, som trænger ind i disse celler under depolarisering som langsomme transmembrane ionstrømme.« Engelsk originaltekst: "Nimodipine is a dihydropyridine calcium channel blocker. The contractile processes of smooth muscle cells are dependent upon calcium ions, which enter these cells during depolarization as slow ionic transmembrane currents." ([DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10), version af 2024-08-30; hentet 2026-11-19).

Homozygot familiær hyperkolesterolæmi skyldes hovedsageligt funktionstabsmutationer i LDLR (sjældnere APOB, PCSK9 eller LDLRAP1), som hæmmer udskillelsen af LDL fra blodet. Calciumkanalblokade adresserer ikke denne defekt. Nogle dihydropyridiner er i prækliniske studier beskrevet med beskedne effekter på vaskulær lipidhåndtering eller aterosklerose, men det er spekulativt og understøttes ikke af nogen data i dette materiale.

Den høje score (0,9929) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, snarere end biologisk evidens. Der er således ikke påvist et direkte mekanistisk led mellem den oprindelige og den nye indikation.

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

## Information om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106465020 | Nimodipin "Paranova" | filmovertrukne tabletter | NIMODIPIN | Gyldig |
| 28101181884 | Nimotop | filmovertrukne tabletter | NIMODIPIN | Gyldig |
| 28105405114 | Nimotop | filmovertrukne tabletter | NIMODIPIN | Gyldig |
| 28106463520 | Nimotop | filmovertrukne tabletter | NIMODIPIN | Gyldig |
| 28101181684 | Nimotop | infusionsvæske, opløsning | NIMODIPIN | Gyldig |

Tabellen viser 5 af 6 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgrafen** (afledt af TxGNN-vidensgrafen, ikke af produktresuméet): leversygdom, galdeblæresygdom og hypotensive tilstande.
- **Lægemiddelinteraktioner**: i alt 162 interaktioner er identificeret. Blandt de viste er to af sværhedsgraden *Major*: **clarithromycin** og **dolasetron**. Blandt de moderate er bl.a. bupropion, aprepitant, morfin, acetylsalicylsyre, cimetidin, miconazol, magnesiumsulfat, canagliflozin, dapagliflozin og empagliflozin samt flere calciumsalte og aminoglykosider (kanamycin, neomycin).
- Nimodipins karudvidende og blodtrykssænkende effekt kan være et særligt sikkerhedsproblem hos patienter med væske- og elektrolytforstyrrelser.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5), uden kliniske forsøg eller litteratur og uden et understøttet mekanistisk led til sygdommens årsag (LDLR-defekt). Samtidig mangler der sikkerhedsdata fra produktresuméet.

**For at komme videre kræves følgende:**
- Gennemgang af produktresuméet for advarsler og kontraindikationer (hentes fra Lægemiddelstyrelsens hjemmeside)
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Prækliniske eller mekanistiske studier, der kan underbygge en effekt på LDL-metabolisme
- Litteratursøgning efter eventuelle kliniske eller observationelle data

---

## Supplerende bemærkning: Forudsagt indikation nr. 2

TxGNN forudsiger også **nefrogent syndrom med uhensigtsmæssig antidiurese (NSIAD)** (score 0,9905, evidensniveau L5, anbefaling: Hold). Sygdommen skyldes aktiverende varianter i AVPR2 med konstitutiv V2-receptoraktivitet. En teoretisk forbindelse via calciumsignalering og aquaporin-2-transport findes, men er spekulativ og uden støtte i forsøg eller litteratur. Nimodipins blodtrykssænkende effekt er desuden en sikkerhedsbekymring hos patienter med væske- og elektrolytforstyrrelser.

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-20 | "Detaljerede data om virkningsmekanisme var ikke tilgængelige i de data, der er indsamlet til denne rapport. Den kendte lægemiddelklasse er derfor lagt til grund" replaced with a sourced mechanism-of-action statement | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde (revideret 2026-11-20; tidligere version gemt i loggen) | [DailyMed: Nymalize (nimodipine) prescribing information, Azurity Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=e660fa26-b5c4-4d6d-8887-9e22b6666a10) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

