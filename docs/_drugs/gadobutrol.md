---
layout: default
title: Gadobutrol
parent: Kun modelforudsigelse (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Gadobutrol
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

# Gadobutrol: Fra MRI-kontrastforstærkning til benign prostatahyperplasi

## Resumé på én sætning

Gadobutrol (Gadovist®) er en makrocyklisk gadolinium-baseret kontrastagent, der administreres intravenøst for at forbedre MRI af centralnervesystemet og vaskulaturen — det er en **diagnostisk billeddiagnostisk agent**, ikke et terapeutisk lægemiddel.
TxGNN-modellen forudsiger, at det kan være effektivt mod **benign prostatahyperplasi (BPH)**,
med **0 kliniske forsøg** og **0 publikationer**, der i øjeblikket støtter denne terapeutiske retning.

> **Kritisk klinisk bemærkning:** Gadobutrol har ingen farmakologisk effekt på vævet hos mennesker. Modellens BPH-forudsigelse skyldes næsten helt sikkert dets etablerede brug som kontrastagent i prostat mpMRI — en diagnostisk samforekomst, ikke et terapeutisk forhold.

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Original indikation | MRI-kontrastforstærkning (CNS-billeddiagnostik, MR-angiografi) |
| Forudsagt ny indikation | Benign prostatahyperplasi |
| TxGNN-forudsigelsesscore | 83.24% |
| Evidensniveau | L5 |
| Status på Danmarks marked | Ikke registreret (datakløft — Gadovist® har EMA-centraliseret godkendelse, der er gyldig i alle EU/EØS-medlemsstater, herunder Danmark) |
| Antal markedsføringstilladelser | 0 (data blev ikke indsamlet — verificer via Lægemiddelstyrelsen) |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanisme-for-virknings-data ikke tilgængelige fra Evidence Pack. Baseret på kendt farmakologi er gadobutrol en 1,0-molar makrocyklisk gadolinium-chelat, der fungerer udelukkende som et paramagnetisk MRI-kontrastagent. Det forkorter T1-relaksationstider for omgivende vandprotoner og øger signalintensiteten på T1-vægtede sekvenser. Gadobutrol har **ingen farmakologisk aktivitet** ved nogen kendt biologisk receptor, enzym eller cellulært target — dets eneste mekanisme er fysisk interaktion med vandmolekyler i et magnetfelt.

TxGNN-modellens forudsigelse af BPH skyldes næsten helt sikkert diagnostisk samforekomst snarere end terapeutisk potentiale. Multiparametrisk MRI (mpMRI) — som bruger gadobutrol til dynamiske kontrast-forstærkede (DCE) sekvenser — er nu standardundersøgelsen før biopsi for prostatbetingelser, herunder BPH og prostatakræft. Modellen ser ud til at have lært dette diagnostiske forhold og misklassificeret det som et repurposering-signal.

Der er ingen kendt biologisk mekanisme, hvorved et gadolinium-chelat kunne terapeutisk ændre prostat-stromal proliferation, reducere blæreudsletningsobstruktion eller modulere de androgeniske veje, der ligger til grund for BPH. En meningsfuld repurposering-hypotese ville kræve identifikation af helt nye og i øjeblikket ikke-eksisterende mekanisme-evidens.

---

## Evidens fra kliniske forsøg

I øjeblikket registreret ingen relaterede kliniske forsøg for gadobutrol i benign prostatahyperplasi.

> **Kontekst om lavere-rangerede forudsigelser:** Gadobutrol har klinisk forsøgs-evidens forbundet til **perifer arteriel sygdom** (rang 3, TxGNN-score 76.72%) og **perifer vaskulær sygdom** (rang 7, TxGNN-score 74.39%), med 4 forsøg hver. Imidlertid bruger alle disse forsøg gadobutrol som en **diagnostisk kontrastagent** til MR-angiografi (MRA) — ikke som en terapeutisk intervention. De bekræfter dets billeddiagnostiske nytte ved vaskulær sygdom, men giver intet grundlag for terapeutisk repurposering.

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig for gadobutrol i benign prostatahyperplasi.

> **Kontekst om lavere-rangerede forudsigelser:** De 20 PubMed-publikationer, som blev hentet for perifer arteriel sygdom (rang 3–4), er ensartet billeddiagnostiske studier, som evaluerer gadobutrol-forstærkede MRA-teknikker, billedkvalitetsammenligninger med andre kontrastagenter og diagnostisk nøjagtighed versus digital subtraktion-angiografi (DSA). Representative eksempler er anført nedenfor for fuldstændighed, men disse repræsenterer **diagnostisk** — ikke terapeutisk — evidens.

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|---------|-------------|
| [26001243](https://pubmed.ncbi.nlm.nih.gov/26001243/) | 2015 | RCT | AJR Am J Roentgenology | Stort randomiseret studie sammenlignet gadobutrol vs. gadoterat meglumin til 3T MRA i PAOD; non-inferiøritet påvist |
| [12928960](https://pubmed.ncbi.nlm.nih.gov/12928960/) | 2003 | Prospektivt | European Radiology | Prospektivt multicenterstudie blindet sammenligning af gadobutrol-forstærket moving-table MRA vs. DSA hos 203 patienter med PAOD |
| [22848033](https://pubmed.ncbi.nlm.nih.gov/22848033/) | 2012 | RCT | J Magn Reson Imaging | Randomiseret crossover-studie af gadoterat 0,5M vs. gadobutrol 1,0M til perifer MRA på 3,0T |
| [20959539](https://pubmed.ncbi.nlm.nih.gov/20959539/) | 2010 | Prospektivt | Radiology | Evaluering af højopløsnings 3T perifer MRA-protokol med lav-dose gadobutrol (0,1 mmol/kg) vs. konventionel angiografi |
| [15149986](https://pubmed.ncbi.nlm.nih.gov/15149986/) | 2004 | Prospektivt | AJR Am J Roentgenology | Hele-legeme 3D MRA med gadobutrol hos 51 PAOD-patienter; diagnostisk præstation vs. DSA |
| [19652610](https://pubmed.ncbi.nlm.nih.gov/19652610/) | 2009 | Prospektivt | Investigative Radiology | Enkelt-dose (0,1 mmol/kg) gadobutrol perifer CTM-MRA kombineret med tids-opløst TWIST-MRA på 3,0T |
| [12928957](https://pubmed.ncbi.nlm.nih.gov/12928957/) | 2003 | Sikkerhedsstudie | European Radiology | Sikkerhedsevaluering af 1,0M gadobutrol hos 435 patienter, der undergår CE-MRA; bivirkningsprofil |
| [23188773](https://pubmed.ncbi.nlm.nih.gov/23188773/) | 2013 | Prospektivt | J Magn Reson Imaging | Diagnostisk nøjagtighed af multi-station CE-MRA af underekstremiteter vs. DSA hos symptomatisk PAOD |
| [24156379](https://pubmed.ncbi.nlm.nih.gov/24156379/) | 2013 | Prospektivt | J Cardiovasc Magn Reson | Steady-state vaskulær billeddiagnostik med gadobutrol som tillæg til perifer MRA-protokol |
| [12720266](https://pubmed.ncbi.nlm.nih.gov/12720266/) | 2003 | Pilot | J Magn Reson Imaging | Første erfaring med 1M gadobutrol til hele-legeme 3D MRA dækkende karotider til runoff-kar på 72 sekunder |

---

## Information om Danmarks marked

Gadobutrol (Gadovist®) optræder ikke i de data, som blev indsamlet for Lægemiddelstyrelsens database. Dette er et **datakløft**, ikke fravær fra markedet — Gadovist® har en centraliseret markedsføringstilladelse fra Det Europæiske Lægemiddel-agentur (EMA), som automatisk er gyldig i Danmark og alle EU/EØS-medlemsstater. Sundhedsfaglige personale bør verificere den aktuelle produktlisting direkte.

> Bekræft venligst den aktuelle danske markedsstatus via [Lægemiddelstyrelsens produktdatabase](https://www.laegemiddelstyrelsen.dk) eller [EMA medicin-søgning](https://www.ema.europa.eu/en/medicines/find-medicine).

---

## Sikkerhedshensyn

Henviser venligst til det godkendte produktresumé (SmPC) for fuldstændig sikkerhedsinformation.

> Som baggrundskontekst for gadolinium-baserede kontrastagenter (GBCA'er) som en klasse: makrocykliske agenter såsom gadobutrol har en betydeligt lavere risiko for gadolinium-deposition og nephrogen systemisk fibrose (NSF) sammenlignet med lineære GBCA'er på grund af deres mere termodynamisk og kinetisk stabil chelat-struktur. Kontraindikationer omfatter typisk alvorlig nyresvækkelse for lineære agenter; makrocykliske agenter har en mere gunstig nyresikkerhedsprofil. Det fuldstændige produktresumé bør konsulteres før enhver klinisk brug.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Gadobutrol er en diagnostisk MRI-kontrastagent uden kendt terapeutisk mekanisme relevant for benign prostatahyperplasi eller nogen af de øvrige forudsagte indikationer. TxGNN-scoren på 83.24% for BPH skyldes næsten helt sikkert diagnostisk samforekomst (rutinebrug i prostat mpMRI) snarere end terapeutisk potentiale, og ingen understøttende klinisk eller præklinisk evidens eksisterer (evidensniveau L5). Desuden repræsenterer de vaskulære sygdoms-forudsigelser (rang 3–8), selvom de er understøttet af en væsentlig billeddiagnostisk litteratur, diagnostisk — ikke terapeutisk — evidens.

**For at fortsætte er følgende nødvendigt:**

- **Regulatorisk data-forbedring:** Verificer og udfyld Danmarks/EMA markedsføringstilladelsesoplysninger for Gadovist® — aktuelle data viser nul licenser, hvilket er uforenelig med dets EMA-centraliserede tilladelsestatus
- **Modelartefakt-gennemgang:** Undersøg, om TxGNN BPH-forudsigelsen opstår fra diagnostisk samforekomst i træningsdata (prostat mpMRI-brug); hvis bekræftet, bør denne kandidat markeres som en kendt modelsbegrænsning
- **Mekanisme-hypotese:** Hvis der opstår ny hypotese, der antyder, at gadolinium-chelater har direkte cellulær aktivitet i prostat-væv, ville målrettede prækliniske studier være nødvendige før nogen klinisk udvikling kan overvejes
- **Vaskulær indikations-genfortolkning:** Evidensen for perifer arteriel sygdom / perifer vaskulær sygdom (rang 3–8) bør omklassificeres som **diagnostisk brugsbevis**, ikke terapeutisk repurposering-evidens, og pipeline-scoringslogikken bør opdateres i overensstemmelse hermed

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

