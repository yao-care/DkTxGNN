---
layout: default
title: Mirabegron
parent: Kun modelforudsigelse (L5)
nav_order: 295
evidence_level: L5
indication_count: 10
---

# Mirabegron
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

# Mirabegron: Fra overaktiv blære til thorakale misdannelser

## Resumé på en sætning

Mirabegron er en selektiv β3-adrenerg receptoragonist, som er godkendt internationalt til behandling af overaktiv blære (OAB), selvom der ikke blev identificeret danske nationale markedsføringsgodkendelser i dette datasæt.
TxGNN-modellen forudsiger, at dens højest-rangerede nye potentielle indikation er **Thorakale misdannelser** (score: 83,06%), understøttet af **0 kliniske forsøg** og **0 publikationer**.
På tværs af alle fem forudsagte indikationer i denne rapport med flere kandidater er den mekanistiske begrundelse svag, og beviserne overstiger ikke L4 (kun litteratur om sygdomsbaggrund); alle har en **Afvent**-anbefaling.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Overaktiv blære (OAB) — baseret på kendt farmakologi; ikke tilgængelig i dansk regulatorisk datasæt |
| Forudsagt ny indikation | Thorakale misdannelser |
| TxGNN forudsigelsesscore | 83,06% |
| Bevisniveau | L5 |
| Danmark markedsstatus | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 (national); se note om EMA centraliseret godkendelse nedenfor |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Der var ikke tilgængelige detaljerede mekanisme-for-handling-data i dette datasæt. Baseret på kendt farmakologi er mirabegron en selektiv β3-adrenerg receptor (β3-AR) agonist. β3-AR (ADRB3) udtrykkes primært i blærens detrusor-muskulatur, fedtvæv og nyretubuli. Dens aktivering stimulerer Gsα → adenylylcyklase → intracellulær cAMP-vej, hvilket forårsager afslapning af detrusor-musklen og øget blærekapacitet — den farmakologiske basis for dens godkendte OAB-indikation.

Thorakale misdannelser er en strukturel medfødt defekt. Dens patogenese involverer embryonisk skelet- og blødt væv udvikling, reguleret af HOX-gennetværk, FGF-signalering og relaterede udviklingsveie. Der er ingen etableret direkte mekanistisk forbindelse mellem β3-AR/cAMP-signaleringsaksen og de embryoniske processer, der ligger til grund for thorakal skeletudvikling.

Den høje TxGNN-forudsigelsesscore (0,83) for denne indikation er derfor sandsynligvis et kunstefakt, der stammer fra indirekte vidensgrafosforbindelser via nyre- eller mesenkymaletknuder snarere end en biologisk grundfestet forudsigelse. Dette er eksplicit markeret i den mekanistiske begrundelse som sandsynlig modelstøj snarere end et reelt lægemidd-sygdom-forhold.

---

## Klinisk forsøgsbeviser

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbeviser

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Danmark markedsinformation

Der blev ikke identificeret markedsføringsgodkendelser for mirabegron i den danske nationale regulatoriske database (0 licenser, ikke markedsført).

> **Bemærk:** Mirabegron (varemærke Betmiga) har en centraliseret EMA-markedsføringsgodkendelse (EU/1/12/809) til overaktiv blære hos voksne. Tilgængelighed i Danmark via EMA centraliserede procedure bør bekræftes direkte med Lægemiddelstyrelsen, da centraliserede EMA-godkendelser muligvis ikke afspejles i det nationale datasæt, der bruges her.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Yderligere forudsagte indikationer

Dette er en rapport med flere kandidater (TW-DB08893-multi). TxGNN-modellen identificerede fem unikke sygdomme på tværs af de 10 øverste forudsigelser. Alle har en **Afvent**-anbefaling. Tabellen nedenfor opsummerer vigtige forskelle i bevisniveau og mekanistiske bekymringer.

| Rang | Sygdom | TxGNN score | Bevisniveau | Vigtig mekanistisk bekymring | Anbefaling |
|------|--------|-------------|-------------|------------------------------|------------|
| 1 | Thorakale misdannelser | 83,06% | L5 | Ingen kendt β3-AR-forbindelse til thorakal udvikling; sandsynlig modelstøj | Afvent |
| 3 | Nyremisdannelser med hepatisk og pancreatic dysplasi | 82,93% | L5 | Ciliopati (NPHP3-mutation); β3-AR/cAMP ikke forbundet med ciliær assembly eller planar cell polarity-veie | Afvent |
| 5 | PKD3 ± Polycystisk leversygdom | 82,20% | L4 | β3-AR → cAMP-akse **deler samme retning** som PKD-sygdomsvej; kan forværre cysteproliferation | Afvent |
| 7 | Joubert-syndrom med nyre-defekt | 80,89% | L5 | Ciliopati (AHI1/CEP290/TMEM67); β3-AR/cAMP ikke forbundet med IFT-system eller Hedgehog-signalering | Afvent |
| 9 | Adult familial nefronoftisis–spastisk kvadriparese | 80,32% | L5 | Ultrasjælden ciliopati; ingen mekanistisk forbindelse; patienttal for små til klinisk gennemførlighed | Afvent |

### PKD3 baggrundslitteratur

PKD3-indikationen (rang 5) er den eneste forudsigelse med tilhørende litteratur (20 publikationer). **Ingen af disse publikationer studerer mirabegron i PKD3; de er kun sygdomsbaggrundskontekst.** Desuden rejser den mekanistiske analyse en potentiel sikkerhedsbeskaffenhed: Mirabegronanals cAMP-forhøjende mekanisme stemmer overens med — i stedet for at modvirker — PKD3-sygdomsvej, hvilket potentielt kan accelerere cysteproliferation. Dette skal præciseres, før indikationen kan avanceres.

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|--------|-------------|
| [30819518](https://pubmed.ncbi.nlm.nih.gov/30819518/) | 2019 | Oversigt | *Lancet* | Omfattende ADPKD-oversigt: systemisk lidelse med nyre-cyster, hypertension, lever-cyster, intrakranielle aneurismer og hjerteklap-sygdom |
| [38958301](https://pubmed.ncbi.nlm.nih.gov/38958301/) | 2024 | Klinisk retningslinje | *Am J Gastroenterol* | ACG retningslinje om fokale leverlæsioner; omfatter ledelse af hepatiske cystiske læsioner, herunder polycystisk leversygdom |
| [35728731](https://pubmed.ncbi.nlm.nih.gov/35728731/) | 2022 | Klinisk retningslinje | *J Hepatol* | EASL-retningslinjer for cystiske leversygdomme: hepatiske cyster, polycystisk leversygdom, Caroli-sygdom — diagnose og ledelse |
| [35487607](https://pubmed.ncbi.nlm.nih.gov/35487607/) | 2022 | Oversigt | *Clin Liver Dis* | ADPKD- og polycystisk leversygdomsoversigt; tolvaptan's rolle i at bremse nyrfunktionsnedgang og cystevasext |
| [29038287](https://pubmed.ncbi.nlm.nih.gov/29038287/) | 2018 | Oversigt | *JASN* | Otte gener forbundet med ADPKD/ADPLD identificeret, herunder GANAB — genet impliceret i PKD3 |
| [38097330](https://pubmed.ncbi.nlm.nih.gov/38097330/) | 2023 | Oversigt | *Adv Kidney Dis Health* | Genetisk spektrum af PKD/PLD: PKD1 tegner sig for ~80% af ADPKD; primær ciliær dysfunktion er central for patogenesen |
| [34724412](https://pubmed.ncbi.nlm.nih.gov/34724412/) | 2022 | Oversigt | *Annu Rev Pathol* | PLD-patogenese: sekvens af primære genmutationer → cysteinitiering → hepatisk cystogenesis-progression; potentielle terapeutiske mål |
| [28375157](https://pubmed.ncbi.nlm.nih.gov/28375157/) | 2017 | Basisforskning | *J Clin Invest* | Helt eksomsekvensering i 102 PCLD-patienter identificerer nye årsaggende gener; isolerede PCLD-gener fungerer som effektorer af polycystin-1 |
| [36200122](https://pubmed.ncbi.nlm.nih.gov/36200122/) | 2022 | Oversigt | *Hepatic Med* | PLD-patofysiologi: ductal plate-misdannelse, ciliær dysfunktion og unormal cellesignalering driver cystogenesis |
| [37943238](https://pubmed.ncbi.nlm.nih.gov/37943238/) | 2023 | Oversigt | *Adv Kidney Dis Health* | Symptomatiske PLD-komplikationer, der opstår fra massiv cysteforstørrelse; leveren er det mest almindelige ekstrarenal sted i ADPKD |

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Ingen af de fem forudsagte indikationer præsenterer et troværdigt mekanistisk grundlag, der forbinder mirabegronanals β3-AR-agonisme til de forudsagte sygdomsveje, som alle involverer medfødte strukturelle defekter eller ciliopati med fundamentalt forskellige molekylære drivere. PKD3-forudsigelsen (rang 5) er den mest udviklet mekanistisk, men mirabegronanals cAMP-fremmende virkning stemmer teoretisk overens med — i stedet for at modvirker — sygdomsmekanismen, hvilket rejser et potentielt skadessignal, der skal løses, før yderligere forskning er berettiget.

**For at fortsætte er følgende nødvendigt:**

- **MOA-data**: Hent komplette mekanisme-for-handling-data fra DrugBank (DB08893) for at understøtte alle mekanistiske plausibilitetsvurderinger
- **Sikkerhedsdata**: Indhent det godkendte produktresumé (SmPC) (EMA Betmiga EU/1/12/809) for at etablere den fulde sikkerhedsprofil, herunder advarsler, kontraindikationer og kendt lægemiddelinteraktioner
- **Dansk regulatorisk bekræftelse**: Bekræft Betmigas aktuelle tilgængelighed i Danmark under EMA centraliserede godkendelsessti med Lægemiddelstyrelsen
- **PKD3 cAMP-retningsstudie**: Før PKD3 kan overvejes yderligere, er dedikerede mekanistiske studier påkrævet for at bestemme, om β3-AR-agonisme forværrer eller beskytter mod cysteproliferation i GANAB-mutant og ADPKD-modeller
- **Nedprioritér resterende indikationer**: Thorakale misdannelser, nyremisdannelser med hepatisk og pancreatic dysplasi, Joubert-syndrom og adult familial nefronoftisis–spastisk kvadriparese mangler alle understøttende beviser og biologisk plausibel mekanistisk forbindelse — yderligere undersøgelse anbefales ikke på dette tidspunkt

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

