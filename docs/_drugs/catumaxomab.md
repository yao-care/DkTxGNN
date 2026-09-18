---
layout: default
title: Catumaxomab
parent: Kun modelforudsigelse (L5)
nav_order: 97
evidence_level: L5
indication_count: 10
---

# Catumaxomab
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

# Catumaxomab: Fra ondartede ascites til alvorlig nonproliferativ diabetisk retinopati

## Opsamling i én sætning

Catumaxomab (Removab) er et trifunktionelt bispecifikt antistof, der oprindeligt var godkendt i EU til behandling af ondartede ascites hos patienter med EpCAM-positive karcinomer, selvom godkendelsen frivilligt blev tilbagekaldt i 2017 af kommercielle årsager uden forbindelse til sikkerhed eller effektivitet.
TxGNN-modellen forudsiger, at det kan være effektivt ved **alvorlig nonproliferativ diabetisk retinopati** (score: 99.64%), mens **0 kliniske forsøg** og **0 publikationer** i øjeblikket understøtter denne retning.
Alle forudsigelser i denne batch er klassificeret som **L5 evidensniveau**, hvilket betyder, at de udelukkende hviler på modelinferens uden understøttende humanstudiedata; den overordnede anbefaling er **Hold**.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Ondartede ascites hos patienter med EpCAM-positive karcinomer (EU/EMA-godkendt, 2009; tilbagekaldt 2017) |
| Forudsagt ny indikation | Alvorlig nonproliferativ diabetisk retinopati |
| TxGNN-forudsigelsesscore | 99.64% |
| Evidensniveau | L5 |
| Danmarks markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Catumaxomab er et trifunktionelt bispecifikt antistof (~150 kDa), designet til samtidig at engagere tre celletyper: det binder **EpCAM** (Epithelial Cell Adhesion Molecule) på tumorceller, **CD3ε** på T-lymfocytter og **Fcγ-receptorer I/IIa/III** på accessoriske immuneceller (makrofager, NK-celler, dendritter) via sin hybrid rat/mus IgG2a/IgG2b Fc-region. Denne trispecifikke engagement danner en immunologisk synapse, der omdirigerer cytotoksiske T-celler og accessoriske immuneceller til at dræbe EpCAM-eksprimerende tumorceller — en mekanisme, der er tæt bundet til EpCAM-positive epitheliale malignancier.

Alvorlig nonproliferativ diabetisk retinopati (alvorlig NPDR) er en mikrovaskulær komplikation af diabetes karakteriseret ved pericyt-tab, kapillær okklusion, VEGF-medieret vaskulær hyperpermeabilitet, akkumulering af avancerede glykationsprodukter (AGE) og oxidativ stress. Disse patologiske mekanismer er helt adskilte fra EpCAM/CD3-medieret immuncellerekruttering. Selvom EpCAM udtrykkes på sporesniveauer i retinale progenitorceller under embryogenese, udtrykkes det ikke meningsfuldt i den syge retinale mikrovaskulatur, og ingen terapeutisk hypotese forbinder T-cellebroering til NPDR-patologi. Desuden gør Catumaxomabs store molekylvægt blod-retina-barrierapenetrationen negligibel efter systemisk administration, hvilket gør farmakokinetisk leverance til målvævet ekstrem usandsynligt.

Den høje TxGNN-forudsigelsesscore for diabetesrelaterede retinopati-spektrumtilstande (rangering 1–6) afspejler mest sandsynligt indirekte forbindelse gennem delte **diabetesrelaterede noder** i den underliggende vidensgrafen snarere end direkte biologisk plausibilitet. Blandt alle unikke forudsigelser i denne batch repræsenterer **sarcomatoid transitionalcellekarcinomi i nyrernes bekken** (rangering 9–10, score 98.29%) den mest mekanistisk troværdig kandidat: urotheliale/transitionalcellekarcinomer er kendt for at udtrykke EpCAM i 40–70% af tilfældene, hvilket stemmer overens med Catumaxomabs oprindelige målprofil. Imidlertid involverer sarcomatoid differentiering almindeligvis epithelial-til-mesenchymal transition (EMT) med betydelig EpCAM-nedregulering, som ville begrænse forventet efficacy selv i denne mere plausible indikation.

---

## Bevis fra kliniske forsøg

I øjeblikket er der ingen relaterede kliniske forsøg registreret for Catumaxomab i nogen af de forudsagte indikationer. Søgninger i ClinicalTrials.gov og WHO ICTRP returnerede nul resultater for alle indikationspar, der blev forespurgt (pr. 2026-03-24).

---

## Litteraturbeviser

I øjeblikket ingen relateret litteratur tilgængelig. PubMed-søgninger kombineret med "Catumaxomab" med hver af de fem forudsagte indikationer (alvorlig NPDR, lægemiddelinduseret osteoporose, diabetisk retinopati, diabetisk katarakt, nyrernes bekken-sarcomatoid TCC) returnerede nul resultater.

---

## Markedsinformation for Danmark

Catumaxomab har **ingen markedsføringstilladelser** i Danmark. Som kontekst var lægemidlet tidligere centralt godkendt af EMA som **Removab** (EU/1/09/512/001–003) til intraperitoneal behandling af ondartede ascites hos patienter med EpCAM-positive karcinomer, som ikke har tilgængelig standardterapi eller for hvilke ingen yderligere standardterapi er mulig. Denne godkendelse blev tilbagekaldt af godkendelsesholderes indehaver (Neovii Biotech GmbH, tidligere Fresenius Biotech) i **juni 2017** af kommercielle årsager; EMA bekræftede, at tilbagekaldelsen ikke var relateret til sikkerhed- eller effektivitetsbetænkeligheder.

Ingen nationale godkendelser fra Lægemiddelstyrelsen blev identificeret.

---

## Cytotoxicitet

Catumaxomab klassificeres som et antineoplastisk lægemiddel (immunterapi rettet mod EpCAM-positive kræftceller), og dette afsnit finder anvendelse.

| Punkt | Indhold |
|-------|---------|
| Cytotoxicitetsklassificering | Målrettet immunterapi — Trifunktionelt bispecifikt antistof (ikke konventionel cytotoxisk) |
| Myelosuppression-risiko | Lav til moderat; immunmedieret cytopenier mulig via cytokinfrigivelse og accessorisk celleaktivering |
| Emetogenicitetsklassificering | Lav (IV/intraperitoneal biologisk middel; kvalme rapporteret primært som infusionsrelateret systemisk reaktion) |
| Overvågningspunkter | Fuldt blodproduktantal med differentialtal, leverfunktionsprøver (ALT, AST, bilirubin), nyrefunktion, serum-cytokiner/CRP (overvågning af cytokinfrigivelsessyndrom), legemstemperatur |
| Håndteringsbeskyttelse | Følg institutionelle håndbetjeningsretningslinjer for biologiske/immunologiske lægemidler; standardisepsissikkerhedsforanstaltninger finder anvendelse; ingen alkylerings-/DNA-skadebetinget risiko, men proteinbaserede biologiske farebeskyttelsesprotokol anbefales |

---

## Sikkerhedshensyn

Detaljerede SmPC-niveau advarsel- og kontraindikationsdata var ikke tilgængelige i dette bevisgodtgørelsessæt (klassificeret som et datakløft på analysetidspunktet). Baseret på kendt klinisk farmakologi fra den oprindelige EU-godkendelse, anerkendes følgende sikkerhedshensyn:

- **Cytokinfrigivelsessyndrom (CRS)**: Den klinisk mest signifikante toksicitet forbundet med Catumaxomab. Systemiske inflammatoriske reaktioner — herunder feber, kulderystelser, kvalme, opkastning og hypotension — blev hyppigt rapporteret i kliniske forsøg, især under og efter intraperitoneal infusion. Alvorlighetsgrad kan spænde fra grad 1–2 til potentielt livstruende.
- **Hepatotoxicitet**: Forbigående stigninger i leverenzymer (ALT, AST, bilirubin) blev observeret i en væsentlig andel af patienterne i pivotale forsøg; tæt hepatisk overvågning anbefales.
- **Infektioner**: Immunaktivering og kateterrelaterede procedurer øger infektionsrisikoen.
- **Lægemiddel–lægemiddel-interaktioner**: Ingen DDI-data identificeret i denne gennemgang (forespørgsel returnerede nul resultater). Forsigtighed anbefales ved samtidige immunsuppressiva, der kan dæmpe terapeutisk T-celleaktivering, eller med midler, der potentialiserer cytokinfrigivelse.

Se venligst det godkendte Produktresumé (SmPC) og den Europæiske offentlige evalueringsrapport (EPAR) for Removab for omfattende sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
Hver TxGNN-forudsigelse genereret for Catumaxomab i denne batch er klassificeret som **L5** (udelukkende computerisk modelforudsigelse), understøttet af hverken kliniske forsøg eller offentliggjort litteratur. De højest rangerede indikationer — der dækker det diabetiske retinopati-spektrum og lægemiddelinduseret osteoporose — er **mekanistisk implausible** givet Catumaxomabs EpCAM/CD3-immunbroerings-mekanisme, dens manglende evne til at penetrere blod-retina-barrieren og det fuldstændige fravær af enhver EpCAM-relateret patologi i disse tilstande. Avancering af nogen af disse indikationer uden præklinis mekanistisk validering ville ikke opfylde en minimumsvidenskabelig begrundelsestærskel.

**For at fortsætte, er det nødvendigt med følgende:**

- **Mekanistisk gennemførlighedsvurdering**: Formel vurdering af en klinisk farmakolog af, hvorvidt nogen forudsagt indikation involverer EpCAM-eksprimerende målvæv, der er tilgængeligt for en ~150 kDa biologisk middel
- **EpCAM-ekspressionsprofilering**: For den mest plausible kandidat (nyrernes bekken-sarcomatoid TCC) er vævsbiopsdata, der bekræfter EpCAM-udtrykkelse i sarcomatoid-differentieret urothelialcarcinom, en forudsætning før yderligere investering
- **Præklinis bevis**: Som minimum in vitro-cytotoxicitetsdata i den foreslåede nye indikations cellelinjer ved hjælp af Catumaxomab; in vivo xenograft-modeller, hvis in vitro-signal er positivt
- **Sikkerhedsprofil-afslutning**: Hentning og struktureret analyse af det fulde Removab SmPC og EPAR for at adressere det nuværende blokkeringsdatakløft (DG001)
- **MOA-dokumentation**: Struktureret ekstraktion af Catumaxomabs virkningsmekanisme fra DrugBank (DG002) for at muliggøre korrekt mekanistisk scoring
- **Reguleringsmæssig vejledningsvurdering**: Givet den tidligere EMA-tilbagekaldelse (kommerciel, ikke sikkerhedsdrevet), ville genkombination kræve en ny ansøgning om markedsføringstilladelse; tidlig videnskabelig vejledning fra EMA eller Lægemiddelstyrelsen anbefales før commitment af præklinis ressourcer
- **Vidensgrafrevisit**: Undersøg de indirekte grafstier, der driver høje TxGNN-scorer for diabetesindikationer, for at bestemme, om en strukturel bias i vidensgraf producerer systematisk oppustede scorer for diabetesadjacente noder

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

