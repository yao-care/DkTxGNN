---
layout: default
title: Ipratropium
parent: Høj evidens (L1-L2)
nav_order: 452
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Ipratropium: forudsagt ny indikation Obstruktiv lungesygdom (evidensniveau L1). Oprindelig indikation: Kronisk obstruktiv lungesygdom (KOL), allergisk rhinitis…"
monitor_inn: "ipratropium"
predicted_indications: ["nasal cavity disease", "pharyngitis", "acute laryngopharyngitis", "respiratory malformation", "papillary conjunctivitis", "Rienhoff syndrome", "anaphylaxis", "food-dependent exercise-induced anaphylaxis"]
---

# Ipratropium
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
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

# Ipratropium: Fra kronisk obstruktiv lungesygdom (KOL) til obstruktiv lungesygdom

## Resumé i én sætning

Ipratropium er et antikolinergt lægemiddel, der oprindeligt anvendes til behandling af kronisk obstruktiv lungesygdom (KOL), allergisk og vasomotorisk rhinitis, bronkitis og andre luftvejslidelser.
TxGNN-modellen forudsiger, at det kan have effekt på **obstruktiv lungesygdom**, men denne forudsigelse ligger tæt op ad den eksisterende KOL-indikation og er derfor reelt dokumentation for den nuværende anvendelse snarere end ægte repurposing.
Forudsigelsen understøttes af **25 registrerede kliniske forsøg** og **20 publikationer** i de data, der er indsamlet til denne rapport.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Kronisk obstruktiv lungesygdom (KOL), allergisk rhinitis, vasomotorisk rhinitis, bronkitis, forkølelse, lungeemfysem (fra TxGNN-vidensgrafen; godkendt indikationstekst er ikke tilgængelig i de danske tilladelser) |
| Forudsagt ny indikation | Obstruktiv lungesygdom |
| TxGNN-forudsigelsesscore | 99,97 % |
| Evidensniveau | L1 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 4 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Ipratropium er en ikke-selektiv muskarin antagonist. Det blokerer især M3-receptor-medieret bronkokonstriktion i luftvejenes glatte muskulatur og dæmper dermed den kolinerge tonus, som spiller en central rolle ved obstruktive lungesygdomme. Mekanismen er beskrevet i den tilgængelige litteratur; detaljerede mekanismedata fra DrugBank var ikke tilgængelige i de data, der er indsamlet til denne rapport.

Forudsagt indikation (obstruktiv lungesygdom) overlapper i høj grad med den allerede kendte KOL-indikation. Der er derfor tale om dokumentation for eksisterende brug snarere end en reel ny anvendelse. Litteraturen om antikolinerge bronkodilatatorer og flere fase 3-forsøg understøtter den kliniske effekt.

Ud over obstruktiv lungesygdom rangerede modellen bl.a. sygdom i næsehulen, faryngitis og trakeal sygdom. For disse er evidensen enten indirekte eller prækliniske (L4), og de er klassificeret som forskningsspørgsmål. For flere andre forudsigelser (akut laryngopharyngitis, papillær konjunktivitis, Rienhoffs syndrom, fødevareafhængig anstrengelsesudløst anafylaksi) foreligger der kun modelforudsigelse (L5), og de bør afventes. Der er desuden en case-rapport om svær anafylaksi udløst af inhaleret ipratropium, hvilket er et sikkerhedssignal mod anafylaksi som indikation.

---

## Evidens fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT02177253](https://clinicaltrials.gov/study/NCT02177253) | Fase 3 | Afsluttet | 1118 | 12-ugers sammenligning af ipratropium/salbutamol (Respimat) med Combivent og ipratropium alene samt placebo ved KOL; bronkodilatorisk effekt og sikkerhed |
| [NCT01136421](https://clinicaltrials.gov/study/NCT01136421) | Fase 3 | Afsluttet | 124 | Magnesiumsulfat versus ipratropium som tillæg til SABA ved akut KOL-exacerbation |
| [NCT02172469](https://clinicaltrials.gov/study/NCT02172469) | Fase 3 | Afsluttet | 215 | Tiotropium versus Atrovent (ipratropium) MDI ved KOL; effekt og sikkerhed |
| [NCT00239434](https://clinicaltrials.gov/study/NCT00239434) | Fase 3 | Afsluttet | 200 | Tiotropium én gang dagligt versus Atrovent MDI fire gange dagligt ved KOL |
| [NCT02172404](https://clinicaltrials.gov/study/NCT02172404) | Fase 3 | Afsluttet | 160 | HandiHaler versus MDI: inhalationsteknik og brugervenlighed ved KOL (indirekte) |
| [NCT00371527](https://clinicaltrials.gov/study/NCT00371527) | Ikke angivet | Afsluttet | 200 | Randomiseret, dobbeltblindet, placebokontrolleret forsøg med ipratropium ved akut bronkitis uden underliggende lungesygdom |
| [NCT01415518](https://clinicaltrials.gov/study/NCT01415518) | Fase 4 | Afsluttet | 581 | Symbicort som tillæg til Atrovent + theophyllin ved svær KOL |
| [NCT01691482](https://clinicaltrials.gov/study/NCT01691482) | Fase 4 | Afsluttet | 56 | 4-ugers crossover: daglig lungefunktion efter albuterol og ipratropium, alene og i kombination, ved KOL |
| [NCT04446637](https://clinicaltrials.gov/study/NCT04446637) | Fase 3 | Trukket tilbage | 0 | Ipratropium/levosalbutamol fastdosiskombination ved KOL; ingen deltagere inkluderet, ingen data |
| [NCT02235428](https://clinicaltrials.gov/study/NCT02235428) | Fase 4 | Afsluttet før tid | 3 | Ipratropium som tillæg til højdosis salbutamol ved akut astma hos børn; for få deltagere til konklusion |

Listen viser et udvalg af de mest relevante forsøg. Flere af forsøgene er ældre, og mange har ipratropium som aktiv komparator frem for som primært undersøgt middel.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [26391969](https://pubmed.ncbi.nlm.nih.gov/26391969/) | 2015 | Cochrane-review | Cochrane Database Syst Rev | Tiotropium versus ipratropiumbromid ved stabil KOL |
| [24043433](https://pubmed.ncbi.nlm.nih.gov/24043433/) | 2013 | Cochrane-review | Cochrane Database Syst Rev | Tidligere version af sammenligningen af tiotropium og ipratropium ved KOL |
| [35616126](https://pubmed.ncbi.nlm.nih.gov/35616126/) | 2022 | Cochrane-review | Cochrane Database Syst Rev | Magnesiumsulfat ved akutte KOL-exacerbationer (relateret behandling) |
| [23170031](https://pubmed.ncbi.nlm.nih.gov/23170031/) | 2012 | Review | Ann Pharmacother | Samtidig brug af ipratropium og tiotropium ved KOL: effekt og sikkerhed |
| [20163324](https://pubmed.ncbi.nlm.nih.gov/20163324/) | 2010 | Review | Expert Opin Drug Metab Toxicol | Inhaleret albuterol, ipratropium og kombinationen ved KOL |
| [10565879](https://pubmed.ncbi.nlm.nih.gov/10565879/) | 1999 | Review | Respir Care Clin N Am | Antikolinerge bronkodilatatorer; veldokumenteret spirometrisk bronkodilatation, også i kombination med albuterol |
| [2977109](https://pubmed.ncbi.nlm.nih.gov/2977109/) | 1988 | Review | Clin Pharm | Farmakologi, effekt, bivirkninger og dosering af ipratropium ved obstruktiv lungesygdom |
| [15987237](https://pubmed.ncbi.nlm.nih.gov/15987237/) | 2005 | Review | Treat Respir Med | Ipratropium HFA-formulering til vedligeholdelsesbehandling af bronkospasme |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Retningslinje | Basic Clin Pharmacol Toxicol | Finske retningslinjer for diagnostik og farmakoterapi ved stabil KOL |
| [38457591](https://pubmed.ncbi.nlm.nih.gov/38457591/) | 2024 | Retrospektiv analyse | Medicine | Probiotika sammen med budesonid og ipratropium ved KOL: effekt på lungefunktion og tarmflora |

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106743822 | Iprazap | Næsespray, opløsning | Ikke angivet i de tilgængelige data |
| 28104130807 | Ipramol Steri-Neb | Inhalationsvæske til nebulisator, opløsning, enkeltdosisbeholder | Ikke angivet i de tilgængelige data |
| 28104314008 | Otrivin Comp | Næsespray, opløsning | Ikke angivet i de tilgængelige data |
| 28103223300 | Berodual | Inhalationsspray, opløsning | Ikke angivet i de tilgængelige data |

Alle fire tilladelser er gyldige enkeltstofpræparater (ingen annullerede).

---

## Sikkerhedsovervejelser

**Sygdomme, hvor lægemidlet er markeret som kontraindiceret eller bør bruges med forsigtighed (fra TxGNN-vidensgrafen, ikke fra produktresuméets tekst):**
- Hjerte-kar: hypertension, langt QT-syndrom (herunder familiært), pludseligt hjertestop, hjerteledningssygdom, myokardieiskæmi, koronarsygdom
- Øjne: snævervinklet glaukom, okulær hypertension
- Urinveje/prostata: benign prostatahyperplasi, blærehalsobstruktion
- Stofskifte og endokrinologi: diabetes mellitus, diabetisk ketoacidose, metabolisk acidose/acidose, kaliummangel, hyperthyroidisme (Graves' sygdom, thyrotoksikose)
- Neurologi: epilepsi

**Lægemiddelinteraktioner:** 126 interaktioner er registreret. De viste er alle af moderat grad og omfatter primært andre antikolinerge stoffer (fx atropin, hyoscyamin, glycopyrronium, scopolamin, trospium, aclidinium), desuden bl.a. promethazin, chlorphenamin, prucalopride, eluxadolin og inhaleret insulin. Additive antikolinerge bivirkninger er den væsentligste bekymring.

**Øvrige signaler fra litteraturen:** Der er beskrevet en case-rapport om svær anafylaksi efter inhaleret ipratropium samt en case-rapport om ensidig pupiludvidelse (mydriasis) efter inhalation hos et spædbarn.

Oplysninger om advarsler og kontraindikationer fra produktresuméerne var ikke tilgængelige i de data, der er indsamlet til denne rapport. Se det godkendte produktresumé (SPC) for fuldstændig sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger)**

**Begrundelse:**
Den forudsagte indikation (obstruktiv lungesygdom) falder sammen med ipratropiums etablerede KOL-anvendelse og understøttes af flere afsluttede fase 3-forsøg og en bred litteratur om antikolinerge bronkodilatatorer. Der er dog ikke tale om ægte repurposing, og de øvrige forudsagte indikationer (næsehule, svælg, luftrør) har kun indirekte eller prækliniske data.

**For at komme videre kræves følgende:**
- Gennemgang af de danske produktresuméer (godkendte indikationer, advarsler og kontraindikationer), da disse data mangler
- Detaljerede data om virkningsmekanisme fra DrugBank
- Klarlæggelse af, om der ønskes en reel ny indikation ud over den eksisterende KOL-indikation. I så fald bør de forsøg, hvor ipratropium kun er komparator, vurderes kritisk
- Sikkerhedsovervågning af patienter med de ovenfor nævnte risikotilstande (især glaukom, prostatahyperplasi og hjerterytmeforstyrrelser) samt opmærksomhed på overfølsomhedsreaktioner
- For indikationer med kun L4/L5-evidens (fx faryngitis, trakeal sygdom): kontrollerede kliniske studier, før der kan tages stilling
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

