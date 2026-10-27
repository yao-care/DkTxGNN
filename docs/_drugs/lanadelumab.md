---
layout: default
title: Lanadelumab
parent: Høj evidens (L1-L2)
nav_order: 477
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Lanadelumab: forudsagt ny indikation C1-hæmmermangel (evidensniveau L1). Oprindelig indikation: Arveligt angioødem (HAE)…"
monitor_inn: "Lanadelumab"
predicted_indications: ["C1 inhibitor deficiency", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "serpinopathy with toxic serpin polymerization", "pancreatitis", "pancreatitis", "pseudo-von Willebrand disease", "pseudo-von Willebrand disease", "primary release disorder of platelets", "primary release disorder of platelets"]
---

# Lanadelumab
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
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

## Lanadelumab: Fra arveligt angioødem til C1-hæmmermangel
{: .text-alpha }

## Resumé i én sætning

Lanadelumab er et monoklonalt antistof, der oprindeligt blev udviklet til forebyggelse af anfald af arveligt angioødem (HAE). TxGNN-modellen forudsiger, at det kan være effektivt ved **C1-hæmmermangel**, og forudsigelsen understøttes af **5 kliniske forsøg** og **20 publikationer**. C1-hæmmermangel er dog i praksis den godkendte brug af lægemidlet (HAE med C1-hæmmermangel). Der er derfor tale om en bekræftelse af den eksisterende indikation og ikke en egentlig ny anvendelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Arveligt angioødem (HAE), herunder HAE med C1-hæmmermangel (de danske markedsføringstilladelser indeholder ingen indikationstekst) |
| Forudsagt ny indikation | C1-hæmmermangel |
| TxGNN-forudsigelsesscore | 99,996 % |
| Evidensniveau | L1 |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede mekanismedata (MOA) var ikke tilgængelige i de data, der er indsamlet til denne rapport. Ud fra almen farmakologisk viden er lanadelumab et fuldt humant monoklonalt antistof, der hæmmer plasmakallikrein (kodet af *KLKB1*). Dette stemmer overens med målinformationen i interaktionsdataene, hvor målet er kallikrein B1.

Ved C1-hæmmermangel mister kroppen kontrollen over kallikrein-kinin-systemet. Ukontrolleret kallikreinaktivitet giver øget dannelse af bradykinin, som forårsager de smertefulde og potentielt livstruende hævelsesanfald. Når kallikrein hæmmes direkte, rammes denne mekanisme på et centralt punkt.

Det er vigtigt at bemærke, at HAE med C1-hæmmermangel allerede er en godkendt anvendelse. Forudsigelsen validerer således den kendte brug. Den bør ikke opfattes som et nyt repurposing-fund.

Modellen foreslog også andre sygdomme (serpinopati med toksisk serpinpolymerisering, pankreatitis, pseudo-von Willebrands sygdom og primær frigørelsesforstyrrelse af blodplader). Der er hverken kliniske forsøg eller litteratur for dem, og der er ingen holdbar mekanistisk begrundelse. De høje scorer afspejler sandsynligvis nærhed i netværket til C1-hæmmeren (et serpin) og ikke en terapeutisk begrundelse. De vurderes som **Hold**, og der er ikke indgået yderligere i dem her.

---

## Klinisk evidens fra forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT04583007](https://clinicaltrials.gov/study/NCT04583007) | Ikke angivet | Ikke længere tilgængelig | Ikke angivet | Udvidet adgangsprogram (compassionate use) til forebyggelse af HAE-anfald hos børn på 2 til under 12 år og ved ikke-histaminerg angioødem med normal C1-hæmmer. Giver adgang til behandling, ikke effektdata |
| [NCT05460325](https://clinicaltrials.gov/study/NCT05460325) | Fase 3 | Afsluttet | 20 | Åbent studie af sikkerhed, farmakokinetik og effekt hos kinesiske HAE-patienter over 26 uger |
| [NCT04070326](https://clinicaltrials.gov/study/NCT04070326) (SPRING) | Fase 3 | Afsluttet | 21 | Åbent studie af sikkerhed, farmakokinetik og farmakodynamik hos børn på 2 til under 12 år med HAE |
| [NCT05397431](https://clinicaltrials.gov/study/NCT05397431) | Ikke angivet | Aktiv, rekrutterer ikke | 155 | Japansk sikkerhedsundersøgelse efter markedsføring af TAKHZYRO 300 mg ved langtidsbehandling |
| [NCT04180163](https://clinicaltrials.gov/study/NCT04180163) | Fase 3 | Afsluttet | 12 | Åbent multicenterstudie af effekt og sikkerhed hos japanske patienter med HAE type I eller II |

Det afgørende fase 3-forsøg (HELP, placebokontrolleret) fremgår af litteraturen nedenfor. De registrerede fase 3-forsøg her er åbne og små.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [30480729](https://pubmed.ncbi.nlm.nih.gov/30480729/) | 2018 | RCT | JAMA | Lanadelumab versus placebo til forebyggelse af HAE-anfald (HELP-studiet) |
| [34287942](https://pubmed.ncbi.nlm.nih.gov/34287942/) | 2022 | Åbent forlængelsesstudie | Allergy | Langtidseffekt og -sikkerhed hos patienter ≥12 år med HAE type 1/2 (HELP OLE) |
| [40434599](https://pubmed.ncbi.nlm.nih.gov/40434599/) | 2025 | Netværksmetaanalyse | Drugs in R&D | Indirekte sammenligning af langtidsprofylakse ved HAE (bl.a. garadacimab, lanadelumab, subkutan C1-hæmmer, berotralstat) |
| [40504359](https://pubmed.ncbi.nlm.nih.gov/40504359/) | 2025 | Kohorte (fase 4, real-world) | Advances in Therapy | EMPOWER: vedvarende effekt og sikkerhed op til 36 måneder |
| [39836016](https://pubmed.ncbi.nlm.nih.gov/39836016/) | 2025 | Indirekte sammenligning | J Comp Eff Res | Lanadelumab versus C1-hæmmer hos børn under 12 år med HAE |
| [39508959](https://pubmed.ncbi.nlm.nih.gov/39508959/) | 2024 | Systematisk review | Clin Rev Allergy Immunol | Anfald hos patienter i langtidsprofylakse |
| [31560114](https://pubmed.ncbi.nlm.nih.gov/31560114/) | 2019 | Review | Drugs | Oversigt over lanadelumab ved HAE; signifikant fald i anfaldsrate i HELP |
| [33556593](https://pubmed.ncbi.nlm.nih.gov/33556593/) | 2021 | Case-rapport | J Allergy Clin Immunol Pract | Effekt af lanadelumab ved erhvervet angioødem med C1-hæmmermangel |
| [39399485](https://pubmed.ncbi.nlm.nih.gov/39399485/) | 2024 | Case-rapport | Frontiers in Immunology | Lanadelumab hos en nyretransplanteret patient med HAE og høj kardiovaskulær risiko |
| [41303734](https://pubmed.ncbi.nlm.nih.gov/41303734/) | 2025 | Farmakovigilansanalyse | Medicina | Sammenligning af sikkerhedsprofil for berotralstat og lanadelumab i VigiBase |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106091818 | TAKHZYRO (Takeda Pharmaceuticals International AG Ireland Branch) | Injektionsvæske, opløsning, hætteglas | Indikationstekst er ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er registreret én farmakologisk interaktion, nemlig med målet kallikrein B1 (*KLKB1*). Det er lægemidlets terapeutiske mål og ikke en klinisk interaktion med et andet lægemiddel. Der er ikke angivet noget interaktionsniveau.
- **Koagulationsanalyser:** Lanadelumab påvirker kontaktsystemet/kallikreinsystemet, som kan påvirke visse koagulationsanalyser. Dette er almen farmakologisk viden og ikke fra de indsamlede data.

Advarsler og kontraindikationer var ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Evidensen for lanadelumab ved HAE med C1-hæmmermangel er stærk (L1): et placebokontrolleret RCT (HELP), langtidsforlængelse, real-world-data og flere afsluttede fase 3-studier. Indikationen er allerede godkendt, så beslutningen handler om validering og ikke om ny anvendelse. Sikkerhedsdata fra produktresuméet mangler dog i de indsamlede data.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer), da dette er en blokerende datamangel
- Mekanismedata (MOA) fra DrugBank
- Bekræftelse af den godkendte indikationstekst for den danske tilladelse
- For de øvrige forudsagte sygdomme (serpinopati, pankreatitis, pseudo-von Willebrands sygdom, primær frigørelsesforstyrrelse af blodplader): ingen videre prioritering uden mekanistisk begrundelse og kliniske data
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

