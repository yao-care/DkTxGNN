---
layout: default
title: Belimumab
parent: Kun modelforudsigelse (L5)
nav_order: 100
evidence_level: L5
indication_count: 6
monitor_inn: "BELIMUMAB"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "fetal and neonatal alloimmune thrombocytopenia", "severe nonproliferative diabetic retinopathy", "autosomal dominant macrothrombocytopenia"]
last_modified_at: 2026-11-06
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
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 4 af 4) |
| Antal markedsføringstilladelser | 4 (gyldige: 4) |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen (ikke) rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Belimumab (uofficiel oversættelse): »BENLYSTA er en BLyS-specifik hæmmer, der blokerer bindingen af opløseligt BLyS, en overlevelsesfaktor for B-celler, til dets receptorer på B-celler. BENLYSTA binder ikke direkte til B-celler, men ved at binde BLyS hæmmer BENLYSTA overlevelsen af B-celler, herunder autoreaktive B-celler, og reducerer differentieringen af B-celler til immunglobulinproducerende plasmaceller.« Engelsk originaltekst: "BENLYSTA is a BLyS-specific inhibitor that blocks the binding of soluble BLyS, a B-cell survival factor, to its receptors on B cells. BENLYSTA does not bind B cells directly, but by binding BLyS, BENLYSTA inhibits the survival of B cells, including autoreactive B cells, and reduces the differentiation of B cells into immunoglobulin-producing plasma cells." ([DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3), version af 2026-10-30; hentet 2026-11-19). Belimumab er ud fra generel viden et antistof, der neutraliserer BLyS (BAFF), hvilket nedsætter B-cellers overlevelse og produktionen af autoantistoffer. Det er relevant ved autoimmune sygdomme som SLE.

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

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Benlysta (belimumab) prescribing information, GlaxoSmithKline LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2fa3c528-1777-4628-8a55-a69dae2381a3) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

