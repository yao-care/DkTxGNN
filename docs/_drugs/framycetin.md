---
layout: default
title: Framycetin
parent: Kun modelforudsigelse (L5)
nav_order: 375
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-14
description: "Framycetin: forudsagt ny indikation Skleroserende cholangitis (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data"
monitor_inn: "framycetin"
predicted_indications: ["sclerosing cholangitis", "urinary tract infection (disease)", "congenital prothrombin deficiency", "Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis"]
---

# Framycetin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **7** stk.
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

# Framycetin: Fra lokal antibiotisk behandling til skleroserende cholangitis

## Resumé i én sætning

Framycetin er et aminoglykosid-antibiotikum (neomycin B), der i Danmark er godkendt i både human- og veterinærlægemidler. Det oprindelige godkendte indikationsområde fremgår ikke af de data, der er sammenstillet til denne rapport. TxGNN-modellen forudsiger, at stoffet kan have effekt på **skleroserende cholangitis**, men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter forudsigelsen. Evidensen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data |
| Forudsagt ny indikation | Skleroserende cholangitis |
| TxGNN-forudsigelsesscore | 99,66 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 3 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Data om virkningsmekanisme (MOA) er ikke tilgængelige i de data, der er sammenstillet til denne rapport. Framycetin er et aminoglykosid, som hæmmer bakteriel proteinsyntese ved binding til 30S-ribosomet og har bred aktivitet mod gramnegative bakterier. Stoffet absorberes meget dårligt fra tarmen.

Den mulige sammenhæng med skleroserende cholangitis er løs og konceptuel. Ikke-absorberbare orale antibiotika, f.eks. vancomycin, er undersøgt ved primær skleroserende cholangitis via påvirkning af tarmens mikrobiom. En antibakteriel effekt i tarmlumen kunne derfor i princippet være relevant. Der findes dog ingen direkte data for framycetin, og aminoglykosider er ikke en etableret strategi ved denne sygdom.

Den høje TxGNN-score (0,997) er en ren modelforudsigelse og understøttes ikke af forsøg eller publikationer.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28100578370 | Benestermycin Vet. (Boehringer Ingelheim Vetmedica GmbH) | Intramammær suspension | Ikke angivet |
| 28100643674 | Canaural (Dechra Veterinary Products A/S) | Øredråber | Ikke angivet |
| 28101903697 | Proctosedyl (Orifarm A/S) | Rektalsalve | Ikke angivet |

Bemærk, at to af de tre produkter er veterinærlægemidler (Benestermycin Vet. og Canaural). Humant er kun Proctosedyl (rektalsalve) repræsenteret.

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige sikkerhedsdata fra produktresuméer, og der er ikke fundet registrerede lægemiddelinteraktioner i de sammenstillede data.

Generelt om aminoglykosider (klasseviden, ikke specifikke data for framycetin): Systemisk eksponering er forbundet med risiko for nyretoksicitet og ototoksicitet, hvilket er årsagen til, at framycetin primært anvendes lokalt.

Se i øvrigt det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Andre forudsagte indikationer

Modellen har også forudsagt følgende indikationer. Ingen af dem er understøttet af forsøg eller litteratur (alle L5, anbefaling: Hold).

| Rang | Sygdom | TxGNN-score | Vurdering |
|------|------|------|------|
| 2 | Urinvejsinfektion | 99,42 % | Biologisk plausibelt (gramnegativ aktivitet), men sikker opnåelse af terapeutiske urinkoncentrationer er problematisk pga. nefro- og ototoksicitet og dårlig oral absorption. Der findes bedre dokumenterede alternativer. |
| 3 | Medfødt protrombinmangel | 99,41 % | Ingen plausibel mekanistisk sammenhæng; sandsynligvis falsk positiv. |
| 4 | Ureaplasma-uretritis | 99,28 % | Svag rationale, da aminoglykosider generelt har begrænset effekt mod Ureaplasma. |
| 5 | Gonokok-uretritis | 99,28 % | Beskeden klasseplausibilitet, men ingen framycetin-specifik evidens, og resistens og toksicitet begrænser rollen. |
| 6 | Inflammatorisk uterussygdom | 99,18 % | Klasseplausibilitet (aminoglykosider bruges i bækkeninfektioner), men ingen data for framycetin og dårlig systemisk tolerabilitet. |
| 7 | Xanthogranulomatøs pyelonefritis | 99,18 % | Behandles primært kirurgisk; nefrotoksicitet er særligt problematisk i en allerede skadet nyre. |

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for skleroserende cholangitis bygger udelukkende på modellen (evidensniveau L5), uden forsøg, litteratur eller mekanistiske data for framycetin. Stoffets dårlige absorption og toksicitetsprofil ved systemisk brug taler imod en hurtig videreudvikling.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Produktresuméer (SmPC) med advarsler og kontraindikationer fra Lægemiddelstyrelsen, da sikkerhedsscreening ikke kan gennemføres uden dem
- Oplysninger om godkendte indikationer for de tre markedsførte produkter
- Præklinisk eller observationel evidens for en effekt af ikke-absorberbare aminoglykosider ved skleroserende cholangitis
- Vurdering af ruteforenelighed (påkrævet administrationsvej versus tilgængelige lægemiddelformer)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

