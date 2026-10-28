---
layout: default
title: Cisatracurium
parent: Kun modelforudsigelse (L5)
nav_order: 198
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-28
description: "Cisatracurium: forudsagt ny indikation Cauda equina-syndrom (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (godkendt indikationstekst er tom)"
monitor_inn: "cisatracurium"
predicted_indications: ["cauda equina syndrome", "preeclampsia", "obsolete neurogenic bladder (disease)", "migraine disorder", "thrombotic disease", "irritable bowel syndrome", "migraine with brainstem aura", "mild pre-eclampsia", "severe pre-eclampsia", "neurocirculatory asthenia"]
---

# Cisatracurium
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

## Cisatracurium: Fra neuromuskulær blokade til cauda equina-syndrom
{: .text-alpha }

## Resumé i én sætning

Cisatracurium er et ikke-depolariserende neuromuskulært blokerende middel, som anvendes under anæstesi. Der foreligger ingen godkendt indikationstekst i de data, der er sammenstillet til denne rapport. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **cauda equina-syndrom**, men der er **0 kliniske forsøg** og **0 publikationer** for denne indikation. Forudsigelsen bygger udelukkende på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (godkendt indikationstekst er tom) |
| Forudsagt ny indikation | Cauda equina-syndrom |
| TxGNN-forudsigelsesscore | 0,9999 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de sammenstillede data. Cisatracurium er dog kendt som et ikke-depolariserende neuromuskulært blokerende middel, der virker på nikotinerge acetylcholinreceptorer ved den neuromuskulære endeplade og giver skeletmuskelrelaksation.

Der er ingen oplagt terapeutisk sammenhæng med cauda equina-syndrom. Tilstanden er en kompressionsbetinget nerverodsskade, som normalt kræver kirurgisk dekompression. Den høje score kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Den understøttes ikke af kliniske data eller litteratur.

Det samme billede gælder for de øvrige forudsagte indikationer (præeklampsi, neurogen blære, migræne, trombotisk sygdom, irritabel tarm m.fl.): Ingen har et plausibelt mekanistisk grundlag, og de har score mellem 0,9995 og 0,9999.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for cauda equina-syndrom. Heller ikke for de øvrige ni forudsagte indikationer er der fundet kliniske forsøg.

---

## Litteraturevidens

For den primære forudsigelse (cauda equina-syndrom) er der i øjeblikket ingen relateret litteratur. Nedenfor ses den begrænsede litteratur, der er fundet for de næste forudsigelser. Den er kun indirekte kontekst, hvor cisatracurium indgår som en del af anæstesiregimet.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [41103680](https://pubmed.ncbi.nlm.nih.gov/41103680/) | 2025 | Kohorte | Anesthesiology and Pain Medicine | Sammenligning af IL-6, leptin og adiponectin efter kejsersnit under generel versus spinal anæstesi (præeklampsi, rang 2) |
| [18383970](https://pubmed.ncbi.nlm.nih.gov/18383970/) | 2008 | Case-serie | Rev Esp Anestesiol Reanim | Remifentanil-bolus ved kejsersnit hos højrisikopatienter (12 tilfælde) (præeklampsi, rang 2) |
| [12565113](https://pubmed.ncbi.nlm.nih.gov/12565113/) | 2002 | Review | Journal of Clinical Anesthesia | Anæstesi ved levertransplantation fra levende donor hos børn (trombotisk sygdom, rang 5) |

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106328919 | Cisatracurium "Accordpharma" (Accord Healthcare B.V.) | Injektions-/infusionsvæske, opløsning | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (90 interaktioner i alt registreret; et udpluk af de vigtigste):

- **Alvorlige (Major):** kanamycin, neomycin, paromomycin, polymyxin B, streptomycin (aminoglykosider og polymyxiner kan forstærke den neuromuskulære blokade)
- **Moderate:** amphotericin B (inkl. lipidformuleringer), doxycyclin, tetracyclin, minocyclin, magnesiumchlorid, magnesiumsulfat, mannitol, metoclopramid, vancomycin
- **Milde (Minor):** ranitidin

Magnesiumsulfat er særligt relevant ved svær præeklampsi, da det potenserer neuromuskulær blokade.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for cauda equina-syndrom bygger udelukkende på modellen (L5) uden kliniske forsøg, uden litteratur og uden et plausibelt virkningsmekanistisk grundlag. De øvrige forudsagte indikationer har heller ikke understøttende evidens ud over indirekte anæstesikontekst.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Godkendt indikationstekst og sikkerhedsoplysninger (advarsler og kontraindikationer) fra produktresuméet hos Lægemiddelstyrelsen
- Præklinisk eller mekanistisk dokumentation, der kan underbygge en biologisk sammenhæng, før yderligere evaluering overvejes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

