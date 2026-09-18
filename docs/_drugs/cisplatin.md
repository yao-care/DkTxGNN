---
layout: default
title: Cisplatin
parent: Kun modelforudsigelse (L5)
nav_order: 113
evidence_level: L5
indication_count: 0
---

# Cisplatin
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

# Cisplatin: Evaluering af lægemiddel til genbrug — Ingen TxGNN-forudsigelser tilgængelig

## Sammenfatning på en sætning

Cisplatin (DB00515) er et veletableret platinbaseret cytotoksisk kemoterapiagent, anerkendt som en hjørnesten i behandlingen af talrige solide tumorer verden over.
TxGNN-modellen genererede ingen genbrug-forudsigelser for denne kandidat i det aktuelle evidenspakke (v4, data cutoff 2026-04-05), da kritiske inputdata – herunder virkningsmekanisme og regulatoriske indikationsregistre – ikke blev hentet med succes.
Denne rapport opsummerer den aktuelle datastatus og identificerer de løsningstrin, der kræves, før en formel genbrugsevaluering kan fortsætte.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Original indikation | Ikke hentet — regulatoriske indikationsregistre mangler i det aktuelle evidenspakke |
| Forudsagt ny indikation | Ikke tilgængelig — TxGNN-modellen returnerede ingen forudsigelser |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Evidensniveau | Ikke bestemmelig |
| Dansk markedsstatus | Ikke markedsført (0 tilladelser fundet i nuværende datasæt) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Vent** |

---

## Hvorfor ingen forudsigelse er tilgængelig

TxGNN-forudsigelsespipeline'n kræver to grundlæggende inputs for at fungere: en kortlagt DrugBank-identifikator og mindst ét regulatorisk indikationsregister. For denne kandidat returnerede DrugBank-forespørgslen et vellykket match (DB00515), men alle efterfølgende inputs fejlede:

- **Virkningsmekanisme (MOA):** Ikke hentet fra DrugBank. Dette er et højtgradig datahul og forhindrer direkte den mekanistiske relevansanalyse, der understøtter modellens kandidatvurdering.
- **Godkendte indikationsregistre:** Nul poster blev fundet i det danske regulatoriske datasæt. Cisplatin er en globalt etableret platinbaseret kemoterapiagent; fraværet af nogen autoriseringsregister afspejler næsten helt sikkert en dataindsamlingsfejl snarere end et reelt fravær fra det danske marked. EMA-centraliseret godkendelse for cisplatin-indeholdende produkter bør kunne verificeres gennem Laegemiddelstyrelsen' produktdatabase.
- **Sikkerhedsadvarsler og kontraindikationer:** Ikke hentet fra den regulatoriske kilde, hvilket forhindrer S1-sikkerhedsforscreening-trinnet.

Indtil disse tre datahul løses, kan ingen mekanistisk begrundelse eller evidensvurdering formelt vurderes.

---

## Cytotoksicitet

Baseret på DrugBank-klassificering (DB00515) og etableret farmakologisk klasse er Cisplatin utvetydigt en antineoplastisk cytotoksisk agent, der tilhører platinkoordinationskomplekserne.

| Element | Indhold |
|---------|---------|
| Klassificering af cytotoksicitet | Konventionel cytotoksisk — Platinkoordinationskompleks |
| Risiko for myelosuppression | Høj — leukopeni, trombocytopeni og anæmi er veldokumenterede dosisbegrænsende toksiciteter |
| Klassificering af emetogenicitet | Høj — cisplatin klassificeres som højt emetogent; profylaktisk antiemetisk terapi (5-HT₃-antagonist + NK₁-antagonist + dexamethason) er obligatorisk |
| Overvågningselementer | Fuldt blodtal (med differential), serum kreatinin og eGFR (nefrotoksicitet er en primær dosisbegrænsende toksicitet), serum-elektrolytter (Mg²⁺, K⁺, Na⁺, Ca²⁺), audiometri (ototoksicitetsovervågning), urinalyse |
| Håndteringsbeskyttelse | Skal håndteres i overensstemmelse med regler for håndtering af cytotoksiske lægemidler; kræver passende personlige værnemidler, dedikeret præparationsområde (laminært flowbord) og cytotoksisk affaldsbehandlingsprocedurer |

---

## Sikkerhedsmæssige hensyn

Se venligst den godkendte produktkarakteristika-oversigt (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Vent**

**Begrundelse:**
TxGNN-modellen kunne ikke generere genbrug-forudsigelser for Cisplatin, fordi de to blokerende datahul – manglende data om virkningsmekanisme og fraværet af nogen regulatorisk indikationsregister – forhindrede pipeline'n i at producere en kandidat, der kunne bedømmes. Ingen evidenstabel eller mekanistisk vurdering kan færdiggøres i den nuværende tilstand.

**For at fortsætte er følgende nødvendigt:**

- **[Blokering]** Hent godkendt indikations-, advarsels- og kontraindikationsdata ved at downloade og parse SmPC-PDF fra Det Danske Lægemiddelagentur (Laegemiddelstyrelsen) — påkrævet for S1-sikkerhedsforscreening
- **[Høj]** Forespørg DrugBank API direkte for DB00515 for at få virkningsmekanismen — påkrævet for mekanistisk relevansanalyse
- **[Høj]** Bekræft dansk markedsstatus: Cisplatin har længe været tilgængelig som standard kemoterapiagent på tværs af EU; resultatet nul-autorisationer bør undersøges som et sandsynligt dataindsamlingsproblem, før der drages nogen regulatorisk konklusion
- **[Opfølgning]** Kør det komplette TxGNN-forudsigelsespipeline igen, når fuldstændige inputdata er tilgængelige, og gen-udsted dette evidenspakke

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

