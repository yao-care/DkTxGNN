---
layout: default
title: Trastuzumab Deruxtecan
parent: Kun modelforudsigelse (L5)
nav_order: 447
evidence_level: L5
indication_count: 10
---

# Trastuzumab Deruxtecan
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

# Trastuzumab Deruxtecan: Fra HER2-målrettet onkologisk brug til forudsagt lægemiddelinduceret osteoporose

## Ét-sætnings sammenfattelse

> Trastuzumab deruxtecan (T-DXd) er et HER2-målrettet antistof-lægemiddelkonjugat (ADC), hvis oprindelige godkendte indikation ikke er specificeret i denne dokumentation.
> TxGNN-modellens vigtigste forudsigelse er **lægemiddelinduceret osteoporose** (score 99,31 %), men denne kandidat — og de fire andre vigtigste forudsigelser — understøttes af **nul kliniske forsøg og nul publikationer**, og dokumentationens egen mekanistiske analyse markerer forudsigelsen som sandsynligvis et artefakt i vidensgrafen snarere end et ægte terapeutisk signal.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Originalindikation | Ikke specificeret i dokumentationen (lægemidlet klassificeres som HER2-målrettet antistof-lægemiddelkonjugat ifølge mekanistiske noter) |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose (duplikat post ved rang 1 og 2 — sandsynligt artefakt fra deduplicering) |
| TxGNN-forudsigelsesscore | 99,31 % |
| Evidensieniveau | L5 (kun modelforudsigelse, ingen understøttende studier) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Vent (Hold) |

---

## Hvorfor er denne forudsigelse rimelig?

Trastuzumab deruxtecan (T-DXd) beskrives i dokumentationen som et HER2-målrettet antistof-lægemiddelkonjugat (ADC) med en nyttelast bestående af en topoisomeraseinhibitor I (DXd). Ingen oprindelige indikationsdata blev leveret til dette pakke, så den traditionelle "oprindelig indikation → ny indikation" mekanistiske bro kan ikke konstrueres med sikkerhed.

Endnu vigtigere er det, at dokumentationens egen begrundelse for hver enkelt af de 10 vigtigste forudsigelser eksplicit konkluderer, at **der ikke findes kendt mekanistisk vej**, der forbinder et HER2/topoisomerasehibitor-I-målrettet ADC til nogen af de forudsagte tilstande (lægemiddelinduceret osteoporose, diabetisk retinopati og dets alvorlige undertype, bronkitis eller diabetisk katarakt). Vurderingen antyder, at disse høje TxGNN-scores mere sandsynligt afspejler semantisk co-forekomst i vidensgrafen (f.eks. delte noder med benmetastase, kemoterapirelateret vævsskade eller generelle antistof-/onkologi-klynger) snarere end en reel behandlingshypotese.

Bemærkselsesværdigt er det, at dokumentationen for adskillige kandidater rejser en **retningsbestemt inverteret bekymring**: T-DXd har en kendt klasse af øjetoksicitet (korneal-/keratopati-signaler) og en veletableret risiko for interstitiel lungensygdom (ILD)/pneumonitis. Hvis vidensgrafen forbinder lægemidlet med øje- eller respiratorrelated sygdomsknuder (diabetisk retinopati, diabetisk katarakt, bronkitis), kan dette afspejle lægemidlets **kendte uønsket vejkningsprofil, der bliver misfortolket som et terapeutisk signal**, snarere end ægte genbrugspotentiale. Dette er en kritisk advarsel for klinisk fortolkning.

---

## Bevis for kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

*(Bekræftet ved direkte forespørgsler mod ClinicalTrials.gov og ICTRP for alle fem unikke forudsagte indikationer — lægemiddelinduceret osteoporose, alvorligt ikke-proliferativt diabetisk retinopati, diabetisk retinopati, bronkitis og diabetisk katarakt — hver returnerer 0 resultater.)*

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

*(Bekræftet ved direkte PubMed-forespørgsler for alle fem unikke forudsagte indikationer, hver returnerer 0 resultater.)*

---

## Markedsinformation for Danmark

Der er i øjeblikket ingen markedsføringstilladelser registreret for dette produkt i Danmark (0 licenser til stede; markedsstatus: Ikke markedsført).

---

## Cellgiftighed

Trastuzumab deruxtecan er et antineoplastisk antistof-lægemiddelkonjugat (HER2-målrettet levering af en cytotoksisk topoisomerasehibitor I-nyttelast), så dette afsnit gælder.

| Punkt | Indhold |
|------|---------|
| Cellgiftighedsklassificering | Målrettet terapi — antistof-lægemiddelkonjugat (ADC) med levering af konventionel cytotoksisk nyttelast (topoisomerasehibitor I) |
| Myelosuppressionrisiko | Se venligst produktresumé (SmPC) for advarsler og forholdsregler |
| Emetogenicitet-klassificering | Se venligst produktresumé (SmPC) for advarsler og forholdsregler |
| Overvågningspunkter | Se venligst produktresumé (SmPC) for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se venligst produktresumé (SmPC) for advarsler og forholdsregler |

---

## Sikkerhedsovervejelser

Se venligst godkendt produktresumé (SmPC) for sikkerhedsinformation. Der blev ikke fundet nogen lægemiddelinteraktionsregistreringer i den forespurgte database.

**Bemærk:** Advarsler og kontraindikationer på produktetiketten er markeret som et **blokerende** datahul i denne dokumentation (utilgængelig fra regulatorkilde), hvilket betyder, at en formel sikkerhedspre-vurdering endnu ikke kan gennemføres for denne kandidat.

---

## Konklusion og næste trin

**Afgørelse: Vent (Hold)**

**Begrundelse:**
- Alle fem unikke forudsagte indikationer er TxGNN-modeloutput kun (evidensieniveau L5), med nul bekræftende kliniske forsøg eller litteratur.
- Dokumentationens egen mekanistiske gennemgang konkluderer, at der ikke er nogen plausibel biologisk rationale for nogen toprangeret forudsigelse, og advarer om, at nogle forbindelser kan afspejle lægemidlets kendt toksicitetsprofil (ILD, keratopati) snarere end terapeutisk potentiale.
- Sikkerhedsdata på produktetiketten (advarsler/kontraindikationer) er et blokerende hul, hvilket forhindrer en formel sikkerhedspre-vurdering.
- Forudsigelseslisten indeholder duplikerede poster (rækkerne 1–2, 3–4, 5–6, 7–8, 9–10 er identiske par), hvilket angiver et datakvalitetsproblem i forbindelseslinjen.

**For at fortsætte kræves følgende:**
- TFDA/SmPC-etiketdata (advarsler, kontraindikationer) — i øjeblikket blokerende
- Bekræftet virkningsmekanisme (MOA) og oprindeligt godkendt indikation(er) for dette lægemiddel
- Deduplicering af predicted_indications-datasettet ved kilden
- Hvis en kandidat bliver forfulgt videre, er prekliniske/mekanistiske studier nødvendige før avancement ud over S0, givet den fuldstændige mangel på klinisk eller litteraturbevis

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

