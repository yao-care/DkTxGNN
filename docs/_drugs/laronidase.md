---
layout: default
title: Laronidase
parent: Høj evidens (L1-L2)
nav_order: 255
evidence_level: L2
indication_count: 10
---

# Laronidase
{: .fs-9 }

Evidensniveau: **L2** | Forudsagte indikationer: **10** stk.
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

# Laronidase: Fra Mukopolysaccharidose I til Lysosomale Lagringssygdomme med Skeletbetonet Involvering

## Ét-linie Sammenfatning

Laronidase er en rekombinant human alfa-L-iduronidase enzymerstattningsterapi, oprindeligt udviklet til **Mukopolysaccharidose I (MPS I; Hurler / Hurler-Scheie / Scheie syndrom)** — selvom denne evidenspakke har et tomt `original_indications`-felt, bliver denne indikation udledt fra pakkens egen mekanistiske rationale og litteratur, ikke bekræftet af en regulatorisk kilde. TxGNNs topforudsigelse, **lysosomale lagringssygdomme med skeletbetonet involvering**, er i praksis en bredere ontologietiket for den samme underliggende sygdom, som lægemidlet allerede behandler, snarere end en genuint ny indikation. Evidensstøtten er moderat: **4 publikationer** (ingen registrerede kliniske forsøg) på evidensniveau **L2**.

---

## Hurtig Oversigt

| Post | Indhold |
|------|---------|
| Original Indikation | Mukopolysaccharidose I (Hurler / Hurler-Scheie / Scheie syndrom) — ikke til stede i denne pakkes `original_indications`/licensdata; udledt fra evidenspakkens egen rationaletekst |
| Forudsagt Ny Indikation | Lysosomale lagringssygdomme med skeletbetonet involvering |
| TxGNN Forudsigelsesscore | 99.31% |
| Evidensniveau | L2 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal Markedsføringstilladelser | 0 |
| Anbefalet Afgørelse | Fortsæt med Sikkerhedsforanstaltninger |

---

## Hvorfor er denne Forudsigelse Rimelig?

I øjeblikket er detaljerede mekanisme-for-handling-data ikke tilgængelig i denne evidenspakke (markeret som en datakløft med høj alvorlighed, DG002). Baseret på de tilgængelige oplysninger er Laronidase en rekombinant form af human alfa-L-iduronidase, det lysosomale enzym, der er defekt i MPS I. Dets efficacitet inden for enzymerstattningsterapi til MPS I er etableret gennem årtiers klinisk brug, og mekanistisk strækker denne aktivitet sig direkte til enhver tilstand defineret ved alfa-L-iduronidase-mangel og den resulterende glycosaminoglycanudsendelse (GAG) akkumulering i knogle og bindevæv.

Vigtigst er det, at pakkens egen `repurposing_rationale` for denne toprangerede forudsigelse angiver, at "lysosomale lagringssygdomme med skeletbetonet involvering" meget sandsynligt er den samme sygdom som MPS I, blot fanget under et bredere/anderledes ontologieterm — TxGNN-kandidaten, der blev afgrænset her, kom hovedsagelig til syne, fordi lægemidlets *oprindelige* indikation ikke blev udfyldt i dette datasæt. Med andre ord bør dette læses som **evidens, der bekræfter en allerede kendt brug**, ikke som en ny repurposingtilgang. En ægte vurdering af ny indikation ville kræve at genafvikle denne analyse med `original_indications` korrekt udfyldt, således at TxGNN-kandidater filtreres mod det sande label-sæt.

For transparens: de resterende kandidater i denne pakke (Sanfilippo-syndrom, lysosomale sygdomme med hypertrofisk kardiomyopati, syndromisk neurometabolsk sygdom med X-bundet intellektuel handicap, øjenlågenes fejlposition) blev alle scoret **L4–L5 med anbefaling om tilbageholdelse**. Flere viser evidensmismatch — f.eks. er litteraturen om Sanfilippo-syndrom, der blev returneret af pipelinen, faktisk MPS I-litteratur, mest sandsynligt på grund af nøgleordoverlap på "mukopolysaccharidose" snarere end ægte faglig relevans — og kandidaterne for X-bundet og hypertrofisk-kardiomyopati mangler et plausibelt genetisk/mekanistisk grundlag. Ingen af disse understøtter yderligere handling på dette tidspunkt.

---

## Evidens fra Kliniske Forsøg

Ingen relaterede kliniske forsøg er i øjeblikket registreret.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtigste Fund |
|------|-----|------|-----------|----------------|
| [23127271](https://pubmed.ncbi.nlm.nih.gov/23127271/) | 2012 | Kohorte/Kasusserie | Pediatric Neurology | 6,5-årig opfølgning af enzymerstattningsterapi i et attenueret MPS I-tilfælde (Scheie-syndrom); dokumenterede skelet-, hjerte- og øjenresultater over langtidsbehandling |
| [25345091](https://pubmed.ncbi.nlm.nih.gov/25345091/) | 2014 | Oversigt | Pediatric Endocrinology Reviews | Oversigt over MPS I-sygdomsspektrum (Hurler / Hurler-Scheie / Scheie), diagnose via urin-GAG-mønster og iduronidase-enzymassay |
| [18758061](https://pubmed.ncbi.nlm.nih.gov/18758061/) | 2008 | In vitro (basisk forskning) | Biological & Pharmaceutical Bulletin | Demonstrerede mannose-6-phosphat-receptor-formidlet optagelse af laronidase af MPS I-fibroblasten og osteoblaster, med lysosomalt procesering og substratspaltning |
| [12196045](https://pubmed.ncbi.nlm.nih.gov/12196045/) | 2002 | Oversigt | BioDrugs | Tidlig udviklingsoversigt af laronidase som rekombinant alfa-L-iduronidase ERT til MPS I, inklusiv orphan-drug-udpegning og fase I-forsøgsdata |

---

## Markedsinformation for Danmark

Laronidase har i øjeblikket ingen markedsføringstilladelse registreret i Danmark (0 tilladelser på fil; markedsstatus: Ikke markedsført).

---

## Sikkerhedsmæssige Overvejelser

Se venligst det godkendte Produktresumésamandrag (SmPC) for sikkerhedsinformation. Denne evidenspakke indeholder ikke TFDA/Laegemiddelstyrelsen-advarsels- eller kontraindikationsdata (markeret som en blokerande datakløft, DG001), og der blev ikke fundet nogen lægemiddelinteraktionsposter.

---

## Konklusion og Næste Trin

**Afgørelse: Fortsæt med Sikkerhedsforanstaltninger**

**Begrundelse:**
Det underliggende evidensniveau (L2, understøttet af MPS I-litteratur) er rimeligt solidt, men denne "nye indikation" synes at overlapse væsentligt med Laronidases allerede kendt brug snarere end at repræsentere en genuint ny repurposingtilgang. Kombineret med de manglende sikkerhedsdata/label-data, skal dette ikke behandles som en grøn lys-sag.

**For at fortsætte er følgende nødvendigt:**
- Løs DG001 (Blokering): indhent det godkendte SmPC/produktadvarsler og kontraindikationer, før nogen sikkerhedsvurdering (S1) kan fortsætte
- Løs DG002: indhent bekræftede mekanisme-for-handling- og oprindelig-indikationsdata fra DrugBank/regulatoriske kilder for at fastslå, om "lysosomale lagringssygdomme med skeletbetonet involvering" virkelig er en ny indikation eller en genmærkning af MPS I
- Hvis en genuint ny indikation er målsætningen, kør TxGNN-kandidatgeneringen igen med et korrekt udfyldt `original_indications`-felt, så overlappinger af eksisterende brug filtreres ud
- Da der er nul markedsføringstilladelser i Danmark, bekræft import-/navnpatient-brug-vejledningsstatus, før nogen klinisk overvejelse

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

