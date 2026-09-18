---
layout: default
title: Vandetanib
parent: Kun modelforudsigelse (L5)
nav_order: 465
evidence_level: L5
indication_count: 10
---

# Vandetanib
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

# Vandetanib: Fra medulær thyroidcancer til nyrecellekarcinoma

## Resumé på én sætning

Vandetanib er en oral multi-kinase-inhibitor (VEGFR2/EGFR/RET) internationalt godkendt til medulær thyroidcancer; der er i øjeblikket ingen dansk markedsføringstilladelse på fil for dette lægemiddel.
TxGNN-modellen forudsiger, at det kan være effektivt til **nyrecellekarcinoma**,
med **4 kliniske forsøg** og **6 publikationer**, der i øjeblikket understøtter denne retning.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke tilgængelig i de danske licensdata; litteraturkontekst (PMID 24451769) angiver, at vandetanib er internationalt godkendt som RET-kinase-inhibitor til medulær thyroidcancer |
| Forudsagt ny indikation | Nyrecellekarcinoma |
| TxGNN forudsigelsesscore | 99.92% |
| Evidensniveau | L2 (1 gennemført randomiseret fase 2-forsøg) |
| Status på dansk marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data for vandetanibs virkningsmekanisme blev ikke returneret af DrugBank i denne evidenspakke (datahul, høj alvorlighed). Baseret på de indsamlede litteraturbevis er vandetanib en multi-mål tyrosinkinase-inhibitor, der virker på VEGFR2, EGFR og RET; en review i evidenssættet (PMID 26677336) grupperer eksplicit vandetanib sammen med sunitinib, sorafenib og pazopanib som anti-angiogenetiske midler, der målretter VEGF-drevet signalering i solide tumorer.

Sunitinib, sorafenib og pazopanib – lægemidler, der deler vandetanibs centrale VEGFR2-inhibitionsmekanisme – er allerede etablerede førsteline-behandlinger for nyrecellekarcinoma, da RCC er en højt vaskulariseret, angiogenese-afhængig tumor. Dette giver en direkte mekanistisk begrundelse for TxGNN-forudsigelsen: en VEGFR2-målrettet agent, der er påvist effektiv i én angiogenese-drevet ondartedelse (thyroidcancer via RET/VEGFR-inhibition), er plausibel i en anden (nyrecellekarcinoma), og flere tidlig-fase forsøg i evidenspakken (VHL-associerede nyretumorer, clear cell-RCC, HLRCC/SDH-associeret nyrekræft) har allerede testet denne hypotese direkte.

---

## Bevis fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Indskrivning | Vigtigste resultater |
|---------|------|------|------|---------|
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Fase 2 | Gennemført | 37 | Testede vandetanib (ZD6474) for anti-angiogenetisk/anti-tumor effekt ved Von Hippel-Lindau-sygdomsassocierede nyretumorer |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Fase 1/2 | Afsluttet | 7 | Vandetanib + metformin-kombination ved HLRCC- eller SDH-associeret nyrekræft og sporadisk papillær RCC |
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Fase 2 | Afsluttet | 3 | Vurderede vandetanib for tumorstørrelsesfald/stabilisering ved avanceret clear cell nyrecellekarcinoma; stoppet tidligt |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Fase 2 (Randomiseret) | Gennemført | 82 | Randomiseret forsøg med carboplatin/gemcitabin ± vandetanib som førsteline-terapi ved cisplatin-uegnet avanceret urotelialkræft/nyrebekkenkræft |

---

## Litteraturbevis

| PMID | År | Type | Journal | Vigtigste resultater |
|------|-----|------|------|---------|
| [36302175](https://pubmed.ncbi.nlm.nih.gov/36302175/) | 2023 | Fase II-forsøg | Clin Cancer Res | Guadecitabin-forsøg ved SDH-deficiente tumorer inklusive HLRCC-associeret nyrecellekarcinoma, en population resistent over for konventionel terapi |
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Review | Clin Exp Metastasis | Diskuterer målrettet terapi-kombinationer for metastatisk fumarathydrolase-deficient RCC, en sjælden, aggressiv subtype uden etableret behandlingsregimen |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Review | OncoTargets Ther | Karakteriserer anti-angiogenetiske TKI'er (sunitinib, sorafenib, pazopanib, vandetanib) godkendt inden for solide tumor-indikationer |
| [28477875](https://pubmed.ncbi.nlm.nih.gov/28477875/) | 2017 | Review | Bull Cancer | Gennemgår cabozantinib virkningsmekanisme/virkning i den bredere sammenhæng af VEGFR/RET-målrettet TKI'er |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Review | ASCO Educational Book | Gennemgår systemisk terapi for avanceret thyroidcancer; noterer vandetanibs FDA-godkendelse som RET-kinase-inhibitor til medulær thyroidcancer |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Præ-klinisk | Mol Cancer Res | Musemodel af TFE3 Xp11.2-translokation RCC identificerer nye terapeutiske mål og en diagnostisk marker (GPNMB) |

---

## Danske markedsoplysninger

Vandetanib har i øjeblikket ingen markedsføringstilladelse på fil hos Lægemiddelstyrelsen – markedsstatus er **Ikke markedsført**, med **0** registrerede tilladelser.

---

## Cytotoxicitet

| Element | Indhold |
|------|------|
| Klassificering af cytotoxicitet | Målrettet terapi (multi-kinase-inhibitor: VEGFR2, EGFR, RET) |
| Risiko for knoglemarvshæmning | Se venligst Produktresuméet (SmPC) advarsler og forholdsregler |
| Klassificering af emetogenicitet | Se venligst Produktresuméet (SmPC) advarsler og forholdsregler |
| Overvågningspunkter | Se venligst Produktresuméet (SmPC) advarsler og forholdsregler |
| Håndteringsbeskyttelse | Som et oralt antineoplastisk middel bør standardiserede institutionelle håndteringsforsigtighedsregler for cytotoksisk/målrettet onkologisk medicin følges i afventning af SmPC-bekræftelse |

---

## Sikkerhedsmæssige overvejelser

Se venligst det godkendte Produktresuméet (SmPC) for sikkerhedsinformationer.

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Begrundelse:**
Mekanistisk begrundelse og tidlig-fase kliniske bevis for nyrecellekarcinoma foreligger, men der eksisterer en blokerende datahul – TFDA/SmPC-advarsler og kontraindikationer er utilgængelige, så kandidaten kan ikke passere indledende sikkerhedsscreening (S1), og vandetanib har ingen markedsføringstilladelse i Danmark.

**For at fortsætte er følgende nødvendigt:**
- SmPC-advarsler, kontraindikationer og lægemiddelinteraktionsdata (i øjeblikket blokerende)
- Bekræftet virkningsmekanisme fra DrugBank
- Dansk/EMA markedsføringstilladelsestatus og eventuelle centraliserede (EMA) licensdetaljer
- Vurdering af en vej til dansk markedsindtræden givet den nuværende status "Ikke markedsført"

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

