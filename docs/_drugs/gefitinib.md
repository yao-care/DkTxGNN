---
layout: default
title: Gefitinib
parent: Kun modelforudsigelse (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Gefitinib
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

# Gefitinib: Fra ikke-småcellet lungekræft til gingivalt fibromatose

## Resumé i én linje

Gefitinib (Iressa) er en selektiv EGFR-tyrosin-kinase-hæmmer, godkendt internationalt til behandling af ikke-småcellet lungekræft (NSCLC) med aktiverende EGFR-mutationer.
TxGNN-modellen tildeler denne indikation den højeste forudsigelsesscore til **Gingivalt fibromatose** (99.89%), men denne indikation har **ingen understøttende kliniske forsøg eller litteratur** — og det mekanistiske rationalet rejser en kritisk bekymring: gingivalhyperplasi (gingivalt overvækst) er selv en kendt uønsket bivirkning af EGFR-TKI'er, hvilket tyder på, at dette meget sandsynligt er et farmakologiovervågnings falsk-positivt signal snarere end en sand terapeutisk mulighed.

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Original indikation | Ikke-småcellet lungekræft (NSCLC) med aktiverende EGFR-mutationer |
| Forudsagt ny indikation | Gingivalt fibromatose |
| TxGNN forudsigelsesscore | 99.89% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Gefitinib er en selektiv, reversibel hæmmer af epidermalt vækstfaktor-receptor-tyrosin-kinase (EGFR/HER1/ErbB1). Det blokerer autofosforylering af det intracelluløre EGFR-kinase-domæne og undertrykker således nedstrøms proliferation og overlevelses-signalerings-kaskader (RAS/MAPK og PI3K/AKT-veje). I NSCLC med aktiverende EGFR-mutationer — mest almindeligt exon 19-deletioner og L858R-punktmutationen — producerer denne blokering klinisk meningsfuld tumorregression, som påvist i det skelsættende IPASS-forsøg (NEJM, 2009). Detaljerede data om mekanisme for virkning blev ikke hentet fra DrugBank i denne bevis-pakke; ovenstående er baseret på etableret farmakologisk klassificering.

Gingivalt fibromatose er en sjælden, godartelig tilstand karakteriseret ved progressiv fibrøs hyperplasi af gingivalt bindevæv. Der er i øjeblikket ingen publiceret evidens for, at EGFR-overekspression eller konstitutiv EGFR-aktivering spiller en patologisk rolle i denne sygdom. Det biologiske rationalet for behandling af gingivalt fibromatose med en EGFR-TKI er derfor fraværende.

**Denne forudsigelse er meget sandsynligt en falsk positiv.** Gingivalhyperplasi (gingivalt overvækst) er en velkendt uønsket bivirkning af EGFR-TKI'er, herunder gefitinib. TxGNN-vidensgrafen har sandsynligt fanget en lægemiddel-sygdom-co-forekomst fra farmakologiovervågningsdatabaser og misfortolket denne bivirkningsassociation som et terapeutisk signal. Dette er et anerkendt artefaktmønster i neurale netværks-baserede repurposing-modeller, hvor bivirkningsknudepunkter og terapeutiske knudepunkter deler strukturel lighed i vidensgrafen.

---

## Klinisk forsøgsevidens

I øjeblikket er der ingen relaterede kliniske forsøg registreret for gefitinib i gingivalt fibromatose.

---

## Litteraturevidens

I øjeblikket er der ingen tilgængelig litteratur for gefitinib i gingivalt fibromatose.

---

## Markedsinformation for Danmark

Gefitinib har i øjeblikket ingen nationale eller centraliserede markedsføringstilladelser registreret hos Lægemiddelstyrelsen. Sundhedspersonale, der ønsker adgang for individuelle patienter, skal ansøge om særlig tilladelse (*særlig tilladelse* / navngivet patient-program).

> **Bemærkning for kontekst:** Gefitinib (Iressa, AstraZeneca) har EU-godkendelse gennem centraliseret procedure for EGFR-muteret NSCLC i andre EU/EØS-medlemsstater. Dens fravær fra det danske marked afspejler ikke en sikkerhedstilbagetrækning, men er en kommerciel beslutning. Adgang via særlig tilladelse er mulig, hvis der er klinisk behov.

---

## Cytotoksicitet

| Emne | Indhold |
|------|---------|
| Cytotoksicitetsklassificering | Målrettet terapi — første generations selektiv EGFR-tyrosin-kinase-hæmmer (ikke et konventionelt cytotoksisk middel) |
| Myelo-suppressionsrisiko | Lav (myelo-suppression er usædvanlig; ikke en karakteristisk toksicitet af EGFR-TKI'er) |
| Emetogenicitetsklassificering | Lav |
| Overvågningsparametre | Leverfunktion (ALT, AST, bilirubin — risiko for hepatotoksicitet); lungefunktion (interstitiel lungesygdom / pneumonitis — sjælden men potentielt dødelig); hud- og neglstoksicitet (akneiformt udslæt, paronychi); nyrefunktion og elektrolytter |
| Sikkerhedsforholdsregler ved håndtering | Standard forholdsregler for oral antineoplastisk behandling gælder; følg lokale institutionelle retningslinjer for håndtering af cytotoksiske stoffer |

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for fuldstændig sikkerhedsinformation. Fuldstændige danske/EMA-advarsler, kontraindikationer og lægemiddelinteraktionsdata var ikke tilgængelige i denne bevis-pakke.

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Rationalet:**
TxGNN-forudsigelsens toprangering — Gingivalt fibromatose (score 99.89%) — vurderes som **et farmakologiovervågnings-drevet falsk-positivt signal**. Gingivalhyperplasi er en kendt uønsket bivirkning af EGFR-TKI'er; modellen har sandsynligt fortolket denne lægemiddel-sygdom-co-forekomst som et terapeutisk signal. Ingen mekanistisk rationalet, ingen kliniske forsøg og ingen understøttende litteratur eksisterer for denne indikation. Gefitinib er heller ikke markedsført i Danmark (0 tilladelser), hvilket udgør en yderligere regulatorisk barriere for enhver klinisk brug.

**For at fortsætte med yderligere evaluering kræves følgende:**

- **Diskvalificering eller bekræftelse af dette signal:** En målrettet litteraturgennemgang af EGFR-signalerings biologi i gingivalt fibromatose bør gennemføres før eventuelle yderligere udviklingsstrin; den nuværende forventning er formel diskvalificering.
- **Lukning af MOA-datakløft:** Hent fuldstændige data om mekanisme for virkning og uønsket effekt fra DrugBank (DB00317) til at understøtte fremtidige evalueringer.
- **Lukning af sikkerhedsdatakløft:** Download og parse SmPC fra EMA's produktside for at komplettere kontraindikations-, advarsels- og lægemiddelinteraktionsprofiler.
- **Overvej det signal af højere kvalitet på rang 9:** **Lungerodscarcinomer** (score 99.86%, L4 evidens, 1 kasuistik om en gefitinib super-responder) repræsenterer en mekanistisk sammenhængende repurposing-kandidat — EGFR-mutationer er udbredt i central-type lungekræft, og gefitinibs efficacy i NSCLC er understøttet af fase 3 RCT-evidens (IPASS). Dette bør være eskaleret til en formel **Forskningsspørgsmål**-fase-vurdering.
- **Regulatorisk strategi:** Hvis klinisk undersøgelse af gefitinib for enhver dansk-relevant indikation overvejes, påbegyn en dialog om navngivet patient-brug / humanitær brug med Lægemiddelstyrelsen, eller vurder berettigelse under EMA's eksisterende centraliseret godkendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

