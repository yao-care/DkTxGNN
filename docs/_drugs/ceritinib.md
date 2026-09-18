---
layout: default
title: Ceritinib
parent: Kun modelforudsigelse (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Ceritinib
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

# Ceritinib: Fra ALK-positiv ikke-småcellet lungecancer til gingivalt fibrom

## Opsummering på én sætning

Ceritinib er en anden-generations oral ALK (anaplastisk lymfom kinase) tyrosinkinase hæmmer, internationalt godkendt til behandling af ALK-ændret ikke-småcellet lungecancer (NSCLC), men ikke i øjeblikket registreret i Danmark.
TxGNN-modellen forudsiger, at det kan have aktivitet i **gingivalt fibrom (fibrom, gingivalt)** med en forudsigelsesscore på **99.86%**; dog **ingen kliniske forsøg eller offentliggjort litteratur** understøtter i øjeblikket denne specifikke indikation.
Den biologiske rationel, der forbinder ceritinibs mekanisme til gingivalt fibrom, er begrænset, og den høje modelscore afspejler højst sandsynligt strukturelle mønstre inden for vidensgrafen snarere end ægte farmakologisk relevans.

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Original indikation | ALK-positiv ikke-småcellet lungecancer (NSCLC) — ikke registreret i Danmark; udledt fra offentliggjort litteratur |
| Forudsagt ny indikation | Fibrom, gingivalt |
| TxGNN forudsigelsesscore | 99.86% |
| Bevisniveau | L5 |
| Danmarks markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Ceritinib (Zykadia®, Novartis) er en potent anden-generations ALK-hæmmer først godkendt af US FDA i 2014 under Breakthrough Therapy-betegnelse for ALK-ændret NSCLC efter progression på crizotinib, og efterfølgende godkendt af EMA i 2015. Selvom fuldstændige mekanisme-af-virkning data ikke blev genfindet i denne bevissamling, dokumenterer offentliggjort litteratur konsistent ceritinibs primære mekanisme som kompetitiv hæmning af ALK-kinasedomænet med cirka 20-gange større potens end crizotinib, sammen med hæmmende aktivitet mod IGF1R, InsR og ROS1 kinaser. Flere fase 3-forsøg (herunder ASCEND-4) har bekræftet dets effektivitet i første-linje ALK-ændret NSCLC, og det er velkendt inden for denne terapeutiske kontekst globalt — selvom det ikke har opnået markedsføringstilladelse i Danmark.

Gingivalt fibrom er en sjælden, typisk arvelig sygdom karakteriseret ved progressiv overdreven vækst af gingivalt bindevæv. Dets kendte patogene gener — **SOS1, REST og KCNJ13** — har ingen etableret relation til ALK-signalering eller nogen af ceritinibs primære target kinaser. Selvom ceritinibs aktivitet ved IGF1R teoretisk kunne påvirke fibroblast-proliferationsveje, forbliver dette en rent spekulativ udledning uden nogen eksperimentel, præ-klinisk eller klinisk støtte.

Den ekstremt høje TxGNN-score (99.86%) for denne indikation afspejler højst sandsynligt **topologisk nærhed** mellem gingivalt fibrom-knuden og andre fibørse væv-relaterede sygdomsknuder inden for vidensgrafen, snarere end en ægte farmakologisk forbindelse. Dette er en anerkendt begrænsning af graf-baserede machine learning-modeller, hvor strukturel lighed i grafen kan give høje scores for sygdomspar uden meningsfuld biologisk relation, og fremhæver den kritiske vigtighed af ekspert mekanistisk gennemgang før enhver klinisk evaluering.

---

## Klinisk forsøgsbevis

Ingen relaterede kliniske forsøg er i øjeblikket registreret.

---

## Litteraturbevis

Ingen relateret litteratur er i øjeblikket tilgængelig.

---

## Cytotoxicitet

| Emne | Indhold |
|------|---------|
| Cytotoxicitets klassifikation | Målrettet terapi — anden-generations ALK tyrosinkinase hæmmer (ikke et konventionelt cytotoxisk middel) |
| Myelosuppression risiko | Lav (hæmatologisk toksicitet er sjælden; anæmi og neutropeni er blevet rapporteret ved lave frekvenser, væsentligt lavere end konventionel kemoterapi) |
| Emetogenitets klassifikation | Moderat (kvalme, opkastning og diarré er de mest hyppige uønskede bivirkninger på tværs af kliniske forsøg; antiemetisk profylakse og dosismodifikation kan være påkrævet) |
| Overvågningspunkter | Leverfunktionsprøver (ALT/AST — hepatotoksicitet risiko), pankreatiske enzymer (lipase/amylase — pankreatitis risiko), EKG (QTc forlængelse), fastende blodglukose (hyperglykæmi), lungefunktion / HRCT hvis respiratoriske symptomer opstår (interstitiel lungesygdom/pneumonitis) |
| Håndteringsbeskyttelse | Standard onkologi-medicinbehandling protokoller gælder; institutionelle cytotoxiske håndteringsprocedurer bør følges per lokale regler |

---

## Sikkerhedshensyn

Se venligst det godkendte resumé af produktkarakteristika (SmPC) — tilgængeligt via EMA (EU/1/15/1017) — for fuldstændig sikkerhedsinformation herunder kontraindikationer, advarsler og lægemiddelinteraktioner.

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Rationel:**
Der er ingen klinisk, præ-klinisk eller mekanistisk bevis, der forbinder ceritinib til gingivalt fibrom. Sygdommen er forårsaget af arvelige bindevævsgenanomalier (SOS1, REST og KCNJ13) uden relation til ALK-signalering, og TxGNN-modellens meget høje forudsigelsesscore afspejler vidensgrafs topologi snarere end biologisk plausibilitet. Fremskridt af denne kandidat kan ikke retfærdiggøres på nuværende bevis.

**For at fortsætte er følgende nødvendigt:**

- Indhentelse af fuldstændige mekanisme-af-virkning data fra DrugBank (DB09063) for at bekræfte det fuldstændige kinase-hæmningsprofil og eventuelle sekundære targets relevant for bindevævs biologi
- Præ-klinisk undersøgelse af, hvorvidt ALK eller IGF1R signaleringsvej-aktivitet spiller nogen rolle i gingivale fibroblasters proliferation eller fibromatosis patogenese
- Gennemgang af TxGNN sygdoms ontologien for at bestemme, hvorvidt "fibrom, gingivalt"-knuden deler strukturelle karakteristika med nogen sygdom, for hvilken ceritinib har etableret aktivitet
- Indhentelse af formel sikkerhedsdata fra Lægemiddelstyrelsen eller fuldt EMA SmPC for kontraindikationer, vigtige advarsler og lægemiddelinteraktionsprofil

---

> ⚠️ **Datakvalitet bemærkning — Rank 9–10 indikation (benign lungeneoplasme):**
> Indgangene "benign lungeneoplasme" ved rang 9–10 er forbundet med **20 PubMed publikationer**; dog behandler alle 20 artikler ALK-ændret **NSCLC** — en malignitet — og ikke benigne lungetumorer. Dette udgør en **kritisk uoverensstemmelse i sygdomsetiketten** i TxGNN sygdoms ontologien. Hvis node-etiketten var planlagt at fange ALK+ NSCLC, ville bevisniveauet opgradere til **L1** (fase 3 RCT ASCEND-4, PMID 28126333, *Lancet* 2017), og en dedikeret evaluering med en **"Fortsæt med sikkerhedsforanstaltninger"** anbefaling ville være berettiget. Denne uoverensstemmelse bør løses i ontologien før yderligere evaluering af hele kandidatlisten.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

