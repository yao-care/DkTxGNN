---
layout: default
title: Ceftolozane
parent: Kun modelforudsigelse (L5)
nav_order: 172
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Ceftolozane: forudsagt ny indikation Ureaplasma-uretritis (evidensniveau L5). Oprindelig indikation: Urinvejsinfektion"
monitor_inn: "ceftolozane"
predicted_indications: ["Ureaplasma urethritis", "gonococcal urethritis", "uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "polyclonal hyperviscosity syndrome", "hyperamylasemia", "urogenital tuberculosis", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease"]
---

# Ceftolozane
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

# Ceftolozan: Fra urinvejsinfektion til Ureaplasma-uretritis

## Resumé i en sætning

Ceftolozan er et cefalosporin-antibiotikum (beta-lactam), som oprindeligt anvendes til behandling af urinvejsinfektion.
TxGNN-modellen forudsiger, at det kan være virksomt mod **Ureaplasma-uretritis**,
men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning. Forudsigelsen bygger udelukkende på modellen, og den biologiske sandsynlighed vurderes som lav.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Urinvejsinfektion (godkendt indikationstekst er ikke angivet i de indsamlede data for den danske tilladelse) |
| Forudsagt ny indikation | Ureaplasma-uretritis |
| TxGNN-forudsigelsesscore | 99,89 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til denne rapport. Ceftolozan er et beta-lactam-cefalosporin med aktivitet primært mod gramnegative bakterier, især *Pseudomonas aeruginosa*. Dets virkning ved urinvejsinfektion er kendt, og det er sammen med tazobactam godkendt til komplicerede urinvejsinfektioner.

Forudsigelsen er dog mekanistisk usandsynlig. *Ureaplasma* mangler cellevæg, og beta-lactamer, som hæmmer cellevægssyntesen, er derfor i sagens natur uvirksomme mod organismen. Den høje modelscore skyldes sandsynligvis en grafbaseret artefakt, drevet af den fælles tilknytning til urogenitale infektioner.

**Øvrige forudsagte indikationer (rangeret 2-10)** har alle evidensniveau L4-L5 og anbefalingen Hold:

| Rang | Forudsagt indikation | Score | Vurdering |
|---|---|---|---|
| 2 | Gonokok-uretritis | 99,89 % | Cefalosporiner som klasse er etableret behandling, men ceftolozan er optimeret til *Pseudomonas* og Enterobacterales, kun intravenøst, og der er ingen data for *N. gonorrhoeae*. Veletablerede alternativer findes. |
| 3 | Inflammatorisk sygdom i uterus | 99,88 % | Infektionerne er ofte polymikrobielle; begrænset anaerob og ingen atypisk dækning. Kun svagt indirekte grundlag. |
| 4 | Xantogranulomatøs pyelonefritis | 99,88 % | Indirekte sandsynlighed via godkendelsen til kompliceret urinvejsinfektion og pyelonefritis, men behandlingen er oftest kirurgisk (nefrektomi). |
| 5 | Polyklonalt hyperviskositetssyndrom | 99,52 % | Ingen plausibel antibakteriel mekanisme; sandsynligvis artefakt. |
| 6 | Hyperamylasæmi | 99,52 % | Laboratoriefund, ikke en infektion; sandsynligvis artefakt. |
| 7 | Urogenital tuberkulose | 99,50 % | *M. tuberculosis* er iboende resistent over for de fleste beta-lactamer (BlaC). |
| 8 | Medfødt analbuminæmi | 99,44 % | Ingen antibakteriel målstruktur; sandsynligvis artefakt. |
| 9 | Blodtypeinkompatibilitet | 99,22 % | Ingen plausibel mekanisme; cefalosporiner kan selv give immunmedieret hæmolyse. |
| 10 | Præmaligne hæmatologiske sygdomme | 99,11 % | Ingen mekanisme; sandsynligvis grafartefakt. |

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105499514 | Zerbaxa (Merck Sharp & Dohme B.V.) | Pulver til koncentrat til infusionsvæske, opløsning | Indikationstekst ikke angivet i de indsamlede data |

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (14 registrerede interaktioner, alle af moderat sværhedsgrad):
- **Aminoglykosider:** kanamycin, neomycin, streptomycin, amikacin (inkl. liposomal) og gentamicin
- **Antikoagulantia:** warfarin og dicoumarol
- **Andre:** chloramphenicol, ethinylestradiol og mycophenolsyre

Der foreligger ikke data om advarsler og kontraindikationer i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er alene modelbaseret (L5) uden kliniske forsøg eller litteratur, og virkningsmekanismen er biologisk usandsynlig, da *Ureaplasma* mangler cellevæg. Ingen af de ti forudsagte indikationer har tilstrækkelig støtte til at komme videre.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé for Zerbaxa fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikation), da manglen på disse data blokerer sikkerhedsscreeningen
- In vitro-følsomhedsdata og, hvis relevant, kliniske data for de mest plausible kandidater (f.eks. xantogranulomatøs pyelonefritis og gonokok-uretritis)
- Afklaring af administrationsvej og kompatibilitet (ceftolozan findes kun som intravenøs infusion)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

