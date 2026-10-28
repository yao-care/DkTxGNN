---
layout: default
title: Risdiplam
parent: Kun modelforudsigelse (L5)
nav_order: 726
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
description: "Risdiplam: forudsagt ny indikation Akne (evidensniveau L5). Oprindelig indikation: Ikke angivet i de danske godkendelsesdata (kendt anvendelse: spinal m…"
monitor_inn: "Risdiplam"
predicted_indications: ["acne (disease)"]
---

# Risdiplam
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **1** stk.
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

## Risdiplam: Fra spinal muskelatrofi til akne
{: .text-alpha }

## Resumé

Risdiplam markedsføres i Danmark under navnet Evrysdi. Den danske godkendelsestekst indeholder ingen angivet indikation, men lægemidlet er kendt som en SMN2-splejsningsmodulator mod spinal muskelatrofi (SMA). TxGNN-modellen forudsiger, at det kan have effekt mod **akne**, men der er **ingen kliniske forsøg** og **ingen publikationer**, der understøtter forudsigelsen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske godkendelsesdata (kendt anvendelse: spinal muskelatrofi) |
| Forudsagt ny indikation | Akne |
| TxGNN-forudsigelsesscore | 0.9945 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger i de indsamlede data ingen detaljerede oplysninger om virkningsmekanismen. Risdiplam er kendt som en modulator af SMN2-præ-mRNA-splejsning, som øger indbygningen af exon 7 og dermed produktionen af funktionelt SMN-protein ved SMA.

Der er ikke identificeret nogen plausibel biologisk sammenhæng mellem SMN2-splejsningsmodulation og aknes patofysiologi (talgkirtler, *C. acnes*, inflammation). Scoren på 0,9945 er et rent beregningsmæssigt output fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens, og er ikke understøttet af kliniske eller litterære data.

Andre forudsigelser i de samlede data er lige så svagt underbyggede (ingen forsøg, ingen litteratur, ingen påvist mekanisme):

| Forudsagt indikation | TxGNN-score | Evidensniveau |
|------|------|------|

Knoglesundhed er relevant hos SMA-patienter på grund af nedsat mobilitet, men det er en følgesygdom og ikke evidens for, at risdiplam behandler osteoporose. Forhøjet plasma-zink er et laboratoriefund snarere end en egentlig behandlingskrævende sygdom. Ved melanom ville off-target-splejsningseffekter desuden kræve en sikkerhedsvurdering.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107163724 | Evrysdi (Roche Registration GmbH) | Filmovertrukne tabletter | Ikke angivet i de tilgængelige data |

Administrationsvej: oral.

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (2 registreret, begge af moderat sværhedsgrad):
- Metformin
- Methylnaltrexon

Oplysninger om advarsler og kontraindikationer var ikke tilgængelige i de data, der er indsamlet til denne rapport. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om akne hviler udelukkende på TxGNN-modellen (deep learning), som kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens, og der foreligger ingen kliniske forsøg, litteratur eller en påvist mekanistisk sammenhæng (evidensniveau L5). Manglende data om advarsler og kontraindikationer forhindrer desuden en egentlig sikkerhedsscreening.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet (SmPC) fra Lægemiddelstyrelsen med advarsler, kontraindikationer og godkendt indikation
- Data om virkningsmekanismen (fx fra DrugBank)
- En hypotese for, hvordan SMN2-splejsningsmodulation kunne påvirke aknes patofysiologi, evt. støttet af prækliniske studier
- Vurdering af administrationsvej (oral tablet) i forhold til den forudsagte indikation
- Systematisk litteratursøgning og søgning efter relevante forsøg
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

