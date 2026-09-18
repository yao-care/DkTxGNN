---
layout: default
title: Dornase Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
---

# Dornase Alfa
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

# Dornase alfa: Fra cystisk fibrose til blandet mineralstofdammpneumokoniose

## En-sætnings sammenfattelse

Dornase alfa (handelsnavn: Pulmozyme) er et rekombinant humant deoxyribonuklease I (DNase I) enzym, der oprindeligt blev godkendt til behandling af cystisk fibrose (CF), hvor det reducerer viskositeten i luftvejsslim ved at nedbryde ekstracellulær DNA, der frigives fra degenererende neutrofiler.
TxGNN-modellen forudsiger, at det kan være effektivt ved **blandet mineralstofdammpneumokoniose** — en erhvervsbetinget lungesygdom drevet af kronisk mineralstofdamminduceret betændelse.
Imidlertid understøttes denne retning ikke i øjeblikket af kliniske forsøg eller publiceret litteratur, og alle 10 forudsagte indikationer i denne pakke er klassificeret som **L5 (kun modelforudsigelse)**, med en samlet anbefaling af **Hold**.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Original indikation | Cystisk fibrose (inhaleret mukolitisk / DNase-terapi) |
| Forudsagt ny indikation | Blandet mineralstofdammpneumokoniose |
| TxGNN-forudsigelsesscore | 50.00% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

For øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i bevisepakken. Baseret på etableret farmakologi er dornase alfa et rekombinant humant DNase I-enzym, der selektivt spalter fosfodiesterbindingerne i ekstracellulær DNA (eDNA). Ved cystisk fibrose skabes patologisk tyktflydende slim i luftvejene på grund af massiv eDNA-ophobning fra lyserede neutrofiler, og inhaleret dornase alfa reducerer denne viskositet, forbedrer mukociliær klaring og sænker således risikoen for pulmonale eksacerbationer.

Den mekanistiske begrundelse, som TxGNN foreslår for blandet mineralstofdammpneumokoniose, er baseret på observationen af, at mineralstofdampe (silika, kul, asbest) udløser vedvarende neutrofil infiltration i lungeparekymet. Aktiverede neutrofiler frigiver neutrofil ekstracellulære fælde (NETs) — netformede strukturer af eDNA, histoner og antimikrobielle proteiner — som kan opretholde kronisk betændelse. I teorien kunne dornase alfa nedbryde disse NETs og derved afbryde inflammatorisk signalering og reducere den inflammatoriske belastning.

Imidlertid er den centrale patologiske drivkraft for pneumokoniose irreversibel silika- eller kulstoffdamminduceret fibrose — en proces, hvor eDNA-ophobning er et sekundært, efterfølgende fænomen snarere end den primære årsag. Den mekanistiske forbindelse mellem dornase alfas DNase-aktivitet og klinisk meningsfuld fibrosereduktion er derfor svag, indirekte og spekulativ. Ingen kliniske eller præ-kliniske studier har direkte undersøgt dornase alfa ved pneumokoniose, og TxGNN-forudsigelsen afspejler mest sandsynligt topologisk nærhed mellem sygdomsnode i vidensgrafen snarere end stærk biologisk begrundelse.

---

## Klinisk forsøgsviden

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturviden

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Ifølge det aktuelle datasæt har dornase alfa ingen markedsføringstilladelser registreret i den danske regulatoriske database (Laegemiddelstyrelsen).

| Markedsføringstilladelsesnummer | Produktnavn | Doseringform | Godkendt indikation |
|---------|------------|------|---|
| — | — | — | Ingen poster fundet |

> **Bemærkning for klinikere:** Pulmozyme (dornase alfa) har en centraliseret EMA-markedsføringstilladelse (EU/1/94/011), der er gyldig i alle EU/EØS-medlemsstater, herunder Danmark. Sundhedsfagpersoner bør bekræfte den aktuelle forsyning og refusionsstatus direkte via EMA's produktdatabase eller Laegemiddelstyrelsen nationale lægemiddelregister, da fravær af en lokal licenspost kan afspejle et datakløft snarere end regulatorisk utilgængelighed.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
Alle 10 TxGNN-forudsagte indikationer for dornase alfa er klassificeret som L5 med en ensartet forudsigelsesscore på 50%, og den højest rangerede indikation (blandet mineralstofdammpneumokoniose) understøttes kun af en svag, inferentiel mekanistisk hypotese uden klinisk eller præ-klinisk evidens. Et genbrugsprogram på dette tidspunkt ville være for tidligt.

**Noter om landskabet for alle 10 forudsigelser:**
Blandt de 10 forudsagte indikationer har **senebetændelse (rang 10)** den videnskabeligt mest velbegrundet hypotese: NETs er blevet påvist i beskadiget senevæv og vist i tidlig præ-klinisk arbejde at fremme kronisk betændelse og tenocyt-apoptose via HMGB1/TLR4-signalvejen. DNase-behandling er blevet rapporteret at nedbryde NET'er i senevæv og forbedre senevævets reparationsmiljø. Selvom stadig L5, er senebetændelse den eneste kandidat, som bevisepakken eksplicit markerer som et **forskningsspørgsmål** værd at udforske yderligere. De resterende 8 indikationer (allergisyndromer, sjældne genetiske lidelser, mastcellesygdomme) har mekanistiske forbindelser fra højst spekulative til fraværende.

**For at fortsætte er følgende nødvendigt:**
- Hentning af den fulde virkningsmekanisme (MOA) for dornase alfa fra DrugBank API (for øjeblikket et kritisk datakløft ifølge denne pakke)
- Hentning og gennemgang af det godkendte produktresumé/patientinformation (SmPC/PIL) på dansk eller fra EMA for dornase alfa for at fuldføre sikkerhedsprofilen (vigtige advarsler, kontraindikationer) — for øjeblikket en blokerende datakløft
- Verifikation af aktuel EMA/Laegemiddelstyrelse-markedsføringstilladelsestatus og lokal tilgængelighed af Pulmozyme
- Specifikt for **blandet mineralstofdammpneumokoniose**: en målrettet litteraturgennemgang i databaser for erhvervsmedicin (f.eks. NIOSHTIC, CISDOC) for at bekræfte fravær af eventuelle præ-kliniske NET-i-pneumokoniose-beviser før denne hypotese lukkes
- Hvis **senebetændelse** prioriteres til yderligere evaluering: bestilling eller identifikation af en præ-klinisk proof-of-concept-undersøgelse (NET-nedbrydning i senevævmodeller) som en nødvendig forudsætning før påbegyndelse af et klinisk genbrugsprogram

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

