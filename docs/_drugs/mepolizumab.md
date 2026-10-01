---
layout: default
title: Mepolizumab
parent: Moderat evidens (L3-L4)
nav_order: 285
evidence_level: L4
indication_count: 10
---

# Mepolizumab
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Mepolizumab: Fra eosinofil-relateret sygdom til immunmedieret trombocytopeni

## Resumé i få sætninger

Mepolizumab (handelsnavn Nucala) er et anti-IL-5-antistof, der nedsætter antallet af eosinofile granulocytter. Det er markedsført i Danmark, men indikationsteksten indgår ikke i datagrundlaget. TxGNN-modellen forudsiger, at det kan have effekt ved **immunmedieret trombocytopeni** (trombocytopeni pga. immundestruktion). Evidensen består kun af **1 case report** og **ingen kliniske forsøg**, så forudsigelsen er endnu et forskningsspørgsmål og ikke et behandlingsgrundlag.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i de danske godkendelsesdata |
| Forudsagt ny indikation | Trombocytopeni pga. immundestruktion (thrombocytopenia due to immune destruction) |
| TxGNN-forudsigelsesscore | 99,66 % |
| Evidensniveau | L4 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ingen detaljerede data om virkningsmekanisme i Evidence Pack. Mepolizumab er dog et monoklonalt antistof mod interleukin-5 (IL-5), som er en central vækst- og overlevelsesfaktor for eosinofile granulocytter. Behandlingen nedsætter derfor antallet af eosinofile. Denne beskrivelse bygger på almen farmakologisk viden og ikke på data i pakken.

Hos patienter med hypereosinofilt syndrom kan eosinofil-drevet immundysregulering optræde sammen med autoimmune cytopenier. Hvis eosinofilien bringes under kontrol, kan immunmedieret trombocytopeni derfor muligvis bedres **indirekte**. Effekten ville i så fald være sekundær til eosinofildepletion og ikke en direkte påvirkning af trombocytdestruktionen.

Den eneste evidens er en enkelt case report om en steroidresistent hypereosinofil immundiatese, der gik i remission under mepolizumab sammen med anden behandling. Patientens trombocytfænotype og den samtidige behandlings bidrag kan ikke bekræftes ud fra de foreliggende oplysninger, fordi titlen er afkortet i datagrundlaget. Den meget høje TxGNN-score (0,997) er en beregningsmæssig forudsigelse og ikke klinisk evidens.

Modellen foreslog også andre trombocytrelaterede tilstande, og de er svagere end hovedkandidaten:

| Forudsagt tilstand | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Primær frigivelsesforstyrrelse af trombocytter | 99,61 % | L5 | Ingen plausibel direkte mekanisme. Blokade af IL-5 påvirker ikke trombocytternes granulafrigivelse. |
| Pseudo-von Willebrands sygdom | 99,44 % | L5 | Skyldes en gain-of-function-defekt i GPIb-alfa, uden kendt forbindelse til IL-5. Ingen studier. |
| Autoimmun trombocytopeni | 99,33 % | L5 | Svag, spekulativ og indirekte begrundelse. Overlapper sandsynligvis med hovedkandidaten og bør afstemmes ved kuratering. |
| Glanzmanns trombastheni | 99,28 % | L5 | Arvelig defekt i integrin αIIbβ3 uden biologisk forbindelse til IL-5. Sandsynligvis en artefakt i vidensgrafen. |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [28648630](https://pubmed.ncbi.nlm.nih.gov/28648630/) | 2018 | Case report | Blood Cells Mol Dis | Steroidresistent hypereosinofil immundiatese, der gik i remission med mepolizumab, sammen med bedring af en blandet trombotisk mikroangiopati. Patienten havde atypisk hæmolytisk uræmisk syndrom (aHUS) med komplementdrevet eosinofili. |

---

## Markedsinformation i Danmark

| Tilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106177118 | Nucala (GlaxoSmithKline Trading Services) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Ikke oplyst i datagrundlaget |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ingen registrerede lægemiddelinteraktioner i de foreliggende data.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger kun på én case report om en anden grundtilstand (hypereosinofilt syndrom med aHUS), og der er ingen kliniske forsøg. Effekten ved immunmedieret trombocytopeni ville desuden være indirekte, via eosinofildepletion. Sikkerhedsscreening kan ikke gennemføres, før advarsler og kontraindikationer fra det danske produktresumé er indhentet.

**For at komme videre kræves følgende:**
- Advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen (blokerende datahul).
- Data om virkningsmekanisme fra DrugBank.
- Den danske indikationstekst for Nucala, så den oprindelige indikation kan dokumenteres.
- Gennemgang af case reporten i fuld tekst, især patientens trombocytfænotype og den samtidige behandling.
- Systematisk litteratursøgning efter mepolizumab ved immun trombocytopeni, herunder eosinofilassocierede tilfælde.
- Afstemning af de overlappende poster for immun trombocytopeni og autoimmun trombocytopeni.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser fra TxGNN skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

