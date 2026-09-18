---
layout: default
title: Tucatinib
parent: Kun modelforudsigelse (L5)
nav_order: 456
evidence_level: L5
indication_count: 10
---

# Tucatinib
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

# Tucatinib: Fra HER2-positiv brystkræft til migræne

## Resumé i én sætning

Tucatinib er en oral HER2-selektiv tyrosinkinaseinhibitor, som i det tilvejebragte bevis beskrives som målrettet mod HER2-stien, der bruges i onkologiske indstillinger; ingen bekræftet oprindelig indikation er registreret i denne bevismappe, fordi medicinen ikke markedsføres i Danmark. TxGNN-modellen forudsiger, at det kan være effektivt mod **Migræne**, men denne forudsigelse understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer**, og bevismappe's egen mekanistiske begrundelse angiver, at der er ingen kendt biologisk forbindelse mellem HER2-signalering og migrænepatofysiologi (CGRP, trigeminovaskulært system, serotoninveje).

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ikke dokumenteret i danske licensdata (medicinen markedsføres ikke i Danmark); bevismappe's begrundelsestekst identificerer Tucatinib som en HER2-selektiv TKI, der bruges i HER2-relateret onkologi |
| Forudsagt ny indikation | Migræne |
| TxGNN-forudsigelsesscore | 98.62% |
| Bevisniveau | L5 (kun modelforudsigelse, ingen kliniske forsøg eller litteratur) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanismedata for virkning (`original_moa`) ikke tilgængelig som et struktureret felt. Baseret på oplysninger indlejret i bevismappe's egen begrundelsestekst er Tucatinib en HER2-selektiv tyrosinkinaseinhibitor, en lægemiddelklasse, der bruges i onkologi til at blokere HER2-drevet tumorcellesignalering.

Migrænes kendte patofysiologi omfatter CGRP-frigivelse, det trigeminovaskulære system og serotonerge veje — ingen af disse overlapper med HER2-receptorsignalering. Bevismappe angiver eksplicit: *"無已知機轉關聯...無臨床或臨床前證據支持"* (ingen kendt mekanistisk forbindelse; ingen klinisk eller præ-klinisk evidens understøtter denne association).

I betragtning af fraværet af en plausibel biologisk mekanisme og det fuldstændige fravær af understøttende kliniske forsøg eller litteratur for dette specifikke lægemiddel-sygdoms-par, bør denne forudsigelse fortolkes som en statistisk association fra TxGNN-modellen snarere end en mekanistisk funderet genbrug-hypotese.

---

## Kliniske forsøgsbeviser

Der er i øjeblikket ingen registrerede relaterede kliniske forsøg.

---

## Litteraturbeviser

Der er i øjeblikket ingen tilgængelig relateret litteratur.

---

## Markedsinformation for Danmark

Tucatinib markedsføres ikke i øjeblikket i Danmark. Ingen markedsføringstilladelser (nationale Lægemiddelstyrelsen eller centraliserede EMA) blev fundet i denne bevismappe (`total_licenses: 0`).

---

## Cytotoxicitet

| Emne | Indhold |
|------|---------|
| Cytotoxicitetsklassificering | Målrettet terapi (HER2-selektiv tyrosinkinaseinhibitor) |
| Myelosuppressionsrisiko | Se venligst Produktinformationen (SmPC) advarsler og forholdsregler |
| Emetogenitetsklassificering | Se venligst Produktinformationen (SmPC) advarsler og forholdsregler |
| Overvågningselementer | Se venligst Produktinformationen (SmPC) advarsler og forholdsregler |
| Beskyttelse ved håndtering | Se venligst Produktinformationen (SmPC) advarsler og forholdsregler |

---

## Sikkerhedshensyn

Se venligst den godkendte Produktinformation (SmPC) for sikkerhedsinformation. Der var ingen vigtige advarsler, kontraindikationer eller lægemiddel-lægemiddel-interaktionsdata tilgængelige i denne bevismappe.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Trods en høj TxGNN-forudsigelsesscore (98.62%) er der ingen understøttende klinisk forsøgs- eller litteraturbevis for Tucatinib ved migræne, og den mekanistiske begrundelse i bevismappe selv finder ingen biologisk plausibilitet (HER2-vej vs. CGRP/trigeminovaskulær/serotonerge veje). Dette er en modeludelukkende (L5) forudsigelse og opfylder ikke tærsklen for at komme videre fra første screening.

Derudover værd at bemærke: blandt dette lægemiddels andre højt rangerede TxGNN-forudsigelser blev "multipel endokrin neoplasi"-beviser (NCT04802759, NCT02892123) markeret som nøgleordsuoverensstemmelse — disse forsøg studerer zanidatamab, ikke Tucatinib — og "lungehypertension"-forudsigelsen blev markeret som et muligt **sikkerhedssignal snarere end terapeutisk fordel**, da tyrosinkinasehemmere som en klasse (f.eks. dasatinib) er kendt for at inducere lungehypertension som en bivirkning. Begge forstærker en forsigtig tilgang over for denne kandidat generelt.

**For at gå videre kræves følgende:**
- TFDA/danske Produktinformation-advarsler og kontraindikationer (i øjeblikket et kritisk dataglip)
- Bekræftede mekanisme-virkning-data via DrugBank API (i øjeblikket et alvorligt dataglip)
- Eventuelle præ-kliniske eller mekanistiske studier, der forbinder HER2-hæmning med migrænepatofysiologi, hvis de findes
- Genvurdering når autentisk (uden nøgleordsuoverensstemmelse) klinisk eller litteraturbevis bliver tilgængelig

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

