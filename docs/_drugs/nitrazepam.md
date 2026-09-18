---
layout: default
title: Nitrazepam
parent: Høj evidens (L1-L2)
nav_order: 310
evidence_level: L2
indication_count: 6
---

# Nitrazepam
{: .fs-9 }

Evidensniveau: **L2** | Forudsagte indikationer: **6** stk.
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

# Nitrazepam: Fra Uregistreret Oprindelig Indikation til Søvnforstyrrelser, Initiering og Opretholdelse af Søvn (Insomni)

## Sammenfatning i én sætning

Nitrazepams egen godkendt indikation er ikke registreret i denne evidenspakke (`original_indications` er et datahul), men det er et længe-markedsført benzodiazepin-hypnotikum (Mogadon). TxGNN-modellen forudsiger, at det er effektivt mod **søvnforstyrrelser, initiering og opretholdelse af søvn** (insomni) med en **99,89%** forudsigelsesscore, understøttet af **20 publikationer** (inklusive 1 RCT) og **ingen registrerede kliniske forsøg**. Note: denne forudsagte indikation overlapper med nitrazepams velkendt historisk brug, så resultatet bør læses som en bekræftelse af kendt farmakologi snarere end som et nyt repurposingssignal.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke registreret (datahul — ingen `original_indications` poster; lægemidlet er ikke aktuelt markedsført i Danmark) |
| Forudsagt ny indikation | Søvnforstyrrelser, initiering og opretholdelse af søvn (Insomni) |
| TxGNN forudsigelsesscore | 99,89% |
| Evidensniveau | L2 |
| Danmarks markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Forløb med forholdsregler |

---

## Hvorfor er denne forudsigelse rimelig?

Feltet `original_moa` er et datahul, men modellens egen repurposing-argumentation leverer mekanismen: nitrazepam er et klassisk benzodiazepin, der binder sig til benzodiazepin-stedet på GABA-A-receptorens α-underenhed, positivt modulerer GABA-styret chloridtilstrømning og forbedrer central hæmmende neurotransmission. Dette producerer sedativ, hypnotisk, anxiolytisk, antikonvulsiv og muskelrelakserende effekter.

Vigtigt er det, at den "forudsagte nye indikation" her — insomni ved søvnstart og søvnopretholdelses — slet ikke er en virkelig ny terapeutisk hypotese. Nitrazepam har været markedsført i årtier under varemærket Mogadon specifikt som et hypnotikum mod insomni. Litteraturovidensen nedenfor (farmakokinetik-reviews, et head-to-head RCT mod triazolam, sikkerhedsreviews) afspejler denne etablerede brug snarere end en uprøvet ekstrapolation. Det tilsyneladende "forudsigte" resultat opstår, fordi feltet `original_indications` i denne evidenspakke er tomt (datahul), så model-/rapportpipelineen ikke kan genkende, at dette allerede er lægemidlets kerneindikation.

Mekanistisk er forbindelsen derfor direkte og velestableret, ikke sluttet: GABA-A-receptorpotentiering reducerer søvnlatens og øger total søvntid, i overensstemmelse med nitrazepams kendt klinisk farmakologi.

---

## Evidens fra kliniske forsøg

Aktuelt ingen relaterede kliniske forsøg registreret

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtige resultater |
|------|-----|------|------|---------|
| [6135296](https://pubmed.ncbi.nlm.nih.gov/6135296/) | 1983 | RCT | Acta Psychiatrica Scandinavica | Dobbelt-blind krydsover i 26 geriatriske indlagte: nitrazepam 5 mg vs triazolam 0,25 mg — sammenlignelig søvnmængde/kvalitet og psykomotorisk ydeevne |
| [7037262](https://pubmed.ncbi.nlm.nih.gov/7037262/) | 1981 | Review | Clinical Pharmacokinetics | Oversigt over nitrazepams kliniske farmakokinetik |
| [4892037](https://pubmed.ncbi.nlm.nih.gov/4892037/) | 1969 | Review | British Medical Journal | 27 patienter med akut nitrazepam-overdosis (op til 80 tabletter) viste kun søvnighed; dobbelblind forsøg fandt nitrazepam lige så effektivt som butobarbiton som hypnotikum |
| [1125532](https://pubmed.ncbi.nlm.nih.gov/1125532/) | 1975 | Case Report | British Journal of Psychiatry | Caseberetning om nitrazepam (Mogadon) afhængighed |
| [4712500](https://pubmed.ncbi.nlm.nih.gov/4712500/) | 1973 | Case Report | British Medical Journal | Caseberetning om nitrazepams effekter på drømme/ubevidst indhold |
| [238826](https://pubmed.ncbi.nlm.nih.gov/238826/) | 1975 | Review | Drugs | Oversigt over søvnfysiologi og bedømmelse af hypnotisk lægemiddeleffektivitet |
| [19450355](https://pubmed.ncbi.nlm.nih.gov/19450355/) | 2007 | Review | BMJ Clinical Evidence | Op til 40% af voksne har insomni; prævalensen stiger med alderen; risikofaktorer inkluderer psykologisk stress og hyperarousal |
| [7725291](https://pubmed.ncbi.nlm.nih.gov/7725291/) | 1995 | Review | Tidsskrift for den Norske Laegeforening | Oversigt over insomni-klassificering, diagnose og behandlingsudviklinger |
| [15089115](https://pubmed.ncbi.nlm.nih.gov/15089115/) | 2004 | Review | CNS Drugs | Oversigt over restsymptomer ("hangover") af hypnotika (dagsøvnighed, psykomotorisk/kognitiv svækkelse) og ulykkesrisiko |
| [39231170](https://pubmed.ncbi.nlm.nih.gov/39231170/) | 2024 | — | PLoS ONE | Undersøgelse af ukorrekt benzodiazepinforskrivning i primær sundhedspleje, inklusive afhængighed og risiko for kognitivt fald hos ældre voksne |

---

## Markedsinformation for Danmark

Nitrazepam har **0 markedsføringstilladelser** i arkivet og er aktuelt **ikke markedsført** i Danmark. Ingen Lægemiddelstyrelsen- eller EMA-centraliserede autoriseringsregistreringer er tilgængelige i denne evidenspakke.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresuméet (SmPC) for sikkerhedsinformation. Ingen vigtige advarsler, kontraindikationer eller lægemiddel-lægemiddel-interaktionsdata er aktuelt i arkivet (DDI-forespørgselsstatus: ikke fundet).

---

## Konklusion og næste trin

**Beslutning: Forløb med forholdsregler**

**Argumentation:**
Litteraturbevis (inklusive et direkte RCT af nitrazepam som hypnotikum) understøtter plausibilitet for insomni, men dette bekræfter i høj grad nitrazepams kendt, årtier gammel klinisk brug snarere end at etablere en virkelig ny indikation. Kritiske datahul — ingen dansk/EU SmPC-advarsler/kontraindikationer (Blocking, DG001), ingen formel MOA-dokumentation (High, DG002), og ingen bekræftet oprindelig indikation — blokerer enhver registreringsniveaubeslutning, og lægemidlet er aktuelt ikke markedsført i Danmark.

**For at fortsætte er følgende nødvendigt:**
- Dansk/EU SmPC-advarsler, kontraindikationer og DDI-data (løs DG001, blocking)
- Formel MOA-dokumentation via DrugBank (løs DG002)
- Bekræftelse af nitrazepams faktiske godkendt indikation(er) på kildemarkeder, for at præcisere, om dette er et ægte signal for ny brug eller et data-registreringshul
- Vurdering af markedsføringstilladelsessti givet aktuelt "Ikke markedsført" status i Danmark

*Note: Modellen flaggede også to lavere-konfidenskandidater — akut encephalopati med bifasisk anfald og sen reduceret diffusion (AESD) og Wernicke-Korsakoff syndrom — begge på evidensniveau L5 uden understøttende litteratur eller forsøg; begge anbefales **Hold**.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

