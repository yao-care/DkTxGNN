---
layout: default
title: Iloprost
parent: Høj evidens (L1-L2)
nav_order: 225
evidence_level: L1
indication_count: 10
---

# Iloprost
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

# Iloprost: Fra Pulmonal Arteriel Hypertension til HIV-Associeret Pulmonal Arteriel Hypertension

## Sammenfatning på en sætning

Iloprost er et syntetisk prostacyclin (prostanoid) analogon oprindeligt anvendt til behandling af pulmonal arteriel hypertension (PAH). Blandt de vurderede indikationsalternativ, hvor TxGNN-modellen har den højeste tillid med faktiske understøttende beviser, peger højest på **HIV-associeret pulmonal arteriel hypertension**, understøttet af **1 gennemført fase 3 randomiseret kontrolleret forsøg (n=64)** og **4 understøttende publikationer**. Det skal dog bemærkes, at modellens højest scorende prediktion samlet set (hårlødhed simplex på scalp) har **nul kliniske forsøg og nul litteraturbevis** og er markeret i den underliggende analyse som sandsynlig viden-graf-støj snarere end et ægte signal.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|----------|
| Oprindelig indikation | Pulmonal Arteriel Hypertension (WHO Gruppe 1, primær/idiopatisk) — udledt fra rationale for genbrugsteknologi; ikke bekræftet via dansk licensdata (se Danmark-markedsinformation) |
| Prædikteret ny indikation | HIV-Associeret Pulmonal Arteriel Hypertension |
| TxGNN-prædikte score | 99.21% |
| Evidensniveau | L1 |
| Danmark-markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Fortsæt med forholdsregler |

---

## Vurderede indikationsalternativ

Denne evidenspakke vurderede flere prædikterede indikationer for iloprost. For at sikre transparens opsummeres alle forskellige kandidater nedenfor (dubletter af KG/DL-poster samlet):

| Sygdom | TxGNN-score | Evidensniveau | Beslutningsstadium | Anbefaling |
|--------|------------|-----------------|-----------------|-----------------|
| HIV-associeret PAH | 99.21% | L1 | S3 | Fortsæt med forholdsregler |
| PAH associeret med bindevævssygdom | 99.21% | L3 | S2 | Forskningsspørgsmål |
| PAH associeret med medfødt hjertesygdom | 99.32% | L3 | S2 | Forskningsspørgsmål |
| Pulmonal arteriovenøs malformation | 99.31% | L4 | S0 | Pause |
| Medfødt hårlødhed milia | 99.33% | L5 | S0 | Pause |
| Hårlødhed simplex af scalp | 99.45% | L5 | S0 | Pause |

De to hårlødhedsrelaterede prædiktioner bærer de *højeste* rå TxGNN-scores, men har ingen mekanistisk plausibilitet, ingen forsøg og ingen litteratur — den underliggende analyse tillægger dette eksplicit embedding-støj på sjældne-sygdoms-noder. Denne rapport fokuserer derfor på **HIV-associeret PAH**, kandidaten med det stærkeste faktiske kliniske bevis.

---

## Hvorfor er denne prediktion rimelig?

Detaljerede mekanisme-for-handling data for iloprost er ikke tilgængelig i denne evidenspakke (datahuller, DrugBank-forespørgsel afventer løsning). Baseret på de tilgængelige oplysninger er iloprost et prostacyclin (IP-receptoragonist) analogon, hvis farmakologi producerer pulmonal vasodilatation og hæmning af blodpladesamling/vaskulær glat muskulatur proliferation. Det er en etableret behandling for primær (idiopatisk) PAH.

HIV-associeret PAH klassificeres sammen med idiopatisk PAH under WHO Gruppe 1 pulmonal arteriel hypertension. Begge deler samme underliggende patofysiologi — pulmonal vaskulær endotelial dysfunktion, glat muskulatur proliferation og progressiv vaskulær ombygging — som er det farmakologiske mål for prostacyclin-analoger. Fordi iloprost allerede er godkendt til den mekanistisk identiske moderindikation (idiopatisk PAH), repræsenterer dets udvidelse til HIV-associeret PAH brug inden for samme lægemiddelklasse for en tæt relateret sygdomsmekanisme, snarere end et spekulativt tværsygdoms-spring.

I modsætning hertil er de to relaterede kandidater — PAH associeret med medfødt hjertesygdom og PAH associeret med bindevævssygdom — også WHO Gruppe 1-undertypetyper med plausibel mekanistisk overlapning, men deres understøttende bevis er svagere (observationelt/review-niveau, L3), og i tilfældet med medfødt hjertesygdom er sygdomsprocessen drevet af en strukturel shunt snarere end primær vaskulær patologi, så reaktion kan afvige fra idiopatisk PAH.

---

## Klinisk forsøgsbevis

| Forsøgsnummer | Fase | Status | Enrolment | Vigtigste resultater |
|---------|------|------|------|---------|
| [NCT00709956](https://clinicaltrials.gov/study/NCT00709956) | Fase 3 | Gennemført | 64 | Multicenterstudie, double-blind, randomiseret, placebo-kontrolleret crossover-studie af en enkelt dosis inhaleret iloprost på arbejdskapacitet hos patienter med symptomatisk PAH, der inkluderede idiopatisk, familiær, HIV-associeret og lægemiddel/toksisk-induceret PAH (NYHA klasse II–IV), oven på stabil baggrundsbehandling (bosentan, ambrisentan eller sildenafil). |

*Understøttende forsøg for en relateret kandidat (PAH associeret med medfødt hjertesygdom):* [NCT01383083](https://clinicaltrials.gov/study/NCT01383083) — Fase N/A, status Ukendt, n=42, vurderer sikkerhed, tolerabilitet og hæmodynamiske effekter af iloprost hos voksne med Eisenmenger-fysiologi PAH. Forsøgsfuldførings-/rapporteringsstatus er ubekræftet, hvilket begrænser dets bevismæssige vægt.

---

## Litteraturbevis

| PMID | År | Type | Journal | Vigtigste resultater |
|------|-----|------|------|---------|
| [31090367](https://pubmed.ncbi.nlm.nih.gov/31090367/) | 2019 | Kohorte/Register | Terapevticheskii arkhiv | Seks års national PAH-registeranalyse af prevalens, klinisk forløb og nuværende terapi på tværs af PAH-undergrupper, herunder associerede former. |
| [18260882](https://pubmed.ncbi.nlm.nih.gov/18260882/) | 2007 | Oversigt | Kardiologiia | Oversigtsserier over kontrollerede forsøg af prostacyclin og dets syntetiske analoger (herunder iloprost) i idiopatisk PAH og PAH associeret med bindevævssygdom, medfødt hjertesygdom og HIV-infektion. |
| [17195895](https://pubmed.ncbi.nlm.nih.gov/17195895/) | 2006 | Oversigt | The Mount Sinai Journal of Medicine | Overblik over HIV-relateret pulmonal hypertension: estimeret incidensrate ~0,5% af HIV-inficerede individer, ukendt patogenese, variabel præsentation fra dyspnø til synkope. |
| [14720012](https://pubmed.ncbi.nlm.nih.gov/14720012/) | 2003 | Oversigt | American Journal of Respiratory Medicine | Oversigt over prostanoid-terapi for PAH, der eksplicit grupperer HIV-associeret PAH med idiopatisk PAH og andre associerede former som deler næsten identisk obstruktiv pulmonal mikrovaskular patologi. |

---

## Danmark-markedsinformation

Iloprost har i øjeblikket **ingen markedsføringstilladelse registreret i Danmark** i denne evidenspakke (0 licenser registreret, markedsstatus "Ikke markedsført"). Ingen Lægemiddelstyrelsen national godkendelse eller EMA centraliseret godkendelsesrekord er tilgængelig i datasættet til at opsummere doseringsformer eller godkendt indikationstekst.

---

## Sikkerhedsovervejelser

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformation. Ingen strukturerede advarsler, kontraindikationer eller lægemiddel-lægemiddel vekselvirkning data blev returneret af de tilgængelige forespørgsler i denne evidenspakke.

---

## Konklusion og næste trin

**Beslutning: Fortsæt med forholdsregler** *(gælder specifikt for HIV-associeret PAH-indikationen)*

**Begrundelse:**
Et gennemført fase 3 randomiseret kontrolleret forsøg (n=64), der evaluerer iloprost i en PAH-population, som omfattede HIV-associerede patienter, sammen med konsistent mekanistisk og review-niveau litteraturunderstøttelse, giver denne indikation det stærkeste evidensgrundlag (L1) blandt alle kandidater i denne pakke. De andre WHO Gruppe 1-kandidater (medfødt hjertesygdom-, bindevævssygdom-associeret PAH) forbliver i "Forskningsspørgsmål"-status (L3) i påvente af stærkere forsøgsniveau-data, og de to hårlødhedsrelaterede prædiktioner bør holdes som sandsynlige modelartefakter uden understøttende bevis.

**For at fortsætte er følgende nødvendigt:**
- Dansk/EU-label sikkerhedsadvarsler og kontraindikationer for iloprost — dette er i øjeblikket en **blokerende** datahul, der forhindrer indgang til S1 sikkerhedspræ-vurderingsstadium.
- Detaljeret mekanisme-for-handling data (DrugBank MOA) for formelt at understøtte den mekanistiske rationale.
- Undergruppeniveau resultater fra NCT00709956 specifikt for HIV-associeret PAH-kohorte, da forsøgspopulationen var blandet (idiopatisk, familiær, HIV-associeret og lægemiddel/toksisk-induceret PAH).
- Lægemiddel-lægemiddel vekselvirkning data med antiretroviral terapi (ART), givet målpopulationen — DDI-forespørgslen for iloprost returnerede ingen resultater.
- Bekræftelse af dansk/EU markedsføringsautoriseringssti, da iloprost i øjeblikket ikke er registreret som markedsført i Danmark.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

