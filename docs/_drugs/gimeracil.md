---
layout: default
title: Gimeracil
parent: Høj evidens (L1-L2)
nav_order: 391
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Gimeracil: forudsagt ny indikation Colonic neoplasm (tyktarmskræft) (evidensniveau L1). Oprindelig indikation: Mavekræft (gastric cancer)"
monitor_inn: "gimeracil"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "lipoma of colon", "cecum neuroendocrine tumor G1", "rectosigmoid junction neoplasm", "colonic lymphangioma", "colon leiomyoma"]
---

# Gimeracil
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

## Gimeracil: Fra mavekræft til tyktarmskræft (colonic neoplasm)
{: .text-alpha }

## Opsummering

Gimeracil er en komponent i kombinationspræparatet S-1 (tegafur/gimeracil/oteracil) og er oprindeligt anvendt til behandling af mavekræft.
TxGNN-modellen forudsiger, at det kan være virksomt mod **colonic neoplasm (tyktarmskræft)**,
og der er i de data, der er indsamlet til denne rapport, identificeret **6 kliniske studier** og **12 publikationer** (primært case reports) inden for denne retning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Mavekræft (gastric cancer) |
| Forudsagt ny indikation | Colonic neoplasm (tyktarmskræft) |
| TxGNN-forudsigelsesscore | 99,88 % |
| Evidensniveau | L1 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er denne forudsigelse rimelig?

Gimeracil er en hæmmer af enzymet DPD (dihydropyrimidindehydrogenase) og en del af S-1-kombinationen (tegafur + gimeracil + oteracil). Ved at hæmme nedbrydningen af 5-FU, som frigives fra tegafur, øger gimeracil den systemiske 5-FU-eksponering. 5-FU er en veletableret antimetabolit ved kolorektal cancer. Detaljerede mekanismedata (MOA) fra DrugBank er ikke tilgængelige i de indsamlede data; ovenstående beskrivelse bygger på den mekanistiske vurdering udarbejdet til denne rapport.

Mavekræft og tyktarmskræft er begge gastrointestinale kræftformer, der kan behandles med fluoropyrimidiner. Mekanismen er derfor direkte relevant for begge sygdomme. Gimeracil er desuden beskrevet at have en radiosensibiliserende effekt via hæmning af homolog rekombinationsreparation, men dette er sekundært her.

**Vigtigt forbehold:** Evidensen vedrører S-1-kombinationen, ikke gimeracil alene. Gimeracil har ingen selvstændig antitumorindikation.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Afsluttet | 1.535 | UFT+leucovorin versus TS-1 (S-1) som adjuverende behandling ved stadie III-tyktarmskræft; undersøger også prædiktive faktorer baseret på genekspression |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Ukendt | 1.191 | SOX (oxaliplatin + S-1) versus XELOX som adjuverende kemoterapi ved stadie III-kolorektalcancer |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Ukendt | 40 | S-1 + bevacizumab ved inoperabel eller recidiverende kolorektalcancer efter tidligere kemoterapi |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Fase 2 | Ukendt | 82 | Raltitrexed + S-1 ved metastatisk kolorektalcancer efter svigt af standardkemoterapi; primært endepunkt er median progressionsfri overlevelse |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Fase 2 | Rekrutterer endnu ikke | 52 | Enkeltarmet studie af fruquintinib + tegafur/gimeracil/oteracil som tredjelinjebehandling ved avanceret metastatisk kolorektalcancer |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Fase 2 | Afsluttet før tid | 20 | Effekt af S-1 og capecitabin med oxaliplatin på koronar blodgennemstrømning (kardiel sikkerhed, ikke effekt) |

Kun ét fase 3-studie (NCT00660894) er afsluttet. Det andet fase 3-studie har ukendt status.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [20841935](https://pubmed.ncbi.nlm.nih.gov/20841935/) | 2010 | Farmakokinetisk studie | Gan to Kagaku Ryoho | Undersøgelse af S-1's anvendelighed ved peritoneale metastaser fra tyktarmskræft i musemodel |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Præklinisk (xenograft) | Oncology Reports | Irinotecan i kombination med S-1 øgede antitumoraktiviteten i 5-FU-resistente tyktarmskræft-xenografter |
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Retrospektiv analyse | Gan to Kagaku Ryoho | Risikofaktorer for alvorlig hæmatologisk toksicitet (grad 3-4: 16,1 %) ved S-1 + irinotecan hos 87 patienter |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case report | Anticancer Research | Komplet respons med S-1 og CPT-11 ved levermetastaser fra tyktarmskræft |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case report/review | J Oncol Pharm Pract | Hypertriglyceridæmi induceret af S-1 |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Case report | Eur J Dermatol | TS-1-induceret erytrodermi med udbredt slimhindeinvolvering og hånd-fod-syndrom |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case report | Gan to Kagaku Ryoho | Totrins-hepatektomi efter SOX + panitumumab ved inoperable levermetastaser |
| [29483452](https://pubmed.ncbi.nlm.nih.gov/29483452/) | 2018 | Case report | Gan to Kagaku Ryoho | Transversumkræft med levermetastaser og portatrombe behandlet effektivt med kemoterapi |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Case report | Gan to Kagaku Ryoho | Gentagne resektioner af peritoneale recidiver efter kolorektalcancer |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Case report | Gan to Kagaku Ryoho | Urinretention som følge af oxaliplatin-induceret akut perifer neuropati efter behandling med tegafur/gimeracil/oteracil |

Der er ingen RCT-publikationer blandt de identificerede artikler; evidensen består hovedsageligt af case reports og prækliniske studier.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104621809 | Teysuno (Nordic Group BV) | Kapsler, hårde | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Konventionelt cytotoksisk (fluoropyrimidin-kombination; gimeracil er selv en DPD-hæmmer, der potenserer 5-FU) |
| Risiko for myelosuppression | Middel (i en retrospektiv analyse af S-1 + irinotecan sås grad 3-4 hæmatologisk toksicitet hos 16,1 %) |
| Emetogenicitetsklassifikation | Lav til moderat (generel vurdering for oral fluoropyrimidin) |
| Monitorering | Fuldt blodbillede med differentialtælling, lever- og nyrefunktion, elektrolytter |
| Håndteringsbeskyttelse | Skal følge gældende regler for håndtering af cytotoksiske lægemidler |

Se produktresuméet (SmPC) for yderligere advarsler og forsigtighedsregler.

---

## Sikkerhedsovervejelser

Der foreligger ingen advarsler, kontraindikationer eller interaktionsdata i de indsamlede data. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Fra litteraturen er følgende bivirkninger ved S-1 rapporteret: hypertriglyceridæmi, erytrodermi med slimhindeinvolvering, hånd-fod-syndrom og hæmatologisk toksicitet (især i kombination med irinotecan).

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Der foreligger et afsluttet fase 3-studie (n=1.535) og et større fase 3-studie med ukendt status, som tester S-1 ved tyktarmskræft, og mekanismen (DPD-hæmning og forstærket 5-FU-eksponering) er direkte relevant. Evidensen gælder dog S-1-kombinationen og ikke gimeracil alene, og litteraturen består hovedsageligt af case reports.

**For at komme videre kræves følgende:**
- Gennemgang af resultaterne fra NCT00660894 og afklaring af status for NCT03448549
- Hentning af produktresumé (SmPC) fra Lægemiddelstyrelsen med advarsler og kontraindikationer samt godkendt indikationstekst for Teysuno
- Data om virkningsmekanisme (MOA) fra DrugBank
- Plan for sikkerhedsmonitorering, herunder DPD-status og hæmatologisk overvågning
- Vurdering af, om en indikationsudvidelse for S-1-kombinationen er relevant i Danmark/EU
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

