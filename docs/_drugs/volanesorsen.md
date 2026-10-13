---
layout: default
title: Volanesorsen
parent: Kun modelforudsigelse (L5)
nav_order: 891
evidence_level: L5
indication_count: 10
---

# Volanesorsen
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

# Volanesorsen: Fra manglende registreret indikation til megaloblastær anæmi

## Sammenfatning i få sætninger

Volanesorsen er et antisense-oligonukleotid, der er rettet mod apolipoprotein C-III (APOC3) og markedsføres i Danmark som Waylivra. En godkendt indikationstekst er ikke tilgængelig i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **megaloblastær anæmi**, men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter denne retning. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i de indsamlede data |
| Forudsagt ny indikation | Megaloblastær anæmi |
| TxGNN-forudsigelsesscore | 99,997 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Ud fra kendt viden er volanesorsen et antisense-oligonukleotid, der binder APOC3-mRNA og dermed nedsætter dannelsen af APOC3. Formålet er at sænke triglycerider.

Megaloblastær anæmi skyldes derimod mangel på vitamin B12 eller folat og nedsat DNA-syntese. Der er ingen kendt mekanistisk forbindelse mellem APOC3-hæmning og disse mekanismer. Den meget høje score er en grafbaseret forudsigelse uden støtte i kliniske data eller litteratur og afspejler sandsynligvis netværksartefakter.

De øvrige forudsigelser i rangordenen er heller ikke mekanistisk understøttet: seglcellesygdom og undertyper heraf, sklerosende kolangitis, meningokokinfektion og paroksysmal nær hæmoglobinuri. Flere seglcelle-undertyper har næsten identiske scorer, hvilket tyder på, at scoren er nedarvet fra ontologiens struktur og ikke udgør uafhængigt signal. Alle ligger på evidensniveau L5 med anbefalingen Hold.

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105996917 | Waylivra | Injektionsvæske, opløsning i fyldt injektionssprøjte | Ikke oplyst |

Indehaver: Akcea Therapeutics Ireland Ltd.

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgraf:** I TxGNN-vidensgrafen (PrimeKG) er der en kontraindikationsrelation mellem volanesorsen og **trombocytopeni**. Dette stammer fra vidensgrafen og ikke fra produktresuméets tekst, og det bør verificeres mod det godkendte produktresumé.

Det anbefales i øvrigt at konsultere det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5) uden kliniske forsøg eller litteratur og uden plausibel mekanistisk forbindelse. Desuden er der en vidensgrafregistreret kontraindikation (trombocytopeni), som er relevant ved en anæmipopulation.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikation)
- Detaljerede data om virkningsmekanisme (MOA) fra DrugBank
- Systematisk litteratur- og forsøgssøgning for at afklare, om der findes biologisk rationale
- Vurdering af trombocytopenirisikoen, før en eventuel anvendelse overvejes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

