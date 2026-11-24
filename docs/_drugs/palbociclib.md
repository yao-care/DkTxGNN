---
layout: default
title: Palbociclib
parent: Kun modelforudsigelse (L5)
nav_order: 624
evidence_level: L5
indication_count: 4
last_modified_at: 2026-11-24
monitor_inn: "Palbociclib"
predicted_indications: ["hyperthyroidism", "rheumatoid arthritis", "thrombotic disease", "resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta"]
description: "Palbociclib: forudsagt ny indikation Hyperthyroidisme (hyperthyroidism) (evidensniveau L5). I Danmark, markedsføringstilladelser: 15 (gyldige: 15)"
---

# Palbociclib
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

## Palbociclib: Hyperthyroidisme (hyperthyroidism)
{: .text-alpha }

## Resumé i én sætning

Palbociclib er en CDK4/6-hæmmer, som er markedsført i Danmark som Ibrance (filmovertrukne tabletter). Den oprindelige godkendte indikationstekst er ikke tilgængelig i de data, der er indsamlet til denne rapport. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **hyperthyroidisme**, men der er **0 kliniske forsøg** og **0 publikationer** bag denne forudsigelse. Den er derfor udelukkende modelbaseret.

Bemærk: Den højest rangerede forudsigelse (hyperthyroidisme) har ingen understøttende evidens. Den bedst understøttede forudsigelse i datasættet er **leddegigt (rheumatoid arthritis)**, som er omtalt i et særskilt afsnit nedenfor.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Hyperthyroidisme (hyperthyroidism) |
| TxGNN-forudsigelsesscore | 0.9944 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 15 af 15) |
| Antal markedsføringstilladelser | 15 (gyldige: 15) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Palbociclib (uofficiel oversættelse): »Palbociclib er en hæmmer af cyklinafhængige kinaser (CDK) 4 og 6. Cyklin D1 og CDK4/6 befinder sig nedstrøms for signalveje, der fører til celleproliferation. In vitro reducerede palbociclib celleproliferationen i østrogenreceptor (ER)-positive brystkræftcellelinjer ved at blokere cellens progression fra G1- til S-fasen i cellecyklussen.« Engelsk originaltekst: "Palbociclib is an inhibitor of cyclin-dependent kinases (CDK) 4 and 6. Cyclin D1 and CDK4/6 are downstream of signaling pathways which lead to cellular proliferation. In vitro, palbociclib reduced cellular proliferation of estrogen receptor (ER)-positive breast cancer cell lines by blocking progression of the cell from G1 into S phase of the cell cycle." ([DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792), version af 2026-07-06; hentet 2026-11-19). Palbociclib tilhører klassen af CDK4/6-hæmmere, som hæmmer cellecyklussens progression og dermed celledeling.

Der er ikke noget i de foreliggende data, der kan forklare en sammenhæng mellem CDK4/6-hæmning og overskud af skjoldbruskkirtelhormon. Scoren på 0,9944 stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke biologisk evidens. Uden kliniske eller litteraturbaserede data kan forudsigelsen ikke vurderes som biologisk plausibel.

---

## Klinisk forsøgsevidens

Der findes i øjeblikket ingen relaterede kliniske forsøg registreret for hyperthyroidisme.

---

## Litteraturevidens

Der findes i øjeblikket ingen relateret litteratur for hyperthyroidisme.

---

## Øvrige forudsigelser i datasættet

| Rang | Sygdom | Score | Evidensniveau | Anbefaling |
|------|------|------|------|------|
| 1-2 | Hyperthyroidisme | 0,9944 | L5 | Hold |
| 3-4 | Leddegigt | 0,9936 | L4 | Forskningsspørgsmål |
| 5-6 | Trombotisk sygdom | 0,9932 | L5 | Hold |
| 7-8 | Thyreoideahormonresistens (THRB-mutation) | 0,9930 | L5 | Hold |

### Leddegigt: den mest understøttede forudsigelse (L4)

Der er ingen registrerede kliniske forsøg, men der findes indirekte evidens:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [33587021](https://pubmed.ncbi.nlm.nih.gov/33587021/) | 2021 | Case report | Modern Rheumatology Case Reports | Forbedring af leddegigt hos en brystkræftpatient behandlet med palbociclib |
| [40504547](https://pubmed.ncbi.nlm.nih.gov/40504547/) | 2025 | Kohortestudie | The Oncologist | Forekomst af eksisterende og nye immunmedierede sygdomme hos brystkræftpatienter i behandling med CDK4/6-hæmmere |
| [25165034](https://pubmed.ncbi.nlm.nih.gov/25165034/) | 2016 | Præklinisk (dyremodel) | Annals of the Rheumatic Diseases | CDK-hæmning af synovialfibroblaster lindrede sygdom i dyremodeller uden at svække den erhvervede immunitet; kombination med cytokinblokade øgede effekten |
| [39940918](https://pubmed.ncbi.nlm.nih.gov/39940918/) | 2025 | Præklinisk (dyremodel) | International Journal of Molecular Sciences | CDK6-afhængig synovial hyperplasi hos artritiske mus; palbociclib er undersøgt som mulig behandling |

Mekanismen (CDK4/6-drevet proliferation af synovialfibroblaster) er plausibel, men evidensen er indirekte (dyremodeller og ét case report). Det skal bemærkes, at CDK4/6-hæmmere kan give neutropeni og muligvis immunsuppression, hvilket kræver særlig sikkerhedsovervejelse hos patienter med leddegigt.

### Trombotisk sygdom: sikkerhedssignal, ikke behandlingsmulighed

Litteraturen (bl.a. PMID 36794339, 39083396, 39123221, 35300061) viser, at CDK4/6-hæmmere er forbundet med øget risiko for tromboembolisme. Forudsigelsen afspejler sandsynligvis en bivirkningsassociation og ikke en behandlingsmulighed. Anvendelse af palbociclib ved trombotisk sygdom understøttes ikke og kan være skadelig. Flere hentede artikler (fx PMID 40623899 om genterapi ved hæmofili B) er ikke relevante.

### Øvrige

Et cytostatisk kræftlægemiddel forventes ikke at korrigere en receptordefekt, og CDK4/6-hæmmere ville give sikkerhedsbekymringer i en udviklingsmæssig sammenhæng.

---

## Information om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106240019 | Ibrance | filmovertrukne tabletter | Palbociclib | Gyldig |
| 28106240119 | Ibrance | filmovertrukne tabletter | Palbociclib | Gyldig |
| 28106239919 | Ibrance | filmovertrukne tabletter | Palbociclib | Gyldig |
| 28105650215 | Ibrance | kapsler, hårde | Palbociclib | Gyldig |
| 28105650315 | Ibrance | kapsler, hårde | Palbociclib | Gyldig |

Tabellen viser 5 af 15 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (CDK4/6-hæmmer, cytostatisk) |
| Risiko for myelosuppression | Neutropeni og myelosuppression er kendte virkninger af CDK4/6-hæmmere (omtalt i præklinisk litteratur og sikkerhedsstudier) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC); blodtal er relevant på grund af risiko for neutropeni |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (interaktionsdatabasen rapporterer i alt 100 interaktioner; et udvalg af de vigtigste vises her):

- **Alvorlig (Major):** clarithromycin, cobicistat, deferipron, samarium (153Sm) lexidronam
- **Moderat:** aprepitant, dexamethason, cimetidin, saxagliptin, eliglustat, metreleptin, miconazol, nitisinon, cisaprid, clotrimazol, simvastatin, troglitazon, deferasirox, strontiumchlorid Sr-89, cilostazol
- **Mindre (Minor):** prucalopride

**Øvrige sikkerhedssignaler fra litteraturen:** øget risiko for tromboembolisme, interstitiel lungesygdom og myelosuppression ved CDK4/6-hæmmere.

For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om hyperthyroidisme er udelukkende modelbaseret (L5) uden kliniske forsøg, litteratur eller en kendt mekanistisk sammenhæng. Af de forudsagte indikationer er kun leddegigt (L4) et rimeligt forskningsspørgsmål, mens trombotisk sygdom snarere er et sikkerhedssignal.

**For at komme videre er følgende nødvendigt:**
- Data om virkningsmekanisme (MOA) og den danske godkendte indikationstekst
- Advarsler og kontraindikationer fra produktresuméet (SmPC)
- For leddegigt: kontrollerede kliniske studier og en vurdering af risikoen for neutropeni og immunsuppression
- Ingen videre undersøgelse af hyperthyroidisme, trombotisk sygdom, thyreoideahormonresistens eller brachydaktyli-syndaktyli-syndrom, medmindre der fremkommer ny evidens

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Ibrance (palbociclib) prescribing information, U.S. Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89a142d5-7e61-48bf-9e77-e2cd124c4792) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

