---
layout: default
title: Agalsidase Beta
parent: Kun modelforudsigelse (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
---

# Agalsidase Beta
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

# Agalsidase Beta: Fra Fabrys sygdom til cervikalt neuroblastom

## Resumé i én sætning

Agalsidase beta (Fabrazyme) er et rekombinant humant α-galactosidase A-enzym, der bruges som enzymerstattningsterapi (ERT) til Fabrys sygdom, en sjælden X-koblet lysosomalt lageringstilstand, der forårsager progressiv Gb3-akkumulering i vitale organer. TxGNN-modellen forudsiger, at det kan være effektivt mod **cervikalt neuroblastom** med en forudsigelsesscore på 98.37 %; dog er **ingen kliniske forsøg eller understøttende publikationer** blevet identificeret for denne indikation. Som en vigtig bekymring deler alle højest-rangerede forudsigelser næsten-identiske scores og klynger udelukkende blandt hoved-/hals- og mundhuletumorer — hvilket kraftigt tyder på en systematisk modelbias snarere end et ægte ombrugssignal.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|---------|
| Original indikation | Fabrys sygdom (α-galactosidase A-mangel / lysosomalt lageringstilstand) — *baseret på almen farmaceutisk viden; officielle indikationsdata ikke tilgængelige i denne bevissamling* |
| Forudsagt ny indikation | Cervikalt neuroblastom |
| TxGNN forudsigelsesscore | 98.37 % |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 |
| Anbefalet beslutning | **Afvent** |

---

## Hvorfor er denne forudsigelse rimelig?

Agalsidase beta er en rekombinant form af humant α-galactosidase A-enzym, administreret intravenøst som enzymerstattningsterapi. Ved Fabrys sygdom forårsager arvelig mangel på dette lysosomale enzym progressiv akkumulering af globotriaosylceramid (Gb3) i hele kroppen — primært beskadiger det nyrerne, hjertet og det perifere nervesystem. Ved at levere funktionelt enzym reducerer agalsidase beta Gb3-aflejringer og bremser organdegeneration.

Cervikalt neuroblastom er en ondartet tumor, der stammer fra neural crest-celler, typisk behandlet med kemoterapie, immunoterapi og stråling. Selvom spredt forskning har bemærket Gb3-overekspression i visse tumortyper, er der **ingen offentliggjort evidens for Gb3-overekspression specifikt ved cervikalt neuroblastom**. Mere fundamentalt er agalsidase betas mekanisme at *nedbryde* akkumuleret Gb3 — det virker ikke som en målrettet antineoplastisk agent, der udnytter Gb3-overekspression. Som et højtmolekylært proteinlægemiddel er det også usandsynligt, at det vil trænge ind i et tumorsmikromiljø ved neuroblastom via intravenøs administration. Der er derfor ingen klart artikulerbar mekanistisk vej, der forbinder agalsidase beta med anti-tumor-aktivitet ved denne indikation.

Et kritisk mønster går gennem alle 10 forudsigelser i denne bevissamling: hver rangeret kandidat er en hoved-/hals- eller mundhuletumor, poster vises i duplikater (rank 1–2 identiske, 3–4 identiske osv.), og forudsigelsesscorene klynger inden for et område på mindre end 0.001 (0.9831–0.9837). Dette er et lærebogeksempel på **TxGNN-klyngerbias**, hvor modellen genererer falske forudsigelser baseret på delt ontologisk nærhed inden for vidensgrafen snarere end ægte biologisk rimelighed. Modelrekalibrering og validering mod et uafhængigt benchmarkværktøj anbefales kraftigt før tegning af nogen klinisk slutning fra disse resultater.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidence

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

> **Bemærkning:** Agalsidase beta er markedsført i Europa som Fabrazyme (centraliseret EMA-godkendelse). SmPC er offentligt tilgængeligt via [EMA-produktsiden](https://www.ema.europa.eu/en/medicines/human/EPAR/fabrazyme) og indeholder fulde advarsler, kontraindikationer og vejledning til infusionsrelaterede reaktioner.

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Begrundelse:**
TxGNN-forudsigelserne for agalsidase beta er helt ustyrkede af kliniske eller prekliniske beviser (bevisniveau L5 på tværs af alle rangerede indikationer), og den foreslåede mekanistiske forbindelse mellem en intravenøs ERT til et lysosomalt lageringstilstand og hoved-/halskræft er biologisk urimelig. De næsten identiske forudsigelsesscorer på tværs af fem forskellige tumortyper — hver vises i duplikater — udgør stærk evidens for en systematisk modelartefakt, der bør behandles, før nogen yderligere evaluering af disse kandidater.

**For at fortsætte, er følgende nødvendigt:**

- **Modeltilsyn først:** Undersøg TxGNN-klyngerbias for ERT-klasse makromolekyler; hvis det bekræftes, skal disse forudsigelser filtreres ud eller ned-vægtlægges på pipelinieniveauet
- **MOA-datahentning:** Hent fuldt virkningsmekanisme og farmakologisk profil fra DrugBank (DB00103) for at muliggøre ordentlig biologisk rimeligheds-scoring i fremtidige kørsler
- **Regulatorisk basislinje:** Hent Fabrazymes EMA SmPC for fulde sikkerhedshensyn, kontraindikationshensyn og advarselsdata for at fuldføre S1-sikkerhedsvurderingen
- **Omdirigeret ombrugsmål:** Hvis ombrug ud over Fabrys sygdom er af ægte interesse for agalsidase beta, fokuser fremtidige søgninger på sygdomme med dokumenteret lysosomalt dysfunktion, sfingolipiddysregulering eller Gb3-akkumulering (f.eks. visse hypertrofisk kardiomyopatier, kronisk nyresygdom med podicyt-involvering) snarere end solide tumorer
- **Danmark-specifikt trin:** Bekræft, om en centraliseret EMA-markedsføringsgodkendelse for Fabrazyme kunne tjene som regulatorisk grundlag for en udvidet indikationsansøgning, hvis fremtidigt evidens berettiger det

---

> ⚠️ **Ansvarsfraskrivelse:** Denne rapport er genereret til forskningsreferencebrug alene og udgør ikke medicinsk rådgivning. Alle lægemiddelombrugskandidater kræver klinisk validering før nogen terapeutisk anvendelse. Datastand: 2026-04-04.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

