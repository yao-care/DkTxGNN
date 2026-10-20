---
layout: default
title: Benazepril
parent: Kun modelforudsigelse (L5)
nav_order: 101
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Benazepril: forudsagt ny indikation Malign hypertensiv nyresygdom (evidensniveau L5). Oprindelig indikation: Hypertension (forhøjet blodtryk)"
monitor_inn: "benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
---

# Benazepril
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **5** stk.
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

# Benazepril: Fra hypertension til malign hypertensiv nyresygdom

## Opsummering

Benazepril er en ACE-hæmmer, som oprindeligt anvendes til behandling af hypertension (forhøjet blodtryk).
TxGNN-modellen forudsiger, at det kan have effekt ved **malign hypertensiv nyresygdom**,
men der er i øjeblikket **0 kliniske forsøg** og **0 relevante publikationer**, der understøtter denne retning. Forudsigelsen er derfor alene modelbaseret.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hypertension (forhøjet blodtryk) |
| Forudsagt ny indikation | Malign hypertensiv nyresygdom |
| TxGNN-forudsigelsesscore | 99,65 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (kun som veterinærlægemidler) |
| Antal markedsføringstilladelser | 3 |
| Anbefalet beslutning | Hold |

Bemærk: Den oprindelige indikation stammer fra TxGNN-vidensgrafen, da de danske godkendelsesdata ikke indeholder indikationstekst.

## Hvorfor er denne forudsigelse rimelig?

De data, der er indsamlet til denne rapport, indeholder ikke en detaljeret beskrivelse af virkningsmekanismen. Ud fra kendt viden er benazepril en ACE-hæmmer, der nedsætter dannelsen af angiotensin II. Det sænker blodtrykket og reducerer trykket i nyrernes glomeruli.

Det er biologisk plausibelt for hypertensiv nyreskade. Den høje score afspejler dog sandsynligvis, at sygdommen ligger tæt på den eksisterende hypertensionsindikation i vidensgrafen, og ikke egentlig klinisk evidens.

Malign hypertension behandles desuden typisk akut med intravenøse midler. En oral ACE-hæmmer ville derfor have en rolle i langtidsbeskyttelse af nyrerne efter stabilisering, ikke som primær behandling.

### Øvrige forudsagte indikationer

| Rang | Forudsagt indikation | Score | Evidensniveau | Kommentar |
|---|---|---|---|---|
| 2 | Malign renovaskulær hypertension | 99,65 % | L5 | Mekanistisk sammenhængende (aktivering af renin-angiotensinsystemet), men ACE-hæmmere kan udløse akut nyreskade ved bilateral nyrearteriestenose eller stenose i en solitær nyre |
| 3 | Pulmonal hypertension med uklar multifaktoriel mekanisme | 99,60 % | L5 | Bygger på delt terminologi; systemiske ACE-hæmmere har ikke vist pålidelig effekt, og der er risiko for hypotension |
| 4 | Pulmonal hypertension pga. lungesygdom og/eller hypoxi | 99,60 % | L5 | Teoretisk rationale; de tre fundne publikationer er irrelevante |
| 5 | Braddock syndrom | 99,44 % | L5 | Ingen klar mekanistisk begrundelse; sandsynligvis et artefakt fra grafen |

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er ingen relevant litteratur for den primære forudsagte indikation (malign hypertensiv nyresygdom).

For rang 4 (pulmonal hypertension pga. lungesygdom/hypoxi) blev der fundet tre publikationer, men de er ikke relevante for benazepril. De er prækliniske studier af traditionelle kinesiske urtepræparater og er sandsynligvis stikordstræf på "hypoxi" eller "fibrose":

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [38803876](https://pubmed.ncbi.nlm.nih.gov/38803876/) | 2024 | Prækliniske | Heliyon | Modified Zhenwu Tang og oxidativt stress/hypoxiske responser ved kronisk nyresvigt |
| [31007700](https://pubmed.ncbi.nlm.nih.gov/31007700/) | 2019 | Prækliniske (rotte) | Evid Based Complement Alternat Med | Danggui Shaoyao San og nyrefibrose via hypoxi og autofagi |
| [31317035](https://pubmed.ncbi.nlm.nih.gov/31317035/) | 2019 | Prækliniske (rotte) | BioMed Res Int | Tongxinluo og myokardiefibrose efter akut myokardieinfarkt |

## Markedsinformation for Danmark

Alle tre tilladelser gælder veterinærlægemidler. Der er ikke fundet humane præparater med benazepril i de indsamlede data.

| Markedsføringstilladelsesnr. | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28107214724 | Benadil Vet. | Filmovertrukne tabletter | Ikke angivet |
| 28104952611 | Cardalis | Tyggetabletter | Ikke angivet |
| 28105341413 | Fortekor Plus | Tabletter | Ikke angivet |

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer var ikke tilgængelige i de indsamlede data.

- **Kontraindikationer fra vidensgrafen** (ikke fra produkttekst, og derfor vejledende): leversvigt, nyresygdom, pancreatitis, leversygdom, galdeblæresygdom, angioødem (herunder arveligt, erhvervet og RAAS-blokker-induceret), systemisk lupus erythematosus, kaliummangel, diabetes mellitus, diabetisk ketoacidose, neutropeni, agranulocytose, hypotension, hyperparathyroidisme, hepatisk encefalopati, bindevævssygdom, knoglesygdom, neonatal gulsot og anuri.
- **Lægemiddelinteraktioner**: 207 interaktioner er registreret. De viste er alle af moderat grad og omfatter hydrocortison samt en række antidiabetika (bl.a. insuliner, glimepirid, glipizid, glyburid, dapagliflozin, exenatid og alogliptin).
- Ved renovaskulær hypertension er der særlig risiko for akut nyreskade.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Alle forudsagte indikationer har evidensniveau L5 uden kliniske forsøg eller relevant litteratur. De høje TxGNN-scorer afspejler sandsynligvis nærhed til hypertension i vidensgrafen. Derudover er de danske tilladelser kun til veterinær brug, og sikkerhedsdata fra produktresuméet mangler.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet (hentet fra Lægemiddelstyrelsen)
- Systematisk litteraturgennemgang og registrering af kliniske forsøg for benazepril ved hypertensiv nyresygdom
- Vurdering af humane benazeprilpræparater, da de danske tilladelser kun omfatter veterinære produkter
- Ekspertvurdering af nyrefunktions- og kaliumovervågning samt risikoen ved renovaskulær sygdom
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

