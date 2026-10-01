---
layout: default
title: Polatuzumab Vedotin
parent: Kun modelforudsigelse (L5)
nav_order: 356
evidence_level: L5
indication_count: 10
---

# Polatuzumab Vedotin
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

# Polatuzumab vedotin: Fra B-celle-rettet antistof-lægemiddelkonjugat til HER2-positivt brystkarcinom

## Resumé i få sætninger

Polatuzumab vedotin er et antistof-lægemiddelkonjugat, der rettes mod CD79b på B-celler og afleverer det mikrotubuli-hæmmende stof MMAE. Datagrundlaget angiver ingen registreret oprindelig indikation.

TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **HER2-positivt brystkarcinom**. Forudsigelsen understøttes af **0 kliniske forsøg** og **0 relevante publikationer**, og den er derfor ren modelforudsigelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | HER2-positivt brystkarcinom |
| TxGNN-forudsigelsesscore | 99,34 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Polatuzumab vedotin binder CD79b, en del af B-cellereceptoren, og leverer MMAE, som hæmmer mikrotubuli. CD79b findes kun på B-cellelinjen og er ikke et etableret mål ved HER2-positivt brystkarcinom. Der er heller ikke påvist CD79b-ekspression i brysttumorer af andre subtyper.

Den høje score på 0,993 skyldes sandsynligvis nærhed i videnskortet (knowledge graph) og generel forbindelse til onkologiske lægemidler. Mekanistisk understøttes den ikke. Den eneste tænkelige forbindelse er den uspecifikke cytotoksiske virkning af MMAE. Det er en klasseeffekt for nyttelasten og ikke en begrundelse, der er specifik for dette lægemiddel.

Detaljerede data om virkningsmekanisme og oprindelig indikation mangler i datagrundlaget, så forudsigelsen kan ikke krydstjekkes mod lægemidlets kendte anvendelse.

### Øvrige forudsigelser

Modellen foreslår også andre brystkræftsubtyper. Alle har evidensniveau L5, beslutningen Hold og ingen kliniske forsøg. Hver indikation optræder to gange i rådata og er her kun vist én gang.

| Forudsagt indikation | Score | Bemærkning |
|------|------|------|
| Normal-like subtype af brystkarcinom | 98,91 % | Ingen kendt CD79b-ekspression |
| Progesteronreceptor-positiv brystkræft | 98,91 % | Ingen kendt sammenhæng med CD79b-rettet behandling |
| Luminal A- eller B-brysttumor | 98,89 % | 19 hentede publikationer er irrelevante (se nedenfor) |
| Progesteronreceptor-negativ brystkræft | 98,86 % | Ingen mekanistisk eller klinisk sammenhæng |

---

## Klinisk evidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der foreligger i øjeblikket ingen relateret litteratur for den primære forudsigelse (HER2-positivt brystkarcinom).

Søgningen for "luminal A- eller B-brysttumor" returnerede 19 publikationer. De ser ud til at være søgeartefakter på bogstavet "B", fx B-cellebiologi, hepatitis B-vacciner, HLA-B og bakteriochlorofyl b. Ingen af dem omhandler polatuzumab vedotin, CD79b, MMAE eller brystkræft, og de er derfor ikke medtaget som evidens.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Indehaver |
|---------|------|------|-----------|
| 28106216319 | Polivy | Pulver til koncentrat til infusionsvæske, opløsning | Roche Registration GmbH |

Godkendt indikationstekst er ikke angivet i datagrundlaget.

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling: antistof-lægemiddelkonjugat med cytotoksisk nyttelast (MMAE, mikrotubuli-hæmmer) |
| Risiko for myelosuppression | Se produktresuméet (SPC). Knogemarvspåvirkning er en forventelig klasseeffekt for MMAE-konjugater |
| Emetogenicitetsklassifikation | Se produktresuméet (SPC) |
| Monitoreringspunkter | Se produktresuméet (SPC). Typisk komplet blodtælling samt lever- og nyrefunktion |
| Håndteringsbeskyttelse | Følg gældende regler for håndtering af cytotoksiske lægemidler |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SPC) for sikkerhedsoplysninger. Der er ikke fundet data om advarsler, kontraindikationer eller interaktioner i datagrundlaget.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende baseret på en modelscore uden kliniske forsøg, relevant litteratur eller mekanistisk understøttelse. CD79b er ikke et etableret mål ved HER2-positivt brystkarcinom. Evidensniveauet er L5, og sikkerhedsdata mangler.

**For at komme videre kræves:**
- Hentning af produktresumé fra Lægemiddelstyrelsen med advarsler og kontraindikationer. Dette blokerer sikkerhedsscreeningen.
- Oplysninger om oprindelig indikation og virkningsmekanisme (fx via DrugBank).
- Præklinisk dokumentation for CD79b-ekspression eller anden målrelevans i brystkræftvæv.
- En målrettet litteratur- og forsøgssøgning med polatuzumab vedotin, CD79b og MMAE kombineret med brystkræft.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

