---
layout: default
title: Caffeine
parent: Moderat evidens (L3-L4)
nav_order: 147
evidence_level: L4
indication_count: 10
last_modified_at: 2026-10-14
description: "Caffeine: forudsagt ny indikation Næsehulesygdom (nasal cavity disease) (evidensniveau L4). Oprindelig indikation: Ikke angivet i de danske markedsføringstilladelser. Den videnbaserede…"
monitor_inn: "caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "acute laryngopharyngitis", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Koffein: Fra migræne og hovedpine til næsehulesygdom

## Opsummering

Koffein er et metylxanthin, som i Danmark bruges i receptfrie kombinationspræparater mod hovedpine og migræne samt forkølelsesrelaterede symptomer.
TxGNN-modellen forudsiger, at det kan have effekt ved **næsehulesygdom (nasal cavity disease)**,
men der er **ingen registrerede kliniske forsøg** og kun **3 publikationer** af svagt og indirekte tilsnit, som understøtter denne retning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske markedsføringstilladelser. Den videnbaserede model (PrimeKG) angiver bl.a. allergisk rhinitis, vasomotorisk rhinitis, migræne, hovedpine, almindelig forkølelse og faryngitis |
| Forudsagt ny indikation | Næsehulesygdom (nasal cavity disease) |
| TxGNN-forudsigelsesscore | 99,91 % |
| Evidensniveau | L4 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 4 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ikke detaljerede data om virkningsmekanismen i de data, der er sammenstillet til denne rapport. Koffein er dog kendt som en adenosinreceptorantagonist og fosfodiesterasehæmmer.

Bittersmagsreceptorer (TAS2R) findes i humant luftvejsepitel og aktiveres bl.a. af koffein. De kan påvirke cilieslag og det medfødte forsvar, hvilket giver en tænkelig, men ubevist forbindelse til sygdomme i næsen. Koffein indgår desuden i kombinationspræparater med indikationer som allergisk og vasomotorisk rhinitis, men evidensen for dette er tynd.

Det eneste studie om næseadministration (nasal in situ-gel, 2022) omhandler kognition efter søvnmangel og er et præklinisk formuleringsstudie, ikke en behandling af en næsesygdom. Forudsigelsen bør derfor betragtes som et hypotesegenererende signal.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [26272040](https://pubmed.ncbi.nlm.nih.gov/26272040/) | 2015 | Review | Pharmacology & Therapeutics | Bittersmagsreceptorer findes i bl.a. næsehule og lunger; farmakologi og rolle i humane luftveje beskrives |
| [35579146](https://pubmed.ncbi.nlm.nih.gov/35579146/) | 2022 | Præklinisk formuleringsstudie | Current Drug Delivery | Termofølsom nasal koffeingel til forbedret kognition efter søvnmangel; ikke en behandling af næsesygdom |
| [9751618](https://pubmed.ncbi.nlm.nih.gov/9751618/) | 1998 | Dyrestudie | Cancer Research | Sort te og koffein hæmmede lungecarcinogenese hos rotter; uden for emnet |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100665775 | Treo | Brusetabletter | Ikke angivet |
| 28100711576 | Ergokoffin | Overtrukne tabletter | Ikke angivet |
| 28104522209 | Arax Extra | Tabletter | Ikke angivet |
| 28100725776 | Kodamid "DAK" | Tabletter | Ikke angivet |

---

## Sikkerhedsovervejelser

Følgende er hentet fra en videnbase (PrimeKG) og ikke fra produktresuméer. Koffein er i videnbasen markeret som kontraindiceret eller problematisk ved bl.a.:

- **Hjerte-kar:** hypertension, ortostatisk hypotension, posturalt ortostatisk takykardisyndrom, multipel systematrofi, langt QT-syndrom (inkl. familiær form)
- **Lever og nyrer:** leversvigt, leversygdom, nyresygdom
- **Neurologi og psyke:** epilepsi, søvnløshed, angstlidelse, neurotisk lidelse, dysthymi
- **Mave-tarm:** mavesår, peptisk ulcussygdom, inflammatorisk tarmsygdom, pancreatitis, galdeblæresygdom
- **Lunger:** kronisk obstruktiv lungesygdom (KOL)
- **Andet:** porfyri, hypothyreose/myxødem, trombocytopeni, pyoureter

**Lægemiddelinteraktioner:** 160 interaktioner er registreret. Blandt de angivne er de mest alvorlige:
- **Alvorlig (Major):** kokain (nasalt og topisk)
- **Moderat:** alosetron, obeticholsyre, abametapir (topisk), adenosin, anagrelid, bendamustin, capmatinib, ciprofloxacin, cycloserin, dipyridamol
- **Mindre:** acetylsalicylsyre, cimetidin, atazanavir

For fuldstændig sikkerhedsinformation, herunder advarsler og kontraindikationer for de enkelte præparater, henvises til de godkendte produktresuméer (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om næsehulesygdom er baseret på en høj modelscore, men understøttes ikke af kliniske forsøg, og den tilgængelige litteratur er indirekte eller præklinisk. Evidensniveauet er L4.

**For at komme videre kræves følgende:**
- Præcisering af, hvilken konkret næsesygdom der tænkes på, da "næsehulesygdom" er en bred kategori
- Data om virkningsmekanisme og en undersøgelse af, om TAS2R-aktivering eller adenosinantagonisme kan have terapeutisk relevans i næseslimhinden
- Præklinisk eller eksplorativt klinisk arbejde i relevante modeller (fx allergisk eller vasomotorisk rhinitis)
- Gennemgang af produktresuméer for de fire danske præparater (advarsler, kontraindikationer og godkendte indikationer mangler i de sammenstillede data)
- Vurdering af egnet administrationsvej og formulering, da de eksisterende danske præparater er orale

---

*Bemærk: Andre forudsagte indikationer (f.eks. hypnic headache og trigeminal autonom cephalalgi, begge evidensniveau L3–L4) ligger tættere på koffeins kendte brug og kan være mere oplagte at undersøge nærmere.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

