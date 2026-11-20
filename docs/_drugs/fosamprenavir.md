---
layout: default
title: Fosamprenavir
parent: Kun modelforudsigelse (L5)
nav_order: 371
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-17
monitor_inn: "fosamprenavir"
predicted_indications: ["feline acquired immunodeficiency syndrome", "simian immunodeficiency virus infection", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "breast fibrocystic disease", "apocrine adenosis of breast", "blunt duct adenosis of breast", "benign mammary dysplasia"]
description: "Fosamprenavir: forudsagt ny indikation Feline acquired immunodeficiency syndrome (evidensniveau L5). I Danmark, markedsføringstilladelser: 1 (gyldige: 0)"
---

# Fosamprenavir
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **7** stk.
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

## Fosamprenavir: Feline acquired immunodeficiency syndrome
{: .text-alpha }

## Resumé

Fosamprenavir er et prodrug af amprenavir, en HIV-1-proteasehæmmer, der oprindeligt anvendes til behandling af HIV-infektion og AIDS.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **felint erhvervet immundefektsyndrom** (kattens AIDS),
men der er i øjeblikket **ingen registrerede kliniske forsøg** og **ingen publikationer** i de data, der er indsamlet til denne rapport. Forudsigelsen er derfor udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Feline acquired immunodeficiency syndrome |
| TxGNN-forudsigelsesscore | 0.9988 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført (afregistrerede tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 0) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Ifølge afsnittene »Mechanism of Action« og »Microbiology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Fosamprenavir (uofficiel oversættelse): »Fosamprenavir er et antiretroviralt middel mod HIV-1. […] Fosamprenavir er et prodrug, der hurtigt hydrolyseres til amprenavir af cellulære phosphataser i tarmepitelet under absorptionen. Amprenavir er en hæmmer af HIV-1-protease. Amprenavir binder til det aktive site på HIV-1-protease og forhindrer derved processeringen af de virale Gag- og Gag-Pol-polyproteinprækursorer, hvilket resulterer i dannelse af umodne, ikke-infektiøse viruspartikler.« Engelsk originaltekst: "Fosamprenavir is an HIV-1 antiretroviral agent. […] Fosamprenavir is a prodrug that is rapidly hydrolyzed to amprenavir by cellular phosphatases in the gut epithelium as it is absorbed. Amprenavir is an inhibitor of HIV-1 protease. Amprenavir binds to the active site of HIV-1 protease and thereby prevents the processing of viral Gag and Gag-Pol polyprotein precursors, resulting in the formation of immature non-infectious viral particles." ([DailyMed: fosamprenavir calcium prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd1eead-9fc1-426c-bee8-214ffa7d9dc1), version af 2026-06-30; hentet 2026-11-19). Fosamprenavir er dog et prodrug af amprenavir, som hæmmer HIV-1-protease og dermed forhindrer modning af nye viruspartikler. Dets effekt ved HIV-infektion er dokumenteret.

Felint immundefektvirus (FIV) er en lentivirus, der er beslægtet med HIV, og dets protease har en vis strukturel lighed med HIV-1-protease. Der er derfor en plausibel mekanistisk forbindelse. FIV-protease adskiller sig imidlertid fra HIV-1-protease med hensyn til substratspecificitet og følsomhed over for hæmmere, og der foreligger ingen FIV-specifikke data.

Den høje score kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Forudsigelsen bør derfor fortolkes med forsigtighed.

**Øvrige forudsagte indikationer** (alle L5, uden kliniske forsøg eller litteratur, anbefaling: Hold):

| Rang | Sygdom | Score | Kommentar |
|------|------|------|------|
| 2 | Simian immundefektvirus-infektion | 0,9988 | Mekanistisk plausibel (primat-lentivirus), men primært en dyremodel for HIV; værdien er overvejende præklinisk |
| 3 | Neuroudviklingsforstyrrelse med ataktisk gang, manglende tale og nedsat kortikal hvid substans | 0,9986 | Ingen identificeret mekanistisk forbindelse; scoren kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens |
| 4 | Fibrocystisk brystsygdom | 0,9957 | Ingen etableret forbindelse; en godartet tilstand, hvor fosamprenavirs interaktions- og sikkerhedsprofil skal vejes mod en lavrisikoindikation |
| 5 | Apokrin adenose i brystet | 0,9934 | Ingen mekanistisk begrundelse; sandsynligvis drevet af sygdomsontologiens nærhed |
| 6 | Blunt duct-adenose i brystet | 0,9934 | Som ovenfor |
| 7 | Godartet mammadysplasi | 0,9910 | Næsten synonym med fibrocystisk brystsygdom og derfor ikke uafhængig af de øvrige brystdiagnoser |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Oplysninger om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103468703 | Telzir (Viiv Healthcare BV) | Filmovertrukne tabletter | Indikationsteksten er ikke tilgængelig i de indsamlede data |

Administrationsvej: oral.

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er registreret 284 interaktioner i de indsamlede data. Blandt de første 20 er de fleste af moderat sværhedsgrad, fx acarbose, famotidin, ranitidin, rabeprazol, hydrocortison, aprepitant, canagliflozin og dapagliflozin. **Budesonid** er klassificeret som **alvorlig** (Major). Clarithromycin er klassificeret som mindre (Minor). Fosamprenavirs CYP3A4-relaterede interaktioner bør tages i betragtning ved enhver ny anvendelse.
- **Kontraindikationer/forsigtighedsområder fra videnbasen** (ikke fra produktresuméet): Sygdomme, hvor lægemidlet er registreret som kontraindiceret i vidensgrafen, omfatter blandt andet hypertension, leversygdom, galdeblæresygdom, hyperglykæmi, diabetes mellitus, diabetisk ketoacidose, kronisk hepatitis B og C, hypertriglyceridæmi, koronararteriesygdom, myokardieinfarkt, fedme, hæmoglobinopati, nefrolitiasis, akut uratnefropati, hæmolytisk anæmi, hæmofili og lipodystrofi.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på modelscoren (evidensniveau L5), og der findes ingen kliniske forsøg eller litteratur. Den mest plausible forudsigelse (FIV og SIV) vedrører primært dyresygdomme og dyremodeller snarere end en klinisk indikation hos mennesker, og de øvrige forudsigelser savner mekanistisk støtte.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra det danske produktresumé (SmPC) hos Lægemiddelstyrelsen
- Den godkendte indikationstekst for Telzir i Danmark
- Præklinisk evidens for effekt af amprenavir mod FIV- eller SIV-protease
- En vurdering af, om en veterinær anvendelse overhovedet er relevant, da der ikke er human indikation
- En risiko-nytte-vurdering af interaktionsprofilen, hvis de godartede brystindikationer overvejes

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: fosamprenavir calcium prescribing information, Sun Pharmaceutical Industries, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5cd1eead-9fc1-426c-bee8-214ffa7d9dc1) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

