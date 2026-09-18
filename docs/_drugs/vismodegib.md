---
layout: default
title: Vismodegib
parent: Kun modelforudsigelse (L5)
nav_order: 472
evidence_level: L5
indication_count: 10
---

# Vismodegib
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

# Vismodegib: Fra Basalcellekarcinom til Hudkræft Forbundet med Xeroderma Pigmentosum

## Ét-linie sammenfatning

> Vismodegib er en Hedgehog-vej (SMO) inhibitor, der bruges til at behandle avanceret/metastatisk basalcellekarcinom (BCC).
> TxGNN-modellen forudsiger, at det også kan være effektivt til **Xeroderma Pigmentosum** (en sjælden genetisk lidelse, der forårsager tilbagevendende, multiple BCC'er fra en ung alder),
> med **ingen registrerede kliniske forsøg**, men **5 understøttende publikationer**, herunder to offentliggjorte kasuistiske rapporter om vismodegib, der blev brugt med succes til xeroderma pigmentosum-patienter.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Basalcellekarcinom, avanceret/metastatisk (ifølge litteraturbevis i denne pakke; officiel dansk labelingdata endnu ikke tilgængelig — se datahuller) |
| Forudsagt ny indikation | Xeroderma Pigmentosum (tilbagevendende/multiple basalcellekarcinomer) |
| TxGNN forudsigelsesscore | 99,91% |
| Evidensniveau | L3 (klinisk evidens på kasuistisk niveau; ingen afsluttede kliniske forsøg) |
| Dansk markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Vismodegib er en lille-molekyle inhibitor af Smoothened (SMO), den vigtigste transducer af Hedgehog (Hh) signalvejen. Som beskrevet i litteraturen, der er indsamlet i denne evidenspakke, er det "en oral inhibitor af Hedgehog-signalvejen", der "er blevet brugt til at behandle basalcellekarcinom (BCC) hos voksne." Aberrant Hedgehog-vej aktivering — oftest gennem *PTCH1* eller *SMO* mutationer — er den vigtigste onkogene driver af sporadisk BCC, og derfor blev vismodegib godkendt til denne indikation.

Xeroderma pigmentosum (XP) er en autosomalt recessiv DNA-reparationsforstyrrelse (nukleotid-excisions-reparations defekt), der forårsager ekstrem UV-følsomhed og dramatisk øget livstidsrisiko for hudkræfter, især multiple, tilbagevendende BCC'er, der starter i barndommen. Det vigtigste er, at de BCC'er, der opstår hos XP-patienter, stadig er drevet af samme Hedgehog-vej dysregulering, som ses i sporadisk BCC — den underliggende DNA-reparations defekt øger *hastigheden* af onkogen mutation, men tumorets biologi nedstrøms konvergerer på samme SMO-afhængige signalering, som vismodegib retter sig mod. Dette er det mekanistiske grundlag for TxGNN-forudsigelsen, og det er direkte bekræftet af litteraturen i denne pakke: to uafhængige kasuistiske rapporter (PMID 30178564, PMID 28297142) dokumenterer vismodegib, der bruges specifikt til at behandle multiple BCC'er hos XP-patienter, hvor én rapporterer en 61% reduktion i samlet læsionsbyrde efter 16,5 måneder behandling og forebyggelse af nye læsioner, og den anden beskriver fuldstændig ophobning af et nodulært BCC hos en 8-årig XP-patient efter 4 måneders terapi.

Det er værd at bemærke, at den enkelte højest-scorede TxGNN-kandidat i denne pakke, **medulloblastom med omfattende nodularitet (MBEN)** (score 99,93%), er mekanistisk endnu mere direkte — MBEN er en Hedgehog-vej-drevet medulloblastom-subtype, for hvilken SMO-inhibitorer er en rationel målrettet terapi. Denne pakke indeholder imidlertid i øjeblikket **nul kliniske forsøg eller publikationer** for denne kandidat. Den begrundelse, der blev genereret sammen med denne forudsigelse, markerer selv dette som et formodet evidensindsamlingshul snarere end en sand mangel på bevis, og anbefaler en manuel PubMed/ClinicalTrials.gov søgning for at bekræfte, før denne kandidat bliver scoret eller der handles på den. Flere andre kandidater i denne pakke (annulær epidermolytisk ichthyosis, epidermolysis bullosa simplex med plettet pigmentering, prostata-/hjerne-kræftsusceptibilitet) har ingen mekanistisk forbindelse til Hedgehog-vejen og ingen understøttende bevis, og de er markeret i selv kildedata som sandsynlige knowledge-graph falske positiver (semantisk klyngedannelse omkring "hudlidelse" eller "kræftsusceptibilitet" noder snarere end sand biologisk signal).

---

## Klinisk forsøgsbevis

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtige resultater |
|------|-----|------|------|---------|
| [35283513](https://pubmed.ncbi.nlm.nih.gov/35283513/) | 2021 | Oversigt | Indian Journal of Dermatology | Gennemgår nuværende terapeutiske strategier for XP, herunder solundgåelse, kirurgi, laser-/fotodynamisk terapi, retinoider, 5-FU, imiquimod og fotolyase-baserede tilgange |
| [30178564](https://pubmed.ncbi.nlm.nih.gov/30178564/) | 2018 | Kasuistisk rapport | Pediatric Dermatology | Vismodegib brugt til at behandle multiple BCC'er hos en XP-patient; 61% reduktion i samlet læsionsdiameter efter 16,5 måneder, med forebyggelse af nye læsioner (en læsion forværredes senere) |
| [28297142](https://pubmed.ncbi.nlm.nih.gov/28297142/) | 2017 | Kasuistisk rapport | Pediatric Dermatology | Vismodegib 150 mg/day ryddet et nodulært BCC på næsetippen hos en 8-årig XP-patient efter 4 måneder, på et sted, der ikke var egnet til Mohs-kirurgi |
| [33901791](https://pubmed.ncbi.nlm.nih.gov/33901791/) | 2021 | Kasuistisk rapport | European Journal of Cancer | Kombination af målrettet terapi og immun-checkpoint-blokering hos en XP-patient med aggressivt angiosarkom og tilbagevendende, ikke-resektabel BCC |
| [36921168](https://pubmed.ncbi.nlm.nih.gov/36921168/) | 2023 | Kasuistisk rapport | Revista Paulista de Pediatria | Generel XP-kasuistisk rapport, der understreger tidlig diagnose og genkendelse af tegn/symptomer (ikke vismodegib-specifik) |

---

## Dansk markedsinformation

Vismodegib har i øjeblikket **ingen markedsføringstilladelser på record i Danmark** (0 licenser; markedsstatus: ikke markedsført). Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) tilladelsesdata er tilgængelige i denne evidenspakke for lokale produkt-/doseringsform-detaljer.

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitets klassifikation | Målrettet terapi (Hedgehog-vej / SMO-inhibitor) — en ikke-cytotoksisk lille molekyle, baseret på mekanisme beskrevet i litteraturen inden for denne evidenspakke |
| Myelosuppressions risiko | Se venligst resuméet af produktegenskaber (SmPC) advarsler og forholdsregler |
| Emetogenicitets klassifikation | Se venligst resuméet af produktegenskaber (SmPC) advarsler og forholdsregler |
| Overvågningspunkter | Se venligst resuméet af produktegenskaber (SmPC) advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se venligst resuméet af produktegenskaber (SmPC) advarsler og forholdsregler |

---

## Sikkerhedshensyn

Se venligst det godkendte resumé af produktegenskaber (SmPC) for sikkerhedsinformation. En medicin-medicin interaktionssøgning returnerede ingen resultater, og ingen formelle advarsler, kontraindikationer eller interaktionsdata er i øjeblikket tilgængelige i denne evidenspakke.

---

## Konklusion og næste skridt

**Beslutning: Afvent**

**Begrundelse:**
- Vismodegib markedsføres i øjeblikket ikke i Danmark (0 tilladelser), og ingen kliniske forsøg understøtter nogen af de kandidat-indikationer, som TxGNN har identificeret for dette lægemiddel.
- Det stærkeste tilgængelige bevis — to kasuistiske rapporter om vismodegib brugt til XP-forbundet BCC — er ægte og mekanistisk sammenhængende, men forbliver på kasuistisk niveau (L3), langt under den tærskel, der er nødvendig for en Go-beslutning.
- Et **blokerende datahul** eksisterer for det officielle produktmærkat (advarsler/kontraindikationer), som forhindrer denne kandidat i at komme ind i S1 sikkerhedspræ-vurderingsstadiet, uanset hvor lovende effektivitetssignalet er.

**For at fortsætte er følgende nødvendig:**
- Officielle danske/EU SmPC-data (advarsler, kontraindikationer) — i øjeblikket et blokerende datahul
- Bekræftet mekanisme-for-virkning dokumentation fra DrugBank — i øjeblikket et datahul af høj alvorlighed
- En manuel litteratur-/forsøgssøgning for at verificere, om den højest-rangerede kandidat (medulloblastom med omfattende nodularitet, TxGNN score 99,93%) virkelig mangler understøttende bevis, eller om dette afspejler et databas-indsamlingshul, som angivet i kildebegrundelsen
- Præcisering af den regulatoriske vej (f.eks. navngivet-patient behandling, off-label protokol), hvorigennem XP-forbundet tilbagevendende BCC kunne behandles med vismodegib i Danmark, givet at lægemidlet ikke markedsføres lokalt

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

