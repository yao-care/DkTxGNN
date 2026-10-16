---
layout: default
title: Iohexol
parent: Kun modelforudsigelse (L5)
nav_order: 448
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Iohexol: forudsagt ny indikation Insomni (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (røntgenkontraststof)"
---

# Iohexol
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

# Iohexol: Fra røntgenkontraststof til søvnløshed (insomni)

## Resumé

Iohexol er et jodholdigt, ikke-ionisk, vandopløseligt røntgenkontraststof, som markedsføres i Danmark under navnet Omnipaque.
TxGNN-modellen forudsiger, at det kan have effekt mod **insomni**, men der er **ingen kliniske forsøg** og **ingen publikationer** for denne indikation.
Forudsigelsen vurderes som en sandsynlig modelartefakt uden farmakologisk begrundelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (røntgenkontraststof) |
| Forudsagt ny indikation | Insomni |
| TxGNN-prædiktionsscore | 99,87 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Iohexol er dog et velkendt ikke-ionisk, jodholdigt kontraststof, som er farmakologisk inaktivt og anvendes til billeddiagnostik.

Der er ingen kendt aktivitet på søvnrelaterede mål som GABA-, orexin- eller histaminreceptorer. Der er derfor ingen plausibel mekanistisk sammenhæng mellem den oprindelige anvendelse (kontrastmiddel) og insomni.

Den høje score (0,9987) skyldes sandsynligvis træk i grafnetværket, f.eks. fælles lægemiddelinteraktioner, og ikke reel biologisk sammenhæng. Forudsigelsen understøttes ikke af kliniske forsøg eller publiceret litteratur.

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur for insomni.

For fuldstændighedens skyld: Modellen rangerer også andre forudsigelser med lignende svag evidens (angst, leddegigt, antithrombinmangel type 2, faktor 5-overskud med spontan trombose). Litteraturen for angst og leddegigt er tilfældig og beskriver iohexol som procedurekontekst, målemetode (f.eks. måling af glomerulær filtrationshastighed) eller bivirkningsrapporter, ikke som behandling. Eksempelvis beskriver en case report (PMID [35286798](https://pubmed.ncbi.nlm.nih.gov/35286798/), 2022) fatal multiorgansvigt efter gentagen jodholdig kontrastinjektion hos en patient i lavdosis methotrexat.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101197284 | Omnipaque (GE Healthcare AS) | Injektionsvæske, opløsning | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er identificeret 100 mulige interaktioner. Blandt de væsentlige (Major) er:
  - Metformin
  - Amphotericin B (inkl. lipidkompleks)
  - Vancomycin, kanamycin og neomycin
  - Levofloxacin
  - Systemiske kortikosteroider (hydrocortison, dexamethason, betamethason, triamcinolon)
  - Mesalazin og balsalazid
  - Bupropion
  - Morphin
  - Metoclopramid
  - Diethylpropion og phentermin
  - Dronabinol

  Mannitol er klassificeret som Moderate.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der er ingen kliniske forsøg eller relevant litteratur, og der er ingen plausibel farmakologisk mekanisme for iohexol ved insomni. Den høje TxGNN-score vurderes som en modelartefakt.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) og godkendt indikationstekst
- Sikkerhedsoplysninger fra produktresuméet (advarsler og kontraindikationer)
- Prækliniske data, der understøtter en effekt på søvnrelaterede mål, før yderligere vurdering er berettiget
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

