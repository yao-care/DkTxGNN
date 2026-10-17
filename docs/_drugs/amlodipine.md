---
layout: default
title: Amlodipine
parent: Kun modelforudsigelse (L5)
nav_order: 54
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Amlodipine: forudsagt ny indikation Hjernestamme-infarkt (evidensniveau L5). Oprindelig indikation: Hypertension, slagtilfælde/cerebrovaskulær sygdom, cerebralt infarkt…"
monitor_inn: "amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
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

# Amlodipin: Fra hypertension til hjernestamme-infarkt (og intracerebral blødning)

> **Bemærkning om valg af forudsagt indikation:** Den højest rangerede forudsigelse (hjernestamme-infarkt) har kun modelscore og ingen studier. Den forudsigelse med klart stærkest evidens i de indsamlede data er **intracerebral blødning** (rang 10). Rapporten viser derfor begge i oversigten, men evidens- og beslutningsafsnittene fokuserer på intracerebral blødning.

## Opsummering

Amlodipin er en calciumkanalblokker, der oprindeligt bruges til behandling af forhøjet blodtryk, Prinzmetals angina og forebyggelse af slagtilfælde og cerebrovaskulære sygdomme.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **hjernestamme-infarkt** (score 99,94 %, kun modelforudsigelse) og ved **intracerebral blødning** (score 99,79 %).
For intracerebral blødning findes der **4 kliniske forsøg** (heraf ét afsluttet fase 3-RCT med 1.671 deltagere) og **9 publikationer**. Forsøget tester dog en trippelkombination, hvor amlodipin kun er en del.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hypertension, slagtilfælde/cerebrovaskulær sygdom, cerebralt infarkt, Prinzmetals angina (fra vidensgrafen; de danske markedsføringstilladelser indeholder ingen indikationstekst) |
| Forudsagt ny indikation (rang 1) | Hjernestamme-infarkt |
| Forudsagt indikation med stærkest evidens | Intracerebral blødning (rang 10) |
| TxGNN-forudsigelsesscore | Hjernestamme-infarkt: 99,94 %; intracerebral blødning: 99,79 % |
| Evidensniveau | Hjernestamme-infarkt: L5; intracerebral blødning: L1 (med forbehold, se nedenfor) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 5 |
| Anbefalet beslutning | Hjernestamme-infarkt: Hold; intracerebral blødning: Proceed with Guardrails |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger i øjeblikket ikke detaljerede data om amlodipins virkningsmekanisme i de data, der er indsamlet til denne rapport. Det er alment kendt, at amlodipin er en calciumkanalblokker af dihydropyridintypen, som sænker blodtrykket ved at mindske den systemiske vaskulære modstand. Mekanismen er her hentet fra almen viden og ikke fra de indsamlede data.

Blodtrykssænkning er den eneste dokumenterede metode til at forebygge recidiverende slagtilfælde. Amlodipin er allerede indiceret ved slagtilfælde og cerebrovaskulære sygdomme gennem denne mekanisme. Derfor er forbindelsen til hjernestamme-infarkt og MR-definerede hjerneinfarkter plausibel som sekundær forebyggelse, men der er ingen direkte evidens. For intracerebral blødning er blodtrykskontrol den vigtigste modificerbare faktor til at forebygge nye blødninger.

Prækliniske rottestudier viser desuden mindre infarktstørrelse og neurobeskyttelse (antiapoptotiske og antioxidative effekter, synergi med atorvastatin) efter cerebral arterieokklusion. Disse resultater kan ikke direkte overføres til mennesker.

Flere andre forudsigelser er mindre plausible: Ved pulmonal hypertension pga. lungesygdom/hypoxi kan systemiske vasodilatatorer forværre ventilations-perfusionsforholdet, og litteraturen er prækliniske studier og kasuistikker (bl.a. overdosis med lungeødem). Ved Braddock syndrom og ABri-amyloidose er der ingen identificerbar mekanistisk begrundelse.

---

## Evidens fra kliniske forsøg

### Intracerebral blødning

| Forsøgsnummer | Fase | Status | Antal deltagere | Vigtigste fund |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Fase 3 | Afsluttet | 1.671 | TRIDENT: dobbeltblindet, placebokontrolleret RCT af en lavdosis trippelpille (indeholder amlodipin) til forebyggelse af recidiverende slagtilfælde efter intracerebral blødning. Direkte evidens, men for kombinationen |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | Ikke fasedelt | Rekrutterer | 140 | Trippel antihypertensiv behandling efter intracerebral blødning (TRICH-score); endnu ingen resultater |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Ikke fasedelt | Afbrudt | 4 | TRIDENT MR-delstudie; for få deltagere til vurdering |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Fase 3 | Afbrudt | 1 | TRIDENT kognitiv delstudie; ingen anvendelige data |

### Cerebral arterieokklusion (rang 6)

| Forsøgsnummer | Fase | Status | Antal deltagere | Vigtigste fund |
|---------|------|------|------|---------|
| [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) | Fase 4 | Afbrudt | 400 | Carotis-endarterektomi versus optimal medicinsk behandling; amlodipin er ikke det testede indgreb |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | Ikke fasedelt | Afbrudt | 4 | Se ovenfor |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Fase 3 | Afbrudt | 1 | Se ovenfor |

For hjernestamme-infarkt er der ingen registrerede kliniske forsøg.

---

## Litteraturevidens

### Intracerebral blødning

| PMID | År | Type | Tidsskrift | Vigtigste fund |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT | N Engl J Med | Lavdosis trippelpille efter intracerebral blødning; resultatet er ikke verificeret ud fra de tilgængelige data |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Design-artikel | Int J Stroke | Rationale og design for TRIDENT |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT (indirekte) | Hypertens Res | CASE-J: design af studie med antihypertensiva (candesartan vs. calciumkanalblokker) |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovasc Drugs Ther | Calciumantagonister ved hypertension og arytmier |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Kasuistik | Ann Pharmacother | Sandsynligt amlodipin-induceret angioødem hos patient med thalamisk blødning (sikkerhedssignal) |

### Cerebral arterieokklusion (prækliniske studier)

| PMID | År | Type | Tidsskrift | Vigtigste fund |
|------|-----|------|------|---------|
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Dyrestudie | Am J Hypertens | Amlodipin reducerede infarktstørrelsen hos ApoE-mangelmus |
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Dyrestudie | J Neurosci Res | Amlodipin + atorvastatin: additiv neurobeskyttelse efter MCAO hos rotter |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Dyrestudie | Brain Res | Synergistisk beskyttelse mod iskæmisk skade |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Dyrestudie | Brain Res | Synergistisk gavn af kombinationen på neuronal skade |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Dyrestudie | Brain Res | Calciumkanalblokkere med antioxidativ effekt forebygger neuronal skade |

Der findes ingen litteratur for hjernestamme-infarkt.

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103988406 | Adipine | Tabletter | Ikke angivet i de indsamlede data |
| 28104581409 | Twynsta | Tabletter | Ikke angivet i de indsamlede data |
| 28106498320 | Tarlodix | Kapsler, hårde | Ikke angivet i de indsamlede data |
| 28105572915 | Amlodipine/Valsartan "Mylan" | Filmovertrukne tabletter | Ikke angivet i de indsamlede data |
| 28106061618 | Amlodipine/Valsartan/Hydrochlorothiazide "Krka" | Filmovertrukne tabletter | Ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Kontraindikationer/risikotilstande fra vidensgrafen** (ikke produktresumétekst): bl.a. leversvigt og leversygdom, nyresygdom, pancreatitis, galdeblæresygdom, hypothyroidisme, angioødem (herunder arveligt), systemisk lupus erythematosus, myopati, familiær periodisk paralyse, kaliummangel, diabetes og diabetisk ketoacidose, neutropeni/agranulocytose, hypotension og hyperparathyroidisme.
- **Lægemiddelinteraktioner:** 343 registrerede interaktioner. Blandt de viste er alle af moderat grad, bl.a. med kortikosteroider (hydrocortison, betamethason, budesonid, dexamethason), aprepitant, acetylsalicylsyre, bupropion, calciumsalte, canagliflozin, dapagliflozin, clarithromycin og clotrimazol.
- **Signaler fra litteraturen:** Hypotension og angioødem er kendte risici (kasuistik). Overdosis er beskrevet med ikke-kardiogent lungeødem.

Se desuden det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning:**
- **Intracerebral blødning: Proceed with Guardrails**
- **Hjernestamme-infarkt og øvrige forudsigelser: Hold** (cerebral arterieokklusion kan betragtes som forskningsspørgsmål)

**Begrundelse:**
- For intracerebral blødning findes et afsluttet fase 3-RCT (TRIDENT, 1.671 deltagere) og en publikation i 2026, men amlodipin indgår kun som del af en trippelkombination, så dets egen effekt kan ikke isoleres. Studiets primære resultat er ikke verificeret ud fra de tilgængelige data. De øvrige forudsigelser bygger på modelscore, prækliniske data eller enkelte kasuistikker.

**For at komme videre kræves:**
- Gennemgang af TRIDENT-publikationens primære resultat (PMID 42019018) og bidraget fra amlodipin som komponent.
- Data om virkningsmekanisme (MOA), som mangler i de indsamlede data.
- Advarsler og kontraindikationer fra de danske produktresuméer fra Lægemiddelstyrelsen (mangler i de indsamlede data).
- Sikkerhedsplan for hypotension, angioødem og interaktioner, særligt hos patienter med lever- og nyresygdom.
- For hjernestamme-infarkt: direkte kliniske eller observationelle data, før en anbefaling kan overvejes.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

