---
layout: default
title: Icatibant
parent: Høj evidens (L1-L2)
nav_order: 419
evidence_level: L1
indication_count: 10
---

# Icatibant
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
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

# Icatibant: Fra arvelig angioødem til C1-hæmmermangel

## Opsummering i en sætning

Icatibant er en selektiv bradykinin B2-receptorantagonist, som oprindeligt anvendes til behandling af akutte anfald af arvelig angioødem (HAE).
TxGNN-modellen forudsiger, at den kan være effektiv ved **C1-hæmmermangel**,
og denne retning understøttes af **12 kliniske forsøg** og **21 publikationer** i de data, der er indsamlet til denne rapport.
Bemærk, at den forudsagte indikation i praksis er identisk med lægemidlets godkendte indikation (arvelig angioødem med C1-hæmmermangel). Der er derfor tale om en bekræftelse af eksisterende indikation snarere end egentlig omlægning af anvendelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Arvelig angioødem (HAE), herunder HAE med C1-hæmmermangel (den godkendte indikationstekst er ikke angivet i de indsamlede data) |
| Forudsagt ny indikation | C1-hæmmermangel |
| TxGNN-forudsigelsesscore | 99,99 % |
| Evidensniveau | L1 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Icatibant er en syntetisk peptid-antagonist (dekapeptid) af bradykinin B2-receptoren. Ved C1-hæmmermangel, uanset om den er arvelig eller erhvervet, mister kallikrein-kinin-systemet sin normale hæmning. Det fører til et overskud af bradykinin, som via B2-receptoren udløser de karakteristiske angioødemanfald. Ved at blokere receptoren angriber icatibant direkte den centrale sygdomsmediator. Detaljerede data om virkningsmekanisme fra DrugBank var ikke tilgængelige i de indsamlede data, men farmakologiske data bekræfter binding til B1- og B2-receptorerne (BDKRB1 og BDKRB2).

Den forudsagte indikation overlapper i høj grad med den oprindelige. Evidensen for **arvelig** form er stærk og bygger på flere fase 3-studier. For den **erhvervede** form (AAE-C1-INH) er evidensen mere begrænset: et observationsstudie fra den virkelige verden (PMID 22686628) beskriver otte patienter med 48 behandlede anfald, mens en nyere retrospektiv undersøgelse (PMID 37716525) angiver, at der ikke findes nogen godkendt behandling til den erhvervede form.

Øvrige forudsagte indikationer (serpinopati med toksisk serpinpolymerisering, pseudo-von Willebrands sygdom, primær frigivelsesforstyrrelse af blodplader og immunmedieret nekrotiserende myopati) har ingen kliniske forsøg eller litteratur og vurderes som modelartefakter eller spekulative. De har evidensniveau L5 og anbefalingen "Hold".

---

## Klinisk evidens fra forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT00097695](https://clinicaltrials.gov/study/NCT00097695) | Fase 3 | Afsluttet | 84 | Randomiseret, dobbeltblindet, placebokontrolleret studie af subkutan icatibant ved akutte anfald af HAE |
| [NCT00500656](https://clinicaltrials.gov/study/NCT00500656) | Fase 3 | Afsluttet | 85 | Randomiseret, dobbeltblindet sammenligning af icatibant og oral tranexamsyre; primært endepunkt var tid til symptomlindring |
| [NCT00912093](https://clinicaltrials.gov/study/NCT00912093) | Fase 3 | Afsluttet | 98 | Randomiseret, dobbeltblindet, placebokontrolleret studie af effekt og sikkerhed ved akutte HAE-anfald |
| [NCT00997204](https://clinicaltrials.gov/study/NCT00997204) | Fase 3 | Afsluttet | 151 | Åbent studie af sikkerhed, lokal tolerabilitet og effekt ved selvadministration |
| [NCT01386658](https://clinicaltrials.gov/study/NCT01386658) | Fase 3 | Afsluttet | 32 | Åbent studie af farmakokinetik, tolerabilitet og sikkerhed hos børn og unge |
| [NCT03888755](https://clinicaltrials.gov/study/NCT03888755) | Fase 3 | Afsluttet | 8 | Åbent studie hos japanske patienter med type I eller II HAE |
| [NCT04654351](https://clinicaltrials.gov/study/NCT04654351) | Fase 3 | Afsluttet | 2 | Japanske børn og unge; meget lille stikprøve |
| [NCT01457430](https://clinicaltrials.gov/study/NCT01457430) | Fase 4 | Afsluttet | 19 | Åbent studie af selvadministreret icatibant mod administration på klinik |
| [NCT07290855](https://clinicaltrials.gov/study/NCT07290855) | Fase 4 | Afsluttet | 5 | Sikkerhed og effekt ved bradykinin-induceret angioødem (Taiwan) |
| [NCT04057131](https://clinicaltrials.gov/study/NCT04057131) | Ikke relevant | Afsluttet | 179 | Japansk observationel undersøgelse af lægemiddelbrug efter markedsføring |

Yderligere to forsøg findes i datagrundlaget (NCT05509569, japansk pædiatrisk overvågning, n=32, og NCT02045264, fase 1 hos raske japanske frivillige, n=12).

---

## Evidens fra litteraturen

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [29757016](https://pubmed.ncbi.nlm.nih.gov/29757016/) | 2018 | Kohorte/oversigt | Expert Rev Clin Immunol | Randomiserede, åbne og observationelle studier har påvist sikkerhed og effekt hos unge og børn over 2 år med C1-INH-HAE |
| [22686628](https://pubmed.ncbi.nlm.nih.gov/22686628/) | 2012 | Observationsstudie | Allergy | Otte patienter med erhvervet C1-INH-mangel; 48 anfald behandlet med icatibant 30 mg subkutant |
| [20030426](https://pubmed.ncbi.nlm.nih.gov/20030426/) | 2010 | Oversigtsartikel | Drugs | I FAST-1 nåede forskellen i tid til symptomlindring ikke statistisk signifikans, men icatibant var effektiv på flere andre endepunkter |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematisk oversigt | Pneumonol Alergol Pol | Sammenligning af conestat alfa, human C1-esteraschæmmer og icatibant ved akutte anfald |
| [37716525](https://pubmed.ncbi.nlm.nih.gov/37716525/) | 2023 | Retrospektivt studie | J Allergy Clin Immunol Pract | Erhvervet angioødem med C1-INH-mangel: diagnose, forløb og behandling; ingen godkendt behandling |
| [33602658](https://pubmed.ncbi.nlm.nih.gov/33602658/) | 2021 | Oversigtsartikel | J Investig Allergol Clin Immunol | Aktuel behandling af C1-INH-HAE og lægemidler under udvikling |
| [28687105](https://pubmed.ncbi.nlm.nih.gov/28687105/) | 2017 | Oversigtsartikel | Immunol Allergy Clin North Am | Erhvervet C1-INH-mangel er ofte forbundet med autoimmunitet og B-celle-lymfoproliferative sygdomme |
| [32753245](https://pubmed.ncbi.nlm.nih.gov/32753245/) | 2020 | Anbefalinger | Rev Med Interne | CREAK-anbefalinger for diagnose og behandling af erhvervet angioødem med C1-INH-mangel |
| [24925394](https://pubmed.ncbi.nlm.nih.gov/24925394/) | 2014 | Oversigtsartikel | Chem Immunol Allergy | Bradykininmedierede sygdomme, herunder C1-INH-mangel og ACE-hæmmerudløst angioødem |
| [21284353](https://pubmed.ncbi.nlm.nih.gov/21284353/) | 2010 | Vurdering | Prescrire Int | Anbefaler fortsat at bruge C1-esteraschæmmer som førstevalg ved anfald |

---

## Oplysninger om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104196507 | Firazyr (Takeda Pharmaceuticals International AG Ireland Branch) | Injektionsvæske, opløsning | Indikationsteksten er ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: 10 moderate interaktioner er registreret med ACE-hæmmere: benazepril, captopril, enalapril, perindopril, trandolapril, moexipril, lisinopril, quinapril, ramipril og fosinopril. Kombinationen kræver forsigtighed, da ACE-hæmmere hæmmer nedbrydningen af bradykinin.
- **Farmakologi**: Icatibant binder til bradykinin B1- og B2-receptorerne.

Oplysninger om advarsler og kontraindikationer var ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger)**

**Begrundelse:**
Flere afsluttede fase 3-forsøg, herunder tre randomiserede kontrollerede studier, understøtter effekt og sikkerhed ved HAE med C1-hæmmermangel (evidensniveau L1), og lægemidlet er allerede markedsført i Danmark. Den forudsagte indikation er i praksis identisk med den godkendte, mens evidensen for den erhvervede form er begrænset til små observationsstudier.

**For at komme videre er følgende nødvendigt:**
- Gennemgang af produktresuméet (SmPC) for advarsler, kontraindikationer og den godkendte indikationstekst
- Mere solid evidens for erhvervet C1-hæmmermangel, hvis udvidet anvendelse overvejes
- Detaljerede data om virkningsmekanisme fra DrugBank
- Plan for sikkerhedsovervågning, især ved samtidig brug af ACE-hæmmere
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

