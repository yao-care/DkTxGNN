---
layout: default
title: Gadoteridol
parent: Kun modelforudsigelse (L5)
nav_order: 200
evidence_level: L5
indication_count: 10
---

# Gadoteridol
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

# Gadoteridol: Fra MRI-kontrastforstærkning til osteoarthritis-modtagelighed

## Sammenfatning i en sætning

Gadoteridol (ProHance®) er et ikke-ionisk, makrocyklisk gadolinium-baseret MRI-kontrastmiddel (GBCA), primært brugt intravenøst til at forbedre vævsvisualisering under MRI-undersøgelser.
TxGNN-modellen forudsiger, at det kan være relevant for **Osteoarthritis-modtagelighed**, med en forudsigelsesscore på **98.90%**; dog **findes der ingen kliniske forsøg og ingen understøttende terapeutisk litteratur** for denne indikation.
Den høje forudsigelsesscore afspejler højst sandsynligt en vidensgraf-netværks-artefakt – gadolinium-forbindelser bruges bredt til OA *diagnostisk* billedbehandling, hvilket skaber netværksnærhed til OA-noder, der ikke indikerer terapeutisk aktivitet.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | MRI-kontrastforstærkelse (ikke registreret i Danmark; baseret på etableret international klinisk brug) |
| Forudsagt ny indikation | Osteoarthritis-modtagelighed |
| TxGNN forudsigelsesscore | 98.90% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Indstilling |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkemekanisme er ikke tilgængelige i denne Evidence Pack. Baseret på etableret klinisk brug er Gadoteridol et ikke-ionisk, makrocyklisk gadolinium-chelat (Gd-HP-DO3A), der forstærker MRI-signalet ved at forkorte lokale T1-relaxationstider i omgivende væv. Dette giver mulighed for tydeligere afgrænsning af læsioner, inflammatorisk væv og vaskulære strukturer – det har ingen tilsigtet farmakologisk interaktion med sygdomsveje.

Den forudsagte indikation, *osteoarthritis-modtagelighed*, er en genetisk defineret fænotype, der beskriver arvelig prædisposition til OA – ikke aktiv ledsygdom. Gadoteridol har ingen kendt molekylære mål relevant for OA-patogenese: det interagerer ikke med enzymer for cartilago-matrixnedbrydning (MMP'er, ADAMTS), chondrocyt-signalkaskadrene eller nogen genetiske modtageligheds-loci. Én teoretisk undtagelse findes: frie Gd³⁺-ioner kan blokere mekanosensitive calciumkanaler (Piezo1, TRPV4), der er involveret i chondrocyt-biologi. Dog frigiver cheleret gadoteridol ubetydelige mængder frit Gd³⁺ ved kliniske doser, så denne mekanisme oversætter ikke til en troværdig terapeutisk hypotese.

Den mest plausible forklaring på TxGNN-scoren på 98.90% er en **vidensgraf-netværks-artefakt**. Gadolinium-baserede kontrastmidler optræder udstrakt i OA-forskningslitteraturen – for dobbelt- og tredobbelt-kontrast CT-vurdering af cartilago, MRI-evaluering af synovitis og proteinoglycanbedømmelse – hvilket skaber stærke indirekte graforbindelser til OA-relaterede noder. Modellen kan ikke skelne mellem "brugt til at studere" og "brugt til at behandle". Dette er en anerkendt begrænsning af graf-baserede repurposing-modeller, når diagnostiske billedbehandlings-midler er inkluderet i lægemiddel-noderne.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for Gadoteridol ved osteoarthritis-modtagelighed.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret terapeutisk litteratur tilgængelig for osteoarthritis-modtagelighed-indikationen.

> **Kontekstuel note – Osteoarthritis (rang 3, score 98.76%):** Tolv publikationer blev hentet, der forbinder Gadoteridol med osteoarthritis. Alle 12 artikler beskriver **udelukkende diagnostiske billedbehandlings-applikationer** – ikke terapeutiske interventioner. Gadoteridol bruges som det ikke-ioniske referencekontrast-middel i dobbelt- og tredobbelt-kontrast CT-protokoller til at kvantificere cartilago-proteinoglycana-indhold og vandfordeling. Udvalgte artikler er angivet nedenfor for at illustrere arten af eksisterende beviser.

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|---------|-------------|
| [32525582](https://pubmed.ncbi.nlm.nih.gov/32525582/) | 2020 | Ex vivo billedbehandling | J Orthop Res | Dobbelt-kontrast CT (jod CA4+ + gadoteridol) muliggør tidligere karakterisering af cartilago-degeneration end enkelt-kontrast; gadoteridol fungerer som ikke-ionisk referenceagent |
| [37593815](https://pubmed.ncbi.nlm.nih.gov/37593815/) | 2024 | Proof of concept | J Orthop Res | Tredobbelt-kontrast CT (BiNPs + CA4+ + gadoteridol) muliggør samtidig cartilago-segmentering og biomekansk vurdering i kadaver-knæled |
| [31068614](https://pubmed.ncbi.nlm.nih.gov/31068614/) | 2019 | Synchrotron-billedbehandling | Sci Reports | Synchrotron-microCT kvantificerer samtidig kationiske og ikke-ioniske kontrastmidler i ledbrusk; gadoteridol-diffusion afspejler vandindhold |
| [39622931](https://pubmed.ncbi.nlm.nih.gov/39622931/) | 2024 | Proof of concept | Sci Reports | Fotontællings-CT med dobbelt-kontrast-tilgang sporer gadoteridol-diffusion i oksebrusket over 72 timer; korrelerer med biomekanske egenskaber |
| [33692379](https://pubmed.ncbi.nlm.nih.gov/33692379/) | 2021 | Kvantitativ billedbehandling | Sci Reports | Fotontællings-CT vurderer ledbruskets sundhed ved hjælp af gadoteridol som ikke-ionisk kontrastmiddel |
| [30816584](https://pubmed.ncbi.nlm.nih.gov/30816584/) | 2019 | Præklinisk billedbehandling | J Orthop Res | Første anvendelse af klinisk full-body CT til dobbelt-kontrast cartilago-billedbehandling ved hjælp af gadoteridol; validerer diagnostisk tilgang |
| [31576504](https://pubmed.ncbi.nlm.nih.gov/31576504/) | 2020 | Ex vivo | Ann Biomed Eng | Tredobbelt-kontrast CT-metode evaluerer cartilago-sammensætning og muliggør segmentering; gadoteridol som ikke-ionisk komponent |
| [31535728](https://pubmed.ncbi.nlm.nih.gov/31535728/) | 2020 | Synchrotron-MicroCT | J Orthop Res | Dobbelt-kontrast-teknik med gadoteridol afslører fuldt kvantitativt potentiale for cartilago-sammensætnings-vurdering |
| [32767676](https://pubmed.ncbi.nlm.nih.gov/32767676/) | 2021 | Mekanistisk/diffusion | J Orthop Res | Cartilago-bestanddele (proteoglycaner, vand, collagen) påvirker samtidig diffusion af kationiske og ikke-ioniske agenter; hjælper med at fortolke diagnostisk nøjagtighed |
| [27161058](https://pubmed.ncbi.nlm.nih.gov/27161058/) | 2016 | Observationel | Eur J Radiol | Dynamisk kontrastforstærket MRI (gadolinium) vurderer peripatellær synovitis i knæ-OA og dens forbindelse til smerter |

---

## Markedsinformation for Danmark

Gadoteridol er **ikke i øjeblikket registreret eller markedsført i Danmark**. Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) markedsføringstilladelser blev identificeret for denne Evidence Pack.

Gadoteridol (ProHance®, Bracco) har regulatoriske tilladelser i andre jurisdiktioner, herunder USA (FDA) og EU (EMA). Klinikere, der har brug for dette kontrastmiddel, bør konsultere SmPC for det gældende godkendte produkt i den relevante jurisdiktion.

---

## Sikkerhedshensyn

Ingen lægemiddelspecifik sikkerhedsdata (advarsler, kontraindikationer eller lægemiddel-vekselvirkninger) var tilgængelig i denne Evidence Pack.

Venligst se den godkendte Summary of Product Characteristics (SmPC) for komplet sikkerhedsinformation.

> **Generelle sikkerhedshensyn for gadolinium-baserede kontrastmidler relevant for enhver repurposing-sammenhæng:**
> - **Nefrogen systemisk fibrose (NSF):** Gadolinium-chelater er kontraindikeret eller kræver særlig forsigtighed hos patienter med alvorlig nyrefunktionsnedsættelse (eGFR <30 mL/min/1.73 m²) eller akut nyresvigt. Makrocykliske midler som gadoteridol har lavere NSF-risiko end lineære midler, men risikoen er ikke nul.
> - **Gadolinium-vævsaflejring:** Gentagen eller høj-dosis GBCA-administration fører til akkumulering af gadolinium i knoglen, hjerne (særligt dentate nucleus og globus pallidus) og andre væv. Kliniske langsigtede konsekvenser er stadig under undersøgelse. Dette er et kritisk hensyn for ethvert hypotetisk kronisk terapeutisk doseringsskema.
> - **Overfølsomhed:** Anafylaktoid reaktioner er mulige, som med alle kontrastmidler.

---

## Konklusion og næste trin

**Afgørelse: Indstilling**

**Begrundelse:**
TxGNN-forudsigelsesscore på 98.90% for osteoarthritis-modtagelighed er næsten med sikkerhed en falsk positiv i vidensgraf: Gadoteridol er et *diagnostisk* billedbehandlings-middel uden farmakologisk mekanisme relevant for OA-patogenese, og dets hyppige fremkomst i OA-billedbehandlings-forskning skaber spuriøs netværksnærhed til OA-noder i vidensgraf. Der er ingen kliniske forsøg, ingen terapeutisk litteratur, ingen mekanistisk hypotese og ingen godkendt indikation, der understøtter repurposing af Gadoteridol som behandling for osteoarthritis-modtagelighed eller nogen muskuloskeletal sygdom.

**For at fortsætte ville følgende være nødvendigt:**

- Identificering af en biologisk plausibel terapeutisk mekanisme, der forbinder Gadoteridol (eller cheleret gadolinium) til OA-modtagelighedsveje – i øjeblikket fuldstændig fraværende
- Prækliniske in vitro/in vivo-studier, der demonstrerer terapeutisk virkning i OA- eller cartilago-sygdomsmodeller, bortset fra diagnostiske billedbehandlings-applikationer
- MOA-data fra DrugBank (DG002) til at verificere eller afvise nogen mekanistiske hypoteser, der involverer Gd³⁺-medieret ionkanal-modulering
- Sikkerhedsdata for kronisk/gentaget terapeutisk dosering, særligt vedrørende gadolinium-vævsaflejring (DG001 – TFDA/regulatorisk SmPC-data)
- En videnskabelig begrundelse, der forklarer, hvorfor TxGNN-forudsigelsen skal tages som et terapeutisk signal snarere end en diagnostisk billedbehandlings-artefakt

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

