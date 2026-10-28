---
layout: default
title: Moroctocog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 567
evidence_level: L5
indication_count: 8
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "Scott syndrome", "bleeding diathesis due to a collagen receptor defect", "hemorrhagic disorder due to a constitutional thrombocytopenia", "flood factor deficiency"]
last_modified_at: 2026-10-28
description: "Moroctocog Alfa: forudsagt ny indikation Primær frigivelsesforstyrrelse af blodplader (evidensniveau L5). Oprindelig indikation: Hæmofili"
---

# Moroctocog Alfa
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **8** stk.
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

## Moroctocog alfa: Fra hæmofili til primær frigivelsesforstyrrelse af blodplader
{: .text-alpha }

## Resumé

Moroctocog alfa er en rekombinant koagulationsfaktor VIII (B-domæne-deleteret), som er knyttet til hæmofili og til symptomatisk hæmofili hos kvindelige bærere. Dens ordinære anvendelse i Danmark dokumenteres her via ét markedsført præparat (ReFacto), men der er ikke indikationstekst i de foreliggende data.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **primær frigivelsesforstyrrelse af blodplader**, men der er **ingen kliniske forsøg** og **ingen publikationer** i de data, der er indsamlet til denne rapport. Forudsigelsen er derfor ren modelgenereret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hæmofili (relation registreret i vidensgrafen; indikationsteksten i den danske godkendelse er ikke tilgængelig) |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN-forudsigelsesscore | 0,9997 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til denne rapport. Moroctocog alfa er dog en rekombinant faktor VIII med deleteret B-domæne, som indgår i det intrinsiske tenasekompleks i den sekundære hæmostase og erstatter manglende faktor VIII.

Primære frigivelsesforstyrrelser af blodplader (defekter i lagring og sekretion) er fejl i den primære hæmostase. Erstatning af faktor VIII forventes derfor ikke mekanistisk at rette op på dem. Den høje score skyldes sandsynligvis grafnærhed, fordi sygdommene deler knudepunkter med andre blødningssygdomme, og ikke en reel mekanistisk sammenhæng.

### Øvrige forudsagte indikationer

Modellen foreslog yderligere kandidater. Ingen af dem har kliniske forsøg eller litteratur i datagrundlaget:

| Rang | Sygdom | Score | Vurdering |
|---|---|---|---|
| 2 | Pseudo-von Willebrands sygdom | 0,9997 | Kerneproblemet er trombocytbaseret (GP1BA-varianter); kun en indirekte, teoretisk kobling via VWF. |
| 3 | Glanzmanns trombasteni | 0,9996 | Defekt i integrin αIIbβ3; faktor VIII retter ikke aggregationsdefekten. Standardbehandling er trombocyttransfusion og rekombinant FVIIa. |
| 4 | Erhvervet koagulationsfaktormangel | 0,9988 | Mekanistisk mest plausibel (fx erhvervet hæmofili A), men hæmmende autoantistoffer neutraliserer ofte infunderet FVIII, og bypass-midler er standard. Kategorien er bred og uensartet. Betragtes som et forskningsspørgsmål. |
| 5 | Scott syndrom | 0,9986 | Defekt i fosfatidylserin-eksponering (TMEM16F/ANO6); FVIII-tilgængelighed er ikke den begrænsende faktor. |
| 6 | Blødningstendens pga. kollagenreceptordefekt | 0,9973 | Defekt i trombocytadhæsion og -aktivering (primær hæmostase). |
| 7 | Blødningssygdom pga. konstitutionel trombocytopeni | 0,9972 | Defekt i trombocyttal eller -produktion; FVIII korrigerer ikke dette. |
| 8 | "Flood factor deficiency" | 0,9911 | Ikke et anerkendt sygdomsnavn, muligvis en ontologi- eller navngivningsartefakt. Kan ikke vurderes, før entiteten er kurateret. |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

| Tilladelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28103002398 | ReFacto (Pfizer Europe MA EEIG) | Pulver og solvens til injektionsvæske, opløsning | Indikationstekst er ikke tilgængelig i de foreliggende data |

Antal tilladelser: 1 national tilladelse (gyldig, enkeltstofpræparat).

---

## Sikkerhedsovervejelser

Der henvises til det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der blev ikke fundet registrerede lægemiddelinteraktioner i de data, der er indsamlet til denne rapport.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5) uden kliniske forsøg eller litteratur, og mekanismen (substitution af faktor VIII) passer ikke til en defekt i trombocytfunktionen. Den høje score afspejler sandsynligvis grafnærhed.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé fra Lægemiddelstyrelsen med advarsler, kontraindikationer og godkendt indikationstekst
- Kuratering af sygdomsnavnet "flood factor deficiency" mod kildeontologien
- Hvis der ønskes videre udforskning, bør "erhvervet koagulationsfaktormangel" undersøges som et forskningsspørgsmål med en systematisk litteratursøgning
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

