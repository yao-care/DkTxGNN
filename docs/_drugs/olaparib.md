---
layout: default
title: Olaparib
parent: Høj evidens (L1-L2)
nav_order: 604
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Olaparib: forudsagt ny indikation Brystkræft hos kvinder (female breast carcinoma) (evidensniveau L1). Oprindelig indikation: Æggestokkræft"
monitor_inn: "Olaparib"
predicted_indications: ["female breast carcinoma", "female breast carcinoma"]
---

# Olaparib
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
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

# Olaparib: Fra æggestokkræft til brystkræft hos kvinder

## Resumé i én sætning

Olaparib er en PARP-hæmmer, der oprindeligt anvendes til behandling af æggestokkræft (primært BRCA-muteret og HRD-positiv sygdom).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **brystkræft hos kvinder** (kvindelig brystcarcinom).
Der er i de data, der er indsamlet til denne rapport, **30 registrerede kliniske forsøg** og **20 publikationer** for denne indikation, herunder flere fase 3-RCT'er (OlympiA og OlympiAD).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Æggestokkræft (godkendelsesteksten for det danske produkt er ikke tilgængelig i de indsamlede data; indikationen er hentet fra videnskabsgrafen) |
| Forudsagt ny indikation | Brystkræft hos kvinder (female breast carcinoma) |
| TxGNN-forudsigelsesscore | 99,09 % |
| Evidensniveau | L1 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Olaparib hæmmer enzymerne PARP1 og PARP2 og fanger PARP på DNA'et. I tumorer med defekt homolog rekombinationsreparation, fx ved kimbaneмutationer i BRCA1/2, fører det til syntetisk letalitet: kræftcellerne kan ikke reparere DNA-skader og dør. Bemærk, at de indsamlede data ikke indeholder en officiel mekanismebeskrivelse fra DrugBank; ovenstående er baseret på den mekanistiske vurdering i det samlede materiale.

Den samme BRCA-relaterede DNA-reparationsdefekt, som ligger til grund for den godkendte indikation ved æggestokkræft, findes ved BRCA-muteret brystkræft. Mekanismen kan derfor overføres direkte. Gevinsten forventes dog begrænset til biomarkørselekterede patienter (kimbane-BRCA1/2-mutation, HER2-negativ sygdom).

Den kliniske litteratur bekræfter dette: OlympiA (adjuverende behandling ved tidlig brystkræft) og OlympiAD (metastatisk brystkræft) er randomiserede fase 3-studier hos patienter med gBRCA-mutation.

---

## Evidens fra kliniske forsøg

Et udvalg af de mest relevante forsøg (op til 10):

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00679783](https://clinicaltrials.gov/study/NCT00679783) | Fase 2 | Afsluttet | 99 | Olaparib (AZD2281) hos patienter med kendt BRCA-mutation eller triple-negativ brystkræft; vurderer responsrate og markører. Direkte effektdata |
| [NCT04330040](https://clinicaltrials.gov/study/NCT04330040) | Fase 4 | Afsluttet | 202 | Indiske patienter med platinfølsom recidiverende æggestokkræft og metastatisk brystkræft med gBRCA1/2; understøtter primært sikkerhed og anvendelse i praksis |
| [NCT01623349](https://clinicaltrials.gov/study/NCT01623349) | Fase 1 | Afsluttet | 118 | PI3K-hæmmer (BKM120/BYL719) plus olaparib ved recidiverende triple-negativ brystkræft eller høj-grads serøs æggestokkræft; sikkerhed og dosis |
| [NCT01237067](https://clinicaltrials.gov/study/NCT01237067) | Fase 1 | Afsluttet | 77 | Farmakokinetik/farmakodynamik med olaparib plus carboplatin ved recidiverende kvindelige kræftformer |
| [NCT04683679](https://clinicaltrials.gov/study/NCT04683679) | Fase 2 | Rekrutterer | 34 | Pembrolizumab og ablativ strålebehandling med eller uden olaparib ved metastatisk triple-negativ/HR-positiv HER2-negativ brystkræft |
| [NCT05358639](https://clinicaltrials.gov/study/NCT05358639) | Fase 1 | Aktiv, rekrutterer ikke | 36 | Olaparib plus navitoclax ved TNBC med BRCA1/2- eller PALB2-mutation og ved høj-grads serøs æggestokkræft |
| [NCT01116648](https://clinicaltrials.gov/study/NCT01116648) | Fase 1/2 | Aktiv, rekrutterer ikke | 155 | Cediranib plus olaparib versus olaparib alene ved recidiverende æggestokkræft eller triple-negativ brystkræft |
| [NCT02418624](https://clinicaltrials.gov/study/NCT02418624) | Fase 1 | Afsluttet | 25 | Carboplatin-olaparib efterfulgt af olaparib versus capecitabin ved BRCA-muteret HER2-negativ avanceret brystkræft; bestemmelse af fase 2-dosis |
| [NCT03109080](https://clinicaltrials.gov/study/NCT03109080) | Fase 1 | Afsluttet | 24 | Olaparib med strålebehandling ved triple-negativ brystkræft |
| [NCT07695259](https://clinicaltrials.gov/study/NCT07695259) | Fase 4 | Rekrutterer | 45 | Olaparib plus trastuzumab og pertuzumab som neoadjuverende behandling hos ældre med HER2-positiv brystkræft |

Størstedelen af de registrerede forsøg er tidlige kombinationsstudier (fase 1/2). Den stærkeste evidens kommer fra de publicerede fase 3-RCT'er nedenfor.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [34081848](https://pubmed.ncbi.nlm.nih.gov/34081848/) | 2021 | RCT | N Engl J Med | OlympiA: adjuverende olaparib ved BRCA1/2-muteret tidlig brystkræft |
| [36228963](https://pubmed.ncbi.nlm.nih.gov/36228963/) | 2022 | RCT | Ann Oncol | OlympiA: samlet overlevelse ved højrisiko, HER2-negativ tidlig brystkræft med gBRCA1/2 |
| [28578601](https://pubmed.ncbi.nlm.nih.gov/28578601/) | 2017 | RCT | N Engl J Med | OlympiAD: olaparib ved metastatisk brystkræft med kimbane-BRCA-mutation |
| [30689707](https://pubmed.ncbi.nlm.nih.gov/30689707/) | 2019 | RCT | Ann Oncol | OlympiAD: endelig samlet overlevelse og tolerabilitet versus kemoterapi efter lægens valg |
| [36893711](https://pubmed.ncbi.nlm.nih.gov/36893711/) | 2023 | Forlænget opfølgning | Eur J Cancer | OlympiAD: forlænget opfølgning; median OS 19,3 vs. 17,1 måneder i den endelige præspecificerede analyse (P = 0,513) |
| [33119476](https://pubmed.ncbi.nlm.nih.gov/33119476/) | 2020 | Fase 2 | J Clin Oncol | TBCRC 048: olaparib ved metastatisk brystkræft med mutationer i homolog rekombinationsrelaterede gener |
| [25366685](https://pubmed.ncbi.nlm.nih.gov/25366685/) | 2015 | Fase 2 | J Clin Oncol | Olaparib-monoterapi ved avanceret kræft med kimbane-BRCA1/2-mutation |
| [34143979](https://pubmed.ncbi.nlm.nih.gov/34143979/) | 2021 | Fase 2 | Cancer Cell | I-SPY2: durvalumab plus olaparib og paclitaxel øgede pCR-raten ved højrisiko HER2-negativ brystkræft |
| [38588696](https://pubmed.ncbi.nlm.nih.gov/38588696/) | 2024 | Fase 2-3 RCT | Nature | PARTNER: neoadjuverende olaparib med kemoterapi ved triple-negativ brystkræft uden gBRCA-mutation |
| [32249603](https://pubmed.ncbi.nlm.nih.gov/32249603/) | 2020 | Oversigtsartikel | Future Oncol | Oversigt over olaparib ved avanceret brystkræft |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105941817 | Lynparza (AstraZeneca AB) | Filmovertrukne tabletter | Indikationstekst er ikke tilgængelig i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet terapi (PARP-hæmmer) |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC); anæmi og andre cytopenier er kendte for PARP-hæmmere |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Blodtal (CBC), lever- og nyrefunktion |
| Håndteringsbeskyttelse | Følg lokale retningslinjer for håndtering af kræftlægemidler |

Der foreligger ikke specifikke toksicitetsdata i de indsamlede data. Se advarsler og forsigtighedsregler i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

Oplysninger om advarsler og kontraindikationer fra produktresuméet er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

**Lægemiddelinteraktioner** (100 interaktioner identificeret; et udvalg vises):

- **Alvorlige (Major):** aprepitant, dexamethason, clarithromycin
- **Moderate:** metformin, bupropion, cimetidin, miconazol, glyburid, ondansetron, repaglinid, rosuvastatin, simvastatin m.fl.
- **Mindre (Minor):** prucaloprid

Mange af interaktionerne skyldes sandsynligvis CYP3A-metabolisme og transportere. Klinisk gennemgang af samtidig medicin anbefales.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Olaparib har robust fase 3-evidens (OlympiA og OlympiAD) ved BRCA1/2-muteret, HER2-negativ brystkræft, og mekanismen er den samme som ved æggestokkræft. Gevinsten er begrænset til biomarkørselekterede patienter, og den danske godkendelsestekst er ikke tilgængelig, så anvendelsen skal afgrænses nøje.

**For at komme videre kræves følgende:**
- Verificering af den danske indikationstekst og eventuel eksisterende brystkræftindikation i produktresuméet (Lægemiddelstyrelsen/EMA)
- Sikkerhedsoplysninger fra produktresuméet (advarsler, kontraindikationer), som mangler i de indsamlede data
- Officielle data om virkningsmekanisme (MOA) fra DrugBank
- Klar patientselektion: kimbane-BRCA1/2-mutation og HER2-negativ sygdom, med genetisk testning
- Plan for monitorering af blodtal og gennemgang af interagerende lægemidler

---

*Bemærkning: Rangering 3-8 i forudsigelserne (kønscelletumorer og choriocarcinom i æggestokken) har evidensniveau L4-L5 og anbefalingen "Hold". De er ikke behandlet nærmere i denne rapport.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

