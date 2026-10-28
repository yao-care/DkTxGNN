---
layout: default
title: Fenoterol
parent: Kun modelforudsigelse (L5)
nav_order: 353
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-28
description: "Fenoterol: forudsagt ny indikation Multipel systematrofi (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (godkendelsesteksten for det dans…"
monitor_inn: "fenoterol"
predicted_indications: ["multiple system atrophy", "postural orthostatic tachycardia syndrome", "variably protease-sensitive prionopathy", "open-angle glaucoma", "Raynaud disease", "primary hereditary glaucoma", "sinoatrial block", "sinoatrial node disease"]
---

# Fenoterol
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

## Fenoterol: Fra bronkodilatation til multipel systematrofi
{: .text-alpha }

## Opsummering

Fenoterol er en selektiv beta-2-adrenerg agonist, der anvendes som bronkodilatator (i Danmark som en del af produktet Berodual).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **multipel systematrofi (MSA)**,
men der er på nuværende tidspunkt **0 kliniske forsøg** og **0 publikationer** i de indsamlede data, der understøtter denne retning. Forudsigelsen er alene beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (godkendelsesteksten for det danske produkt er tom) |
| Forudsagt ny indikation | Multipel systematrofi |
| TxGNN-forudsigelsesscore | 0,9970 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig (eller ej)?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i de indsamlede data. Farmakologiske data viser, at fenoterol binder til beta-adrenoreceptorer (ADRB1, ADRB2 og ADRB3), og lægemidlet er kendt som en selektiv beta-2-agonist, der bruges som bronkodilatator og til at hæmme for tidlig veorvirksomhed.

Et teoretisk link til MSA kunne være beta-2-agonisters påvirkning af alfa-synuclein-ekspression (rapporteret for andre beta-2-agonister som salbutamol i epidemiologiske og cellebaserede studier) eller symptomatiske effekter på autonom dysfunktion. Der er dog en væsentlig modsætning: MSA er kendetegnet ved neurogen ortostatisk hypotension, og en vasodilaterende beta-2-agonist, der kan give takykardi, kan forværre den hæmodynamiske ustabilitet.

Den høje score er derfor en ren computerbaseret forudsigelse fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, men er ikke biologisk evidens og ikke et resultat understøttet af kliniske data.

---

## Dokumentation fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| MA 28103223300 | Berodual (Boehringer Ingelheim Int. GmbH) | Inhalationsspray, opløsning | Ikke angivet |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Farmakologiske data viser, at fenoterol virker på beta-1-, beta-2- og beta-3-adrenoreceptorer. Der er ikke identificeret specifikke interaktioner med andre lægemidler i de indsamlede data.
- **Mekanistisk sikkerhedsbekymring:** Som beta-2-agonist kan fenoterol give vasodilatation og refleks-takykardi, hvilket er særligt problematisk ved MSA (ortostatisk hypotension).

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger, herunder kontraindikationer og advarsler.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en computermodel (L5) uden kliniske forsøg eller publikationer. Desuden er der en mekanistisk sikkerhedsbekymring, da en beta-2-agonist kan forværre ortostatisk hypotension og takykardi ved MSA.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen (blokerende datahul for sikkerhedsscreening)
- Præklinisk evidens for effekt på alfa-synuclein eller autonome symptomer ved MSA
- Vurdering af kardiovaskulær sikkerhed hos patienter med neurogen ortostatisk hypotension
- Bekræftelse af den oprindelige godkendte indikation for Berodual

---

## Andre forudsagte indikationer (til orientering)

Alle nedenstående har evidensniveau L5, ingen kliniske forsøg eller litteratur og anbefalingen Hold.

| Rang | Sygdom | TxGNN-score | Bemærkning |
|------|------|------|------|
| 2 | Postural ortostatisk takykardisyndrom (POTS) | 0,9961 | Mekanistisk tvivlsom; kan forværre takykardi |
| 3 | Variabelt proteasefølsom prionopati | 0,9954 | Ingen klar mekanistisk begrundelse; ultrasjælden sygdom |
| 4 | Åbenvinklet glaukom | 0,9943 | Plausibel men indirekte (påvirkning af kammervand); systemiske bivirkninger |
| 5 | Raynauds sygdom | 0,9941 | Vasodilatation er plausibel, men tolerabiliteten er begrænset |
| 6 | Primær arvelig glaukom | 0,9937 | Strukturelle defekter; højst symptomatisk effekt |
| 7 | Sinoatrial blok | 0,9935 | Kronotrop effekt plausibel, men proarytmisk risiko |
| 8 | Sygdom i sinusknuden | 0,9925 | Behandles typisk med pacemaker; arytmirisiko |
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

