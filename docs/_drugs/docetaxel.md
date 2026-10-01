---
layout: default
title: Docetaxel
parent: Kun modelforudsigelse (L5)
nav_order: 146
evidence_level: L5
indication_count: 10
---

# Docetaxel
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

# Docetaxel: Fra en ikke oplyst oprindelig indikation til brystkræft hos kvinder

## Resumé

Docetaxel er et cytostatikum (taxan), som er markedsført i Danmark som infusionskoncentrat. Evidence Pack'en oplyser ikke den oprindelige godkendte indikation.
TxGNN-modellen forudsiger, at lægemidlet kan være effektivt ved **brystkræft hos kvinder (female breast carcinoma)**. Forudsigelsen understøttes af **mere end 40 identificerede kliniske forsøg** (heraf flere afsluttede fase 3-forsøg) og **20 publikationer**.
Brystkræft er en veletableret anvendelse af docetaxel, så forudsigelsen er mere en bekræftelse end egentlig drug repurposing.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Female breast carcinoma (brystkræft hos kvinder) |
| TxGNN-forudsigelsesscore | 99,90 % |
| Evidensniveau | L1 (flere afsluttede fase 3-RCT'er) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede mekanismedata fra DrugBank er ikke tilgængelige. Ifølge evidensanalysen stabiliserer docetaxel mikrotubuli ved at binde sig til beta-tubulin. Det giver mitotisk standsning og apoptose i hurtigt delende tumorceller.

Mekanismen er velkendt og biologisk plausibel ved brystkræft. Mange af de identificerede studier bruger docetaxel som en del af adjuverende, neoadjuverende eller metastatisk kemoterapi, ofte sammen med anthracykliner, cyclophosphamid, trastuzumab eller bevacizumab. Evidens for brystkræft er derfor omfattende.

Evidens fra kombinationsregimer kan ikke altid tilskrive effekten til docetaxel alene. Det gælder især de studier, hvor docetaxels rolle ikke fremgår af titlen.

---

## Kliniske forsøg

Tabellen viser de 10 mest relevante forsøg. Der er ikke fundet EudraCT-numre i datagrundlaget.

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT00054587](https://clinicaltrials.gov/study/NCT00054587) | Fase 3 | Afsluttet | 3010 | Docetaxel + epirubicin vs. FEC 100 ved brystkræft med positive lymfeknuder, med sekventiel tilføjelse af trastuzumab ved HER2-positiv sygdom |
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Fase 3 | Afsluttet | 736 | Dobbeltblindet: bevacizumab + docetaxel vs. docetaxel + placebo som førstelinjebehandling ved HER2-negativ metastatisk brystkræft |
| [NCT00887536](https://clinicaltrials.gov/study/NCT00887536) | Fase 3 | Afsluttet | 1613 | TC + bevacizumab vs. TC alene vs. TAC ved HER2-negativ brystkræft med positive eller højrisiko-negative lymfeknuder |
| [NCT00047099](https://clinicaltrials.gov/study/NCT00047099) | Fase 3 | Afsluttet | 446 | FEC vs. EC-Doc (efterfulgt af docetaxel) ved primær brystkræft |
| [NCT00004125](https://clinicaltrials.gov/study/NCT00004125) | Fase 3 | Afsluttet | Ikke oplyst | AC efterfulgt af paclitaxel eller docetaxel ugentligt vs. hver 3. uge ved brystkræft med lymfeknudemetastaser |
| [NCT01354522](https://clinicaltrials.gov/study/NCT01354522) | Fase 3 | Afsluttet | 204 | TAC vs. TCX (docetaxel, cyclophosphamid, capecitabin) som adjuverende behandling ved højrisiko HER2-negativ brystkræft |
| [NCT00321633](https://clinicaltrials.gov/study/NCT00321633) | Fase 2 | Afsluttet | 148 | Randomiseret: carboplatin vs. docetaxel ved metastatisk genetisk (BRCA) brystkræft |
| [NCT00217672](https://clinicaltrials.gov/study/NCT00217672) | Fase 2 | Afsluttet | 76 | Docetaxel med eller uden bevacizumab som førstelinjebehandling ved HER2-negativ metastatisk brystkræft |
| [NCT02748213](https://clinicaltrials.gov/study/NCT02748213) | Fase 2 | Afsluttet | 225 | Trastuzumab + docetaxel med eller uden capecitabin ved HER2-positiv avanceret brystkræft |
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Fase 2 | Ukendt | 42 | Docetaxel + ifosfamid som førstelinjebehandling ved metastatisk brystkræft (lille, enkeltarmet) |

---

## Litteratur

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC-forsøgene: randomiseret sammenligning af docetaxel + cyclophosphamid (TC6) med standard TaxAC-regimer (herunder TAC6) ved tidlig brystkræft |
| [11481357](https://pubmed.ncbi.nlm.nih.gov/11481357/) | 2001 | Randomiseret fase IIb | J Clin Oncol | Dosis-tæt doxorubicin + docetaxel med G-CSF, med eller uden tamoxifen, som præoperativ behandling |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Kohorte | Breast Cancer | Docetaxel, cyclophosphamid og trastuzumab som neoadjuverende behandling ved HER2-positiv brystkræft |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Fase 2 | Cancer | Capecitabin + docetaxel + epirubicin som førstelinjebehandling ved avanceret brystkræft |
| [16020974](https://pubmed.ncbi.nlm.nih.gov/16020974/) | 2005 | Fase 2 | Oncology | Ugentligt docetaxel + gemcitabin som førstelinjebehandling ved metastatisk brystkræft |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Fase 2 | Clin Breast Cancer | Docetaxel/cisplatin som primær kemoterapi ved lokalt fremskreden brystkræft |
| [12714881](https://pubmed.ncbi.nlm.nih.gov/12714881/) | 2003 | Fase 2 | Am J Clin Oncol | Docetaxel + vinorelbin hver 14. dag ved anthracyclinresistent metastatisk brystkræft (n = 49) |
| [15858439](https://pubmed.ncbi.nlm.nih.gov/15858439/) | 2005 | Fase 2 (interimanalyse) | Breast Cancer | CEF efterfulgt af docetaxel som neoadjuverende behandling ved tidlig brystkræft (79 patienter) |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Kohorte (retrospektiv) | Anti-Cancer Drugs | Sammenhæng mellem adjuverende docetaxelbaseret kemoterapi og brystkræftrelateret lymfødem |
| [15074734](https://pubmed.ncbi.nlm.nih.gov/15074734/) | 2004 | Erfaringsstudie | Clin Oncol | Trastuzumab + docetaxel ved HER2-overudtrykkende metastatisk brystkræft: toksicitet og effekt |

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28105087411 | Docetaxel "Accord" | Koncentrat til infusionsvæske, opløsning | Accord Healthcare S.L.U. |

Teksten om godkendte indikationer er ikke tilgængelig i datagrundlaget.

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksisk klassifikation | Konventionelt cytostatikum (taxan, mikrotubulistabiliserende) |
| Risiko for knoglemarvssuppression | Høj (neutropeni er den primære toksicitet) |
| Emetogenicitetsklasse | Lav til moderat |
| Monitorering | Fuldt blodbillede med differentialtælling, lever- og nyrefunktion, væskeretention/ødem og perifer neuropati |
| Håndtering og beskyttelse | Kræver særlige forholdsregler i henhold til gældende regler for håndtering af cytotoksiske lægemidler |

Der er ikke tilgængelige toksicitetsdata fra DrugBank. Se produktresuméet (SmPC) for advarsler og forsigtighedsregler.

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Flere afsluttede, randomiserede fase 3-forsøg med docetaxelholdige regimer understøtter brug ved brystkræft, og mekanismen er veletableret. Brystkræft er en kendt anvendelse, så forudsigelsen bekræfter eksisterende praksis. Sikkerhedsdata fra Lægemiddelstyrelsen mangler imidlertid, og der skal derfor tages forbehold.

**For at komme videre skal følgende på plads:**
- Hent og gennemgå produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer, interaktioner). Dette er en blokerende datamangel.
- Hent mekanismedata (MOA) fra DrugBank.
- Bekræft de godkendte indikationer for Docetaxel "Accord" i Danmark.
- Bekræft docetaxels rolle i de forsøg, hvor titlen er afkortet eller regimet er uklart.
- Sæt en plan for monitorering af knoglemarv, væskeretention og neuropati.

**Øvrige forudsigelser i Evidence Pack'en (sammenlagt efter fjernelse af dubletter):**
- **Ewing-sarkom** (L2, Research Question): evidensen vedrører næsten udelukkende kombinationen gemcitabin + docetaxel ved recidiverende sygdom, så docetaxels bidrag alene kan ikke isoleres.
- **Småcellet lungekræft** (L4, Hold): næsten al evidens gælder ikke-småcellet lungekræft, og der er ingen SCLC-specifik evidens.
- **Velddifferentieret føtalt adenokarcinom i lungen** (L4, Hold): kun ét case report.
- **Primært pulmonalt lymfom** (L5, Hold): ingen lymfomspecifikt belæg; forudsigelsen skyldes sandsynligvis nærhed mellem lungesygdomme i vidensgrafen.

*Dette resultat er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser skal valideres klinisk, før de anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

