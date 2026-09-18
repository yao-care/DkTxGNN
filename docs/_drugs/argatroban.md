---
layout: default
title: Argatroban
parent: Kun modelforudsigelse (L5)
nav_order: 45
evidence_level: L5
indication_count: 0
---

# Argatroban
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **0** stk.
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

# Argatroban: Vurdering af lægemidlers genbrug — TxGNN-forudsigelse ikke tilgængelig

## Sammenfatning på én sætning

Argatroban er en syntetisk direkte trombinhæmmer, der bruges intravenøst til profylakse og behandling af trombose hos patienter med heparin-induceret trombocytopeni (HIT).
Evidensepakken indeholder **ingen TxGNN-forudsigelser om genbrug** af dette lægemiddel, og kritiske data, herunder virkningsmekanisme, sikkerhedsadvarsler og kontraindikationer, er helt fraværende.
**En fuldstændig vurdering af genbrug kan ikke produceres på dette tidspunkt; denne rapport opsummerer datamangler og nødvendige næste trin.**

---

## Hurtigt overblik

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Trombose-profylakse/behandling ved heparin-induceret trombocytopeni (HIT) *(fra almenkendt viden; ingen regulatorisk registrering i datasættet)* |
| Forudsagt ny indikation | Ikke tilgængelig — TxGNN returnerede ingen kandidater |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Bevisniveau | Ikke vurderbar |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Afvent** |

---

## Hvorfor denne vurdering ikke kan fortsætte

Evidensepakken for Argatroban (DrugBank ID: DB00278) har to kritiske strukturelle problemer, der forhindrer en standardvurdering af genbrug.

**Først returnerede TxGNN-forudsigelsespipeline nul genbrugskandidater.** Dette er det grundlæggende output, som hele rapportstrukturen afhænger af. Uden mindst én forudsagt indikation og en tilhørende score er det ikke muligt at vurdere mekanistisk plausibilitet, søge efter understøttende kliniske forsøg eller vurdere bevisstyrke.

**For det andet er alle lægemiddelniveau-sikkerhedsdata fraværende.** Advarsler, kontraindikationer og lægemiddel–lægemiddelinteraktioner blev enten ikke hentet eller ikke fundet under søgekørslen den 26. marts 2026. For et antikoagulans-lægemiddel — en klasse med et snævert terapeutisk vindue og klinisk signifikant blødningsrisiko — ville det være uansvarligt at fortsætte uden sikkerhedsdata.

Fra generel farmakologisk viden er Argatroban en direkte, reversibel trombinhæmmer. Den binder det aktive sted på trombin og blokerer trombinkatalyse-reaktioner, herunder fibrinformation, blodpladeaktivering og aktivering af koagulationsfaktorer V, VIII og XIII. I modsætning til heparin kræver den ikke antitrombin som en kofaktor, hvilket gør den til det foretrukne lægemiddel, når heparinbrug er kontraindiceret på grund af HIT. Dette mekanistiske profil er relevant baggrundsviden for enhver fremtidig genbrugs-analyse, især i trombotiske eller inflammatoriske sammenhænge, hvor trombin spiller en patologisk rolle.

---

## Sikkerhedsmæssige overvejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

> **Bemærk for vurdereren:** Argatroban (varemærke *Argatra*) har en centraliseret EMA-markedsføringstilladelse i Den Europæiske Union. EMA-produktresumé er offentligt tilgængeligt på De Europæiske Lægemidlers Agenturs produktsider og bør bruges som den primære sikkerhedsreference, mens datamangler fra TFDA/Danmark løses.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Evidensepakken er strukturelt ufuldstændig — ingen TxGNN-forudsigelser blev genereret, og alle sikkerhedsfelter mangler — hvilket gør det umuligt at producere en valid genbrugsvurdering eller sikkerhedsvurdering. At fortsætte til klinisk overvejelse uden disse data ville ikke opfylde minimumbevisstandarden.

**For at fortsætte kræves følgende:**

- **[Blokerende]** Genkør TxGNN-forudsigelsespipeline for DB00278 og bekræft, at Argatroban er til stede og korrekt mappet i vidensgrafen; verificer, at lægemiddel–sygdom-kandidatlisten ikke blev utilsigtet filtreret ud
- **[Høj]** Hent virkningsmekanisme (MOA) data via DrugBank API for DB00278
- **[Høj]** Download og parse EMA *Argatra* SmPC (eller de danske nationale produktoplysninger, hvis tilgængelige) for at udfylde advarsler, kontraindikationer og særlige forholdsregler
- **[Medium]** Verificer Argatrobans registreringsstatus hos Lægemiddelstyrelsen; bemærk, at centraliseret EMA-godkendte produkter er juridisk tilgængelige i alle EU/EØS-medlemsstater, selv uden en national markedsføringstilladelelsesregistrering
- **[Opfølgning]** Når TxGNN-forudsigelser er tilgængelige, skal man gennemføre bevisindsamling fra standard kliniske forsøg (ClinicalTrials.gov, EudraCT) og litteratur (PubMed) for hver kandidatindikation

---

*Denne rapport genereres kun til forskningsformål og udgør ikke medicinsk rådgivning. Alle kandidater til lægemiddel-genbrug kræver klinisk validering før anvendelse. Dette dokument blev produceret under TxGNN Drug Repurposing Research Programme (Evidence Pack v4, dataskæring: 2026-04-04).*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

