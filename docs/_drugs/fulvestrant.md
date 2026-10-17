---
layout: default
title: Fulvestrant
parent: Kun modelforudsigelse (L5)
nav_order: 377
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Fulvestrant: forudsagt ny indikation HIV-infektion (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (godkendelsesteksten er tom)"
monitor_inn: "Fulvestrant"
predicted_indications: ["HIV infectious disease", "HIV infectious disease", "multiple endocrine neoplasia", "multiple endocrine neoplasia", "simian immunodeficiency virus infection", "simian immunodeficiency virus infection", "feline acquired immunodeficiency syndrome", "feline acquired immunodeficiency syndrome", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
---

# Fulvestrant
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

# Fulvestrant: Fra brystkræft til HIV-infektion

## Resumé

Fulvestrant er en selektiv østrogenreceptor-nedbryder (SERD), som markedsføres i Danmark som Faslodex. Lægemidlet anvendes til hormonfølsom brystkræft, men den indikationstekst, der er indgået i dataene til denne rapport, er tom. TxGNN-modellen forudsiger, at det kan have effekt på **HIV-infektion**, men der foreligger **ingen kliniske forsøg** og kun **2 publikationer**, hvoraf kun én er direkte relevant, og den er præklinisk.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (godkendelsesteksten er tom) |
| Forudsagt ny indikation | HIV-infektion |
| TxGNN-prædiktionsscore | 99,91 % |
| Evidensniveau | L4 (kun præklinisk/mekanistisk evidens) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i de indsamlede data. Fulvestrant er dog kendt som en selektiv østrogenreceptor-nedbryder (SERD), der binder til østrogenreceptoren og fremmer dens nedbrydning.

Den eneste direkte relevante publikation (PMID 42430506, JCI Insight, 2026) undersøger østrogenreceptor α (ERα) i CD4+ T-celler i forbindelse med HIV-latens og latency-reversing agents. Her indgår fulvestrant som et værktøj til at påvirke ER-signalering. Det antyder en mulig sammenhæng mellem ERα-signalering og HIV-latens, og nedbrydning af receptoren kunne tænkes at modulere reaktivering af latent virus.

Evidensen er præklinisk og indirekte. Ingen studier har testet fulvestrant som HIV-behandling. Den høje TxGNN-score er en computerbaseret forudsigelse og ikke klinisk validering. Den anden publikation omhandler HTLV-1, en anden retrovirus, og er kun løst relateret.

---

## Evidens fra kliniske forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret for HIV-infektion.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [42430506](https://pubmed.ncbi.nlm.nih.gov/42430506/) | 2026 | Præklinisk/mekanistisk | JCI Insight | Undersøger effekten af ligander og HIV latency-reversing agents på østrogenreceptor α i CD4+ T-celler, herunder fulvestrants evne til at påvirke ER-signalering |
| [40343334](https://pubmed.ncbi.nlm.nih.gov/40343334/) | 2025 | Multi-omics-kohorteanalyse (HTLV-1, ikke HIV) | Research Square | Analyse af sygdomsmekanismer og terapeutiske targets ved HTLV-1-associeret myelopati. Kun løst relevant, da den omhandler en anden retrovirus |

---

## Markedsinformation i Danmark

| Tilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103481503 | Faslodex (AstraZeneca AB) | Injektionsvæske, opløsning | Ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Hormonel/endokrin kræftbehandling (SERD), ikke konventionelt cytotoksisk |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) |
| Emetogenicitet | Se produktresuméet (SmPC) |
| Monitorering | Se produktresuméet (SmPC) |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

Der henvises til advarsler og forsigtighedsregler i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

- **Mulige kontraindikationer (fra vidensgraf, ikke fra produkttekst):** Vidensgrafen (PrimeKG) angiver forbindelser til leversygdom, galdeblæresygdom, trombocytopeni og blodkoagulationsforstyrrelser. Disse stammer ikke fra godkendt produktinformation og skal verificeres i SmPC.
- **Lægemiddelinteraktioner:** Der er identificeret 92 mulige interaktioner (kilde: DDInter), alle med uklassificeret alvorlighed. Eksempler: warfarin, metformin, simvastatin, prednison, dexamethason, morfin, acetylsalicylsyre, omeprazol, pantoprazol, ondansetron og bupropion. Klinisk betydning er ikke vurderet.

Advarsler og kontraindikationer fra den godkendte produktinformation er ikke tilgængelige. Der henvises til SmPC.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der er ingen kliniske forsøg for fulvestrant ved HIV, og evidensen begrænser sig til ét præklinisk studie af ER-signalering i HIV-latens. Den høje TxGNN-score er ikke klinisk validering.

**For at komme videre er følgende nødvendigt:**
- Præklinisk validering af fulvestrants effekt på HIV-latens og -reaktivering i relevante modeller
- Data om virkningsmekanisme fra DrugBank
- Hentning og gennemgang af produktresuméet (SmPC) fra Lægemiddelstyrelsen, herunder godkendt indikation, advarsler og kontraindikationer
- Vurdering af sikkerhed og interaktioner hos HIV-patienter, især i forhold til antiretroviral behandling
- Afklaring af, om en hormonel SERD er hensigtsmæssig i en population med både mandlige og kvindelige patienter

---

### Bemærkning om øvrige forudsigelser

De indsamlede data indeholder også forudsigelser for multipel endokrin neoplasi (score 99,85 %), SIV-infektion, felint ervervet immundefektsyndrom og en sjælden neuroudviklingsforstyrrelse. De 13 forsøg knyttet til multipel endokrin neoplasi omhandler i realiteten ER+/HER2-negativ avanceret brystkræft og viser ikke effekt ved denne sygdom. Koblingen skyldes sandsynligvis en term-mapping-artefakt. De øvrige forudsigelser har ingen forsøg eller litteratur (L5). Alle har anbefalingen Hold.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

