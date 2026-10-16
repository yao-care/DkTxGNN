---
layout: default
title: Metformin
parent: Kun modelforudsigelse (L5)
nav_order: 535
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-14
description: "Metformin: forudsagt ny indikation Fokal stiff limb-syndrom (evidensniveau L5). Oprindelig indikation: Type 2-diabetes mellitus"
monitor_inn: "metformin"
predicted_indications: ["focal stiff limb syndrome", "classic stiff person syndrome", "opsismodysplasia", "thiamine-responsive dysfunction syndrome", "drug-induced localized lipodystrophy"]
---

# Metformin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **5** stk.
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

# Metformin: Fra type 2-diabetes til fokal stiff limb-syndrom

## Resumé

Metformin er et oralt antidiabetikum, der oprindeligt anvendes til behandling af type 2-diabetes mellitus.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt på **fokal stiff limb-syndrom** (en variant inden for stiff person-spektret).
Der er dog **ingen registrerede kliniske forsøg** og **ingen publikationer**, der understøtter denne retning. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Type 2-diabetes mellitus (fra vidensgrafen; der er ikke registreret indikationstekst i de danske markedsføringstilladelser) |
| Forudsagt ny indikation | Fokal stiff limb-syndrom |
| TxGNN-forudsigelsesscore | 99,45 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 18 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om metformins virkningsmekanisme i de data, der er indsamlet til denne rapport. Det er alment kendt, at metformin aktiverer AMPK, nedsætter leverens glukoseproduktion og hæmmer mitokondriets kompleks I. Disse oplysninger stammer dog ikke fra de foreliggende data og er ikke brugt til at underbygge forudsigelsen.

Fokal stiff limb-syndrom hører til stiff person-syndrom-spektret, en autoimmun neurologisk lidelse med nedsat GABAerg neurotransmission. Der kan ikke påvises en etableret mekanistisk sammenhæng mellem metformin og denne sygdom. En mulig forklaring på modelsignalet kan være sammenhængen mellem GAD65-autoimmunitet og diabetes, men det er ikke evidens for effekt.

Forudsigelsen bør derfor betragtes som en hypotese frembragt af modellen og ikke som et klinisk begrundet behandlingsforslag.

### Øvrige forudsagte indikationer (alle L5, Hold)

| Rang | Sygdom | TxGNN-score | Kommentar |
|------|------|------|------|
| 2 | Klassisk stiff person-syndrom | 99,45 % | Autoimmun, anti-GAD65; ingen understøttende data |
| 3 | Opsismodysplasi | 99,40 % | Sjælden skeletdysplasi (INPPL1); rent teoretisk link via PI3K/insulinsignalering |
| 4 | Tiaminresponsivt dysfunktionssyndrom | 99,40 % | Diabetes indgår i syndromet, men håndteres typisk med insulin og tiamin |
| 5 | Lægemiddelinduceret lokaliseret lipodystrofi | 99,06 % | Metformin er undersøgt ved andre lipodystrofier, men ikke ved denne |

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Alle 18 tilladelser er gyldige og omfatter filmovertrukne tabletter til oral anvendelse. De fleste er kombinationspræparater, der indeholder metformin, men er registreret som enkeltstående tilladelser. Indikationstekst er ikke tilgængelig i de foreliggende data. Nedenfor ses fem af tilladelserne.

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106612321 | Forminet (STADA Arzneimittel AG) | Filmovertrukne tabletter | Ikke angivet |
| 28105128112 | Vipdomet (Takeda Pharma A/S) | Filmovertrukne tabletter | Ikke angivet |
| 28104196807 | Efficib (Merck Sharp & Dohme B.V.) | Filmovertrukne tabletter | Ikke angivet |
| 28105485314 | Synjardy (Boehringer Ingelheim Int. GmbH) | Filmovertrukne tabletter | Ikke angivet |
| 28104745610 | Komboglyze (AstraZeneca AB) | Filmovertrukne tabletter | Ikke angivet |

---

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer var ikke tilgængelige i de indsamlede data. Følgende oplysninger stammer fra vidensgrafen og ikke fra produkttekst.

- **Kontraindikationer fra vidensgraf (ikke produkttekst)**: leversvigt og leversygdom, nyresygdom, pancreatitis, galdeblæresygdom, kongestiv hjerteinsufficiens, binyrebarkinsufficiens, thymussygdom samt en række tilstande med hypofysesvigt og hypogonadotrop hypogonadisme (bl.a. Kallmanns syndrom og Sheehans syndrom).
- **Lægemiddelinteraktioner**: Der er registreret 907 interaktioner i alt. Blandt de udvalgte er følgende af alvorlig grad (Major):
  - Acetazolamid
  - Ethanol (alkohol)
- Eksempler på moderate interaktioner: dolutegravir, abemaciclib, phenylephrin, ranitidin, formoterol, pseudoephedrin, ketorolac, nifedipin, adrenalin, ibuprofen, ethinylestradiol, hydrocortison, salbutamol, hydrochlorthiazid og acetohexamid.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende baseret på en beregningsmodel (evidensniveau L5) uden kliniske forsøg eller publikationer. Der kan ikke påvises en rimelig mekanistisk sammenhæng mellem metformin og fokal stiff limb-syndrom. Samtidig mangler produktresuméets sikkerhedsdata.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra de danske produktresuméer (Lægemiddelstyrelsen)
- Systematisk litteratursøgning og søgning efter prækliniske eller mekanistiske studier om metformin ved stiff person-spektret
- Vurdering af, om den autoimmune baggrund (GAD65) og eventuel samtidig diabetes kan forklare modelsignalet
- Afklaring af klinisk behov og alternative, veletablerede behandlinger, før der overvejes et forsøg
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

