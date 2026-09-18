---
layout: default
title: Vonicog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 474
evidence_level: L5
indication_count: 10
---

# Vonicog Alfa
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

# Vonicog Alfa: Fra von Willebrands sygdom til primær frigivelsesforstyrrelse af blodplader

## Et-sætnings sammenfatning

> Vonicog Alfa (rekombinant von Willebrands faktor, rVWF) er et biologisk lægemiddel til faktorerstatning, hvis etablerede indikation — som afspejlet i de kliniske forsøgs- og litteraturregistre, der indgår i denne bevissamling — er behandling af alvorlig von Willebrands sygdom (VWD).
> TxGNN-modellens højest rangerede prognose er **Primær frigivelsesforstyrrelse af blodplader**, men denne kombination understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer**, og modellens egen mekanistiske analyse flaggerer det som et sandsynligt vidensgraf-topologi-artefakt snarere end et farmakologisk begrundet signal.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Von Willebrands sygdom (VWD) — afledt fra den kliniske forsøgs-/litteraturkontekst, der indgår i denne samling; ingen formel dansk etiketttekst er tilgængelig (se Datakløfter nedenfor) |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader (blodplatelet granula sekretion / lagerbeholder defekt) |
| TxGNN-prognosescore | 99.98% |
| Bevisniveau | L5 |
| Markeds status i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne prognose rimelig?

I øjeblikket er detaljerede virkningsmekanisme-data for Vonicog Alfa ikke tilgængelige i denne bevissamling (flagget som en høj-alvorligheds datakløft). Baseret på de oplysninger, der er tilgængelige, er Vonicog Alfa en rekombinant form af von Willebrands faktor (rVWF), hvis påvist rolle er at genoprette VWF-medieret blodplatelet **adhesion** (via GPIb-receptoren) og stabilisere cirkulerende Faktor VIII hos patienter med von Willebrands sygdom.

Primær frigivelsesforstyrrelse af blodplader derimod er en forstyrrelse af blodplatelet **sekretion** — en defekt i frigivelsen af tætte eller alfa-granula efter blodplatelet aktivering. Dette er et mekanistisk adskilt trin i hemostase fra VWF-medieret adhesion, og erstatning af VWF behandler ikke en granula-frigivelses defekt. Rationaleteksten, der ledsager denne prognose, angiver eksplicit, at der ikke eksisterer en direkte farmakologisk forbindelse mellem de to, og foreslår, at den meget høje TxGNN-score mere sandsynligt afspejler topologisk nærhed mellem "blodplatelet funktionsforstyrrelse" sygdomsknuder og VWF-knuden i visdensgrafen, snarere end ægte mekanistisk relevans.

I overensstemmelse hermed blev der ikke hentet nogen kliniske forsøgs- eller litteraturregistre for dette lægemiddel-sygdoms par (0 resultater på tværs af ClinicalTrials.gov, ICTRP og PubMed-forespørgsler). Denne prognose bør derfor behandles som et model output med lav troværdighed, der kræver mekanistisk præcisering, før enhver yderligere evaluering.

---

## Klinisk forsøgsbeviser

Der er i øjeblikket ingen relaterede registrerede kliniske forsøg.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markeds information for Danmark

Vonicog Alfa er i øjeblikket **ikke markedsført** i Danmark, med **0 markedsføringstilladelser** på rekord (ingen nationale Lægemiddelstyrelsen- eller centraliserede EMA-licenser fundet i denne bevissamling).

---

## Sikkerhedshensyn

Se venligst den godkendte produktinformationsdokumentet (SmPC) for sikkerhedsoplysninger.

*Bemærk: TFDA/Danske etiketadvarsler og kontraindikationer for dette lægemiddel var ikke tilgængelige på tidspunktet for denne evaluering (Blokering datakløft — `DG001`), hvilket betyder, at en fuld sikkerhed (S1) vurdering ikke kunne gennemføres.*

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
- Den højest rangerede forudsagte indikation (Primær frigivelsesforstyrrelse af blodplader) har ingen understøttende kliniske forsøgs- eller litteraturbeviser (Bevisniveau L5, Beslutningsstade S0), og den mekanistiske begrundelse selv konkluderer, at VWF-erstatning ikke plausibelt behandler en blodplatelet granula-frigivelses defekt.
- Lægemidlet er ikke i øjeblikket markedsført i Danmark, og virkningsmekanisme- og sikkerhed/etiketdata (advarsler, kontraindikationer) mangler begge — sidstnævnte er en Blokering-alvorligheds kløft, der forhindrer enhver foreløbig sikkerhedsvurdering.

**For at fortsætte kræves følgende:**
- Bekræftet virkningsmekanisme data for Vonicog Alfa (DrugBank API-forespørgsel, pr. `DG002`)
- TFDA/Danske SmPC advarsler og kontraindikationer (pr. `DG001`, Blokering)
- Uafhængig mekanistisk eller præ-klinisk evidens direkte forbindende VWF-erstatning til blodplatelet sekretion/lagerbeholder forstyrrelser
- Præcisering af, hvordan TxGNN-visdensgrafen kortlægger sygdoms-ontologi-termer (for at bekræfte, at dette ikke er et topologisk artefakt snarere end et ægte signal)
- Som en separat efterforskningslinje: "hæmofili" kandidaten i denne bevissamling (Bevisniveau L2, 4 fase 3-forsøg + 5 publikationer) berettiger til sin egen dedikerede evaluering, selvom disse forsøg rekrutterede von Willebrands sygdoms patienter snarere end klassisk hemofili A/B patienter — sygdoms-etiket kortlægningen bør verificeres før behandling af den som direkte hemofili-beviser.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

