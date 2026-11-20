---
layout: default
title: Reslizumab
parent: Kun modelforudsigelse (L5)
nav_order: 713
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-28
monitor_inn: "Reslizumab"
predicted_indications: ["thrombocytopenia due to immune destruction", "primary release disorder of platelets"]
description: "Reslizumab: forudsagt ny indikation Trombocytopeni på grund af immundestruktion (thrombocytopenia due to immune destruction) (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale da…"
---

# Reslizumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Reslizumab: Trombocytopeni på grund af immundestruktion (thrombocytopenia due to immune destruction)
{: .text-alpha }

## Resumé i én sætning

Reslizumab er et anti-IL-5-antistof, som oprindeligt er knyttet til behandling af eosinofil pneumoni og pulmonal eosinofili.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **immunmedieret trombocytopeni** (trombocytopeni på grund af immundestruktion).
Der foreligger **ingen kliniske forsøg** og **ingen publikationer** direkte for denne indikation, så forudsigelsen hviler alene på modellens score.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Foreslået ny indikation | Trombocytopeni på grund af immundestruktion (thrombocytopenia due to immune destruction) |
| TxGNN-prædiktionsscore | 0.9953 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Reslizumab (uofficiel oversættelse): »Reslizumab er en interleukin-5-antagonist (IgG4, kappa). IL-5 er det vigtigste cytokin, der er ansvarligt for eosinofilers vækst og differentiering, rekruttering, aktivering og overlevelse. Reslizumab binder til IL-5 med en dissociationskonstant på 81 pM og hæmmer IL-5's bioaktivitet ved at blokere dets binding til alfakæden i IL-5-receptorkomplekset, der udtrykkes på eosinofilernes overflade.« Engelsk originaltekst: "Reslizumab is an interleukin-5 antagonist (IgG4, kappa). IL-5 is the major cytokine responsible for the growth and differentiation, recruitment, activation, and survival of eosinophils. Reslizumab binds to IL-5 with a dissociation constant of 81 pM, inhibiting the bioactivity of IL-5 by blocking its binding to the alpha chain of the IL-5 receptor complex expressed on the eosinophil surface." ([DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33), version af 2020-02-29; hentet 2026-11-19). Reslizumab er dog et monoklonalt anti-IL-5-antistof, som nedsætter eosinofilernes aktivitet og overlevelse. Det forklarer den oprindelige tilknytning til eosinofile lungesygdomme.

Immunmedieret trombocytopeni drives primært af autoantistof- og T-cellemedieret nedbrydning af blodplader samt nedsat megakaryopoiese. Der er ingen kendt eosinofil- eller IL-5-afhængig sygdomsvej, og derfor er den mekanistiske sammenhæng svag. Den høje score (0,9953) er det eneste, der støtter forudsigelsen.

Der er tale om genetiske eller intrinsiske trombocytdefekter eller autoimmune processer uden kendt forbindelse til IL-5.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

For den primære forudsagte indikation (immunmedieret trombocytopeni) foreligger der ingen relateret litteratur.

For den tredje forudsagte indikation (primær frigørelsesdefekt af blodplader) er der identificeret én publikation, som kun giver indirekte kontekst:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [20565230](https://pubmed.ncbi.nlm.nih.gov/20565230/) | 2010 | Review | Current Medical Research and Opinion | Oversigt over behandling af hypereosinofilt syndrom, herunder mepolizumab (et andet anti-IL-5-lægemiddel). Omhandler eosinofil sygdom og understøtter ikke trombocytindikationerne. |

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105634315 | Cinqaero (Teva B.V.) | Koncentrat til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

Der er ikke fundet registrerede interaktioner i de data, der er indsamlet til denne rapport. Se i øvrigt det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en høj modelscore uden kliniske forsøg, uden direkte litteratur og uden plausibel mekanistisk forbindelse mellem IL-5-hæmning og blodpladesygdomme. Evidensniveauet er L5.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen, da sikkerhedsscreening ikke kan gennemføres uden disse
- Litteratursøgning og prækliniske data, der kan underbygge en mulig rolle for IL-5/eosinofiler i immunmedieret trombocytopeni
- Godkendt indikationstekst for Cinqaero i Danmark til sammenligning med den oprindelige indikation

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Cinqair (reslizumab) prescribing information, Teva Respiratory, LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=053b9158-2a5b-48b9-bf47-5fa78a35ec33) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

