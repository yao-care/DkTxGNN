---
layout: default
title: Dienogest
parent: Moderat evidens (L3-L4)
nav_order: 142
evidence_level: L3
indication_count: 10
---

# Dienogest
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

# Dienogest: Fra endometriose til amenorre

## Enlineopsummering

Dienogest (Visanne®) er en fjerdegenerations syntetisk progestin med etableret klinisk verwendelse til **endometriose** i adskillige lande uden for Danmark.
TxGNN-modellen forudsiger, at det kan være effektivt til **amenorre**, med **4 kliniske forsøg** og **6 publikationer** hentet i relation til denne retning.
⚠️ Imidlertid er en kritisk mekanistisk modsætning identificeret: dienogests kernefarmakologiske virkning inducerer aktivt amenorre som et terapeutisk endepunkt — hvilket stærkt foreslår, at denne højt scorende prognose er et algoritmisk falsk positivt snarere end en genuine repurposing-mulighed.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Endometriose (udledt fra klinisk kontekst og forsøgsdata; ingen dansk markedsføringstilladelse registreret) |
| Forudsagt ny indikation | Amenorre (sygdom) |
| TxGNN-prognosescore | 99.71% |
| Evidensniveau | L3 |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne prognose rimelig?

> ⚠️ **Advarsel om mekanistisk modsætning — Sandsynligvis algoritmisk falsk positivt**

Detaljeret mekanisme-af-virkning-data er ikke tilgængelig fra DrugBank til denne vurdering. Baseret på etableret farmakologi er dienogest imidlertid en fjerdegenerations progestin med højt selektiv progesteronreceptor-agonistaktivitet og ingen østrogenisk aktivitet. Dens kernemekanisme for behandling af endometriose involverer undertrykkelse af LH-pulsatil sekretion, reducering af ovariål østradiolproduktion og inducering af endometrial atrofi via hypotalamisk-hypofysær-ovarial (HPO) aksen. Klinisk tjener **amenorre-raten som et primært effektivitetsendepunkt** i endometriose-forsøg — amenorre er den påtænkte farmakologiske konsekvens af behandling, ikke en sygdomstilstand, som dienogest er designet til at reversere.

Positionering af dienogest som behandling for amenorre (sygdom) skaber således en grundlæggende mekanistisk modsætning: **stoffet forårsager amenorre; det behandler det ikke**. TxGNN højprognosescoren (0.9971) stammer mest plausibelt fra tæt vidensgrafikonnektivitet mellem dienogest, HPO-aksen og menstruationscyklus-noder — en velkendt kilde til uspecifik, falsk-positiv scoring i grafbaserede modeller.

Den eneste teoretisk indirekte forbindelse ville involvere vurdering af menstruationsgenfinding *efter* ophør med dienogest hos kvinder med endometriose-relateret sekundær menstruationsdysfunktion. Imidlertid repræsenterer dette en post-behandlings farmakokinetisk observation, ikke en direkte terapi mekanisme rettet mod amenorre som en primær tilstand. Intet klinisk program er designet omkring denne hypotese.

---

## Evidens fra kliniske forsøg

> Alle hentet forsøg rekrutterede endometriose-patienter. Amenorre optræder i disse studier udelukkende som en rapporteret bivirkning, tolerabilitetendepunkt eller som en *baseline farmakologisk tilstand* bevidst induceret af dienogest — ikke som målsygdommen.

| Forsøgsnummer | Fase | Status | Rekruttering | Vigtige fund |
|---------|------|--------|------|---------|
| [NCT07164183](https://clinicaltrials.gov/study/NCT07164183) | Fase 3 | Rekrutterer | 290 | Multicetralt åbent-label RCT sammenlignende Indinol Forto® 200 mg vs Visanne® 2 mg (dienogest) til endometriose; ikke-mindreværdigheds-design; amenorre sandsynligvis fanget som et tolerabilitetsmål |
| [NCT02425462](https://clinicaltrials.gov/study/NCT02425462) | N/A (Observationel) | Afsluttet | 895 | Prospektivt observationelt kohorte af Visanne® hos asiatiske kvinder med endometriose på tværs af rutinekliniske indstillinger; livskvalitet som primært endepunkt; amenorre-rate dokumenteret som sekundært sikkerhed/tolerabilitetselement |
| [NCT04495855](https://clinicaltrials.gov/study/NCT04495855) | N/A (Observationel) | Afsluttet | 968 | Virkeligheds-observationelt studie af dienogest i endometriose-klinisk praksis; evaluerede symptomkontrol og langsigtet behandlingsresultater; amenorre registreret som en almindelig bivirkning |
| [NCT07204093](https://clinicaltrials.gov/study/NCT07204093) | N/A | Aktivt, ikke rekrutterer | 138 | Sammenligner transdermal østradiol add-back (med dienogest vs drospirenon) i endometriose; studie-design forudsætter eksplicit *dienogest-induceret amenorre som den farmakologiske baseline-tilstand, og tilføjer derefter østradiol for at mindske hypoøstrogeniske bivirkninger — dette bekræfter yderligere dienogest som en amenorre-*inducer*, ikke en behandling |

---

## Litteraturbevis

| PMID | År | Type | Journal | Vigtige fund |
|------|------|------|---------|---------|
| [39090694](https://pubmed.ncbi.nlm.nih.gov/39090694/) | 2024 | Systematisk oversigt + Bayesian analyse | BMC Pharmacology & Toxicology | Omfattende analyse af bivirkninger af dienogest i endometriose og adenomyose; amenorre bekræftet som den predominante rapporterede farmakologiske effekt, konsistent med dens virkningsmekanisme |
| [34405378](https://pubmed.ncbi.nlm.nih.gov/34405378/) | 2022 | Narrativ oversigt | Reviews in Endocrine & Metabolic Disorders | Gennemgår hormonel behandling af endometriose; bekræfter østrogenafhængighed og progesteronresistens som vigtige patogeniske faktorer; beskriver HPO-akses undertrykkelse af dienogest som den centrale terapeutiske mekanisme |
| [41329046](https://pubmed.ncbi.nlm.nih.gov/41329046/) | 2026 | Farmakologisk / mekanistisk studie | European Journal of Contraception & Reproductive Health Care | Demonstrerer høj inhibitionsforhold og transformationsindeks af dienogest 2 mg; understøtter inducering af amenorre og et hypoøstrogenisk miljø som det påtænkte farmakologiske formål i endometriose-behandling |
| [29161960](https://pubmed.ncbi.nlm.nih.gov/29161960/) | 2018 | Retrospektivt kohorte | Reproductive Sciences | Langsigtet effektivitet og sikkerhed af dienogest i ovarial endometrioma (N=514, 7 universitetes hospitaler); amenorre-rate og endometrioma-recidiv evalueret som vigtige resultater ved >12 måneders behandling |
| [34918698](https://pubmed.ncbi.nlm.nih.gov/34918698/) | 2021 | Sag rapport | Medicine | Sag rapport om ovarial granulosacelle-tumor hos en PCOS-patient; tangentielt relateret til ovarial hormonalfysiologi, men giver ingen evidens for dienogest-brug i amenorre |
| [40543564](https://pubmed.ncbi.nlm.nih.gov/40543564/) | 2025 | Oversigt / Imaging-studie | Journal of Pediatric and Adolescent Gynecology | Avanceret 3D- og VR-visualiseringstekniker for Müllerianske anomalier; behandler strukturelle årsager til amenorre, men indeholder ingen data relevant for dienogest som farmakologisk intervention |

---

## Oplysninger om det danske marked

Dienogest er i øjeblikket **ikke autoriseret til salg i Danmark**. Ingen markedsføringstilladelser er registreret hos Lægemiddelstyrelsen, og produktet har ingen markedstilstedeværelse.

Som reference har dienogest (som Visanne® 2 mg tabletter, Bayer AG) markedsføringstilladelse i Tyskland og adskillige andre EU-medlemsstater og er godkendt til endometriose i Japan, Sydkorea og Australien blandt andet. Enhver brug i Danmark ville i øjeblikket kræve en navngivet-patient- eller medfølende brugsansøgning til Lægemiddelstyrelsen.

---

## Sikkerhedsmæssige overvejelser

Se venligst det godkendte produktinformationsblad (SPC) — for eksempel det tyske eller EMA-registrerede Visanne® SPC — for fuld sikkerhedsinformation.

Advarsler, kontraindikationer og lægemiddelinteraktionsdata specifikt for den danske reguleringsmæssige kontekst var ikke tilgængelige til denne vurdering. Klinikere skal bemærke, at progestiner som en klasse bærer klassespecifikke overvejelser, herunder tromboembolisk risiko i relevante patientpopulationer, virkninger på knoglemineral-densitet med længerevarende brug og potentielle humør-relaterede bivirkninger.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
TxGNN-prognosen for amenorre som en ny indikation for dienogest vurderes som et **højpålideligt algoritmisk falsk positivt**. Dienogests etablerede farmakologiske mekanisme *forårsager* amenorre som et terapeutisk resultat i endometriose-behandling; der er intet biologisk eller klinisk grundlag for dets brug som behandling for amenorre som en primær sygdom. Alle fire hentet kliniske forsøg og den mest direkte relevant litteratur bekræfter dette omvendte forhold. Prognosescoren stammer sandsynligvis fra uspecifik HPO-akses netværksforbindelse i TxGNN-vidensgrafen snarere end et genuin drug-disease-terapeutisk forhold.

**For at fortsætte kræves følgende:**

- **Mekanistisk præcisering**: Definer, hvorvidt en specifik amenorre-undertype eksisterer (f.eks. anovulatorisk amenorre sekundær til kronisk østrogenoverskud), hvor progestogen aktivitet teoretisk kunne gendanne cykling — og bekræft, at dette er forskelligt fra dienogests undertrykkende mekanisme
- **MOA-datahentning**: Indhent komplette DrugBank MOA-indgang for dienogest, herunder progesteronreceptor-subtype (PRA/PRB) selektivitet og nedstrømssignalering i endometrium
- **Sikkerhedsdatahentning**: Download og tolkning af Visanne® SPC (Bayer AG) eller TFDA-pakkeseddel for at fuldføre sikkerhedsprofilering, herunder kontraindikationer og vigtige advarsler
- **Målrettet litteratursøgning**: Udfør en fokuseret PubMed-søgning for progestin-terapi specifikt indiceret til amenorre-behandling (ikke endometriose-behandling) for at identificere eventuelle præcedenser
- **Falsk-positivt flag**: Overvej kategorisering af denne prognose som et graft-artefakt falsk positivt i TxGNN-outputpipeline for at forhindre gentagelse i fremtidige kørsler; amenorre-progestin-knude-forbindelsen bør annoteres med retningsbestemthed (drug *inducerer* tilstand, ikke *behandler* den)

---

*Denne rapport genereres til forskningsformål udelukkende og udgør ikke medicinsk rådgivning. Alle drug repurposing-kandidater kræver prospektiv klinisk validering før enhver terapeutisk anvendelse. Data-afskæring: 2026-04-05.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

