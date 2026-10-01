---
layout: default
title: Aflibercept
parent: Kun modelforudsigelse (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Aflibercept
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

# Aflibercept: Fra øjensygdomme (VEGF-hæmmer) til esotropi

## Resumé

Aflibercept er en VEGF-fælde (binder VEGF-A, VEGF-B og PlGF) og kendes fra behandling af øjensygdomme. TxGNN-modellen forudsiger, at det kan virke mod **esotropi** (indadgående skelen), men der findes **ingen kliniske forsøg og ingen publikationer**, der understøtter forudsigelsen. Den vurderes derfor som en ren modelforudsigelse (evidensniveau L5).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Esotropi |
| TxGNN-forudsigelsesscore | 99,38 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Aflibercept blokerer VEGF-A, VEGF-B og PlGF og hæmmer dermed karnydannelse og karlækage. Detaljerede mekanismedata fra DrugBank foreligger ikke i denne evidenspakke.

Esotropi er en neuromuskulær og sensorimotorisk lidelse, hvor øjnene ikke står parallelt. Der er ingen kendt biologisk mekanisme, der forbinder VEGF-blokade med korrektion af øjets stilling. Den høje score (0,994) skyldes sandsynligvis, at modellen har koblet lægemidlet til nærliggende øjensygdomme i vidensgrafen. Intravitreal anti-VEGF-behandling ved præmatur retinopati er desuden beskrevet som muligt forbundet med senere skelen, altså som en mulig bivirkning og ikke som en gavnlig effekt.

### Øvrige forudsagte indikationer (samme evidensniveau L5, alle Hold)

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| Esofagusvaricer uden blødning | 97,56 % | Der er et præklinisk rationale (angiogenese ved portal hypertension), men ingen kliniske data. Systemisk VEGF-blokade indebærer risiko for blødning og GI-perforation. |
| Esofagusvaricer med blødning | 97,56 % | Samme rationale. Aktiv variceblødning er et stærkt sikkerhedsmæssigt modsignal, fordi anti-VEGF-midler har advarsler om blødning. |
| Varicer (åreknuder) | 96,95 % | Sammenhængen med VEGF-fælder er svag og spekulativ. Anti-VEGF kan hæmme sårheling og karintegritet. |
| Urethral sten | 95,97 % | Ingen troværdig mekanisme. Sandsynligvis en artefakt i vidensgrafen. |

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|------|
| 28107330825 | Afiveg | Injektionsvæske, opløsning, hætteglas | STADA Arzneimittel AG |

---

## Sikkerhedsovervejelser

Der er ikke leveret data om advarsler, kontraindikationer eller interaktioner for dette lægemiddel. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Ud fra den mekanistiske vurdering bør man dog være opmærksom på:
- **Blødningsrisiko:** anti-VEGF-midler har advarsler om blødning, hvilket er særligt relevant ved skrøbelige esofagusvaricer.
- **GI-perforation og nedsat sårheling:** risici ved systemisk VEGF-blokade.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden kliniske forsøg eller litteratur. Der er ingen plausibel mekanisme for esotropi, og for flere af de øvrige kandidater (især varicer med blødning) taler sikkerhedsprofilen imod anvendelse.

**For at komme videre kræves:**
- Sikkerhedsoplysninger fra Lægemiddelstyrelsens produktresumé (advarsler og kontraindikationer)
- Data om virkningsmekanisme fra DrugBank
- Prækliniske eller kliniske studier, der understøtter mindst én af de forudsagte indikationer
- Vurdering af administrationsvej: Afiveg er en intravitreal injektionsvæske, og det er uafklaret, om den er forenelig med de forudsagte indikationer

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelserne skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

