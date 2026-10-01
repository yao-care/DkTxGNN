---
layout: default
title: Voclosporin
parent: Kun modelforudsigelse (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Voclosporin
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

# Voclosporin: Fra immunsuppressiv calcineurinhæmmer til primær frigørelsesforstyrrelse af blodplader

## Resumé i én sætning

Voclosporin er en calcineurinhæmmer (en analog til ciclosporin), som undertrykker T-cellernes aktivering. TxGNN-modellen forudsiger, at stoffet kan have effekt ved **primær frigørelsesforstyrrelse af blodplader** (primary release disorder of platelets), men der er **ingen kliniske forsøg og ingen publikationer**, der understøtter forudsigelsen. Den hviler udelukkende på en model baseret på en vidensgraf (evidensniveau L5).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Primær frigørelsesforstyrrelse af blodplader |
| TxGNN-forudsigelsesscore | 95,42 % |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig (eller ej)?

Voclosporin er en calcineurinhæmmer. Den blokerer calcineurin-NFAT-IL-2-signalvejen og dermed T-cellernes aktivering. Der foreligger ingen detaljerede mekanismedata fra DrugBank i datagrundlaget. Beskrivelsen her bygger på stofklassens kendte virkemåde. Datagrundlaget nævner, at voclosporin anvendes ved lupusnefritis, men den danske tilladelse indeholder ingen indikationstekst.

Primær frigørelsesforstyrrelse af blodplader er en arvelig defekt i blodpladernes sekretion. Calcineurinhæmning er ikke en etableret vej til at korrigere en sådan defekt, og calcineurinsignalering i blodplader er ikke et valideret behandlingsmål ved denne sygdom. Den høje score skyldes sandsynligvis nærhed i vidensgrafen snarere end en reel biologisk sammenhæng.

### Øvrige forudsigelser

Samme vurdering gælder de andre forudsigelser. Mange optræder to gange i data og er her kun vist én gang.

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Glanzmanns trombasteni | 94,87 % | L5 | Skyldes manglende eller dysfunktionelt integrin αIIbβ3. Calcineurinhæmning genopretter ikke receptoren, og immunsuppression kan øge risikoen for blødning og infektion. Sandsynligvis en artefakt i grafen. |
| Pseudo-von Willebrands sygdom | 94,57 % | L5 | Skyldes gain-of-function-varianter i GP1BA. Der er ingen kendt mekanistisk forbindelse til calcineurinhæmning. |
| Dermatitis | 94,18 % | L4 | Biologisk plausibel, se nedenfor. Anbefaling: Research Question. |
| Renal osteodystrofi | 94,16 % | L5 | Skyldes CKD-mineral- og knoglesygdom. Calcineurinhæmmere er som klasse forbundet med ændret knogleomsætning og knogletab, så skade er mere sandsynlig end gavn. |

Dermatitis er den eneste forudsigelse med en rimelig biologisk sammenhæng. Calcineurinhæmmere blokerer T-cellernes aktivering og cytokinfrigørelse (bl.a. IL-2), som driver T-cellemedierede inflammatoriske hudsygdomme. Systemisk ciclosporin og tacrolimus er etablerede off-label-muligheder ved svær dermatitis, og voclosporin er en strukturelt beslægtet og mere potent calcineurinhæmmer. Evidensen er dog indirekte og udledt af andre calcineurinhæmmere.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ikke registreret relaterede kliniske forsøg for nogen af de forudsagte indikationer.

---

## Litteraturevidens

For den primære forudsigelse (primær frigørelsesforstyrrelse af blodplader) foreligger der ingen relateret litteratur.

For dermatitis er der to oversigtsartikler. Ingen af dem indeholder primære kliniske data for voclosporin ved dermatitis.

| PMID | År | Type | Tidsskrift | Hovedpointer |
|------|-----|------|------|---------|
| [37307993](https://pubmed.ncbi.nlm.nih.gov/37307993/) | 2024 | Review | Journal of the American Academy of Dermatology | Gennemgang af off-label-brug af systemisk tacrolimus og voclosporin i dermatologi. Der er retningslinjer for ciclosporin, men ingen stærk konsensus for tacrolimus og voclosporin. |
| [41361657](https://pubmed.ncbi.nlm.nih.gov/41361657/) | 2025 | Review | Molecular neurobiology | Oversigt over calcineurinhæmmeres rolle, håndtering af toksicitet og fremtidsperspektiver. Beskriver hæmning af calcineurin og NFAT og dermed af IL-2-transkription og T-cellernes aktivering. |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28106649721 | Lupkynis | Kapsler, bløde | Otsuka Pharmaceutical Netherlands B.V. |

---

## Sikkerhedsovervejelser

Der foreligger ingen sikkerhedsdata i datagrundlaget. Opslag på lægemiddelinteraktioner gav ingen resultater.

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Alle forudsigelser mangler klinisk og litterær støtte, og for de tre blødningssygdomme og renal osteodystrofi er der ingen plausibel mekanisme. Dermatitis er biologisk rimelig, men evidensen er indirekte, og hensynet til nyretoksicitet, hypertension og infektionsrisiko skal vejes mod alternativer ved en ikke-livstruende hudsygdom. Dermatitis kan derfor kun betragtes som et forskningsspørgsmål.

**For at komme videre kræves:**
- Sikkerhedsoplysninger (advarsler og kontraindikationer) fra Lægemiddelstyrelsens produktresumé. Manglen på disse er en blokerende datamangel for sikkerhedsvurderingen.
- Detaljerede mekanismedata (MOA) fra DrugBank.
- Primære kliniske data eller forsøg med voclosporin ved dermatitis, før en egentlig vurdering kan foretages.
- Afklaring af den godkendte indikationstekst for Lupkynis i Danmark.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelserne er modelbaserede og kræver klinisk validering, før de kan anvendes i praksis.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

