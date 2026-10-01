---
layout: default
title: Pemigatinib
parent: Kun modelforudsigelse (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: Fra kræftbehandling (FGFR-hæmmer) til multipel endokrin neoplasi

## Resumé

Pemigatinib er en selektiv hæmmer af FGFR1-3-kinaser og markedsføres i Danmark som Pemazyre (tabletter). Den oprindelige indikation er ikke angivet i datagrundlaget.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **multipel endokrin neoplasi (MEN)**.
Forudsigelsen er rent grafbaseret: der er **0 kliniske forsøg** og **0 publikationer** for denne indikation.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i datagrundlaget |
| Forudsagt ny indikation | Multipel endokrin neoplasi |
| TxGNN-forudsigelsesscore | 99,71 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Pemigatinib er en selektiv hæmmer af FGFR1-3-kinaser. Datafeltet med den oprindelige virkningsmekanisme (MOA) er ikke udfyldt, så beskrivelsen bygger på lægemidlets kendte farmakologiske klasse.

Mekanistisk er koblingen svag. MEN-syndromerne drives primært af ændringer i *MEN1* og *RET*, og der er ikke påvist en direkte FGFR-afhængighed. Den meget høje score (0,997) afspejler derfor sandsynligvis mønstre i vidensgrafen og ikke en dokumenteret biologisk sammenhæng. Forudsigelsen bør betragtes som en hypotese, der kræver prækliniske data, før den kan vurderes klinisk.

### Øvrige forudsigelser i datasættet

| Forudsagt indikation | Score | Evidens | Vurdering |
|------|------|------|------|
| Amenoré | 99,54 % | L5 | Ingen plausibel mekanistisk kobling. Symptom/syndrom med heterogene årsager, sandsynligvis en grafartefakt |
| HER2-positivt brystkarcinom | 99,49 % | L4 | Biologisk plausibelt, da FGFR-signalering indgår i resistens og krydstale i HER2-positiv brystkræft. Kun indirekte evidens (ét generelt review). Forskningsspørgsmål |
| Cytomegalovirusinfektion | 99,46 % | L5 | Ingen etableret kobling mellem FGFR-hæmning og antiviral aktivitet |
| Infektiøs bovin rhinotracheitis | 99,43 % | L5 | Veterinærsygdom, ikke relevant for human anvendelse. Sandsynligvis en ontologiartefakt |
| Malign katar (malignant catarrhal fever) | 99,43 % | L5 | Veterinærsygdom, ikke relevant for human anvendelse. Samme score som ovenstående tyder på en fælles artefakt |

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen registrerede kliniske forsøg for denne indikation.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relevant litteratur for multipel endokrin neoplasi.

Til sammenligning findes der for en anden forudsagt indikation (HER2-positivt brystkarcinom) ét indirekte litteraturfund:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Review | Pharmacological Research | Generel oversigt over egenskaber ved FDA-godkendte småmolekylære proteinkinasehæmmere. Tester ikke pemigatinib ved denne sygdom |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106368019 | Pemazyre (Incyte Biosciences Distribution) | Tabletter | Ikke oplyst i datagrundlaget |

---

## Cytotoksicitet

Pemigatinib er en kinasehæmmer og hører til de målrettede kræftlægemidler (targeted therapy).

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (FGFR-kinasehæmmer) |
| Knoglemarvssuppression | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Emetogenicitetsklasse | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC) |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ikke fundet registrerede lægemiddelinteraktioner i datagrundlaget.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for multipel endokrin neoplasi er baseret udelukkende på modellen (evidensniveau L5). Der er hverken kliniske forsøg eller litteratur, og der er ingen etableret FGFR-afhængighed i MEN-syndromer. Den høje score alene er ikke tilstrækkelig grundlag for at gå videre.

**For at komme videre kræves:**
- Mekanistiske og prækliniske data, der undersøger FGFR-signalering i MEN-relaterede tumorer (*MEN1*/*RET*)
- Oplysninger om lægemidlets oprindelige indikation og virkningsmekanisme (MOA) fra DrugBank/SmPC
- Gennemgang af Lægemiddelstyrelsens produktresumé for advarsler og kontraindikationer
- Hvis man ønsker at forfølge en mere plausibel retning: biomarkørselekterede (FGFR-ændrede) studier ved HER2-positivt brystkarcinom

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Lægemiddelkandidater til nye indikationer kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

