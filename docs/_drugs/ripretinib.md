---
layout: default
title: Ripretinib
parent: Kun modelforudsigelse (L5)
nav_order: 380
evidence_level: L5
indication_count: 10
---

# Ripretinib
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

# Ripretinib: Fra oprindelig indikation (data afventes) til multipel endokrin neoplasi

## Resumé i én sætning

> Ripretinib (DrugBank DB14840) markedsføres ikke i øjeblikket i Danmark, og dets oprindelige godkendte indikation er ikke tilgængelig i denne bevismappe.
> TxGNN-modellens øverst rangerede forudsigelse er **multipel endokrin neoplasi (MEN)**, med en forudsigelsesscore på **98.84%**,
> men dette understøttes af **0 kliniske forsøg** og **0 publikationer**, og modellens egen begrundelse påpeger en svag mekanistisk forbindelse.

---

## Hurtig oversigt

| Emne | Indhold |
|------|----------|
| Oprindelig indikation | Ingen data tilgængelige (ikke registreret i Danmark; ingen tekst om oprindelig indikation angivet) |
| Forudsagt ny indikation | Multipel endokrin neoplasi |
| TxGNN forudsigelsesscore | 98.84% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om ripretinibs virkningsmekanisme er ikke tilgængelige i denne bevismappe (markeret som et datakløft, alvorlighed: Høj). Det, der er tilgængeligt, er modellens eget rationale, som identificerer ripretinib som en **switch-control KIT/PDGFRA tyrosinkinasehæmmer**.

Multipel endokrin neoplasi (især MEN2) er primært drevet af **RET**-mutationer, ikke KIT/PDGFRA — en anden gren af receptortyrosinkinaser. Bevismappe-rationalets egen forklaring til denne forudsigelse angiver eksplicit, at der ikke er noget direkte target-overlap mellem ripretinibs kendt farmakologi og MEN's driver-gen, og at forudsigelsen udelukkende er baseret på TxGNN knowledge-graph embedding-lighed uden understøttende forsøgs- eller litteraturbevis.

Bemærkelsesværdigt er det, at flere andre TxGNN-rangerede kandidater for dette lægemiddel (ondartede katarrer, infektiøs bovint rhinotracheitis) er **veterinær-/kvæglidelser**, ikke humane indikationer — hvilket tyder på sygdomsontologi-støj i den underliggende knowledge graph for denne kandidat. Dette sænker yderligere tilliden til, at den rå rangering afspejler et biologisk meningsfuldt signal for ripretinib specifikt, og forstærker behandlingen af MEN-forudsigelsen som alene hypotesegenererende.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Ripretinib markedsføres ikke i øjeblikket i Danmark. Ingen markedsføringstilladelser (nationale eller centraliserede/EMA) er registreret i denne bevismappe.

---

## Cytotoxicitet

Ripretinib er karakteriseret i bevismappe-rationalets beskrivelse som en KIT/PDGFRA switch-control tyrosinkinasehæmmer, konsistent med en målrettet (ikke klassisk-cytotoksisk) småmolekyle-anticancer-agent.

| Emne | Indhold |
|------|----------|
| Cytotoxicitetsklassifikation | Målrettet terapi (KIT/PDGFRA tyrosinkinasehæmmer) |
| Risiko for myelosuppression | Se venligst resume af produktegenskaber (SmPC) advarsler og forholdsregler |
| Emetogenicitetsklassifikation | Se venligst resume af produktegenskaber (SmPC) advarsler og forholdsregler |
| Monitorerings-elementer | Se venligst resume af produktegenskaber (SmPC) advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se venligst resume af produktegenskaber (SmPC) advarsler og forholdsregler |

---

## Sikkerhedshensyn

Se venligst det godkendte resume af produktegenskaber (SmPC) for sikkerhedsinformation. Bemærk: regulatoriske advarsler/kontraindikation-data (f.eks. TFDA/SmPC-mærkning) er markeret som et **blokerende datakløft** i denne bevismappe og skal indhentes før enhver sikkerhedsvurdering kan fortsætte.

---

## Konklusion og næste trin

**Afgørelse: Afvent**

**Begrundelse:**
- Den øverst rangerede forudsagt indikation (MEN) har nul kliniske forsøgs- eller litteraturunderstøttelse, et bevisniveau på L5 (modelforudsigelse alene), og modellens egen begrundelse identificerer en svag/ubekræftet mekanistisk forbindelse (RET-drevet sygdom vs. et KIT/PDGFRA-målrettet lægemiddel). Lægemidlet markedsføres heller ikke i øjeblikket i Danmark, og vigtige sikkerhedsdata fra mærkning mangler (blokerende kløft).

**For at fortsætte er følgende nødvendig:**
- Ripretinibs officielle virkningsmekanisme og oprindelig godkendt indikation (i øjeblikket et datakløft)
- Danske/EU SmPC-advarsler, kontraindikationer og forholdsregler (i øjeblikket et blokerende datakløft — påkrævet før nogen sikkerhedsvurdering)
- Uafhængig mekanistisk eller præ-klinisk validering af en RET/KIT-PDGFRA-forbindelse før forfølgelse af MEN som en re-indikation-hypotese
- Genskanning af den fulde TxGNN-kandidatliste for dette lægemiddel for at filtrere ikke-menneskelige (veterinær) sygdomsposter før yderligere evaluering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

