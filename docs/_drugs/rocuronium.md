---
layout: default
title: Rocuronium
parent: Kun modelforudsigelse (L5)
nav_order: 732
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Rocuronium: forudsagt ny indikation Migræne (migraine disorder) (evidensniveau L5). Oprindelig indikation: Ikke angivet i de data…"
monitor_inn: "rocuronium"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "cauda equina syndrome", "migraine with or without aura, susceptibility to", "atrophoderma vermiculata", "ulerythema ophryogenesis", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "sciatic neuropathy", "headache disorder"]
---

# Rocuronium
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

## Rocuronium: Fra neuromuskulær blokade til migræne
{: .text-alpha }

## Resumé i én sætning

Rocuronium er et ikke-depolariserende neuromuskulært blokerende middel, som er godkendt i Danmark som injektionsvæske. Det bruges typisk som hjælpemiddel ved anæstesi. TxGNN-modellen forudsiger, at det kan have effekt ved **migræne**, men denne forudsigelse understøttes kun af **1 klinisk studie** uden relevans for indikationen og **ingen publikationer** om migræne. Forudsigelsen skal derfor betragtes som rent modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de data, der er indsamlet til denne rapport (godkendt indikationstekst for det danske produkt er tom) |
| Forudsagt ny indikation | Migræne (migraine disorder) |
| TxGNN-forudsigelsesscore | 99,90 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i de indsamlede data. Rocuronium er dog kendt som en kompetitiv antagonist ved nikotinerge acetylcholinreceptorer på den motoriske endeplade, hvilket hæmmer neuromuskulær transmission i skeletmuskulatur.

Der kendes ingen mekanisme, hvorved dette kan påvirke migrænens patofysiologi, f.eks. CGRP-signalering, trigeminovaskulær aktivering eller cortical spreading depression. Den høje TxGNN-score afspejler sandsynligvis nærhed i vidensgrafen snarere end en biologisk begrundelse.

Botulinumtoksin, som også hæmmer neuromuskulær transmission, bruges ved kronisk migræne. Det virker imidlertid via præsynaptisk hæmning af acetylcholinfrigivelse og modulering af nociceptorer, og denne effekt kan ikke overføres til en postsynaptisk blokker som rocuronium.

Øvrige forudsigelser i modellen (migræne med hjernestammeaura, cauda equina-syndrom, irritabel tyktarm, iskiasneuropati, hovedpine m.fl.) mangler ligeledes plausibel mekanisme og dokumentation.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | Ikke relevant (N/A) | Afsluttet | 3520 | Farmakokinetikstudie af underbelyste lægemidler givet til børn som standardbehandling. Ikke designet til at undersøge effekt ved migræne; rocuronium indgår kun som anæstesihjælpemiddel. Ingen indikationsspecifik evidens. |

---

## Litteraturevidens

Der foreligger ingen litteratur om rocuronium ved migræne. Den eneste litteratur, der er knyttet til den nærtstående forudsigelse "hovedpine", er anført nedenfor og er ikke evidens for terapeutisk effekt.

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [23812022](https://pubmed.ncbi.nlm.nih.gov/23812022/) | 2014 | Klinisk studie | The Journal of ECT | Sammenligning af succinylcholin og rocuronium-sugammadex med hensyn til myalgi og hovedpine efter elektrokonvulsiv behandling. Hovedpine er her en bivirkning, ikke et behandlingsmål. |
| [24196089](https://pubmed.ncbi.nlm.nih.gov/24196089/) | 2013 | Case report | Pediatric Emergency Care | Hurtig sekvensintubation hos et barn med forhøjet intrakranielt tryk og aspirationsrisiko. Ingen relevans for migræne. |

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106623721 | Rocuronium bromide "Accord" (Accord Healthcare B.V.) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Ikke angivet i de tilgængelige data |

---

## Sikkerhedsmæssige overvejelser

Der er ikke tilgængelige data om advarsler eller kontraindikationer fra produktresuméet. Der er heller ikke registreret kontraindikationer i vidensgrafen.

**Lægemiddelinteraktioner:** Der er identificeret i alt 114 interaktioner, hvoraf et udvalg er vist her:

- **Alvorlige (Major):** paromomycin, kanamycin, neomycin
- **Moderate:** doxycyclin, tetracyclin, minocyclin, vancomycin, amphotericin B, magnesiumsulfat, magnesiumchlorid, mannitol, metoclopramid, hydrocortison, dexamethason, betamethason, triamcinolon, prednison, neomycin (topisk)
- **Milde (Minor):** ranitidin

Derudover bør godkendt produktresumé (SmPC) konsulteres for fuldstændige sikkerhedsoplysninger. Systemisk neuromuskulær blokade medfører risiko for respirationslammelse og kræver kontrolleret anvendelse med mulighed for ventilation.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (evidensniveau L5) og mangler både biologisk rationale og klinisk dokumentation. Det eneste tilknyttede studie er et generelt farmakokinetikstudie uden relation til migræne. En systemisk neuromuskulær blokker vil desuden indebære uacceptabel risiko for respirationslammelse ved en kronisk, ikke-livstruende tilstand.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé (SmPC) med advarsler og kontraindikationer fra Lægemiddelstyrelsen
- Prækliniske eller mekanistiske data, som kan understøtte en sammenhæng med migræne
- Afklaring af, om der findes et realistisk administrationsrationale, da lægemidlet kun foreligger som injektion
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

