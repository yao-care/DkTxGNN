---
layout: default
title: Milrinone
parent: Kun modelforudsigelse (L5)
nav_order: 557
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-14
description: "Milrinone: forudsagt ny indikation Alopeci (evidensniveau L5). Oprindelig indikation: Ikke angivet i den danske registrering. Litteraturen beskriver intrav…"
monitor_inn: "milrinone"
predicted_indications: ["alopecia", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "headache disorder", "migraine disorder", "migraine with brainstem aura", "trigeminal autonomic cephalalgia", "acute pulmonary heart disease"]
---

# Milrinone
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

## Milrinon: Fra hjertesvigt til alopeci
{: .text-alpha }

## Resumé

Milrinon er en PDE3-hæmmer, der gives som infusion og bruges til hjertesvigt (indikationsteksten i den danske registrering er ikke angivet i de indsamlede data). TxGNN-modellen forudsiger, at det kan have effekt ved **alopeci** (hårtab). Forudsigelsen står alene: der er **0 kliniske forsøg** og **0 publikationer** for denne indikation.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske registrering. Litteraturen beskriver intravenøs milrinon til kortvarig behandling af hjertesvigt |
| Forudsagt ny indikation | Alopeci |
| TxGNN-forudsigelsesscore | 0,9991 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

## Hvorfor kan forudsigelsen være rimelig?

Detaljerede data om virkningsmekanismen foreligger ikke i de indsamlede data. Milrinon er kendt som PDE3-hæmmer. Det øger cAMP og giver både øget hjertekontraktilitet og karudvidelse (en "inodilator"-effekt).

Der er kun et spekulativt link til alopeci: cAMP-signalering eller bedre perfusion omkring hårfollikler. Ingen undersøgelser understøtter dette. Ved autoimmun alopecia areata er PDE4-hæmmere den mere relevante klasse, og PDE3-hæmning med milrinon har ingen påvist rolle. Den høje score kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke egentlig biologisk evidens.

De øvrige forudsigelser med høj score for milrinon (hårtabsdiagnoser som hypotrichosis simplex of the scalp, congenital hypotrichosis milia og diffuse alopecia areata) er ligeledes uden kliniske data.

## Klinisk evidens (forsøg)

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for alopeci.

## Litteraturevidens

Der foreligger i øjeblikket ingen relateret litteratur for alopeci.

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105826516 | Milnocor (Macure Pharma ApS) | Injektions-/infusionsvæske, opløsning | Ikke angivet i de indsamlede data |

Der er kun én gyldig tilladelse (monopræparat). Den foreligger udelukkende som injicerbar form, hvilket ikke uden videre passer til en indikation som hårtab, hvor lokal eller oral behandling ville være mere sandsynlig.

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

- **Mulige kontraindikationer ifølge vidensgrafen** (afledt af relationer mellem lægemiddel og sygdom i TxGNN/PrimeKG, ikke af produktresuméets tekst): nyresygdom, hypotension, myokardieinfarkt og koronar trombose, hæmoglobinopati, hjertestop, hjerteledningsforstyrrelser, pulmonal klapstenose og hypertrofisk kardiomyopati (herunder familiær).
- **Lægemiddelinteraktioner** (5 fundet, alle af moderat sværhedsgrad): amifostin, diatrizoat, anagrelid, ozanimod og procarbazin.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om alopeci er alene baseret på en modelscore, uden kliniske forsøg, litteratur eller en plausibel mekanistisk forklaring. Milrinon er desuden kun markedsført som infusion med betydelige hjerte-kar-forbehold.

**For at komme videre kræves:**
- Præklinisk eller mekanistisk evidens for, at PDE3-hæmning påvirker hårfollikler eller hårcyklus
- Afklaring af en egnet administrationsvej (fx lokal behandling) og tilhørende sikkerhedsprofil
- Gennemgang af det danske produktresumé for advarsler og kontraindikationer
- Detaljerede data om virkningsmekanismen

**Bemærkning:** Andre forudsigelser for milrinon har væsentligt mere evidens, men er i praksis etableret eller nært beslægtet med eksisterende brug. For kongestiv hjerteinsufficiens (evidensniveau L2, "Proceed with Guardrails") og akut pulmonal hjertesygdom (L1, bør tolkes forsigtigt, da det eneste forsøg omfatter en blandet kritisk syg population) kunne en særskilt vurdering være mere relevant. Headache disorder (L4, kun case reports om reversibelt cerebralt vasokonstriktionssyndrom) er en forskningsmæssig problemstilling.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

