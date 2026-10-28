---
layout: default
title: Probenecid
parent: Moderat evidens (L3-L4)
nav_order: 686
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-28
monitor_inn: "PROBENECID"
predicted_indications: ["hypouricemia, renal", "Lesch-Nyhan syndrome", "hypoxanthine guanine phosphoribosyltransferase partial deficiency"]
description: "Probenecid: forudsagt ny indikation Renal hypouricæmi (hypouricemia, renal) (evidensniveau L4). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Probenecid
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **3** stk.
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

## Probenecid: Renal hypouricæmi (hypouricemia, renal)
{: .text-alpha }

## Resumé

Probenecid er et urinsyreudskillende (uricosurisk) lægemiddel, der oprindeligt bruges til behandling af urinsyregigt og hyperurikæmi.
TxGNN-modellen forudsiger, at det kan være virksomt ved **renal hypouricæmi**, men der er **ingen registrerede kliniske forsøg** og kun **indirekte litteratur** (primært case reports og oversigtsartikler).
Den forudsagte virkning er mekanistisk modsat rettet af det, man ville forvente, så forudsigelsen bør tolkes med stor forsigtighed.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Renal hypouricæmi (hypouricemia, renal) |
| TxGNN-forudsigelsesscore | 0.9973 |
| Evidensniveau | L4 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i de data, der er indsamlet til denne rapport. Ud fra kendt farmakologi hæmmer probenecid urattransportøren URAT1 (SLC22A12) samt OAT1/OAT3. Det reducerer genoptagelsen af urat i nyrerne og øger udskillelsen af urinsyre, hvilket er grunden til, at det virker mod urinsyregigt.

Renal hypouricæmi skyldes hovedsageligt funktionstabsmutationer i URAT1 (SLC22A12) eller GLUT9 (SLC2A9), så patienterne har allerede en for høj urat-udskillelse via nyrerne. Yderligere hæmning af URAT1 ville forventeligt forværre tilstanden frem for at behandle den. Den høje TxGNN-score skyldes sandsynligvis, at lægemidlet og sygdommen ligger tæt på hinanden i vidensnetværket (fælles urattransportgener og -veje) og afspejler næppe et reelt terapeutisk signal.

Probenecid anvendes i stedet som farmakologisk prøvestof i studier af nyrernes håndtering af urat, bl.a. til at karakterisere defekter i reabsorption og sekretion hos patienter med renal hypouricæmi.

Modellen foreslår også andre indikationer med højt score, nemlig **Lesch-Nyhans syndrom** (score 0,9939) og **partiel HPRT-mangel** (score 0,9937). Begge giver purinoverproduktion og hyperurikæmi. Probenecid kan teoretisk sænke serum-urat, men løser ikke den underliggende overproduktion og øger risikoen for urinsyrenefropati og nyresten. Xanthinoxidasehæmmere (f.eks. allopurinol) er standardbehandling. Ved Lesch-Nyhan påvirker probenecid desuden ikke de neuroadfærdsmæssige symptomer, som er det primære uopfyldte behov.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Tabellen viser et udvalg af de publikationer, der er fundet for renal hypouricæmi. Ingen af dem undersøger probenecid som behandling.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [16678460](https://pubmed.ncbi.nlm.nih.gov/16678460/) | 2006 | Oversigtsartikel | Mol Genet Metab | Arvelig renal hypouricæmi skyldes oftest funktionstabsmutationer i SLC22A12 (URAT1) |
| [31650389](https://pubmed.ncbi.nlm.nih.gov/31650389/) | 2020 | Oversigtsartikel | Clin Rheumatol | Opdatering til reumatologer om årsager til og håndtering af hypouricæmi |
| [14694169](https://pubmed.ncbi.nlm.nih.gov/14694169/) | 2004 | Kohorte (genetisk/klinisk) | J Am Soc Nephrol | SLC22A12 sekventeret hos 32 patienter; URAT1-genets betydning for urat-udskillelse |
| [7771493](https://pubmed.ncbi.nlm.nih.gov/7771493/) | 1995 | Oversigt/case report | Am J Kidney Dis | Forebyggelse af anstrengelsesudløst akut nyresvigt ved renal hypouricæmi |
| [8976099](https://pubmed.ncbi.nlm.nih.gov/8976099/) | 1996 | Oversigtsartikel | Nihon Rinsho | Begreb og klassifikation af forstyrrelser i urat-stofskiftet |
| [854144](https://pubmed.ncbi.nlm.nih.gov/854144/) | 1977 | Case-serie (fysiologisk) | Nephron | Svækket respons på probenecid og pyrazinamid ved familiær hypouricæmi (reabsorptionsdefekt) |
| [2709741](https://pubmed.ncbi.nlm.nih.gov/2709741/) | 1989 | Case report | Klin Wochenschr | Akut nyresvigt pga. urinsyrenefropati; probenecid øgede udskillelsen af urinsyre (brugt diagnostisk) |
| [8302413](https://pubmed.ncbi.nlm.nih.gov/8302413/) | 1993 | Case report | Nephron | Probenecid og benzbromaron øgede urat-clearance (diagnostisk brug); urinvejssten behandlet med alkalinisering |
| [9583212](https://pubmed.ncbi.nlm.nih.gov/9583212/) | 1998 | Case report | Acta Paediatr Jpn | Anstrengelsesudløst akut nyresvigt hos en pige med renal hypouricæmi |
| [3813739](https://pubmed.ncbi.nlm.nih.gov/3813739/) | 1987 | Case report | Arch Intern Med | Diabetisk renal hypouricæmi med øget urat-clearance |

For Lesch-Nyhans syndrom er der kun to indirekte publikationer (en beregningsmodel af urat-stofskiftet fra 2013, [24078686](https://pubmed.ncbi.nlm.nih.gov/24078686/), og en biokemisk oversigt fra 1976 om Tourettes syndrom, [1070064](https://pubmed.ncbi.nlm.nih.gov/1070064/)). For partiel HPRT-mangel findes ingen litteratur.

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100744876 | Probenecid "Medic" (Viatris ApS) | Tabletter | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

**Kontraindikationer/sygdomme med risikosignal (fra TxGNN-vidensgrafen, ikke fra produktresumé):**
TxGNN-modellen (deep learning) giver score for bl.a. leversvigt, nyresygdom og nedsat nyrefunktion, blodsygdomme (trombocytopeni, leukopeni, agranulocytose, neutropeni og flere medfødte former for neutropeni), mavesår, muskelsygdomme (myopati, rabdomyolyse, familiær periodisk paralyse), samt diarrésygdomme (herunder *Clostridium difficile*-colitis og nekrotiserende enterokolitis hos nyfødte). Scorerne kommer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

**Lægemiddelinteraktioner:** I alt 71 interaktioner er identificeret. De vigtigste:
- **Alvorlige (Major):** phenylbutyrinsyre, glycerolphenylbutyrat
- **Moderate:** acetylsalicylsyre, sulfonylurinstoffer og beslægtede antidiabetika (chlorpropamid, glimepirid, glipizid, glibenclamid, tolbutamid, tolazamid, acetohexamid), repaglinid og nateglinid
- **Milde:** bl.a. famotidin, amoxicillin, levofloxacin, eluxadolin

Ud over ovenstående henvises til det godkendte produktresumé (SmPC) for fuldstændige advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Der er ingen kliniske forsøg og kun indirekte litteratur, og probenecids virkningsmekanisme (øget urat-udskillelse) peger i modsat retning af et terapeutisk behov ved renal hypouricæmi. De øvrige forudsagte indikationer (Lesch-Nyhan, partiel HPRT-mangel) har stærkt begrænset evidens, og et uricosurisk middel indebærer risiko for nyresten og urinsyrenefropati ved purinoverproduktion.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer mangler)
- Detaljerede data om virkningsmekanisme (MOA) fra DrugBank
- Specialistvurdering af, om der overhovedet er et klinisk rationale; for HPRT-relaterede tilstande eventuelt kun som supplement eller ved intolerans over for xanthinoxidasehæmmere
- Prækliniske eller kliniske data, der kan påvise en reel gavnlig effekt, før en evaluering kan fortsætte
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

