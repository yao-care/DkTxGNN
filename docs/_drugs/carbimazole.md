---
layout: default
title: Carbimazole
parent: Kun modelforudsigelse (L5)
nav_order: 161
evidence_level: L5
indication_count: 2
monitor_inn: "carbimazole"
predicted_indications: ["resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta", "hyperthyroxinemia"]
last_modified_at: 2026-11-24
description: "Carbimazole: forudsagt ny indikation Resistens over for thyreoideahormon på grund af mutation i thyreoideahormonreceptor beta (resistance to thyroid hormone… (evidensniveau L5). Oprindelig indikation…"
---

# Carbimazole
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

## Carbimazol: thyreoperoxidasehæmmer (prodrug for methimazol) → Resistens over for thyreoideahormon på grund af mutation i thyreoideahormonreceptor beta (resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta)
{: .text-alpha }

## Resumé i én sætning

Carbimazol er et prodrug af methimazol, som hæmmer syntesen af thyreoideahormon.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **resistens over for thyreoideahormon på grund af mutation i thyreoideahormonreceptor beta (resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta)**.
Evidensen er meget svag: der er **ingen kliniske forsøg** og kun **1 publikation** (en case-beskrivelse om differentialdiagnostik), som ikke undersøger behandlingseffekt.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Resistens over for thyreoideahormon på grund af mutation i thyreoideahormonreceptor beta (resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta) |
| TxGNN-forudsigelsesscore | 0,9971 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge ChEMBL (EMBL-EBI) er den registrerede virkningsmekanisme for Carbimazole (uofficiel oversættelse): »Thyroideaperoxidasehæmmer«. Engelsk originaltekst: "Thyroid peroxidase inhibitor" ([ChEMBL CHEMBL508102 (carbimazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL508102), CC BY-SA 3.0; hentet 2026-11-19). Carbimazol omdannes til methimazol, som hæmmer thyreoperoxidase og dermed nedsætter dannelsen af thyreoideahormon.

Ved resistens over for thyreoideahormon (RTH-beta) ligger defekten på receptorniveau: T4/T3 er forhøjet, og TSH er ikke undertrykt. Hvis hormonsyntesen sænkes, vil TSH i princippet stige yderligere, hvilket kan stimulere væksten af skjoldbruskkirtlen (struma) og forværre vævshypothyreose i receptorresistente væv. Den høje score afspejler sandsynligvis modellens nærhed til fænotyper med hormonoverskud snarere end en reel behandlingsmæssig begrundelse. Antithyreoide lægemidler anses generelt for uhensigtsmæssige ved RTH-beta.

## Evidens fra kliniske forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [24165508](https://pubmed.ncbi.nlm.nih.gov/24165508/) | 2013 | Case-beskrivelse | BMJ Case Reports | Ung mand med vedvarende forhøjet frit T4 og ikke-undertrykt TSH, tidligere behandlet med carbimazol med afbrydelser; omhandler differentialdiagnostik, ikke behandlingseffekt |

## Markedsinformation i Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28100096555 | Neo-mercazole | overtrukne tabletter | CARBIMAZOL | Gyldig |

Tabellen viser den eneste markedsføringstilladelse til et humant lægemiddel med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler.

<!-- licenses:end -->

## Sikkerhedsovervejelser

Der henvises til det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der findes ingen kliniske forsøg og ingen studier, der viser behandlingseffekt ved denne sygdom. Mekanistisk er nedsættelse af hormonsyntesen sandsynligvis uhensigtsmæssig ved receptorresistens, og den høje modelscore er ikke understøttet af evidens.

**For at komme videre kræves:**
- Direkte kliniske eller prækliniske data, der undersøger carbimazol ved RTH-beta, herunder vurdering af risikoen for TSH-stigning og struma
- Detaljerede data om virkningsmekanisme
- Gennemgang af produktresuméets advarsler og kontraindikationer

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde (revideret 2026-11-20; tidligere version gemt i loggen) | [ChEMBL CHEMBL508102 (carbimazole): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL508102) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

