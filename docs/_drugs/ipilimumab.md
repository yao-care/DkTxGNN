---
layout: default
title: Ipilimumab
parent: Kun modelforudsigelse (L5)
nav_order: 244
evidence_level: L5
indication_count: 4
---

# Ipilimumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

# Ipilimumab: Fra melanom til choroideremi

## Resumé

Ipilimumab er et CTLA-4-blokerende antistof (immun-checkpoint-hæmmer), som i Danmark markedsføres som Yervoy. I det danske registreringsdata er indikationsteksten tom. Brugen i melanom fremgår dog tydeligt af de tilknyttede studier.
TxGNN-modellen forudsiger, at ipilimumab kan have effekt ved **choroideremi**, en arvelig nethindedegeneration. Der er dog **0 kliniske forsøg** og **0 publikationer**, som understøtter denne retning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske registrering (melanom ifølge de tilknyttede studier) |
| Forudsagt ny indikation | Choroideremi |
| TxGNN-forudsigelsesscore | 99,06 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i datagrundlaget. Ipilimumab er dog et monoklonalt antistof, der blokerer CTLA-4 og dermed forstærker T-cellernes aktivering.

Choroideremi er en X-bundet arvelig nethindedegeneration. Den skyldes tab af CHM-genet (REP1), hvilket forstyrrer Rab-prenylering i nethindens pigmentepitel og i fotoreceptorerne. Intet i de tilgængelige data forbinder T-celle-checkpoint-blokade med denne sygdomsmekanisme.

Der er desuden en sikkerhedsmæssig bekymring. Checkpoint-hæmning kan give immunrelateret øjenbetændelse, for eksempel uveitis, og det vil være problematisk ved en degenerativ nethindesygdom. Den høje score på 0,99 skyldes sandsynligvis en artefakt i vidensgrafen og understøttes ikke af nogen undersøgelse.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104713610 | Yervoy (Bristol-Myers Squibb Pharma EEIG) | Koncentrat til infusionsvæske, opløsning | Indikationstekst ikke angivet i registreringen |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Immunterapi (CTLA-4-hæmmer), ikke konventionelt cytotoksisk |
| Risiko for knoglemarvssuppression | Generelt lav. Se produktresuméet (SmPC) |
| Emetogenicitet | Generelt lav. Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC) for anbefalede kontroller, herunder immunrelaterede bivirkninger |
| Håndteringsbeskyttelse | Følg SmPC og lokale retningslinjer for håndtering af onkologiske lægemidler |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Ved choroideremi er den særlige risiko for immunrelateret øjenbetændelse nævnt ovenfor.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for choroideremi hviler udelukkende på modellen. Der er ingen kliniske forsøg eller publikationer, og der er ingen plausibel mekanistisk forbindelse. Samtidig er der en teoretisk risiko for øjenbetændelse.

**Supplerende bemærkning:** Samme datapakke indeholder også en forudsigelse for **non-kutant melanom** (score 99,02 %). Her er evidensniveauet L3 med anbefalingen "Proceed with Guardrails". Evidensen består af flere randomiserede fase 3-forsøg i melanom generelt, bl.a. NCT00324155 og NCT03068455. De er overvejende udført i kutant melanom og er derfor indirekte i forhold til uveal og mukosal melanom. Denne retning er langt mere lovende og bør vurderes separat.

**For at komme videre kræves:**
- Produktresumé fra Lægemiddelstyrelsen med advarsler og kontraindikationer (blokerende datamangel)
- Mekanismedata (MOA) fra DrugBank
- Præklinisk eller mekanistisk dokumentation for en sammenhæng mellem CTLA-4-blokade og choroideremi, før der overvejes kliniske studier

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelreposition kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

