---
layout: default
title: Efmoroctocog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 293
evidence_level: L5
indication_count: 9
monitor_inn: "EFMOROCTOCOG ALFA"
predicted_indications: ["pseudo-von Willebrand disease", "primary release disorder of platelets", "Glanzmann thrombasthenia", "Scott syndrome", "acquired coagulation factor deficiency", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "fetal and neonatal alloimmune thrombocytopenia", "thrombotic thrombocytopenic purpura"]
last_modified_at: 2026-10-23
description: "Efmoroctocog Alfa: forudsagt ny indikation Pseudo-von Willebrand sygdom (evidensniveau L5). Oprindelig indikation: Hæmofili"
---

# Efmoroctocog Alfa
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

## Efmoroctocog alfa: Fra hæmofili til pseudo-von Willebrand sygdom
{: .text-alpha }

## Resumé i én sætning

Efmoroctocog alfa er et rekombinant faktor VIII-Fc-fusionsprotein, der oprindeligt er registreret i vidensgrafen i relation til hæmofili.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **pseudo-von Willebrand sygdom**,
men der er **ingen kliniske forsøg** og **ingen publikationer** i de data, der er indsamlet til denne rapport. Forudsigelsen er alene modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hæmofili (relation registreret i vidensgrafen; den danske markedsføringstilladelse indeholder ingen indikationstekst) |
| Forudsagt ny indikation | Pseudo-von Willebrand sygdom |
| TxGNN-forudsigelsesscore | 1,0000 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor kan forudsigelsen forekomme rimelig, og hvorfor er den svag?

Data om lægemidlets oprindelige virkningsmekanisme er ikke tilgængelige. Efmoroctocog alfa er et rekombinant faktor VIII (FVIII) koblet til et Fc-fragment. Det erstatter manglende FVIII i den indre koagulationskaskade og er kendt i relation til hæmofili.

Pseudo-von Willebrand sygdom er en trombocytlidelse, som skyldes funktionsforstærkende varianter i GP1BA. De øger trombocytternes binding til von Willebrand-faktor (VWF) og fører til tab af højmolekylære VWF-multimerer. FVIII-erstatning løber ikke ind i denne trombocytreceptordefekt. Et eventuelt udbytte ville være indirekte. Den høje score kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

### Øvrige forudsagte indikationer

Modellen foreslår også en række andre blødningssygdomme. Ingen af dem har kliniske forsøg eller litteratur i datagrundlaget, og alle er på evidensniveau L5.

| Sygdom | Score | Vurdering af mekanisme |
|------|------|------|
| Primær frigivelsesforstyrrelse af trombocytter | 1,0000 | Defekt i trombocytters granulafrigivelse; FVIII virker ikke på dette. |
| Glanzmanns trombasteni | 1,0000 | Defekt integrin αIIbβ3; FVIII korrigerer ikke aggregationsdefekten. Etableret behandling er trombocyttransfusion og rekombinant FVIIa. |
| Scott syndrom | 0,9997 | Manglende phosphatidylserin-eksponering på trombocytter; mere FVIII genopretter ikke overfladen. Svag og spekulativ kobling. |
| Erhvervet koagulationsfaktormangel | 0,9995 | Biologisk mest plausible kandidat, men kategorien er heterogen. Ved erhvervet hæmofili A vil inhibitorer neutralisere infunderet FVIII. Indikationen skal præciseres. |
| Blødningstendens pga. kollagenreceptordefekt | 0,9992 | Primær trombocytreceptordefekt; ingen direkte mekanistisk kobling. |
| Blødningssygdom pga. konstitutionel trombocytopeni | 0,9992 | Lavt trombocyttal eller nedsat funktion; FVIII hæver ikke trombocyttallet. |
| Føtal og neonatal alloimmun trombocytopeni | 0,9984 | Immunmedieret trombocytdestruktion; behandles med IVIG og kompatible trombocytter. |
| Trombotisk trombocytopenisk purpura (TTP) | 0,9972 | Prokoagulant tilstand med ADAMTS13-mangel; FVIII kan teoretisk forværre trombose. Dette er et sikkerhedsproblem frem for en terapeutisk begrundelse. |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ikke registreret relaterede kliniske forsøg for nogen af de forudsagte indikationer.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105539814 | Elocta (Swedish Orphan Biovitrum AB) | Pulver og solvens til injektionsvæske, opløsning | Indikationstekst er ikke angivet i de indsamlede data |

Der er tale om 1 gyldig national tilladelse til et enkeltstofpræparat.

---

## Sikkerhedsovervejelser

Der foreligger ingen oplysninger om advarsler, kontraindikationer eller lægemiddelinteraktioner i de data, der er indsamlet til denne rapport. Se det godkendte produktresumé (SmPC) for sikkerhedsinformation.

Det skal dog bemærkes, at for TTP kan en prokoagulant behandling som FVIII teoretisk øge risikoen for trombose.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for pseudo-von Willebrand sygdom bygger udelukkende på modelscore uden kliniske forsøg eller litteratur. Mekanismen taler imod en effekt, da sygdommen skyldes en trombocytreceptordefekt, som FVIII ikke korrigerer. Evidensniveauet er derfor L5.

**For at komme videre kræves følgende:**
- Data om lægemidlets virkningsmekanisme
- Præcisering af "erhvervet koagulationsfaktormangel" til en specifik mangel (f.eks. erhvervet hæmofili A), som er den eneste kandidat, der er værd at undersøge nærmere (status: forskningsspørgsmål)
- Gennemgang af produktresuméet for advarsler og kontraindikationer
- Systematisk litteratursøgning og søgning efter kliniske forsøg for de udvalgte indikationer
- Vurdering af ruteforenelighed, som endnu ikke er udført
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

