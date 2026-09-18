---
layout: default
title: Pitolisant
parent: Moderat evidens (L3-L4)
nav_order: 353
evidence_level: L4
indication_count: 6
---

# Pitolisant
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **6** stk.
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

# Pitolisant: Fra narkolepsi til søvnløshed

## Sammenfatning i en sætning

> Pitolisant er en selektiv histamin H3-receptorinvers agonist/antagonist, bedst dokumenteret i litteraturen for behandling af overdreven dagssomnolens ved **narkolepsi** og resterende somnolens ved obstruktiv søvnapnø (OSA).
> TxGNN-modellen forudsiger, at det kan være effektivt mod **søvnløshed**, men dette understøttes kun af **1 urelativ, tilbagetrukket klinisk forsøg** og **8 publikationer**, hvoraf ingen specifikt studerede søvnløshed.
> Lægemidlets farmakologiske virkning er opvækkende, hvilket er mekanistisk modsat det, som en søvnløshedsbehandling kræver — denne forudsigelse bør betragtes som en kandidat til gennemgang, ikke som et valideret omformål-signal.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Narkolepsi med eller uden katapleksi (ifølge litteraturevidence; ingen dansk licenserings-post til bekræftelse tilgængelig) |
| Forudsagt ny indikation | Søvnløshed (sygdom) |
| TxGNN-forudsigelsesscore | 99.71% |
| Evidensniveau | L4 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Påhold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i det strukturerede DrugBank-felt for denne evidenspakke. Baseret på den understøttende litteratur er pitolisant kendt som et first-in-class, selektivt histamin H3-receptorinvers agonist/antagonist. Ved at blokere præsynaptiske H3-autoreceptorer øger det histaminudskillelsen (og nedstrøms dopamin/acetylcholin-signalering) i hjernen og producerer en **opvækkende** effekt. Denne mekanisme ligger til grund for dets etablerede brug til overdreven dagssomnolens ved narkolepsi og, i forsøgsindstillinger, til resterende somnolens hos OSA-patienter på CPAP.

Dette er præcis hvorfor TxGNN-forudsigelsen for **søvnløshed** bør behandles med forsigtighed snarere end taget for pålydende. Søvnløshedsbehandling kræver en **sedativ/hypnotisk** effekt, hvorimod pitolisants dokumenterede farmakologi virker i den modsatte retning (opvækkende). Selve evidenspakken markerer dette som en sandsynlig ontologi-mapping-artefakt: noden "søvnløshed (sygdom)" i den underliggende videngraf kan være for bred og kunne være ved at fange søvnforstyrrelses-forhold generelt (herunder narkolepsi/EDS) snarere end et specifikt søvnløsheds-signal. Ingen af de 8 understøttende publikationer studerede søvnløshed som et endpoint — de dækker narkolepsi, OSA-relateret somnolens og generel H3-receptorfarmakologi.

Givet denne mekanistiske modsætning kan forudsigelsen for øjeblikket ikke fortolkes som klinisk rimelig uden manuel gennemgang af, hvordan sygdomsnoden blev afbildet. Det bør ikke fremmes på baggrund af TxGNN-scoren alene.

---

## Klinisk forsøgsevidence

| Forsøgsnummer | Fase | Status | Tilmelding | Vigtige fund |
|---------|------|------|------|---------|
| [NCT02800083](https://clinicaltrials.gov/study/NCT02800083) | Fase 2 | Tilbagetrukket | 0 | Forsøget var designet til at evaluere pitolisant til **alkoholmisbrug**, ikke søvnløshed (titel afkortet i kildedata som "For A..."). Tilbagetrukket med nul tilmelding — ingen kliniske data blev genereret. Klassificeret "C" relevans: understøtter ikke søvnløshedsindikationen. |

*Intet klinisk forsøg i denne evidenspakke evaluerede direkte pitolisant til søvnløshed.*

---

## Litteraturevidence

| PMID | År | Type | Tidsskrift | Vigtige fund |
|------|-----|------|------|---------|
| [36931805](https://pubmed.ncbi.nlm.nih.gov/36931805/) | 2023 | RCT | The Lancet. Neurology | Fase 3 RCT bekræftende sikkerhed/effektivitet af pitolisant hos børn ≥6 år med narkolepsi med/uden katapleksi — ikke et søvnløsheds-studie. |
| [33121980](https://pubmed.ncbi.nlm.nih.gov/33121980/) | 2021 | RCT | Chest | RCT af pitolisant til resterende overdreven dagssomnolens hos OSA-patienter på CPAP — opvækkende effekt, modsat retning til søvnløshedsbehandling. |
| [31917607](https://pubmed.ncbi.nlm.nih.gov/31917607/) | 2020 | RCT | Am J Respir Crit Care Med | RCT af pitolisant til dagssomnolens hos OSA-patienter, der afviser CPAP — igen en opvækkende indikation. |
| [36169322](https://pubmed.ncbi.nlm.nih.gov/36169322/) | 2022 | Kohorte | Revista de neurología | Real-life kohorte (WAKE-studie) af pitolisant i behandlingsresistent type 1 narkolepsi med katapleksi. |
| [34521328](https://pubmed.ncbi.nlm.nih.gov/34521328/) | 2022 | Oversigt | Current Neuropharmacology | Oversigt over histaminerg-systemændringer i neuropsykiatriske lidelser; bemærker at pitolisant bruges til narkolepsi-somnolens, i modsætning til H1-antagonister (f.eks. doxepin) brugt til søvnløshed. |
| [34225942](https://pubmed.ncbi.nlm.nih.gov/34225942/) | 2021 | Oversigt | Handbook of Clinical Neurology | Generel oversigt over histamin-receptorfarmakologi (H1–H4); baggrund mekanisme-reference kun. |
| [30214155](https://pubmed.ncbi.nlm.nih.gov/30214155/) | 2018 | Oversigt | Drug Design, Development and Therapy | Profil af pitolisants udvikling og terapeutisk rolle, bekræftende at dets godkendte brug er narkolepsi, ikke søvnløshed. |
| [22356925](https://pubmed.ncbi.nlm.nih.gov/22356925/) | 2012 | Oversigt | Clinical Neuropharmacology | Tidlig oversigt, der beskriver pitolisant som et stimulans til narkolepsi-katapleksi hos teenagere med refraktær somnolens. |

*Ingen af ovenstående litteratur studerede pitolisant specifikt til søvnløshed; alle direkte relevante kliniske studier vedrører narkolepsi eller OSA-relateret overdreven dagssomnolens — den modsatte kliniske retning.*

---

## Markedsinformation om Danmark

Pitolisant har for øjeblikket **ingen markedsføringstilladelse i Danmark** (markedsstatus: Ikke markedsført; 0 tilladelser på rekord). Ingen produkt-, dosisform- eller godkendt-indikations-data er tilgængelig fra danske kilder i denne evidenspakke.

---

## Sikkerhedshensyn

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformation. Ingen strukturerede advarsler, kontraindikationer eller lægemiddelinteraktions-data var tilgængelig i denne evidenspakke (DDI-forespørgsel returnerede ingen resultater).

---

## Konklusion og næste trin

**Beslutning: Påhold**

**Begrundelse:**
- Den forudsagte indikation (søvnløshed) strider mekanistisk mod pitolisants kendte opvækkende farmakologi, og intet klinisk forsøg eller publikation i evidenspakken studerede faktisk søvnløshed som et endpoint. Det enkelte tilknyttede forsøg (NCT02800083) havde fokus på alkoholmisbrug og blev tilbagetrukket uden tilmelding. Dette mønster er i overensstemmelse med en for bred sygdom-node-afbildning i den underliggende videngraf snarere end et ægte omformål-signal.

**For at fortsætte er følgende nødvendigt:**
- Manuel gennemgang/kuratoring af den "søvnløshed (sygdom)" node-afbildning, som TxGNN-modellen bruger, for at bekræfte, om den utilsigtet aggregerer narkolepsi/EDS-relaterede forhold
- Bekræftet virkningsmekanisme (MOA) dokumentation fra DrugBank eller SmPC'en, snarere end at stole udelukkende på litteraturinferens
- Dansk/EU-licenserings- og SmPC-data (advarsler, kontraindikationer, interaktioner), da pitolisant for øjeblikket ikke er markedsført i Danmark
- Hvis den mekanistiske konflikt ikke kan løses, bør denne kandidat deprioriteres til fordel for det mindre sikre, men mekanistisk plausible ADHD-signal (TxGNN-score 99.36%), som for øjeblikket kun understøttes af præklinisk/mekanistisk litteratur og berettiger til en Forskningsspørgsmål-fase snarere end yderligere søvnløshed-fokuseret gennemgang

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

