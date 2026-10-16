---
layout: default
title: Vismodegib
parent: Kun modelforudsigelse (L5)
nav_order: 889
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Vismodegib: forudsagt ny indikation Medulloblastom med udtalt nodularitet (evidensniveau L5). Oprindelig indikation: Basalcellekarcinom (hudkarcinom, svedkirtelkræft…"
---

# Vismodegib
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

# Vismodegib: Fra basalcellekarcinom til medulloblastom med udtalt nodularitet

## Opsummering i en sætning

Vismodegib er en oral hæmmer af Hedgehog-signalvejen, oprindeligt anvendt til behandling af basalcellekarcinom og andre hudkræftformer.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **medulloblastom med udtalt nodularitet**,
men der er i de data, der er indsamlet til denne rapport, **ingen kliniske forsøg** og **ingen publikationer** for netop denne indikation. Støtten består udelukkende af modellens forudsigelsesscore.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Basalcellekarcinom (hudkarcinom, svedkirtelkræft, sebaceøst adenokarcinom m.fl. ifølge vidensgrafen). Indikationsteksten i den danske registrering er ikke angivet |
| Forudsagt ny indikation | Medulloblastom med udtalt nodularitet |
| TxGNN-forudsigelsesscore | 99,93 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de indsamlede data. Ud fra almen farmakologisk viden hæmmer vismodegib Smoothened (SMO) i Hedgehog-signalvejen. Denne vurdering er ikke baseret på de leverede data.

Medulloblastom, især den SHH-drevne undergruppe, er biologisk et plausibelt mål. Varianten med udtalt nodularitet er hyppigt SHH-drevet og forbundet med Gorlin-syndrom/PTCH1-ændringer. Basalcellekarcinom er ligeledes drevet af overaktiv Hedgehog-signalering, hvilket giver en mekanistisk sammenhæng mellem den oprindelige og den forudsagte indikation.

Det skal understreges, at der ikke foreligger forsøg eller litteratur for denne indikation. Forudsigelsen hviler alene på modellens score og på generel biologisk plausibilitet.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig for medulloblastom med udtalt nodularitet.

*Bemærk:* For de øvrige forudsagte indikationer fandtes litteratur kun for xeroderma pigmentosum (se nedenfor under næste skridt).

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105032611 | Erivedge (Roche Registration GmbH) | Kapsler, hårde | Indikationstekst ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (Hedgehog-/SMO-hæmmer) |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Monitoreringspunkter | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) for advarsler og forholdsregler |

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der er identificeret 56 interaktioner i alt. De fleste er af mindre betydning (minor), primært syrehæmmende midler:
- **Moderat:** Clarithromycin
- **Mindre:** Protonpumpehæmmere (omeprazol, esomeprazol, lansoprazol, dexlansoprazol, pantoprazol, rabeprazol), H2-blokkere (famotidin, ranitidin, cimetidin, nizatidin) samt antacida (aluminiumhydroxid, calciumcarbonat, magnesiumoxid/-hydroxid/-carbonat, magaldrat, natriumbicarbonat, natriumcitrat)

Oplysninger om advarsler og kontraindikationer var ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for medulloblastom med udtalt nodularitet er alene støttet af en høj modelscore (L5) uden kliniske forsøg eller publikationer. Mekanistisk plausibilitet er til stede, men utilstrækkelig til at gå videre uden yderligere evidens.

**For at komme videre kræves følgende:**
- Systematisk gennemgang af litteratur og forsøgsregistre for vismodegib ved SHH-medulloblastom
- Detaljerede data om virkningsmekanisme (MOA) fra DrugBank
- Fuldstændige advarsler og kontraindikationer fra det danske produktresumé (blokerende datamangel for sikkerhedsscreening)
- Særlig sikkerhedsvurdering hos børn og i populationer med defekt DNA-reparation

**Andre forudsagte indikationer (til orientering):**
- **Xeroderma pigmentosum** (score 99,91 %, evidensniveau L4): Fire publikationer (to case reports med vismodegib mod basalcellekarcinom hos patienter med XP, PMID [28297142](https://pubmed.ncbi.nlm.nih.gov/28297142/) og [30178564](https://pubmed.ncbi.nlm.nih.gov/30178564/), en gennemgangsartikel [35283513](https://pubmed.ncbi.nlm.nih.gov/35283513/) og en case report [36921168](https://pubmed.ncbi.nlm.nih.gov/36921168/)). Effekten ses på basalcellekarcinom hos XP-patienter, ikke på den underliggende DNA-reparationsdefekt. Dette er indirekte evidens og kan være et relevant forskningsspørgsmål.
- **Annulær epidermolytisk ichthyosis** (99,87 %), **epidermolysis bullosa simplex med spættet pigmentering** (99,86 %) og **prostata-/hjernekræft-modtagelighed** (99,85 %): Alle L5 uden forsøg eller litteratur og uden klar mekanistisk sammenhæng med Hedgehog-hæmning. Anbefaling: Hold.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

