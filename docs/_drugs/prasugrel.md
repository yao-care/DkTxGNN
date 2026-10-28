---
layout: default
title: Prasugrel
parent: Kun modelforudsigelse (L5)
nav_order: 677
evidence_level: L5
indication_count: 9
monitor_inn: "Prasugrel"
predicted_indications: ["pulmonary hypertension", "migraine disorder", "migraine with brainstem aura", "kyphoscoliotic heart disease", "rheumatoid arthritis", "homozygous familial hypercholesterolemia", "hypoalphalipoproteinemia", "brachydactyly-syndactyly syndrome", "leprosy"]
last_modified_at: 2026-10-23
description: "Prasugrel: forudsagt ny indikation Pulmonal hypertension (evidensniveau L5). Oprindelig indikation: Akut koronarsyndrom"
---

# Prasugrel
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **9** stk.
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

## Prasugrel: Fra akut koronarsyndrom til pulmonal hypertension
{: .text-alpha }

## Resumé i én sætning

Prasugrel er en blodpladehæmmer (P2Y12-antagonist). TxGNN-modellen (deep learning) forudsiger, at lægemidlet kan have effekt ved **pulmonal hypertension**; denne forudsigelse kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og er ikke biologisk evidens. Der er dog **ingen kliniske forsøg** og ingen publikationer, der direkte undersøger prasugrel ved denne sygdom, så forudsigelsen bygger alene på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Akut koronarsyndrom (relation registreret i vidensgrafen; indikationsteksten i den danske registrering er tom) |
| Forudsagt ny indikation | Pulmonal hypertension |
| TxGNN-forudsigelsesscore | 0,9988 |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen foreligger ikke i de data, der er indsamlet til denne rapport. Prasugrel er kendt som en P2Y12-receptorantagonist, der hæmmer blodpladeaggregation, og dette er grundlaget for brugen ved akut koronarsyndrom.

Ved pulmonal hypertension spiller blodpladeaktivering og trombose in situ en rolle i ombygningen af lungekarrene. Der er derfor en plausibel, men ubevist forbindelse mellem P2Y12-hæmning og sygdommen. Modellens score er høj, men der er ingen klinisk evidens, der understøtter den.

Til sammenligning har andre forudsagte indikationer mere indirekte støtte. Det gælder fx migræne med åbent foramen ovale (PFO), hvor tidlige undersøgelser af tienopyridiner er set (se nedenfor), men det gælder ikke den primære forudsigelse.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen registrerede kliniske forsøg for pulmonal hypertension.

For fuldstændighedens skyld kan nævnes, at der for den næstrangerede forudsigelse, migræne, findes to forsøg. Ingen af dem tester prasugrel direkte:

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT07629635](https://clinicaltrials.gov/study/NCT07629635) | Fase 3 | Rekrutterer | 32 | PFO-rettet behandling mod migræne; indirekte støtte til PFO-migræne-hypotesen |
| [NCT04100135](https://clinicaltrials.gov/study/NCT04100135) | Ikke relevant (device) | Afsluttet tidligt | 7 | Lukning af PFO med septal occluder; ingen data om lægemiddeleffekt |

---

## Litteraturevidens

Der er ingen publikationer, som direkte undersøger prasugrel ved pulmonal hypertension. De to fundne publikationer vedrører andre emner:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [21241206](https://pubmed.ncbi.nlm.nih.gov/21241206/) | 2011 | Kohorte | Current Medical Research and Opinion | Faktorer for brug af og vedholdenhed til clopidogrel efter PCI ved akut koronarsyndrom; ikke relateret til pulmonal hypertension |
| [34713782](https://pubmed.ncbi.nlm.nih.gov/34713782/) | 2021 | Kohorte | Kardiologiia | Betydning af baggrundsbehandling for dødelighed ved COVID-19 i et register; ikke relateret til pulmonal hypertension |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107432225 | Prasugrel "Epione" (Epione Medicine ApS) | Filmovertrukne tabletter | Indikationstekst foreligger ikke i de indsamlede data |

Der er registreret én gyldig tilladelse til et enkeltstofpræparat til oral brug.

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (100 interaktioner fundet; et udvalg nedenfor):
- **Alvorlige (Major):** deferasirox, ibritumomab tiuxetan
- **Moderate:** acetylsalicylsyre, morfin, opium, fenfluramin, dexfenfluramin, sibutramin
- **Mindre betydningsfulde:** bl.a. protonpumpehæmmere (omeprazol, pantoprazol m.fl.) og H2-blokkere (famotidin, ranitidin, cimetidin)

**Relationer i vidensgrafen (ikke præparatets mærkningstekst):** Vidensgrafen registrerer kontraindikationsrelationer til bl.a. leversvigt, blodkoagulationssygdom, intrakraniel blødning, cerebral infarkt, transitorisk iskæmisk anfald, trombocytopenisk purpura, hypotension og skade. Disse skal bekræftes i produktresuméet.

Derudover bør blødningsrisiko altid indgå i vurderingen. Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for pulmonal hypertension støttes kun af modellen (evidensniveau L5), og der findes hverken forsøg eller publikationer, som direkte undersøger prasugrel ved sygdommen. Blødningsrisikoen ved en blodpladehæmmer og de mange interaktioner taler for forsigtighed.

**For at komme videre kræves følgende:**
- Prækliniske eller mekanistiske studier af P2Y12-hæmning ved pulmonal hypertension
- Detaljerede data om virkningsmekanisme (MOA)
- Gennemgang af produktresuméet for advarsler og kontraindikationer, som mangler i de indsamlede data
- Overvejelse af migræne med PFO som mere lovende, men stadig kun indirekte understøttet, forskningsspørgsmål. Her findes kun en åben pilotundersøgelse (ticagrelor) og en retrospektiv gennemgang af tienopyridiner, og de omfatter ikke prasugrel specifikt
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

