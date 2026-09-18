---
layout: default
title: Omalizumab
parent: Moderat evidens (L3-L4)
nav_order: 321
evidence_level: L3
indication_count: 10
---

# Omalizumab
{: .fs-9 }

Evidensniveau: **L3** | Forudsagte indikationer: **10** stk.
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

# Omalizumab: Fra allergisk astma/nældefeber til bronkitis

## Sammenfatning på én sætning

Omalizumab (Xolair) er et humaniseret monoklonalt antistof mod IgE, hvis etablerede indikation ifølge litteraturen i denne evidenspakke er moderat til svær allergisk astma og kronisk spontan urticaria (CSU); der er endnu ikke til rådighed en formelt dansk/DrugBank-verificeret oprindelig indikationsregistrering. TxGNN-modellen forudsiger en ny anvendelse ved **bronkitis**, men de **2 kliniske forsøg** og **8 publikationer**, der i øjeblikket er knyttet til denne kandidat, består næsten udelukkende af astmadata, og modellens egen rationalisering markerer dette som sandsynligt værende et sygdomsmærkat/ontologi-mismatch snarere end direkte bronkitisevidens.

---

## Hurtigt overblik

| Element | Indhold |
|--------|---------|
| Oprindelig indikation | Ikke registreret i Danmark; internationalt indikeret for moderat til svær allergisk astma og kronisk spontan urticaria (ifølge litteratur i denne pakke) |
| Forudsagt ny indikation | Bronkitis |
| TxGNN forudsigelsesscore | 99.9992% |
| Evidensniveau | L3 |
| Danmarks markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

En struktureret virkningsmekanisme-registrering fra DrugBank er i øjeblikket markeret som et datakløft i denne pakke (DG002). Imidlertid er den vedhæftede litteratur i sig selv informativ: omalizumab er et rekombinant humaniseret monoklonalt antistof, der binder frit IgE og blokerer dets interaktion med høj-affinitets FcεRI-receptoren på mastceller og basofiler, hvilket reducerer efterfølgende allergisk luftveisinflamation (PMID 16222080, 11270941). Dette er medicinen's veludokumenterede mekanisme i allergisk astma.

På et rent patofysiologisk grundlag kunne denne mekanisme tænkeligvis udvides til luftvejstilstande med en eosinofilisk/allergisk komponent, såsom eosinofil bronkitis, da kronisk bronkitis og astma deler overlappende inflammatoriske veje og forekommer hyppigt samtidigt klinisk.

**Imidlertid bør denne rationalisering læses med forsigtighed.** Modellens egen `repurposing_rationale` noterer eksplicit, at de forsøg og litteratur, der returneres under "bronkitis"-mærket, er næsten udelukkende astmastudier (f.eks. NCT02477332 er et kronisk spontan urticaria-forsøg; litteratursettet inkluderer anmeldelser med titler som "Omalizumab i astma" og "Astmaforværringer hos voksne"), hvor kun en enkelt case-rapport (PMID 31478531) tangentielt refererer til bronkitis via en post-procedural komplikation. Dette mønster tyder på et sandsynligt kendskabsgraf-node-overlap mellem "bronkitis" og "astma" snarere end et ægte, uafhængigt understøttet genbrugssignal for bronkitis selv.

---

## Klinisk forsøgsbevis

| Forsøgsnummer | Fase | Status | Tilmelding | Vigtige fund |
|---------|------|------|------|---------|
| [NCT02049294](https://clinicaltrials.gov/study/NCT02049294) | Fase 2/3 | Afsluttet | 11 | Kortikosteroid-sparende effekt af omalizumab hos patienter med astma og vedvarende eosinofil bronkitis; meget lille stikprøve (relevansgrad B — faktisk befolkning er astma + eosinofil bronkitis, ikke kun bronkitis) |
| [NCT02477332](https://clinicaltrials.gov/study/NCT02477332) | Fase 2 | Afsluttet | 382 | Dosisfindingsstudium af QGE031 (ligelizumab, et anti-IgE-middel relateret til omalizumab) som add-on-terapi i kronisk spontan urticaria — sygdomspopulation matcher ikke bronkitis (relevansgrad C) |

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtige fund |
|------|-----|------|------|---------|
| [16222080](https://pubmed.ncbi.nlm.nih.gov/16222080/) | 2005 | Anmeldelse | Clinical reviews in allergy & immunology | Oversigt over omalizumab-godkendelse og post-godkendelseserfaringer; effektivitet etableret i moderat til svær vedvarende astma, ikke bronkitis |
| [21121874](https://pubmed.ncbi.nlm.nih.gov/21121874/) | 2011 | Kohortestudie/sikkerhedstudie | Current medical research and opinion | Samlet sikkerhedsanalyse af omalizumab hos børn med allergisk (IgE-medieret) astma |
| [35369622](https://pubmed.ncbi.nlm.nih.gov/35369622/) | 2022 | Kohorte | Postepy dermatologii i alergologii | Omalizumab hos ældre patienter med svær allergisk astma-COPD-overlap |
| [30196731](https://pubmed.ncbi.nlm.nih.gov/30196731/) | 2018 | Anmeldelse | Expert opinion on pharmacotherapy | Diskuterer røgfremkaldte luftvejssygdomme (kronisk bronkitis, emfysem) som komorbiditet med astma; ikke et omalizumab-effektivitetsstudium i bronkitis |
| [17663923](https://pubmed.ncbi.nlm.nih.gov/17663923/) | 2007 | Anmeldelse | Allergologia et immunopathologia | Generel anmeldelse af monoklonalt antistofbrug i pædiatri; nævner anti-IgE-terapi kun i forbifarten |
| [21163396](https://pubmed.ncbi.nlm.nih.gov/21163396/) | 2010 | Anmeldelse | Revue des maladies respiratoires | Fransk ekspertanmeldelse om astmaforværringer hos voksne; ikke bronkitis-specifik |
| [31478531](https://pubmed.ncbi.nlm.nih.gov/31478531/) | 2019 | Case-rapport | Journal of investigational allergology & clinical immunology | Sjælden tilfælde af plastisk bronkitis efter bronkial termoplasti (en enhedsprocedure); ingen omalizumab-behandlingsdata |
| [26466493](https://pubmed.ncbi.nlm.nih.gov/26466493/) | 2015 | Anmeldelse | Masui (Japanese J. Anesthesiology) | Perioperativ ledelsesanmeldelse af astma/kronisk bronkitis-patienter; nævner omalizumab som en astmamulighed kun |

---

## Markedsinformation for Danmark

Omalizumab har i øjeblikket **ingen markedsføringstilladelser på rekorden** i denne evidenspakke (`total_licenses: 0`, `market_status: Not marketed/Not marketed`), så ingen tilladelsestabel kan udfyldes. Bemærk, at dette afspejler de data, der er optaget i denne evidenspakke — omalizumab (Xolair®) har en centraliseret EU/EMA-markedsføringstilladelse for astma, CSU og kronisk rhinosinusitis med næsepolypper i andre jurisdiktioner; dette bør uafhængigt bekræftes i forhold til Det Danske Medicinstyrelsens produktregister.

---

## Sikkerhedshensyn

Se den godkendte Produktsammenfattelse (SmPC) for sikkerhedsinformation. Ingen strukturerede advarsler, kontraindikationer eller lægemiddel-vekselvirkningsdata blev returneret for denne kandidat (DDI-forespørgselsstatus: ikke fundet).

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Rationalisering:**
- Evidensniveauet er L3, og — vigtigere — det forsøg- og litteraturbevis, der er knyttet til "bronkitis"-mærket, er overvejende astmafokuseret, hvilket indikerer, at dette kan være et TxGNN-sygdomsnode-/ontologi-mappingartefakt snarere end et valideret, uafhængigt understøttet genbrugssignal for bronkitis.
- To strukturelle datakløfter blokerer yderligere evaluering: DG001 (Blocking) — ingen lokalt produktmærkat/advarsler til rådighed, så en sikkerhedsscreening (S1) kan ikke gennemføres; DG002 (High) — ingen bekræftet virkningsmekanisme-registrering fra DrugBank.
- Medicinen selv har nul markedsføringstilladelser registreret i Danmark, så der er ikke noget lokalt regulatorisk grundlag at bygge på.

**For at fortsætte er følgende nødvendig:**
- Bekræft, hvorvidt TxGNN "bronkitis"-sygdomsnoden er adskilt fra eller sammenlagt med "astma" i det underliggende kendskabsgraf, før dette behandles som en ny kandidat.
- Indhent dedikeret bronkitis-specifik (ikke astma-mærket) klinisk bevis, ideelt fra et kontrolleret forsøg i eosinofil eller kronisk bronkitis-populationer.
- Hent TFDA/dansk SmPC-advarsler og kontraindikationer (DG001) og en bekræftet DrugBank-virkningsmekanisme-registrering (DG002).
- I betragtning af at samme evidenspakke indeholder en materielt stærkere, direkte relevant kandidat — "obstruktiv luftvejssygdom" (dvs. svær allergisk astma), der bærer L1-bevis (flere afsluttede fase 3 RCT'er, f.eks. NCT00314574, n=850) og en "Fortsæt med guardrails"-anbefaling — bør den kandidat evalueres separat, da den ser ud til at være den sande kilde til de høj-kvalitets-forsøgsdata, der i øjeblikket er forkert tilskrevet bronkitis.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

