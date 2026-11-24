---
layout: default
title: Lanadelumab
parent: Kun modelforudsigelse (L5)
nav_order: 477
evidence_level: L5
indication_count: 9
monitor_inn: "Lanadelumab"
predicted_indications: ["serpinopathy with toxic serpin polymerization", "pancreatitis", "pseudo-von Willebrand disease", "primary release disorder of platelets", "immune-mediated necrotizing myopathy", "Glanzmann thrombasthenia", "antisynthetase syndrome", "focal myositis", "Scott syndrome"]
last_modified_at: 2026-11-24
description: "Lanadelumab: forudsagt ny indikation Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) (evidensniveau L5)."
---

# Lanadelumab
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

## Lanadelumab: Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)
{: .text-alpha }

## Resumé i én sætning

Lanadelumab er et monoklonalt antistof, der hæmmer plasmakallikrein. Lægemidlet er i forvejen markedsført i Danmark. TxGNN-modellen forudsiger, at det kan have effekt ved **serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization)**, men der er **ingen kliniske forsøg** og **ingen publikationer**, der understøtter denne forudsigelse.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Serpinopati med toksisk serpinpolymerisering (serpinopathy with toxic serpin polymerization) |
| TxGNN-forudsigelsesscore | 0.9999 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 4 af 4) |
| Antal markedsføringstilladelser | 4 (gyldige: 4) |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Lanadelumab (uofficiel oversættelse): »Lanadelumab-flyo er et fuldt humant monoklonalt antistof (IgG1/κ-let kæde), der binder plasmakallikrein og hæmmer dets proteolytiske aktivitet. Plasmakallikrein er en protease, der spalter højmolekylært kininogen (HMWK) under dannelse af spaltet HMWK (cHMWK) og bradykinin, en potent vasodilatator, der øger den vaskulære permeabilitet, hvilket resulterer i hævelse og smerter forbundet med HAE.« Engelsk originaltekst: "Lanadelumab-flyo is a fully human monoclonal antibody (IgG1/κ-light chain) that binds plasma kallikrein and inhibits its proteolytic activity. Plasma kallikrein is a protease that cleaves high-molecular-weight-kininogen (HMWK) to generate cleaved HMWK (cHMWK) and bradykinin, a potent vasodilator that increases vascular permeability resulting in swelling and pain associated with HAE." ([DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8), version af 2026-09-18; hentet 2026-11-19). Lanadelumab er kendt som en hæmmer af plasmakallikrein (målprotein: KLKB1), og det virker dermed på kallikrein-bradykinin-systemet.

Der er ikke påvist nogen direkte mekanistisk sammenhæng mellem lanadelumabs virkning og den forudsagte sygdom. Forudsigelsen skyldes sandsynligvis nærhed mellem relaterede proteiner i modellens netværk, især SERPING1 (C1-hæmmer) og andre serpinsygdomme. Lanadelumab hæmmer plasmakallikrein og påvirker ikke ophobning af toksiske serpinpolymerer. Forudsigelsen bør derfor betragtes som et hypotesegenererende modelresultat og ikke som en biologisk begrundet anbefaling.

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

## Markedsinformation i Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106091818 | TAKHZYRO | injektionsvæske, opløsning, hætteglas | Lanadelumab | Gyldig |
| 28106873022 | TAKHZYRO | injektionsvæske, opløsning i fyldt injektionssprøjte | Lanadelumab | Gyldig |
| 28106517319 | TAKHZYRO | injektionsvæske, opløsning i fyldt injektionssprøjte | Lanadelumab | Gyldig |
| 28107307324 | TAKHZYRO | injektionsvæske, opløsning i fyldt pen | Lanadelumab | Gyldig |

Tabellen viser alle 4 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er registreret én farmakologisk relation til målproteinet kallikrein B1 (KLKB1), som er lanadelumabs målmolekyle. Det er en målbeskrivelse og ikke en klinisk interaktion med et andet lægemiddel.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er alene modelbaseret (evidensniveau L5), uden kliniske forsøg eller litteratur og uden en plausibel mekanistisk forbindelse mellem plasmakallikrein-hæmning og toksisk serpinpolymerisering.

**For at komme videre kræves følgende:**
- En biologisk begrundet hypotese for, hvordan hæmning af plasmakallikrein kunne påvirke serpinpolymerisering
- Præklinisk evidens (celle- eller dyremodeller) for den forudsagte sygdom
- Detaljerede data om virkningsmekanisme og produktresumé med advarsler og kontraindikationer til en sikkerhedsvurdering

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Takhzyro (lanadelumab-flyo) prescribing information, Takeda Pharmaceuticals America, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=15f99d8c-efe7-4f7d-aa20-0d0f1e30c6e8) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

