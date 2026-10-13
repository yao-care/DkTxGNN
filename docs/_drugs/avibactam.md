---
layout: default
title: Avibactam
parent: Kun modelforudsigelse (L5)
nav_order: 90
evidence_level: L5
indication_count: 6
---

# Avibactam
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

# Avibactam: Fra pyelonefritis til streptokok-pneumoni

## Resumé i én sætning

Avibactam er en beta-lactamasehæmmer, som oprindeligt anvendes sammen med et beta-lactam-antibiotikum til behandling af pyelonefritis (nyrebækkenbetændelse). TxGNN-modellen forudsiger, at stoffet kan have effekt ved **streptokok-pneumoni**, men der er i de data, der er indsamlet til denne rapport, **ingen kliniske forsøg** og **ingen publikationer**, som understøtter forudsigelsen. Forudsigelsen er derfor udelukkende modelbaseret og vurderes som mekanistisk usandsynlig.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Pyelonefritis (fra vidensgrafen; produkternes godkendte indikationstekst er ikke tilgængelig) |
| Forudsagt ny indikation | Streptokok-pneumoni |
| TxGNN-forudsigelsesscore | 99,70 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 2 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger i øjeblikket ikke detaljerede data om virkningsmekanismen i de indsamlede data. Avibactam er kendt som en ikke-beta-lactam beta-lactamasehæmmer, der dækker Ambler-klasse A, C og nogle D-enzymer. Stoffet har ingen egen antibakteriel aktivitet og markedsføres kun i kombination med beta-lactamer, f.eks. ceftazidim-avibactam.

*Streptococcus pneumoniae* udvikler primært beta-lactamresistens gennem ændrede penicillinbindende proteiner og ikke gennem beta-lactamaser. En beta-lactamasehæmmer forventes derfor ikke at give merværdi. Den høje score skyldes sandsynligvis, at antibakterielle lægemidler ligger tæt på luftvejsinfektioner i vidensgrafen, snarere end en reel mekanistisk sammenhæng.

**Andre forudsagte indikationer (alle L5, anbefaling Hold):**

| Forudsagt indikation | Score | Vurdering af mekanistisk sammenhæng |
|------|------|------|
| Svær influenza (modtagelighed) | 99,28 % | Ingen plausibel antiviral mekanisme. Sandsynligvis et artefakt i vidensgrafen. Kan kun have relevans ved sekundær bakteriel lungebetændelse, hvilket er en anvendelse af kombinationspartneren. |
| Uretertuberkulose | 99,11 % | Delvis indirekte rationale: *M. tuberculosis* producerer beta-lactamasen BlaC, og avibactam har in vitro hæmmet BlaC og styrket nogle beta-lactamer (f.eks. carbapenemer). Evidensen er prækliniske data for generel/pulmonal tuberkulose, ikke for urogenital tuberkulose. |
| Urinær schistosomiasis | 99,06 % | Ingen kendt antiparasitær aktivitet. Scoren skyldes sandsynligvis det fælles urinvejsområde med pyelonefritis. |
| Polyklonalt hyperviskositetssyndrom | 99,01 % | Ingen identificerbar mekanistisk forbindelse. Sandsynligvis modelartefakt. |
| Hyperamylasæmi | 99,01 % | Laboratoriefund, ikke en sygdom, som avibactam behandler. Kan afspejle bivirknings-/laboratorieassociationer. |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der foreligger i øjeblikket ingen relateret litteratur.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105600015 | Zavicefta (Pfizer Ireland Pharmaceuticals) | Pulver til koncentrat til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig |
| 28107028323 | Emblaveo (Pfizer Europe MA EEIG) | Pulver til koncentrat til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig |

Begge tilladelser er gyldige, og begge produkter indgives som intravenøs infusion.

---

## Sikkerhedsovervejelser

Der foreligger ingen sikkerhedsdata i de indsamlede data, og der blev ikke fundet registrerede lægemiddelinteraktioner. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden kliniske forsøg eller publikationer (L5). Mekanismen taler desuden imod effekt, fordi pneumokokresistens over for beta-lactamer ikke skyldes beta-lactamaser, og avibactam har ingen egen antibakteriel aktivitet.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen (mangler og blokerer sikkerhedsscreeningen)
- Prækliniske eller kliniske data, der understøtter en anvendelse ved den forudsagte indikation
- Hvis man ønsker at forfølge en af de forudsagte indikationer, er uretertuberkulose den eneste med et indirekte biologisk rationale (hæmning af BlaC), men kun som kombinationsstrategi og med prækliniske data
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

