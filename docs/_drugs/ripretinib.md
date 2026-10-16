---
layout: default
title: Ripretinib
parent: Kun modelforudsigelse (L5)
nav_order: 724
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ripretinib: forudsagt ny indikation Multipel endokrin neoplasi (evidensniveau L5). Oprindelig indikation: Ikke oplyst i de indsamlede data (indikationsteksten i den danske god…"
monitor_inn: "Ripretinib"
predicted_indications: ["multiple endocrine neoplasia", "multiple endocrine neoplasia", "HER2 positive breast carcinoma", "HER2 positive breast carcinoma", "malignant catarrh", "malignant catarrh", "infectious bovine rhinotracheitis", "infectious bovine rhinotracheitis", "cytomegalovirus infection", "cytomegalovirus infection"]
---

# Ripretinib
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

# Ripretinib: Fra godkendt indikation til multipel endokrin neoplasi

## Opsummering i én sætning

Ripretinib er en tyrosinkinasehæmmer, som er markedsført i Danmark som tabletten QINLOCK. Den originale godkendte indikation fremgår ikke af de data, der er indsamlet til denne rapport. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **multipel endokrin neoplasi**, men der er **ingen kliniske forsøg** og **ingen publikationer** specifikt for denne indikation, så forudsigelsen hviler udelukkende på modellen.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Original indikation | Ikke oplyst i de indsamlede data (indikationsteksten i den danske godkendelse er tom) |
| Forudsagt ny indikation | Multipel endokrin neoplasi |
| TxGNN-forudsigelsesscore | 98,84 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i de indsamlede data. Ud fra den information, der foreligger, er ripretinib en såkaldt "switch-control" tyrosinkinasehæmmer, der primært er rettet mod KIT og PDGFRA. In vitro hæmmer den desuden andre kinaser, bl.a. RET, VEGFR2 og TIE2.

Der er en teoretisk sammenhæng, fordi aktiverende RET-mutationer er årsag til MEN2 (multipel endokrin neoplasi type 2). Ripretinib er dog ikke en etableret RET-selektiv hæmmer, og den høje score (98,84 %) er alene en modelprediktion. Koblingen kan ikke verificeres ud fra de foreliggende data.

Andre indikationer i modellens topliste er mindre plausible:
- **HER2-positiv brystkræft** (score 98,3 %): Ripretinibs primære mål er ikke HER2 eller dets signalpartnere. Den eneste tilknyttede publikation er en generel oversigtsartikel om kinasehæmmere.
- **Malignt katarralfeber** og **infektiøs bovin rhinotracheitis** (score 98,3 %): Det er veterinære virussygdomme hos drøvtyggere uden plausibel kobling til ripretinib. Forudsigelserne ligner artefakter fra vidensgrafen.
- **Cytomegalovirusinfektion** (score 98,2 %): En værtsrettet kinasehæmning er tænkelig, men der er ingen dokumenteret antiviral aktivitet, og sikkerheden hos immunsupprimerede patienter er en bekymring.

## Kliniske forsøg

Der er i øjeblikket ingen registrerede kliniske forsøg for denne indikation.

## Litteraturevidens

Der er ingen litteratur specifikt for multipel endokrin neoplasi. For forudsigelsen om HER2-positiv brystkræft findes alene følgende generelle oversigtsartikel:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Oversigtsartikel | Pharmacological Research | Opdateret oversigt over egenskaber ved FDA-godkendte småmolekylære proteinkinasehæmmere. Indeholder ingen indikationsspecifik klinisk evidens for ripretinib ved brystkræft. |

## Information om markedet i Danmark

| Tilladelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28106510020 | QINLOCK (Deciphera Pharmaceuticals (Netherlands) B.V.) | Tabletter | Indikationstekst ikke angivet |

## Cytotoksicitet

Ripretinib er et antineoplastisk lægemiddel (kinasehæmmer, målrettet behandling). De indsamlede data indeholder ikke detaljerede toksicitetsoplysninger.

| Punkt | Indhold |
|------|------|
| Klassifikation | Målrettet behandling (tyrosinkinasehæmmer) |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Emetogenicitet | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Monitoreringspunkter | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Håndteringsbeskyttelse | Følg gældende regler for håndtering af cytotoksiske lægemidler, og se SmPC |

## Sikkerhedsovervejelser

Der er registreret **90 lægemiddelinteraktioner** i interaktionsdatabasen. Blandt de viste er følgende af alvorlig (Major) grad:
- **Clarithromycin**
- **Cobicistat**

Der er registreret en række interaktioner af moderat grad, bl.a. med pioglitazon, rosiglitazon, troglitazon, repaglinid, canagliflozin, aprepitant, rolapitant, dexamethason, cimetidin, miconazol, clotrimazol, fidaxomicin, eliglustat, metreleptin, glycerolphenylbutyrat, deferasirox, fostamatinib og selexipag.

Oplysninger om advarsler og kontraindikationer foreligger ikke i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er alene baseret på modellen (evidensniveau L5), uden kliniske forsøg eller indikationsspecifik litteratur. Virkningsmekanismen er ikke dokumenteret i de tilgængelige data, og flere af de øvrige forudsagte indikationer er biologisk implausible (veterinære sygdomme). Sikkerhedsdata fra produktresuméet mangler desuden, hvilket blokerer den videre sikkerhedsscreening.

**For at komme videre kræves følgende:**
- Hent og gennemgå produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikation)
- Indhent data om virkningsmekanisme fra DrugBank
- Gennemfør en systematisk litteraturgennemgang af ripretinibs aktivitet over for RET og ved MEN2 (præklinisk og klinisk)
- Vurder, om præklinisk evidens (L4) kan etableres, før kliniske forsøg overvejes
- Medtag en samlet vurdering af interaktionsrisikoen, især ved samtidig behandling med stærke CYP3A-hæmmere som clarithromycin og cobicistat
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

