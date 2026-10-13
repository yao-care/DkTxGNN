---
layout: default
title: Tazobactam
parent: Kun modelforudsigelse (L5)
nav_order: 796
evidence_level: L5
indication_count: 2
---

# Tazobactam
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

# Tazobactam: Fra bakteriel lungebetændelse til lungebetændelse (hospitalserhvervet/ventilatorassocieret) og urinvejsinfektion

## Resumé i én sætning

Tazobactam er en betalaktamasehæmmer, der altid gives i kombination med et betalaktamantibiotikum (fx piperacillin eller ceftolozan), og som oprindeligt anvendes mod bakteriel lungebetændelse, bughindebetændelse, blindtarmsbetændelse og stafylokokinfektioner.
TxGNN-modellen forudsiger, at lægemidlet også kan være virksomt ved **lungebetændelse** (score 99,5 %) og **urinvejsinfektion** (score 99,1 %).
Evidensen omfatter **20 kliniske forsøg og 20 publikationer for lungebetændelse** samt **5 kliniske forsøg og 17 publikationer for urinvejsinfektion**. Evidensen understøtter kombinationerne, ikke tazobactam alene.

*Bemærk: Lungebetændelse ligger tæt på den oprindelige indikation (bakteriel lungebetændelse), så prognosen er i høj grad en bekræftelse af eksisterende anvendelse snarere end ægte repurposing. Urinvejsinfektion er en egentlig udvidelse.*

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Bakteriel lungebetændelse, peritonitis, appendicitis, infektioner med *Staphylococcus aureus* (godkendelsesteksten for de danske tilladelser er ikke tilgængelig i de indsamlede data) |
| Forudsagt ny indikation | Lungebetændelse (pneumonia); sekundært: urinvejsinfektion |
| TxGNN-forudsigelsesscore | 99,5 % (lungebetændelse); 99,1 % (urinvejsinfektion) |
| Evidensniveau | L1 (begge indikationer) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 4 |
| Anbefalet beslutning | Proceed with Guardrails |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til denne rapport. Ud fra kendt viden er tazobactam en betalaktamasehæmmer, der hæmmer klasse A- og visse klasse C-betalaktamaser, herunder ESBL. Dermed beskyttes partnerantibiotikaet (piperacillin eller ceftolozan) mod nedbrydning, og aktiviteten genoprettes over for betalaktamaseproducerende gramnegative og nogle grampositive bakterier.

**Lungebetændelse:** Mekanismen er direkte relevant for hospitalserhvervet og ventilatorassocieret lungebetændelse, hvor gramnegative bakterier som *Pseudomonas aeruginosa* og Enterobacterales er hyppige. Forudsigelsen ligger tæt på den eksisterende indikation, og den høje score er i overensstemmelse hermed.

**Urinvejsinfektion:** Mange urinvejspatogener (*E. coli*, *Klebsiella*) producerer enzymer, som tazobactam hæmmer, så mekanismen er plausibel ved komplicerede urinvejsinfektioner. Piperacillin/tazobactam anvendes allerede klinisk til dette. Evidens fra ESBL-producerende blodbaneinfektioner antyder dog, at piperacillin/tazobactam kan være dårligere end carbapenemer, så overførsel til ESBL-urinvejsinfektion kræver forsigtighed.

---

## Klinisk evidens (kliniske forsøg)

### Lungebetændelse (udvalgte forsøg)

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT02070757](https://clinicaltrials.gov/study/NCT02070757) | Fase 3 | Afsluttet | 726 | Ceftolozan/tazobactam versus meropenem ved ventileret hospitalserhvervet lungebetændelse (ASPECT-NP); non-inferioritet på 28-dages dødelighed |
| [NCT02493764](https://clinicaltrials.gov/study/NCT02493764) | Fase 3 | Afsluttet | 537 | Imipenem/relebactam versus piperacillin/tazobactam ved HABP/VABP; piperacillin/tazobactam er komparator |
| [NCT00253955](https://clinicaltrials.gov/study/NCT00253955) | Fase 3 | Afsluttet | 460 | Levofloxacin 750 mg versus piperacillin/tazobactam ved mild til moderat hospitalserhvervet lungebetændelse |
| [NCT04223752](https://clinicaltrials.gov/study/NCT04223752) | Fase 1 | Afsluttet | 41 | Sikkerhed, tolerabilitet og farmakokinetik af ceftolozan/tazobactam hos børn med nosokomiel lungebetændelse |
| [NCT00438269](https://clinicaltrials.gov/study/NCT00438269) | Fase 2 | Afsluttet | 80 | Pilotforsøg om hensigtsmæssig antibiotisk behandling på intensivafdeling; indirekte relation til tazobactam |
| [NCT06972537](https://clinicaltrials.gov/study/NCT06972537) | Ikke angivet | Rekrutterer | 42 | Modelstyret versus empirisk dosering af piperacillin/tazobactam hos ældre med lungebetændelse |
| [NCT06977347](https://clinicaltrials.gov/study/NCT06977347) | Ikke angivet | Ikke rekrutterende endnu | 100 | Piperacillin/tazobactam alene versus kombineret med fluorquinolon ved svær samfundserhvervet lungebetændelse |
| [NCT01853982](https://clinicaltrials.gov/study/NCT01853982) | Fase 3 | Afbrudt | 4 | Ceftolozan/tazobactam versus piperacillin/tazobactam ved VAP; kun 4 deltagere, kan ikke understøtte konklusioner |
| [NCT03006679](https://clinicaltrials.gov/study/NCT03006679) | Fase 3 | Trukket tilbage | 0 | Meropenem-vaborbactam versus piperacillin/tazobactam; ingen deltagere, ingen data |
| [NCT04673175](https://clinicaltrials.gov/study/NCT04673175) | Fase 4 | Afbrudt | 17 | Ceftolozan/tazobactam ved *Pseudomonas*-infektioner hos patienter med blodkræft/stamcelletransplantation; begrænset værdi |

### Urinvejsinfektion

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT03687255](https://clinicaltrials.gov/study/NCT03687255) | Fase 3 | Afsluttet | 1043 | Cefepim-AAI101 (enmetazobactam) versus piperacillin/tazobactam ved kompliceret urinvejsinfektion; piperacillin/tazobactam er komparator |
| [NCT02728089](https://clinicaltrials.gov/study/NCT02728089) | Fase 3 | Afsluttet | 115 | Ukontrolleret japansk studie af ceftolozan/tazobactam ved kompliceret urinvejsinfektion og pyelonefritis |
| [NCT03230838](https://clinicaltrials.gov/study/NCT03230838) | Fase 2 | Afsluttet | 134 | Ceftolozan/tazobactam versus meropenem hos børn med kompliceret urinvejsinfektion |
| [NCT03891433](https://clinicaltrials.gov/study/NCT03891433) | Fase 4 | Suspenderet | 198 | Piperacillin/tazobactam versus carbapenemer ved ESBL-urinvejsinfektion uden bakteriæmi (CAPITIS) |
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | Ikke angivet | Afsluttet | 3520 | Farmakokinetik af underbelyste lægemidler hos børn; ikke specifik for urinvejsinfektion |

---

## Litteraturevidens

### Lungebetændelse (udvalgte publikationer)

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [31563344](https://pubmed.ncbi.nlm.nih.gov/31563344/) | 2019 | RCT | Lancet Infect Dis | ASPECT-NP: ceftolozan/tazobactam versus meropenem ved nosokomiel lungebetændelse |
| [32785589](https://pubmed.ncbi.nlm.nih.gov/32785589/) | 2021 | RCT | Clin Infect Dis | RESTORE-IMI 2: imipenem/relebactam versus piperacillin/tazobactam ved HABP/VABP |
| [39674398](https://pubmed.ncbi.nlm.nih.gov/39674398/) | 2025 | RCT | Int J Infect Dis | Fase 3 non-inferioritetsstudie af IMI/REL versus PIP/TAZ ved HABP/VABP |
| [38823453](https://pubmed.ncbi.nlm.nih.gov/38823453/) | 2024 | Systematisk review/netværksmetaanalyse | Clin Microbiol Infect | Empiriske antibiotikaregimer ved hospitalserhvervet lungebetændelse uden ventilator |
| [38971203](https://pubmed.ncbi.nlm.nih.gov/38971203/) | 2024 | Systematisk review | Int J Antimicrob Agents | PK/PD for nye betalaktamer ved lungebetændelse med carbapenemresistente gramnegative bakterier |
| [36543346](https://pubmed.ncbi.nlm.nih.gov/36543346/) | 2022 | Review | Eur Respir Rev | Nye antibiotika mod gramnegativ lungebetændelse |
| [35088403](https://pubmed.ncbi.nlm.nih.gov/35088403/) | 2022 | Review | Semin Respir Crit Care Med | Nye antibiotika til HAP og VAP |
| [32600375](https://pubmed.ncbi.nlm.nih.gov/32600375/) | 2020 | Review | Crit Care | Opdatering af behandling af nosokomiel lungebetændelse på intensivafdeling |
| [38902935](https://pubmed.ncbi.nlm.nih.gov/38902935/) | 2025 | Kohorte | Clin Infect Dis | Resistensudvikling ved ceftazidim-avibactam (40 %) versus ceftolozan-tazobactam (10 %) ved MDR *P. aeruginosa* |
| [38688353](https://pubmed.ncbi.nlm.nih.gov/38688353/) | 2024 | Review/retningslinje | Int J Antimicrob Agents | Praktisk tilgang til behandling af multiresistente gramnegative infektioner |

### Urinvejsinfektion (udvalgte publikationer)

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [36194218](https://pubmed.ncbi.nlm.nih.gov/36194218/) | 2022 | RCT | JAMA | Cefepim/enmetazobactam versus piperacillin/tazobactam: klinisk helbredelse og mikrobiologisk eradikering ved kompliceret UVI/pyelonefritis |
| [29486041](https://pubmed.ncbi.nlm.nih.gov/29486041/) | 2018 | RCT | JAMA | TANGO I: meropenem-vaborbactam versus piperacillin/tazobactam ved kompliceret UVI |
| [30861061](https://pubmed.ncbi.nlm.nih.gov/30861061/) | 2019 | RCT (fase 2/3) | Clin Infect Dis | ZEUS: fosfomycin i.v. versus piperacillin/tazobactam ved kompliceret UVI |
| [39817442](https://pubmed.ncbi.nlm.nih.gov/39817442/) | 2025 | Systematisk review/netværksmetaanalyse | J Comp Eff Res | Effekt af behandlingsmuligheder ved kompliceret UVI inkl. akut pyelonefritis |
| [40583996](https://pubmed.ncbi.nlm.nih.gov/40583996/) | 2025 | Systematisk review | JAC Antimicrob Resist | Klinisk effekt, sikkerhed og farmakokinetik for nye BL/BLI-kombinationer |
| [35787918](https://pubmed.ncbi.nlm.nih.gov/35787918/) | 2022 | Review | Int J Antimicrob Agents | Kliniske data for nye antibiotika mod multiresistente gramnegative infektioner |
| [30219824](https://pubmed.ncbi.nlm.nih.gov/30219824/) | 2019 | Review | Clin Infect Dis | Renal dosering af antibiotika, herunder ceftolozan/tazobactam |
| [29493397](https://pubmed.ncbi.nlm.nih.gov/29493397/) | 2018 | Review | Expert Rev Anti Infect Ther | Ceftolozan/tazobactam: plads i behandlingen |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| MA 28107303324 | Piperacillin/Tazobactam "B. Braun" | Pulver og solvens til infusionsvæske, opløsning | Ikke tilgængelig i de indsamlede data |
| MA 28105499514 | Zerbaxa (ceftolozan/tazobactam) | Pulver til koncentrat til infusionsvæske, opløsning | Ikke tilgængelig i de indsamlede data |
| MA 28106711921 | Piperacillin/Tazobactam "Antibiotice" | Pulver til infusionsvæske, opløsning | Ikke tilgængelig i de indsamlede data |
| MA 28104035606 | Piperacillin/Tazobactam "Reig Jofre" | Pulver til infusionsvæske, opløsning | Ikke tilgængelig i de indsamlede data |

Alle fire tilladelser er gyldige og injicerbare (intravenøs infusion).

---

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer er ikke indeholdt i de data, der er indsamlet til denne rapport. Der blev ikke fundet registrerede lægemiddelinteraktioner i de indsamlede data, men det bør ikke tolkes som fravær af interaktioner.

- **Sygdomme knyttet til kontraindikation i videnbasen (ikke fra produkttekst):** nyresygdom, pyoureter, neutropeni, agranulocytose, blodkoagulationsforstyrrelser, *Clostridium difficile*-colitis, perinatal nekrotiserende enterokolitis, infektiøs mononukleose og kronisk Epstein-Barr-virusinfektionssyndrom. Disse bør verificeres mod det godkendte produktresumé.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
- Der foreligger flere afsluttede fase 3-RCT'er for tazobactamholdige kombinationer ved lungebetændelse (fx ASPECT-NP med 726 deltagere) og ved kompliceret urinvejsinfektion, og kombinationerne er allerede markedsført i Danmark. Evidensen understøtter dog kombinationerne og ikke tazobactam alene, og i flere forsøg er piperacillin/tazobactam kun komparator.
- Lungebetændelse er tæt på den eksisterende indikation, mens urinvejsinfektion er en egentlig udvidelse, hvor ESBL-infektioner kræver forsigtighed.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméer fra Lægemiddelstyrelsen (godkendte indikationer, advarsler, kontraindikationer) – i de indsamlede data er dette mangelfuldt og blokerende for sikkerhedsscreening.
- Data om virkningsmekanisme (MOA) fra DrugBank.
- Afklaring af, om de forudsagte indikationer allerede er dækket af de eksisterende danske godkendelser.
- Vurdering af piperacillin/tazobactam versus carbapenemer ved ESBL-urinvejsinfektion, når resultater fra CAPITIS foreligger.
- Overvejelse af nyrefunktion og dosisjustering samt overvågning af blodbillede og koagulation hos udsatte patienter.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

