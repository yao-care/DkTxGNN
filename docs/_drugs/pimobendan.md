---
layout: default
title: Pimobendan
parent: Kun modelforudsigelse (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
---

# Pimobendan
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

# Pimobendan: Fra canin kongestiv hjerteinsufficiens til blandet mineralstøvpneumokonose

## Resumé i én sætning

Pimobendan er en PDE3-inhibitor/calciumsensibilisator kendt for sine positive inotrope og vasodilatatoriske effekter ved canin kongestiv hjerteinsufficiens. TxGNN-modellens topforudsigelse er **blandet mineralstøvpneumokonose**, men denne understøttes af **0 kliniske forsøg** og **0 publikationer**, og forudsigelsesscore (50%) svarer til en ikke-informativ baselineværdi snarere end et ægte signal.

## Hurtig oversigt

| Element | Indhold |
|------|------|
| Oprindelig indikation | Ikke tilgængelig fra dansk registerdata (medicin ikke markedsført, ingen godkendt indikationstekst på arkiv). Bevispakningen's mekanistiske noter refererer til canin kongestiv hjerteinsufficiens som medicinens kendt anvendelse. |
| Forudsagt ny indikation | Blandet mineralstøvpneumokonose |
| TxGNN-forudsigelsesscore | 50% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanisme-data for pimobendan er markeret som et datahul i denne bevispakke (alvorlighed: høj). Den eneste mekanistiske kontekst, der er tilgængelig, kommer fra omstillings-rationale-noter, som beskriver pimobendan som en PDE3-inhibitor/calciumsensibilisator brugt klinisk for sine positive inotrope og vasodilatatoriske effekter.

Vigtigst er det, at bevispakningen's egen vurdering angiver, at denne forudsigelse **ikke** er mekanistisk understøttet: der er ingen kendt sammenhæng mellem pimobendan's kardiovaskulær farmakologi og de fibrotiske/inflammatoriske processer, der ligger til grund for blandet mineralstøvpneumokonose. En TxGNN-score på 0.5 svarer til en ikke-informativ standardværdi snarere end et meningsfuldt signal — modellen udtrykker effektivt ingen præference. Det samme mønster gælder for alle ti rangerede forudsigelser for denne medicin (alle scoret 0.5, alle bevisniveau L5, alle anbefalet Afvent), flere af hvilke er sjældne genetiske syndromer eller immun-mediere tilstande uden plausibel farmakologisk forbindelse til pimobendan.

I betragtning heraf bør forudsigelsen behandles som et lavt-konfidensmodel-artefakt snarere end en troværdig omstillings-hypotese på nuværende tidspunkt.

## Bevis fra kliniske forsøg

Aktuelt ingen relaterede kliniske forsøg registreret.

## Litteraturbeviser

Aktuelt ingen relateret litteratur tilgængelig.

## Markedsinformation for Danmark

Pimobendan har aktuelt ingen markedsføringstilladelse i Danmark (markedsstatus: ikke markedsført; 0 tilladelser på arkiv), så ingen produkt-/doseringsform-information er tilgængelig.

## Sikkerhedshensyn

Se venligst den godkendte produktkarakteristika-oversigt (SmPC) for sikkerhedsinformation. Bemærk: TFDA/regulatorisk advarsel og kontraindikationsdata for denne medicin er markeret som et **blokerende** datahul (DG001) — dette skal løses, før nogen sikkerhedsvurdering (S1-trin) kan fortsætte.

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
- Alle ti forudsagte indikationer bærer den samme ikke-informativ TxGNN-score (0.5), ingen understøttende kliniske forsøg eller litteratur, og bevisniveau L5. Pakken selv bemærker ingen mekanistisk plausibilitet for den højest rangerede indikation. Medicinen er ikke markedsført i Danmark, og centrale sikkerhedsdata (advarsler/kontraindikationer) er et blokerende datahul.

**For at fortsætte er følgende nødvendigt:**
- TFDA/SmPC-advarsler og kontraindikationer (blokerende hul, DG001)
- Verificeret virkningsmekanisme-data (høj-prioritets-hul, DG002)
- Genkørsel af TxGNN-forudsigelse med en korrekt diskriminerende score for at bekræfte, om de nuværende 0.5-værdier afspejler ægte modelusikkerhed eller et data- eller mappingproblem
- Eventuel preliminær præ-klinisk eller mekanistisk begrundelse, der forbinder pimobendan's kardiovaskulær farmakologi til den forudsagte indikation, før yderligere evaluering er berettiget

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

