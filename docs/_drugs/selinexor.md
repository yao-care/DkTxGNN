---
layout: default
title: Selinexor
parent: Høj evidens (L1-L2)
nav_order: 396
evidence_level: L2
indication_count: 10
---

# Selinexor
{: .fs-9 }

Evidensniveau: **L2** | Forudsagte indikationer: **10** stk.
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

# Selinexor: Fra en udokumenteret original indikation til Progesterone-receptor negativ brystkræft

## Resumé i en sætning

Selinexor (DrugBank DB11942) er en XPO1/CRM1 kerneksporthæmmer; dens dokumenterede oprindelige indikation er ikke tilgængelig i denne bevissamling, og lægemidlet markedsføres i øjeblikket ikke i Danmark. TxGNN-modellen frembragte flere brystkræft-relaterede forudsigelser, men kun **Progesterone-receptor negativ brystkræft** understøttes af et faktisk afsluttet klinisk forsøg — et lille, efterforsker-initieret fase 2-studie (n=10) — mens modellens højest-scorende output ("lægemiddelinduceret osteoporose") er markeret i selve bevissamlingen som sandsynligt modelbrus uden understøttende mekanisme, forsøg eller litteratur.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|--------|
| Oprindelig indikation | Ikke dokumenteret i denne bevissamling (`original_indications` tom; ikke markedsført i Danmark) |
| Forudsagt ny indikation | Progesterone-receptor negativ brystkræft |
| TxGNN-forudsigelsesscore | 97.20% |
| Bevisniveau | L2 |
| Danmarks markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Standby |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanisme-data for Selinexor er ikke tilgængelige i Laegemiddelstyrelsen-registreringsposten, der blev brugt til at bygge denne bevissamling (markeret som datakløft med høj alvor). Baseret på analysen, der ledsager denne forudsigelse, forstås Selinexor at fungere som en selektiv kerneksporthæmmer (SINE), der målretter XPO1/CRM1. Dette tvinger tumorundertrykkende proteiner såsom p53, FOXO3a og IκB til at forblive i kernen og reducerer translationen af onkoproteiner såsom MYC og cyclin D1 — en mekanisme med præklinisk understøttelse på tværs af flere solide tumorer, herunder brystkræft.

Progesterone-receptor negativ brystkræft bærer typisk en dårligere prognose og reagerer mindre godt på hormonbehandling. En XPO1-hæmningsmekanisme tilbyder en ikke-hormon-afhængig terapeutisk begrundelse, hvilket er konsistent med, hvorfor denne kandidat — blandt modellens brystkræft-relaterede forudsigelser — har faktisk klinisk undersøgelse bag sig (se Klinisk forsøgsbevis nedenfor).

Det er værd at bemærke, at dette ikke var modellens højest-scorende output. Det højest-rangerede output, "lægemiddelinduceret osteoporose" (score 99.22%), er eksplicit anmærket i bevissamlingen som manglende knogleskyttelsesmekanisme — Selinexors kendte bivirkningsprofil (manglende appetit, vægttab, træthed, trombocytopeni) går imod sådan en indikation — og har nul understøttende forsøg eller litteratur. På samme måde viser HER2-positiv brystcarcinom, normal brystlignende subtype og PR-positiv brystkræft ingen direkte mekanistisk eller klinisk-forsøgs-understøttelse og ser ud til at afspejle generisk "brystkræft" nodeproksimitet i vidensgraf'et snarere end subtype-specifikt signal. Progesterone-receptor negativ brystkræft præsenteres derfor her som den mest troværdige kandidat, da det er den eneste, der er forankret i et faktisk afsluttet forsøg.

---

## Klinisk forsøgsbevis

| Forsøgsnummer | Fase | Status | Tilmelding | Vigtige resultater |
|---------|------|------|------|---------|
| [NCT02402764](https://clinicaltrials.gov/study/NCT02402764) | Fase 2 | Afsluttet | 10 | Efterforsker-initieret, enkelt-arms studie af selinexor (KPT-330) i metastatisk triple-negativ brystkræft, vurderer effektivitet, sikkerhed og tolerabilitet. Lille stikprøvestørrelse (n=10) begrænser statistisk styrke; klassificeret som eksplorativ snarere end bekræftende bevis. |

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Danmarks markedsinformation

Selinexor markedsføres i øjeblikket ikke i Danmark (Laegemiddelstyrelsen markedsstatus: **Ikke markedsført**) og har ingen nationale eller centraliserede (EMA) markedsføringstilladelser registreret i denne bevissamling.

---

## Cytotoxicitet

| Punkt | Indhold |
|------|--------|
| Cytotoxicitets-klassifikation | Målrettet terapi (XPO1/CRM1 selektiv kerneksporthæmmer, SINE) |
| Myelosuppression-risiko | Signal noteret i bevissamlings-analyse: trombocytopeni anført blandt Selinexors kendte sikkerhedsspørgsmål; endnu ikke bekræftet mod en officiel etiket |
| Emetogenicitets-klassifikation | Se venligst produktresumét (SmPC) advarsler og forholdsregler |
| Overvågningspunkter | Fuldstændig blodcelletælling (med opmærksomhed på blodplader), givet det noterede thrombocytopeni-signal; lever- og nyrefunktion |
| Håndteringsbeskyttelse | Se venligst produktresumét (SmPC) og institutionel cytotoxisk/farefyldt-lægemiddel håndteringspolitik |

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation — vigtige advarsler, kontraindikationer og lægemiddel-lægemiddel-vekselvirkningsdata er endnu ikke tilgængelige i denne bevissamling (DDI-forespørgsel returnerede ingen resultater).

Bemærk: bevissamlingens analytiske kommentar (ikke bekræftet mod en officiel etiket) refererer til kendte Selinexor-forbundne uønskede virkninger — manglende appetit, vægttab, træthed og trombocytopeni — relevant for fremtidigt overvågningsplan-design.

---

## Konklusion og næste trin

**Beslutning: Standby**

**Begrundelse:**
Hovedkandidaten (progesterone-receptor negativ brystkræft) har en plausibel mekanisme og et afsluttet men lille, enkelt-arms fase 2-forsøg (L2, n=10) — et lovende men tidligt-stadiet signal. Progression er i øjeblikket blokeret af et datakløft med blokeringsmæssig alvor (manglende dansk/TFDA-ækvivalent etiketadvarsler og kontraindikationer, som forhindrer selv initial sikkerhedsscreening) og et datakløft med høj alvor i dokumenteret virkningsmekanisme. Modellens øvrige, højere scorende brystkræft- og osteoporose-forudsigelser mangler nogen klinisk eller mekanistisk støtte og vurderes som sandsynlige modelartefakter snarere end ægte genbestemmelsessignaler.

**For at fortsætte er følgende nødvendigt:**
- Officielt dansk/EU produktresumé advarsler, kontraindikationer og DDI-data for Selinexor (blokerer i øjeblikket initial sikkerhedsscreening)
- Bekræftet oprindelig indikation og virkningsmekanisme-dokumentation fra DrugBank eller regulatoriske kilder
- Større kontrolleret (ideelt randomiseret) forsøgsdata ud over det enkelt-arms n=10 studie, før nogen guardrail-baseret progression overvejes
- Genbesyn af de øvrige høj-score, bevis-frie forudsigelser (lægemiddelinduceret osteoporose, HER2-positiv brystcarcinom, normal brystlignende subtype, PR-positiv brystkræft) for at bekræfte eller formelt afvise dem som modelbrus

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

