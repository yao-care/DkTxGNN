---
layout: default
title: Moroctocog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 567
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Moroctocog Alfa: forudsagt ny indikation Primær frigivelsesforstyrrelse af blodplader (evidensniveau L5). Oprindelig indikation: Hæmofili"
monitor_inn: "MOROCTOCOG ALFA"
predicted_indications: ["primary release disorder of platelets", "primary release disorder of platelets", "pseudo-von Willebrand disease", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Glanzmann thrombasthenia", "acquired coagulation factor deficiency", "acquired coagulation factor deficiency", "Scott syndrome", "Scott syndrome"]
---

# Moroctocog Alfa
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

# Moroctocog alfa: Fra hæmofili til primær frigivelsesforstyrrelse af blodplader

## Resumé i én sætning

Moroctocog alfa er rekombinant human koagulationsfaktor VIII (B-domæne-deleteret), som oprindeligt anvendes til behandling af hæmofili.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **primær frigivelsesforstyrrelse af blodplader**,
men der er **ingen registrerede kliniske forsøg** og **ingen publikationer**, som understøtter denne retning. Forudsigelsen hviler alene på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hæmofili (jf. vidensgrafen; godkendt indikationstekst for det danske produkt er ikke tilgængelig i de indsamlede data) |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN-prædiktionsscore | 99,97 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Moroctocog alfa er rekombinant faktor VIII, som erstatter manglende faktor VIII i koagulationskaskaden og anvendes ved hæmofili.

Primære frigivelsesforstyrrelser af blodplader er kvalitative defekter i trombocytfunktionen (nedsat granulesekretion og signalering). De skyldes ikke mangel på faktor VIII. Tilførsel af faktor VIII forventes derfor ikke at korrigere den iboende trombocytdefekt. Den høje score afspejler sandsynligvis, at sygdommene ligger tæt på hinanden i vidensgrafen som "blødningssygdomme", snarere end en reel mekanistisk sammenhæng.

### Øvrige forudsagte indikationer

Modellen foreslog også følgende. Alle har evidensniveau L5 og anbefalingen Hold:

| Sygdom | Score | Vurdering |
|------|------|------|
| Pseudo-von Willebrands sygdom | 99,97 % | Teoretisk forbindelse via VWF-FVIII-aksen, men årsagen er øget GPIbα-funktion i blodpladerne. Standardbehandling er trombocyttransfusion, og FVIII-substitution adresserer ikke defekten. |
| Glanzmanns trombasteni | 99,96 % | Skyldes manglende eller dysfunktionelt integrin αIIbβ3. FVIII er normal, så der er ingen mekanistisk begrundelse. Etablerede muligheder er trombocyttransfusion, antifibrinolytika og rekombinant faktor VIIa. |
| Erhvervet koagulationsfaktormangel | 99,88 % | Mekanistisk mest plausibel, især ved erhvervet hæmofili A. Her er autoantistoffer mod FVIII dog årsagen, og førstevalg er bypassing-midler (rFVIIa, aPCC) eller porcint FVIII med immunsuppression. Begrebet er bredt og dækker flere faktormangler, som FVIII alene ikke afhjælper. |
| Scotts syndrom | 99,86 % | Skyldes defekt fosfatidylserin-eksponering (TMEM16F/ANO6). FVIII er normal; sammenhængen er svag og spekulativ. |

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| MA 28103002398 | ReFacto (Pfizer Europe MA EEIG) | Pulver og solvens til injektionsvæske, opløsning | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

Der henvises til det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. I de indsamlede data er der ikke fundet registrerede lægemiddelinteraktioner, og vidensgrafen indeholder ingen kontraindikationer for dette lægemiddel.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modelforudsigelse (L5) uden kliniske forsøg eller litteratur. Den mekanistiske sammenhæng er svag eller fraværende for de fleste af de foreslåede sygdomme, og der findes etablerede behandlinger, som målrettet adresserer de underliggende defekter.

**For at komme videre kræves følgende:**
- Detaljerede data om virkningsmekanismen (MOA), f.eks. fra DrugBank
- Godkendt indikationstekst og sikkerhedsoplysninger (advarsler og kontraindikationer) fra produktresuméet hos Lægemiddelstyrelsen
- Præklinisk eller klinisk evidens for, at FVIII-substitution har gavn ved den forudsagte sygdom
- Hvis man vil arbejde videre med en af forudsigelserne, bør erhvervet koagulationsfaktormangel (specifikt erhvervet hæmofili A) vurderes først, herunder betydningen af hæmmende antistoffer
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

