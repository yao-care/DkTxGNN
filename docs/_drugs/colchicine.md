---
layout: default
title: Colchicine
parent: Kun modelforudsigelse (L5)
nav_order: 218
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Colchicine: forudsagt ny indikation Plasmodium falciparum-malaria (evidensniveau L5). Oprindelig indikation: Gigt, familiær middelhavsfeber"
monitor_inn: "colchicine"
predicted_indications: ["Plasmodium falciparum malaria", "dermatofibrosarcoma protuberans"]
---

# Colchicine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
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

# Colchicin: Fra gigt og familiær middelhavsfeber til Plasmodium falciparum-malaria

## Resumé i én sætning

Colchicin er et gammelt lægemiddel, der oprindeligt bruges til behandling af gigt og familiær middelhavsfeber (FMF).
TxGNN-modellen forudsiger, at det kan have effekt på **Plasmodium falciparum-malaria**,
men der er **ingen kliniske forsøg** og kun **2 laboratoriestudier** (ikke om colchicin), så evidensen er meget svag og baseret på modelforudsigelse alene.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Gigt, familiær middelhavsfeber (fra videngrafen; den danske godkendelsestekst er ikke angivet i de indsamlede data) |
| Forudsagt ny indikation | Plasmodium falciparum-malaria |
| TxGNN-forudsigelsesscore | 99,60 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Data om colchicins detaljerede virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til denne rapport. Colchicin er dog kendt for at binde tubulin og hæmme mikrotubulidannelse. Det er også kendt, at mikrotubulusforstyrrelser er beskrevet som en cellulær effekt i P. falciparum (f.eks. med curcumin). Det giver en mulig, men indirekte, mekanistisk begrundelse.

Det andet studie handler om pfmdr1-ekspression i pattedyrsceller og følsomhed over for lægemidler. Det peger på en mulig forbindelse via transportere af P-glykoprotein-typen, som også påvirker colchicins optagelse. Det er en observation om transport og resistens, **ikke** bevis for antimalariaeffekt.

Der foreligger ingen kliniske eller direkte in vivo-data for colchicin mod malaria. Colchicin har desuden et snævert terapeutisk indeks og høj toksicitet. Antiparasitær aktivitet ville sandsynligvis kræve tubulinhæmning ved koncentrationer tæt på de toksiske hos mennesker.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [23505424](https://pubmed.ncbi.nlm.nih.gov/23505424/) | 2013 | In vitro / cellebiologi | PLoS One | Curcumin (ikke colchicin) forstyrrer mikrotubuli i P. falciparum |
| [7511206](https://pubmed.ncbi.nlm.nih.gov/7511206/) | 1994 | In vitro / cellebiologi | Mol Cell Biol | pfmdr1-ekspression i pattedyrsceller er forbundet med øget følsomhed over for chloroquin; ikke direkte evidens for colchicin |

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106588021 | Colchicin "Strides" (Strides Pharma (Cyprus) Limited) | Tabletter | Indikationstekst ikke angivet i de indsamlede data |

---

## Cytotoksicitet

Colchicin er ikke et klassisk kræftlægemiddel, men et antiinflammatorisk middel med antimitotisk virkning og snævert terapeutisk indeks. Se produktresuméet (SmPC) for advarsler og forsigtighedsregler.

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra videnbasen (PrimeKG, ikke produkttekst):** leversvigt, hæmatologiske sygdomme, trombocytopeni, mavesår, myopati og andre muskelsygdomme, rabdomyolyse, diarrésygdomme, nedsat nyrefunktion, leukopeni, agranulocytose, neutropeni (inkl. kongenitte former), aplastisk anæmi og akut uratnefropati.
- **Lægemiddelinteraktioner:** 125 interaktioner er registreret. Blandt de **alvorlige (Major)** er aprepitant, clarithromycin, eliglustat, rolapitant, rosuvastatin, simvastatin, cobicistat og deferipron. Blandt de **moderate** er bl.a. metronidazol, cimetidin, eluxadolin, miconazol, tinidazol, deferasirox, ticagrelor, chloroquin og benznidazol. Kombinationen med chloroquin er relevant, da chloroquin anvendes ved malaria.

Det officielle produktresumé (SmPC) skal konsulteres for godkendte advarsler og kontraindikationer, da disse ikke er tilgængelige i de indsamlede data.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger kun på modelscore. Der er ingen kliniske forsøg og ingen direkte data for colchicin mod malaria, og den toksicitet, der følger af det snævre terapeutiske indeks, gør en antiparasitær anvendelse tvivlsom.

**For at komme videre kræves:**
- In vitro-data for colchicins aktivitet mod P. falciparum og selektivitet over for humane celler
- Præklinisk dokumentation i dyremodeller for effekt ved tolerable doser
- Detaljerede data om virkningsmekanisme og sikkerhedsoplysninger fra produktresuméet
- Vurdering af interaktioner med gængse malariamidler (f.eks. chloroquin)

---

## Supplerende bemærkninger om andre forudsigelser

- **Familiær middelhavsfeber, autosomal dominant (score 99,38 %, evidensniveau L4):** Colchicin er allerede førstevalgsbehandling ved FMF og er en del af de oprindelige indikationer, så dette er i store træk en omdefinering af en eksisterende indikation snarere end ægte repurposing. Litteraturen (20 publikationer) består hovedsageligt af oversigtsartikler; der er ingen forsøg specifikt for denne undertype, så evidensen er indirekte. Anbefaling: forskningsspørgsmål.
- **Dermatofibrosarcoma protuberans (score 99,37 %, evidensniveau L5):** Ingen forsøg eller litteratur. Sygdommen drives af COL1A1-PDGFB-fusionen og behandles med kirurgi og imatinib, og der er ingen evidens for en forbindelse til colchicin. Anbefaling: Hold.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

