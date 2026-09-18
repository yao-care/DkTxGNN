---
layout: default
title: Ciclopirox
parent: Kun modelforudsigelse (L5)
nav_order: 110
evidence_level: L5
indication_count: 0
---

# Ciclopirox
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

# Ciclopirox: Ingen TxGNN-prognose tilgængelig — utilstrækkelige data til repurposing-vurdering

## Sammenfatning på en sætning

Ciclopirox (DrugBank: DB01188) er et bredt spektrum antifungalt middel, der primært bruges topikalt til dermatomykoser og onychomykose.
**Ingen TxGNN repurposing-prognose er tilgængelig** for denne kandidat i den aktuelle bevissamling, da `predicted_indications`-feltet er tomt.
Uden en modelgenereret målindikation eller understøttende bevis kan en fuldstændig repurposing-evaluering ikke gennemføres på dette stadium.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Svampeinfektioner i hud og negle (dermatomykoser, onychomykose) — baseret på generel farmakologisk viden; ingen TFDA/SmPC-data indlæst |
| Forudsagt ny indikation | Ikke tilgængelig — ingen TxGNN-prognose genereret |
| TxGNN-prognosescore | Ikke tilgængelig |
| Bevisniveau | L5 (ingen understøttende studier identificeret i denne samling) |
| Status på det danske marked | Ikke markedsført (ingen godkendelser registreret hos Laegemiddelstyrelsen) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Afvent** |

---

## Hvorfor ingen prognose er tilgængelig

Bevisamlingen for denne kandidat (TW-DB01188-multi, v4) blev genereret med to bekræftede datagab, der sammen forhindrer en fuldstændig analyse:

1. **Manglende virkningsmekanisme (MOA)-data** — DrugBank-forespørgsel returnerede en post (forespørgsels-ID 2, status: vellykket), men MOA blev ikke udtrukket til samlingen. Ciclopirox virker ved at kompleksere polyvalente metalionioner (Fe³⁺, Al³⁺), der er vigtige kofaktorer for svampes cytokrom-afhængige enzymer, og forstyrrer således DNA-reparation, cellerespiration og celledeling. Disse oplysninger er imidlertid ikke blevet formelt valideret og indlæst i pipelinen.

2. **Ingen TFDA/reguleringsdata** — TFDA Summary of Product Characteristics (SmPC), herunder godkendte indikationer og kontraindikationer, blev ikke hentet (datagab DG001, alvorlighed: Blocking). Dette er en forudsætning for Sikkerhedsstadium 1-screening.

Uden disse to input kunne TxGNN-vidensgraf-matchning og sygdommapping-trin ikke producere en rangeret prognosliste, hvilket resulterede i et tomt `predicted_indications`-felt.

---

## Information om det danske marked

Ciclopirox har i øjeblikket **ingen markedsføringstilladelser** hos Laegemiddelstyrelsen og er ikke registreret som et markedsført produkt i Danmark. Hverken en national godkendelse eller en centraliseret EMA-godkendelse er blevet identificeret for denne substans.

> Bemærk: Ciclopirox markedsføres i flere andre EU/EØS-lande (f.eks. Tyskland, Frankrig) under mærkenavne som **Batrafen** og **Mycoster**, primært som topikale formuleringer (creme, opløsning, negleslak). En centraliseret eller gensidig anerkendelsesprocedure kan være en vej, hvis en dansk indikation forfølges.

---

## Sikkerhedshensyn

Både vigtige advarsler og kontraindikationer var anført som datagab i denne bevissamling. Ingen lægemiddel-lægemiddelinteraktionsposter blev fundet i DDI-forespørgslen (forespørgsels-ID 1, status: ikke_fundet).

> Se venligst den godkendte Summary of Product Characteristics (SmPC) — tilgængelig fra EMA-produktdatabasen eller nationale agenturer, hvor ciclopirox er godkendt — for fuldstændig sikkerhedsinformation herunder kontraindikationer, advarsler og lægemiddelinteraktioner.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Bevisamlingen er strukturelt ufuldstændig — både TxGNN forudsagt indikation og reguleringsmæssige sikkerhedsdata mangler, hvilket gør det umuligt at vurdere repurposing-gennemførlighed eller sikkerhedsprofil på dette stadium.

**For at fortsætte er følgende nødvendigt:**

- [ ] **Hent TFDA SmPC / EMA SmPC**: Download og parse det godkendte produktmærkat for at udtrække indikationer, kontraindikationer og vigtige advarsler (løser datagab DG001 — Blocking)
- [ ] **Indlæs MOA fra DrugBank API**: DrugBank-forespørgslen var vellykket (result_count: 1); kør ekstraktionstrinnet igen for at udfylde `original_moa` (løser datagab DG002 — High)
- [ ] **Kør TxGNN-prognose pipeline igen**: Når MOA og indikationsdata er indlæst, genkør vidensgraf- og deep-learning-prognosetrinene for at generere `predicted_indications`
- [ ] **Bekræft dansk regulatorisk vej**: Selvom ciclopirox i øjeblikket ikke markedsføres i Danmark, vurderes det, hvorvidt en eksisterende EMA-centraliseret godkendelse eller gensidig anerkendelsesprocedure kan tjene som grundlag for en dansk ansøgning
- [ ] **Regenerer bevissamling**: Efter de ovenstående trin skal du generere en ny samling (v5+) for fuld L1–L5 bevisvurdering og endelig Start/Afvent/Fortsæt med sikkerhedsforanstaltninger-beslutning

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

