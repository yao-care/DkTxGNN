---
layout: default
title: Probenecid
parent: Kun modelforudsigelse (L5)
nav_order: 360
evidence_level: L5
indication_count: 6
---

# Probenecid
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
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

# Probenecid: Fra en udokumenteret oprindelig indikation til renale hypourikæmi

## Ét-sætning-sammenfatning

> Probenecid (DrugBank DB01032) er en veletableret urikosurik agent, men denne bevissamling dokumenterer ingen bekræftet oprindelig indikation eller virkningsmechanisme for den.
> TxGNN-modellen forudsiger en mulig forbindelse til **Renale hypourikæmi** ("hypourikæmi, renale") med en **99.73%** prognose-score, men dette er i øjeblikket understøttet af kun **0 kliniske forsøg** og **20 publikationer, der beskriver sygdommen selv snarere end probenecid som behandling for den**.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ikke dokumenteret i denne bevissamling (drug.original_indications er tom) |
| Forudsagt ny indikation | Renale hypourikæmi (hypourikæmi, renale) |
| TxGNN prognose-score | 99.73% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Suspendér |

---

## Hvorfor er denne forudsigelse fornuftig?

Detaljerede data om virkningsmechanismen for probenecid er ikke tilgængelige i denne bevissamling (markeret som datakløft DG002, høj alvorlighed), og ingen oprindelig indikation er på arkiv (drug.original_indications er tom). På grund af dette er den mekanistiske begrundelse nedenfor nødvendigvis begrænset og bør behandles som foreløbig i påvente af bekræftede MOA-data.

Der er en specifik bekymring værd at fremhæve: renale hypourikæmi er en tilstand med *abnormt lavt* serum-urinsyre forårsaget af defekt nyretubulær urinsyre-reabsorption, og farmakologisk er det det modsatte problem fra hyperurikæmi/podagra (som urikosurik medicin typisk bruges til at behandle ved *at øge* urinsyre-udskillelse). Efter gennemgang af de 20 understøttende publikationer vises probenecid ikke som en foreslået behandling for denne sygdom — det optræder gentagne gange som et **diagnostisk test-agens** ("probenecid-testen"), brugt af forskere til at karakterisere den defekte urinsyre-transporter (URAT1/SLC22A12) hos disse patienter (f.eks. PMID 8341392, PMID 7099326, PMID 854144). I flere af disse rapporter beskrives urinsyre-udskillelsen hos berørte patienter som minimalt responsiv, eller endda paradoksalt nedsat, når probenecid administreres.

Dette mønster er i overensstemmelse med den forsigtighed, der allerede er noteret andetsteds i denne bevissamling: den samme underliggende logik (en urikosurik medicin som ikke passer til en lavurinsyre-tilstand) er eksplicit hvorfor rang 3/4-kandidaten "Lesch-Nyhan-syndrom" allerede blev scoret **Bevisniveau L4, Suspendér** i denne samling, med bemærkningen at urikosurik agentier er relativt kontraindicerede i tilstande med urinsyre-overbelastning eller defekt urinsyre-håndtering. Da den samme klasse af mekanistisk mismatch gælder for renale hypourikæmi, bør top-ranget forudsigelse behandles med tilsvarende forsigtighed snarere end som en enkelt oldrug-ny-brug-mulighed.

---

## Klinisk forsøg-bevis

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

---

## Litteratur-bevis

| PMID | År | Type | Tidsskrift | Vigtige resultater |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Klassificering afventende | Molecular Genetics and Metabolism | Arvelig renale hypourikæmi forårsages af mutationer med tab af funktion i SLC22A12 (URAT1), transporteren ansvarlig for proksimal tubulær urinsyre-reabsorption |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Klassificering afventende | American Journal of Kidney Diseases | Oversigt over renale hypourikæmi og dets tilknytning til træningsudløst akut nyrenesvigt; diskuterer præventionsstrategier |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Klassificering afventende | Journal of the American Society of Nephrology | Klinisk/molekylær analyse af 32 japanske patienter med renale hypourikæmi; korrelerer SLC22A12-genotype med urinsyre-clearance |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Klassificering afventende | Archives of Internal Medicine | Diabetiske patienter viser øget pyrazinamid-suppressibel urinsyre-clearance underliggende diabetisk renale hypourikæmi |
| [14655203](https://pubmed.ncbi.nlm.nih.gov/14655203/) | 2003 | Klassificering afventende | American Journal of Kidney Diseases | Kasuistik af to søskende med arvelig renale hypourikæmi og træningsudløst akut nyrenesvigt |
| [1944743](https://pubmed.ncbi.nlm.nih.gov/1944743/) | 1991 | Klassificering afventende | Nephron | Undersøgelse af urikosurik-mekanismer hos type I-diabetikere med forhøjet urinsyre-clearance og fraktioneret udskillelse |
| [1656732](https://pubmed.ncbi.nlm.nih.gov/1656732/) | 1991 | Klassificering afventende | American Journal of Kidney Diseases | Kasuistik: cholangiocarcinoma forbundet med alvorlig renale hypourikæmi; nyre-mekanisme studeret |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Klassificering afventende | Clinical Rheumatology | Narrativ oversigt over hypourikæmi-ætiologi for praktiserende reumatologer |
| [8341392](https://pubmed.ncbi.nlm.nih.gov/8341392/) | 1993 | Klassificering afventende | Nephron | Ny undertype af renale hypourikæmi uden urinsyre-respons på hverken pyrazinamid eller **probenecid**-test |
| [7099326](https://pubmed.ncbi.nlm.nih.gov/7099326/) | 1982 | Klassificering afventende | Nephron | Familiær tilfælde hvor urinsyre-udskillelse var **paradoksalt nedsat** af probenecid-administration |

*Studie-type-klassificering for denne kandidat er markeret som "afventende" i kildedata; typer ovenfor vises som angivet snarere end udledt.*

---

## Markedsinformation for Danmark

Ingen markedsføringstilladelser er registreret for probenecid i denne bevissamling. Markedsstatus er anført som **Ikke markedsført**, med 0 i alt registrerede licenser.

---

## Sikkerhedshensyn

Se venligst den godkendte produktresumé (SmPC) for sikkerhedsinformation. Bemærk: denne bevissamling markerer lægemiddeletikettet advarsler og kontraindikationer-vurdering (DG001) som et **Blokerande** datakløft — en formel sikkerhedsvurdering kan ikke gennemføres før dette løses.

---

## Konklusion og næste trin

**Beslutning: Suspendér**

**Begrundelse:**
- Grundlæggende data mangler på Blokerande/høj alvorlighed-niveau (DG001: etiketadvarsler/kontraindikationer; DG002: virkningsmechanisme), så ingen formel sikkerhedsvurdering er i øjeblikket mulig.
- Den forudsagte indikation selv er mekanistisk tvivlsom: probenecid er en urikosurik agent, og den understøttende litteratur bruger den som en diagnostisk probe for defekt urinsyre-reabsorption snarere end som en foreslået terapi for renale hypourikæmi — et mismatch-mønster i overensstemmelse med "Suspendér" allerede tildelt den relaterede Lesch-Nyhan-kandidat i denne samme samling.
- Der er ingen kliniske forsøg og ingen dansk markedsføringstilladelse til at forankre en Go-beslutning.

**For at fortsætte, er følgende nødvendigt:**
- Bekræftet oprindelig indikation og virkningsmechanisme for probenecid (løs DG002)
- TFDA/dansk produktetiketadvarsler og kontraindikationer (løs DG001, Blokerande)
- Præcisering fra TxGNN/bevis-pipelinen om retning — dvs. hvorvidt "hypourikæmi, renale" var tilsigtet som en målsygdom til behandling eller afspejler en netværksforbindelse drevet af probenecids rolle som en urinsyre-transport-probe
- Hvis forfølgt videre, farmakologisk begrundelse for hvorfor øget urinsyre-udskillelse ville gavne en tilstand allerede karakteriseret ved overdreven urinsyre-tab

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

