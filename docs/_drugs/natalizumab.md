---
layout: default
title: Natalizumab
parent: Kun modelforudsigelse (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
---

# Natalizumab
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

# Natalizumab: Fra multipel sklerose til bronkitis

## Resumé i én sætning

Natalizumab er et monoklonalt antistof, som ifølge litteraturen i datapakken anvendes til behandling af multipel sklerose. TxGNN-modellen forudsiger, at det kan være effektivt mod **bronkitis**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne specifikke forudsigelse. Forudsigelsen er derfor udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i datapakken (litteraturen beskriver brug ved multipel sklerose) |
| Forudsagt ny indikation | Bronkitis |
| TxGNN-forudsigelsesscore | 99,46 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede mekanismedata fra DrugBank. Natalizumab blokerer alfa-4-integrin og dermed leukocytternes migration ind i væv. Det er biologisk plausibelt ved inflammatoriske tilstande.

Bronkitis er dog oftest infektiøs eller selvlimiterende. Immunsuppression kan øge risikoen for luftvejsinfektioner, så der er ikke noget underbygget argument for, at natalizumab skulle gavne ved bronkitis. Den høje score afspejler sandsynligvis nærhed i modellens netværk snarere end en dokumenteret terapeutisk effekt.

Pakken indeholder yderligere forudsigelser. Bemærk, at flere indikationer optræder to gange med identiske data:

- **Psoriasis** (score 99,19 %, L4) har den stærkeste evidens. Den er modstridende: flere case-rapporter beskriver natalizumab-induceret eller forværret psoriasis, mens én rapport fra 2021 beskriver bedring hos 18 patienter med både MS og psoriasis.
- **Parapsoriasis** og **akut lichenoid pityriasis** (L4) bygger kun på én case-rapport om bivirkninger, ikke om behandlingseffekt.
- **Svær non-proliferativ diabetisk retinopati** (L5) er kun en modelforudsigelse. Anti-VEGF og laser er standardbehandling.

---

## Klinisk forsøgsevidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret, hverken for bronkitis eller for de øvrige forudsagte indikationer.

---

## Litteraturevidens

For bronkitis foreligger der ingen relateret litteratur.

Til sammenligning er herunder de mest relevante publikationer for den næstplacerede indikation, psoriasis:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [33589543](https://pubmed.ncbi.nlm.nih.gov/33589543/) | 2021 | Observationel/case-serie (design skal verificeres) | Neurol Neuroimmunol Neuroinflamm | Bedring af samtidig psoriasis hos 18 MS-patienter behandlet med natalizumab |
| [40526577](https://pubmed.ncbi.nlm.nih.gov/40526577/) | 2025 | Review | Dtsch Arztebl Int | Behandlingsmuligheder ved MS med samtidige kroniske inflammatoriske sygdomme, bl.a. psoriasis |
| [35646438](https://pubmed.ncbi.nlm.nih.gov/35646438/) | 2022 | Case-rapport | Dermatol Pract Concept | Natalizumab-induceret pustulær psoriasis på håndflader og fodsåler |
| [28905124](https://pubmed.ncbi.nlm.nih.gov/28905124/) | 2018 | Case-rapport + review | Neurol Sci | Artritisk psoriasis under natalizumab-behandling |
| [30323758](https://pubmed.ncbi.nlm.nih.gov/30323758/) | 2018 | Case-rapport + review | Case Rep Neurol | Plaque-psoriasis opstået under natalizumab. Spørgsmålet om induktion eller forværring diskuteres |
| [23096069](https://pubmed.ncbi.nlm.nih.gov/23096069/) | 2012 | Case-rapport | J Neurol | Alvorlig forværring af psoriasis med lægemiddelresistent forløb under natalizumab |
| [28765121](https://pubmed.ncbi.nlm.nih.gov/28765121/) | 2018 | Review | Ann Rheum Dis | Nye behandlinger af immunmedierede inflammatoriske sygdomme, herunder psoriasis |
| [19184539](https://pubmed.ncbi.nlm.nih.gov/19184539/) | 2009 | Review | Immunol Res | Leukocytintegriner og deres terapeutiske potentiale ved bl.a. psoriasis og MS |
| [25448040](https://pubmed.ncbi.nlm.nih.gov/25448040/) | 2015 | Review | Pharmacol Ther | Leukocytintegrinernes rolle i leukocytrekruttering og som terapeutiske mål |
| [15955735](https://pubmed.ncbi.nlm.nih.gov/15955735/) | 2005 | Review | Curr Opin Pharmacol | Anti-adhæsionsterapier rettet mod celleadhæsionsmolekyler |

Evidensen for parapsoriasis og akut lichenoid pityriasis består af én case-rapport: [32470781](https://pubmed.ncbi.nlm.nih.gov/32470781/) (2020, Clin Neurol Neurosurg), som beskriver usædvanlige dermatologiske bivirkninger under fingolimod og natalizumab hos en MS-patient.

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106803822 | Tyruko (Sandoz GmbH) | Koncentrat til infusionsvæske, opløsning | Indikationsteksten er ikke oplyst i datapakken |

---

## Sikkerhedsovervejelser

- **Progressiv multifokal leukoencefalopati (PML):** Flere reviews i datapakken beskriver PML forårsaget af JC-virus som en alvorlig og ofte dødelig komplikation ved natalizumab (fx PMID 19647202, 20298966, 36283150).
- **Hudreaktioner:** Der er rapporteret induceret eller forværret psoriasis (pustulær, artritisk) og andre usædvanlige dermatologiske bivirkninger under natalizumab.
- **Infektionsrisiko:** Immunsuppression kan øge risikoen for luftvejsinfektioner, hvilket er særligt relevant ved bronkitis.

Der er ikke fundet registrerede lægemiddelinteraktioner i datapakken. Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for bronkitis er kun modelbaseret (L5), uden kliniske forsøg eller litteratur, og der er ikke noget plausibelt gavnligt virkningsprincip. Immunsuppression kan tværtimod øge infektionsrisikoen. For psoriasis, den indikation med mest evidens, er signalet modstridende og case-baseret og kræver først en vurdering af sikkerhed og effektretning.

**For at komme videre skal følgende foreligge:**
- Produktresumé fra Lægemiddelstyrelsen med advarsler, kontraindikationer og den godkendte indikation
- Detaljerede mekanismedata (MOA) fra DrugBank
- For psoriasis: verifikation af designet i PMID 33589543 og en struktureret vurdering af, om natalizumab bedrer eller udløser sygdommen, før der overvejes effektstudier
- For bronkitis: præklinisk eller klinisk belæg, før indikationen overvejes igen

*Resultaterne er kun til forskningsbrug og udgør ikke lægefaglig rådgivning. Kandidater til lægemiddelomplacering skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

