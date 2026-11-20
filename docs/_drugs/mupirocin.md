---
layout: default
title: Mupirocin
parent: Kun modelforudsigelse (L5)
nav_order: 572
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-06
monitor_inn: "Mupirocin"
predicted_indications: ["pleural empyema (disease)", "punctate epithelial keratoconjunctivitis"]
description: "Mupirocin: forudsagt ny indikation Pleural empyem (pleural empyema (disease)) (evidensniveau L5). I Danmark, markedsføringstilladelser: 9 (gyldige: 9)"
---

# Mupirocin
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

## Mupirocin: Pleural empyem (pleural empyema (disease))
{: .text-alpha }

## Resumé i én sætning

Mupirocin er et topisk antibiotikum, der oprindeligt anvendes til behandling af hudinfektioner som impetigo og bulløs impetigo.
TxGNN-modellen forudsiger, at det kan have effekt på **pleural empyem**,
men der er **ingen registrerede kliniske forsøg** og **ingen publikationer** til at understøtte denne forudsigelse. Forudsigelsen bygger udelukkende på modelberegning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Pleural empyem (pleural empyema (disease)) |
| TxGNN-forudsigelsesscore | 0.9949 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 9 af 9) |
| Antal markedsføringstilladelser | 9 (gyldige: 9) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge afsnittene »Mechanism of Action« og »Microbiology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Mupirocin (uofficiel oversættelse): »Mupirocin er et antibakterielt middel, der hæmmer RNA-syntetase. […] Mupirocin hæmmer den bakterielle proteinsyntese ved reversibelt og specifikt at binde sig til bakteriel isoleucyl-transfer-RNA (tRNA)-syntetase. Mupirocin er baktericidt ved de koncentrationer, der opnås ved topikal administration.« Engelsk originaltekst: "Mupirocin is an RNA synthetase inhibitor antibacterial. […] Mupirocin inhibits bacterial protein synthesis by reversibly and specifically binding to bacterial isoleucyl-transfer RNA (tRNA) synthetase. Mupirocin is bactericidal at concentrations achieved by topical administration." ([DailyMed: Pirnuo (mupirocin) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89c43f7b-1a88-45bf-a356-07518d4e7870), version af 2020-03-20; hentet 2026-11-19). Det er dog almindeligt kendt, at mupirocin hæmmer bakteriens isoleucyl-tRNA-syntetase og dermed proteinsyntesen. Stoffet er aktivt over for *Staphylococcus aureus* og visse streptokokker.

Disse bakterier kan også forårsage pleural empyem, så der findes en teoretisk antibakteriel sammenhæng med den oprindelige indikation. Den høje modelscore afspejler sandsynligvis denne ligheden i mikrobiologi.

Forudsigelsen er dog farmakologisk usandsynlig. Mupirocin er et topisk middel uden betydelig systemisk eksponering og kan derfor ikke nå pleurahulen. Uden kliniske eller litteraturmæssige data bør forudsigelsen betragtes som et rent computergenereret signal.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig for pleural empyem.

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101502892 | Bactroban (GlaxoSmithKline Pharma A/S) | Salve | Indikationstekst ikke angivet i de tilgængelige data |

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgrafen**: TxGNN-vidensgrafen angiver dermatitis som en sygdom, hvor brug af lægemidlet er kontraindiceret. Dette stammer fra grafdata og ikke fra produktresuméet.
- **Lægemiddelinteraktioner**: Der er identificeret 100 mulige interaktioner i interaktionsdatabasen (DDInter), men alvorlighedsgraden er angivet som "ukendt" for alle viste. Eksempler: calcitriol, clotrimazol, morfin, metformin, pantoprazol, omeprazol, vancomycin, prednison, simvastatin og rosuvastatin. Klinisk relevans er ikke vurderet.

Oplysninger om advarsler og kontraindikationer fra produktresuméet mangler. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om pleural empyem har kun evidensniveau L5 uden forsøg eller publikationer, og den topiske administrationsvej gør det farmakologisk usandsynligt, at stoffet kan nå infektionsstedet.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Sikkerhedsoplysninger fra produktresuméet (advarsler og kontraindikationer) fra Lægemiddelstyrelsen
- Dokumentation for, at en relevant systemisk eller lokal formulering kan opnå tilstrækkelig eksponering i pleurahulen
- Prækliniske eller kliniske data, der understøtter effekt ved pleural empyem

---

## Bemærkning om øvrige forudsigelser

Andre forudsigelser i de indsamlede data har ligeledes begrænset evidens:

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Punktformet epitelial keratokonjunktivitis | 0,9910 | L5 | Hold. Ofte viral eller immunmedieret, og mupirocin er ikke udviklet til øjenbrug |

**Litteratur om kutan candidiasis:**

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [1678836](https://pubmed.ncbi.nlm.nih.gov/1678836/) | 1991 | Klinisk studie (design ikke bekræftet) | Lancet | Undersøgelse af mupirocins effekt ved kutan candidiasis |
| [24021363](https://pubmed.ncbi.nlm.nih.gov/24021363/) | 2013 | Case report | Dermatology Online Journal | Perianal og periumbilikal dermatitis med gruppe G-streptokokinfektion samt gennemgang af lignende hudlidelser |

Mupirocin er primært antibakterielt og ikke et egentligt antimykotikum. En eventuel effekt kan skyldes behandling af samtidige bakterielle infektioner. Etablerede antimykotika forbliver standardbehandling.

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Pirnuo (mupirocin) prescribing information, Glenmark Pharmaceuticals Inc., USA](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=89c43f7b-1a88-45bf-a356-07518d4e7870) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

