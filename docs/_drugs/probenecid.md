---
layout: default
title: Probenecid
parent: Moderat evidens (L3-L4)
nav_order: 361
evidence_level: L4
indication_count: 6
---

# Probenecid
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **6** stk.
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

# Probenecid: Fra urikosurisk middel til renal hypourikæmi (modelforudsigelse)

## Resumé

Probenecid er et urikosurisk lægemiddel, der øger nyrernes udskillelse af urinsyre og dermed sænker serumurat. TxGNN-modellen forudsiger, at det kan have effekt ved **renal hypourikæmi**, men der er **ingen kliniske forsøg** og **20 publikationer**, som næsten udelukkende er case reports og oversigtsartikler. Litteraturen støtter ikke probenecid som behandling, og mekanismen peger snarere på en risiko for forværring. Forudsigelsen vurderes som sandsynligt et artefakt fra vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige danske registerdata |
| Forudsagt ny indikation | Renal hypourikæmi (hypouricemia, renal) |
| TxGNN-forudsigelsesscore | 99,73 % |
| Evidensniveau | L4 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i Evidence Pack. Ud fra den mekanistiske vurdering i materialet hæmmer probenecid urattransportørerne URAT1 (SLC22A12) og OAT1/OAT3. Det øger nyrernes udskillelse af urat og sænker serumurat.

Hereditær renal hypourikæmi skyldes oftest funktionstabsmutationer i SLC22A12 (URAT1) eller SLC2A9 (GLUT9). Nyrerne taber altså allerede urat. Et lægemiddel, der yderligere hæmmer genoptagelsen af urat, ville forventeligt **forværre** tilstanden. Det kan øge risikoen for uratnefropati, nyresten og motionsudløst akut nyresvigt. Forbindelsen skyldes sandsynligvis, at lægemidlet og sygdommen deler urattransport-entiteter i vidensgrafen. Den høje score (0,997) understøttes ikke af nogen terapeutisk evidens.

I den fundne litteratur optræder probenecid som **diagnostisk/farmakologisk redskab** til at undersøge nyrernes urathåndtering, for eksempel ved at teste, om urinsyreudskillelsen reagerer på lægemidlet. Det er ikke beskrevet som behandling.

**Øvrige forudsigelser for probenecid:**
- **Lesch-Nyhan syndrom** (score 99,39 %, L4): HPRT-mangel giver purinoverproduktion og hyperurikæmi. Urikosurika øger urinsyrebelastningen i urinen hos overproducenter og dermed risikoen for nyresten. Xanthinoxidasehæmmere (fx allopurinol) er standardbehandling, og probenecid adresserer ikke de neuroadfærdsmæssige og motoriske symptomer. Der er ingen kliniske forsøg, og litteraturen er historisk, indirekte eller beregningsbaseret.
- **Partiel HPRT-mangel** (score 99,37 %, L5): Samme forbehold gælder. Der er hverken kliniske forsøg eller litteratur, så der er kun tale om en modelforudsigelse.

Dublerede poster for de tre sygdomme er slået sammen.

---

## Klinisk evidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Tabellen viser de 10 mest relevante af i alt 20 publikationer for renal hypourikæmi.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Oversigtsartikel | Molecular Genetics and Metabolism | Hereditær renal hypourikæmi skyldes oftest funktionstabsmutationer i SLC22A12 (URAT1) |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Oversigtsartikel | Clinical Rheumatology | Opdateret gennemgang af årsager til hypourikæmi (serumurat < 2 mg/dL) til reumatologer |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Kohorte (klinisk og genetisk) | J Am Soc Nephrol | SLC22A12 sekventeret hos 32 japanske patienter, og sammenhæng mellem URAT1-genet og urinsyreudskillelse |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Case report med litteraturgennemgang | Am J Kidney Dis | Forebyggelse af motionsudløst akut nyresvigt ved renal hypourikæmi |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Case report | Am J Kidney Dis | To brødre med hereditær renal hypourikæmi og motionsudløst akut nyresvigt |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Case report (mekanistisk) | Nephron | Ingen respons på hverken pyrazinamid eller probenecid, hvilket tyder på en ny type renal hypourikæmi |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Case report | Nephron | Urataudskillelsen blev paradoksalt nedsat af probenecid |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case report | Nephron | Svækket respons på probenecid og pyrazinamid tyder på defekt i tubulær urat-reabsorption |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Probenecid og benzbromaron øgede urat-clearance (diagnostisk brug). Urolithiasis blev behandlet med alkalisering af urinen |
| [9510398](https://pubmed.ncbi.nlm.nih.gov/9510398/) | 1998 | Patientserie | Internal Medicine | Risikofaktorer for hæmaturi hos 16 japanske patienter med renal hypourikæmi |

Ingen af publikationerne viser, at probenecid behandler renal hypourikæmi.

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100744876 | Probenecid "Medic" (Viatris ApS) | Tabletter | Indikationstekst ikke angivet i data |

---

## Sikkerhedsovervejelser

Der er ikke fundet data om advarsler, kontraindikationer eller interaktioner i Evidence Pack. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Forudsigelsesspecifikke risici ved brug af probenecid ved de forudsagte sygdomme, ud fra mekanismen:
- **Renal hypourikæmi:** risiko for uratnefropati, nyresten og motionsudløst akut nyresvigt.
- **Lesch-Nyhan syndrom og partiel HPRT-mangel:** øget urinsyrebelastning i urinen og dermed øget risiko for urinsyrenyresten og nefropati.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Den høje TxGNN-score støttes ikke af terapeutisk evidens. Der er ingen kliniske forsøg, og litteraturen består af case reports og oversigtsartikler, hvor probenecid kun er brugt som diagnostisk redskab. Mekanismen taler for en risiko for forværring frem for gavn.

**For at komme videre kræves:**
- Sikkerhedsoplysninger (advarsler og kontraindikationer) fra Lægemiddelstyrelsens produktresumé, da disse mangler.
- Oplysninger om den godkendte indikation for Probenecid "Medic" og om virkningsmekanismen (fx fra DrugBank).
- Et fagligt review, der bekræfter, om forbindelsen blot er et artefakt i vidensgrafen, før der foretages yderligere evaluering.
- Foreløbig bør Lesch-Nyhan syndrom og partiel HPRT-mangel heller ikke prioriteres, da xanthinoxidasehæmmere er standardbehandling, og probenecid kan øge risikoen for nyresten.

*Resultaterne er kun til forskningsformål og udgør ikke medicinsk rådgivning. Forudsigelser fra modellen kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

