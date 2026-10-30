---
layout: default
title: Meloxicam
parent: Kun modelforudsigelse (L5)
nav_order: 526
evidence_level: L5
indication_count: 8
monitor_inn: "MELOXICAM"
predicted_indications: ["acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "myosclerosis", "brachyolmia", "pseudoachondroplasia", "rheumatoid nodulosis", "WHIM syndrome", "colobomatous microphthalmia-rhizomelic dysplasia syndrome"]
last_modified_at: 2026-10-30
description: "Meloxicam: forudsagt ny indikation Akromesomel dysplasi af Hunter-Thompson-typen (evidensniveau L5). Oprindelig indikation: Reumatoid artritis, slidgigt og juvenil idiopatisk artritis"
---

# Meloxicam
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **8** stk.
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

## Meloxicam: Fra slidgigt og reumatoid artritis til akromesomel dysplasi af Hunter-Thompson-typen
{: .text-alpha }

## Resumé i én sætning

Meloxicam er en NSAID-hæmmer (præferentiel COX-2-hæmmer), som i den viden, der er indgået i rapporten, er knyttet til reumatoid artritis, slidgigt og juvenil idiopatisk artritis.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **akromesomel dysplasi af Hunter-Thompson-typen**, men der er **ingen kliniske forsøg** og **ingen publikationer** i de data, der er samlet til denne rapport. Forudsigelsen er derfor ren modelforudsigelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Reumatoid artritis, slidgigt og juvenil idiopatisk artritis (relationer registreret i vidensgrafen; godkendelsesteksten for det danske produkt er ikke angivet) |
| Forudsagt ny indikation | Akromesomel dysplasi af Hunter-Thompson-typen |
| TxGNN-forudsigelsesscore | 0,9992 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ikke detaljerede data om virkningsmekanismen for meloxicam i de data, der er samlet til denne rapport. Meloxicam er kendt som en præferentiel COX-2-hæmmer med smertestillende og antiinflammatorisk effekt ved ledlidelser. Det begrænser mulighederne for en mekanistisk vurdering.

Akromesomel dysplasi af Hunter-Thompson-typen er en sjælden skeletdysplasi, som skyldes funktionstabsvarianter i CDMP1/GDF5 og påvirker udviklingen af bruskvæv i lemmerne. Meloxicam virker ikke på GDF5-signalering eller på den underliggende udviklingsdefekt. Den høje score stammer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens for en reel terapeutisk sammenhæng.

Andre forudsigelser på listen følger samme mønster. Den mest plausible kandidat er **reumatoid nodulose** (score 0,9951), som ligger tæt på den kendte indikation reumatoid artritis, og hvor meloxicam i bedste fald kan lindre symptomer fra led. NSAID'er påvirker dog ikke dannelsen af noduli. Ved pseudoachondroplasi kan symptomlindring ved sekundær slidgigt tænkes, men der er ingen evidens for effekt på den COMP-relaterede sygdomsproces.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der foreligger i øjeblikket ingen relateret litteratur.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104143007 | Animeloxan (aniMedica GmbH) | Oral suspension | Indikationstekst er ikke angivet i de foreliggende data |

Der er registreret 1 tilladelse (enkeltstofpræparat, gyldig).

---

## Sikkerhedsovervejelser

Oplysninger fra produktresuméet om advarsler og kontraindikationer foreligger ikke i de data, der er samlet til denne rapport. Se det godkendte produktresumé (SmPC).

- **Kontraindikationsrelationer i vidensgrafen** (ikke mærkningstekst): hypertension, nyresygdom og nedsat nyrefunktion, kongestiv hjerteinsufficiens, hjerte-kar-sygdom, hjertesygdom, myokardieinfarkt, koronar trombose, apopleksi/cerebrovaskulær sygdom, cerebralt infarkt, aktivt peptisk mavesår, gastritis, blodkoagulationssygdom, diabetes mellitus, diabetisk ketoacidose, hyperlipidæmi (inkl. familiær), anæmi, hæmoglobinopati, pyoureter og misbrug/afhængighed.
- **Lægemiddelinteraktioner** (100 registreret; udvalgte):
  - Moderate: hydrocortison, dexamethason, betamethason, triamcinolon, budesonid (kortikosteroider), acetylsalicylsyre, metformin, glimepirid, chlorpropamid, mesalazin, balsalazid, aprepitant, vancomycin, kanamycin, kaliumcitrat, kaliumbicarbonat, natriumsulfat, picosulfat og polyethylenglycol med elektrolytter.
  - Mindre: linaclotid.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på scoren fra TxGNN-modellen (deep learning) uden kliniske forsøg eller publikationer. Der er ingen plausibel mekanisme, og scoren afspejler sandsynligvis ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Evidensniveauet er L5.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) for meloxicam
- Godkendt produktresumé med advarsler, kontraindikationer og godkendt indikationstekst for det danske præparat
- Prækliniske eller kliniske data, der direkte undersøger meloxicam ved akromesomel dysplasi af Hunter-Thompson-typen
- Hvis der ønskes et realistisk spor, bør man i stedet vurdere reumatoid nodulose, hvor kun symptomlindring er plausibel, og hvor der også mangler evidens
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

