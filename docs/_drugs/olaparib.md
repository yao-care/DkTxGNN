---
layout: default
title: Olaparib
parent: Kun modelforudsigelse (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
---

# Olaparib
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

# Olaparib: Mod kvindelig brystkræft (female breast carcinoma)

## Resumé i få sætninger

Olaparib er en oral PARP-hæmmer, som markedsføres i Danmark som Lynparza. Datasættet indeholder ingen registreret original indikation for lægemidlet.
TxGNN-modellen forudsiger, at olaparib kan være effektivt ved **kvindelig brystkræft**. Forudsigelsen understøttes af **50 kliniske forsøg** og **20 publikationer**, herunder store randomiserede fase 3-studier (OlympiA og OlympiAD) hos patienter med kimbane-BRCA-mutation.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Kvindelig brystkræft (female breast carcinoma) |
| TxGNN-forudsigelsesscore | 99,09 % |
| Evidensniveau | L1 (baseret på fase 3-RCT'er i litteraturen) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ingen detaljerede mekanismedata (MOA) i datasættet. Olaparib tilhører klassen af PARP-hæmmere. PARP er et enzym, der indgår i reparation af DNA-skader. Ved at hæmme PARP opstår der "syntetisk letalitet" i tumorceller med defekt homolog rekombinationsreparation, for eksempel ved kimbane-BRCA1/2-mutationer. Sunde celler tåler hæmningen bedre.

Mekanismen er veletableret ved BRCA-muteret, HER2-negativ brystkræft. Den centrale pointe er, at effekten er biomarkørafhængig. Fordelen er påvist ved kimbane-BRCA-muteret sygdom og for visse andre HRR-muterede tilfælde. Brug skal derfor ske efter biomarkørselektion.

Olaparib er allerede godkendt til BRCA-muteret brystkræft i andre regioner. Forudsigelsen er derfor snarere et spørgsmål om datakompletthed end et egentligt nyt repurposing-signal. TxGNN-scoren (0,99) stemmer overens med den kliniske evidens, men er ikke i sig selv evidens.

---

## Klinisk forsøgsevidens

Der er identificeret 50 forsøg. Tabellen viser de 10 mest relevante for brystkræft. Det er vigtigt, at ingen afsluttede fase 3-forsøg med brystkræft som primær population fremgår af forsøgslisten. Fase 3-evidensen findes i publikationerne nedenfor.

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Fase 4 | Afsluttet | 202 | Indiske patienter med platinfølsom recidiverende ovariecancer og metastatisk brystkræft med kimbane-BRCA1/2-mutation |
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Fase 2 | Afsluttet | 99 | Åbent studie af AZD2281 (olaparib) ved BRCA-positiv eller triple-negativ brystkræft samt ovariecancer; responsrate og korrelative markører |
| [NCT05498155](https://clinicaltrials.gov/study/NCT05498155) | Fase 2 | Aktiv, rekrutterer ikke | 50 | Neoadjuverende olaparib alene eller med durvalumab ved BRCA-muteret, tidlig HER2-negativ brystkræft |
| [NCT06201234](https://clinicaltrials.gov/study/NCT06201234) | Fase 2 | Rekrutterer | 176 | Elacestrant tillagt olaparib ved HR-positiv, HER2-negativ, avanceret eller metastatisk brystkræft med gBRCA1/2-mutation |
| [NCT02624973](https://clinicaltrials.gov/study/NCT02624973) | Fase 2 | Aktiv, rekrutterer ikke | 200 | PETREMAC: personaliseret behandling ved højrisiko-brystkræft; biomarkørdrevet, ikke-konfirmatorisk design |
| [NCT01445418](https://clinicaltrials.gov/study/NCT01445418) | Fase 1 | Afsluttet | 103 | Olaparib plus carboplatin ved bryst- og ovariecancer hos BRCA1/2-bærere samt sporadisk triple-negativ brystkræft; sikkerhed og dosering |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Fase 1 | Afsluttet | 118 | PI3K-hæmmer plus olaparib ved recidiverende triple-negativ brystkræft eller højgradig serøs ovariecancer; kombinationssikkerhed |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Fase 1 | Aktiv, rekrutterer ikke | 36 | Olaparib plus navitoclax ved triple-negativ brystkræft med BRCA1/2- eller PALB2-mutation |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Fase 1/2 | Aktiv, rekrutterer ikke | 155 | Cediranib og olaparib ved recidiverende triple-negativ brystkræft eller ovariecancer |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Fase 1 | Afsluttet | 24 | Olaparib sammen med strålebehandling ved triple-negativ brystkræft |

---

## Litteraturevidens

Der er identificeret 20 publikationer. Tabellen viser de 10 mest relevante, prioriteret som RCT, derefter oversigtsartikler.

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|---------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT (fase 3) | N Engl J Med | OlympiA: adjuverende olaparib til patienter med BRCA1/2-muteret tidlig brystkræft |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT (fase 3) | Ann Oncol | OlympiA: samlet overlevelse for 1 års adjuverende olaparib versus placebo ved kimbane-BRCA1/2-variant og højrisiko, tidlig HER2-negativ brystkræft |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT (fase 3) | N Engl J Med | OlympiAD: olaparib ved metastatisk brystkræft med kimbane-BRCA-mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT (fase 3) | Ann Oncol | OlympiAD: endelig overlevelses- og tolerabilitetsanalyse versus kemoterapi efter lægens valg |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | RCT (fase 3) | Eur J Cancer | OlympiAD forlænget opfølgning; median samlet overlevelse 19,3 mdr. (olaparib) mod 17,1 mdr. (kemoterapi) i den endelige præspecificerede analyse (P = 0,513) |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | RCT (fase 2) | Cancer Cell | I-SPY2: durvalumab, olaparib og paclitaxel ved højrisiko HER2-negativ brystkræft stadium II/III; pCR-raten steg i alle HER2-negative undergrupper |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Fase 2-studie | J Clin Oncol | TBCRC 048: olaparib ved metastatisk brystkræft med somatiske BRCA1/2-mutationer eller mutationer i andre HR-relaterede gener |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | Fase 2-3 RCT | Nature | PARTNER: neoadjuverende carboplatin-paclitaxel med eller uden olaparib ved triple-negativ brystkræft uden kimbane-BRCA-mutation (n = 559) |
| [33710534](https://pubmed.ncbi.nlm.nih.gov/33710534/) | 2021 | Oversigtsartikel | Target Oncol | Opdatering om orale PARP-hæmmere ved brystkræft; olaparib og talazoparib er godkendt som monoterapi ved kimbane-BRCA-muteret HER2-negativ brystkræft |
| [39791278](https://pubmed.ncbi.nlm.nih.gov/39791278/) | 2025 | Oversigtsartikel | CA Cancer J Clin | Pan-tumor-oversigt over PARP-hæmmeres rolle på tværs af kræftformer |

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28105941817 | Lynparza (AstraZeneca AB) | Filmovertrukne tabletter | Ikke oplyst i datasættet |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Målrettet behandling (PARP-hæmmer) |
| Risiko for knoglemarvssuppression | Hæmatologisk toksicitet bør forventes; sjælden MDS/AML er beskrevet |
| Emetogenicitet | Se produktresuméet (SmPC) |
| Monitorering | Fuldt blodbillede (CBC) |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

Datasættet indeholder ingen registrerede data om advarsler, kontraindikationer eller interaktioner. Der blev ikke fundet interaktionsdata for olaparib. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Det er også relevant, at et tilfælde i litteraturen (PMID 36947209) peger på, at olaparib ikke anbefales ved svært nedsat nyrefunktion (CrCl ≤ 30 ml/min), fordi farmakokinetik og sikkerhed ikke er evalueret hos disse patienter.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
- Der er stærk evidens fra store fase 3-RCT'er (OlympiA og OlympiAD) for brug ved kimbane-BRCA-muteret, HER2-negativ brystkræft. Fordelen er knyttet til biomarkørstatus, så brug skal være biomarkørstyret.
- TxGNN-scoren på 99,09 % er modellens forudsigelse og ikke evidens i sig selv. Samtidig udgør indikationen formentlig ikke et reelt repurposing-signal, da olaparib allerede er godkendt til BRCA-muteret brystkræft i andre regioner.

**For at komme videre kræves følgende:**
- Den godkendte danske indikationstekst (data fra Lægemiddelstyrelsen mangler) og en gennemgang af produktresuméets advarsler og kontraindikationer. Sikkerhedsscreeningen kan ikke afsluttes uden disse.
- Detaljerede mekanismedata (MOA) fra DrugBank.
- Bekræftelse af, at de behandlede patienter er biomarkørselekterede (kimbane-BRCA1/2 eller andre HRR-mutationer).
- Plan for hæmatologisk monitorering og opmærksomhed på sjælden MDS/AML.

Øvrige forudsagte indikationer vurderes ikke i dette dokument, men resultatet i datasættet er: Ovariecancer (ovarian neoplasm) støttes af fase 3-RCT'er og er som brystkræft en allerede godkendt indikation (Proceed with Guardrails). Kimcelletumorer i gonader og æggestokke samt choriocarcinom i ovarie har ingen eller kun utilstrækkelig evidens (Hold).

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddel-repurposing kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

