---
layout: default
title: Pemigatinib
parent: Kun modelforudsigelse (L5)
nav_order: 644
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Pemigatinib: forudsagt ny indikation Multipel endokrin neoplasi (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data"
monitor_inn: "Pemigatinib"
predicted_indications: ["multiple endocrine neoplasia", "multiple endocrine neoplasia", "amenorrhea (disease)", "amenorrhea (disease)", "HER2 positive breast carcinoma", "HER2 positive breast carcinoma", "cytomegalovirus infection", "cytomegalovirus infection", "infectious bovine rhinotracheitis", "malignant catarrh"]
---

# Pemigatinib
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

## Pemigatinib: Fra ukendt oprindelig indikation til multipel endokrin neoplasi
{: .text-alpha }

## Resumé i én sætning

Pemigatinib er et målrettet kræftlægemiddel (FGFR-hæmmer), som er markedsført i Danmark, men for hvilket der i de data, der er indsamlet til denne rapport, ikke er angivet en godkendt indikationstekst.
TxGNN-modellen forudsiger, at lægemidlet kan være virksomt ved **multipel endokrin neoplasi**.
Forudsigelsen understøttes af **0 kliniske forsøg** og **0 publikationer**, så den er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data |
| Forudsagt ny indikation | Multipel endokrin neoplasi |
| TxGNN-forudsigelsesscore | 99,71 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de indsamlede data. Pemigatinib er dog kendt som en selektiv hæmmer af FGFR1-3 (fibroblastvækstfaktorreceptorer), og en mulig forbindelse kunne gå via FGFR-signalering i endokrine tumorer.

Denne kobling er ikke understøttet af de foreliggende data. De gener, der typisk knyttes til multipel endokrin neoplasi (MEN1 og RET), er ikke medlemmer af FGFR-signalvejen. Den høje score på 99,71 % afspejler en netværksbaseret grafforudsigelse og ikke klinisk eller litteraturbaseret dokumentation.

Det bør bemærkes, at den oprindelige indikation ikke fremgår af de indsamlede data, hvilket begrænser en vurdering af sammenhængen mellem oprindelig og ny indikation.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig for den primære forudsagte indikation.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28106368019 | Pemazyre | Tabletter | Ikke angivet i de indsamlede data |

Indehaver: Incyte Biosciences Distribution. Status: gyldig (monopræparat).

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (selektiv FGFR1-3-tyrosinkinasehæmmer) |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Overvågningspunkter | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) for advarsler og forholdsregler |

---

## Sikkerhedsovervejelser

Der foreligger ingen oplysninger om advarsler eller kontraindikationer i de indsamlede data. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

**Lægemiddelinteraktioner:** Der er identificeret 50 interaktioner i alt. Blandt de viste er følgende af alvorlighedsgraden **Major**:

- Aprepitant
- Dexamethason
- Clarithromycin
- Cobicistat
- Lumacaftor
- Chloramphenicol
- Erythromycin
- Ketoconazol
- Fluconazol

Interaktioner af moderat grad omfatter blandt andet cimetidin, metreleptin, clotrimazol, glycerolphenylbutyrat, troglitazon, deferasirox, ivacaftor, zafirlukast, griseofulvin, elagolix og osilodrostat.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5) uden kliniske forsøg eller litteratur, og der er ingen påviselig mekanistisk kobling mellem FGFR-hæmning og de gener, der driver multipel endokrin neoplasi.

**For at komme videre kræves følgende:**
- Oplysninger om den godkendte indikation og produktresumé fra Lægemiddelstyrelsen, herunder advarsler og kontraindikationer
- Data om virkningsmekanisme fra DrugBank
- Præklinisk eller mekanistisk dokumentation for FGFR-involvering i multipel endokrin neoplasi
- Systematisk litteratursøgning og søgning efter relevante kliniske forsøg
- Vurdering af administrationsvej og lægemiddelinteraktioner (især stærke CYP3A4-hæmmere og -induktorer) ved eventuelt videre arbejde

---

## Bemærkning om øvrige forudsigelser

De øvrige forudsigelser med høje scorer er lige så svagt understøttede (alle L5, anbefaling Hold):

- **Amenorré** (99,54 %): ingen plausibel mekanistisk kobling.
- **HER2-positiv brystkarcinom** (99,49 %): biologisk plausibel hypotese via FGFR-signalering og resistens over for HER2-rettet behandling, men den eneste litteratur er en generel oversigtsartikel om godkendte kinasehæmmere (PMID [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/), Roskoski, 2021, *Pharmacological Research*) uden sygdomsspecifik klinisk evidens.
- **Cytomegalovirusinfektion** (99,46 %): ingen understøttet mekanistisk kobling.
- **Infektiøs bovin rhinotracheitis** og **malignt katarr** (99,43 %): veterinære sygdomme uden human klinisk relevans, sandsynligvis artefakter i vidensgrafen.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

