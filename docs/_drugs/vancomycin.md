---
layout: default
title: Vancomycin
parent: Kun modelforudsigelse (L5)
nav_order: 875
evidence_level: L5
indication_count: 10
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
last_modified_at: 2026-11-24
description: "Vancomycin: forudsagt ny indikation Diffus sklerodermi (evidensniveau L5). Oprindelig indikation: Clostridium difficile-colitis"
---

# Vancomycin
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

## Vancomycin: Fra Clostridium difficile-colitis til diffus sklerodermi
{: .text-alpha }

## Opsummering

Vancomycin er et glykopeptid-antibiotikum, der oprindeligt bruges mod grampositive bakterielle infektioner, bl.a. Clostridium difficile-colitis, stafylokokinfektioner og endokarditis (relationer registreret i vidensgrafen).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt mod **diffus sklerodermi**, men der er **ingen kliniske forsøg** og kun **1 publikation** (en case-rapport om erytrodermi, som ikke handler om behandling af sklerodermi).
Forudsigelsen vurderes som en grafbaseret artefakt uden biologisk grundlag.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Clostridium difficile-colitis (relation registreret i vidensgrafen; godkendelsesteksten i den danske registrering er ikke angivet) |
| Forudsagt ny indikation | Diffus sklerodermi |
| TxGNN-forudsigelsesscore | 0,9992 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: mindst 20) |
| Antal markedsføringstilladelser | mindst 20 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge afsnittene »Mechanism of Action« og »Microbiology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Vancomycin (uofficiel oversættelse): »Vancomycin er et antibakterielt lægemiddel. […] Den baktericide virkning af vancomycin skyldes primært hæmning af cellevægsbiosyntesen. Desuden ændrer vancomycin bakteriecellemembranens permeabilitet og RNA-syntesen.« Engelsk originaltekst: "Vancomycin is an antibacterial drug. […] The bactericidal action of vancomycin results primarily from inhibition of cell-wall biosynthesis. In addition, vancomycin alters bacterial-cell-membrane permeability and RNA synthesis." ([DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560), version af 2026-08-19; hentet 2026-11-19). Det er kendt, at vancomycin er et glykopeptid, der virker mod grampositive bakterier ved at hæmme cellevægssyntesen.

Diffus sklerodermi (systemisk sklerose) er en autoimmun, fibrotisk sygdom. Der findes ingen plausibel antibakteriel mekanisme, som forbinder vancomycin med denne sygdom. Den høje score stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke biologisk evidens.

Den eneste tilknyttede publikation beskriver et tilfælde af eksfoliativt udslæt (erytrodermi) med sepsis og eosinofili og undersøger ikke behandling af sklerodermi.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case-rapport | The American Journal of Case Reports | Patient med diffust eksfoliativt udslæt, sepsis og eosinofili (erytrodermi); handler ikke om behandling af sklerodermi |

---

## Markedsinformation for Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28104655310 | Bactocin | pulver til infusionsvæske, opløsning | VANCOMYCINHYDROCHLORID | Gyldig |
| 28104655210 | Bactocin | pulver til infusionsvæske, opløsning | VANCOMYCINHYDROCHLORID | Gyldig |
| 28103008798 | Vancocin | kapsler, hårde | VANCOMYCIN | Gyldig |
| 28101207685 | Vancocin | kapsler, hårde | VANCOMYCINHYDROCHLORID | Gyldig |
| 28104526009 | Vancomycin "Fresenius Kabi" | pulver til koncentrat til infusionsvæske, opløsning | VANCOMYCINHYDROCHLORID | Gyldig |

Tabellen viser 5 af mindst 20 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først. Dataene i denne rapport omfatter kun en del af tilladelserne.

<!-- licenses:end -->

Der er mindst 20 nationale tilladelser (enkeltstofpræparater, gyldige). Producent: Strides Pharma (Cyprus) Limited.

<!-- review:begin dk-lic-20261112-vancomycin-1 -->

> **Rettelse ved gennemgang (2026-11-12)**: Oprindeligt stod der: "Der er 1 national tilladelse (enkeltstofpræparat, gyldig)." Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler: der er mindst 20 (dataene er delvise) tilladelser for dette lægemiddel (heraf 20 enkeltstofpræparater i dataene); det tidligere antal kom fra en ældre version af dataene. De aktuelle tal står i hurtigt overblik. Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261112-vancomycin-1 -->

---

## Sikkerhedsovervejelser

- **Kontraindikationer/risikorelationer i vidensgrafen** (ikke fra produktresuméet): nyresygdom, pyoureter, neutropeni, agranulocytose, hørenedsættelse og sygdomme i høresystemet.
- **Lægemiddelinteraktioner**: 100 interaktioner er identificeret. Eksempler på **alvorlige** (Major): intravenøst humant immunglobulin G, humant botulisme-immunglobulin (A/B) og levende kolera-vaccine (CVD 103-HgR). Eksempler på **moderate**: ketorolac, ibuprofen, diclofenac, celecoxib, metformin, amphotericin B, amikacin, bacitracin, capreomycin, carboplatin, cholestyramin, mesalazin og ibandronat.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der er ingen kliniske forsøg og ingen litteratur, der direkte undersøger vancomycin ved diffus sklerodermi, og der er ingen plausibel mekanisme. Evidensniveauet er L5 (kun modelforudsigelse).

**For at komme videre kræves:**
- Et biologisk rationale for en effekt i sklerodermi, og data om virkningsmekanisme
- Prækliniske data, der direkte undersøger sygdommen
- Produktresuméets advarsler og kontraindikationer, som mangler i de indsamlede data

**Bemærkning om øvrige forudsigelser:** De øvrige forudsigelser i listen (bl.a. paratyfus, salmonellose, tyfus, medfødt analbuminæmi, hyperamylasæmi, polyklonalt hyperviskositetssyndrom, blodtypeinkompatibilitet og præmaligne hæmatologiske sygdomme) er alle vurderet som L5 med anbefalingen Hold. For gramnegative Salmonella-arter er vancomycin ikke virksomt, da stoffet ikke kan trænge gennem den ydre membran. Streptokokpneumoni har en biologisk plausibel mekanisme, men evidensen er indirekte (retningslinjer, overvågnings- og resistensstudier), og der findes en rapport om vancomycin-tolerante pneumokokker; betalaktamer er fortsat førstevalg. Der er ingen studier, der direkte viser effekt af vancomycin ved disse tilstande i de indsamlede data.

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse).

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-12 | Antal tilladelser: “Der er 1 national tilladelse (enkeltstofpræparat, gyldig).” → “Der er mindst 20 nationale tilladelser (enkeltstofpræparater, gyldige).” | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Tyzavan (vancomycin) prescribing information, Hikma Pharmaceuticals USA Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=72e9c5e2-07cc-4a8b-ba64-b2e7619ea560) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

