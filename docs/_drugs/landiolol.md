---
layout: default
title: Landiolol
parent: Kun modelforudsigelse (L5)
nav_order: 478
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-14
description: "Landiolol: forudsagt ny indikation Lingual-facial-bukkal dyskinesi (evidensniveau L5). Oprindelig indikation: Supraventrikulær takykardi (atrieflimren og atrieflagren) iht. farmak…"
monitor_inn: "landiolol"
predicted_indications: ["lingual-facial-buccal dyskinesia", "chronic tic disorder", "psychogenic movement disorders", "extrapyramidal and movement disease", "benign shuddering attacks", "primary orthostatic tremor"]
---

# Landiolol
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
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

# Landiolol: Fra supraventrikulær takykardi til lingual-facial-bukkal dyskinesi

## Resumé i én sætning

Landiolol er en ultrakortvirkende, stærkt beta-1-selektiv adrenerg antagonist, som anvendes intravenøst til hurtig reduktion af hjerterytmen ved supraventrikulære takyarytmier (f.eks. atrieflimren og atrieflagren).
TxGNN-modellen forudsiger, at lægemidlet muligvis kan have effekt ved **lingual-facial-bukkal dyskinesi**.
Der er dog **ingen kliniske forsøg** og **ingen publikationer** i de data, der er indsamlet til denne rapport, så forudsigelsen hviler udelukkende på modellens score.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Supraventrikulær takykardi (atrieflimren og atrieflagren) iht. farmakologidata; indikationsteksten i den danske markedsføringstilladelse er ikke angivet |
| Forudsagt ny indikation | Lingual-facial-bukkal dyskinesi |
| TxGNN-forudsigelsesscore | 99,11 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig (eller ikke)?

Der foreligger ikke detaljerede data om landiolols virkningsmekanisme i de samlede data. Det er dog kendt, at landiolol er en intravenøs, ultrakortvirkende beta-1-selektiv blokker, ca. 250 gange mere selektiv for beta-1- end for beta-2-adrenoceptorer. Dets kendte farmakologi er kardial (frekvenskontrol ved supraventrikulære takyarytmier).

Orofacial dyskinesi hænger sammen med dysfunktion i de dopaminerge systemer i basalganglierne. Der er ingen etableret central mekanisme, hvorigennem selektiv beta-1-blokade kan påvirke tilstanden. Nogle beta-blokkere virker perifert på visse bevægelsessymptomer (f.eks. tremor), men landiolol er hydrofilt med minimal penetration til centralnervesystemet. Sammenhængen er derfor svag og spekulativ.

TxGNN-scoren (0,991) er alene en grafbaseret forudsigelse og kan ikke i sig selv begrunde det videre forløb.

### Øvrige forudsagte indikationer

Modellen forudsagde også følgende tilstande. Alle har evidensniveau L5 og anbefalingen Hold:

| Rang | Sygdom | TxGNN-score | Kort vurdering |
|------|------|------|------|
| 2 | Kronisk tics-lidelse | 99,08 % | Noradrenerg modulation er relevant (alfa-2-agonister), men beta-1-antagonisme har ingen etableret rolle; en intravenøs, ultrakortvirkende profil passer dårligt til en kronisk tilstand |
| 3 | Psykogene bevægelsesforstyrrelser | 99,05 % | Behandlingen er hovedsageligt ikke-farmakologisk; kun en indirekte perifer effekt på sympatiske symptomer er tænkelig |
| 4 | Ekstrapyramidale bevægelsesforstyrrelser og bevægelsessygdomme | 99,04 % | Bred og heterogen kategori; ekstrapolation fra propranolol er ikke understøttet, da landiolol er beta-1-selektivt, hydrofilt og kortvirkende |
| 5 | Benigne rystelsesanfald (shuddering attacks) | 99,04 % | Sjælden, selvlimiterende tilstand hos børn; risiko-nytte ved en intravenøs hjertemedicin er ugunstig |
| 6 | Primær ortostatisk tremor | 99,00 % | Central højfrekvent oscillator; beta-blokkere er generelt ineffektive, og landiolol penetrerer ikke CNS |

---

## Kliniske forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret.

---

## Litteratur

Der er aktuelt ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105531814 | Rapibloc (Amomed Pharma GmbH) | Koncentrat til injektionsvæske, opløsning | Indikationstekst ikke angivet i de tilgængelige data |

---

## Sikkerhedsovervejelser

Der er ikke tilgængelige data om advarsler og kontraindikationer fra produktresuméet i de data, der er indsamlet til denne rapport. Interaktionsforespørgslen er gennemført, men har kun returneret farmakologiske målproteiner, ikke egentlige lægemiddelinteraktioner:

- **Farmakologiske mål**: Landiolol binder til beta-1-adrenoceptoren (ADRB1) og i mindre grad beta-2-adrenoceptoren (ADRB2).

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en grafbaseret modelscore uden kliniske forsøg eller publikationer. Der er desuden ingen plausibel central mekanisme for et hydrofilt, beta-1-selektivt og ultrakortvirkende intravenøst lægemiddel ved de forudsagte bevægelsesforstyrrelser.

**For at komme videre kræves følgende:**
- Gennemgang af produktresuméet (advarsler og kontraindikationer) fra Lægemiddelstyrelsen, som er en blokerende datamangel for sikkerhedsscreening
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Prækliniske eller mekanistiske data, der kan understøtte en effekt ved dyskinesi
- Litteratur- og forsøgssøgning for beta-blokkere ved orofaciale dyskinesier og tics
- Vurdering af administrationsvej og -varighed i forhold til en kronisk tilstand
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

