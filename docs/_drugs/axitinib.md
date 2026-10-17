---
layout: default
title: Axitinib
parent: Kun modelforudsigelse (L5)
nav_order: 91
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Axitinib: forudsagt ny indikation Nyrecellekarcinom forbundet med Xp11.2-translokationer/TFE3-genfusion… (evidensniveau L5). Oprindelig indikation: Nyrecellekarcinom (klarcellet, ikke-papillært…"
monitor_inn: "Axitinib"
predicted_indications: ["liposarcoma", "liposarcoma"]
---

# Axitinib
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

# Axitinib: Fra nyrecellekarcinom til nyrecellekarcinom forbundet med Xp11.2-translokationer/TFE3-genfusioner

## Opsummering i én sætning

Axitinib er en oral tyrosinkinasehæmmer, der oprindeligt anvendes til behandling af nyrecellekarcinom (herunder klarcellet type).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **nyrecellekarcinom forbundet med Xp11.2-translokationer/TFE3-genfusioner**,
og der findes **1 klinisk forsøg** (fase 2, 15 patienter, ingen offentliggjorte resultater) og **ingen publikationer** for netop denne indikation.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Nyrecellekarcinom (klarcellet, ikke-papillært, nyrecelleadenokarcinom). Godkendelsesteksten i den danske tilladelse er ikke angivet i de indsamlede data, så indikationerne stammer fra TxGNN-vidensgrafen |
| Forudsagt ny indikation | Nyrecellekarcinom forbundet med Xp11.2-translokationer/TFE3-genfusioner |
| TxGNN-forudsigelsesscore | 99,90 % |
| Evidensniveau | L2 (designmæssigt signal fra ét randomiseret fase 2-forsøg; ikke påvist effekt) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails |

---

## Hvorfor er denne forudsigelse rimelig?

Data om lægemidlets detaljerede virkningsmekanisme er ikke tilgængelige i de indsamlede data. Axitinib er dog kendt som en hæmmer af VEGF-receptorerne 1-3 (VEGFR1-3), og dets effekt ved nyrecellekarcinom er veletableret. Mekanistisk kan det derfor være relevant for beslægtede nyrecellesubtyper.

Nyrecellekarcinom med Xp11.2/TFE3-translokation er en ikke-klarcellet subtype, hvor der er rapporteret følsomhed over for VEGFR-rettet behandling. Hæmning af angiogenese kan derfor give en rationel baggrund. Kombinationen med nivolumab (PD-1-blokade) tilføjer en immunterapeutisk komponent.

Bemærk, at den høje TxGNN-score sandsynligvis afspejler den tætte relation til den overordnede diagnose nyrecellekarcinom og ikke selvstændig dokumentation for denne subtype.

---

## Evidens fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT03595124](https://clinicaltrials.gov/study/NCT03595124) | Fase 2 | Aktivt, rekrutterer ikke | 15 | Randomiseret sammenligning af axitinib + nivolumab versus nivolumab alene ved inoperabelt eller metastatisk TFE/translokations-nyrecellekarcinom i alle aldersgrupper. Planlagt afslutning: nov. 2026. Ingen resultater tilgængelige |

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur for denne indikation.

Til oplysning findes der for andre forudsagte indikationer: en oversigtsartikel om avanceret pædiatrisk nyrecellekarcinom ([31012542](https://pubmed.ncbi.nlm.nih.gov/31012542/), 2019), en case report om axitinib hos et barn med malignt epiteloidt angiomyolipom ([26279736](https://pubmed.ncbi.nlm.nih.gov/26279736/), 2015) og et præklinisk studie ved myxoid liposarkom ([27822137](https://pubmed.ncbi.nlm.nih.gov/27822137/), 2016). Disse understøtter ikke direkte den indikation, der er i fokus her.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106940523 | Axitinib "Accord" (Accord Healthcare S.L.U.) | Filmovertrukne tabletter | Indikationstekst ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Målrettet behandling (tyrosinkinasehæmmer, VEGFR), ikke konventionel cytotoksisk kemoterapi |
| Risiko for myelosuppression | Se produktresuméet (SmPC) |
| Emetogenicitetsklasse | Se produktresuméet (SmPC) |
| Monitorering | Se produktresuméet (SmPC) for anbefalede kontroller |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) og lokale retningslinjer |

Der henvises til advarsler og forsigtighedsregler i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

Data om advarsler og kontraindikationer er ikke tilgængelige i de indsamlede data. Der henvises til det godkendte produktresumé (SmPC).

**Lægemiddelinteraktioner** (100 interaktioner registreret; udvalgte nedenfor):
- **Alvorlige (Major):** clarithromycin, dexamethason
- **Moderate:** aprepitant, clotrimazol, miconazol, naltrexon
- **Mindre (Minor):** bl.a. famotidin, ranitidin, cimetidin, protonpumpehæmmere (rabeprazol, esomeprazol, lansoprazol, dexlansoprazol) og antacida (aluminiumhydroxid, calciumcarbonat, magnesiumsalte)

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Axitinib er markedsført i Danmark og har en veletableret rolle ved nyrecellekarcinom, og der pågår et randomiseret fase 2-forsøg ved TFE3-translokationskarcinom. Forsøget er dog meget lille (n=15), uden tilgængelige resultater, og der er ingen supplerende litteratur. Evidensen er derfor kun et designmæssigt signal. Øvrige forudsagte indikationer (f.eks. neuroblastomassocieret og uklassificeret nyrecellekarcinom, pædiatrisk nyrecellekarcinom og liposarkom) har kun prædiktions-, case- eller præklinisk evidens og bør afvente (Hold).

**For at komme videre kræves:**
- Resultater fra NCT03595124 (forventet afslutning nov. 2026)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Gennemgang af produktresuméets advarsler og kontraindikationer (blokerende datahul for sikkerhedsscreening)
- Afklaring af godkendt indikationstekst for den danske tilladelse
- Sikkerhedsovervågningsplan, herunder håndtering af interaktioner med CYP3A4-hæmmere/-induktorer (f.eks. clarithromycin, dexamethason)
- For pædiatriske patienter: dosis- og sikkerhedsdata for axitinib
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

