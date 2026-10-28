---
layout: default
title: Spectinomycin
parent: Kun modelforudsigelse (L5)
nav_order: 773
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "spectinomycin"
predicted_indications: ["disease of uterine broad ligament", "abdominal ectopic pregnancy", "celiac trunk compression syndrome", "abdominal cystic lymphangioma", "lymph node palisaded myofibroblastoma", "disease of retroperitoneum", "sacrum chordoma", "urethral disease", "disease of peritoneum", "embryonic cyst of fallopian tube"]
description: "Spectinomycin: forudsagt ny indikation Disease of uterine broad ligament (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Spectinomycin
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

## Spectinomycin: Disease of uterine broad ligament
{: .text-alpha }

## Resumé

Spectinomycin er et aminocyclitol-antibiotikum, der oprindeligt blev brugt til behandling af gonoré og akut gonokok-cervicitis. TxGNN-modellen forudsiger, at det kan have effekt på **sygdom i ligamentum latum uteri** (uterus' brede ledbånd). Der er **ingen kliniske forsøg** og **ingen publikationer**, der understøtter denne specifikke forudsigelse, så den er alene modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Disease of uterine broad ligament |
| TxGNN-forudsigelsesscore | 0.9957 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger ikke detaljerede data om virkningsmekanismen i de data, der er sammenstillet til denne rapport. Spectinomycin er kendt som et aminocyclitol-antibiotikum, der hæmmer bakteriens proteinsyntese ved at binde til den lille (30S) ribosomale underenhed. Lægemidlets effekt ved gonoré er veldokumenteret.

En mekanistisk sammenhæng med sygdom i ligamentum latum uteri ville kun findes, hvis tilstanden skyldtes en bakteriel infektion, f.eks. gonokokker. De foreliggende data understøtter ikke en sådan årsag. Scoren kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke biologisk evidens. Forudsigelsen bør derfor tolkes som en hypotese uden understøttelse.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relevante registrerede kliniske forsøg.

---

## Litteraturevidens

Der er i øjeblikket ingen relevant litteratur for den forudsagte indikation.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106307819 | Lismay | Pulver til anvendelse i drikkevand | Ikke angivet |
| 28101550493 | Norospeclin Vet. | Injektionsvæske, opløsning | Ikke angivet |

Begge tilladelser er nationale og gyldige. Ud fra produktnavn, producent og lægemiddelform ser de ud til at være veterinærlægemidler. Der er derfor ikke identificeret et humant præparat med spectinomycin på det danske marked i de data, der er sammenstillet til denne rapport.

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er registreret én interaktion af moderat sværhedsgrad med **picosulfat** (picosulfuric acid).

Oplysninger om advarsler og kontraindikationer var ikke tilgængelige i de sammenstillede data. Der henvises til det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en grafbaseret model uden kliniske forsøg, litteratur eller en plausibel biologisk sammenhæng med en antibakteriel mekanisme. Evidensniveauet er L5.

**Supplerende bemærkning:** Blandt de ti forudsagte indikationer er **uretral sygdom** (score 0,9953) den eneste med meningsfuld litteratur (evidensniveau L3). Det er hovedsageligt en forlængelse af den eksisterende gonoréindikation og ikke en egentlig nyanvendelse. Eksempler:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [3156805](https://pubmed.ncbi.nlm.nih.gov/3156805/) | 1985 | RCT | Genitourin Med | 2 g spectinomycin versus 250 mg ceftriaxon i.m. hos 200 mænd med ukompliceret gonokokuretritis; alle opfulgte patienter i spectinomycingruppen (93) blev helbredt |
| [6134959](https://pubmed.ncbi.nlm.nih.gov/6134959/) | 1983 | Sammenlignende studie | Lancet | Helbredelsesrate på 97 % med spectinomycin mod 100 % med ceftriaxon ved ukompliceret gonoré hos mænd |
| [40714374](https://pubmed.ncbi.nlm.nih.gov/40714374/) | 2025 | Kohorte | J Infect Chemother | Intramuskulær spectinomycin vurderet ved vanskeligt behandlelig *Mycoplasma genitalium*-uretritis i fire tilfælde |

Evidensen er hovedsageligt ældre, og brugen er begrænset af tilgængelighed og resistensproblemer.

**For at komme videre kræves følgende:**
- Data om virkningsmekanismen (MOA) fra DrugBank
- Oplysninger om advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen
- Dokumentation for en mulig bakteriel ætiologi ved sygdom i ligamentum latum uteri, før en klinisk undersøgelse overvejes
- Afklaring af, om et humant spectinomycinpræparat er tilgængeligt i Danmark, da de nuværende tilladelser ser ud til at gælde veterinærlægemidler
- Overvejelse af, om uretral sygdom (gonokok- og *M. genitalium*-uretritis) bør vurderes som et særskilt forskningsspørgsmål
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

