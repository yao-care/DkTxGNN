---
layout: default
title: Dalbavancin
parent: Kun modelforudsigelse (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Dalbavancin: forudsagt ny indikation Postinfektiøs vaskulitis (evidensniveau L5). Oprindelig indikation: Infektionsbetingede hudsygdomme (fra vidensgrafen"
monitor_inn: "dalbavancin"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "otitis externa", "ophthalmic herpes zoster", "infectious mononucleosis", "orbital cellulitis"]
---

# Dalbavancin
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

## Dalbavancin: Fra hudinfektioner til postinfektiøs vaskulitis
{: .text-alpha }

## Resumé i én sætning

Dalbavancin er et lipoglykopeptid-antibiotikum, der oprindeligt anvendes til behandling af infektionsbetingede hudsygdomme.
TxGNN-modellen forudsiger, at det kan have effekt på **postinfektiøs vaskulitis**,
men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter denne retning. Forudsigelsen bygger udelukkende på modellen.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Infektionsbetingede hudsygdomme (fra vidensgrafen; den danske godkendelsestekst er ikke angivet) |
| Forudsagt ny indikation | Postinfektiøs vaskulitis |
| TxGNN-forudsigelsesscore | 99,76 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Dalbavancin tilhører dog gruppen af lipoglykopeptid-antibiotika, der virker mod grampositive bakterier ved at hæmme bakteriens cellevægssyntese (binding til D-Ala-D-Ala-enden af peptidoglykan-forstadier). Dets effekt ved bakterielle hud- og bløddelsinfektioner er veletableret.

Postinfektiøs vaskulitis er typisk immunmedieret og opstår, efter infektionen er afklaret. Antibakteriel aktivitet forventes derfor ikke at behandle den underliggende patologi. Behandling af et vedvarende grampositivt udløsende fokus kunne have en indirekte betydning, men det er spekulativt. Den høje score skyldes sandsynligvis nærhed til infektionsnoder i vidensgrafen snarere end en konkret mekanisme.

**Øvrige forudsagte indikationer (alle uden kliniske forsøg eller litteratur):**

| Rang | Sygdom | Score | Evidensniveau | Vurdering |
|---|---|---|---|---|
| 2 | Post-bakteriel lidelse | 99,76 % | L5 | Hold: uspecifik kategori uden klar mekanisme |
| 3 | Postinfektiøst syndrom | 99,76 % | L5 | Hold: bred kategori, ingen kendt aktivitet mod immunologiske følger |
| 4 | Infektiøs uretral striktur | 99,74 % | L5 | Hold: fibrotisk tilstand, ofte gramnegative årsager |
| 5 | Chagas-kardiomyopati | 99,72 % | L5 | Hold: parasitær årsag, ingen antiprotozoær mekanisme |
| 6 | Infektionsrelateret hæmolytisk uræmisk syndrom | 99,72 % | L5 | Hold: oftest gramnegativ STEC; antibiotika er kontroversielle og kan skade |
| 7 | Otitis externa | 99,70 % | L5 | Hold: ofte Pseudomonas; lokal behandling er tilstrækkelig |
| 8 | Oftalmisk herpes zoster | 99,25 % | L5 | Hold: viral sygdom, ingen antiviral effekt |
| 9 | Infektiøs mononukleose | 99,16 % | L5 | Hold: viral sygdom, antibiotika er ikke indiceret |
| 10 | Orbital cellulitis | 99,02 % | L4 | Forskningsspørgsmål: biologisk mest plausibel, da S. aureus (inkl. MRSA) og streptokokker dækkes, men kun indirekte evidens |

---

## Klinisk evidens fra forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der foreligger på nuværende tidspunkt ingen relateret litteratur.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106925323 | Dalbavancin "Adalvo" (AdAlvo Limited) | Pulver til koncentrat til infusionsvæske, opløsning | Indikationstekst ikke angivet |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner** (3 registreret, alle af moderat sværhedsgrad):
  - Picosulfat (picosulfuric acid)
  - Ethinylestradiol
  - Mycofenolsyre

For øvrige sikkerhedsoplysninger (advarsler og kontraindikationer) henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for postinfektiøs vaskulitis bygger udelukkende på modellen uden støtte fra kliniske forsøg eller litteratur, og den mekanistiske sammenhæng er svag, da sygdommen er immunmedieret efter infektionens ophør. Blandt de forudsagte indikationer er orbital cellulitis den biologisk mest plausible, men også her er evidensen kun indirekte.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen (afgørende for sikkerhedsscreening)
- Godkendt indikationstekst for den danske tilladelse
- Systematisk litteratur- og forsøgssøgning, især for orbital cellulitis, herunder data om vævspenetration i orbita
- Vurdering af administrationsvej (kun intravenøs formulering er tilgængelig)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

