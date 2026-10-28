---
layout: default
title: Felypressin
parent: Kun modelforudsigelse (L5)
nav_order: 349
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Felypressin: forudsagt ny indikation Lægemiddelinduceret osteoporose (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (godkendt indikationstekst er tom)"
monitor_inn: "felypressin"
predicted_indications: ["drug-induced osteoporosis", "severe nonproliferative diabetic retinopathy", "esotropia", "diabetic retinopathy", "bronchial adenomas/carcinoids childhood", "ductal or ductular proliferation", "chondroid hamartoma", "non-seminomatous lesion", "tumor of testis and paratestis", "pre-malignant neoplasm"]
---

# Felypressin
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

## Felypressin: Fra lokalbedøvelsestilsætning til lægemiddelinduceret osteoporose
{: .text-alpha }

## Resumé

Felypressin er et syntetisk vasopressinanalog, som markedsføres i Danmark som vasokonstriktor sammen med lokalbedøvelse (Citanest Dental Octapressin). TxGNN-modellen forudsiger, at det kan have effekt på **lægemiddelinduceret osteoporose**, men der er **ingen kliniske forsøg** og **ingen publikationer**, der understøtter forudsigelsen. Den er udelukkende baseret på modelberegning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (godkendt indikationstekst er tom) |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose |
| TxGNN-forudsigelsesscore | 0,9980 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger ingen detaljerede data om felypressins virkningsmekanisme i de data, der er sammenstillet til denne rapport. Felypressin er kendt som et syntetisk vasopressinanalog, der primært virker som V1-receptoragonist og giver vasokonstriktion. Det anvendes sammen med lokalbedøvelse for at forlænge og forstærke effekten.

Ud fra de foreliggende data kan der ikke påvises nogen plausibel mekanistisk sammenhæng mellem V1-receptoragonisme og knoglestofskifte eller glukokortikoidinduceret knogletab. Den høje score (0,9980) skal derfor ses som et rent modelresultat, der ikke er understøttet af forsøg eller litteratur. Scoren stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

### Øvrige forudsagte indikationer

Samtlige ti forudsigelser har evidensniveau L5 og anbefalingen Hold:

| Rang | Forudsagt indikation | Score | Bemærkning |
|----|------|------|------|
| 1 | Lægemiddelinduceret osteoporose | 0,9980 | Ingen påviselig mekanistisk sammenhæng |
| 2 | Svær non-proliferativ diabetisk retinopati | 0,9965 | Spekulativ; vasokonstriktion kan potentielt forværre retinal iskæmi |
| 3 | Esotropi | 0,9941 | Ingen mekanistisk sammenhæng; sandsynligvis artefakt |
| 4 | Diabetisk retinopati | 0,9939 | Som ovenfor; sikkerhedsspørgsmål ved vasokonstriktion |
| 5 | Bronkiale adenomer/karcinoider hos børn | 0,9919 | Uspecifik onkologiklasse-forudsigelse |
| 6 | Duktal/duktulær proliferation | 0,9919 | Identisk score med urelaterede termer |
| 7 | Kondroid hamartom | 0,9919 | Godartet læsion uden kendt relevans |
| 8 | Non-seminomatøs læsion | 0,9919 | Uspecifik forudsigelse |
| 9 | Tumor i testikel og paratestikulært væv | 0,9918 | Spekulativ |
| 10 | Præmalign neoplasi | 0,9917 | Bred og uspecifik kategori |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100484865 | Citanest Dental Octapressin (Dentsply DeTrey GmbH) | Injektionsvæske, opløsning | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

Der er ikke fundet interaktionsdata for felypressin i de sammenstillede data. Vær desuden opmærksom på, at felypressins vasokonstriktive virkning rejser et teoretisk sikkerhedsspørgsmål ved de forudsagte indikationer inden for diabetisk retinopati, hvor retinal iskæmi kunne forværres.

Se i øvrigt det godkendte produktresumé (SmPC) for sikkerhedsoplysninger, herunder advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden kliniske forsøg, litteratur eller plausibel mekanistisk sammenhæng (evidensniveau L5). Felypressins vasokonstriktive profil giver desuden en teoretisk sikkerhedsbekymring for flere af de forudsagte indikationer.

**For at gå videre kræves følgende:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen
- Prækliniske eller mekanistiske studier, der kan underbygge en sammenhæng mellem vasopressinreceptorer og lægemiddelinduceret osteoporose
- Systematisk litteratursøgning for at bekræfte, at der ikke findes relevant evidens
- Vurdering af administrationsvej, da felypressin kun er godkendt som injektionsvæske til dental brug
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

