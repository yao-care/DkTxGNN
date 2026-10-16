---
layout: default
title: Becaplermin
parent: Kun modelforudsigelse (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Becaplermin: forudsagt ny indikation Amenoré (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data"
---

# Becaplermin
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

# Becaplermin: Fra sårheling til amenoré (forudsigelse uden evidens)

## Resumé

Becaplermin er en rekombinant human vækstfaktor (PDGF-BB), som anvendes som lokalt gel til sårbehandling. Den originale godkendte indikation fremgår ikke af de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **amenoré**, men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter denne retning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Original indikation | Ikke angivet i de indsamlede data |
| Forudsagt ny indikation | Amenoré |
| TxGNN-forudsigelsesscore | 99,86 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ikke detaljerede data om virkningsmekanismen i de indsamlede data. Becaplermin er imidlertid kendt som rekombinant human PDGF-BB. Stoffet aktiverer PDGF-receptorerne (PDGFR-alfa/beta) og stimulerer dermed fibroblastproliferation, angiogenese og sårgranulation.

Der er ikke identificeret nogen plausibel forbindelse mellem denne mekanisme og de forhold, der ligger bag amenoré, dvs. hypothalamus-hypofyse-ovarie-aksen eller livmoder- og endometriepatologi. Da produktet kun anvendes lokalt på huden, er systemiske effekter på reproduktionssystemet desuden usandsynlige. Den høje score er en rent grafbaseret forudsigelse uden støtte i forsøg eller litteratur.

Modellen har også forudsagt andre indikationer, som alle har evidensniveau L5 og anbefalingen Hold:

| Forudsagt indikation | TxGNN-score | Vurdering af mekanisme |
|------|------|------|
| Erektil dysfunktion | 99,72 % | Spekulativ forbindelse via PDGF i karombygning og angiogenese. PDGF er også impliceret i fibrose (f.eks. Peyronies sygdom), hvilket kan være skadeligt. |
| HER2-positiv brystkræft | 99,70 % | Becaplermin er en PDGFR-agonist og vil snarere kunne stimulere end hæmme tumorvækst. Effektretningen er sandsynligvis modsat terapeutisk gavn. |
| Progesteronreceptor-negativ brystkræft | 99,50 % | Samme betænkelighed som ovenfor. Mekanismen er tvivlsom. |
| Pulmonal hypertension | 99,49 % | PDGF driver ombygning af lungearterier, og PDGFR-hæmmere er undersøgt som behandling. Som agonist kan becaplermin forværre tilstanden. |

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101915697 | Regranex (Janssen-Cilag International NV) | Gel | Indikationstekst ikke angivet |

---

## Sikkerhedsovervejelser

Der er ikke tilgængelige data om advarsler, kontraindikationer eller lægemiddelinteraktioner i de indsamlede data. Der blev ikke fundet registrerede interaktioner.

Nogle forudsagte indikationer giver dog anledning til særlig opmærksomhed. Som PDGFR-agonist kan becaplermin teoretisk fremme tumorvækst, og produktomtalen har tidligere indeholdt en advarsel om risiko for malignitet ved øget brug. Advarslen er senere fjernet. Det taler imod at forfølge de forudsagte kræftindikationer.

Se i øvrigt den godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelserne bygger udelukkende på modellens graf (evidensniveau L5), uden kliniske forsøg eller litteratur. Mekanismen for en lokal PDGFR-agonist passer ikke til nogen af de forudsagte indikationer. For kræft og pulmonal hypertension peger den biologiske effekt sandsynligvis i skadelig retning.

**For at komme videre kræves følgende:**
- Den godkendte indikationstekst og produktresuméet (SmPC) fra Lægemiddelstyrelsen med advarsler og kontraindikationer
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Præklinisk eller klinisk evidens, der kan understøtte en forbindelse til den forudsagte indikation
- En vurdering af, om lokal administration overhovedet er forenelig med de forudsagte systemiske indikationer
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

