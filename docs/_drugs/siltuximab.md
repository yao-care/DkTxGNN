---
layout: default
title: Siltuximab
parent: Kun modelforudsigelse (L5)
nav_order: 761
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Siltuximab: forudsagt ny indikation Ekstrakutant mastocytom (evidensniveau L5). Oprindelig indikation: Castlemans sygdom"
monitor_inn: "Siltuximab"
predicted_indications: ["extracutaneous mastocytoma", "extracutaneous mastocytoma", "hepatic infarction", "hepatic infarction", "hepatic veno-occlusive disease", "hepatic veno-occlusive disease", "peliosis hepatis", "peliosis hepatis", "Kaposi's sarcoma (disease)", "Kaposi's sarcoma (disease)"]
---

# Siltuximab
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

# Siltuximab: Fra Castlemans sygdom til ekstrakutant mastocytom

## Resumé i én sætning

Siltuximab er et lægemiddel, der oprindeligt anvendes til behandling af Castlemans sygdom (og i vidensgrafen også Kimuras sygdom). TxGNN-modellen forudsiger, at det kan have effekt på **ekstrakutant mastocytom**. Der er dog **ingen kliniske forsøg og ingen publikationer** for denne indikation, så forudsigelsen er rent beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Castlemans sygdom (kilde: vidensgrafen; godkendt indikationstekst for det danske produkt er ikke tilgængelig i de indsamlede data) |
| Forudsagt ny indikation | Ekstrakutant mastocytom |
| TxGNN-forudsigelsesscore | 99,64 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen foreligger ikke i de data, der er indsamlet til denne rapport. Siltuximab er dog kendt som et monoklonalt antistof mod interleukin-6 (IL-6). Dets effekt ved Castlemans sygdom, hvor IL-6 er en central drivkraft, er dokumenteret.

IL-6-signalering er beskrevet som en mulig faktor i mastcelleproliferation og -aktivering, hvilket giver en teoretisk forbindelse til mastocytom. Forbindelsen er imidlertid spinkel: der er ingen understøttende kliniske data eller litteratur i datagrundlaget, og den høje score er udelukkende en modelberegning.

**Andre forudsigelser fra modellen** (alle uden kliniske forsøg):
- **Hepatisk infarkt** (99,44 %): Ingen klar mekanistisk begrundelse, da tilstanden primært er vaskulær/iskæmisk.
- **Hepatisk veno-okklusiv sygdom** (99,40 %): Svag teoretisk begrundelse via cytokinmedieret endotelaktivering.
- **Peliosis hepatis** (99,29 %): Indirekte forbindelse via Castleman-lignende inflammatoriske tilstande.
- **Kaposis sarkom** (99,28 %): Biologisk plausibel, da HHV-8/KSHV og IL-6 (viralt og humant) driver både Kaposis sarkom og HHV-8-associeret multicentrisk Castlemans sygdom. Der findes én oversigtsartikel (indirekte evidens), men ingen forsøg specifikke for Kaposis sarkom. Evidensniveauet er her L4 med vurderingen "forskningsspørgsmål".

Bemærk: Flere indikationer optræder dobbelt i de modtagne data (dubletter); hver er kun medtaget én gang her.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret for ekstrakutant mastocytom.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur for ekstrakutant mastocytom.

Til information findes der for den alternative forudsigelse Kaposis sarkom følgende indirekte kilde:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [39970477](https://pubmed.ncbi.nlm.nih.gov/39970477/) | 2024 | Oversigtsartikel | AIDS Reviews | Gennemgang af Castlemans sygdoms forskellige ætiologier, herunder virusinfektioner (bl.a. HHV-8) og mekanismer bag multicentrisk Castlemans sygdom |

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105331813 | Sylvant (Recordati (Netherlands) B.V.) | Pulver til koncentrat til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der er identificeret 100 mulige interaktioner i interaktionsdatabasen (DDInter); et udvalg af de første 20 er gennemgået:

- **Alvorlig (Major):** Deferipron
- **Moderat:** simvastatin, apixaban, warfarin, rivaroxaban, dicoumarol, lidocain, hydrocodon, theophyllin, roflumilast, aminophyllin, oxtriphyllin, tacrolimus, fentanyl, tetanustoksoid-vaccine, nifedipin
- **Mindre (Minor):** zinksulfat, zinkacetat, zinkglukonat, zinkklorid

Mange af de moderate interaktioner gælder lægemidler med snæver terapeutisk bredde eller CYP-metabolisme (fx warfarin, tacrolimus, theophyllin). Det er i overensstemmelse med, at hæmning af IL-6 kan normalisere CYP-enzymaktivitet. Dette er en generel vurdering og ikke hentet fra de indsamlede data.

For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC), da disse data ikke er tilgængelige.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for ekstrakutant mastocytom bygger udelukkende på en modelscore (evidensniveau L5), uden kliniske forsøg, litteratur eller bekræftet virkningsmekanisme. Blandt de øvrige forudsigelser er Kaposis sarkom den mest biologisk plausible (L4), men også her mangler direkte evidens.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen (afgørende for sikkerhedsscreening)
- Den godkendte indikationstekst for Sylvant i Danmark
- Systematisk litteratursøgning og søgning efter forsøg specifikt for ekstrakutant mastocytom og IL-6-hæmning
- Overvejelse af at prioritere Kaposis sarkom som forskningsspørgsmål, med målrettet søgning efter data om KSHV-associeret inflammatorisk cytokinsyndrom
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

