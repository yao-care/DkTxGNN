---
layout: default
title: Cerliponase Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 104
evidence_level: L5
indication_count: 10
---

# Cerliponase Alfa
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

# Cerliponase Alfa: Fra Neuronal Ceroid Lipofuscinosis Type 2 til Scheies Syndrom

## Sammenfatning (One-Sentence Summary)

Cerliponase alfa (Brineura) er en rekombinant human tripeptidylpeptidase 1 (TPP1) enzym-erstatningsterapi, godkendt i EU til neuronal ceroid lipofuscinose type 2 (CLN2-sygdom / sent infantil Battens sygdom), administreret intracerebroventriklet (ICV).
TxGNN-modellen forudsiger, at det kan være effektivt for **Scheies Syndrom** (MPS I-S) med en score på 99.98%, men der er **ikke fundet understøttende kliniske forsøg eller litteratur** for denne kombination.
Denne forudsigelse ser ud til at være drevet af nærhed i vidensgrafen inden for kategorien lysosomal lagringssygdom (LSD), snarere end ægte mekanistisk overlap.

---

## Hurtig Oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig Indikation | Neuronal ceroid lipofuscinose type 2 (CLN2-sygdom) — TPP1-mangel forårsager progressiv neurodegeneration hos børn |
| Forudsagt Ny Indikation | Scheies Syndrom (MPS I-S) |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal Markedsføringstilladelser | 0 |
| Anbefalet Afgørelse | Afvent |

---

## Hvorfor er Denne Forudsigelse Rimelig?

Cerliponase alfa er en rekombinant form af humant tripeptidylpeptidase 1 (TPP1), et lysosomalt serinprotease. I CLN2-sygdom forårsager loss-of-function-mutationer i *TPP1*-genet manglende evne til at nedbryde ceroid-type proteinaggregater inden for neuronale lysosomer, hvilket resulterer i progressiv motor- og sprogtilbagegang og for tidlig død hos ramte børn. Cerliponase alfa leveres via en implanteret intracerebroventriklet (ICV) reservoirenhed specifikt for at omgå blod-hjerne-barrieren og nå CNS-neuroner — hvilket afspejler den fundamentalt neurologiske natur af dens target-sygdom.

Scheies Syndrom (MPS I-S) er forårsaget af en partiel mangel på et helt forskelligt lysosomalt enzym: **α-L-iduronidase (IDUA)**, kodet af *IDUA*-genet. Den resulterende ophobning af dermatan sulfat og heparan sulfat i bindevæv, hjerteklaffer og andre perifere organer er fuldstændig uafhængig af TPP1/ceroid-banen. En godkendt enzym-erstatningsterapi — laronidase (Aldurazyme, BioMarin/Genzyme) — findes allerede for denne indikation og retter sig mod det rigtige enzymdefekt.

Den høje TxGNN-forudsigelsesscore afspejler næsten helt sikkert vidensgraf-nærhed: både CLN2 og Scheies Syndrom er lysosomale lagringssygdomme (LSD'er), og TxGNN-modellen har sandsynligvis lært stærke associationer inden for LSD-sygdomsklyngen. Men **enzym-erstatningsterapi er meget target-specifik** — TPP1 har ingen funktionel redundans med IDUA, og administrering af cerliponase alfa til en patient med Scheies Syndrom ville ikke adressere den underliggende glykosaminoglyan-ophobning. Dette er et tilfælde, hvor graf-niveau kategori-lighed ikke oversættes til mekanistisk plausibilitet.

---

## Klinisk Forsøgsbevis

Ingen kliniske forsøg, der undersøger cerliponase alfa ved Scheies Syndrom, er blevet identificeret.

---

## Litteraturbevis

Ingen publikationer, der undersøger cerliponase alfa ved Scheies Syndrom, er blevet identificeret.

---

## Yderligere Forudsagte Indikationer — Mekanistisk Vurdering

Evidence Pack'et omfatter fire yderligere forudsagte indikationer, alle inden for LSD-kategorien. For fuldstændighed gives en kort vurdering af hver. Alle bærer samme fundamentale bekymring: enzym-target mismatch.

| Forudsagt Indikation | TxGNN Score | Enzymdefekt i Sygdom | Hvorfor Cerliponase Alfa Ikke Gælder |
|---|---|---|---|
| Scheies Syndrom (MPS I-S) | 99.98% | IDUA (α-L-iduronidase) | Godkendt ERT findes (Laronidase); TPP1 ≠ IDUA |
| Hurlers Syndrom (MPS I-H) | 99.97% | IDUA (samme som Scheie, alvorlig fænotype) | Laronidase godkendt; TPP1 ≠ IDUA |
| LSD med knogleinvolvering | 99.95% | Multipel (samlebetegnelse: MPS, Gaucher, osv.) | CLN2 er udelukkende CNS; ingen skelettal patologi; ICV-vej ikke relevant |
| Kolesterylester lagringssygdom | 99.93% | LAL (lysosomalt surt lipase, *LIPA*-gen) | Godkendt ERT findes (Sebelipase alfa/Kanuma); TPP1 ≠ LAL |
| Gauchers Sygdom | 99.93% | β-glucocerebrosidase (*GBA*-gen) | Flere godkendte ERT'er/SRT'er; TPP1 ≠ GBA |

**Bemærkning om Gauchers Sygdom-litteratur**: En PubMed-artikel (PMID [41527340](https://pubmed.ncbi.nlm.nih.gov/41527340/)) blev hentet. Dette er et metodologisk paper om naturhistorie-kortlægning af LSD'er ved brug af Gauchers Sygdom som rammeværk; det indeholder intet bevis for cerliponase alfa ved Gauchers Sygdom.

---

## Markedsinformation for Danmark

Cerliponase alfa er ikke godkendt til brug i Danmark og har ingen markedsføringstilladelser registreret hos Lægemiddelstyrelsen.

> **Bemærkning for ordinanter**: Cerliponase alfa (Brineura) har en centraliseret EMA-markedsføringstilladelse (EU/1/17/1189, givet i maj 2017) for CLN2-sygdom i hele EU/EØS. Adgang i Danmark ville kræve ansøgning gennem named patient- eller compassionate use-ordningen. Denne tilladelse dækker kun lægemidlets godkendte indikation (CLN2) — ikke nogen af de LSD-repurposing-mål, der diskuteres i denne rapport.

---

## Sikkerhedshensyn

Detaljerede danske SmPC-advarsler og kontraindikationer for cerliponase alfa var ikke tilgængelige i det nuværende datasæt. Ingen lægemiddel-lægemiddel interaktioner blev identificeret i DDI-databasen.

Se venligst den godkendte EMA-resumé af produktegenskaber (SmPC) for Brineura for fuldstændig sikkerhedsinformation, herunder de kendte risici forbundet med ICV-kateter-implantation, enhedsrelaterede infektioner og overfølsomhedsreaktioner.

---

## Konklusion og Næste Trin

**Afgørelse: Afvent**

**Begrundelse:**
Alle fem forudsagte indikationer er mekanistisk usandsynlige repurposing-mål for cerliponase alfa: hver tilstand involverer et særskilt lysosomalt enzymdefekt, der er helt adskilt fra TPP1, det enzym cerliponase alfa erstatter. De høje TxGNN-scores (≥99.93%) på tværs af alle forudsigelser afspejler kategori-niveau-lighed inden for LSD-vidensgraf-klyngen, ikke ægte biologisk overlap. Desuden findes der allerede godkendt enzym-erstatningsterapi for Scheies Syndrom, Hurlers Syndrom, kolesterylester lagringssygdom og Gauchers Sygdom, hvilket efterlader ingen uopfyldt terapeutisk niche for cerliponase alfa i disse indikationer.

**For at kunne fortsætte, ville følgende være nødvendigt:**

- **Mekanistisk revurdering**: En formel mekanistisk hypotese, der forklarer, hvordan TPP1-substitution kunne være gavnlig for MPS I, LSD med knogleinvolvering, CESD eller Gauchers fænotype, ville skulle etableres — dette mangler i øjeblikket
- **Præklin dokumentation**: In vitro- eller in vivo-studier, der demonstrerer en TPP1-medieret fordel i de forudsagte sygdomsmodeller, ville være påkrævet som minimum, før klinisk undersøgelse kunne overvejes
- **SmPC og sikkerhedsdata**: Fuldstændig ordinationsinformation for cerliponase alfa (ICV-administrations-risici, infektionsrater, overfølsomhedsprofil) skal gennemgås for enhver fremtidig tværindikativ sikkerhedsvurdering
- **Dansk regulatorisk vej**: Hvis fremtidigt bevis skulle opstå, ville en variation af den eksisterende EMA-godkendelse eller en ny indikationsansøgning være påkrævet; named-patient adgang til ikke-godkendte indikationer ville kræve gennemgang af etisk komité

> **Ansvarsfraskrivelse for forskning**: Denne rapport er til forskningsformål alene og udgør ikke medicinsk rådgivning. Repurposing-kandidater kræver klinisk validering forud for enhver klinisk anvendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

