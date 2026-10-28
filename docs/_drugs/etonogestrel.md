---
layout: default
title: Etonogestrel
parent: Kun modelforudsigelse (L5)
nav_order: 336
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Etonogestrel: forudsagt ny indikation Amenoré (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (implantatet er et hormonelt præv…"
monitor_inn: "ETONOGESTREL"
predicted_indications: ["amenorrhea (disease)", "breast fibrocystic disease", "blunt duct adenosis of breast", "apocrine adenosis of breast", "benign mammary dysplasia"]
---

# Etonogestrel
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **5** stk.
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

## Etonogestrel: Fra prævention til amenoré
{: .text-alpha }

## Resumé i én sætning

Etonogestrel er et progestin, der anvendes i det subkutane implantat Nexplanon, og som i Danmark er markedsført som hormonel prævention (indikationsteksten er ikke tilgængelig i de data, der er indsamlet til denne rapport).
TxGNN-modellen forudsiger, at stoffet kan være effektivt ved **amenoré** (samt godartede brystlidelser), men der er **0 kliniske forsøg** og **ingen relevant litteratur** bag forudsigelsen.
Amenoré er en kendt bivirkning af implantatet, så scoren stammer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, som modellen har lært mellem beslægtede sygdomme, og ikke en terapeutisk gevinst eller biologisk evidens.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (implantatet er et hormonelt præventionsmiddel) |
| Forudsagt ny indikation | Amenoré |
| TxGNN-forudsigelsesscore | 0,9984 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig – eller ikke?

Der foreligger ikke detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Etonogestrel er et potent progestin, som kendes for at hæmme ovulation og fremkalde endometrieatrofi.

Netop denne virkning gør, at amenoré er en velkendt effekt af implantatet hos en betydelig andel af brugerne. Amenoré er altså en bivirkning eller sekundær effekt af den eksisterende præventionsindikation og ikke et egentligt mål for drug repurposing. At behandle amenoré med et progestin vil desuden være farmakologisk kontraintuitivt. Den høje score (0,9984) kommer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens eller en behandlingsmæssig fordel.

Modellen forudsiger også flere godartede brystlidelser (fibrocystisk brystsygdom, 0,9961; blunt duct adenosis og apokrin adenosis, 0,9929; benign mammær dysplasi, 0,9921). Progestiner har historisk været brugt ved godartede brystlidelser og mastalgi via modvirkning af østrogendrevet proliferation, hvilket giver en plausibel men indirekte begrundelse. Brystspænding er imidlertid en hyppig bivirkning ved implantatet, hvilket taler imod nytte. Forudsigelserne for disse lidelser er sandsynligvis indbyrdes korrelerede, fordi TxGNN-modellen (deep learning) har lært ligheder mellem beslægtede sygdomme.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | RCT-protokol | Trials | Omhandler BIO101 til forebyggelse af respiratorisk forværring ved COVID-19-lungebetændelse. Ikke relateret til etonogestrel eller amenoré. |

Der er ingen kliniske forsøg registreret for den forudsagte indikation.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103037998 | Nexplanon (N.V. Organon) | Implantat | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

- **Mulige kontraindikationer fra vidensgrafen** (baseret på lægemiddel-sygdom-relationer i PrimeKG, ikke på produktresuméets tekst): hypertension, epilepsi, angst- og neurotiske lidelser, dysthymi, porfyri, nyresygdom, leversygdom, galdeblæresygdom, systemisk lupus erythematosus, astma, diabetes mellitus og diabetisk ketoacidose, hypertriglyceridæmi, hyperlipidæmi, kvindelig brystkræft, tromboflebitis, migræne, koronararteriesygdom og fedme.
- **Lægemiddelinteraktioner** (100 registrerede; alle viste eksempler er af moderat grad): antidiabetika (acarbose, metformin, glimepiride, chlorpropamide, SGLT2-hæmmere som canagliflozin, dapagliflozin og empagliflozin, DPP-4-hæmmere som alogliptin og saxagliptin, GLP-1-agonister som semaglutid, dulaglutid og albiglutid, samt insuliner), desuden aprepitant, clarithromycin og linaclotid.

Konsulter det godkendte produktresumé (SmPC) for de officielle advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på modellen (L5). Der er ingen relevante kliniske forsøg eller litteratur, og amenoré er en kendt bivirkning af stoffet snarere end et behandlingsmål. Den eneste tilknyttede publikation er uden relation til etonogestrel.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikation mangler)
- Data om virkningsmekanismen (fx fra DrugBank)
- Målrettet litteratursøgning efter etonogestrel/progestiner ved godartede brystlidelser, hvis denne retning skal forfølges
- Vurdering af, om TxGNN-modellens (deep learning) forudsigelse blot afspejler en bivirkningsassociation og ligheder, som modellen har lært mellem beslægtede sygdomme
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

