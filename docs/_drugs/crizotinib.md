---
layout: default
title: Crizotinib
parent: Kun modelforudsigelse (L5)
nav_order: 222
evidence_level: L5
indication_count: 9
monitor_inn: "Crizotinib"
predicted_indications: ["fibromatosis, gingival", "fibroma of lung", "hamartoma of lung", "lung benign neoplasm", "pulmonary sulcus neoplasm", "lung germ cell tumor", "inclusion body myopathy with early-onset Paget disease with or without frontotemporal dementia", "junctional epidermolysis bullosa", "Leukomelanoderma-infantilism-intellectual disability-hypodontia-hypotrichosis syndrome"]
last_modified_at: 2026-10-30
description: "Crizotinib: forudsagt ny indikation Gingival fibromatose (evidensniveau L5). Oprindelig indikation: Ikke-småcellet lungekræft (NSCLC) og lungekræft"
---

# Crizotinib
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **9** stk.
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

## Crizotinib: Fra ikke-småcellet lungekræft til gingival fibromatose
{: .text-alpha }

> Bemærk: Rapporten er baseret på den højest rangerede forudsigelse (gingival fibromatose). Den har ingen kliniske studier eller publikationer. Øvrige forudsigelser omtales kort, hvor det er relevant.

## Kort resumé

Crizotinib er en tyrosinkinasehæmmer, der oprindeligt anvendes til behandling af ikke-småcellet lungekræft (NSCLC). TxGNN-modellen (deep learning) forudsiger, at lægemidlet kan have effekt ved **gingival fibromatose**, men der er **ingen kliniske forsøg** og **ingen publikationer** til støtte for denne forudsigelse. Scoren stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke-småcellet lungekræft (NSCLC) og lungekræft (relation registreret i vidensgrafen; licenstekst med godkendt indikation er ikke tilgængelig i de indsamlede data) |
| Forudsagt ny indikation | Gingival fibromatose |
| TxGNN-forudsigelsesscore | 0,9981 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der er ingen detaljerede data om virkningsmekanisme i de indsamlede data. Det er dog kendt fra den tilgængelige litteratur, at crizotinib hæmmer receptortyrosinkinaserne ALK, ROS1 og MET.

Disse mål er veldokumenterede drivere ved ALK- eller ROS1-omlejret NSCLC. Der er ikke dokumenteret nogen kobling mellem ALK, ROS1 eller MET og hereditær gingival fibromatose. Der er derfor ikke etableret en mekanistisk sammenhæng, og den høje modelscore er ikke understøttet af kliniske eller litteraturmæssige data.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for gingival fibromatose.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig for gingival fibromatose.

---

## Information om det danske marked

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106983123 | Xalkori (Pfizer Europe MA EEIG) | Granulat i kapsler til åbning | Indikationstekst er ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (tyrosinkinasehæmmer mod ALK, ROS1 og MET) |
| Risiko for myelosuppression | Se produktresuméet (SmPC) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC), herunder blodtal samt lever- og nyrefunktion |
| Beskyttelse ved håndtering | Se produktresuméet (SmPC) og lokale retningslinjer for håndtering af antineoplastiske lægemidler |

Der er ikke tilgængelige toksicitetsdata i de indsamlede data. Se advarsler og forsigtighedsregler i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er identificeret 100 interaktioner i interaktionsdatabasen. Blandt de angivne er følgende klassificeret som **alvorlige (Major)**: clarithromycin, cisaprid, dolasetron, eliglustat og granisetron. Flere andre, bl.a. famotidin, metformin, loperamid, bupropion, aprepitant, dexamethason og budesonid, er klassificeret som moderate.
- **Signaler fra litteraturen (ikke relateret til den forudsagte indikation):** Der er beskrevet tilfælde af hjertetoksicitet (bradykardi, QT-forlængelse) og fatal fulminant leversvigt under crizotinibbehandling.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for gingival fibromatose hviler alene på en beregningsmodel uden kliniske forsøg, uden publikationer og uden plausibel mekanistisk kobling. Den øvrige top-ni-liste er heller ikke et reelt omlægningssignal: de fleste forudsigelser har ingen evidens, og litteraturen for godartede lungeneoplasier handler om den allerede kendte NSCLC-brug, ikke om den forudsagte sygdom.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) og en begrundet hypotese for, hvordan ALK-, ROS1- eller MET-hæmning skulle påvirke gingival fibromatose
- Præklinisk evidens (celle- eller dyremodeller) for sygdommen
- Gennemgang af advarsler og kontraindikationer i det godkendte produktresumé (SmPC), som mangler i de indsamlede data
- Vurdering af sikkerhedsprofilen (hjerte- og levertoksicitet samt alvorlige interaktioner) i forhold til en godartet tilstand
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

