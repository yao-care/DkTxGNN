---
layout: default
title: Ertapenem
parent: Kun modelforudsigelse (L5)
nav_order: 323
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
monitor_inn: "Ertapenem"
predicted_indications: ["bacterial arthritis", "staphylococcus aureus infection"]
description: "Ertapenem: forudsagt ny indikation Bacterial arthritis (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Ertapenem
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Ertapenem: Bacterial arthritis
{: .text-alpha }

## Resumé i én sætning

Ertapenem er et bredspektret carbapenem-antibiotikum, der oprindeligt anvendes til bakteriel lungebetændelse (herunder streptokok-pneumoni) og infektioner med Peptostreptococcus.
TxGNN-modellen forudsiger, at det kan være effektivt mod **Staphylococcus aureus-infektion**, især som kombinationsbehandling med cefazolin ved vedvarende MSSA-bakteriæmi.
Evidensen består af **2 kliniske forsøg** (begge igangværende, uden resultater) og **20 publikationer**, hovedsageligt case-serier og kohortestudier.

Denne rapport fokuserer på Staphylococcus aureus-infektion, som har den stærkeste evidens blandt forudsigelserne (L2).*

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Bacterial arthritis |
| TxGNN-forudsigelsesscore | 0.9972 |
| Evidensniveau | L5 (jf. klassificering i de kompilerede data; ingen afsluttede RCT'er, evidensen er case-serier, kohorter og to igangværende forsøg) |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Proceed with Guardrails |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om ertapenems oprindelige virkningsmekanisme er ikke tilgængelige i de kompilerede data. Ertapenem er et carbapenem, som hæmmer bakteriens cellevægssyntese ved at binde til penicillinbindende proteiner (PBP), primært PBP 2 og 3. Det har bredt spektrum mod Enterobacterales (inkl. ESBL-producenter) og anaerobe bakterier.

Ertapenem anvendes normalt ikke som monoterapi mod S. aureus. I kombination med cefazolin ses der imidlertid synergi mod methicillin-følsom S. aureus (MSSA). Den foreslåede mekanisme er, at de to betalaktamer mætter komplementære PBP'er (bl.a. PBP1), hvilket øger den baktericide effekt og kan rydde vedvarende bakteriæmi. Det er en udvidelse af den antibakterielle anvendelse snarere end en ny virkningsmekanisme.

Synergien er understøttet af dyremodeller (rotte-endokarditis, muse-hudinfektion), case-serier og kohortestudier. Ertapenem er stærkt proteinbundet, og hypoalbuminæmi kan give suboptimal eksponering.

---

## Klinisk forsøgsevidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Fase 2 | Rekrutterer | 60 | Cefazolin + ertapenem ved MSSA-bakteriæmi; delstudie af SNAP-platformsforsøget. Første randomiserede forsøg; ingen resultater endnu. Forventet afslutning 2027-07 |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Fase 4 | Inviterede deltagere | 300 | Åbent, pragmatisk RCT af tidlig dobbeltbehandling vs. enkeltstof IV ved S. aureus-bakteriæmi. Uklart om ertapenem er nøglestoffet; ingen resultater endnu |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Case-serie/kohorte | Clin Infect Dis | Cefazolin + ertapenem som redningsbehandling i 11 tilfælde af vedvarende MSSA-bakteriæmi (6 med endokarditis); 8 med clearance inden for 24 timer |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Case-serie/in vitro | Antimicrob Agents Chemother | Synergi mellem cefazolin og ertapenem in vitro og i musemodel; vedvarende bakteriæmi ryddet |
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Komparativ kohorte | J Antimicrob Chemother | Carbapenem-kombination vs. standardbehandling ved vedvarende MSSA-bakteriæmi |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Kohorte | J Antimicrob Chemother | Betydning af hypoalbuminæmi ved ertapenem-kombinationsbehandling af MSSA-bakteriæmi |
| [41759962](https://pubmed.ncbi.nlm.nih.gov/41759962/) | 2026 | Multicenter case-serie | Infect Dis Now | Ertapenem + penicillin M eller cefazolin ved kompliceret S. aureus-bakteriæmi i klinisk praksis |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Review | Am J Health Syst Pharm | Kombinationsbehandlingsmuligheder ved vedvarende MSSA-bakteriæmi |
| [34599521](https://pubmed.ncbi.nlm.nih.gov/34599521/) | 2021 | Case-serie | J Card Surg | Cefazolin + ertapenem som redningsbehandling ved refraktær LVAD-infektion |
| [39935929](https://pubmed.ncbi.nlm.nih.gov/39935929/) | 2025 | Case-rapport | Cureus | Hurtig clearance af vedvarende S. aureus-bakteriæmi ved pulmonalklap-endokarditis |
| [39777519](https://pubmed.ncbi.nlm.nih.gov/39777519/) | 2025 | In vitro | J Infect Dis | Forstærket dræbning af MRSA med ceftarolin eller vancomycin + carbapenemer (ertapenem/meropenem) |
| [11772242](https://pubmed.ncbi.nlm.nih.gov/11772242/) | 2001 | Review | Expert Opin Investig Drugs | Oversigt over ertapenems spektrum og PBP-binding |

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103216600 | Invanz (Merck Sharp & Dohme B.V.) | Pulver til koncentrat til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig i de kompilerede data |

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgraf (ikke fra produktresumé):** epilepsi, nyresygdom, pyoureter, Clostridium difficile-colitis, perinatal nekrotiserende enterokolitis. Disse stammer fra TxGNN-grafen og bør verificeres mod produktresuméet.
- **Lægemiddelinteraktioner:** I alt 38 registrerede interaktioner. Den eneste af alvorlighedsgrad *Major* er **bupropion** (øget risiko for krampeanfald er den kendte klasseproblematik for carbapenemer; verificér i produktresumé). *Moderate*: picosulfat, polyethylenglycol (3350 med elektrolytter) og natriumsulfat. Øvrige (bl.a. metronidazol, vancomycin, doxycyclin, morfin, metformin) er klassificeret som "ukendt" alvorlighed.
- **Kliniske hensyn fra litteraturen:** Hypoalbuminæmi kan give lavere ertapenem-eksponering pga. høj proteinbinding. Carbapenem-stewardship og risiko for resistens og C. difficile-infektion bør vægtes.

Godkendte advarsler og kontraindikationer fra produktresuméet var ikke tilgængelige i de kompilerede data; se det godkendte produktresumé (SmPC) for fuld sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Der findes konsistente case-serier, kohortestudier og dyredata for cefazolin + ertapenem ved vedvarende MSSA-bakteriæmi, og et fase 2-forsøg samt et fase 4-forsøg er i gang. Der foreligger dog endnu ingen afsluttede RCT'er, så brugen bør begrænses til kombinationsbehandling ved vedvarende MSSA-bakteriæmi.

**For at komme videre kræves:**
- Resultater fra NCT04886284 (CERT) og NCT07148960 (SABEDTIO)
- Hentning og gennemgang af produktresuméet (advarsler, kontraindikationer, godkendt indikationstekst)
- Data om virkningsmekanisme (MOA) fra DrugBank
- Retningslinjer for carbapenem-stewardship og monitorering (albuminniveau, krampetærskel, C. difficile)
- Gennemgang af den alvorlige interaktion med bupropion samt de moderate interaktioner
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

