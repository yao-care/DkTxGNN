---
layout: default
title: Regadenoson
parent: Kun modelforudsigelse (L5)
nav_order: 369
evidence_level: L5
indication_count: 8
---

# Regadenoson
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **8** stk.
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

# Regadenoson: Fra diagnostisk farmakologisk stressmiddel til anafylaksi

## Resumé i én sætning

Regadenoson er en selektiv A2A-adenosinreceptoragonist, som markedsføres i Danmark som Rapiscan (injektionsvæske) og anvendes som farmakologisk stressmiddel ved hjertebilleddiagnostik.
TxGNN-modellen forudsiger, at stoffet kan have effekt ved **anafylaksi**, men der findes **1 klinisk forsøg** (uden direkte relevans for indikationen) og **0 publikationer**, der understøtter forudsigelsen.
Forudsigelsen er derfor udelukkende modelbaseret og bør betragtes som spekulativ.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i det modtagne registerudtræk (anvendes i praksis som farmakologisk stressmiddel ved myokardieperfusionsbilleddannelse) |
| Foreslået ny indikation | Anafylaksi |
| TxGNN-forudsigelsesscore | 99,85 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor kan forudsigelsen se rimelig ud?

Der foreligger ikke detaljerede data om regadenosons oprindelige virkningsmekanisme i det modtagne datasæt. Regadenoson er kendt som en selektiv A2A-adenosinreceptoragonist. A2A-signalering har i prækliniske studier vist antiinflammatoriske og mastcellestabiliserende effekter, hvilket giver et teoretisk link til allergiske reaktioner.

Dette link er dog svagt. Regadenosons produktinformation indeholder selv advarsler om overfølsomhed og anafylaksi, og stoffet er ikke en etableret behandling af anafylaksi; adrenalin er fortsat førstevalg. Den høje score (0,998) afspejler sandsynligvis nærhed i adenosin-signalvejen i vidensgrafen og ikke terapeutisk relevans.

### Øvrige forudsigelser fra modellen

| Forudsagt indikation | TxGNN-score | Vurdering |
|------|------|------|
| Fødeafhængig anstrengelsesudløst anafylaksi | 99,74 % | Undertype af anafylaksi. Forudsigelsen skyldes sandsynligvis propagering fra overordnet anafylaksi-knude. Intravenøs bolusindgivelse passer dårligt til forebyggende behandling. |
| Esotropi | 99,12 % | Ingen plausibel mekanistisk forbindelse fundet. Sandsynligvis falsk positiv. |
| Pseudoallergi | 99,12 % | Samme teoretiske mastcelle-rationale som anafylaksi, kun prækliniske antagelser. Regadenoson kan selv udløse overfølsomhedsreaktioner. |

Ingen af de øvrige forudsigelser har kliniske forsøg eller litteratur.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT06854458](https://clinicaltrials.gov/study/NCT06854458) | Ikke relevant (NA) | Rekrutterer | 1.000 | SPINS2: kvantitativ stress-hjertemagnetisk resonans (CMR) perfusionsbilleddannelse ved brystsmerter eller åndenød. Regadenoson bruges sandsynligvis som diagnostisk stressmiddel. Forsøget tester ikke anafylaksi (relevansgrad C). |

Fundet skyldes sandsynligvis et artefakt i søgningen på lægemiddelnavn og giver hverken direkte eller meningsfuld indirekte evidens for den foreslåede indikation.

---

## Litteraturevidens

Der findes i øjeblikket ingen relateret litteratur.

---

## Information om det danske marked

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28104535109 | Rapiscan | Injektionsvæske, opløsning | Rapidscan Pharma Solutions EU Ltd |

Indikationsteksten er ikke angivet i det modtagne registerudtræk.

---

## Sikkerhedsovervejelser

Interaktionsopslag gav ingen fund. Der er ikke modtaget øvrige sikkerhedsdata.

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Bemærk især, at produktinformationen for regadenoson indeholder advarsler om overfølsomhed og anafylaksi.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er rent modelbaseret (L5) uden understøttende kliniske forsøg eller litteratur. Det eneste fundne forsøg anvender sandsynligvis regadenoson som diagnostisk stressmiddel. Stoffet kan desuden selv udløse overfølsomhedsreaktioner, og adrenalin er etableret førstevalg ved anafylaksi.

**For at komme videre kræves følgende:**
- Hentning af produktresumé (SmPC) fra Lægemiddelstyrelsen med advarsler, kontraindikationer og godkendt indikationstekst
- Detaljerede data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prækliniske data, der viser en effekt af A2A-agonisme på mastcelleaktivering ved anafylaksi
- En vurdering af, om intravenøs bolusindgivelse og regadenosons hæmodynamiske virkninger (takykardi, vasodilatation) overhovedet er forenelige med et akut eller forebyggende allergisk behandlingsscenarie

*Resultaterne er kun til forskningsbrug og udgør ikke lægefaglig rådgivning. Kandidater til lægemiddelomplacering skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

