---
layout: default
title: Capmatinib
parent: Kun modelforudsigelse (L5)
nav_order: 156
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-06
description: "Capmatinib: forudsagt ny indikation Leddegigt (rheumatoid arthritis) (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data"
monitor_inn: "capmatinib"
predicted_indications: ["rheumatoid arthritis", "brachydactyly-syndactyly syndrome"]
---

# Capmatinib
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

## Capmatinib: Fra ikke-angivet oprindelig indikation til leddegigt
{: .text-alpha }

## Resumé i én sætning

Capmatinib er en selektiv MET-receptor-tyrosinkinasehæmmer, der er markedsført i Danmark som Tabrecta. Den oprindelige godkendte indikation fremgår ikke af de data, der er indsamlet til denne rapport. TxGNN-modellen forudsiger, at lægemidlet kan være virksomt mod **leddegigt (rheumatoid arthritis)**, men der findes **0 kliniske forsøg** og kun **1 generel oversigtsartikel** uden specifikke data for leddegigt.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data |
| Forudsagt ny indikation | Leddegigt (rheumatoid arthritis) |
| TxGNN-forudsigelsesscore | 0,9945 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Capmatinib er en selektiv hæmmer af MET (c-Met), en receptortyrosinkinase. Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Capmatinib (uofficiel oversættelse): »Capmatinib er en kinasehæmmer, der er rettet mod MET, herunder den mutante variant, der dannes ved exon 14-skipping. MET exon 14-skipping resulterer i et protein med et manglende regulatorisk domæne, hvilket reducerer dets negative regulering og fører til øget downstream MET-signalering.« Engelsk originaltekst: "Capmatinib is a kinase inhibitor that targets MET, including the mutant variant produced by exon 14 skipping. MET exon 14 skipping results in a protein with a missing regulatory domain that reduces its negative regulation leading to increased downstream MET signaling." ([DailyMed: Tabrecta (capmatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=455892c3-d144-4ba8-9ab4-79cabff9876d), version af 2026-10-26; hentet 2026-11-19).

MET-signalering er i litteraturen sat i forbindelse med synovial inflammation, angiogenese og invasivitet i fibroblastlignende synoviocytter ved leddegigt. Derfor er en mekanistisk sammenhæng plausibel. Der er dog ingen direkte evidens, der kobler capmatinib til leddegigt.

Den høje TxGNN-score er en ren computerbaseret forudsigelse. Den eneste fundne publikation er en generel oversigt over godkendte småmolekylære kinasehæmmere, som nævner capmatinib, men ikke indeholder data om leddegigt. Forudsigelsen bør derfor ses som hypotesegenererende.

Den næstrangerende forudsigelse, *brachydactyly-syndactyly syndrome* (score 0,9903), er en sjælden medfødt misdannelse af lemmerne. Der er hverken kliniske forsøg eller litteratur, og det er usandsynligt, at capmatinib kan korrigere en medfødt udviklingsdefekt. Den vurderes ikke yderligere her.

---

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Oversigtsartikel | Pharmacological Research | Opdateret oversigt over egenskaberne ved FDA-godkendte småmolekylære proteinkinasehæmmere. Capmatinib er opført som godkendt kinasehæmmer, men der er ingen data specifikt for leddegigt. |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106617021 | Tabrecta (Novartis Europharm Limited) | Filmovertrukne tabletter | Ikke angivet i de tilgængelige data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (tyrosinkinasehæmmer, MET) |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Overvågningsparametre | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) for advarsler og forsigtighedsregler |

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner:** Der er registreret 137 potentielle interaktioner. Blandt de omfattede eksempler er følgende de vigtigste:

- **Alvorlige (Major):** dexamethason, clarithromycin
- **Moderate:** metformin, alosetron, loperamid, aprepitant, empagliflozin, glycerolphenylbutyrat, methylnaltrexon, metreleptin, naldemedin, naltrexon
- **Lette (Minor):** rabeprazol, dexlansoprazol, esomeprazol, fidaxomicin, lansoprazol, naloxegol, omeprazol, pantoprazol

For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en computerbaseret model (evidensniveau L5). Der findes ingen kliniske forsøg og ingen leddegigtspecifik litteratur, og de vigtigste data om sikkerhed og virkningsmekanisme mangler.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af det danske produktresumé (godkendt indikation, advarsler og kontraindikationer)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Prækliniske data, der undersøger MET-hæmning i leddegigtmodeller
- En vurdering af sikkerhedsprofilen hos patienter med leddegigt, herunder interaktioner med almindelig samtidig medicin (fx dexamethason)

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Tabrecta (capmatinib) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=455892c3-d144-4ba8-9ab4-79cabff9876d) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

