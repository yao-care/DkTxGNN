---
layout: default
title: Posaconazole
parent: Kun modelforudsigelse (L5)
nav_order: 673
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
monitor_inn: "posaconazole"
predicted_indications: ["pneumocystosis"]
description: "Posaconazole: forudsagt ny indikation Pneumocystose (pneumocystosis) (evidensniveau L5). I Danmark, markedsføringstilladelser: 13 (gyldige: 13)"
---

# Posaconazole
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **1** stk.
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

## Posaconazole: Pneumocystose (pneumocystosis)
{: .text-alpha }

## Resumé i én sætning

Posaconazol er et azol-antimykotikum, der oprindeligt anvendes til behandling og forebyggelse af svampeinfektioner som aspergillose, candidiasis og histoplasmose.
TxGNN-modellen forudsiger, at det kan have effekt mod **pneumocystose**, men der er **ingen direkte kliniske data** for posaconazol på denne indikation (1 registreret forsøg, som ikke undersøger posaconazol, og 5 oversigts- eller kohortepublikationer uden direkte evidens).
Forudsigelsen bygger primært på lægemiddelklassen og vurderes som mekanistisk tvivlsom.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Pneumocystose (pneumocystosis) |
| TxGNN-forudsigelsesscore | 0.9977 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 13 af 13) |
| Antal markedsføringstilladelser | 13 (gyldige: 13) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Posaconazol hæmmer svampeenzymet lanosterol-14-alfa-demethylase (CYP51) og blokerer dermed syntesen af ergosterol, en vigtig bestanddel af svampes cellemembran. Ifølge afsnittene »Mechanism of Action« og »Microbiology« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Posaconazole (uofficiel oversættelse): »Posaconazol er et azolsvampemiddel. […] Posaconazol blokerer syntesen af ergosterol, en vigtig bestanddel af svampecellemembranen, ved at hæmme det cytochrom P-450-afhængige enzym lanosterol-14α-demethylase, som er ansvarligt for omdannelsen af lanosterol til ergosterol i svampecellemembranen. Dette medfører en ophobning af methylerede sterolprækursorer og en udtømning af ergosterol i cellemembranen, hvorved svampecellemembranens struktur og funktion svækkes.« Engelsk originaltekst: "Posaconazole is an azole antifungal agent. […] Posaconazole blocks the synthesis of ergosterol, a key component of the fungal cell membrane, through the inhibition of cytochrome P-450 dependent enzyme lanosterol 14α-demethylase responsible for the conversion of lanosterol to ergosterol in the fungal cell membrane. This results in an accumulation of methylated sterol precursors and a depletion of ergosterol within the cell membrane thus weakening the structure and function of the fungal cell membrane." ([DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84), version af 2026-02-13; hentet 2026-11-19).

*Pneumocystis jirovecii* har i modsætning til de fleste svampe ikke ergosterol i sin cellemembran, men anvender primært kolesterol. Azolers virkningsmekanisme er derfor ikke mekanistisk plausibel mod denne organisme. Den høje TxGNN-score skyldes sandsynligvis lægemidlets brede tilknytning til antimykotika som klasse og ikke en reel mekanistisk sammenhæng.

Selvom de oprindelige indikationer (fx aspergillose og candidiasis) og pneumocystose alle er opportunistiske svampeinfektioner hos immunsvækkede patienter, er der i de foreliggende data hverken kliniske eller prækliniske tegn på, at posaconazol virker mod Pneumocystis.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT04368559](https://clinicaltrials.gov/study/NCT04368559) | Fase 3 | Afsluttet | 602 | ReSPECT-studiet: intravenøs rezafungin versus standardregime til forebyggelse af invasive svampeinfektioner efter allogen knoglemarvstransplantation. Posaconazol er ikke studielægemidlet, og forsøget giver ingen direkte evidens for posaconazol ved pneumocystose. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [26901377](https://pubmed.ncbi.nlm.nih.gov/26901377/) | 2016 | Oversigtsartikel | Swiss Medical Weekly | Overblik over invasiv candidiasis, aspergillose, kryptokokkose og Pneumocystis-pneumoni; nævner, at profylakse med skimmelaktivt posaconazol har reduceret invasive svampeinfektioner hos højrisiko hæmato-onkologiske patienter |
| [41232547](https://pubmed.ncbi.nlm.nih.gov/41232547/) | 2026 | Oversigtsartikel | The Lancet Infectious Diseases | Opdaterede britiske anbefalinger til diagnostik af alvorlige svampeinfektioner |
| [41362140](https://pubmed.ncbi.nlm.nih.gov/41362140/) | 2025 | Oversigtsartikel (retningslinje) | Chinese Journal of Tuberculosis and Respiratory Diseases | Kinesiske retningslinjer for diagnostik og behandling af invasive lungesvampeinfektioner |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Oversigtsartikel | Clinical Pharmacokinetics | Gennemgang af antimykotikas penetration til lungernes epitelvæske |
| [35596686](https://pubmed.ncbi.nlm.nih.gov/35596686/) | 2022 | Kohortestudie | Transplant Infectious Disease | Infektiøse komplikationer ved akut graft-versus-host-sygdom efter levertransplantation |

Ingen af publikationerne viser direkte, at posaconazol er effektivt mod pneumocystose.

---

## Information om markedet i Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106510720 | Noxafil | enteropulver og solvens til oral suspension | POSACONAZOL | Gyldig |
| 28105258513 | Noxafil | enterotabletter | POSACONAZOL | Gyldig |
| 28105320313 | Noxafil | koncentrat til infusionsvæske, opløsning | POSACONAZOL | Gyldig |
| 28103701404 | Noxafil | oral suspension | POSACONAZOL | Gyldig |
| 28106133018 | Posaconazol "Teva B.V." | oral suspension | POSACONAZOL | Gyldig |

Tabellen viser 5 af 13 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

Dataene indeholder desuden 2 tilladelser til veterinærlægemidler (ATC-kode Q eller »Vet.« i navnet), som ikke er medtaget i tabellen eller i antallet ovenfor.

<!-- licenses:end -->

---

## Sikkerhedsmæssige overvejelser

Der foreligger ikke data om advarsler og kontraindikationer i de indsamlede data. Se det godkendte produktresumé (SmPC) for sikkerhedsinformation.

**Lægemiddelinteraktioner:** Der er registreret 327 interaktioner. Blandt de første 20 er følgende klassificeret som **alvorlige (Major)**:
- Loperamid
- Triamcinolon
- Budesonid

Eksempler på **moderate** interaktioner:
- Syrehæmmere: famotidin, ranitidin, rabeprazol, omeprazol, cimetidin
- Kortikosteroider: hydrocortison, dexamethason, betamethason
- Øvrige: aprepitant, clarithromycin, saxagliptin, bisacodyl, picosulfat, polyethylenglycol

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler alene på modellen (evidensniveau L4). Det eneste identificerede forsøg undersøger et andet lægemiddel, og Pneumocystis mangler ergosterol, hvilket gør azolers virkningsmekanisme usandsynlig. Den høje score afspejler formentlig klassetilknytning.

**For at komme videre kræves:**
- Prækliniske eller kliniske data, der viser aktivitet af posaconazol mod *Pneumocystis jirovecii*
- Data om virkningsmekanisme fra DrugBank
- Gennemgang af produktresumé (SmPC) for advarsler og kontraindikationer, da disse mangler i de indsamlede data
- Vurdering af administrationsvej og relevant formulering til lungeinfektion
- Sammenligning med etableret behandling og profylakse af pneumocystose (fx trimethoprim-sulfamethoxazol)

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Noxafil (posaconazole) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=b073b082-7b57-4423-8c06-4fd4263d6f84) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

