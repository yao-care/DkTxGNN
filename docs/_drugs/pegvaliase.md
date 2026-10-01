---
layout: default
title: Pegvaliase
parent: Kun modelforudsigelse (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Pegvaliase
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

# Pegvaliase: Fra fenylketonuri til diabetisk retinopati

## Resumé i én sætning

Pegvaliase er et PEGyleret phenylalanin-ammoniak-lyase-enzym (PAL), som oprindeligt anvendes til behandling af fenylketonuri (PKU).
TxGNN-modellen forudsiger, at det kan have effekt ved **diabetisk retinopati**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning.
Forudsigelsen er udelukkende grafbaseret og bør ikke tages som tegn på klinisk effekt.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Fenylketonuri (PKU). Indikationsteksten mangler i det danske markedsføringstilladelsesdata, så oplysningen stammer fra vurderingen af lægemidlet |
| Foreslået ny indikation | Diabetisk retinopati |
| TxGNN-forudsigelsesscore | 99,17 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Pegvaliase er et PEGyleret phenylalanin-ammoniak-lyase, som omdanner phenylalanin til trans-kanelsyre og ammoniak. Det er godkendt til fenylketonuri. Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen (MOA) i evidensgrundlaget.

Der er ingen dokumenteret biologisk vej fra phenylalaninnedbrydning til retinal mikrovaskulær sygdom, hvor VEGF, inflammation og hyperglykæmisk skade spiller en rolle. Den høje score skyldes sandsynligvis nærhed i vidensgrafen snarere end en egentlig biologisk begrundelse. Eksisterende standardbehandlinger (anti-VEGF og laserfotokoagulation) har veldokumenteret evidens, og intet i dette datagrundlag taler for at fortrænge dem.

Modellen har også foreslået fire beslægtede øjenindikationer:

- **Svær non-proliferativ diabetisk retinopati**, score 99,16 %. Det er et undertrin af diabetisk retinopati, så vurderingen er den samme.
- **Diabetisk katarakt**, score 99,11 %. Tilstanden skyldes polyolvej og osmotisk eller oxidativ linseskade, og kirurgi er den definitive behandling. Der er ingen kendt vej fra et systemisk phenylalaninnedbrydende enzym til linsen.
- **Nuklear senil katarakt** og **kortikal katarakt**, begge med score 98,97 %. De identiske scorer tyder på, at forudsigelsen afspejler et fælles, uspecifikt kataraktområde i grafen. De fire kataraktforudsigelser bør derfor ses som ét signal med lav sikkerhed og ikke som uafhængig støtte.

Dublerede poster i inputtet er slået sammen.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106089818 | Palynziq (BioMarin International Limited) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Der er ikke registreret data om advarsler, kontraindikationer eller interaktioner i evidensgrundlaget. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Vurderingen af lægemidlet peger desuden på risiko for anafylaksi og immunogenicitet, hvilket ville være en tung belastning for patienter uden PKU.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er rent modelbaseret (L5) uden kliniske forsøg, publikationer eller dokumenteret mekanistisk sammenhæng. Anafylaksi- og immunogenicitetsrisikoen gør det desuden svært at forsvare brug hos patienter uden PKU.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Sikkerhedsoplysninger (advarsler og kontraindikationer) fra det danske produktresumé hos Lægemiddelstyrelsen
- Præklinisk eller mekanistisk evidens for en sammenhæng mellem phenylalaninnedbrydning og retinal eller linserelateret patologi
- Litteratur- og forsøgssøgning med specifikke søgetermer, før forudsigelsen vurderes på ny

---

*Resultaterne er kun til forskningsbrug og udgør ikke lægefaglig rådgivning. Kandidater til lægemiddelrepositionering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

