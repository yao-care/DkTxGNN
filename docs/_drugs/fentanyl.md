---
layout: default
title: Fentanyl
parent: Kun modelforudsigelse (L5)
nav_order: 354
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Fentanyl: forudsagt ny indikation Nefrogent syndrom med uhensigtsmæssig antidiurese (evidensniveau L5). Oprindelig indikation: Ikke tilgængelig i de indsamlede data (godkendelsens indikationstekst…"
monitor_inn: "FENTANYL"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
---

# Fentanyl
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

## Fentanyl: Fra smertebehandling til nefrogent syndrom med uhensigtsmæssig antidiurese
{: .text-alpha }

## Resumé i én sætning

Fentanyl er en stærk opioid (mu-opioidreceptoragonist), som i Danmark markedsføres som depotplaster (Durogesic). Den oprindelige godkendte indikationstekst er ikke tilgængelig i de data, der er indsamlet til denne rapport. TxGNN-modellen forudsiger, at fentanyl kan være effektivt ved **nefrogent syndrom med uhensigtsmæssig antidiurese (NSIAD)**, men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter forudsigelsen. Evidensen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke tilgængelig i de indsamlede data (godkendelsens indikationstekst er tom) |
| Forudsagt ny indikation | Nefrogent syndrom med uhensigtsmæssig antidiurese |
| TxGNN-forudsigelsesscore | 0,9946 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

Bemærk: Den næsthøjest rangerede forudsigelse er **Tourettes syndrom** (score 0,9905, evidensniveau L5, anbefaling Hold). Begge forudsigelser optræder to gange i datagrundlaget.

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Data om fentanyls detaljerede virkningsmekanisme er ikke tilgængelige i det indsamlede materiale. Fentanyl er dog generelt kendt som en mu-opioidreceptoragonist med stærk smertestillende effekt.

NSIAD skyldes en aktiverende (gain-of-function) mutation i vasopressin V2-receptoren (AVPR2), som virker uafhængigt af vasopressin. Opioider kan påvirke frigivelsen af antidiuretisk hormon og nyrernes vandhåndtering, men en mu-opioidagonist forventes ikke at kunne korrigere en defekt på receptorniveau. Forudsigelsen er derfor biologisk usandsynlig uden yderligere evidens. Scoren stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

For **Tourettes syndrom** involverer sygdommen forstyrrelser i cortico-striato-thalamo-corticale kredsløb og dopaminerg signalering. Endogen opioidmodulation af disse kredsløb er undersøgt i litteraturen, men fentanyl har ingen etableret terapeutisk rolle. Misbrugspotentiale, risiko for respirationsdepression samt tolerans- og afhængighedsprofil gør stoffet til en dårlig kandidat til en kronisk neuropsykiatrisk tilstand.

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101545493 | Durogesic (Janssen-Cilag A/S) | Depotplaster | Indikationstekst ikke tilgængelig |

Status: gyldig, enkeltstofpræparat. Der er ingen annullerede tilladelser.

---

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer var ikke tilgængelige i de indsamlede data. Der henvises til det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

**Sygdomme, der i vidensgrafen er koblet til kontraindikation** (fra TxGNN-vidensgrafen, ikke fra produktresuméet), blandt andet:
- Hjerte-kar: hypertension, hypotension, ortostatisk hypotension, langt QT-syndrom, torsades de pointes
- Lunge: kronisk obstruktiv lungesygdom (KOL), astma
- Lever, nyrer og mave-tarm: leversvigt, leversygdom, nyresygdom, pankreatitis, galdeblæresygdom, inflammatorisk tarmsygdom
- Neurologi og psykiatri: multipel systematrofi, basalganglie-sygdom, blefarospasme, angstlidelse, dysthymi, misbrug/afhængighed
- Øvrige: kaliummangel, benign prostatahyperplasi

**Lægemiddelinteraktioner** (100 interaktioner fundet i alt; et udvalg):

| Niveau | Interagerende lægemidler |
|------|------|
| Major | Alvimopan, aprepitant, bupropion, clarithromycin, clotrimazol, dexamethason, dexfenfluramin, dolasetron, fenfluramin, granisetron, lorcaserin |
| Moderat | Atropin, cimetidin, clidinium, dicyclomin, dronabinol, eluxadolin, glycerolphenylbutyrat, glycopyrronium, hyoscyamin |

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en grafbaseret modelscore uden kliniske forsøg eller litteratur. Den biologiske sammenhæng er svag (NSIAD er en receptordefekt i V2-receptoren), og fentanyls sikkerhedsprofil, herunder misbrugspotentiale og respirationsdepression, taler imod anvendelse ved kroniske tilstande som Tourettes syndrom.

**For at komme videre kræves følgende:**
- Fuldstændige data om virkningsmekanisme (MOA)
- Produktresuméets advarsler og kontraindikationer fra Lægemiddelstyrelsen samt den godkendte indikationstekst
- Prækliniske data eller et mekanistisk rationale for den forudsagte indikation
- En sikkerhedsfokuseret gennemgang før yderligere overvejelser
- Vurdering af administrationsvej (depotplaster) i forhold til den forudsagte indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

