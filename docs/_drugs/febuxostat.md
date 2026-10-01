---
layout: default
title: Febuxostat
parent: Moderat evidens (L3-L4)
nav_order: 188
evidence_level: L4
indication_count: 6
---

# Febuxostat
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **6** stk.
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

# Febuxostat: Fra hyperurikæmi til renal hypourikæmi

## Resumé i få sætninger

Febuxostat er en xanthinoxidasehæmmer, der markedsføres i Danmark som Adenuric. Midlet er kendt som urinsyresænkende behandling, men de danske data angiver ikke selve indikationsteksten. TxGNN-modellen forudsiger, at det kan være relevant ved **renal hypourikæmi**. Evidensen er meget begrænset: **1 klinisk forsøg** med uklar relevans og **2 publikationer** (en oversigtsartikel og en hypotese-/case-baseret artikel).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske registerdata (febuxostat er kendt som urinsyresænkende middel ved hyperurikæmi) |
| Foreslået ny indikation | Renal hypourikæmi (hypouricemia, renal) |
| TxGNN-prædiktionsscore | 99,99 % |
| Evidensniveau | L4 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne prædiktion rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om virkningsmekanismen. Febuxostat tilhører gruppen af ikke-purin selektive xanthinoxidoreduktase-hæmmere (XOR-hæmmere), og lægemidlet sænker dannelsen af urinsyre.

Ved renal hypourikæmi, fx ved tab af funktion i urattransportørerne URAT1 eller GLUT9, er der risiko for træningsudløst akut nyreskade. Man antager, at en høj urinsyrebelastning i urinen og oxidativt stress spiller en rolle. XOR-hæmmere er foreslået som en mulig måde at mindske udskillelsen af urinsyre og dannelsen af XOR-afledte reaktive iltforbindelser. Det giver en plausibel, men indirekte begrundelse.

Der er dog en vigtig modsætning: febuxostat sænker i forvejen serum-urat, og patienter med hypourikæmi har allerede for lavt niveau. Sikkerheden ved denne tilgang er derfor uafklaret. TxGNN-scoren er en beregnet prædiktion og udgør ikke klinisk støtte.

---

## Klinisk evidens fra forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT04398251](https://clinicaltrials.gov/study/NCT04398251) | Fase 4 | Ukendt | 100 | Undersøger effekten af urinsyrekontrol på recidiv af nyresten og nyrefunktion hos patienter med stenlidelse og hyperurikæmi (Shanghai Xu-hui Central Hospital, 2020-2022). Relevansen for renal hypourikæmi kan ikke bekræftes (vurderet som grad C), og forsøget tæller ikke som direkte fase 2- eller fase 3-evidens. |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [36754409](https://pubmed.ncbi.nlm.nih.gov/36754409/) | 2023 | Review/hypotese | Internal Medicine | Beskriver en 16-årig japansk fodboldspiller med familiær renal hypourikæmi (URAT1-mutationer) og gentagne træningsudløste akutte nyreskader. Hydrering forebyggede ikke tilfældene, og man overvejede febuxostat som profylakse. Det fremgår ikke af de foreliggende data, hvad udfaldet var. |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Review | Clinical Rheumatology | Narrativ oversigt over hypourikæmi (serum-urat < 2 mg/dL), dens årsager og relevans for reumatologer. Indeholder ikke febuxostat-specifikke effektdata. |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104019206 | Adenuric (Menarini International Operation Luxembourg S.A.) | Filmovertrukne tabletter | Ikke angivet i de tilgængelige data |

---

## Sikkerhedsovervejelser

Der er ikke fundet registrerede lægemiddelinteraktioner i de tilgængelige data. Produktresuméets advarsler og kontraindikationer er ikke indlæst.

Ud fra den foreslåede indikation er følgende forhold særligt vigtige:
- **Yderligere sænkning af serum-urat:** febuxostat sænker urinsyre hos patienter, der allerede har for lave værdier, og sikkerheden er ikke afklaret.
- **Generelt for XOR-hæmning:** hypoxanthin og xanthin stiger, så man skal være opmærksom på xanthin-nefropati og stendannelse.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Evidensen er på modelprædiktionsniveau (L4). Det eneste forsøg er af uklar relevans, og litteraturen består af en oversigtsartikel og en hypotesebaseret case. Der er en uafklaret sikkerhedsmæssig modsætning, fordi et urinsyresænkende middel foreslås til patienter, der i forvejen har for lav urinsyre.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer), som blokerer sikkerhedsscreeningen.
- Detaljerede data om virkningsmekanismen (fx fra DrugBank).
- Kontrol af de fulde forsøgsdata for NCT04398251 samt resultatet i den beskrevne case (PMID 36754409).
- En vurdering af, om serum-urat og urinsyreudskillelse kan monitoreres sikkert, før man overvejer et kontrolleret studie.

Datapakken indeholder også prædiktioner for partiel HPRT-mangel og Lesch-Nyhan syndrom. De er ikke vurderet i denne rapport.

*Resultaterne er udelukkende til forskningsformål og udgør ikke medicinsk rådgivning. Lægemiddelkandidater til nye indikationer kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

