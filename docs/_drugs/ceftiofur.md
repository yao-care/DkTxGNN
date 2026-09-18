---
layout: default
title: Ceftiofur
parent: Kun modelforudsigelse (L5)
nav_order: 99
evidence_level: L5
indication_count: 10
---

# Ceftiofur
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

# Ceftiofur: Fra veterinær bakteriel infektion til ventrikulært septum-aneurisme

---

## Resumé i én sætning

Ceftiofur er en tredjegenerations-cephalosporin-antibiotikum godkendt udelukkende til **veterinær brug** — det har ingen godkendte menneskelige indikationer og markedsføres ikke i Danmark.
TxGNN-modellen forudsiger, at det kan være relevant for **ventrikulært septum-aneurisme**, med en høj modelsikkerhedsværdi på 96.01%.
Der er dog i øjeblikket **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning, og den mekanistiske begrundelse anses for svag — denne forudsigelse er sandsynligvis et falsk positivt signal fra indirekte veje gennem vidensgrafen.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Original indikation | Veterinær brug alene — bakterielle infektioner hos husdyr (ingen godkendt menneskelig indikation) |
| Forudsagt ny indikation | Ventrikulært septum-aneurisme |
| TxGNN-forudsigelsesscore | 96.01% |
| Bevissniveau | L5 (modelforudsigelse alene — uden understøttende studier) |
| Marked i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Vent** |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanisme-handling-data ikke tilgængelige fra bevis-pakken. Baseret på kendt farmakologisk klasseinformation er Ceftiofur en tredjegenerations beta-lactam-cephalosporin-antibiotikum udviklet udelukkende til veterinærmedicin. Det virker ved at binde til penicillin-bindende proteiner (PBPs) og hæmme bakteriel cellevæggens peptidoglycan-syntese, hvorved det udøver en bakteriedødende effekt. Det bruges rutinemæssigt hos kvæg, svin og fjerkræ til infektioner i luftvejene og andre bakterielle sygdomme.

Ventrikulært septum-aneurisme er en strukturel hjertedejekt — enten medfødt eller erhvervet som følgetilstand efter infektion (f.eks. bakteriel endokarditis-relateret vævsnedbrydning). I sidstnævnte scenarie er der en indirekte teoretisk forbindelse til antibiotika-terapi under den akutte infektionsfase. Ceftiofur har dog ingen kendt mekanisme til at reparere eller ændre kardiale strukturer, og standardbehandling for bakteriel endokarditis benytter menneskegodkendte midler som penicillin G, ampicillin eller vancomycin.

Den høje TxGNN-værdi afspejler sandsynligvis en indirekte grafsti i vidensgrafen — specifikt en "bakteriel infektion → kardial patologi"-forbindelse — snarere end et autentisk Ceftiofur-specifikt terapeutisk signal. Det fuldstændige fravær af menneskelig farmakokinetik, dosering og sikkerhedsdata for denne veterinære forbindelse underminerer yderligere plausibiliteten af denne forudsigelse. Dette anses for at være en sandsynlig falsk positiv.

---

## Evidens fra kliniske forsøg

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

---

## Literaturbevis

I øjeblikket er der ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Ceftiofur har ingen markedsføringstilladelser i Danmark og er ikke registreret hos Lægemiddelstyrelsen. Det er et veterinært lægemiddel uden godkendt menneskelig indikation i nogen jurisdiktion.

---

## Sikkerhedsovervejelser

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformation.

> **Vigtig bemærkning**: Ceftiofur er et udelukkende veterinært stof. Menneskelig farmakokinetik, anbefalinger til menneskelig dosering, menneskelige toksicitetsdata og kliniske lægemiddelinteraktioner er helt fraværende. Enhver overvejelse af menneskelig brug ville kræve de novo klinisk udvikling, herunder first-in-human-studier.

---

## Konklusion og næste trin

**Beslutning: Vent**

**Begrundelse:**
Alle fem unikke forudsagte indikationer (ventrikulært septum-aneurisme, lungemitralskade, orofacial spalte-syndrom, Laubry-Pezzi-syndrom og genetisk syndromalt Pierre Robin-syndrom) er strukturelle eller medfødte tilstande, for hvilke et antibiotikum har ingen plausibel direkte terapeutisk mekanisme. Bevisniveauet er L5 på tværs af hele spektret, og Ceftiofur har ingen godkendt menneskelig brug i noget land. TxGNN-forudsigelserne i dette tilfælde vurderes som forstærkning af støj i vidensgrafen fra sjældne sygdomsknuder og indirekte infektionsrelaterede veje.

For at fortsætte ville følgende være nødvendigt — minimum:

- Bekræftelse af, at Ceftiofur ikke er udelukkende veterinært (dvs. identificering af enhver undersøgende menneskelig brugssammenhæng)
- Grundlæggende menneskelig farmakokinetik og toksikologidata (Phase 0 / first-in-human-studier)
- En troværdig mekanistisk hypotese, der forbinder beta-lactam-antibiotikum-aktivitet til de forudsagte strukturelle kardiale eller kranio-faciale tilstande
- Regulatorisk konsultation med Lægemiddelstyrelsen og EMA om vejen til genanvendelse af et veterinært lægemiddel til menneskelig brug
- Gennemgang af, om TxGNN-graftopologi i området omkring disse sygdomsknuder er tilstrækkeligt tæt til at understøtte pålidelige forudsigelser

> ⚠️ **Forskningsmæssig ansvarsfravisning**: Denne rapport er kun til forskningsreference og udgør ikke medicinsk rådgivning. Lægemiddelgenanvendelseskandidater kræver klinisk validering, før de kan anvendes i patientbehandling.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

