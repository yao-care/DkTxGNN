---
layout: default
title: Miglustat
parent: Kun modelforudsigelse (L5)
nav_order: 556
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Miglustat: forudsagt ny indikation Autosomal ichthyose-syndrom med dødeligt forløb (evidensniveau L5). Oprindelig indikation: Gauchers sygdom, Niemann-Pick-sygdom"
monitor_inn: "Miglustat"
predicted_indications: ["autosomal ichthyosis syndrome with fatal disease course", "autosomal ichthyosis syndrome with fatal disease course", "cholesteryl ester storage disease", "cholesteryl ester storage disease", "Krabbe disease", "Krabbe disease", "metachromatic leukodystrophy", "metachromatic leukodystrophy", "Wolman disease with hypolipoproteinemia and acanthocytosis", "Wolman disease with hypolipoproteinemia and acanthocytosis"]
---

# Miglustat
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

## Miglustat: Fra Gauchers sygdom til autosomal ichthyose-syndrom med dødeligt forløb
{: .text-alpha }

## Resumé i én sætning

Miglustat er en hæmmer af glucosylceramidsyntase, som oprindeligt anvendes til behandling af Gauchers sygdom og Niemann-Pick-sygdom.
TxGNN-modellen forudsiger, at det kan være virksomt ved **autosomal ichthyose-syndrom med dødeligt forløb**,
men der er på nuværende tidspunkt **ingen kliniske forsøg** og **ingen publikationer**, der understøtter forudsigelsen. Den er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Gauchers sygdom, Niemann-Pick-sygdom (den danske godkendelse har ingen angivet indikationstekst i de indsamlede data) |
| Foreslået ny indikation | Autosomal ichthyose-syndrom med dødeligt forløb |
| TxGNN-forudsigelsesscore | 99,83 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de indsamlede data. Miglustat er dog kendt som en hæmmer af glucosylceramidsyntase (UGCG), og princippet kaldes substratreduktionsterapi: syntesen af glykosfingolipider nedsættes, så mængden af ophobet substrat falder.

Svære ichthyose-syndromer indebærer forstyrret metabolisme af lipider og ceramider i overhuden. Det er derfor biologisk plausibelt, at en modulering af glykosfingolipidsyntesen kan have betydning. Forbindelsen til den oprindelige indikation er den fælles lipidmetaboliske tematik.

Forudsigelsen er dog alene beregningsmæssig. Sygdomsposten optræder desuden to gange i inputtet og er ikke klart defineret, så den skal dedupliceres og afklares i forhold til sygdomsontologien, før der arbejdes videre.

### Øvrige forudsigelser af interesse

Modellen forudsiger også følgende sygdomme, alle med evidensniveau L5 og uden kliniske forsøg eller publikationer:

| Sygdom | TxGNN-score | Mekanistisk vurdering |
|------|------|------|
| Cholesterylester-lagringssygdom | 99,82 % | Indirekte forbindelse via lysosomal lagringspatologi. Enzymerstatning (sebelipase alfa) er allerede en etableret og mekanisme-matchet behandling. |
| Krabbes sygdom | 99,78 % | Delvis mekanistisk overlap. Miglustats målenzym ligger ikke på galactosylceramid-/psykosinvejen. |
| Metakromatisk leukodystrofi | 99,77 % | Indirekte forbindelse. Sulfatidsyntesen deler opstrøms galactosylceramidveje og ikke glucosylceramidvejen. |
| Wolmans sygdom med hypolipoproteinæmi og akantocytose | 99,76 % | Indirekte forbindelse. Sygdomsbetegnelsen er sammensat, hvilket tyder på en fejl i ontologikortlægningen. |

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105309513 | Miglustat "Bluefish" (Bluefish Pharmaceuticals AB) | Kapsler, hårde | Indikationstekst ikke angivet i de indsamlede data |

---

## Sikkerhedsmæssige overvejelser

- **Kontraindikationer/risici fra vidensgraf (ikke præparatomtale):** Vidensgrafen (PrimeKG) knytter miglustat til sygdomme i det perifere nervesystem, perifer neuropati og nedsat nyrefunktion.
- **Lægemiddelinteraktioner:**
  - **Imiglucerase**: moderat interaktion (kilde: DDInter).
  - **UDP-glucose-ceramid-glucosyltransferase (UGCG)**: dette er lægemidlets farmakologiske mål og ikke en klassisk interaktion.

Kontrollér i øvrigt den godkendte produktresumé (SmPC) for yderligere sikkerhedsoplysninger, da advarsler og kontraindikationer fra produktresuméet ikke indgår i de indsamlede data.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en modelscore uden understøttende kliniske forsøg eller litteratur (evidensniveau L5). Sygdomsposten er desuden duplikeret og uklart defineret, og data om virkningsmekanisme og produktresumé mangler.

**For at komme videre er følgende nødvendigt:**
- Deduplikering og afklaring af sygdomsdefinitionen i sygdomsontologien
- Systematisk litteratur- og forsøgssøgning for miglustat og ichthyose-syndromer
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Advarsler og kontraindikationer fra den danske produktresumé (SmPC) hos Lægemiddelstyrelsen
- Prækliniske data, der understøtter effekt på epidermal ceramid- og lipidmetabolisme
- Vurdering af sikkerhed, særligt perifer neuropati og nyrefunktion
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

