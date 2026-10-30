---
layout: default
title: Vandetanib
parent: Kun modelforudsigelse (L5)
nav_order: 876
evidence_level: L5
indication_count: 10
monitor_inn: "Vandetanib"
predicted_indications: ["renal cell carcinoma (disease)", "unclassified renal cell carcinoma", "renal cell carcinoma associated with neuroblastoma", "renal cell carcinoma associated with Xp11.2 translocations/TFE3 gene fusions", "renal pelvis carcinoma", "clear cell renal carcinoma", "childhood kidney cell carcinoma", "renal carcinoma", "angiolipoma", "familial spontaneous pneumothorax"]
last_modified_at: 2026-10-30
description: "Vandetanib: forudsagt ny indikation Nyrecellekarcinom (evidensniveau L5). Oprindelig indikation: Skjoldbruskkirtelkarcinom"
---

# Vandetanib
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

## Vandetanib: Fra skjoldbruskkirtelkarcinom til nyrecellekarcinom
{: .text-alpha }

## Resumé i én sætning

Vandetanib er en oral tyrosinkinasehæmmer, som i den viden, der ligger til grund for modellen, er knyttet til skjoldbruskkirtelkarcinom. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **nyrecellekarcinom**. Evidensen består af **4 kliniske forsøg** (3 fase 2-forsøg og 1 fase 1/2-forsøg direkte på nyrekræft, hvoraf 2 er afsluttet) og en række publikationer, men ingen offentliggjorte effektresultater.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Skjoldbruskkirtelkarcinom (relation registreret i vidensgrafen; den danske markedsføringstilladelse indeholder ingen indikationstekst) |
| Forudsagt ny indikation | Nyrecellekarcinom |
| TxGNN-forudsigelsesscore | 0,9992 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Antal godkendelser | 1 national markedsføringstilladelse |
| Anbefalet beslutning | Hold |

Evidensniveauet er sat til L5. De fire forsøg undersøger nyrekræft, men der er ingen publicerede resultater, og to af dem blev afsluttet tidligt med henholdsvis 3 og 7 patienter. Dermed er der ikke noget fortolkeligt datagrundlag for effekt ved nyrecellekarcinom. Den datakompilering, der ligger til grund for rapporten, vurderede selv evidensen som L2. Jeg har dog ikke kunnet finde noget publiceret studie med resultater, der understøtter dette.

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i den datakompilering, der ligger til grund for rapporten. Ud fra den kendte biologi hæmmer vandetanib VEGFR2, EGFR og RET. Hæmning af VEGFR2 (anti-angiogenese) er en veletableret mekanisme ved nyrecellekarcinom.

Ved klarcellet nyrecellekarcinom, især ved von Hippel-Lindau-sygdom, fører tab af VHL til ophobning af HIF og overekspression af VEGF. Det gør tumorerne afhængige af nydannelse af blodkar. Skjoldbruskkirtelkarcinom og nyrecellekarcinom er forskellige sygdomme, men en fælles angiogenesemekanisme kan forklare, hvorfor modellen forbinder dem.

Der er dog vigtige forbehold. De tilgængelige forsøg viser ingen klar positiv effekt, og der findes allerede godkendte lægemidler til nyrecellekarcinom. Det eneste afsluttede randomiserede forsøg (NCT01191892) omhandlede urotelialt karcinom og ikke nyrecellekarcinom.

## Evidens fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Vigtigste fund |
|---------|------|------|------|---------|
| [NCT01372813](https://clinicaltrials.gov/study/NCT01372813) | Fase 2 | Afsluttet tidligt | 3 | Vandetanib ved fremskreden klarcellet nyrekræft. Stoppet efter kun 3 patienter, ingen brugbare data |
| [NCT00566995](https://clinicaltrials.gov/study/NCT00566995) | Fase 2 | Afsluttet | 37 | Vandetanib ved von Hippel-Lindau-sygdom med nyretumorer. Arvelig subpopulation, resultater ikke tilgængelige |
| [NCT02495103](https://clinicaltrials.gov/study/NCT02495103) | Fase 1/2 | Afsluttet tidligt | 7 | Vandetanib + metformin ved HLRCC-/SDH-associeret eller sporadisk papillær nyrekræft. Stoppet med 7 patienter, ingen fortolkelige effektdata |
| [NCT01191892](https://clinicaltrials.gov/study/NCT01191892) | Fase 2 | Afsluttet | 82 | Randomiseret: carboplatin + gemcitabin med eller uden vandetanib ved fremskreden urotelkræft (ikke egnet til cisplatin). Kun indirekte relevant for nyrecellekarcinom |

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Vigtigste fund |
|------|-----|------|------|---------|
| [40779213](https://pubmed.ncbi.nlm.nih.gov/40779213/) | 2025 | Oversigtsartikel | Clin Exp Metastasis | Målrettede behandlinger ved fumaratdehydratase-mangelfuld nyrecellekarcinom. Ingen standardbehandling endnu |
| [32105149](https://pubmed.ncbi.nlm.nih.gov/32105149/) | 2020 | Metaanalyse | Expert Rev Clin Pharmacol | Forekomst og risiko for proteinuri ved VEGFR-tyrosinkinasehæmmere, herunder vandetanib |
| [22651902](https://pubmed.ncbi.nlm.nih.gov/22651902/) | 2012 | Metaanalyse | Cancer Treat Rev | Behandlingsrelateret dødelighed ved VEGFR-tyrosinkinasehæmmere ved avancerede solide tumorer |
| [23981115](https://pubmed.ncbi.nlm.nih.gov/23981115/) | 2014 | Metaanalyse | Br J Clin Pharmacol | Forekomst og risiko for levertoksicitet ved antiangiogene tyrosinkinasehæmmere |
| [32691271](https://pubmed.ncbi.nlm.nih.gov/32691271/) | 2021 | Kohorte | Endocrine | Langtidsopfølgning og sikkerhed af vandetanib ved medullært skjoldbruskkirtelkarcinom |
| [24451769](https://pubmed.ncbi.nlm.nih.gov/24451769/) | 2012 | Oversigtsartikel | ASCO Educ Book | Systemisk behandling af avanceret skjoldbruskkirtelkræft, herunder vandetanib |
| [31043488](https://pubmed.ncbi.nlm.nih.gov/31043488/) | 2019 | Præklinisk | Mol Cancer Res | Musemodel for TFE3-translokationsnyrecellekarcinom; ikke direkte test af vandetanib |
| [20346054](https://pubmed.ncbi.nlm.nih.gov/20346054/) | 2011 | Præklinisk | BJU Int | Effekt af tyrosinkinasehæmmere på ophobning af antistoffet cG250 i nyrecellekarcinom-xenografter i mus |
| [26677336](https://pubmed.ncbi.nlm.nih.gov/26677336/) | 2015 | Oversigtsartikel | OncoTargets Ther | Profil af nintedanib; nævner vandetanib blandt antiangiogene midler |
| [42107510](https://pubmed.ncbi.nlm.nih.gov/42107510/) | 2026 | Oversigtsartikel | Pharmacol Res | RET-hæmmere ved RET-drevet skjoldbruskkirtel- og lungekræft |

Ingen af disse publikationer rapporterer effekt af vandetanib ved nyrecellekarcinom hos patienter.

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104777710 | Caprelsa | Filmovertrukne tabletter | Indikationstekst er ikke tilgængelig i de samlede data |

Der er registreret 1 gyldig national tilladelse til et monopræparat (Sanofi B.V.). Tilladelsen er markedsført i Danmark.

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (multikinasehæmmer mod VEGFR2, EGFR og RET) |
| Risiko for myelosuppression | Se produktresuméet (SmPC) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC). Litteraturen peger på overvågning af QT-interval, elektrolytter, blodtryk, nyrefunktion (proteinuri) og leverfunktion |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

## Sikkerhedsovervejelser

Data om advarsler og kontraindikationer fra produktresuméet er ikke tilgængelige i de samlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

- **Sygdomme med registreret kontraindikationsrelation i vidensgrafen** (ikke fra produkttekst): forhøjet blodtryk, langt QT-syndrom og torsades de pointes, hypothyreose, kaliummangel, hyperkalcæmi, nedsat nyrefunktion, interstitiel lungesygdom, hjertesvigt, hjerneiskæmi/transitorisk iskæmisk anfald og posterior leukoencefalopatisyndrom.
- **Lægemiddelinteraktioner:** 100 interaktioner er registreret. Der er flere af alvorlig grad (major), bl.a. med clarithromycin, levofloxacin, dolasetron, palonosetron, picosulfat, natriumsulfat og polyethylenglycol med elektrolytter. Flere af disse er relevante på grund af risikoen for QT-forlængelse og forstyrrelser i elektrolytbalancen. Moderate interaktioner omfatter bl.a. famotidin, metformin, loperamid, dexamethason, bisacodyl og lactitol.
- **Litteraturens sikkerhedssignaler:** QT-forlængelse, proteinuri, levertoksicitet og behandlingsrelateret dødelighed ved VEGFR-hæmmere.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Mekanismen er biologisk rimelig, men de fire forsøg på nyrekræft har ingen tilgængelige resultater, og to blev stoppet meget tidligt. Der findes allerede godkendte behandlinger til nyrecellekarcinom, og sikkerhedsprofilen (QT-forlængelse, blodtryk, proteinuri) kræver forsigtighed. Der er derfor ikke grundlag for at gå videre til klinisk anvendelse.

**For at komme videre kræves:**
- Resultater fra NCT00566995 (VHL-sygdom, n=37) og de afsluttede forsøg
- Data om virkningsmekanisme og produktresumé (advarsler, kontraindikationer) fra Lægemiddelstyrelsen
- Et velgennemført forsøg i en veldefineret nyrekræftpopulation, fx VHL-associeret eller papillær nyrecellekarcinom, med sammenligning mod nuværende standardbehandling
- En risikovurdering for hjerte- og elektrolytsikkerhed samt interaktioner
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

