---
layout: default
title: Perampanel
parent: Høj evidens (L1-L2)
nav_order: 345
evidence_level: L2
indication_count: 10
---

# Perampanel
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

# Perampanel: Fra Epilepsi (Fokal & Generaliseret Anfald) til Visuell Epilepsi

## Sammenfatning på Én Sætning

> Perampanel (DrugBank DB08883) er et velkendt anfaldshemmende lægemiddel, der allerede bruges internationalt til behandling af fokal-opstartede og primært generaliserede tonisk-kloniske anfald ved epilepsi.
> TxGNN-modellen forudsiger, at det også kan være effektivt til **Visuell Epilepsi**, en refleks-epilepsi-undertype udløst af visuelle stimuli,
> med **3 kliniske studier** og **20 publikationer**, der i øjeblikket er forbundet med denne kandidat — selvom ingen af dem specifikt undersøger visuell epilepsi.

---

## Hurtig Oversigt

| Emne | Indhold |
|------|------|
| Oprindelig Indikation | Ikke registreret i dansk regulatoriske data (ingen licenser på filen). Ifølge litteraturen i denne bevismappe er perampanel internationalt godkendt som supplerende/monoterapi til fokal-opstartede anfald (med eller uden sekundær generalisering) og som supplerende terapi til primært generaliserede tonisk-kloniske anfald (PMID 24559052) |
| Forudsagt Ny Indikation | Visuell Epilepsi |
| TxGNN Forudsigelsesscore | 99.92% |
| Bevisniveau | L2 |
| Dansk Markedsstatus | Ikke markedsført (Ikke markedsført) |
| Antal Markedsføringstilladelser | 0 |
| Anbefalet Beslutning | Hold |

---

## Hvorfor er Denne Forudsigelse Rimelig?

I øjeblikket er detaljerede virkningsmekanisme-data ikke tilgængelige fra DrugBank (markeret som datagab DG002, alvorlighed Høj). Imidlertid beskriver den kliniske litteratur, der er inkluderet i denne bevismappe, konsekvent perampanel som en selektiv, ikke-konkurrerende antagonist af AMPA (α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid) glutamat-receptorer (PMID 36150304, 24559052, 21635236). Ved at blokere AMPA-receptorformidlet postsynaptisk excitation, dæmper perampanel den kortikale hypereksitabilitet, der ligger til grund for anfaldsdannelse — grundlaget for dets godkendelse i over 35 lande som anfaldshemmende lægemiddel (AHL) til fokal-opstartede anfald og primært generaliserede tonisk-kloniske anfald (PMID 24559052).

Visuell epilepsi er en undertype af refleks-epilepsi, hvor anfald udløses af specifikke visuelle stimuli (f.eks. flimrende lys, kontrastmønstre). Fordi anfaldsdannelsesmekanismen i refleks-epilepsier — overdreven glutamaterg (AMPA-formidlet) kortical excitation — overlapper mekanistisk med fokal og generaliseret epilepsi, er det biologisk plausibelt, at en AMPA-receptor antagonist, der allerede er bevist effektiv ved epilepsi, også ville undertrykke anfald udløst af visuelle stimuli. Dette forstærkes af det faktum, at TxGNN genererede tæt beslægtede forudsigelser for flere andre refleks-/situationelle epilepsi-undertyper i samme kørselsrunde (audiogen anfald, startle epilepsi, spisningrelaterede anfald, miktionsudløst anfald, tænkerelaterede anfald, orgasme-udløst anfald), konsistent med en klassenivenmekanistisk effekt snarere end et sygdomspecifikt signal.

Det bør bemærkes, at ingen af de kliniske studier eller publikationer, der i øjeblikket er forbundet med denne kandidat, specifikt undersøgte "visuell epilepsi" som en defineret klinisk enhed — det underliggende bevis vedrører perampanels brug ved epilepsi bredt (partialt-opstartet og generaliseret anfald, EEG/neurofiziologi-effekter, pediatrisk og voksenbefolkning). Den mekanistiske begrundelse er derfor betydeligt stærkere end det direkte kliniske bevis for denne specifikke refleks-epilepsi-undertype.

---

## Klinisk Studiebevis

| Studiernummer | Fase | Status | Tilmelding | Vigtige Fund |
|---------|------|------|------|---------|
| [NCT03780907](https://clinicaltrials.gov/study/NCT03780907) | Fase 2 | Afsluttet | 18 | Randomiseret, dobbeltblindet, placebo-kontrolleret studie af tolerabilitet, sikkerhed og farmakokinetik for perampanel (E2007) hos patienter med refraktære partielle eller generaliserede anfald på samtidig AED-terapi |
| [NCT02900755](https://clinicaltrials.gov/study/NCT02900755) | Fase 4 | Afsluttet | 30 | Evaluerede kognitiv funktion og EEG-effekter af perampanel som supplerende behandling til refraktære fokal-opstartede anfald |
| [NCT03653741](https://clinicaltrials.gov/study/NCT03653741) | Fase 4 | Afsluttet | 12 | Vurderede perampanels effekter på EEG, somatosensoriske/hjernestamme auditive/visuelle fremkaldte potentialer hos sunde forsøgspersoner, for at bestemme, om det påvirker standard neurofiziologi-testning |

*Ingen af ovenstående studier rekrutterede specifikt patienter med visuell/fotosensitiv refleks-epilepsi; alle vedrører epilepsi generelt.*

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtige Fund |
|------|-----|------|------|---------|
| [36206645](https://pubmed.ncbi.nlm.nih.gov/36206645/) | 2022 | Systematisk Gennemgang & Meta-analyse (RCT'er) | Seizure | Samlet effektivitet og sikkerhed for perampanel ved epilepsi på tværs af randomiserede kontrollerede studier |
| [36878742](https://pubmed.ncbi.nlm.nih.gov/36878742/) | 2023 | Systematisk Gennemgang & Meta-analyse | Brain & Development | Effektivitet, tolerabilitet og sikkerhed for perampanel hos børn og unge med epilepsi |
| [25878177](https://pubmed.ncbi.nlm.nih.gov/25878177/) | 2015 | Samlet Fase 3 RCT-analyse | Neurology | Virkningen af samtidig enzym-inducerende AED'er på perampanels effektivitet/sikkerhed på tværs af de tre centrale Fase 3-studier |
| [24559052](https://pubmed.ncbi.nlm.nih.gov/24559052/) | 2014 | Gennemgang | Expert Opinion on Drug Discovery | Opdagelse og udvikling af perampanel; beskriver AMPA-receptor antagonist-mekanisme og godkendelses historik |
| [36150304](https://pubmed.ncbi.nlm.nih.gov/36150304/) | 2022 | Gennemgang (Klinisk Studie & Virkelighedsdata) | Epilepsy & Behavior | Opsummerer perampanel monoterapi-effektivitet på tværs af studie- og virkelighedsdata |
| [29898971](https://pubmed.ncbi.nlm.nih.gov/29898971/) | 2018 | Praksis Retningslinje | Neurology | AAN/AES retningslinje-opdatering om effektivitet/tolerabilitet af nyere AED'er (inklusive perampanel) til nyopstået epilepsi |
| [26111428](https://pubmed.ncbi.nlm.nih.gov/26111428/) | 2015 | Gennemgang | Expert Opinion on Drug Metabolism & Toxicology | Farmakokinetisk og farmakodynamisk evaluering af perampanel til fokal-opstartede anfald |
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematisk Gennemgang & Netværks Meta-analyse | Journal of Neurology | Sammenligner anfaldshemmende lægemidler, inklusive perampanel, til idiopatiske generaliserede epilepsier |
| [37684052](https://pubmed.ncbi.nlm.nih.gov/37684052/) | 2023 | Gennemgang | BMJ | Håndtering af epilepsi (inklusive AED sikkerhedsprofiler) under graviditet og amning |
| [41043235](https://pubmed.ncbi.nlm.nih.gov/41043235/) | 2025 | Prospektivt Multicenterstudie | Epilepsy & Behavior | Evaluerede perampanels effekt på anfaldskontrol og søvnkvalitet hos mennesker med epilepsi |

*10 af 20 tilgængelige publikationer vist, prioriteret efter bevisets kvalitet (systematiske gennemgange/meta-analyser og samlet Fase 3-data først). Ingen behandler specifikt visuell/fotosensitiv epilepsi.*

---

## Information om Dansk Marked

Der er ingen markedsføringstilladelser til stede i Bevisemappen for Danmark — `taiwan_regulatory.total_licenses = 0` og licenselisten er tom, med markedsstatus registreret som **Ikke markedsført (Ikke markedsført)**.

Dette berettiger verifikation: litteraturen i denne bevismappe angiver, at perampanel er "godkendt i over 35 lande... herunder medlemmerne af Den Europæiske Union" (PMID 24559052), som normalt ville omfatte Danmark via EMA centraliseret godkendelse. Fraværet af nogen dansk licensrecord bør derfor behandles som et muligt **dataindsamlingsgab** snarere end bekræftet ikke-tilgængelighed, og bør re-verificeres direkte mod Lægemiddelstyrelsen og EMA-registrene før endelig beslutningstagning.

---

## Sikkerhedshensyn

Se venligst det godkendte sammendrag af produktegenskaber (SmPC) for sikkerhedsinformation.

Der er ingen vigtige advarsler, kontraindikationer eller lægemiddel-lægemiddel-interaktions-data tilgængelige i denne bevismappe:
- `safety.key_warnings` og `safety.contraindications` indeholder kun "[Data Gap]" pladsholders.
- DDI-forespørgslen for PERAMPANEL returnerede `not_found` (0 interaktioner hentet).
- Dette er registreret som **DG001 (Blokeringsalvorlighed)** i bevisemappen: de manglende SmPC-advarsler/kontraindikations-data blokerer eksplicit indgang til S1 sikkerhed præ-vurdering.

---

## Konklusion og Næste Trin

**Beslutning: Hold**

**Begrundelse:**
- DG001 er et **Blokeringsalvorlighed**-datagab — TFDA/danske SmPC-advarsler og kontraindikationer er utilgængelige, hvilket per definition forhindrer sikkerhed præ-vurdering (S1) i at fortsætte.
- Der er i øjeblikket ingen markedsføringstilladelse på filen for Danmark (0 licenser), og denne status skal selv afstemmes mod medicinalstoffets kendte brede internationale godkendelse.
- Selvom AMPA-receptor antagonist-mekanismen giver stærk mekanistisk plausibilitet for refleks-epilepsi-undertyper, **ingen prøve eller publikation i bevisemappen undersøger specifikt visuell epilepsi** — alle tilgængelige bevis vedrører epilepsi generelt, så det kliniske bevisgrundlag for denne specifikke indikation forbliver indirekte.

**For at fortsætte, er følgende nødvendigt:**
- Løs DG001: indhent og analysér det godkendte SmPC (advarsler, forholdsregler, kontraindikationer) fra TFDA/Lægemiddelstyrelsen eller EMA
- Løs DG002: bekræft virkningsmekanisme via DrugBank API-forespørgsel
- Afstem "ikke markedsført / 0 licenser" status for Danmark mod medicinalstoffets kendte brede internationale godkendelse
- Kør DDI-forespørgslen igen (aktuel status: not_found) for at få en brugbar interaktionsprofil
- Søg efter eller bestil case series/studier, der specifikt handler om perampanel ved visuell eller andre refleks-epilepsi-undertyper, da det nuværende bevis støtter epilepsi bredt men ikke denne indikation specifikt

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

