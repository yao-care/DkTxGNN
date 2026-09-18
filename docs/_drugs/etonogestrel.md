---
layout: default
title: Etonogestrel
parent: Kun modelforudsigelse (L5)
nav_order: 180
evidence_level: L5
indication_count: 10
---

# Etonogestrel
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

# Etonogestrel: Fra Prævention til Amenoré

## Opsummering i én sætning

Etonogestrel er et tredje-generations-gestagen, der primært bruges til langtidsvirkende reversibel prævention (f.eks. subdermal implantat markedsført som Nexplanon/Implanon).
TxGNN-modellen forudsiger, at det kan være effektivt mod **Amenoré**, med en forudsigelsesscore på 99,84%; dette er dog næsten helt sikkert en **omvendt associationsartefakt** — etonogestrel vides at *forårsage* amenoré som en bivirkning hos 20–30% af implantbrugere, ikke at behandle det.
Understøttende bevis er begrænset til **1 klinisk forsøg** (fokuseret på prævention, ikke amenoré-behandling) og **1 relevant publikation**.

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Prævention (langtidsvirkende reversibel) |
| Forudsagt ny indikation | Amenoré (sygdom) |
| TxGNN forudsigelsesscore | 99,84% |
| Bevisniveau | L4 — Intet direkte terapeutisk bevis; kun mekanistiske studier |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Afvent** |

## Hvorfor er denne forudsigelse rimelig?

> I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i evidenspakken. Baseret på kendt farmakologi er etonogestrel et syntetisk gestagen (det aktive metabolit af desogestrel), der fungerer som en potent agonist ved progesteronreceptoren. Det opnår prævention primært ved at undertrykke ovulation via hæmning af LH-toppen, fortykking af cervixslim og induktion af endometrial atrofi.

**⚠️ Kritisk forbehold — Omvendt association:** TxGNN-modellen har meget sandsynligt fejltolket en veldokumenteret *bivirkningsrelation* som en *terapeutisk relation*. Etonogestrel-frigivende implantater forårsager amenoré hos cirka 20–30% af brugere på grund af dyb undertrykkelse af hypotalamisk-hypofysær-ovarial-aksen og endometrial atrofi. Med andre ord **fremkalder** etonogestrel amenoré snarere end at behandle det. Videngrafen indeholder sandsynligvis talrige co-occurrence-links mellem etonogestrel og amenoré i bivirkningsmeldinger og kliniske forsøgsdata, hvilket øger forudsigelsesscore'n.

Fra et klinisk synspunkt har amenoré diverse ætiologier (hypotalamisk, hypofysær, ovarial, uterinsk), og tilføjelse af et gestagen, der yderligere undertrykker HPO-aksen, ville være kontraproduktivt i de fleste former for patologisk amenoré. Denne forudsigelse har ingen terapeutisk betydning og bør ikke forfølges som en kandidat til genudnyttelse.

## Klinisk forsøgsbeviser

| Forsøgsnummer | Fase | Status | Antal deltakere | Vigtige fund |
|---------|------|------|------|---------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Fase 3 | Afsluttet | 498 | Vurderede præventiv virkning og sikkerhed ved etonogestrel-implantatet under forlænget brug (år 4–5). **Ikke et behandlingsforsøg for amenoré** — amenoré blev registreret kun som en blødningsmønster-bivirkning. Relevans for amenoré-behandling: **Lav (Grad C).** |

> **Bemærk:** Ingen kliniske forsøg, der undersøgte etonogestrel som *behandling* for amenoré, blev identificeret.

## Litteraturbevis

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|------|---------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | RCT | Contraception | Sammenlignede Implanon (enkelt-rod etonogestrel) mod Norplant (seks-kapsel levonorgestrel) for præventiv virkning og blødningsmønstre hos 200 kvinder over 2–4 år. Ingen graviditeter forekom. **Amenoré blev rapporteret som en bivirkning**, ikke undersøgt som et behandlingsendepunkt. |

> **Bemærk:** Et second litteraturresultat (PMID 33430924) blev returneret ved søgningen, men angår et COVID-19-pneumoni-forsøg (BIO101/COVA-studie) uden relevans for etonogestrel eller amenoré og er blevet udelukket.

## Markedsinformation for Danmark

Etonogestrel har i øjeblikket ingen markedsføringstilladelser i det gennemgåede datasæt.

> **Bemærk:** Produkter indeholdende etonogestrel (f.eks. Nexplanon) kan have centraliserede EMA-tilladelser, der gælder i Danmark. Klinikere bør konsultere Lægemiddelstyrelsen eller EMA-unionsregisteret for aktuel tilladelsestatus.

## Yderligere forudsagte indikationer (lavere rangerede)

TxGNN-modellen forudsagde også flere godartede brysttilstande. Disse er opsummeret herunder for fuldstændighed:

| Rangering | Sygdom | TxGNN-score | Bevisniveau | Anbefaling | Kommentar |
|------|---------|-------------|----------------|----------------|---------|
| 3 | Godartad fibrocystisk brystsygdom | 99,61% | L5 | Forskningsspørgsmål | Hormonel følsomhed giver teoretisk begrundelse, men klinisk bevis er modstridende. Ingen forsøg eller publikationer fundet. |
| 5 | Stump ductus-adenose i brystet | 99,29% | L5 | Afvent | Sjælden histopatologisk undertype; typisk styret af billeddiagnostik-overvågning, ikke farmakoterapia. Høj score er sandsynligvis refleksion af grafnærhed til andre brystsygdomme. |
| 6 | Apokrin adenose i brystet | 99,29% | L5 | Afvent | Identisk score til stump ductus-adenose, hvilket tyder på, at modellen grupperer disse via sygdomsklynge-nærhed snarere end uafhængige lægemiddel-sygdoms-bevis. Ikke behandlet farmakologisk. |
| 9 | Godartad mamma-dyspladasi | 99,21% | L5 | Forskningsspørgsmål | Meget overlappende diagnostisk koncept med fibrocystisk sygdom. Gestagen-anti-østrogen-effekter er teoretisk plausible, men klinisk ubevist. |

> **Mønsterobservation:** Klyngen af godartede brysttilstande med næsten identiske TxGNN-score (99,2–99,6%) tyder stærkt på, at modellen propagerer forudsigelser gennem sygdomsgrafnærhed snarere end at identificere uafhængige terapeutiske signaler.

## Sikkerhedshensyn

> Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation. Vigtige sikkerhedsdata (advarsler, kontraindikationer og lægemiddel-lægemiddel-interaktioner) var ikke tilgængelige i denne evidenspakke.

> For produkter godkendt i EU (f.eks. Nexplanon) er SmPC tilgængeligt via EMA-websitet. Kendte klassebrede bekymringer for gestagener omfatter tromboemboliske hændelser, effekter på lipidstofskiftet, humørændringer og interaktioner med CYP3A4-induktorer (f.eks. rifampicin, carbamazepin, phenytoin).

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Den toprangerede TxGNN-forudsigelse (amenoré) repræsenterer en klassisk **omvendt associationsartefakt** — etonogestrel forårsager amenoré som en kendt farmakologisk bivirkning og behandler det ikke. De resterende forudsigelser (godartede brysttilstande) befinder sig alle på bevisniveau L5 (kun modelforudsigelse) uden kliniske forsøg og uden publikationer, og de identiske score på tværs af relaterede brysttilstande indikerer grafnærhed-drevne forudsigelser snarere end genuine terapeutiske signaler. Denne kandidat bør ikke gå videre til yderligere evaluering.

**Hvis fremtidig re-evaluering overvejes, ville følgende være nødvendigt:**
- Detaljerede virkningsmekanisme-data (MOA) fra DrugBank
- Sikkerhedsdata fra det godkendte produktresumé (advarsler, kontraindikationer, lægemiddel-lægemiddel-interaktioner)
- Afklaring af markedsstatus i Danmark via Lægemiddelstyrelsen / EMA-registre
- For fibrocystisk brystsygdom specifikt: en målrettet litteratursøgning for gestagen-effekter på fibrocystiske brystændringer (bredere end blot etonogestrel)
- Ekspertlig klinisk gennemgang for at skelne genuine terapeutiske signaler fra bivirkning- eller grafnærhed-artefakter i TxGNN-resultater

---

*Denne rapport er til forskningsformål og udgør ikke medicinsk rådgivning. Alle kandidater til genudnyttelse af lægemidler kræver klinisk validering før eventuel terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

