---
layout: default
title: Imidapril
parent: Kun modelforudsigelse (L5)
nav_order: 428
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
monitor_inn: "imidapril"
predicted_indications: ["pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "Braddock syndrome"]
description: "Imidapril: forudsagt ny indikation Pulmonary hypertension owing to lung disease and/or hypoxia (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Imidapril
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

## Imidapril: Pulmonary hypertension owing to lung disease and/or hypoxia
{: .text-alpha }

## Opsummering

Imidapril er en ACE-hæmmer (prodrug), som oprindeligt anvendes til behandling af forhøjet blodtryk.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **pulmonal hypertension som følge af lungesygdom og/eller hypoksi**,
men der er **ingen registrerede kliniske forsøg** og **ingen publikationer** i de indsamlede data, så forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Pulmonary hypertension owing to lung disease and/or hypoxia |
| TxGNN-prædiktionsscore | 0.9978 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til denne rapport. Imidapril er en ACE-hæmmer, der omdannes til den aktive metabolit imidaprilat. Stoffet hæmmer angiotensin-konverterende enzym (ACE) og mindsker dermed dannelsen af angiotensin II, hvilket kan reducere karsammentrækning og vaskulær remodellering.

Teoretisk kan det renin-angiotensin-aldosteron-system (RAAS)-relaterede mekanismer være relevante for lungekarsygdom. Forbindelsen er dog plausibel, men ikke verificeret. Ved pulmonal hypertension forårsaget af lungesygdom er hypoksisk pulmonal vasokonstriktion den dominerende drivkraft, og ACE-hæmmere har ikke vist ensartet gavn. Desuden er systemisk hypotension en bekymring hos patienter med lungesygdom.

Det bør også bemærkes, at de to øverste pulmonale hypertensionsforudsigelser har identisk score (0,9978). Scoren kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

---

## Alternative forudsigelser fra modellen

| Rang | Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|------|
| 2 | Pulmonal hypertension med uklar multifaktoriel mekanisme | 0,9978 | L5 | Svag mekanistisk forbindelse; ingen imidapril-specifik evidens |
| 3 | Malign hypertensiv nyresygdom | 0,9976 | L5 | Tæt på den eksisterende indikation; ACE-hæmning er nyrebeskyttende, men tilstanden er en akut nødsituation, der normalt behandles intravenøst |
| 4 | Malign renovaskulær hypertension | 0,9976 | L5 | Mekanistisk sammenhængende, men risiko for akut nyreskade ved bilateral nyrearteriestenose eller stenose i solitær nyre |
| 5 | Braddock syndrom | 0,9970 | L5 | Ingen mekanistisk sammenhæng kan etableres; sandsynligvis grafbaseret association |

---

## Klinisk evidens fra forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er aktuelt ingen relevant litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103415502 | Prilium Vet. | Pulver til oral opløsning | Ikke angivet i de indsamlede data |

Bemærk: Det eneste godkendte produkt, Prilium Vet. (Vetoquinol S.A.), er et veterinærlægemiddel. Der er i de indsamlede data ikke fundet en markedsføringstilladelse til human anvendelse i Danmark.

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Den eneste registrerede interaktion er farmakologisk, nemlig hæmning af målproteinet angiotensin-konverterende enzym (ACE). Der er ikke angivet interaktionsniveau eller interaktioner med specifikke lægemidler.
- **Forhold knyttet til de forudsagte indikationer** (baseret på klasseviden om ACE-hæmmere): risiko for systemisk hypotension hos patienter med lungesygdom, risiko for akut nyreskade ved bilateral nyrearteriestenose samt behov for monitorering af nyrefunktion og kalium (hyperkaliæmi).

Se i øvrigt det godkendte produktresumé (SmPC) for yderligere sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en modelscore og generel klasseviden (evidensniveau L5), uden kliniske forsøg eller publikationer. Mekanismen er svag for pulmonal hypertension ved lungesygdom, og det eneste danske produkt er et veterinærlægemiddel.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé/indlægsseddel med advarsler og kontraindikationer (p.t. en blokerende datamangel for sikkerhedsscreening)
- Systematisk litteratursøgning og præklinisk eller klinisk evidens for imidapril eller ACE-hæmmere ved de forudsagte indikationer
- Afklaring af, om et humant lægemiddel med imidapril er tilgængeligt og godkendt i Danmark
- Vurdering af administrationsvej og kompatibilitet med den forudsagte indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

