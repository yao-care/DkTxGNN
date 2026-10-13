---
layout: default
title: Dextromethorphan
parent: Kun modelforudsigelse (L5)
nav_order: 258
evidence_level: L5
indication_count: 6
---

# Dextromethorphan
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
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

# Dextromethorphan: Fra forkølelse og rhinitis til sygdomme i næsehulen

## Resumé i én sætning

Dextromethorphan er et lægemiddel, der oprindeligt anvendes ved symptomer på øvre luftvejsinfektioner og rhinitis (bl.a. forkølelse, svælgbetændelse og allergisk rhinitis).
TxGNN-modellen forudsiger, at det kan være virksomt ved **sygdom i næsehulen (nasal cavity disease)**,
men der er på nuværende tidspunkt **0 kliniske forsøg** og **0 publikationer** i de data, der er indsamlet til denne rapport. Forudsigelsen hviler derfor alene på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske markedsføringstilladelse. Videnbasen nævner allergisk rhinitis, vasomotorisk rhinitis, faryngitis, forkølelse, nasofaryngitis og hovedpinesygdom |
| Forudsagt ny indikation | Sygdom i næsehulen (nasal cavity disease) |
| TxGNN-forudsigelsesscore | 99,98 % |
| Evidensniveau | L4 (som angivet i data; ingen kliniske forsøg eller publikationer er tilgængelige) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om virkningsmekanismen. Dextromethorphan er kendt som et centralt virkende hostedæmpende middel (NMDA-receptorantagonist og sigma-1-agonist), men dette er ikke bekræftet i de data, der er indsamlet til denne rapport.

Næsehulesygdomme omfatter bl.a. rhinitis, som allerede er en af lægemidlets oprindelige indikationer i videnbasen. Den meget høje score afspejler sandsynligvis dette overlap med eksisterende indikationer snarere end et nyt repurposing-signal. Koblingen er indirekte og kan ikke bekræftes med de foreliggende data.

Til sammenligning har modellen også forudsagt andre indikationer (se nedenfor), hvoraf flere er spekulative.

### Øvrige forudsigelser fra modellen

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Akut laryngofaryngitis | 99,98 % | L4 | Tæt på eksisterende indikationer (faryngitis, forkølelse). Kun symptomlindring af hoste, ikke sygdomsmodificerende |
| Faucial difteri | 99,36 % | L5 | Ingen kendt antibakteriel eller antitoksin-aktivitet. Ikke et meningsfuldt repurposing-grundlag |
| Trigeminal autonom cephalalgi | 99,32 % | L5 | Muligt, men ubevist link via NMDA-antagonisme og centrale smertebaner. Mekanistisk adskilt fra almindelig hovedpine |
| Degenerativ cervikal diskussygdom | 99,30 % | L5 | Spekulativt link via neuropatisk smerte. Påvirker ikke selve degenerationen |
| Allergisk urticaria | 99,25 % | L5 | Sandsynligvis grafnærhed til allergisk rhinitis. Dextromethorphan er hverken antihistamin eller mastcellestabilisator |

Alle fem har Hold som anbefaling.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Doseringsform | Godkendt indikation |
|---------|------|------|-----------|
| 28101229585 | Dexofan (Orifarm Healthcare A/S) | Filmovertrukne tabletter | Indikationsteksten er ikke tilgængelig |

Lægemidlet er markedsført som enkeltstofpræparat til oral anvendelse. Der er ikke registreret nogen annullerede tilladelser.

---

## Sikkerhedsovervejelser

Der foreligger ikke godkendt produktresumé-information om advarsler og kontraindikationer i de indsamlede data. Følgende oplysninger stammer fra videnbasen og/eller interaktionsdatabaser og er **ikke** hentet fra produktresuméet.

**Kontraindikationer fra videnbasen (ikke fra produktresumé):**
Videnbasen knytter lægemidlet til en lang række tilstande, bl.a.: hypertension, hypotension, langt QT-syndrom (herunder torsades de pointes), leversvigt og leversygdom, nyresygdom, epilepsi, kronisk obstruktiv lungesygdom, bronkitis, mavesår/ulcus pepticum, inflammatorisk tarmsygdom, pankreatitis, galdeblæresygdom, trombocytopeni, binyrebarkinsufficiens (Addisons sygdom), hypothyreose, diabetes mellitus (inkl. diabetisk ketoacidose), benign prostatahyperplasi, kaliummangel og dermatitis herpetiformis.

**Lægemiddelinteraktioner:** Der er identificeret i alt 381 mulige interaktioner. Blandt de vigtigste:
- **Alvorlige (Major):** dexfenfluramin, fenfluramin, lorcaserin, sibutramin (risiko for serotonerge effekter), samt dolasetron, granisetron, ondansetron og palonosetron
- **Moderate:** bupropion, morfin (inkl. liposomal), cimetidin, dronabinol, eliglustat, glycerolphenylbutyrat, mazindol, metoclopramid, nabilon, opium og phentermin

Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for sygdom i næsehulen understøttes ikke af kliniske forsøg eller litteratur, og den høje score afspejler sandsynligvis overlap med eksisterende rhinitis-indikationer snarere end en ny anvendelse. Der mangler desuden data om virkningsmekanisme og produktresumé-sikkerhed.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer), da dette er blokerende for sikkerhedsscreening
- Systematisk litteratur- og forsøgssøgning for dextromethorphan ved sygdomme i næsehulen
- Afklaring af, hvilken konkret klinisk indikation i næsehulen der er tale om, og om den adskiller sig fra de eksisterende rhinitis-indikationer
- Vurdering af administrationsvej (data er endnu ikke afklaret)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

