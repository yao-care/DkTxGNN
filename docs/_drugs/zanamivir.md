---
layout: default
title: Zanamivir
parent: Kun modelforudsigelse (L5)
nav_order: 476
evidence_level: L5
indication_count: 10
---

# Zanamivir
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

# Zanamivir: Fra influenza til pyelonephritis

## Enlinies resumé

Zanamivir er en antiviral neuraminidasehæmmer, der er internationalt godkendt til behandling og forebyggelse af influenza A og B.
TxGNN-modellens højest rangerede forudsigelse foreslår mulig relevans til **Pyelonephritis**, men dette er et **kun model-baseret (L5)** signal —
der er **ingen understøttende kliniske forsøg og ingen understøttende litteratur**, og bevissamlingen's egen mekanistisk gennemgang finder ingen troværdig farmakologisk grundlag for forbindelsen.

---

## Hurtig oversigt

| Element | Indhold |
|---|---|
| Oprindelig indikation | Ikke dokumenteret i danske licensdata (ingen markedsføringstilladelser registreret); Zanamivir er internationalt indiceret til behandling og profylakse af influenza A/B |
| Forudsagt ny indikation | Pyelonephritis |
| TxGNN-forudsigelsesscore | 99.84% |
| Bevisgrad | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Formelle virkningsmekanisme-data var ikke tilgængelige i denne bevissamling (datagap på medicinal-niveau, markeret som høj alvorlighed i kildemetadata). Baseret på etableret farmakologi er zanamivir en inhalativ neuraminidasehæmmer, der blokerer influenzavirusens overfladeglykoproteinneuroaminidase, hvilket forhindrer frigivelse af nye viruspartikler fra inficerede respiratoriske epitelceller. Dets godkendte anvendelse er snævert begrænset til influenza A og B.

Modellens højest rangerede nye indikation, **Pyelonephritis**, er en bakteriel øvre urinvejsinfektion. Der er ingen overlap mellem bakteriel infektionspatofysiologi og antiviral neuraminidasehæmning, og der er ikke dokumenteret nogen antibakteriel aktivitet for zanamivir. Bevissamlingen's egen mekanistisk-link-vurdering for denne kandidat konkluderer eksplicit, at der ikke er nogen troværdig farmakologisk forbindelse.

De resterende model-markerede kandidater — forstyrrelser i tyrosin- og fenylalaninmetabolisme, tetrahydrobiopterin-responsiv phenylketonuri og teratogen Pierre Robin-syndrom — er alle medfødte metabolske eller kraniofaciale udviklingsforstyrrelser, hvoraf ingen har nogen kendt biokemisk sammenhæng med neuraminidasehæmning. Bemærkelsesværdigt blev de tre litteraturhenvisninger hentet under "forstyrrelser i tyrosinmetabolisme" alle vedrørende oseltamivir/zanamivir antivirale **resistensmutationer** (f.eks. H275Y / H274Y neuraminidaseerstatningerne) — mutationsnomenklaturen refererer tilfældigvis til en tyrosin/histidin-substitution, som ser ud til at have udløst et falsk tekstmatchende link i vidensgraf snarere end at afspejle ægte terapeutisk relevans. Dette tolkes bedst som en **falsk positiv vidensgraf** snarere end som understøttende bevis.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede registrerede kliniske forsøg.

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig for den højest rangerede kandidatindikation (Pyelonephritis).

*(Bemærk: 3 publikationer blev hentet under en lavere-rangeret kandidat, "forstyrrelser i tyrosinmetabolisme," men efter gennemgang vedrører disse antivirale resistensmutationsnomenklaturen, ikke selve metabolske forstyrrelser — se begrundelse ovenfor.)*

---

## Markedsinformation for Danmark

Ingen markedsføringstilladelser er i øjeblikket registreret for zanamivir i Danmark (Markedsstatus: **Ikke markedsført**; Samlede licenser: **0**). Dette lægemiddel har i øjeblikket ikke en registreret tilstedeværelse på det danske marked.

---

## Sikkerhedshensyn

Se venligst det godkendte produktsammenfatting (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Alle forudsagte indikationer for zanamivir i denne bevissamling understøttes kun på model-forudsigelsesniveauet (L5), uden kliniske forsøg og uden ægte relevant litteratur. Top-kandidaten (Pyelonephritis) og alle andre kandidater mangler enhver troværdig mekanistisk rationale, der forbinder en antiviral neuraminidasehæmmer til deres respektive sygdomsbiologi, og et litteratursignal blev identificeret som en falsk positiv vidensgraf.

**For at gå videre er følgende nødvendigt:**
- Bekræftet virkningsmekanisme-data for zanamivir (DrugBank API-forespørgsel — i øjeblikket et datagap)
- SmPC/produktinformation-advarsler og kontraindikationer (Dansk lægemiddelagentur-kilde — i øjeblikket et blokerende datagap for sikkerhedsscreening)
- Uafhængig (ikke-TxGNN-udløst) hypotesegenerering eller målrettet litteratur-/forsøgssøgning specifik til pyelonephritis før yderligere evaluering
- Revurdering af, hvorvidt disse kandidater skal forblive i den aktive pipeline, givet fraværet af et plausibelt mekanistisk grundlag

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

