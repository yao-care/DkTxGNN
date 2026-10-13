---
layout: default
title: Reteplase
parent: Kun modelforudsigelse (L5)
nav_order: 714
evidence_level: L5
indication_count: 10
---

# Reteplase
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

# Reteplase: Fra myokardieinfarkt til posteroinferiort myokardieinfarkt

## Opsummering i én sætning

Reteplase er et rekombinant vævsplasminogenaktivator-præparat (fibrinolytikum), som oprindeligt anvendes til behandling af akut myokardieinfarkt.
TxGNN-modellen forudsiger, at det kan være virksomt ved **posteroinferiort myokardieinfarkt**, men der er i de data, der er indsamlet til denne rapport, **ingen kliniske forsøg** og **ingen publikationer** for netop denne undertype. Den høje score afspejler hovedsageligt nærhed til den allerede godkendte indikation, og der er derfor ikke tale om en reel repurposing.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Myokardieinfarkt (fra videngrafen; teksten for den godkendte indikation i den danske registrering er ikke tilgængelig) |
| Forudsagt ny indikation | Posteroinferiort myokardieinfarkt |
| TxGNN-prædiktionsscore | 99,90 % |
| Evidensniveau | L4 (L5 kan argumenteres; ingen studier for undertypen) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om virkningsmekanismen. Reteplase er dog kendt som et rekombinant vævsplasminogenaktivator-præparat. Dets effekt ved akut myokardieinfarkt er veletableret, og mekanismen (opløsning af den okklusive blodprop i kranspulsåren) kan principielt anvendes ved posteroinferiort myokardieinfarkt.

Posteroinferiort myokardieinfarkt er en anatomisk undertype af den allerede godkendte indikation, myokardieinfarkt. Mekanismen gælder derfor direkte, men der er ikke tale om en egentlig ny anvendelse. Den høje score (0,999) afspejler primært ontologisk nærhed til den oprindelige indikation og ikke selvstændig klinisk evidens.

Øvrige forudsagte indikationer i datasættet omfatter posterolateralt og septalt myokardieinfarkt, medfødt koronararterieanomali og koronar stenose. De to første er ligeledes undertyper af myokardieinfarkt. Ved medfødt koronararterieanomali er den underliggende afvigelse strukturel og kan ikke behandles med fibrinolyse. Ved koronar stenose findes der studier af reteplase som led i facilitering af PCI, men effekten ved stenose i sig selv er ikke påvist.

---

## Evidens fra kliniske forsøg

Der er for øjeblikket ikke registreret relaterede kliniske forsøg for posteroinferiort myokardieinfarkt.

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur for posteroinferiort myokardieinfarkt.

Til orientering fandtes der litteratur for nærtliggende forudsagte indikationer (alle med indirekte evidens):

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [15800019](https://pubmed.ncbi.nlm.nih.gov/15800019/) | 2005 | Post hoc-analyse af kliniske forsøg | European Heart Journal | Sammenhæng mellem aPTT og kliniske udfald i GUSTO-V (standarddosis reteplase vs. halv dosis reteplase + abciximab) |
| [11079647](https://pubmed.ncbi.nlm.nih.gov/11079647/) | 2000 | Klinisk studie | J Am Coll Cardiol | Tidlig PCI efter reteplase med eller uden abciximab ved akut myokardieinfarkt (SPEED/GUSTO-4 pilot) |
| [21351226](https://pubmed.ncbi.nlm.nih.gov/21351226/) | 2011 | Case report | Catheter Cardiovasc Interv | PCI af ubeskyttet venstre hovedstamme faciliteret af intrakoronar reteplase ved posterolateralt myokardieinfarkt |
| [16786798](https://pubmed.ncbi.nlm.nih.gov/16786798/) | 2005 | Case report | Przeglad Lekarski | Akut inferiort og højresidigt ventrikelinfarkt hos patient med atrieseptumdefekt, behandlet med reteplase og abciximab (GUSTO V) med elektrokardiografisk reperfusion |
| [34512848](https://pubmed.ncbi.nlm.nih.gov/34512848/) | 2021 | Case report | Pan African Medical Journal | De Winter-mønster i EKG som tegn på okklusiv koronarsygdom; vurderer ikke reteplase |

---

## Oplysninger om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101765295 | Rapilysin | Pulver og solvens til injektionsvæske, opløsning | Indikationsteksten er ikke tilgængelig i de indsamlede data |

Indehaver: Actavis Group PTC ehf.

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (100 registrerede interaktioner i alt; et udvalg nedenfor):

- **Alvorlige (Major):** abciximab, apixaban, betrixaban, acalabrutinib, avapritinib, deferasirox, ibritumomab tiuxetan, tositumomab
- **Moderate:** acetylsalicylsyre, ibuprofen, ketorolac, celecoxib, diclofenac (topisk), aminocapronsyre, omega-3-fedtsyrer, fenfluramin, dexfenfluramin, sibutramin

Interaktionerne vedrører især øget blødningsrisiko ved samtidig brug af lægemidler, der påvirker blodstørkning eller trombocytfunktion.

Der foreligger ikke data om advarsler og kontraindikationer i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Posteroinferiort myokardieinfarkt er en undertype af den allerede godkendte indikation, så der er ikke tale om reel repurposing. Der er ingen kliniske forsøg eller litteratur for netop denne undertype, og den høje TxGNN-score afspejler primært ontologisk nærhed.

**For at komme videre kræves følgende:**
- Hent og gennemgå produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikationstekst). Dette er en blokerende datamangel for sikkerhedsscreening.
- Indhent data om virkningsmekanisme (MOA) fra DrugBank.
- Afklar, om undertypen allerede er omfattet af den eksisterende indikation, så den ikke behandles som en ny indikation.
- Hvis koronar stenose (facilitering af PCI) skal forfølges som forskningsspørgsmål, kræves en systematisk gennemgang af de større forsøg, da strategien har vist begrænset gavn.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

