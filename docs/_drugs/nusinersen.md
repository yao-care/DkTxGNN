---
layout: default
title: Nusinersen
parent: Kun modelforudsigelse (L5)
nav_order: 313
evidence_level: L5
indication_count: 10
---

# Nusinersen
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

# Nusinersen: Fra original indikation ikke tilgængelig til Blandet mineralstøv-pneumokonose

## Ét-linjes resumé

Nusinerserens oprindeligt godkendte indikation er ikke registreret i denne evidenspakke (ingen licens- eller virkningsmekanismedata tilgængelige). TxGNN-modellens højest rangerede forudsigelse er **Blandet mineralstøv-pneumokonose**, men forudsigelsesscore (50%) ligger ved modellens ikke-diskriminativ baseline, og **0 kliniske forsøg** og **0 publikationer** understøtter denne retning i øjeblikket.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Ikke tilgængelig i evidenspakke (ingen markedsføringstilladelse eller etiketdata på fil) |
| Forudsagt ny indikation | Blandet mineralstøv-pneumokonose |
| TxGNN forudsigelsesscore | 50.0% |
| Evidensniveau | L5 |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Udsat |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanismedata er ikke i øjeblikket tilgængelige for Nusinersen i denne evidenspakke, og ingen oprindelig indikation er på fil til sammenligning. På grundlag af modellens egen genererede begrundelse antages Nusinersen at virke som et antisense-oligonukleotid, der målretter SMN2 pre-mRNA splicing (intron 7 / ISS-N1-region), administreret intrathekal, med farmakologisk aktivitet begrænset til centralnervesystemets motorneuroner.

Blandet mineralstøv-pneumokonose er en inhalationslungesigte drevet af makrofagaktivering og TGF-β–medieret fibrotisk/inflammatorisk vej — en mekanisme uden kendt overlap med SMN2-splicingregulation. Evidenspakkens egen mekanistiske vurdering konkluderer, at en TxGNN-score på 0,5 repræsenterer en væsentlig ikke-diskriminativ baselineværdi og udgør ikke evidens for biologisk plausibilitet.

Det er også værd at bemærke, at alle ti af modellens højest rangerede forudsagte indikationer for dette lægemiddel har den identiske score på 0,5, der spænder over ikke-relaterede sygdomsområder (pneumokonose, sjældne genetiske syndromer, mastcellesygdomme, madvareallergisyndrom, senepatologi). Dette mønster indikerer, at modellen ikke fandt et selvtillidsfuldt diskriminerende signal for Nusinersen i denne kørsel, snarere end at identificere en specifik højt tillidsfuld genforbrug-kandidat.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

Nusinersen er **ikke markedsført** i Danmark ifølge denne evidenspakke, og ingen markedsføringstilladelser (nationale Lægemiddelstyrelsen eller centraliserede EMA) er på fil.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresuméet (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Afgørelse: Udsat**

**Begrundelse:**
- TxGNN-scoren (0,5) er ved modellens ikke-diskriminativ baseline — delt identisk på tværs af alle ti højest rangerede kandidater — og understøttes ikke af nogen kliniske forsøgs- eller litteraturbevis. Der er heller ingen etableret mekanistisk forbindelse mellem Nusinerserens CNS-begrænsede splicingmodulationsaktivitet og blandet mineralstøv-pneumokonose.

**For at fortsætte er følgende nødvendig:**
- Original indikation og etiket-/MOA-data for Nusinersen (i øjeblikket et blokerings-/høj-alvor-datatab)
- Danske/EU regulatoriske advarsler og kontraindikationer (SmPC) for at muliggøre en baseline-sikkerhedsgennemgang
- En genkørsel eller omrangering mod en højere, mere diskriminativ TxGNN-scoretærskel, før denne kandidat betragtes for yderligere evaluering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

