---
layout: default
title: Sunitinib
parent: Kun modelforudsigelse (L5)
nav_order: 412
evidence_level: L5
indication_count: 10
---

# Sunitinib
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

# Sunitinib: Fra godkendte kræftindikationer til liposarkom

## Resumé

Sunitinib er en oral multikinasehæmmer, der markedsføres i Danmark som kapsler til behandling af kræft. Evidence Pack'en angiver ingen original indikation i den danske registrering.
TxGNN-modellen forudsiger, at sunitinib kan være virksomt mod **liposarkom**. Understøttelsen er **2 afsluttede fase 2-forsøg i non-GIST-sarkom**, **1 publiceret fase 2-studie** og **1 kasuistik** om et enkelt tilfælde.
Alle data er fra enkeltarmede studier, og der er ikke isoleret et liposarkomspecifikt effektsignal.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Original indikation | Ikke oplyst i den danske registrering. Sunitinib er generelt kendt fra bl.a. nyrecellekarcinom, så se produktresuméet (SmPC) |
| Forudsagt ny indikation | Liposarkom |
| TxGNN-prædiktionsscore | 99,87 % |
| Evidensniveau | L2 (se bemærkning nedenfor) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

Bemærkning om evidensniveau: L2 er tildelt i Evidence Pack'en. De bagvedliggende studier er dog enkeltarmede fase 2-studier uden randomisering og uden fase 3-data. Niveauet bør derfor læses forsigtigt.

---

## Hvorfor er denne prædiktion rimelig?

Sunitinib hæmmer flere receptor-tyrosinkinaser, bl.a. VEGFR, PDGFR, KIT, RET og FLT3. Det kan hæmme tumorens nydannelse af blodkar (angiogenese) og PDGFR-signalering i bløddelssarkomer. Detaljerede mekanismedata fra DrugBank mangler dog i Evidence Pack'en.

Liposarkom er en af de hyppigste bløddelssarkomer hos voksne. Avanceret sygdom har få medicinske behandlingsmuligheder ud over kirurgi. Angiogenese og PDGFR-signalering spiller en rolle i sarkombiologi, og sunitinib er veletableret i andre solide tumorer med lignende signalveje. Det gør en effekt biologisk plausibel.

Den høje TxGNN-score er en modelforudsigelse og ikke bevis for klinisk effekt. Kilderne viser ikke et stærkt liposarkomspecifikt signal, fordi fase 2-studierne inkluderer flere sarkomtyper samlet.

---

## Evidens fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal patienter | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT00400569](https://clinicaltrials.gov/study/NCT00400569) | Fase 2 | Afsluttet | 48 | Åbent enkeltcenterstudie af sunitinib ved metastatisk eller inoperabelt bløddelssarkom (bl.a. leiomyosarkom, liposarkom, fibrosarkom, MFH). Liposarkom-undergruppen er ikke isoleret i de foreliggende data |
| [NCT00474994](https://clinicaltrials.gov/study/NCT00474994) | Fase 2 | Afsluttet | 53 | Multicenterstudie af kontinuerlig sunitinib-dosering ved non-GIST-sarkom. Populationen omfatter sandsynligvis liposarkom |
| [NCT02048371](https://clinicaltrials.gov/study/NCT02048371) | Fase 2 | Afsluttet | 131 | SARC024 undersøger regorafenib, ikke sunitinib. Har kun værdi som klassekontekst for multikinasehæmmere ved sarkom |

Der er ikke registreret EudraCT-numre eller ICTRP-forsøg i datagrundlaget.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [21154746](https://pubmed.ncbi.nlm.nih.gov/21154746/) | 2011 | Fase 2-studie | Int J Cancer | Enkeltcenterstudie af sunitinib ved recidiverende/refraktære bløddelssarkomer med fokus på leiomyosarkom, liposarkom og MFH |
| [23482782](https://pubmed.ncbi.nlm.nih.gov/23482782/) | 2013 | Kasuistik | Anticancer Res | Langvarig klinisk gavn af sunitinib hos én kraftigt forbehandlet patient med metastatisk liposarkom |
| [38254762](https://pubmed.ncbi.nlm.nih.gov/38254762/) | 2024 | Review | Cancers | Genetiske, epigenetiske og transkriptomiske ændringer i liposarkom med henblik på valg af målrettet behandling |
| [24555529](https://pubmed.ncbi.nlm.nih.gov/24555529/) | 2014 | Review | Expert Rev Anticancer Ther | Nye behandlingsmuligheder ved bløddelssarkom hos voksne |
| [22987955](https://pubmed.ncbi.nlm.nih.gov/22987955/) | 2012 | Review | Ann Oncol | Histologidrevet behandling af bløddelssarkomer. Trabectedin fremhæves ved liposarkom |
| [24712007](https://pubmed.ncbi.nlm.nih.gov/24712007/) | 2014 | Review | Magy Onkol | Medicinsk behandling af bløddelssarkomer ud fra histologisk subtype |
| [28423517](https://pubmed.ncbi.nlm.nih.gov/28423517/) | 2017 | Genomisk studie | Oncotarget | Sekventering af ekstraskeletalt myxoidt chondrosarkom, herunder prædiktive faktorer for effekt af sunitinib. Anden tumortype |
| [25884155](https://pubmed.ncbi.nlm.nih.gov/25884155/) | 2015 | Forsøgsprotokol | BMC Cancer | REGOSARC: randomiseret fase 2-studie af regorafenib. Studerer ikke sunitinib |

PMID 38717131 (case series om en anden sarkomtype) er udeladt, fordi den ikke er relevant for sunitinib ved liposarkom.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106347719 | Sunitinib "Accord" (Accord Healthcare S.L.U.) | Kapsler, hårde | Ikke oplyst i datagrundlaget |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksisk klassifikation | Målrettet behandling (multikinasehæmmer) |
| Risiko for knoglemarvssuppression | Middel (neutropeni og trombocytopeni er kendte bivirkninger) |
| Emetogenicitet | Lav til middel |
| Monitoreringspunkter | Fuldt blodbillede med differentialtælling, leverfunktion, nyrefunktion, blodtryk, skjoldbruskkirtelfunktion og hjertefunktion |
| Håndtering og beskyttelse | Følg lokale retningslinjer for håndtering af cytostatika og antineoplastiske lægemidler |

Evidence Pack'en indeholder ingen toksicitetsdata. Ovenstående er generel klassifikation, og de endelige krav fremgår af produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Evidensen består af enkeltarmede fase 2-studier i blandede sarkomtyper og en enkelt kasuistik. Der er ingen randomiserede data og intet isoleret liposarkomspecifikt effektsignal. Sikkerhedsdata fra Lægemiddelstyrelsen mangler desuden, hvilket blokerer den videre sikkerhedsvurdering. Den høje TxGNN-score kan ikke erstatte klinisk evidens.

**For at komme videre kræves:**
- Produktresumé (SmPC) fra Lægemiddelstyrelsen med advarsler og kontraindikationer
- Mekanismedata (MOA) fra DrugBank
- Liposarkom-specifikke resultater fra NCT00400569, NCT00474994 og PMID 21154746
- Sammenligning med de etablerede alternativer ved liposarkom, f.eks. doxorubicin, ifosfamid og trabectedin
- Vurdering af anvendelse uden for godkendt indikation (off-label)

Evidence Pack'en indeholder også andre forudsigelser. Ikke-klarcellet og uklassificeret nyrecellekarcinom har stærkere evidens (L2, "Proceed with Guardrails"), men ligger tættere på sunitinibs eksisterende anvendelse. Flere nicheindikationer (ovariel myxoid liposarkom, neuroblastom-associeret og TFE3-translokations-RCC) ser ud til at skyldes ontologimapning snarere end uafhængige kliniske signaler.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepositionering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

