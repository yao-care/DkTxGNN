---
layout: default
title: Mepivacaine
parent: Kun modelforudsigelse (L5)
nav_order: 529
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Mepivacaine: forudsagt ny indikation Gastroduodenitis (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (godkendelsesteksten er tom)"
monitor_inn: "mepivacaine"
predicted_indications: ["gastroduodenitis", "peptic ulcer disease"]
---

# Mepivacaine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Mepivacain: Fra lokalbedøvelse til gastroduodenitis
{: .text-alpha }

## Resumé

Mepivacain er et amid-type lokalanæstetikum, der markedsføres i Danmark som injektionsvæske. Der foreligger ingen godkendt indikationstekst i de data, der er indsamlet til denne rapport. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **gastroduodenitis** (score 99,5 %), men der er **0 kliniske forsøg** og **0 relevante publikationer**, der understøtter forudsigelsen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (godkendelsesteksten er tom) |
| Forudsagt ny indikation | Gastroduodenitis |
| TxGNN-forudsigelsesscore | 99,5 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 3 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede data om virkningsmekanismen i de indsamlede data. Mepivacain er generelt kendt som et amid-type lokalanæstetikum, der blokerer spændingsfølsomme natriumkanaler og dermed hæmmer overførsel af smertesignaler. Det er dog ikke bekræftet i de data, der ligger til grund for rapporten.

Det eneste, der kan foreslås som en mulig, men ubekræftet forklaring, er en lokal smertelindrende effekt på visceral smerte eller slimhindesmerter. Det er ikke det samme som en sygdomsmodificerende effekt ved betændelse i mavesæk og tolvfingertarm. Der er derfor ikke påvist nogen understøttet mekanistisk sammenhæng, og forudsigelsen hviler udelukkende på modellen.

Modellen forudsiger også **mavesår (peptic ulcer disease)** som den næstrangerede indikation (score 99,4 %). Heller her mangler der et underbygget mekanistisk link. En eventuel effekt på visceral smertesignalering er spekulativ og knyttet hverken til sårheling eller til sygdomsårsagerne (syresekretion, *H. pylori*, NSAID-skade).

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

For gastroduodenitis foreligger der på nuværende tidspunkt ingen relateret litteratur.

For mavesår blev der fundet én publikation, men den vurderes som irrelevant:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [6890367](https://pubmed.ncbi.nlm.nih.gov/6890367/) | 1982 | Dyreforsøg | Arzneimittel-Forschung | Sikkerhedsfarmakologi for et andet lægemiddel (lofexidin, en alfa-2-agonist). Omhandler hverken mepivacain eller behandling af mavesår. |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101001756 | Carbocain (Sandoz A/S) | Injektionsvæske, opløsning | Ikke angivet |
| 28101593094 | Scandonest-Adrenalin (Septodont) | Injektionsvæske, opløsning | Ikke angivet |
| 28101002156 | Carbocain-adrenalin (Sandoz A/S) | Injektionsvæske, opløsning | Ikke angivet |

Alle tre tilladelser er gyldige, og alle er nationale enkeltstofpræparater.

---

## Sikkerhedsovervejelser

**Sygdomme knyttet til lægemidlet i vidensgrafen (TxGNN/PrimeKG).** Disse stammer fra en vidensgraf og ikke fra produktresuméet, og de skal derfor fortolkes med forsigtighed:
- Nyresygdom
- Leversygdom
- Galdeblæresygdom
- Myasthenia gravis (herunder voksendebuterende form) og sygdomme i den neuromuskulære overgang
- Butyrylkolinesterase-mangel
- Hjerte-kar-sygdom og hjertesygdom
- Pyoureter

**Lægemiddelinteraktioner** (14 registrerede, alle fra DDInter):
- **Moderat**: liposomal morfin samt andre lokalanæstetika og overfladebedøvende midler, bl.a. lidocain (topisk og oftalmisk), benzocain (topisk), cocain (topisk og nasal), tetracain (oftalmisk og topisk), oxybuprocain (oftalmisk) og cinchocain (topisk).
- **Mindre**: hyaluronidase.

Der foreligger ikke oplysninger om advarsler og kontraindikationer fra produktresuméet i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (evidensniveau L5) uden kliniske forsøg og uden relevant litteratur. Der er ingen understøttet mekanistisk sammenhæng, og de data, der er indsamlet om lægemidlets oprindelige indikation og sikkerhed, er ufuldstændige.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméer fra Lægemiddelstyrelsen (godkendte indikationer, advarsler og kontraindikationer)
- Data om virkningsmekanisme fra DrugBank
- Systematisk litteratursøgning specifikt for mepivacain ved gastroduodenitis og mavesår
- Vurdering af administrationsvej: de nuværende præparater er injektionsvæsker, og det er uafklaret, om de er forenelige med en gastrointestinal indikation
- Prækliniske eller mekanistiske studier, der kan underbygge en eventuel effekt ud over symptomatisk smertelindring
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

