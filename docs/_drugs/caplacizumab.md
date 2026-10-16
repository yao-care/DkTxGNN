---
layout: default
title: Caplacizumab
parent: Kun modelforudsigelse (L5)
nav_order: 155
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Caplacizumab: forudsagt ny indikation Primær frigørelsesforstyrrelse af blodplader (evidensniveau L5). Oprindelig indikation: Trombocytopenisk purpura (erhvervet TTP)"
---

# Caplacizumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

# Caplacizumab: Fra trombocytopenisk purpura til primær frigørelsesforstyrrelse af blodplader

## Resumé i få sætninger

Caplacizumab er en anti-von Willebrand-faktor (vWF) nanobody, som oprindeligt anvendes til behandling af trombocytopenisk purpura (i praksis erhvervet trombotisk trombocytopenisk purpura, TTP).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **primær frigørelsesforstyrrelse af blodplader** (primary release disorder of platelets).
Forudsigelsen er **udelukkende modelbaseret**: der er **0 kliniske studier** og **0 publikationer** for netop denne indikation, og den mekanistiske sammenhæng vurderes som svag.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Trombocytopenisk purpura (erhvervet TTP) |
| Forudsagt ny indikation | Primær frigørelsesforstyrrelse af blodplader |
| TxGNN-prædiktionsscore | 99,9998 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede data om virkningsmekanismen fra lægemiddeldatabasen var ikke tilgængelige i de data, der er indsamlet til denne rapport. Ud fra den kendte farmakologi binder caplacizumab A1-domænet i vWF og blokerer dermed vWF's binding til blodpladernes GPIb-IX-V-receptor. Ved erhvervet TTP mangler enzymet ADAMTS13, så ultralange vWF-multimerer ophobes og driver mikrotrombedannelse. Caplacizumab rammer netop denne mekanisme.

Primære frigørelsesforstyrrelser af blodplader er derimod iboende defekter i pladernes lagrings- eller sekretionsfunktion. De drives ikke af vWF-medieret adhæsion. Sygdommen er en blødningsforstyrrelse, og en hæmning af vWF-pladebinding forventes snarere at forværre end at forbedre tilstanden. Den meget høje TxGNN-score afspejler sandsynligvis nærhed i vidensgrafen mellem blodpladesygdomme og ikke et reelt terapeutisk rationale.

Blandt de øvrige forudsigelser er pseudo-von Willebrand-sygdom den eneste med en teoretisk plausibel kobling. Den skyldes gain-of-function-mutationer i GPIbα, som øger pladernes affinitet for vWF. Også her er der dog betydelig blødningsrisiko, og der findes ingen kliniske data. Glanzmanns trombasteni og Scott-syndrom har ingen tydelig mekanistisk forbindelse til caplacizumab, og yderligere svækkelse af pladefunktionen vil forventes at øge blødningsrisikoen.

Det bemærkes, at TTP-forudsigelsen i datasættet (evidensniveau L1) er lægemidlets godkendte oprindelige indikation og altså ikke egentlig repurposing.

---

## Evidens fra kliniske studier

Der er på nuværende tidspunkt ingen registrerede kliniske studier for primær frigørelsesforstyrrelse af blodplader.

Til orientering: De studier, der findes for caplacizumab, vedrører den oprindelige indikation (erhvervet TTP), bl.a. fase 3-studiet HERCULES (NCT02553317, n=145) og fase 2-studiet TITAN (NCT01151423, n=75). De kan ikke overføres til den forudsagte indikation.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relevant litteratur for primær frigørelsesforstyrrelse af blodplader.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105912417 | Cablivi (Ablynx NV) | Pulver og solvens til injektionsvæske, opløsning | Indikationsteksten er ikke angivet i de indsamlede data |

---

## Sikkerhedsmæssige overvejelser

**Lægemiddelinteraktioner:** Interaktionsforespørgslen er gennemført og viser i alt 100 registrerede interaktioner. Blandt de gennemgåede er følgende af betydning, især fordi caplacizumab hæmmer pladeadhæsion og dermed øger blødningsrisikoen.

- **Alvorlige (Major):** acetylsalicylsyre, abciximab, alteplase, fondaparinux, anagrelid, acalabrutinib, deferasirox, trastuzumab emtansin, ibritumomab tiuxetan og tositumomab (inkl. I-131).
- **Moderate:** ibuprofen, ketorolac (inkl. oftalmisk), celecoxib, topisk diclofenac, fluvoxamin, fenfluramin, dexfenfluramin og sibutramin.

Ved en blødningsforstyrrelse som den forudsagte indikation vil disse kombinationer have ekstra vægt. Oplysninger om advarsler og kontraindikationer findes i det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger kun på en grafbaseret modelscore uden kliniske studier eller litteratur. Caplacizumabs virkningsmekanisme (hæmning af vWF-pladebinding) peger desuden mod øget blødningsrisiko ved en blødningsforstyrrelse i blodpladerne, ikke mod gavn.

**For at komme videre kræves:**
- Hentning af data om virkningsmekanisme og af produktresuméets advarsler og kontraindikationer, så sikkerhedsscreeningen kan gennemføres
- En fornyet mekanistisk vurdering, evt. med præklinisk dokumentation, før et eventuelt klinisk spor overvejes
- Hvis der alligevel ønskes en videre udredning, bør pseudo-von Willebrand-sygdom prioriteres, med en grundig risikovurdering af blødning
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

