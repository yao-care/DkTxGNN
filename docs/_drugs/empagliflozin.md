---
layout: default
title: Empagliflozin
parent: Kun modelforudsigelse (L5)
nav_order: 163
evidence_level: L5
indication_count: 6
---

# Empagliflozin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaceutens vurderingsrapport

</div>

# Empagliflozin: Fra type 2-diabetes til klassisk stiff person-syndrom

## Resumé i én sætning

Empagliflozin er en SGLT2-hæmmer, som i almindelighed anvendes til behandling af type 2-diabetes (indikationsteksten mangler i det danske registerudtræk).
TxGNN-modellen forudsiger, at stoffet kan have effekt på **klassisk stiff person-syndrom**,
men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen. Den er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske registrering (feltet er tomt). Type 2-diabetes er den almindeligt kendte anvendelse for SGLT2-hæmmere |
| Foreslået ny indikation | Klassisk stiff person-syndrom |
| TxGNN-prædiktionsscore | 99,06 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

Pakken indeholder seks prædiktionsrækker, men kun tre unikke sygdomme. Rækkerne for klassisk stiff person-syndrom, fokalt stiff limb-syndrom og opsismodysplasi optræder hver to gange. Alle har evidensniveau L5 og anbefalingen Hold.

| Sygdom | TxGNN-score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Klassisk stiff person-syndrom | 99,06 % | L5 | Hold |
| Fokalt stiff limb-syndrom | 99,06 % | L5 | Hold |
| Opsismodysplasi | 99,03 % | L5 | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ingen detaljerede mekanismedata (MOA) i datagrundlaget. Empagliflozin tilhører klassen af SGLT2-hæmmere, som virker ved at hæmme genoptagelsen af glukose i nyrerne. Mekanistisk er der ikke noget kendt grundlag for, at stoffet virker på stiff person-syndrom.

Stiff person-syndrom er en autoimmun sygdom i det GABAerge nervesystem, ofte med anti-GAD65-antistoffer. SGLT2-hæmning har ingen kendt virkning på denne signalvej. Den høje score på 0,99 afspejler sandsynligvis nærhed i vidensgrafen, for eksempel overlappet mellem GAD65-autoimmunitet og diabetes, og ikke biologisk sandsynlighed.

Det samme gælder fokalt stiff limb-syndrom, som er en lokaliseret variant inden for samme sygdomsspektrum. For opsismodysplasi, en sjælden skeletdysplasi forårsaget af INPPL1 (SHIP2)-mutationer, er der kun en spekulativ, indirekte forbindelse via PI3K/insulinsignalering. Empagliflozin har ingen kendt effekt på skeletudvikling eller SHIP2-funktion.

Alle tre forudsigelser er uverificerede beregningsmæssige resultater.

---

## Klinisk evidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107095624 | Bifoglan (Denk Pharma GmbH & Co KG) | Filmovertrukne tabletter (oral) | Ikke angivet i registerudtrækket |

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller lægemiddelinteraktioner i datagrundlaget (interaktionsforespørgslen gav ingen resultater).
Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modellen (L5), uden kliniske forsøg eller publikationer og uden et kendt mekanistisk link mellem SGLT2-hæmning og de forudsagte sygdomme. Sikkerhedsdata fra den danske produktinformation mangler desuden og er blokerende for det videre arbejde.

**For at komme videre kræves følgende:**
- Hent og gennemgå produktresuméet fra Lægemiddelstyrelsen for advarsler og kontraindikationer (blokerende)
- Indhent mekanismedata (MOA) for empagliflozin, for eksempel fra DrugBank
- Gennemfør en systematisk litteratur- og forsøgssøgning for stiff person-syndrom og SGLT2-hæmmere
- Vurder biologisk plausibilitet (GABAerg/autoimmun signalvej) før yderligere prioritering
- Afklar den godkendte indikation og administrationsvej for præparatet i Danmark

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

