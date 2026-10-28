---
layout: default
title: Galcanezumab
parent: Kun modelforudsigelse (L5)
nav_order: 382
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
monitor_inn: "Galcanezumab"
predicted_indications: ["heparin cofactor 2 deficiency", "antithrombin deficiency type 2", "factor 5 excess with spontaneous thrombosis"]
description: "Galcanezumab: forudsagt ny indikation Heparin-cofaktor-2-mangel (heparin cofactor 2 deficiency) (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Galcanezumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
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

## Galcanezumab: Heparin-cofaktor-2-mangel (heparin cofactor 2 deficiency)
{: .text-alpha }

## Resumé

Galcanezumab er et humaniseret monoklonalt antistof mod calcitonin gene-related peptide (CGRP). Det anvendes oprindeligt til forebyggelse af migræne. TxGNN-modellen forudsiger, at det kan have effekt ved **heparin-cofaktor-2-mangel** (score 0,9950), men der findes **ingen kliniske forsøg og ingen publikationer**, og der er ingen plausibel biologisk forbindelse. Forudsigelsen skal derfor betragtes som en ren modelartefakt.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Heparin-cofaktor-2-mangel (heparin cofactor 2 deficiency) |
| TxGNN-prædiktionsscore | 0.9950 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Galcanezumab neutraliserer CGRP, som spiller en central rolle i migrænens patofysiologi. Lægemidlet er godkendt til forebyggelse af migræne og af episodisk clusterhovedpine. Detaljerede data om virkningsmekanismen fra lægemiddeldatabasen er ikke tilgængelige i de data, der er indsamlet til denne rapport.

Galcanezumab påvirker hverken koagulationskaskaden eller heparin-cofaktor II. Der er derfor ingen mekanistisk sammenhæng mellem migræne og heparin-cofaktor-2-mangel. Den høje score stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

Det samme gælder de øvrige koagulationsrelaterede forudsigelser i datasættet. De er alle uden kliniske forsøg og litteratur og uden plausibel mekanisme:

- Antitrombinmangel type 2 (99,41 %)
- Faktor 5-overskud med spontan trombose (99,41 %)
- Trombofili (98,99 %)

Dobbeltposter i inputtet er slået sammen.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur for heparin-cofaktor-2-mangel.

### Supplerende bemærkning: migræne med hjernestammeaura

Blandt de forudsigelser, der er indsamlet til denne rapport, er det kun **migræne med hjernestammeaura** (evidensniveau L4) der har litteraturstøtte. Det er en undertype af migræne og ligger tæt på den godkendte indikation, så det er en udvidelse inden for migrænespektret snarere end repurposing til en ny sygdom. Den fremlagte litteratur handler dog ikke specifikt om hjernestammeaura. Fase 3-evidensen er indirekte og stammer fra generel episodisk migræne.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [29813147](https://pubmed.ncbi.nlm.nih.gov/29813147/) | 2018 | RCT | JAMA Neurology | EVOLVE-1: galcanezumab til forebyggelse af episodisk migræne |
| [33549036](https://pubmed.ncbi.nlm.nih.gov/33549036/) | 2021 | RCT (post hoc-analyse af fase 3) | J Headache Pain | Effekt på migrænens sværhedsgrad og symptomer i EVOLVE-1, EVOLVE-2 og REGAIN |
| [36266558](https://pubmed.ncbi.nlm.nih.gov/36266558/) | 2023 | RCT (sekundæranalyse, japansk delpopulation) | Neurol Ther | Effekt på sværhedsgrad og symptomer hos japanske patienter med episodisk migræne |
| [32504377](https://pubmed.ncbi.nlm.nih.gov/32504377/) | 2020 | Review | Drugs | Oversigt over galcanezumab til forebyggelse af migræne og behandling af episodisk clusterhovedpine |
| [40341526](https://pubmed.ncbi.nlm.nih.gov/40341526/) | 2025 | Review/observationel | Headache | Genetiske migrænesygdomme og respons på CGRP-antagonister; titlen viser ikke data specifikke for hjernestammeaura |
| [42390441](https://pubmed.ncbi.nlm.nih.gov/42390441/) | 2026 | Kohorte/sikkerhedsstudie | Cephalalgia | Cerebrovaskulær risiko ved CGRP-antistoffer sammenlignet med onabotulinumtoxinA |
| [39365416](https://pubmed.ncbi.nlm.nih.gov/39365416/) | 2024 | Case report | Pain Ther | Cerebral arterievasokonstriktion efter galcanezumabs startdosis |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106224617 | Emgality (Eli Lilly Nederland B.V.) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Indikationsteksten er ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

Der foreligger ikke strukturerede data om advarsler, kontraindikationer eller interaktioner. Der er ikke fundet registrerede lægemiddelinteraktioner. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Litteraturen indeholder dog signaler, som bør vurderes ved enhver anvendelse til aurarelaterede tilstande. Det gælder en case report om cerebral arterievasokonstriktion efter galcanezumabs startdosis (PMID 39365416) og et studie af cerebrovaskulær risiko ved CGRP-antistoffer (PMID 42390441).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om heparin-cofaktor-2-mangel er udelukkende modelbaseret (L5) uden kliniske forsøg, litteratur eller plausibel mekanisme. Den bør ikke forfølges.

**For at komme videre kræves følgende:**
- Hvis der ønskes et repurposing-spor, bør fokus flyttes til migræne med hjernestammeaura, hvor evidensen er indirekte (L4). Der skal da indhentes data specifikke for denne undertype.
- Gennemgang af cerebrovaskulære sikkerhedsdata (bl.a. PMID 42390441 og 39365416) før enhver anvendelse til aurasubtyper.
- Hentning og gennemgang af SmPC for advarsler og kontraindikationer, da disse data mangler.
- Supplerende data om virkningsmekanisme fra lægemiddeldatabasen.
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

