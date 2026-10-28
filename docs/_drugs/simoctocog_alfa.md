---
layout: default
title: Simoctocog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 762
evidence_level: L5
indication_count: 9
monitor_inn: "SIMOCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
last_modified_at: 2026-10-28
description: "Simoctocog Alfa: forudsagt ny indikation Pseudo-von Willebrand sygdom (evidensniveau L5). Oprindelig indikation: Hæmofili"
---

# Simoctocog Alfa
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **9** stk.
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

## Simoctocog alfa: Fra hæmofili til pseudo-von Willebrand sygdom
{: .text-alpha }

## Resumé i én sætning

Simoctocog alfa er en rekombinant human koagulationsfaktor VIII, som oprindeligt anvendes til behandling af hæmofili.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **pseudo-von Willebrand sygdom**,
men der er **ingen registrerede kliniske forsøg** og **ingen publikationer**, der understøtter denne forudsigelse. Den er udelukkende baseret på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hæmofili (relation registreret i vidensgrafen; der foreligger ingen godkendt indikationstekst i de danske lægemiddeldata) |
| Forudsagt ny indikation | Pseudo-von Willebrand sygdom |
| TxGNN-forudsigelsesscore | 1,0000 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til denne rapport. Simoctocog alfa er et rekombinant humant faktor VIII-præparat (B-domæne-deleteret, produceret i en human cellelinje), som erstatter manglende faktor VIII ved hæmofili.

Pseudo-von Willebrand sygdom (blodpladetype) skyldes en funktionsforøgende defekt i blodpladernes GPIbα, som øger bindingen til von Willebrand-faktor (VWF). Det medfører tab af højmolekylære VWF-multimerer og nedsat VWF-funktion. Faktor VIII-niveauet kan være normalt eller kun let nedsat, og faktor VIII-substitution adresserer derfor ikke den primære blodpladedefekt.

Den høje modelscore kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede blødningssygdomme, ikke biologisk evidens. Forudsigelsen bør betragtes med stor forsigtighed.

### Øvrige forudsagte indikationer (alle evidensniveau L5)

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| Primær frigivelsesforstyrrelse af blodplader | 1,0000 | Intrinsisk blodpladedefekt; faktor VIII korrigerer ikke sekretionen |
| Glanzmanns trombasteni | 1,0000 | Defekt i integrin αIIbβ3; standardbehandling er blodpladetransfusion og rekombinant FVIIa |
| Scott syndrom | 0,9997 | Teoretisk link via den prokoagulante overflade, men FVIII kan ikke genskabe den manglende fosfolipidoverflade |
| Erhvervet koagulationsfaktormangel | 0,9995 | Mekanistisk mest plausibel (fx erhvervet hæmofili A), men neutraliserende autoantistoffer begrænser effekten, og bypassing-midler er standard; kategorien er bred |
| Blødningstendens ved kollagenreceptordefekt | 0,9992 | Primær blodpladedefekt uden direkte rationale for FVIII |
| Hæmoragisk lidelse ved konstitutionel trombocytopeni | 0,9992 | Blødning skyldes blodplademangel, ikke FVIII-mangel |
| Føtal og neonatal alloimmun trombocytopeni | 0,9984 | Immunmedieret blodpladedestruktion; FVIII har ingen rolle |
| Trombotisk trombocytopenisk purpura (TTP) | 0,9972 | Sandsynligvis falsk positiv; FVIII er prokoagulant og kan øge trombosisiko |

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105298513 | Nuwiq (Octapharma AB) | Pulver og solvens til injektionsvæske, opløsning | Indikationstekst ikke tilgængelig i de indsamlede data |

Antal tilladelser: 1 (gyldig, enkeltstofpræparat).

---

## Sikkerhedsovervejelser

Der foreligger ingen produktresumédata om advarsler, kontraindikationer eller interaktioner i de indsamlede data. Der blev ikke fundet registrerede lægemiddelinteraktioner.

Bemærk dog, at vurderingen af de forudsagte indikationer peger på en potentiel sikkerhedsbekymring ved **trombotisk trombocytopenisk purpura (TTP)**, hvor et prokoagulant middel som faktor VIII i princippet kan øge risikoen for trombose.

Se i øvrigt det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (evidensniveau L5), uden kliniske forsøg eller publikationer for nogen af de forudsagte sygdomme. Den mekanistiske sammenhæng er svag eller fraværende for de fleste af dem, og for TTP er der en mulig sikkerhedsrisiko.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) og produktresumé med advarsler og kontraindikationer
- Hvis man vil forfølge en af forudsigelserne, bør "erhvervet koagulationsfaktormangel" præciseres til en bestemt undertype (fx erhvervet hæmofili A) og vurderes i en systematisk litteraturgennemgang
- Præklinisk eller mekanistisk dokumentation for, at faktor VIII-substitution gavner den pågældende sygdom
- Vurdering af administrationsvej og lægemiddelform i forhold til den nye indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

