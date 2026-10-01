---
layout: default
title: Catumaxomab
parent: Kun modelforudsigelse (L5)
nav_order: 98
evidence_level: L5
indication_count: 10
---

# Catumaxomab
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

# Catumaxomab: Fra malign ascites til svær ikke-proliferativ diabetisk retinopati

## Resumé i én sætning

Catumaxomab er et trifunktionelt bispecifikt antistof (EpCAM × CD3), som markedsføres i Danmark under navnet Korjuny. Det anvendes i onkologi, og godkendelsen i EU har været til EpCAM-positiv malign ascites. TxGNN-modellen forudsiger, at det kan virke ved **svær ikke-proliferativ diabetisk retinopati**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Malign ascites hos EpCAM-positive karcinomer (fremgår af evidensgrundlagets mekanistiske vurdering; indikationsteksten i den danske registrering er ikke oplyst) |
| Forudsagt ny indikation | Svær ikke-proliferativ diabetisk retinopati |
| TxGNN-forudsigelsesscore | 99,64 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede mekanistiske data (MOA) er ikke tilgængelige i DrugBank-udtrækket. Catumaxomab er dog et bispecifikt antistof, der binder EpCAM på tumorceller og CD3 på T-celler. Fc-delen rekrutterer desuden accessoriske immunceller. Resultatet er en immunmedieret destruktion af EpCAM-positive tumorceller.

Diabetisk retinopati er en mikrovaskulær og neurodegenerativ sygdom uden kendt EpCAM-drevet patologi. Der er derfor ikke identificeret nogen plausibel mekanistisk sammenhæng mellem den oprindelige onkologiske anvendelse og den forudsagte indikation. Den høje score (0,996) skyldes sandsynligvis en artefakt i vidensgrafen, især fordi kilderegistreringen ikke har dokumenterede oprindelige indikationer eller virkningsmekanisme. CD3-medieret immunaktivering kunne desuden indebære risiko for okulær inflammation.

Modellen har også forudsagt følgende indikationer, alle uden kliniske eller litterære data:

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| Lægemiddelinduceret osteoporose | 99,58 % | Ingen plausibel mekanistisk sammenhæng (cytokinfrigivelse ville i givet fald være en bivirkning) |
| Diabetisk retinopati | 99,47 % | Overordnet term til ovenstående, samme svage grundlag |
| Diabetisk katarakt | 98,45 % | Ingen plausibel sammenhæng (polyol-vej og oxidativt stress i linsen) |
| Sarkomatoid overgangscellekarcinom i nyrebækkenet | 98,29 % | Indirekte biologisk plausibilitet (EpCAM udtrykkes i urotelkarcinom), men EpCAM-ekspressionen kan være nedsat ved sarkomatoid differentiering; markeret som "Research Question" |

Bemærk: Evidence Pack indeholder hver forudsigelse to gange. Her er dubletterne slået sammen.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106834422 | Korjuny (Lindis Biotech GmbH) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i datagrundlaget |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Immunterapi (bispecifikt antistof, EpCAM × CD3) |
| Risiko for myelosuppression | Se produktresuméet (SmPC) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC). Da lægemidlet udløser cytokinfrigivelse, bør immunreaktioner overvåges |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

Der er ikke fundet registrerede lægemiddelinteraktioner i de tilgængelige data. Oplysninger om advarsler og kontraindikationer fra Lægemiddelstyrelsens produktresumé mangler.

Teoretisk kan CD3-medieret immunaktivering give risiko for okulær inflammation ved anvendelse i øjet. Dette er ikke dokumenteret klinisk.

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modelscoren (evidensniveau L5) uden kliniske forsøg eller publikationer. Der er ingen plausibel mekanistisk sammenhæng mellem EpCAM × CD3 T-celleomdirigering og diabetisk retinopati. Sikkerhedsdata fra det danske produktresumé mangler, hvilket blokerer for sikkerhedsscreening.

**For at komme videre skal følgende foreligge:**
- Advarsler og kontraindikationer fra Lægemiddelstyrelsens produktresumé (blokerende datamangel)
- Detaljerede data om virkningsmekanisme fra DrugBank
- Hvis en onkologisk retning ønskes undersøgt: bekræftelse af EpCAM-ekspression i sarkomatoid overgangscellekarcinom i nyrebækkenet som en separat forskningsspørgsmål
- Præklinisk eller mekanistisk dokumentation, før nogen okulær anvendelse overvejes

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelreposition kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

