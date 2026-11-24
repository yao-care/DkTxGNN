---
layout: default
title: Caffeine
parent: Kun modelforudsigelse (L5)
nav_order: 147
evidence_level: L5
indication_count: 8
last_modified_at: 2026-11-24
description: "Caffeine: forudsagt ny indikation Næsehulesygdom (nasal cavity disease) (evidensniveau L5). Oprindelig indikation: Ikke angivet i de danske markedsføringstilladelser. Den videnbaserede…"
monitor_inn: "caffeine"
predicted_indications: ["nasal cavity disease", "thrombotic disease", "papillary conjunctivitis", "neuralgia", "glossodynia", "coccygodynia", "trigeminal autonomic cephalalgia", "vein disease"]
---

# Caffeine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **8** stk.
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

## Koffein: Fra migræne og hovedpine til næsehulesygdom
{: .text-alpha }

## Opsummering

Koffein er et metylxanthin, som i Danmark bruges i receptfrie kombinationspræparater mod hovedpine, migræne og forkølelsesrelaterede symptomer og findes desuden som koffeincitrat (enkeltstof) til infusion og oral opløsning (Gencebok, Peyona).
TxGNN-modellen forudsiger, at det kan have effekt ved **næsehulesygdom (nasal cavity disease)**,
men der er **ingen registrerede kliniske forsøg** og kun **3 publikationer** af svagt og indirekte tilsnit, som understøtter denne retning.

<!-- review:begin dk-lic-20261124c-caffeine-1 -->

> **Rettelse ved gennemgang (2026-11-24)**: Oprindeligt stod der: "kombinationspræparater mod hovedpine og migræne samt forkølelsesrelaterede symptomer." Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler. Lægemiddelstyrelsens liste over godkendte lægemidler (2026-11-24) har også Gencebok og Peyona (Caffeincitrat, infusionsvæske og oral opløsning). Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261124c-caffeine-1 -->

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske markedsføringstilladelser. Den videnbaserede model (PrimeKG) angiver bl.a. allergisk rhinitis, vasomotorisk rhinitis, migræne, hovedpine, almindelig forkølelse og faryngitis |
| Forudsagt ny indikation | Næsehulesygdom (nasal cavity disease) |
| TxGNN-forudsigelsesscore | 0,9991 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 11 af 12) |
| Antal markedsføringstilladelser | 12 (gyldige: 11) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Caffeine (uofficiel oversættelse): »Koffein er strukturelt beslægtet med andre methylxanthiner, theophyllin og theobromin. Det er et afslappende middel for bronkiernes glatte muskulatur, et CNS-stimulans, et stimulans for hjertemusklen og et diuretikum. Selvom virkningsmekanismen for koffein ved apnø hos præmature ikke kendes, er der fremsat hypoteser om flere mekanismer.« Engelsk originaltekst: "Caffeine is structurally related to other methylxanthines, theophylline, and theobromine. It is a bronchial smooth muscle relaxant, a CNS stimulant, a cardiac muscle stimulant, and a diuretic. Although the mechanism of action of caffeine in apnea of prematurity is not known, several mechanisms have been hypothesized." ([DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a), version af 2026-07-29; hentet 2026-11-19). Koffein er dog kendt som en adenosinreceptorantagonist og fosfodiesterasehæmmer.

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

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28104522209 | Arax Extra | tabletter | Caffein, PARACETAMOL | Gyldig |
| 28100725776 | Kodamid "DAK" | tabletter | Caffein, CODEINPHOSPHATHEMIHYDRAT, Magnesiumhydroxid, tungt, PROPYPHE… | Gyldig |
| 28105935717 | Panodil Extra | filmovertrukne tabletter | Caffein, PARACETAMOL | Gyldig |
| 28107241724 | Paracetamol/Caffein "Orifarm" | filmovertrukne tabletter | Caffein, PARACETAMOL | Gyldig |
| 28100665775 | Treo | brusetabletter | ACETYLSALICYLSYRE, Caffein | Gyldig |

Tabellen viser 5 af 12 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

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
- Gennemgang af produktresuméer for de danske præparater (advarsler, kontraindikationer og godkendte indikationer mangler i de sammenstillede data)
- Vurdering af egnet administrationsvej og formulering, da de eksisterende danske præparater er tabletter (orale) eller, for koffeincitratets vedkommende, infusionsvæske og oral opløsning

<!-- review:begin dk-lic-20261124c-caffeine-2 -->

> **Rettelse ved gennemgang (2026-11-24)**: Oprindeligt stod der: "Gennemgang af produktresuméer for de fire danske præparater" Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler. Lægemiddelstyrelsens liste har flere end fire præparater med koffein (antal: se Hurtigt overblik). Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261124c-caffeine-2 -->

<!-- review:begin dk-lic-20261124c-caffeine-3 -->

> **Rettelse ved gennemgang (2026-11-24)**: Oprindeligt stod der: "da de eksisterende danske præparater er orale" Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler. Gencebok og Peyona (Caffeincitrat) er infusionsvæsker (Peyona også oral opløsning). Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261124c-caffeine-3 -->

---

*Bemærk: Andre forudsagte indikationer (f.eks. hypnic headache og trigeminal autonom cephalalgi, begge evidensniveau L3–L4) ligger tættere på koffeins kendte brug og kan være mere oplagte at undersøge nærmere.*

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse).

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: caffeine citrate prescribing information, Sagent Pharmaceuticals](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5f38c395-0093-4afd-89ec-f96e5dc0934a) |
| 2026-11-24 | kombinationspræparater mod hovedpine og migræne samt forkølelsesrelaterede symptomer. | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |
| 2026-11-24 | Gennemgang af produktresuméer for de fire danske præparater | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |
| 2026-11-24 | da de eksisterende danske præparater er orale | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

