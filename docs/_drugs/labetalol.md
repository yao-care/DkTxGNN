---
layout: default
title: Labetalol
parent: Kun modelforudsigelse (L5)
nav_order: 472
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "labetalol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism"]
description: "Labetalol: forudsagt ny indikation Malignant hypertensive renal disease (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Labetalol
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
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

## Labetalol: Malignant hypertensive renal disease
{: .text-alpha }

## Resumé

Labetalol er en kombineret alfa-1- og beta-adrenerg antagonist, som oprindeligt anvendes til behandling af forhøjet blodtryk (hypertension).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **malign renovaskulær hypertension**,
men der foreligger **ingen registrerede kliniske forsøg** og kun **1 publikation** (en case-rapport fra 1981) om denne retning. Evidensen er således begrænset til modelforudsigelsen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Malignant hypertensive renal disease |
| TxGNN-forudsigelsesscore | 0.9908 |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen foreligger ikke i de data, der er indsamlet til denne rapport. Ud fra kendt farmakologi er labetalol en kombineret alfa-1/beta-adrenerg blokker, som sænker karmodstand og hjertefrekvens. Lægemidlet anvendes allerede ved svær hypertension og hypertensive nødsituationer.

Malign hypertensiv nyresygdom er en svær form for forhøjet blodtryk med nyreskade. Blodtrykssænkning med en alfa/beta-blokker er biologisk plausibel. Der er dog tale om en udvidelse af den eksisterende hypertensionsindikation snarere end egentlig repurposing. Den høje score (0.9908) er en ren beregningsmæssig forudsigelse fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

De øvrige forudsagte indikationer er mindre overbevisende:
- **Malign hypertensiv nyresygdom** (score 0,9908, L5): ingen forsøg og ingen litteratur. Mekanismen er plausibel, men uden dokumentation.
- **Pulmonal hypertension ved lungesygdom/hypoxi** (score 0,9908, L4) og **pulmonal hypertension med uklar multifaktoriel mekanisme** (L5): den fundne litteratur handler om systemisk hypertension (fx præeklampsi), ikke pulmonal hypertension. Betablokade og systemisk vasodilatation kan desuden forværre højre ventrikelfunktion og ventilations-perfusionsforhold, så der er en potentiel sikkerhedsbekymring.

---

## Evidens fra kliniske forsøg

Der er for tiden ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

For den primære forudsagte indikation (malign renovaskulær hypertension):

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [7242419](https://pubmed.ncbi.nlm.nih.gov/7242419/) | 1981 | Case-rapport | Med J Aust | Ung mand med malign hypertension og vaskulitis udløst af hallucinogene stoffer; arteritis svarede på prednison. Minoxidil og labetalol blev brugt til den indledende blodtryksregulering. Artiklen undersøger ikke labetalol specifikt ved renovaskulær hypertension. |

---

## Information om det danske marked

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105662615 | Labetalol "S.A.L.F." | Injektions-/infusionsvæske, opløsning | Indikationstekst ikke angivet |

Producent: S.A.L.F. S.p.A. Tilladelsen er gyldig og omfatter kun injektionsformen.

---

## Sikkerhedsovervejelser

**Kontraindikationer (fra vidensgrafen, ikke fra produktresumé):**
Vidensgrafen (PrimeKG) angiver følgende sygdomme som kontraindikationer. De bør verificeres mod det godkendte produktresumé (SmPC):
- Hjerte- og lungesygdomme: atrioventrikulært blok, lungeemfysem, bronkiale sygdomme, hypotension
- Lever- og nyresygdomme: leversvigt, leversygdom, hepatisk encefalopati/koma, nyresygdom, anuri, galdeblæresygdom, pancreatitis
- Stofskifte: diabetes mellitus, diabetisk ketoacidose, kaliummangel, hyperurikæmi, urinsyregigt, hyperparathyroidisme, hypercalcæmi, nefrokalcinose
- Øvrige: systemisk lupus erythematosus, angst- og neurotiske lidelser, dysthymi, neonatal gulsot, intraoperativt floppy iris-syndrom

**Lægemiddelinteraktioner:**
287 interaktioner er registreret. Blandt de viste er de vigtigste:
- **Major:** adrenalin (epinephrin), dolasetron
- **Moderate:** bl.a. hydrocortison, dexamethason, betamethason, triamcinolon, budesonid, morfin, atropin, cimetidin, canagliflozin, dapagliflozin og chlorpropamid
- **Minor:** acetylsalicylsyre, magnesiumoxid

For fuldstændig sikkerhedsinformation om advarsler henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der er ingen kliniske forsøg og kun én ikke-relevant case-rapport bag forudsigelsen. Den høje score afspejler sandsynligvis overlap med den eksisterende hypertensionsindikation snarere end ny evidens. For de pulmonale indikationer er der desuden en potentiel sikkerhedsbekymring.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer mangler og er afgørende for sikkerhedsscreening)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Systematisk litteratursøgning efter kliniske data om labetalol ved malign/renovaskulær hypertension og hypertensiv nyresygdom
- Vurdering af, om den forudsagte indikation reelt er dækket af den eksisterende hypertensionsindikation
- Pulmonal hypertension bør ikke forfølges uden stærk mekanistisk og klinisk begrundelse
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

