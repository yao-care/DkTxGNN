---
layout: default
title: Pemigatinib
parent: Kun modelforudsigelse (L5)
nav_order: 343
evidence_level: L5
indication_count: 10
---

# Pemigatinib
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

# Pemigatinib: Fra Uregistreret Oprindelig Indikation til Multipel Endokrin Neoplasi

## Resumé i én sætning

> Pemigatinib's oprindeligt godkendte indikation er ikke registreret i dette bevismaterirum (datakløft DG002), selvom modellens egen rationaletext identificerer det som en FGFR1/2/3 kinasehæmmer.
> TxGNN-modellens toprangerede signal er **Multipel Endokrin Neoplasi**, men denne prognose understøttes ikke af nogen klinisk forsøg eller litteraturbevis, og det ledsagende mekanistiske rationale selv markerer det som et sandsynligt vidensgrafartefakt snarere end et ægte biologisk signal.
> På tværs af alle 10 prognoser i dette pakke når ingen et handlingsdygtigt bevisniveau – det bedst understøttede signal (HER2-positiv brystcancer) er kun L4/"Forskningen spørgsmål," og Pemigatinib er ikke i øjeblikket markedsført i Danmark.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig Indikation | Ikke registreret i dette bevismaterirum (datakløft — bekræft via DrugBank/SmPC) |
| Prognose for ny indikation | Multipel Endokrin Neoplasi |
| TxGNN Prognosescore | 99,71% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afgør at vente |

---

## Hvorfor er denne prognose rimelig?

Detaljerede virkemådedata er ikke tilgængelige som et struktureret felt i dette bevismaterirum (datakløft DG002). Imidlertid beskriver modellens eget gentilsynsvirkningsrationale konsistent Pemigatinib som en FGFR1/2/3 (fibroblasttilværekstfaktorreceptor) tyrosinkinasehæmmer, så denne klassificering kan behandles som pålidelig kontekst snarere end en fabrikeret tilføjelse.

For det toprangerede signal, **Multipel Endokrin Neoplasi (MEN)**, er rationalet teksten eksplicit negativ: MEN er drevet af germline-mutationer i *RET*, *MEN1* og *CDKN1B*, hvoraf ingen har et kendt direkte forhold til FGFR-signalering. Rationalet angiver, at der ikke er litteratur- eller præklinisk støtte til, at en FGFR-hæmmer har nogen rolle i MEN, og det markerer eksplicit denne prognosescore som "manglende en forklarlig biologisk basis," mistænkt at stamme fra indirekte co-occurence-støj i vidensgrafen snarere end et sandt medicin-sygdoms-forhold. Den samme sygdom vises to gange på den rangerede liste (rang 1 og 2) med identiske scores, hvilket er i overensstemmelse med en duplikeringsgenstande i den underliggende prognosetabel snarere end uafhængigt bekræftende bevis.

Det tredie rangerede signal, **amenore**, er endnu mere bekymrende fra et sikkerhedssynspunkt: FGFR1-funktionalverlust er en kendt årsag til Kallmann-syndrom / hypogonadotropisk hypogonadisme, som kan præsentere sig med amenore. Da Pemigatinib farmakologisk *hæmmer* FGFR (samme retning som funktionalverlust-mutationen), angiver rationalet eksplicit, at dette bør læses som et potentielt **sikkerhedssignal** (dvs. Pemigatinib kunne plausibelt forårsage eller forværre amenore), ikke som bevis for terapeutisk fordel. Denne kandidat bør ikke tolkes som en gentilsyningsmulighed.

Det eneste signal med nogen litteraturstøtte er **HER2-positiv brystcancer** (rang 5–6, score 99,49%, bevisniveau L4, beslutningsstadium S1 "Forskning Spørgsmål"). Rationalet beskriver en plausibel indirekte mekanisme: FGFR1/2 amplifikation/aktivering er blevet rapporteret i litteraturen som en bypass-modstandsvej til anti-HER2-terapier (f.eks. trastuzumab, lapatinib), hvilket foreslår en teoretisk rolle for en FGFR-hæmmer som Pemigatinib som en *tilføjelse* til at overvinde HER2-målrettet terapimodstand — ikke som monoterapi for HER2-positiv brystcancer i sig selv. Det eneste støttende citat er imidlertid en generel 2021-gennemgang af FDA-godkendte kinasehæmmere, ikke en undersøgelse specifik for Pemigatinib eller denne kombinationshypotese, så dette forbliver et forsøgsspørgsmål snarere end en understøttet indikation.

To yderligere poster — **infektiøs bovint rhinotracheitis** og **ondsindet katarr** — er veterinær-/drøvtyggelliderherpesvirus-sygdomme uden relevans for menneskelig medicingentilsyning; rationalet markerer disse som sandsynlig tværarts-ontologi-forurening i vidensgrafen og anbefaler, at de udelukkes under datagranskning snarere end evalueres yderligere. **Cytomegalovirus-infektion** har ligeledes intet rationalt understøttet mekanistisk link til FGFR-signalering og ingen litteratur- eller forsøgsbevis.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

*(Dette gælder for den toprangerede indikation, Multipel Endokrin Neoplasi. Ingen kandidat-sygdom i dette bevismaterirum — på tværs af alle 10 rangerede poster — har noget registreret ClinicalTrials.gov eller ICTRP-forsøg.)*

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig for den toprangerede indikation (Multipel Endokrin Neoplasi).

### Andre prognosticerede signaler i dette bevismaterirum

For transparens, da dette pakke indeholder 10 rangerede poster (5 unikke sygdomme, hver duplikeret), hører det ene litteraturcitat, der eksisterer, til en lavere-rangeret, højere-bevis-niveau kandidat:

| PMID | År | Type | Tidsskrift | Tilknyttet sygdom | Vigtige resultater |
|------|-----|------|------|------|---------|
| [33513356](https://pubmed.ncbi.nlm.nih.gov/33513356/) | 2021 | Gennemgang | Pharmacological Research | HER2-positiv brystcancer | Generel gennemgang af FDA-godkendte kinasehæmmere; ikke specifik for Pemigatinib eller til en FGFR/HER2-kombinationsstrategi |

| Sygdom (unik) | Bedste TxGNN score | Bevisniveau | Beslutningsstadium | Anbefaling | Forbehold |
|---|---|---|---|---|---|
| Multipel endokrin neoplasi | 99,71% | L5 | S0 | Afgør at vente | Intet mekanistisk link til FGFR; mistænkt vidensgrafartefakt |
| Amenore | 99,54% | L5 | S0 | Afgør at vente | Mekanisme peger på, at Pemigatinib *forårsager* amenore, ikke behandler det — sikkerhedssignal, ikke terapeutisk |
| HER2-positiv brystcancer | 99,49% | L4 | S1 | Forskning Spørgsmål | Kun kandidat med nogen litteratur; hypotese er kombination-med-anti-HER2-terapi, ikke monoterapi |
| Cytomegalovirus-infektion | 99,46% | L5 | S0 | Afgør at vente | Intet kendt mekanistisk link |
| Infektiøs bovint rhinotracheitis / Ondsindet katarr | 99,43% | L5 | S0 | Afgør at vente | Veterinær-/dyresygdomme — sandsynlig tværarts-ontologi-støj; anbefal udelukkelse fra rangering |

Ingen kandidat i dette pakke understøtter i øjeblikket en Gå-beslutning.

---

## Markeds­information for Danmark

Pemigatinib er **ikke i øjeblikket markedsført i Danmark**. Bevisumaterialet registrerer 0 Markedsføringstilladelser (hverken nationale Laegemiddelstyrelsen eller centraliserede EMA-tilladelser), så ingen produkt/doserings-form-tabel kan produceres på dette tidspunkt.

---

## Sikkerhedshensyn

Venligst se den godkendte Produktkarakteristik (SmPC) for sikkerhedsinformation. Dette bevismaterirum indeholder ikke i øjeblikket vigtige advarsler, kontraindikationer eller medicin-medicin-interaktionsdata for Pemigatinib (datakløft DG001, markeret som Blokering-alvor — dette skal løses, før nogen S1 sikkerhedspræ-vurdering kan gennemgås).

---

## Konklusion og næste trin

**Beslutning: Afgør at vente**

**Rationale:**
- Toprangeringsprognosen (Multipel Endokrin Neoplasi) er eksplicit markeret af dets eget mekanistiske rationale som manglende biologisk plausibilitet og sandsynligvis repræsenterer vidensgrafartefakt, med nul understøttende forsøg eller litteratur.
- Den anden kandidat (amenore) peger på et sandsynligt **sikkerhedssignal** snarere end en terapeutisk mulighed givet Pemigatinib's FGFR-hemmende mekanisme.
- Den eneste kandidat, der når et "Forskning Spørgsmål" stadium (HER2-positiv brystcancer, kombinationshypotese), understøttes af en enkelt ikke-specifik review-artikel, ikke primært bevis.
- Blokering sikkerhedsdata (dansk SmPC advarsler/kontraindikationer, DG001) og mekanisme-for-virkning bekræftelse (DG002) mangler begge, så denne kandidat kan ikke gå videre til en S1 sikkerhedspræ-vurdering uanset hvilket sygdomsmål der er valgt.
- Pemigatinib er ikke markedsført i Danmark, så der er ingen eksisterende lokal regulerings-/sikkerhedsdossier at trække på.

**For at gå videre er følgende nødvendigt:**
- Løs DG001: få Pemigatinib's godkendte advarsler/kontraindikationer (f.eks. fra EMA SmPC, da det ikke er registreret i Danmark) — i øjeblikket en Blokering-kløft
- Løs DG002: bekræft mekanisme-for-virkning via DrugBank API
- Bekræft og dokumentér Pemigatinib's oprindelig godkendte indikation(er), som helt mangler fra dette bevismaterirum
- Markér veterinær-sygdoms-posterne (infektiøs bovint rhinotracheitis, ondsindet katarr) til vidensgrafdatagranskningen pipeline til sandsynlig udelukkelse
- Hvis amenore-signalet forfølges overhovedet, omdiriger det til farmakovigilans/bivirknings-gennemgang snarere end gentilsyns-evaluering
- Hvis HER2-positiv brystcancer kombinationshypotesen forfølges, bestil en målrettet litteratursøgning specifikt på FGFR-hæmmer + anti-HER2-terapi modstands-reversering, snarere end at stole på det aktuelle generelle kinasehæmmer-review-citat

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

