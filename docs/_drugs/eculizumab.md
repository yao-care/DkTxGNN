---
layout: default
title: Eculizumab
parent: Kun modelforudsigelse (L5)
nav_order: 154
evidence_level: L5
indication_count: 10
---

# Eculizumab
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

# Eculizumab: Fra komplementmedierte sygdomme til cyklisk hæmatopoiese

## Sammenfatning i en sætning

Eculizumab (Soliris) er et humaniseret monoklonalt antistof, der blokerer terminal komplementaktivering, og er internationalt godkendt til paroxysmalt nokturnal hæmoglobinuri (PNH), atypisk hæmolytisk uræmisk syndrom (aHUS), generaliseret myasthenia gravis (gMG) og neuromyelitis optica-spektrumsygdom (NMOSD).
TxGNN-modellen forudsiger, at det kan være effektivt til **cyklisk hæmatopoiese** (cyklisk neutropeni),
med **ingen kliniske forsøg** og **ingen publikationer**, der i øjeblikket understøtter denne specifikke indikation — denne forudsigelse er baseret alene på modelinferens.

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ikke registreret i Danmark; internationalt godkendt til PNH, aHUS, gMG og NMOSD |
| Forudsagt ny indikation | Cyklisk hæmatopoiese (cyklisk neutropeni) |
| TxGNN-forudsigelsesscore | 99.97% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanismedata er ikke tilgængelige i det aktuelle bevissamling. Baseret på publiceret farmakologi er eculizumab et humaniseret IgG2/4κ monoklonalt antistof, der binder med høj affinitet til komplementprotein C5 og blokerer dets spaltning til C5a (et pro-inflammatorisk anafylatoksin) og C5b (nukleringseenheden i membranangrebskomplekset, MAC). Dette forhindrer terminal komplementvejsaktivering, nedstrøms cellelyse og komplementdrevet inflammation. Dets etablerede virkning ved PNH og aHUS kan direkte tilskrives denne mekanisme, da begge tilstande karakteriseres ved ukontrolleret alternativ komplementaktivering, der forårsager hæmolyse og trombotisk mikroangiopati.

Cyklisk hæmatopoiese (cyklisk neutropeni) er en genetisk distinkt lidelse, der primært er forårsaget af autosomalt dominante mutationer i ELANE-genet, der koder for neutrofil-elastase. Disse mutationer udløser endoplasmatisk retikulumstress og accelereret apoptose af neutrofil-forløberceller, hvilket producerer karakteristiske 21-dages oscillationer i cirkulerende neutrofil-antal. Sygdomsmekanismen er fundamentalt intracellulær — endoplasmatisk retikulummediert stressrespons fra ufoldet protein og mitokondrial apoptotisk signalering — snarere end ekstracellulær komplementdrevet ødelæggelse.

Den mekanistiske sammenhæng mellem eculizumabs C5-blokeringsaktivitet og ELANE-medieret patologi ved cyklisk hæmatopoiese er derfor i bedste fald indirekte. Selvom komplementaktivering teoretisk kan bidrage til neutrofil-clearance i nogle hæmatologiske sammenhænge, er dette ikke en primær drivkraft for cyklisk neutropeni. TxGNN-modellens høje forudsigelsesscore afspejler sandsynligvis indirekte forbindelser inden for vidensgrafen mellem komplementsystem-knuder og hæmatopoietiske netværksknuder, snarere end et direkte farmakologisk forhold understøttet af eksperimentelle beviser.

---

## Klinisk forsøgsbeviser

Der er i øjeblikket ingen registrerede kliniske forsøg relateret til eculizumab ved cyklisk hæmatopoiese.

---

## Litteraturbeviser

Der er i øjeblikket ingen litteratur tilgængelig for eculizumab ved cyklisk hæmatopoiese.

---

## Sikkerhedshensyn

Se venligst den godkendte Produktinformationsbeskrivelse (SmPC) for sikkerhedsinformation.

> **Bemærk:** Eculizumab har en velkendt risiko for livstruende *Neisseria meningitidis*-infektioner. Alle patienter behandlet med eculizumab internationalt skal være vaccineret mod meningokokkersygdom forud for behandlingsstart og kan have behov for profylaktisk antibiotika. Denne sikkerhedshensyn er kritisk for enhver fremtidig brugesvurdering, uanset indikation.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Der er ingen klinisk forsøgsbeviser eller sygdomsspecifik litteratur, der understøtter brugen af eculizumab ved cyklisk hæmatopoiese, og det mekanistiske grundlag for TxGNN-forudsigelsen er svagt — cyklisk neutropeni er drevet af intracellulær ELANE-medieret endoplasmatisk retikulumstress, en vej, der ligger uden for eculizumabs C5-komplementblokeringsmekanisme. Derudover er eculizumab ikke registreret i Danmark, hvilket gør nær-termins klinisk anvendelse umulig uden en formelt regulatorisk vej.

**For at fortsætte er følgende nødvendig:**

- **Præklinisk mekanistisk beviser:** Mindst en in vitro- eller dyremodel-undersøgelse, der demonstrerer en komplementafhængig komponent i ELANE-medieret apoptose af neutrofil-forløberceller
- **Regulatoriske data:** Hentelse af den godkendte SmPC (Soliris EU/EMA-produktinformation, EU/1/07/393) for at fuldende sikkerhedsprofil, herunder advarsler, kontraindikationer og meningokokokker-profylaksekrav
- **Formelle MOA-data:** DrugBank eller EMA EPAR-data, der bekræfter den molekylære farmakologi for at forfine den mekanistiske plausibilitetsanalyse
- **Indikationskontekstgennemgang:** Præcisering af, om TxGNN-modellen blander cyklisk hæmatopoiese med andre komplementrelaterede neutrofil-lidelser (f.eks. aHUS-associeret neutropeni) inden for sin videnskabsgraf
- **Regulatorisk vejvurdering:** Evaluering af EMA-centraliseret procedures anvendelighed for enhver fremtidig compassionate use eller klinisk forsøgsansøgning i Danmark

---

> ⚠️ **Ansvarsfraskrivelse:** Denne rapport er beregnet til formål vedrørende forskningsreferencer og udgør ikke medicinsk rådgivning. Alle kandidater til lægemiddelomfunktionalisering kræver streng klinisk validering før enhver anvendelse i patientbehandling.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

