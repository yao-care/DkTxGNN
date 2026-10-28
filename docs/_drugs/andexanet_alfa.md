---
layout: default
title: Andexanet Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 65
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
description: "Andexanet Alfa: forudsagt ny indikation Glanzmanns trombasteni (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (godkendelsesteksten er tom). Ifølg…"
monitor_inn: "ANDEXANET ALFA"
predicted_indications: ["Glanzmann thrombasthenia", "primary release disorder of platelets", "pseudo-von Willebrand disease", "hemophilia"]
---

# Andexanet Alfa
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

## Andexanet alfa: Fra reversering af faktor Xa-hæmmere til Glanzmanns trombasteni
{: .text-alpha }

## Resumé i én sætning

Andexanet alfa er et rekombinant lægemiddel, som er markedsført i Danmark under navnet Ondexxya. Det bruges til at neutralisere virkningen af faktor Xa-hæmmende blodfortyndende midler. TxGNN-modellen forudsiger, at det kan have effekt ved **Glanzmanns trombasteni**, men der foreligger **0 kliniske forsøg** og **0 publikationer** for denne indikation. Forudsigelsen er derfor udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (godkendelsesteksten er tom). Ifølge litteraturen anvendes lægemidlet til reversering af faktor Xa-hæmmere (apixaban, rivaroxaban) ved livstruende blødning |
| Forudsagt ny indikation | Glanzmanns trombasteni |
| TxGNN-forudsigelsesscore | 0,9977 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i de indsamlede data. Ud fra den kendte farmakologi er andexanet alfa en rekombinant, katalytisk inaktiv faktor Xa-"lokkemad" (decoy), der binder og neutraliserer direkte faktor Xa-hæmmere. Det genopretter dermed trombindannelsen, men kun når en faktor Xa-hæmmer er til stede.

Glanzmanns trombasteni er en arvelig defekt i trombocytternes integrin αIIbβ3 (GPIIb/IIIa), som medfører manglende trombocytaggregation. Lokkemad-mekanismen adresserer ikke denne defekt, og der er derfor ingen plausibel mekanistisk forbindelse.

Den meget høje score (0,9977) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede koagulations- og blødningssygdomme, ikke biologisk evidens eller et reelt farmakologisk rationale.

Det samme gælder de øvrige forudsigelser i datasættet: primær frigørelsesdefekt i trombocytter og pseudo-von Willebrands sygdom (score hhv. 0,9976 og 0,9965, begge L5, uden forsøg eller litteratur) samt hæmofili (score 0,9910, L4). For hæmofili erstatter andexanet alfa ikke den manglende faktor, og tromboembolisk risiko (set i ANNEXA-4 og ANNEXA-I) ville give anledning til bekymring. Den hentede litteratur omhandler DOAC-reversering og laboratoriemæssig interferens, ikke behandling af hæmofili. Højst er en hæmofilipatient i behandling med en faktor Xa-hæmmer og alvorlig blødning en randtilfælde-anvendelse af den eksisterende indikation, ikke repurposing.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er ingen litteratur for den primært forudsagte indikation (Glanzmanns trombasteni). Nedenfor er de mest relevante publikationer, der er fundet for hæmofili (rang 7). De er alle indirekte og evaluerer ikke andexanet alfa som behandling af hæmofili.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [38620086](https://pubmed.ncbi.nlm.nih.gov/38620086/) | 2024 | Kohorte-/subanalyse | Circulation | ANNEXA-4-subanalyse af effekt og sikkerhed af andexanet alfa ved akut gastrointestinal blødning under faktor Xa-hæmmere |
| [33742436](https://pubmed.ncbi.nlm.nih.gov/33742436/) | 2021 | Retningslinje | Thromb Haemost | Opdaterede ICSH-anbefalinger for laboratoriemåling af DOAC'er; omtaler et specifikt reverseringsmiddel |
| [31962376](https://pubmed.ncbi.nlm.nih.gov/31962376/) | 2020 | Laboratoriestudie | Haemophilia | Sammenligning af DOAC Stop og andexanet alfa til at fjerne rivaroxabans interferens i FVIII/FIX-analyser |
| [31298165](https://pubmed.ncbi.nlm.nih.gov/31298165/) | 2019 | Review | Curr Pharm Des | Nye hæmostatiske midler og antidoter: perioperative overvejelser for anæstesiologer |
| [30309890](https://pubmed.ncbi.nlm.nih.gov/30309890/) | 2018 | Review | Blood | Reversering af anti-faktor Xa-midler og uopfyldte behov hos traumepatienter |
| [26519420](https://pubmed.ncbi.nlm.nih.gov/26519420/) | 2016 | Review | Drug Saf | Reverseringsstrategier for NOAC'er: udvikling og fremtidsperspektiver |
| [27254626](https://pubmed.ncbi.nlm.nih.gov/27254626/) | 2016 | Review | Dtsch Med Wochenschr | Koagulationsforstyrrelser på intensivafdelingen, herunder håndtering af NOAC-relateret blødning |
| [36819179](https://pubmed.ncbi.nlm.nih.gov/36819179/) | 2023 | Review af lokale protokoller | EJHaem | Gennemgang af britiske hospitalers lokale protokoller for brug af andexanet alfa |
| [42033142](https://pubmed.ncbi.nlm.nih.gov/42033142/) | 2026 | Positionspapir | Br J Haematol | Britisk positionspapir fra British Society for Haematology om brug af andexanet alfa |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105829516 | Ondexxya (AstraZeneca AB) | Pulver til infusionsvæske, opløsning | Indikationsteksten er ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller interaktioner i de indsamlede data. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Fra litteraturen kendes en tromboembolisk risiko ved brug af andexanet alfa (set i ANNEXA-4 og ANNEXA-I), hvilket er særligt relevant ved blødningssygdomme.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for Glanzmanns trombasteni er udelukkende modelbaseret (L5) uden kliniske forsøg eller litteratur, og der er ingen plausibel mekanistisk forbindelse, da lokkemad-mekanismen ikke adresserer trombocytternes aggregationsdefekt. Den høje score skyldes sandsynligvis grafnærhed.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Godkendt indikationstekst og sikkerhedsoplysninger (advarsler og kontraindikationer) fra produktresuméet hos Lægemiddelstyrelsen
- Prækliniske eller mekanistiske data, der kan underbygge en eventuel sammenhæng, før yderligere vurdering er relevant
- Vurdering af tromboembolisk risiko hos patienter med blødningssygdomme
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

