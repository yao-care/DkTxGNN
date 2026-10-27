---
layout: default
title: Tapentadol
parent: Kun modelforudsigelse (L5)
nav_order: 793
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tapentadol: forudsagt ny indikation Migræne (migraine disorder) (evidensniveau L5). Oprindelig indikation: Ikke tilgængelig i de indsamlede data (indikationsteksten er tom)"
monitor_inn: "tapentadol"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "migraine with or without aura, susceptibility to"]
---

# Tapentadol
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

## Tapentadol: Fra smertebehandling til migræne
{: .text-alpha }

## Resumé

Tapentadol er et stærkt virkende smertestillende middel, der er markedsført i Danmark som Palexia (filmovertrukne tabletter). Der foreligger ingen godkendt indikationstekst i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at det kan have effekt på **migræne** (score 99,7 %), men der er **ingen registrerede kliniske forsøg** og **ingen publikationer, der direkte undersøger tapentadol ved migræne**. Forudsigelsen er rent beregningsmæssig.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke tilgængelig i de indsamlede data (indikationsteksten er tom) |
| Forudsagt ny indikation | Migræne (migraine disorder) |
| TxGNN-forudsigelsesscore | 99,67 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de indsamlede data. Tapentadol er generelt kendt som både en agonist på mu-opioidreceptoren og en hæmmer af noradrenalingenoptag. Den noradrenerge komponent giver kun et spekulativt link til central smertemodulering ved migræne.

TxGNN-scoren er meget høj, men den afspejler en graf-baseret associationsmodel og ikke klinisk dokumentation. Opioider anbefales generelt ikke til migræne på grund af begrænset effekt, risiko for medicinoverforbrugshovedpine (medication-overuse headache), risiko for kronificering samt afhængighed.

Modellen forudsiger også to beslægtede fænotyper: *migræne med hjernestammeaura* (score 99,6 %) og *modtagelighed for migræne med eller uden aura* (score 99,1 %). Sidstnævnte er en genetisk disposition og ikke en behandlingsindikation, så den har ringe translationel betydning. Ved hjernestammeaura kan opioidernes sedative effekt desuden forplumre neurologiske symptomer. Ingen af de tre forudsigelser understøttes af kliniske data.

---

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Ingen publikationer undersøger tapentadol direkte ved migræne. To indirekte publikationer blev fundet under den genetiske migrænefænotype:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [33689517](https://pubmed.ncbi.nlm.nih.gov/33689517/) | 2021 | Review | Expert Opin Pharmacother | Gennemgang af NSAID og paracetamol som alternativer til opioider ved akut smerte. Tester ikke tapentadol ved migræne. |
| [29760569](https://pubmed.ncbi.nlm.nih.gov/29760569/) | 2018 | Kohorte | Drug Healthc Patient Saf | Samtidig brug af opioider med triptaner eller serotonerge antidepressiva i USA. Opioider anbefales ikke rutinemæssigt til migræne pga. risiko for medicinoverforbrugshovedpine og afhængighed. Omtaler risiko for serotoninsyndrom. |

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28104515109 | Palexia (Grünenthal GmbH) | Filmovertrukne tabletter | Ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er identificeret 136 interaktioner. Blandt de registrerede er følgende klassificeret som **alvorlige (Major)**: bupropion, morfin, lorcaserin, diethylpropion, dolasetron, palonosetron og phentermin. Moderate interaktioner omfatter bl.a. adrenalin, hyoscyamin, atropin, glycopyrronium, dicyclomin, dronabinol, eluxadolin, naloxon, trospium og nabilon.
- **Serotonerg risiko:** Litteraturen advarer om risikoen for serotoninsyndrom ved samtidig brug af opioider med triptaner (standardbehandling ved migræne) eller serotonerge antidepressiva (SSRI/SNRI). Det er særligt relevant ved migræne.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en beregningsmodel (L5) uden kliniske forsøg eller direkte litteratur. Samtidig taler opioidernes kendte risici ved migræne (medicinoverforbrugshovedpine, kronificering, afhængighed, serotonerge interaktioner med triptaner) imod anvendelse.

**For at komme videre kræves:**
- Produktresumé med advarsler, kontraindikationer og godkendt indikation (manglende data blokerer sikkerhedsscreening)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prækliniske eller kliniske data, der direkte undersøger tapentadol ved migræne
- Vurdering af, om fordelene kan opveje risikoen sammenlignet med etablerede migrænebehandlinger
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

