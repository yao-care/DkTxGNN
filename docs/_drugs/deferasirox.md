---
layout: default
title: Deferasirox
parent: Kun modelforudsigelse (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Deferasirox
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

# Deferasirox: Fra kronisk jernoverskud til HIV-infektionssygdom

## Resumé i én sætning

Deferasirox er en oral jernchelator, der bruges internationalt til kronisk jernoverskud på grund af hyppige blodtransfusioner (f.eks. ved β-thalassæmi og myelodysplastisk syndrom).
TxGNN-modellen forudsiger, at det kan være effektivt til **HIV-infektionssygdom**, med en prognose-score på 99,40%.
Aktuelt **0 kliniske forsøg** og **2 publikationer** understøtter denne retning — begge kun på præklinisk, mekanistisk niveau.

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Kronisk jernoverskud på grund af hyppige blodtransfusioner (transfusionsbetinget hemosiderosis) |
| Forudsagt ny indikation | HIV-infektionssygdom |
| TxGNN Prognose Score | 99,40% |
| Evidensniveau | L4 (kun prækliniske/mekanistiske studier) |
| Status på det danske marked | Ikke på markedet |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afhold |

---

## Hvorfor er denne prognose rimelig?

Detaljerede data om virkningsmekanisme fra DrugBank var ikke tilgængelige for denne rapport. Baseret på etableret farmakologi er deferasirox en oral jernchelator, der tages én gang dagligt og selektivt binder trivalent jern (Fe³⁺) med høj affinitet, hvilket fremmer jernafsondring via urin og fæces. Dens dokumenterede effektivitet til at reducere systemisk jernbelastning hos transfusionsafhængige patienter (β-thalassæmi, MDS) er grundlaget for denne hypotese om gentildelingspotentiale.

Jernmetabolisme spiller en grundlæggende rolle i HIV-1-replikationscyklus. Frit jern i endolysosomet letter korrekt foldning af HIV-1 Tat-proteinet, hvilket gør det muligt at transaktivere LTR-promotoren — et kritisk trin, der driver virale genudtrykt. Ved at chelere indre frit jern inden for endolysosomer kan deferasirox fremkalde unormal oligomerisering af HIV-1 Tat, hvilket dermed forstyrrer LTR-transaktivering og undertrykker viral replikation. Dette udgør en potentiel **vært-rettet antiviral terapi (HDT)**-mekanisme, som ikke overlapper med nogen eksisterende antiretroviral (ARV) medicin-target, hvilket tyder på teoretisk potentiale for kombinationsbrug.

Det må understreges, at denne mekanistiske hypotese udelukkende hviler på in vitro-bevis. Der er ikke genereret nogen dyremodel-studier eller humane kliniske data til dato. På dette stadium klassificeres prognosen bedst som et tidligt forskningsspørgsmål snarere end en kandidat til klinisk udvikling.

---

## Klinisk forsøgsbevis

Aktuelt ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtigste resultater |
|------|-----|------|-----------|-------------|
| [34550543](https://pubmed.ncbi.nlm.nih.gov/34550543/) | 2021 | In vitro mekanistisk studie | Journal of Neurovirology | Frit jern i endolysosomer fremmer HIV-1 Tat-medieret LTR-transaktivering; chelering af jern i endolysosomer øger HIV-1 Tat-oligomerisering og β-catenin-ekspression, hvilket begrænser viral transkriptionel aktivering — giver det primære mekanistiske rationalet for denne genuddelingsprognose |
| [16529348](https://pubmed.ncbi.nlm.nih.gov/16529348/) | 2006 | Medicin-oversigt / nyt medicin-resumé | Journal of the American Pharmacists Association | Narrativ oversigt over deferasirox ved første godkendelse; ingen direkte bevis for HIV-indikation, men kontekstualiserer medicinets farmakologiske profil |

---

## Information om det danske marked

Ingen markedsføringstilladelser for deferasirox blev identificeret i datasættet fra Lægemiddelstyrelsen (0 registrerede tilladelser).

> **Klinisk note:** Deferasirox (Exjade®, Jadenu®) har en centraliseret EMA-markedsføringstilladelse (EU/1/05/313), som gælder på tværs af alle EU/EØS-medlemsstater, herunder Danmark. Sundhedsprofessionelle bør verificere aktuel tilgængelighed, refusionsstatus og godkendte indikationer direkte hos Lægemiddelstyrelsen eller via EMA's produktinformationsportal.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

> Sikkerhedsdata (vigtige advarsler, kontraindikationer og lægemiddelinteraktioner) var ikke tilgængelige i dette Evidence Pack. Dette klassificeres som en **Blocking Data Gap** (DG001), der skal løses, før nogen klinisk sikkerhedsvurdering kan fortsætte. SmPC'et for Exjade®/Jadenu® er tilgængeligt via EMA-webstedet.

---

## Konklusion og næste trin

**Beslutning: Afhold**

**Begrundelse:**
Bevis er begrænset udelukkende til in vitro mekanistiske studier (Evidensniveau L4) uden kliniske forsøg og uden observationelle humane data. Hypotesen om jern-chelering / HIV-Tat-oligomerisering er biologisk sammenhængende, men helt uvalideret uden for cellekulturafsnittet, hvilket gør klinisk translation for tidlig på dette stadium.

**For at fortsætte, er følgende nødvendigt:**

- **Løs Blocking Data Gap (DG001):** Indhent og gennemse det fulde SmPC (advarsler, kontraindikationer, lægemiddel-lægemiddel-interaktioner), før nogen sikkerhed præ-screening kan fuldføres
- **Løs High-Priority Data Gap (DG002):** Bekræft deferasirox MOA via DrugBank API for at understøtte mekanistisk forbindelsesanalyse
- **In vivo-validering:** Dyremodel-studier (f.eks. HIV-inficerede humaniserede musemodeller), der demonstrerer antiviral aktivitet af deferasirox
- **DDI-vurdering med ARV-regimerter:** Evaluer farmakokinetiske interaktioner mellem deferasirox og standard antiretroviral medicin (f.eks. integrase-inhibitorer, protease-inhibitorer, NRTIer), især given deferasirox's kendte interaktioner med CYP3A4 og UGT-substrater
- **CNS-penetreringsdata:** I betragtning af relevansen til HIV-associeret neurokognitiv dysfunktion (HAND), som fremhæves i det mekanistiske papir, ville CNS farmakokinetisk profilering være påkrævet for denne indikation
- **Proof-of-concept klinisk studiedesign:** Hvis præklinisk validering er succesfuld, bør et Phase 1b/2a-tilførelsesstudium hos virologisk suppresseret PLHIV eller en behandlings-intensificeringsmodel defineres, før der går videre

---

*Denne rapport er genereret til forskningsformål og udgør ikke medicinsk rådgivning. Alle lægemiddel-genuddelingskandidater kræver klinisk validering før anvendelse til terapi.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

