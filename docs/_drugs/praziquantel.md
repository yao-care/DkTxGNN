---
layout: default
title: Praziquantel
parent: Kun modelforudsigelse (L5)
nav_order: 357
evidence_level: L5
indication_count: 10
---

# Praziquantel
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

# Praziquantel: Fra schistosomiasis til epithelioid leiomyosarkom i corpus uteri

## Sammenfatning i en sætning

Praziquantel er et klassisk antiparasitært middel, der bruges til behandling af schistosomiasis og andre trematode-/cestode-infektioner (leverflynke- og bændelorminfektioner). TxGNN-modellens højest rangerede prognose peger på **epithelioid leiomyosarkom i corpus uteri**, men dette signal er i øjeblikket understøttet af **0 kliniske forsøg** og **0 publikationer** uden etableret mekanistisk begrundelse.

## Hurtigt overblik

| Punkt | Indhold |
|------|---------|
| Original indikation | Schistosomiasis og andre trematode-/cestode-infektioner (parasitære orminfektioner) |
| Forventet ny indikation | Epithelioid leiomyosarkom i corpus uteri |
| TxGNN-prognosescore | 97.28% |
| Bevisniveau | L5 |
| Markedsstatus for Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

## Hvorfor er denne prognose rimelig?

Detaljerede data om virkningsmekanisme for praziquantel er en dokumenteret datakløft i denne bevissamling. Baseret på etableret farmakologi øger praziquantel permeabiliteten for calcium-ioner gennem tegumentet og muskulaturen i flatorme (leverflynke og bændelorme), hvilket forårsager spastisk lammelse og tegmental forstyrrelse, der eksponerer parasitten for værtsimmunforsvar. Denne mekanisme er specifik for flatormenes neuromuskulære/tegmentale biologi.

Der er ingen kendt mekanistisk overlapning mellem denne platyelmint-specifikke calcium-kanal/tegument-effekt og de patogene veje involveret i leiomyosarkom i corpus uteri (f.eks. TP53, RB1-mutation, MDM2-vejdysregulering). Omformål-begrundelsen for denne kandidat angiver eksplicit, at ingen plausibel biologisk hypotese kunne opstilles.

Det er vigtigt, at TxGNN-scoren på 97.28% ikke understøttes af nogen klinisk forsøgs- eller litteraturbevis for denne specifikke indikation (0/0). Dette hul mellem en høj modelscore og en fuldstændig mangel på støttende bevis tyder på, at scoren sandsynligvis afspejler vidensgrafs topologi (f.eks. indirekte nodeproximitet) snarere end et valideret farmakologisk signal — konsistent med dets L5-bevisklassificering og Afvent-anbefaling.

*Bemærk: blandt denne medicins 10 modelrangerede kandidater er Plasmodium falciparum-malaria (plads 3, score 97.22%) et separat signal, der faktisk understøttes af kliniske forsøgs- og litteraturdata (L3, "Forskningstspørgsmål"-stadium) — se Konklusion for en note om denne alternative kandidat.*

## Evidens fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

## Markedsinformation for Danmark

Praziquantel har i øjeblikket ingen markedsføringstilladelse i Danmark (0 licenser på rekord; markedsstatus: ikke markedsført).

## Sikkerhedsovervejelser

Se venligst i det godkendte produktresumé (SmPC) for sikkerhedsinformation.

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Den højest rangerede prognose (epithelioid leiomyosarkom i corpus uteri) understøttes kun af en TxGNN-modelscore, uden kliniske forsøg, uden litteratur og uden plausibel mekanistisk hypotese (L5). Medicinen er heller ikke i øjeblikket markedsført i Danmark og mangler de grundlæggende virkningsmekanisme- og SmPC-sikkerhedsdata, der er nødvendige for at påbegynde en formel sikkerhedsgennemgang.

**For at fortsætte er følgende nødvendigt:**
- Data om virkningsmekanisme via DrugBank API (datakløft DG002, høj prioritet)
- SmPC-advarsler/kontraindikationer fra den ansvarlige regulatoriske kilde (datakløft DG001, blokering)
- Prækliniske/mekanistiske studier, der udforsker enhver plausibel aktivitet mod leiomyosarkom i corpus uteri, før yderligere bevisindsamling er berettiget
- Hvis man forfølger antiparasitære omformål-signaler for denne medicin, skal man separat evaluere Plasmodium falciparum-malaria-kandidaten (plads 3, L3, "Forskningstspørgsmål"-stadium), som har faktiske støttende forsøgs- og litteraturdata i modsætning til den nuværende højest rangerede kandidat

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

