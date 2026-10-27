---
layout: default
title: Calcifediol
parent: Kun modelforudsigelse (L5)
nav_order: 148
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Calcifediol: forudsagt ny indikation Forældet betegnelse for D-vitaminmangel (evidensniveau L5). Oprindelig indikation: Hypercalcæmi, nefrocalcinose, forstyrrelser i fosfatomsætningen…"
monitor_inn: "calcifediol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "hereditary hypophosphatemic rickets", "vitamin D-dependent rickets"]
---

# Calcifediol
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

## Calcifediol: Fra rakitis og knoglemetaboliske sygdomme til D-vitaminmangel
{: .text-alpha }

## Resumé

Calcifediol (25-hydroxyvitamin D3) er den direkte forstadie til calcitriol og bruges oprindeligt ved sygdomme i calcium- og fosfatomsætningen, bl.a. rakitis, osteomalaci og renal osteodystrofi.
TxGNN-modellen forudsiger, at stoffet kan være effektivt ved **D-vitaminmangel** (en forældet sygdomsbetegnelse i ontologien).
Der er i de data, der er indsamlet til denne rapport, **ingen kliniske forsøg** og **ingen publikationer** direkte for denne indikation. Evidensen er derfor alene modelbaseret og mekanistisk.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hypercalcæmi, nefrocalcinose, forstyrrelser i fosfatomsætningen, hypofosfatæmi, rakitis, osteomalaci, renal osteodystrofi (fra TxGNN-vidensgrafen; godkendt indikationstekst for det danske produkt er ikke tilgængelig) |
| Forudsagt ny indikation | Forældet betegnelse for D-vitaminmangel |
| TxGNN-forudsigelsesscore | 99,99 % |
| Evidensniveau | L4 (mekanistisk, ingen kliniske studier) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails |

---

## Hvorfor er denne forudsigelse rimelig?

Data om lægemidlets detaljerede virkningsmekanisme er ikke tilgængelige i det indsamlede materiale. Ud fra kendt viden er calcifediol det cirkulerende forstadie til calcitriol og den vigtigste markør for D-vitaminstatus. Tilskud hæver direkte serum-25(OH)D og omgår leverens 25-hydroxylering, så mekanismen er biologisk ligetil.

D-vitaminmangel overlapper tydeligt med stoffets oprindelige indikationer (rakitis og osteomalaci). Den høje modelscore afspejler sandsynligvis nærhed i ontologien snarere end ny evidens. Calcifediol anvendes i flere lande allerede ved D-vitaminmangel, men det er ikke dokumenteret i de foreliggende data. Indikationen bør derfor ses som næsten on-label og ikke som egentlig repurposing.

Øvrige forudsagte indikationer i materialet (kort omtale):
- **Renal tubulær acidose** (score 99,86 %, L5, Hold): Ingen direkte mekanistisk sammenhæng. Calcifediol kan højst adressere knoglekomplikationer, ikke acidosen. Standardbehandling er alkali.
- **Hereditær hypofosfatæmisk rakitis** (score 99,76 %, L4, Research Question): Sygdommen skyldes renalt fosfattab (FGF23), og calcifediol kræver renal 1-alfa-hydroxylering, som hæmmes. Rollen er begrænset til samtidig D-vitaminmangel.
- **D-vitaminafhængig rakitis** (score 99,18 %, L4, Research Question): Stærk mekanistisk begrundelse for type 1B (CYP2R1-mangel), da calcifediol er produktet af det manglende enzymtrin. Type 1A og type 2 forventes ikke at reagere på samme måde.

---

## Dokumentation fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret for den forudsagte hovedindikation.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur for den forudsagte hovedindikation. For de øvrige forudsagte indikationer foreligger følgende indirekte litteratur:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [38337700](https://pubmed.ncbi.nlm.nih.gov/38337700/) | 2024 | Review | Nutrients | Gennemgang af rakitistyper og behandling med D-vitamin og analoger (relevant for hereditær hypofosfatæmisk rakitis) |
| [28548312](https://pubmed.ncbi.nlm.nih.gov/28548312/) | 2017 | Case report/review | Journal of Bone and Mineral Research | D-vitaminafhængig rakitis type 1B (25-hydroxylasemangel): 7 patienter fra 2 familier; sjælden eller overset tilstand |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107351325 | Defevix (Berlin-Chemie AG) | Bløde kapsler | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

**Kontraindikationer ifølge vidensgrafen** (fra TxGNN-vidensgrafen, ikke fra produktresuméet): nyresygdom, pyouretær, sarkoidose, hypercalcæmi, nefrocalcinose, forstyrrelser i fosfatomsætningen, nefrolithiasis (inkl. SLC26A1-relateret), akut uratnefropati, hyperfosfatæmi, hypervitaminose og arteriosclerosis obliterans.

**Lægemiddelinteraktioner** (71 registrerede i alt; et udvalg):
- **Alvorlige (Major):** cholecalciferol, calcitriol, burosumab
- **Moderate:** fosphenytoin, carbamazepin, barbiturater (amobarbital, butalbital, butabarbital), thiaziddiuretika (hydrochlorthiazid, bendroflumethiazid, benzthiazid, chlorothiazid, chlorthalidon), aluminiumhydroxid, galdesyrebindere (cholestyramin, colesevelam, colestipol), digitoxin, topisk calcipotriol og topisk calcitriol

Oplysninger om advarsler og kontraindikationer fra det godkendte produktresumé (SmPC) er ikke tilgængelige i det indsamlede materiale. Se det godkendte produktresumé for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Den mekanistiske sammenhæng er enkel og indikationen ligger tæt på stoffets oprindelige anvendelse, og produktet er allerede markedsført i Danmark. Der er dog ingen kliniske forsøg eller litteratur for indikationen, og sikkerhedsdata fra produktresuméet mangler, så evidensen er kun L4.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer, godkendt indikation)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Litteratursøgning efter kliniske studier med calcifediol ved D-vitaminmangel
- Overvågning af serumcalcium, fosfat, nyrefunktion og 25(OH)D samt vurdering af interaktioner (især andre D-vitaminpræparater, thiazider og antiepileptika)
- For D-vitaminafhængig rakitis: bekræftelse af type 1B-genotype før anvendelse
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

