---
layout: default
title: Rozanolixizumab
parent: Kun modelforudsigelse (L5)
nav_order: 390
evidence_level: L5
indication_count: 10
---

# Rozanolixizumab
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

# Rozanolixizumab: Fra IgG-medieret autoimmun sygdom til bronkitis (undersøgelse)

## Sammenfatning i en sætning

Rozanolixizumab er et anti-FcRn monoklonalt antistof; dokumentationen for den formelt godkendte indikation er **manglende** i denne bevispapper, selvom understøttende rationale-tekst indikerer, at det blev udviklet til IgG-medierede autoimmune tilstande (f.eks. generaliseret myasthenia gravis, ITP, CIDP). TxGNN-modellens bedst rangerede forudsigelse er **Bronkitis**, men dette er en udelukkende på vidensgrafen baseret forudsigelse med **0 kliniske forsøg** og **0 publikationer**, og modellens egen mekanistiske rationale argumenterer for, at det biologiske link er svagt — muligvis endda modsatrettet til gavnlig virkning.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Original indikation | Ikke dokumenteret (datamangler — ingen godkendt indikationstekst på fil) |
| Forudsagt ny indikation | Bronkitis |
| TxGNN forudsigelsesscore | 95.28% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afventende |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i den strukturerede post (`original_moa`: datamangler). Baseret på det rationale for omformål, der er tilvejebragt sammen med forudsigelserne, er Rozanolixizumab et monoklonalt antistof mod neonatale Fc-receptor (FcRn), der blokerer FcRn-medieret IgG-genbrug og derved sænker de cirkulerende IgG-koncentrationer. Dets tilsigtede sygdomme er IgG-medierede autoimmune tilstande såsom generaliseret myasthenia gravis (gMG), immun trombocytopeni (ITP) og kronisk inflammatorisk demyeliniserende polyneuropati (CIDP).

For den bedst rangerede forudsagt indikation, **Bronkitis**, understøtter bevispapperets egen mekanistiske analyse **ikke** biologisk plausibilitet: bronkitis skyldes primært infektion eller luftvejsirritation, uden kendt patofysiologisk sammenhæng med FcRn/IgG-genbrugsstien. Fordi anti-FcRn-terapi sænker beskyttende IgG-niveauer, kunne det teoretisk *øge* modtageligheden for luftvejsinfektioner snarere end at behandle bronkitis — en virkning modsat terapeutisk fordel. TxGNN-scoren afspejler mest sandsynligt nærhed inden for vidensgrafen snarere end egentlig biologisk plausibilitet.

De øvrige kandidater i denne batch (plasmacelle-myelom, indolent plasmacelle-myelom, hemoglobinopati, mavekræft) beskrives i deres eget rationale som indirekte, uvaliderede eller mekanistisk urelaterede associationer — ingen understøttes af kliniske eller præ-kliniske data i denne pakke. Samlet set er dette blot et screenings-stadie signal, ikke en kandidat klar til yderligere evaluering.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret

---

## Bevis fra litteratur

Der er i øjeblikket ingen tilgængelig relevant litteratur

---

## Information om det danske marked

Rozanolixizumab har i øjeblikket **ingen markedsføringstilladelse** i Danmark (0 licenser på fil; markedsstatus: Ikke markedsført).

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation. Bemærk: TFDA/SmPC-advarsler og kontraindikationsdata kunne ikke hentes til denne evaluering (blokerende datamangler — DG001), og ingen registreringer af lægemiddel-lægemiddel-interaktioner blev fundet.

---

## Konklusion og næste trin

**Beslutning: Afventende**

**Rationale:**
- Den bedst rangerede forudsigelse (Bronkitis) har intet understøttende bevis fra kliniske forsøg eller litteratur, og modellens egen mekanistiske rationale argumenterer imod biologisk plausibilitet. Kombineret med medicinerets manglende markedstering i Danmark og en blokerende datamangler i sikkerhed og etiket-data, er der intet grundlag for at fortsætte i øjeblikket.

**For at fortsætte kræves følgende:**
- TFDA/SmPC-tilsvarende advarsler, kontraindikationer og ordinationsinformation (i øjeblikket blokerende — DG001)
- Bekræftet virkningsmekanisme og oprindelig godkendt indikation fra en primær regulatorisk eller DrugBank-kilde (DG002)
- Uafhængig mekanistisk eller præ-klinisk validering af enhver kandidatindikation før yderligere bevisindsamling
- Løbende overvågning for nye kliniske forsøgsregistreringer eller publikationer om Rozanolixizumab på tværs af de anførte kandidatindikationer

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

