---
layout: default
title: Ezetimibe
parent: Kun modelforudsigelse (L5)
nav_order: 344
evidence_level: L5
indication_count: 1
monitor_inn: "ezetimibe"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-23
description: "Ezetimibe: forudsagt ny indikation Kolesterolester-transferprotein-mangel (evidensniveau L5). Oprindelig indikation: Hyperlipidæmi og beslægtede lidelser"
---

# Ezetimibe
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

## Ezetimib: Fra hyperlipidæmi til kolesterolester-transferprotein-mangel
{: .text-alpha }

## Resumé i én sætning

Ezetimib er et kolesterolsænkende lægemiddel, der er knyttet til hyperlipidæmi, familiær hyperkolesterolæmi og sitosterolæmi.
TxGNN-modellen forudsiger, at det kan have effekt ved **kolesterolester-transferprotein-mangel (CETP-mangel)**.
Der er dog **ingen kliniske forsøg** og **ingen publikationer, der direkte undersøger denne sygdom**, så forudsigelsen hviler alene på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hyperlipidæmi og beslægtede lidelser (relationer registreret i vidensgrafen; godkendelsesteksten i de danske tilladelser er ikke tilgængelig) |
| Forudsagt ny indikation | Kolesterolester-transferprotein-mangel |
| TxGNN-forudsigelsesscore | 0,9909 |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ikke detaljerede data om virkningsmekanismen i de data, der er sammenstillet til denne rapport. Ezetimib er kendt som en hæmmer af optagelsen af kolesterol i tarmen (via NPC1L1) og sænker dermed LDL-kolesterol. Dette er baseret på almen farmakologisk viden og ikke på de sammenstillede data.

CETP-mangel er en genetisk tilstand med forhøjet HDL-kolesterol og nedsat overførsel af kolesterolestere mellem lipoproteiner. Et muligt link er, at begge forhold vedrører kolesterolets samlede fordeling mellem lipoproteiner. Der findes dog ingen direkte mekanistiske eller kliniske data, der forbinder ezetimib med CETP-mangel.

Den høje score (0,9909) kommer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens eller påvist gavnlig effekt. CETP-mangel er desuden ofte symptomfri eller ledsaget af højt HDL-kolesterol, så det er uklart, om der overhovedet er et behandlingsbehov.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Ingen af de fundne publikationer undersøger direkte ezetimib ved CETP-mangel. De er kun tangentielt relateret til lipidstofskifte.

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [40911366](https://pubmed.ncbi.nlm.nih.gov/40911366/) | 2025 | Oversigtsartikel | European Heart Journal | Gennemgang af nye mål for lipidsænkning (LDL-C, triglycerider, apoB, Lp(a)) og de nuværende lipidsænkende lægemidlers mekanismer |
| [31779098](https://pubmed.ncbi.nlm.nih.gov/31779098/) | 2019 | Dyrestudie | Int J Mol Sci | Hamstermodel med Ldlr-mangel anvendt til at evaluere et PCSK9-antistof ved hyperlipidæmi og aterosklerose; omhandler ikke ezetimib |

---

## Information om det danske marked

Godkendelsesteksten for indikationerne er ikke angivet i de tilgængelige data.

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105500214 | Carditimib | Tabletter | Ikke angivet |
| 28106230919 | Nustendi | Filmovertrukne tabletter | Ikke angivet |
| 28106300219 | Ezetimibe/Simvastatin "Accord" | Tabletter | Ikke angivet |

Bemærk: Nustendi og Ezetimibe/Simvastatin "Accord" er i praksis kombinationspræparater, selvom de er registreret som enkeltstofpræparater i datagrundlaget. Deres tilladelser siger derfor ikke noget om, hvordan ezetimib som enkeltstof er godkendt.

---

## Sikkerhedsmæssige overvejelser

Der foreligger ingen oplysninger fra produktresuméer. Vidensgrafen indeholder dog følgende registrerede kontraindikationsrelationer (ikke mærkningstekst): pancreatitis, leversygdom, galdeblæresygdom, myopati, muskelsygdomme, skeletmuskelsygdom, familiær periodisk paralyse, misbrug/afhængighed, rabdomyolyse og nodulær fasciitis.

**Lægemiddelinteraktioner:** 209 interaktioner er registreret. Blandt de som er klassificeret som moderate er:
- Chenodeoxycholsyre
- Eluxadolin
- Rosuvastatin
- Simvastatin

Flere andre (fx pantoprazol, metformin, omeprazol, doxycyclin, morfin) er registreret med ukendt alvorlighedsgrad.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen understøttes kun af modellen (evidensniveau L5). Der findes ingen kliniske forsøg eller publikationer, der direkte omhandler ezetimib ved CETP-mangel, og det er uklart, om der er et klinisk behandlingsbehov.

**For at komme videre kræves:**
- Data om virkningsmekanisme og en mekanistisk begrundelse for effekt ved CETP-mangel
- Dokumentation for et klinisk behandlingsbehov ved CETP-mangel
- Præklinisk eller klinisk evidens, der direkte undersøger ezetimib ved denne tilstand
- Indhentning af produktresuméer fra Lægemiddelstyrelsen (advarsler, kontraindikationer, godkendte indikationer)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

