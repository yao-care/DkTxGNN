---
layout: default
title: Tecovirimat
parent: Kun modelforudsigelse (L5)
nav_order: 797
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "tecovirimat"
predicted_indications: ["hordeolum", "vibrio infectious disease", "Klebsiella infectious disease", "noma", "coinfection", "arbovirus infection", "equine infectious anemia", "idiopathic recurrent and disabling cutaneous herpes", "Astroviridae infectious disease", "Arterivirus infectious disease"]
description: "Tecovirimat: forudsagt ny indikation Hordeolum (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Tecovirimat
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

## Tecovirimat: Hordeolum
{: .text-alpha }

## Et-sætnings-resumé

Tecovirimat er et antiviralt middel, der oprindeligt anvendes mod orthopoxvirusinfektioner som kopper (smallpox), kokopper og relaterede virale hudsygdomme. TxGNN-modellen forudsiger, at lægemidlet kan have effekt mod **hordeolum** (bygkorn) med en score på **0,9966**, men der er **ingen kliniske forsøg** og **ingen publikationer**, der understøtter forudsigelsen. Forudsigelsen vurderes som en sandsynlig netværksartefakt uden biologisk begrundelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Hordeolum |
| TxGNN-forudsigelsesscore | 0.9966 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger i de indsamlede data ingen detaljerede oplysninger om virkningsmekanismen. Ifølge den faglige vurdering hæmmer tecovirimat orthopoxvirussets VP37-envelopeprotein (F13L-homolog) og dermed dannelsen af ekstracellulært omsluttet virus. Mekanismen er specifik for orthopoxvirus.

Hordeolum er typisk en lokal, stafylokok-bakteriel infektion i øjenlågets kirtler. Tecovirimat har ingen kendt antibakteriel aktivitet, og der er derfor ingen troværdig mekanistisk sammenhæng mellem den oprindelige og den forudsagte indikation. Den høje score kommer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke biologisk evidens.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106491420 | Tecovirimat SIGA (SIGA Technologies Netherlands B.V.) | Kapsler, hårde | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Andre forudsagte indikationer (til orientering)

Ni øvrige forudsigelser med scorer fra 0,9962 til 0,9965 er også gennemgået. Alle undtagen én mangler kliniske forsøg og litteratur og har ingen plausibel mekanisme (evidensniveau L5, Hold):

| Forudsagt indikation | Vurdering |
|------|------|
| Vibrio-infektion | Bakteriel; ingen mekanisme |
| Klebsiella-infektion | Bakteriel; ingen mekanisme |
| Noma | Polymikrobiel, overvejende bakteriel; ingen mekanisme |
| Arbovirusinfektion | RNA-vira uden VP37-homolog; svag |
| Ekvin infektiøs anæmi | Lentivirus og veterinær sygdom; ingen mekanisme |
| Idiopatisk tilbagevendende og invaliderende kutan herpes | Herpesvirus; effektive standardbehandlinger findes |
| Astroviridae-infektion | Ikke-omsluttet RNA-virus; ingen mekanisme |
| Arterivirus-infektion | Dyrevira; ingen mekanisme |

**Koinfektion (rang 5)** adskiller sig ved at have 20 publikationer (evidensniveau L4, anbefaling: forskningsspørgsmål). Litteraturen består dog af kasuistikker, reviews og retningslinjer om **mpox** (et orthopoxvirus inden for tecovirimats virkningsspektrum) hos patienter med samtidige infektioner som HIV, varicella-zoster og syfilis. "Koinfektion" er ikke en selvstændig sygdom, så signalet afspejler brug mod mpox hos koinficerede patienter og ikke en ny indikation. En artikel om metabolismeveje for mpox-lægemidler ved HIV-koinfektion er relevant for interaktioner med antiretrovirale midler. Der er ingen randomiserede forsøg i de indsamlede data. Studiedesign er udledt af titler og bør verificeres.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om hordeolum mangler både kliniske forsøg, litteratur og biologisk rimelighed, da tecovirimat er orthopoxvirus-specifikt og hordeolum er bakterielt. Scoren er sandsynligvis en grafartefakt.

**For at komme videre kræves følgende:**
- Hentning af produktresuméet (SmPC) for advarsler, kontraindikationer og godkendt indikationstekst
- Data om virkningsmekanisme (MOA) fra DrugBank
- Hvis der ønskes et sporbart signal, bør fokus flyttes til mpox hos koinficerede patienter, med systematisk gennemgang af randomiserede forsøg (fx PALM007 og STOMP), som ikke indgår i de indsamlede data, samt vurdering af interaktioner med antiretrovirale midler
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

