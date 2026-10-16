---
layout: default
title: Conestat Alfa
parent: Høj evidens (L1-L2)
nav_order: 220
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Conestat Alfa: forudsagt ny indikation C1-inhibitormangel (evidensniveau L1). Oprindelig indikation: Arveligt angioødem"
monitor_inn: "Conestat alfa"
predicted_indications: ["C1 inhibitor deficiency", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "serpinopathy with toxic serpin polymerization", "hereditary angioedema with C1Inh deficiency", "hereditary angioedema with C1Inh deficiency", "primary release disorder of platelets", "primary release disorder of platelets", "pseudo-von Willebrand disease", "pseudo-von Willebrand disease"]
---

# Conestat Alfa
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

# Conestat alfa: Fra arveligt angioødem til C1-inhibitormangel

## Resumé i én sætning

Conestat alfa er et rekombinant humant C1-esteraseinhibitor-protein, som oprindeligt anvendes til behandling af akutte anfald af arveligt angioødem (HAE).
TxGNN-modellen forudsiger, at lægemidlet kan være effektivt ved **C1-inhibitormangel**, og der er **4 registrerede kliniske forsøg** og **9 publikationer** på området. Den forudsagte indikation ligger dog meget tæt på den allerede godkendte, så der er reelt tale om en on-label-indikation og ikke om egentlig repurposing.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Arveligt angioødem |
| Forudsagt ny indikation | C1-inhibitormangel |
| TxGNN-forudsigelsesscore | 99,999 % |
| Evidensniveau | L1 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med forholdsregler) |

*Bemærkning: Den kliniske indikationstekst i den danske tilladelse er ikke tilgængelig i de samlede data, så den oprindelige indikation er hentet fra TxGNN-vidensgrafen.*

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger i øjeblikket ikke detaljerede data om virkningsmekanismen i de samlede data. Ud fra kendt viden er conestat alfa en rekombinant form af humant C1-esteraseinhibitor (C1-INH), produceret i transgene kaniner. Det erstatter direkte det manglende eller dysfunktionelle C1-INH-protein og genopretter reguleringen af komplement-, kontakt- (kallikrein-kinin) og koagulationssystemet. Herved hæmmes blandt andet kallikrein, faktor XIIa og C1s/C1r, hvilket mindsker den bradykininmedierede hævelse.

Arveligt angioødem skyldes netop mangel på eller dysfunktion af C1-INH. "C1-inhibitormangel" og "arveligt angioødem med C1-INH-mangel" beskriver derfor i praksis den samme sygdomsmekanisme. Forudsigelsen bekræfter altså lægemidlets eksisterende, godkendte anvendelse og fungerer som en positiv kontrol for modellen.

**Øvrige forudsigelser med lav evidens:** Modellen forudsiger også *serpinopati med toksisk serpinpolymerisering*, *primær frigivelsesforstyrrelse af blodplader* og *pseudo-von Willebrands sygdom* (alle score ca. 99,99 %). For ingen af dem er der fundet kliniske forsøg eller litteratur (evidensniveau L5, beslutning: Hold). Der er ikke identificeret en klar mekanistisk sammenhæng:
- Ved serpinopatier ophobes polymerer inde i cellerne, hvilket eksogent, ekstracellulært C1-INH næppe kan korrigere.
- Pseudo-von Willebrand skyldes en gain-of-function-defekt i trombocytternes GPIb, hvor C1-INH ikke har en kendt virkning.

---

## Klinisk evidens

| Forsøgsnummer | Fase | Status | Deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00262301](https://clinicaltrials.gov/study/NCT00262301) | Fase 3 | Afsluttet | 75 | Randomiseret, placebokontrolleret, dobbeltblindet studie af rekombinant C1-INH ved akutte HAE-anfald |
| [NCT00225147](https://clinicaltrials.gov/study/NCT00225147) | Fase 2/3 | Afsluttet | 77 | Randomiseret, placebokontrolleret, dobbeltblindet studie af sikkerhed og effekt ved akutte HAE-anfald |
| [NCT02247739](https://clinicaltrials.gov/study/NCT02247739) | Fase 2 | Afsluttet | 32 | Randomiseret, dobbeltblindet 3-periode crossover-studie af profylakse mod angioødemanfald |
| [NCT04414631](https://clinicaltrials.gov/study/NCT04414631) | Fase 2 | Afbrudt | 80 | Forebyggelse af alvorlig SARS-CoV-2-infektion hos indlagte COVID-19-patienter; ikke relevant for C1-INH-mangel |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [30021471](https://pubmed.ncbi.nlm.nih.gov/30021471/) | 2018 | RCT-baseret gennemgang | Expert Rev Clin Immunol | Conestat alfa som profylakse mod anfald hos voksne og unge med HAE; godkendt til akutte anfald i Europa |
| [22946752](https://pubmed.ncbi.nlm.nih.gov/22946752/) | 2012 | Review | BioDrugs | Effekt ved akutte HAE-anfald vist i to ensartede randomiserede, placebokontrollerede studier |
| [23420425](https://pubmed.ncbi.nlm.nih.gov/23420425/) | 2013 | Systematisk review | Pneumonol Alergol Pol | Sammenligning af conestat alfa, plasmaafledt C1-INH og icatibant ved akutte anfald |
| [24801469](https://pubmed.ncbi.nlm.nih.gov/24801469/) | 2014 | Kohorte | Allergy Asthma Proc | Hjemmebehandling af 65 ødemepisoder hos to kvinder under virkelige forhold |
| [24556385](https://pubmed.ncbi.nlm.nih.gov/24556385/) | 2014 | Kohorte | Eur J Dermatol | Brug af rekombinant C1-INH ved resistente eller hyppige anfald af hereditært eller erhvervet angioødem |
| [39675680](https://pubmed.ncbi.nlm.nih.gov/39675680/) | 2025 | Kohorte | J Allergy Clin Immunol | Klinisk respons og blodtranskriptom ved behandling af HAE-prodromer sammenlignet med aktive anfald |
| [29357215](https://pubmed.ncbi.nlm.nih.gov/29357215/) | 2018 | Review | Skin Ther Lett | Nye behandlinger af HAE, herunder rekombinant C1-INH og kallikrein-kinin-hæmmere |
| [23776358](https://pubmed.ncbi.nlm.nih.gov/23776358/) | 2010 | Review | Appl Clin Genet | Behandling af akutte abdominale og ansigtsanfald med C1-INH |
| [19093699](https://pubmed.ncbi.nlm.nih.gov/19093699/) | 2008 | Review | Drugs | Aktuelle og nye behandlingsmuligheder ved HAE |

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105726916 | Ruconest (Pharming Group N.V.) | Pulver og solvens til injektionsvæske, opløsning | Indikationsteksten er ikke tilgængelig i de samlede data |

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er registreret 41 interaktioner. Blandt de vist er én af alvorlig grad (**Major**): **carfilzomib**. De øvrige viste er af moderat grad, blandt andet:
  - Androgener og anabolske steroider: oxandrolon, oxymetholon, stanozolol, testosteron, danazol, prasteronenantat
  - Østrogener og hormonelle præparater: ethinylestradiol, estradiol (inkl. topisk), konjugerede østrogener, esterificerede østrogener, diethylstilbestrol, drospirenon, dienestrol (topisk)
  - Trombolytika: alteplase, anistreplase
  - Erytropoiese-stimulerende midler: darbepoetin alfa, erythropoietin
- **Forholdsregler fra evidensgrundlaget:** Overvågning for overfølsomhed (produktet udvindes fra kaninmælk, og kaninallergi er en kendt kontraindikation) samt risiko for tromboemboli.

Hvad angår advarsler og kontraindikationer fra produktresuméet, henvises til det godkendte produktresumé (SmPC), da disse data ikke er tilgængelige.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails (fortsæt med forholdsregler)**

**Begrundelse:**
- Flere randomiserede, placebokontrollerede forsøg (heriblandt et afsluttet fase 3-forsøg og et fase 2/3-forsøg) understøtter effekten ved HAE med C1-INH-mangel, og lægemidlet er markedsført i Danmark. Forudsigelsen er dog en bekræftelse af den eksisterende indikation og ikke en ny repurposing-fund. De øvrige forudsagte sygdomme (serpinopati, trombocytfrigivelsesforstyrrelse, pseudo-von Willebrand) har kun modelstøtte og bør afvente (Hold).

**For at komme videre kræves:**
- Det danske produktresumé (advarsler, kontraindikationer og godkendt indikationstekst) fra Lægemiddelstyrelsen
- Detaljerede data om virkningsmekanisme (MOA) fra DrugBank
- Plan for overvågning af overfølsomhed (kaninallergi) og tromboemboli samt gennemgang af interaktionen med carfilzomib
- Hvis der ønskes nye indikationer: præklinisk eller mekanistisk dokumentation, før de lavt rangerede forudsigelser undersøges videre
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

