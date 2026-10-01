---
layout: default
title: Emicizumab
parent: Kun modelforudsigelse (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Emicizumab
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

# Emicizumab: Fra hæmofili A til pseudo-von Willebrands sygdom

## Resumé i én sætning

Emicizumab (handelsnavn Hemlibra) er et bispecifikt antistof, der erstatter manglende faktor VIII-funktion ved hæmofili A. TxGNN-modellen forudsiger, at det kan virke ved **pseudo-von Willebrands sygdom** (trombocyttype), men der findes **ingen kliniske forsøg og ingen litteratur** for denne indikation. Forudsigelsen understøttes heller ikke af nogen kendt mekanisme.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i Lægemiddelstyrelsens data. Kendt klinisk anvendelse: profylakse ved hæmofili A |
| Forudsagt ny indikation | Pseudo-von Willebrands sygdom |
| TxGNN-forudsigelsesscore | 99,99 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger ingen detaljerede mekanismedata i databasen. Ud fra den tilgængelige vurdering virker emicizumab ved at forbinde aktiveret faktor IX og faktor X og dermed erstatte den manglende FVIIIa-kofaktorfunktion i tenase-komplekset.

Pseudo-von Willebrands sygdom (trombocyttype) skyldes derimod en gain-of-function-defekt i trombocyttens GPIbα. Den giver øget binding til von Willebrand-faktor og tab af højmolekylære multimerer. Emicizumab virker nedstrøms i koagulationskaskaden og korrigerer ikke denne defekt.

Den høje TxGNN-score afspejler sandsynligvis, at sygdommene ligger tæt på hinanden i vidensgrafen som blødningssygdomme, og ikke en reel biologisk sammenhæng. Forudsigelsen bør derfor betragtes som en modelartefakt, indtil det modsatte er vist.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for denne indikation.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig for denne indikation.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105974617 | Hemlibra (Roche Registration GmbH) | Injektionsvæske, opløsning | Ikke angivet i de tilgængelige data |

---

## Øvrige forudsagte indikationer (til sammenligning)

TxGNN har forudsagt flere indikationer for emicizumab. Den indikation, der er stillet først, har den svageste evidens. En anden har væsentligt stærkere støtte.

| Forudsagt indikation | Score | Evidensniveau | Anbefaling | Kommentar |
|---------|------|------|------|---------|
| Pseudo-von Willebrands sygdom | 99,99 % | L5 | Hold | Ingen mekanistisk eller klinisk støtte |
| Primær frigivelsesdefekt af trombocytter | 99,99 % | L5 | Hold | Emicizumab genopretter ikke trombocyttens frigivelsesreaktion |
| Glanzmanns trombasteni | 99,98 % | L4 | Hold | Kun [NCT04398628](https://clinicaltrials.gov/study/NCT04398628) (observationelt register, ikke specifikt for sygdommen). Den eneste artikel ([37391649](https://pubmed.ncbi.nlm.nih.gov/37391649/)) handler om rFVIIa, ikke emicizumab |
| Scotts syndrom | 99,92 % | L5 | Hold | Aktiviteten vil sandsynligvis være begrænset, fordi fosfolipidoverfladen mangler |
| Erhvervet koagulationsfaktormangel | 99,90 % | L2 | Proceed with Guardrails | Evidensen dækker kun **erhvervet hæmofili A (AHA)**, ikke erhvervede faktormangler generelt |

**Evidens for erhvervet hæmofili A (rang 9 og 10):**

| PMID | År | Type | Tidsskrift | Hovedfund |
|---------|-----|------|------|---------|
| [36696195](https://pubmed.ncbi.nlm.nih.gov/36696195/) | 2023 | Fase III, enkeltarmet, åbent | J Thromb Haemost | Første prospektive studie af emicizumab-profylakse ved AHA (AGEHA) |
| [39134043](https://pubmed.ncbi.nlm.nih.gov/39134043/) | 2025 | Prospektivt studie, slutanalyse | Thromb Haemost | AGEHA-slutanalyse, inkl. patienter uden mulighed for immunsuppression og langtidsprofylakse |
| [37858328](https://pubmed.ncbi.nlm.nih.gov/37858328/) | 2023 | Fase II, enkeltarmet, åbent | Lancet Haematol | GTH-AHA-EMI: emicizumab beskytter mod blødning og muliggør udsættelse af immunsuppression |
| [40795229](https://pubmed.ncbi.nlm.nih.gov/40795229/) | 2025 | Kohorte/opfølgning | Blood Adv | Toårsopfølgning af GTH-AHA-EMI-patienter med vedvarende overlevelsesfordel |
| [39361769](https://pubmed.ncbi.nlm.nih.gov/39361769/) | 2024 | Retrospektiv multicenterkohorte | Blood Adv | 62 AHA-patienter behandlet off-label i 12 amerikanske centre |
| [38049124](https://pubmed.ncbi.nlm.nih.gov/38049124/) | 2024 | Konsensusanbefaling | Hamostaseologie | GTH-AHA-anbefalinger for brug af emicizumab ved AHA |
| [39536818](https://pubmed.ncbi.nlm.nih.gov/39536818/) | 2025 | Narrativt review | J Thromb Haemost | Behandling af AHA i emicizumab-æraen |

Studierne er enkeltarmede og ikke-randomiserede. Evidensen er derfor klassificeret L2, ikke L1.

---

## Sikkerhedsovervejelser

Der er ikke fundet registrerede lægemiddelinteraktioner i databasen. For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
For den primære forudsagte indikation, pseudo-von Willebrands sygdom, findes hverken kliniske forsøg, litteratur eller en plausibel mekanisme. Emicizumab virker nedstrøms for den trombocytdefekt, der forårsager sygdommen. Evidensniveauet er L5.

**For at komme videre kræves:**
- Hent advarsler og kontraindikationer fra Lægemiddelstyrelsens produktresumé (blokerende datamangel for sikkerhedsscreening).
- Hent mekanismedata (MOA) fra DrugBank.
- Prioritér i stedet **erhvervet hæmofili A** til nærmere vurdering. Her er der prospektive studier (AGEHA, GTH-AHA-EMI), og anbefalingen er "Proceed with Guardrails". Den brede TxGNN-betegnelse "erhvervet koagulationsfaktormangel" dækker dog kun delvist, og andre erhvervede mangler (FV, FX, vWF) er ikke understøttet.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

