---
layout: default
title: Oteracil
parent: Høj evidens (L1-L2)
nav_order: 614
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-28
monitor_inn: "oteracil"
predicted_indications: ["colonic neoplasm", "cecum villous adenoma", "cecum neuroendocrine tumor G1", "lipoma of colon", "cecal disease", "rectosigmoid junction neoplasm", "benign neoplasm of cecum", "colonic lymphangioma", "colon leiomyoma", "cavernous hemangioma of colon"]
description: "Oteracil: forudsagt ny indikation Colonic neoplasm (evidensniveau L1). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Oteracil
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
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

## Oteracil: Colonic neoplasm
{: .text-alpha }

## Opsummering

Oteracil er en komponent i kombinationspræparatet S-1 (tegafur/gimeracil/oteracil), som oprindeligt anvendes til behandling af mavekræft.
TxGNN-modellen forudsiger, at det kan have effekt ved **colonic neoplasm (tyktarmsneoplasi)**,
og der er i de data, der er indsamlet til denne rapport, **6 kliniske forsøg** og **10 publikationer** inden for denne retning. Det bør bemærkes, at den kliniske effekt stammer fra tegafur, mens oteracils rolle er at reducere toksicitet i mave-tarm-kanalen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Colonic neoplasm |
| TxGNN-forudsigelsesscore | 0.9999 |
| Evidensniveau | L1 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er denne forudsigelse rimelig?

Oteracil er en del af S-1, en oral fluoropyrimidin-baseret kombination. Tegafur er et prodrug af 5-FU, gimeracil hæmmer enzymet DPD og forlænger dermed 5-FU-eksponeringen, og oteracil hæmmer OPRT i mave-tarm-slimhinden og mindsker dermed gastrointestinal toksicitet. Detaljerede data om oteracils egen virkningsmekanisme (MOA) er ikke tilgængelige; sammenhængen er udledt af den kendte farmakologi for S-1.

Mavekræft og tyktarmskræft er begge gastrointestinale tumorer, og tyktarmskræft behandles standardmæssigt med 5-FU-baseret kemoterapi. Den mekanistiske kobling er derfor stærk.

Det er dog vigtigt at understrege, at den kliniske gavn kommer fra tegafur. Evidensen understøtter derfor S-1 som kombinationspræparat og ikke oteracil som enkeltstof.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT00660894](https://clinicaltrials.gov/study/NCT00660894) | Fase 3 | Afsluttet | 1535 | Randomiseret sammenligning af UFT+leucovorin og S-1 (TS-1) som adjuverende behandling ved stadie III-tyktarmskræft |
| [NCT03448549](https://clinicaltrials.gov/study/NCT03448549) | Fase 3 | Ukendt | 1191 | SOX (oxaliplatin + S-1) versus XELOX som adjuverende behandling ved stadie III-kolorektalkræft |
| [NCT00974389](https://clinicaltrials.gov/study/NCT00974389) | Fase 2 | Ukendt | 40 | S-1 + bevacizumab ved inoperabel eller recidiverende kolorektalkræft efter tidligere kemoterapi |
| [NCT02618356](https://clinicaltrials.gov/study/NCT02618356) | Fase 2 | Ukendt | 82 | Raltitrexed + S-1 ved metastatisk kolorektalkræft efter svigt af standardkemoterapi; primært endepunkt er median progressionsfri overlevelse |
| [NCT06255379](https://clinicaltrials.gov/study/NCT06255379) | Fase 2 | Endnu ikke i rekruttering | 52 | Enkeltarmet studie af fruquintinib + tegafur/gimeracil/oteracil som tredjelinjebehandling ved avanceret metastatisk kolorektalkræft |
| [NCT02216149](https://clinicaltrials.gov/study/NCT02216149) | Fase 2 | Afbrudt | 20 | Effekt af S-1 og capecitabin med oxaliplatin på koronar blodgennemstrømning; sikkerheds-/fysiologistudie uden effektvurdering |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [21084813](https://pubmed.ncbi.nlm.nih.gov/21084813/) | 2010 | Retrospektivt kohortestudie | Gan to Kagaku Ryoho | Risikofaktorer for alvorlig hæmatologisk toksicitet (grad 3-4: 16,1 %) hos 87 patienter med S-1 + irinotecan |
| [20811661](https://pubmed.ncbi.nlm.nih.gov/20811661/) | 2010 | Præklinisk (xenograft) | Oncology Reports | Irinotecan overvinder 5-FU-resistens i tyktarmskræft-xenografter ved nedregulering af thymidylatsyntase; kombination med S-1 øgede antitumoraktiviteten |
| [18630468](https://pubmed.ncbi.nlm.nih.gov/18630468/) | 2008 | Case report | Anticancer Research | Komplet respons ved levermetastaser fra tyktarmskræft med S-1 og CPT-11 |
| [29394831](https://pubmed.ncbi.nlm.nih.gov/29394831/) | 2017 | Case report | Gan to Kagaku Ryoho | Todelt hepatektomi efter SOX + panitumumab som nedstadiering ved levermetastaser |
| [32936722](https://pubmed.ncbi.nlm.nih.gov/32936722/) | 2021 | Case report og review | J Oncol Pharm Pract | S-1-induceret hypertriglyceridæmi |
| [28414195](https://pubmed.ncbi.nlm.nih.gov/28414195/) | 2017 | Case report | Eur J Dermatol | TS-1-induceret erytrodermi med udbredt slimhindepåvirkning og hånd-fod-syndrom |
| [41253353](https://pubmed.ncbi.nlm.nih.gov/41253353/) | 2025 | Case report | Gan to Kagaku Ryoho | Urinretention ved oxaliplatin-induceret akut perifer neuropati efter behandling med tegafur/gimeracil/oteracil |
| [35444144](https://pubmed.ncbi.nlm.nih.gov/35444144/) | 2022 | Case report | Gan to Kagaku Ryoho | Peritoneale recidiver efter resektion af kolorektalkræft behandlet laparoskopisk |
| [30692384](https://pubmed.ncbi.nlm.nih.gov/30692384/) | 2018 | Case report | Gan to Kagaku Ryoho | Smertelindring med cøliakuspleksus-neurolyse efter recidiv af tyktarmskræft |
| [34650027](https://pubmed.ncbi.nlm.nih.gov/34650027/) | 2021 | Case report | Am J Case Rep | Resektion af pancreashalekræft med kolonperforation efter neoadjuverende kemoterapi |

Bemærk: Der er ingen randomiserede studier blandt de fundne publikationer, og størstedelen er case reports, der ikke dokumenterer effekt.

---

## Information om det danske marked

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104621809 | Teysuno (Nordic Group BV) | Kapsler, hårde | Indikationstekst ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Konventionel cytotoksisk (fluoropyrimidin-baseret kombination) |
| Risiko for myelosuppression | Moderat; i en retrospektiv undersøgelse med S-1 + irinotecan sås grad 3-4 hæmatologisk toksicitet hos 16,1 % |
| Emetogenicitet | Lav til moderat (generel klassifikation for orale fluoropyrimidiner) |
| Monitorering | Fuldt blodbillede med differentialtælling, lever- og nyrefunktion, elektrolytter |
| Håndteringsbeskyttelse | Skal følge gældende regler for håndtering af cytotoksiske lægemidler |

Se produktresuméet (SmPC) for yderligere advarsler og forsigtighedsregler.

---

## Sikkerhedsovervejelser

Der er ingen data om advarsler, kontraindikationer eller interaktioner i de data, der er indsamlet til denne rapport. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Fra de identificerede publikationer er der rapporteret bivirkninger ved S-1-regimer, bl.a. hånd-fod-syndrom, erytrodermi med slimhindepåvirkning, hypertriglyceridæmi og hæmatologisk toksicitet.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger)**

**Begrundelse:**
Der foreligger et afsluttet fase 3-forsøg (NCT00660894, n=1535) samt et yderligere fase 3-forsøg og flere fase 2-forsøg med S-1 ved tyktarmskræft, og mekanismen er biologisk plausibel. Evidensen gælder dog S-1 som kombination, ikke oteracil alene, og flere forsøg har ukendt status og ingen bekræftede resultater.

**For at komme videre kræves:**
- Gennemgang af resultater fra NCT00660894 og NCT03448549
- Indhentning og gennemgang af produktresuméet (SmPC) fra Lægemiddelstyrelsen med advarsler og kontraindikationer (manglende i de indsamlede data)
- Data om oteracils virkningsmekanisme (MOA), f.eks. fra DrugBank
- Afklaring af den godkendte indikation for Teysuno i Danmark samt vurdering af, om tyktarmskræft allerede er dækket
- Sikkerhedsovervågningsplan, herunder DPD-relaterede forhold og hæmatologisk monitorering
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

