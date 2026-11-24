---
layout: default
title: Lincomycin
parent: Kun modelforudsigelse (L5)
nav_order: 500
evidence_level: L5
indication_count: 3
last_modified_at: 2026-11-24
description: "Lincomycin: forudsagt ny indikation hyperamylasæmi (evidensniveau L5). Oprindelig indikation: Pneumokokinfektion, stafylokokinfektion og streptokokinfektion"
monitor_inn: "lincomycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia"]
---

# Lincomycin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
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

## Lincomycin: Fra bakterielle infektioner til hyperamylasæmi
{: .text-alpha }

## Resumé i få sætninger

Lincomycin er et lincosamid-antibiotikum, der oprindeligt anvendes til behandling af pneumokok-, stafylokok- og streptokokinfektioner.
TxGNN-modellen forudsiger, at det kan have effekt ved **hyperamylasæmi**,
men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Pneumokokinfektion, stafylokokinfektion og streptokokinfektion (fra videnbasen; godkendte indikationstekster er ikke tilgængelige i de indsamlede data) |
| Forudsagt ny indikation | Hyperamylasæmi |
| TxGNN-prædiktionsscore | 0,9914 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Kun godkendt som veterinærlægemiddel |
| Antal markedsføringstilladelser | 0 (gyldige: 0) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger i de indsamlede data ingen detaljerede oplysninger om virkningsmekanismen. Lincomycin er kendt som et lincosamid-antibiotikum, der hæmmer bakteriel proteinsyntese ved binding til den ribosomale 50S-underenhed. Dets effekt ved bakterielle infektioner er veletableret.

Hyperamylasæmi er imidlertid et laboratoriefund og ikke én enkelt behandlingsbar sygdom. Det kan skyldes bl.a. pancreatitis, sygdom i spytkirtlerne, nedsat nyrefunktion eller makroamylasæmi. Der er ingen kendt biologisk sammenhæng mellem lincomycin og regulering af amylase. En eventuel antibakteriel rolle ville være indirekte, f.eks. ved behandling af en infektiøs årsag som inficeret pancreasnekrose, og udgør ikke en egentlig repurposing-begrundelse.

Den høje score (0,9914) skal derfor tolkes forsigtigt: Den stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Den er en ren modelforudsigelse uden understøttende kliniske data. De to næstrangerende forudsigelser, polyklonalt hyperviskositetssyndrom (score 0,9914) og kongenit analbuminæmi (score 0,9906), har heller ingen plausibel mekanistisk sammenhæng og ingen evidens. Kongenit analbuminæmi skyldes en genetisk defekt i ALB-genet, som et antibiotikum ikke kan korrigere.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ikke registreret relaterede kliniske forsøg.

---

## Litteraturevidens

Der foreligger i øjeblikket ingen relateret litteratur.

---

## Markedsinformation for Danmark

<!-- licenses:begin -->

Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler indeholder ingen markedsføringstilladelser til humane lægemidler med dette aktive stof.

Dataene indeholder 9 tilladelser til veterinærlægemidler (ATC-kode Q eller »Vet.« i navnet).

<!-- licenses:end -->

Alle tilladelser i dataene er veterinærlægemidler; de fleste er kombinationspræparater (lincomycin med spectinomycin eller neomycin). Bemærk, at de angivne præparater er registreret som veterinære lægemidler (dosisformer til dyr), og at godkendte indikationstekster ikke er tilgængelige i de indsamlede data.

<!-- review:begin dk-lic-20261124b-lincomycin-1 -->

> **Rettelse ved gennemgang (2026-11-24)**: Oprindeligt stod der: "Alle fem tilladelser er enkeltstofpræparater med status gyldig." Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler (data fra 2026-11-05): Ifølge feltet AktiveSubstanser er de fleste veterinære produkter med lincomycin kombinationspræparater, og der er flere end fem. Markedsstatus og antallet af veterinære tilladelser vedligeholdes af programmet i Hurtigt overblik og under markedsinformationen. Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261124b-lincomycin-1 -->

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra videnbasen** (afledt af videngraf, ikke produktresumétekst): leversvigt, Clostridioides difficile-colitis, perinatal nekrotiserende enterokolitis, colitis, sygdomme i fordøjelsessystemet og tarmsygdomme.
- **Lægemiddelinteraktioner**: Der er identificeret 26 potentielle interaktioner. De af moderat sværhedsgrad omfatter balsalazid, picosulfat, attapulgit, kaolin og erythromycin. Øvrige registrerede interaktioner er uden klassificeret sværhedsgrad, bl.a. warfarin, metformin, simvastatin, morphin, lidocain, omeprazol, cimetidin og ranitidin.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5) uden kliniske forsøg eller publikationer og uden plausibel mekanistisk sammenhæng mellem lincomycin og hyperamylasæmi. De registrerede danske tilladelser er desuden til veterinær anvendelse.

**For at komme videre kræves følgende:**
- Detaljerede data om virkningsmekanisme (MOA)
- Produktresumé med advarsler og kontraindikationer for humane præparater
- Præklinisk eller mekanistisk dokumentation for en sammenhæng med amylaseregulering
- Afklaring af, om der findes humane lincomycin-præparater på det danske marked

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-24 | Alle fem tilladelser er enkeltstofpræparater med status gyldig. | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

