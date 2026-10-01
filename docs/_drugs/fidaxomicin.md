---
layout: default
title: Fidaxomicin
parent: Kun modelforudsigelse (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

# Fidaxomicin: Fra Clostridioides difficile-infektion til stafylokok-skoldet hud-syndrom

## Resumé i én sætning

Fidaxomicin er et smalspektret makrocyklisk antibiotikum, som oprindeligt anvendes mod *Clostridioides difficile*-infektion (baseret på baggrundsviden, da indikationsteksten ikke er angivet i data). TxGNN-modellen forudsiger, at det kan have effekt ved **stafylokok-skoldet hud-syndrom (SSSS)**. Der er dog **ingen kliniske forsøg og ingen publikationer**, der understøtter forudsigelsen, som udelukkende er modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | *C. difficile*-infektion (baggrundsviden; indikationstekst ikke angivet i den danske registrering) |
| Forudsagt ny indikation | Stafylokok-skoldet hud-syndrom (staphylococcal scalded skin syndrome) |
| TxGNN-forudsigelsesscore | 99,71 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig (eller ej)?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i datagrundlaget. Ud fra baggrundsviden hæmmer fidaxomicin bakterielt RNA-polymerase og er markedsført til behandling af *C. difficile*-infektion. Modellens forudsigelse hviler formentlig på, at både *C. difficile* og *Staphylococcus aureus* er grampositive bakterier, og at lægemidlet derfor knyttes til sygdomme forårsaget af grampositive organismer.

Den mekanistiske sammenhæng er svag. SSSS er en toksinmedieret hudsygdom forårsaget af eksfoliative toksiner fra *S. aureus*. Fidaxomicin har kun begrænset rapporteret aktivitet mod stafylokokker og optages stort set ikke systemisk efter oral indtagelse. Det passer dårligt til en systemisk toksinmedieret sygdom. Koblingen er derfor kun plausibel på niveau med grampositiv antibakteriel klasse.

TxGNN forudsiger også andre indikationer med næsten identiske scorer (ca. 99,7 %). De vurderes alle som svagt underbyggede:

- **Bulløs impetigo og impetigo:** Overfladiske hudinfektioner med *S. aureus* (og *S. pyogenes*). Oralt fidaxomicin forbliver hovedsageligt i tarmlumen og når ikke hudlæsionerne. Der findes allerede etablerede lokale og systemiske behandlinger.
- **Inhalationsbotulisme:** Skyldes præformeret neurotoksin, ikke bakteriel vækst. Antibiotika neutraliserer ikke toksin, og behandlingen bygger på antitoksin og understøttende pleje. Der er ingen oplagt mekanisme for en fidaxomicineffekt.
- **Toksinmedieret infektiøs botulisme:** Den biologisk mest plausible kandidat, fordi *C. botulinum* vokser i tarmen, og fidaxomicin virker lokalt i tarmen mod clostridier. Antibiotika er dog ikke standardbehandling, da bakterielyse kan frigive mere toksin. Der kræves præklinisk arbejde (in vitro og dyremodeller), før klinisk anvendelse kan overvejes.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104752610 | Dificlir (Tillotts Pharma GmbH) | Filmovertrukne tabletter (oral) | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Der foreligger ingen sikkerhedsdata i datagrundlaget (ingen registrerede lægemiddelinteraktioner, advarsler eller kontraindikationer). Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er rent modelbaseret (evidensniveau L5) uden kliniske forsøg eller litteratur. Fidaxomicins farmakokinetik (minimal systemisk absorption) og mekanisme passer dårligt til de forudsagte hud- og toksinmedierede sygdomme. Der findes desuden allerede etablerede behandlinger.

**For at komme videre kræves følgende:**
- Produktresumé (SmPC) fra Lægemiddelstyrelsen med advarsler og kontraindikationer, da sikkerhedsscreening ikke kan gennemføres uden dem
- Detaljerede data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Præklinisk dokumentation (in vitro-aktivitet mod *S. aureus* og *C. botulinum*, dyremodeller), især for toksinmedieret infektiøs botulisme som den mest plausible kandidat
- Vurdering af rutekompatibilitet (oral tablet mod hud- eller systemiske indikationer) og ligheden med den oprindelige indikation

*Resultaterne er udelukkende til forskningsformål og udgør ikke medicinsk rådgivning. Lægemiddelkandidater til nye indikationer kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

