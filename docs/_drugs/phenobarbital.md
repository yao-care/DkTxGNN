---
layout: default
title: Phenobarbital
parent: Kun modelforudsigelse (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
---

# Phenobarbital
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

# Phenobarbital: Fra epilepsi til trigeminalnervesvulst

## Ét-linjers resumé

Phenobarbital er et barbiturat historisk brugt til behandling af epilepsi, anfaldssygdomme og som sedat-hypnotikum.
TxGNN-modellens højest rangerede forudsigelse er **trigeminalnervesvulst** (score **99.96%**), men den eneste understøttende publikation beskriver faktisk en uafhængig tilstand (Sturge-Weber-syndrom), hvilket stærkt tyder på, at denne specifikke forudsigelse er et **kendskabsgraf-mappingartefakt snarere end et ægte lægemiddel-sygdomssignal**.
Andre lavere-score kandidater i samme batch (f.eks. audiogene anfald, prikkelseepilepsi) er mekanistisk mere plausible, men understøttet kun af præ kliniske/dyrestudier eller isolerede case reports.

---

## Hurtig oversigt

| Element | Indhold |
|------|------|
| Oprindelig indikation | Epilepsi / anfaldssygdomme (inkl. neonatale anfald), sedation — baseret på etableret farmakologisk klassifikation; ingen struktureret registreringspost blev returneret for dette felt |
| Forudsagt ny indikation | Trigeminalnervesvulst |
| TxGNN forudsigelsesscore | 99.96% |
| Bevisniveau | L5 (modelforudsigelse alene; understøttende litteratur matcher ikke sygdommen) |
| Danmark markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

En struktureret mekanisme-for-handling (MOA) post var ikke tilgængelig for dette lægemiddel i det aktuelle dataudtræk (datahul, høj alvorligheds grad).
Baseret på etableret farmakologi dokumenteret andre steder i denne bevismappe er phenobarbital en positiv allosterisk modulator af GABA‑A-receptoren, som fremkalder depression af centralt nervesystem og antikonvulsiv aktivitet, og det er også en kendt hepatisk CYP450-enzyminducer.
Der er ingen etableret antineoplastisk eller anti-neuralsvulst-mekanisme forbundet med denne lægemiddelklasse.

Forholdet mellem den oprindelige indikation (epilepsi/anfaldskontrol) og den forudsagte nye indikation (trigeminalnervesvulst) er ikke farmakologisk sammenhængende.
Det eneste litteraturcitat, der blev returneret for denne forudsigelse (PMID 9157801), er en kasusserie af **Sturge-Weber-syndrom** — et neurokutant vaskulært misdannelsessyndrom, der præsenterer sig med en ansigtsports-vinstain i trigeminalnervefordeling kombineret med anfald — som er en fundamentalt anderledes klinisk enhed end en "trigeminalnervesvulst".
Denne uoverensstemmelse er mest konsistent med en sygdomsontologi-mappingfejl inde i kendskabsgrafen (trigeminal-fordelingsfunktionen af Sturge-Weber-syndrom ser ud til at være blevet mappes til en neoplasme-relateret sygdomsknude).

Givet dette bør TxGNN-scoren på 99.96% for denne specifikke forudsigelse behandles med forsigtighed: den afspejler mest sandsynligt en mappingfejl snarere end en ægte farmakologisk association og bør ikke fremme uden først at korrigere eller gen-verificere det underliggende sygdomsknude-mapping.

---

## Klinisk prøvebevis

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtige fund |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Kasusserie | Anales españoles de pediatría | Gennemgang af 14 tilfælde af **Sturge-Weber-syndrom** — et vaskulært misdannelse/anfaldssyndrom, ikke en trigeminalnervesvulst. Sygdomsuoverensstemmelsen er grundlaget for at mistænke en kendskabsgraf-mappingfejl, der ligger til grund for denne forudsigelse. |

---

## Yderligere forudsagte indikationer i denne batch (lavere prioritet, ikke endnu formelt scoret)

Bevisp akken indeholdt ti rangerede forudsigelser, der kollapsede til seks forskellige kandidatsygdomme (flere rækker er duplikatposter for samme sygdom). Disse er ikke analyseret i detaljer her, men er noteret for fuldstændighed, da nogle bærer mere plausible mekanistiske begrundelser end overskriftsforudsigelsen ovenfor:

| Forudsagt indikation | TxGNN score | Bevisniveau | Anbefaling | Noter |
|---|---|---|---|---|
| Trigeminalnervesvulst | 99.96% | L5 | Afvent | Sandsynligvis KG-mappingartefakt (se ovenfor) |
| Audiogene anfald | 99.96% | L3 | Forskningsspørgsmål | GABAerg mekanisme plausibel; bevis er næsten helt præ klinisk/dyr (DBA/2 musemodeller); kun 1 menneskelig case report |
| Tankeudløste anfald | 99.96% | L3 | Forskningsspørgsmål | En reflex-epilepsi undertype; bevis er indirekte (generelle neonatale anfaldsvejledninger/RCT'er), ingen undersøgelse målretter denne undertype specifikt |
| Vandladningsudløste anfald | 99.96% | L4 | Afvent | Rent indirekte ekstrapolation fra generelt antiepileptisk bevis; ingen direkte undersøgelse identificeret |
| Prikkelseepilepsi / Hyperekpleksia | 99.96% | L4 | Forskningsspørgsmål | Mest mekanistisk sammenhængende kandidat — forbundet til GABA/glycin receptorpatofysiologi — men understøttet kun af case reports/genetiske studier, ingen phenobarbital-specifik undersøgelse |
| Spiseanfald | 99.96% | L4 | Afvent | Understøttet kun af en enkelt 50-årig case opfølgningsrapport |

Alle seks kandidater deler samme TxGNN-score band (~99.96%), hvilket tyder på, at modellen scorer disse som en klynge af "anfaldtype" sygdomsknuder snarere end at diskriminere meningsfuldt mellem dem — en yderligere grund til forsigtighed før behandling af enhver enkelt score som stærkt bevis.

---

## Danmark markedsinformation

Phenobarbital har i øjeblikket **ingen markedsføringstilladelse i Danmark** (0 licenser i arkiv; markedsstatus: Ikke markedsført).
Ingen nationale (Laegemiddelstyrelsen) eller centraliserede (EMA) tilladelsespost blev returneret i dette dataudtræk.

---

## Sikkerhedsovervejelser

Venligst henvises til det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.
Ingen strukturerede advarsler, kontraindikationer eller lægemiddel-lægemiddelinteraktionsdata var tilgængelige i det aktuelle bevismappe (DDI-forespørgsel returnerede ingen resultater).

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Begrundelse:**

- Overskriftsforudsigelsen (trigeminalnervesvulst) har ingen plausibel mekanistisk basis, og dens eneste understøttende citat beskriver et uafhængigt syndrom — hvilket indikerer en sandsynlig kendskabsgraf-mappingfejl snarere end et ægte lægemiddel-sygdomssignal.
- Phenobarbital markedsføres ikke i Danmark (0 tilladelser), og der eksisterer et **blokerings**-alvorligheds datahul for SmPC-niveau advarsler/kontraindikationer, hvilket i sig selv forhindrer enhver sikkerhed-præ-screening (trin S1) uanset den indikation, der overvejes.
- De mekanistisk mere troværdige alternative kandidater i denne batch (audiogene anfald, prikkelseepilepsi) understøttes kun af præ klinisk eller case-report-niveau bevis (L3–L4) og er ikke endnu klar til at komme videre end et forskningsspørgsmål.

**For at fortsætte er følgende nødvendig:**

- Bekræft og, hvis nødvendigt, korriger TxGNN sygdomsknude-mapping, der er ansvarlig for forudsigelsen "trigeminalnervesvulst" (sandsynligvis blandet sammen med Sturge-Weber-syndrom)
- Indhent det godkendte SmPC (advarsler, kontraindikationer) fra den danske Lægemiddelstyrelse eller et tilsvarende EMA-referenceprodukt for at lukke det blokerings-alvorligheds datahul
- Indhent en bekræftet mekanisme-for-handling post fra DrugBank
- Hvis du forfølger reflex-epilepsi kandidaterne (audiogene anfald, prikkelseepilepsi), få udarbejdet en målrettet litteraturgennemgang for at kontrollere for enhver menneskelig klinisk bevis ud over case reports
- Givet lægemidlets ikke-markedsførte status i Danmark, vurder gennemførligheden af en navngivet-patient/importvej før yderligere evalueringsinvestering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

