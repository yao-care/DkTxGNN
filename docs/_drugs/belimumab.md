---
layout: default
title: Belimumab
parent: Kun modelforudsigelse (L5)
nav_order: 100
evidence_level: L5
indication_count: 6
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-10-28
description: "Belimumab: forudsagt ny indikation Primær frigivelsesforstyrrelse af blodplader (evidensniveau L5). Oprindelig indikation: Systemisk lupus erythematosus og pædiatrisk SLE"
---

# Belimumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
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

## Belimumab: Fra systemisk lupus erythematosus til primær frigivelsesforstyrrelse af blodplader
{: .text-alpha }

## Resumé i én sætning

Belimumab er et monoklonalt antistof, der er registreret i vidensgrafen for systemisk lupus erythematosus (SLE) og pædiatrisk SLE.
TxGNN-modellen forudsiger, at det kan have effekt ved **primær frigivelsesforstyrrelse af blodplader**.
Der er dog **0 kliniske forsøg** og **0 publikationer** i de indsamlede data, så forudsigelsen er udelukkende beregningsbaseret.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Systemisk lupus erythematosus og pædiatrisk SLE (relation registreret i vidensgrafen; Lægemiddelstyrelsens godkendelsesdata indeholder ingen indikationstekst) |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN-forudsigelsesscore | 0,9996 |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen (ikke) rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i det sammenstillede datagrundlag. Belimumab er ud fra generel viden et antistof, der neutraliserer BLyS (BAFF), hvilket nedsætter B-cellers overlevelse og produktionen af autoantistoffer. Det er relevant ved autoimmune sygdomme som SLE.

Primære frigivelsesforstyrrelser af blodplader er typisk arvelige eller erhvervede kvalitative defekter i trombocytfunktionen og er ikke primært drevet af B-celler eller autoantistoffer. Der er derfor ikke identificeret en plausibel mekanistisk sammenhæng. Den høje score (0,9996) er alene en computerbaseret forudsigelse og understøttes ikke af kliniske data eller litteratur.

### Øvrige forudsigelser i samme analyse

| Forudsagt indikation | TxGNN-score | Evidensniveau | Vurdering |
|------|------|------|------|
| Pseudo-von Willebrands sygdom | 0,9996 | L5 | Genetisk defekt i trombocytreceptoren GP1BA, ikke immunmedieret; ingen rationale for BAFF-blokade |
| Glanzmanns trombasteni | 0,9988 | L5 | Arvelig defekt i integrin αIIbβ3; kun en spekulativ, indirekte relevans ved alloantistoffer efter trombocyttransfusion |
| Føtal og neonatal alloimmun trombocytopeni (FNAIT) | 0,9959 | L5 | Mekanistisk mest sammenhængende (maternelle alloantistoffer), men belimumab nedsætter ikke hurtigt etableret IgG, og graviditetsdata er begrænsede |
| Svær ikke-proliferativ diabetisk retinopati | 0,9905 | L5 | Primært mikrovaskulær/VEGF-drevet; ingen etableret rolle for BAFF |
| Autosomal dominant makrotrombocytopeni | 0,9904 | L5 | Arvelig defekt i megakaryocytter/trombocytter; ingen mekanistisk rationale |

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105851916 | Benlysta (GlaxoSmithKline (Ireland) Limited) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Indikationstekst er ikke angivet i de tilgængelige data |

Listen kan være ufuldstændig med hensyn til indikationstekst, men antallet af tilladelser er fuldstændigt (1).

## Sikkerhedsovervejelser

Lægemidlets produktresumé indeholder oplysninger om advarsler og kontraindikationer, men disse indgår ikke i det sammenstillede datagrundlag. Se det godkendte produktresumé (SPC) for sikkerhedsoplysninger.

**Lægemiddelinteraktioner:** Der er fundet 69 potentielle interaktioner. Eksempler:
- **Alvorlige (Major):** adalimumab, baricitinib, certolizumab pegol, levende BCG-vaccine (Tice-stammen)
- **Moderate:** azathioprin, anakinra, alemtuzumab, alefacept, canakinumab, roflumilast, tetanustoksoid samt flere levende eller andre vacciner
- **Mindre (Minor):** zinksalte (acetat, gluconat, sulfat, chlorid)

Generelt er kombination med andre immunsupprimerende biologiske lægemidler og levende vacciner væsentlig at vurdere.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Alle forudsigelser er på evidensniveau L5: der findes ingen kliniske forsøg eller publikationer, der undersøger sygdommen direkte, og for den højest rangerede indikation er der ingen plausibel mekanistisk sammenhæng med BAFF-hæmning.

**For at komme videre er følgende nødvendigt:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet (blokerende datahul for sikkerhedsscreening)
- Prækliniske eller kliniske studier, der direkte undersøger belimumab ved den forudsagte sygdom
- Hvis én forudsigelse skal prioriteres til yderligere vurdering, er FNAIT den mekanistisk mest sammenhængende, men kræver først en grundig vurdering af graviditetssikkerhed
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

