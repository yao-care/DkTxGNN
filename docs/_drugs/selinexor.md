---
layout: default
title: Selinexor
parent: Kun modelforudsigelse (L5)
nav_order: 754
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Selinexor: forudsagt ny indikation Lægemiddelinduceret osteoporose (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (indikationsteksten for markedsfø…"
---

# Selinexor
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

# Selinexor: Fra manglende registreret indikation til lægemiddelinduceret osteoporose

## Kort resumé

Selinexor er en selektiv hæmmer af nuklear eksport (XPO1/CRM1-hæmmer) og er markedsført i Danmark som NEXPOVIO. Der foreligger ingen godkendt indikationstekst i de data, der er sammenstillet til denne rapport. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **lægemiddelinduceret osteoporose**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning. Forudsigelsen er derfor rent beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (indikationsteksten for markedsføringstilladelsen er tom) |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose |
| TxGNN-forudsigelsesscore | 99,22 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Selinexor hæmmer XPO1 (CRM1), et protein der transporterer en række tumorsuppressorer og regulatoriske proteiner ud af cellekernen. De detaljerede mekanismedata var ikke tilgængelige i de sammenstillede data, men lægemidlets klasse er kendt som selektiv hæmmer af nuklear eksport og anvendes i kræftbehandling.

Der er ikke dokumenteret en direkte mekanistisk sammenhæng mellem XPO1-hæmning og lægemiddelinduceret osteoporose. Selinexor er forbundet med bivirkninger som kvalme, appetitløshed, vægttab og træthed, som muligvis kan påvirke knoglehelbredet indirekte. Dette er imidlertid spekulativt og ikke understøttet af data. Den høje score (0,992) bør derfor ses som en computerbaseret hypotese, der kræver validering, og ikke som tegn på dokumenteret effekt.

Det bør bemærkes, at modellen også rangerer flere brystkræftundertyper højt (HER2-positiv brystkræft, progesteronreceptor-negativ og -positiv brystkræft samt "normal breast-like"-undertypen, alle med scorer omkring 97-98 %). Heller ikke for disse findes der kliniske forsøg eller relevant litteratur. Den eneste tilknyttede publikation (PMID 36943683) handler om endometriekræft og ikke brystkræft, og koblingen skyldes sandsynligvis en søgeartefakt.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for denne indikation.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur for lægemiddelinduceret osteoporose.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106216419 | NEXPOVIO (Stemline Therapeutics B.V.) | Filmovertrukne tabletter | Indikationstekst ikke tilgængelig |

---

## Cytotoksicitet

Selinexor er et lægemiddel mod kræft (XPO1-hæmmer), og derfor gælder dette afsnit.

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (selektiv hæmmer af nuklear eksport) |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Emetogenicitetsklassifikation | Kvalme er en kendt bivirkning; se SmPC for klassifikation |
| Overvågningspunkter | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) for advarsler og forholdsregler |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er identificeret 81 interaktioner. Blandt de registrerede er flere af sværhedsgraden **Major**, bl.a. deferipron, samarium (153Sm) lexidronam, adalimumab, baricitinib, certolizumab pegol, cladribin og clozapin. Flere interaktioner af moderat grad er også registreret (bl.a. strontiumchlorid Sr-89, roflumilast, chloramphenicol, zidovudin, azathioprin, alemtuzumab, anakinra, canakinumab samt visse vacciner). Mange af disse vedrører additiv immunsuppression eller knoglemarvshæmning.

For øvrig sikkerhedsinformation, herunder advarsler og kontraindikationer, henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for lægemiddelinduceret osteoporose bygger udelukkende på modelscoren (evidensniveau L5), uden kliniske forsøg, litteratur eller dokumenteret mekanistisk sammenhæng. Desuden mangler oplysninger om den godkendte indikation og om advarsler og kontraindikationer.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (indikation, advarsler, kontraindikationer)
- Detaljerede data om virkningsmekanisme (f.eks. fra DrugBank)
- Præklinisk eller mekanistisk undersøgelse af XPO1-hæmning og knoglemetabolisme (osteoklaster/osteoblaster)
- Systematisk litteratursøgning og registersøgning efter kliniske forsøg for lægemiddelinduceret osteoporose
- Vurdering af, om selinexors kendte bivirkninger (vægttab, appetitløshed) udgør en risiko for knoglehelbredet snarere end en gevinst
- Manuel gennemgang af de højt rangerede brystkræftforudsigelser, da den tilknyttede litteratur ikke omhandler brystkræft
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

