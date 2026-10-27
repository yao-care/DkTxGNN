---
layout: default
title: Lipegfilgrastim
parent: Kun modelforudsigelse (L5)
nav_order: 501
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Lipegfilgrastim: forudsagt ny indikation Primær frigivelsesforstyrrelse af blodplader (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (godkendelsesteksten er tom)"
monitor_inn: "LIPEGFILGRASTIM"
predicted_indications: ["primary release disorder of platelets", "primary release disorder of platelets", "severe nonproliferative diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "pseudo-von Willebrand disease", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Glanzmann thrombasthenia", "diabetic retinopathy", "diabetic retinopathy"]
---

# Lipegfilgrastim
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

## Lipegfilgrastim: Fra neutropeni til primær frigivelsesforstyrrelse af blodplader
{: .text-alpha }

## Resumé i én sætning

Lipegfilgrastim er en pegyleret vækstfaktor (G-CSF-analog), og det er markedsført i Danmark som Lonquex. De data, der er indsamlet til denne rapport, indeholder dog ingen godkendt indikationstekst.
TxGNN-modellen forudsiger, at stoffet kan have effekt på **primær frigivelsesforstyrrelse af blodplader**, men der findes **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (godkendelsesteksten er tom) |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN-forudsigelsesscore | 99,93 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen. Lipegfilgrastim er dog en pegyleret G-CSF-analog, som stimulerer proliferation og differentiering af neutrofile granulocytter via G-CSF-receptoren på myeloide celler.

Der er ingen kendt sammenhæng mellem denne mekanisme og blodpladernes granulefrigivelse eller trombocytfunktionsforstyrrelser. Den høje score (0,9993) afspejler sandsynligvis blot nærhed mellem hæmatologiske sygdomme i modellens vidensgraf og understøttes ikke af mekanistiske eller kliniske data. Forudsigelsen bør derfor betragtes som en hypotese og ikke som et fund.

**Øvrige forudsigelser fra modellen** (alle uden kliniske forsøg og litteratur, alle evidensniveau L5, anbefaling Hold):

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| Svær non-proliferativ diabetisk retinopati | 99,91 % | Ingen klar mekanistisk begrundelse. Teoretisk risiko for, at G-CSF påvirker retinal neovaskularisering ugunstigt. |
| Pseudo-von Willebrands sygdom | 99,91 % | Skyldes en funktionsforøgende defekt i trombocyt-GPIbα. Lipegfilgrastim har ingen kendt effekt på GPIb-VWF-interaktionen. |
| Glanzmanns trombasteni | 99,91 % | Skyldes mangel på eller dysfunktion af integrin αIIbβ3. G-CSF-receptoragonisme adresserer ikke denne defekt. |
| Diabetisk retinopati | 99,75 % | Ingen etableret mekanisme. Potentiel sikkerhedsbekymring pga. G-CSF's effekt på patologisk angiogenese. |

Bemærk: Hver indikation optræder to gange i de indsamlede data (dublet). Begge poster er vurderet ens og er her samlet.

---

## Kliniske forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret.

---

## Litteratur

Der er aktuelt ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106822720 | Lonquex (Teva B.V.) | Injektionsvæske, opløsning, hætteglas | Ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

Der foreligger ingen sikkerhedsdata i de indsamlede data. Der blev ikke fundet registrerede lægemiddelinteraktioner, og der er ingen kontraindikationer fra vidensgrafen.

Der er udelukkende et teoretisk forbehold: G-CSF kan påvirke patologisk angiogenese, hvilket er relevant, hvis der overvejes anvendelse ved diabetisk retinopati.

Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende baseret på modellens vidensgraf (evidensniveau L5), uden kliniske forsøg, litteratur eller en plausibel mekanistisk sammenhæng. Manglende produktresumédata (advarsler og kontraindikationer) blokerer desuden en sikkerhedsscreening.

**For at komme videre kræves følgende:**
- Hent og gennemgå produktresuméet for Lonquex fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikation)
- Indhent data om virkningsmekanisme fra DrugBank
- Gennemfør en systematisk litteratursøgning og søgning i registre over kliniske forsøg for de forudsagte indikationer
- Vurder den mekanistiske sammenhæng mellem G-CSF-receptoraktivering og de forudsagte sygdomme
- Ved overvejelse af diabetisk retinopati: foretag en særskilt sikkerhedsvurdering af G-CSF's effekt på retinal neovaskularisering
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

