---
layout: default
title: Darbepoetin Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 130
evidence_level: L5
indication_count: 0
---

# Darbepoetin Alfa
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **0** stk.
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

# Darbepoetin Alfa: Evaluering afventer — Ingen aktiv TxGNN-genbrugsprognose

## Sammenfatning i én sætning

Darbepoetin alfa er et hyperglykosileret erythropoeseunderstøttende agens (ESA), der internationalt er indiceret til behandling af anæmi ved kronisk nyrensygdom og kemoterapirelateret anæmi.
TxGNN-modellen genererede **ingen genbrugsprognose** for denne kandidat i det aktuelle kørselsforløb.
To blokerende eller høj-alvorlighedsgrad-datakløfter — manglende regulatoriske advarseldata og manglende handlingsmekanismedata — forhindrer formel evaluering og skal løses, før pipelinen kan køres igen.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Anæmi (kronisk nyrensygdom; kemoterapirelateret) — baseret på internationale kilder; ikke udfyldt i evidenspakken |
| Forudsagt ny indikation | — (ingen prognose genereret) |
| TxGNN-prognosescore | — |
| Evidensniveau | Ikke vurderbar (pipeline returnerede ingen kandidater) |
| Danske markedsstatus | Ikke markedsført (ifølge evidenspakken) |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | **Hold** |

---

## Hvorfor ingen prognose blev genereret

TxGNN-pipelinen returnerede en tom liste over `predicted_indications` for darbepoetin alfa (DrugBank: DB00012). Baseret på evidenspakkens metadata og datakløftlogg skyldes det højst sandsynligt:

**1. Manglende handlingsmekanisme (DG002 — høj alvorlighed)**
TxGNN's grafneuralnetværksræsonnement afhænger af medicin–protein–sygdom forbindelser i vidensgraf. Uden MOA-annotationen — specifikt medicinets målproteiner og farmakologisk klasse — er medicinnoden sandsynligvis utilstrækkeligt forbundet til at vurdere kandidat-sygdomassociationer. Darbepoetin alfa virker via erythropoietinreceptoren (EPOR) og nedstrøms JAK2/STAT5-signalering; denne information er velkendt i DrugBank, men blev ikke hentet i det aktuelle kørselsforløb.

**2. Tom original-indikationsliste**
Feltet `original_indications` er ikke udfyldt. Prognose-pipelinen kan være afhængig af eksisterende indikationsanker til at initialisere søgningen i sygdomsomegnen. Uden dem kan kandidatvurdering være blevet udeladt eller returneret under rapporteringstærskelen.

**3. Blokerende datakløft (DG001 — blokering alvorlighed)**
Lokale regulatoriske advarsels- og kontraindikationsdata er fraværende. Selvom dette ikke direkte påvirker prognosealgorritmen, forhindrer det efterfølgende sikkerhedsscreening af hypotetiske kandidater, hvilket gør hele evalueringen ufuldstændig, selv hvis prognoser var tilgængelige.

Darbepoetin alfa er et etableret biologisk lægemiddel med en lang sikkerhed- og effektivitetshistorie. Genbrugshypoteser udforsket i litteraturen omfatter neuroprotektion (iskæmisk apopleksi, traumatisk hjerneskade), kardioprotektion (akut myokardieinfarkt) og anti-inflammatoriske anvendelser — alle drevet af EPOR-udtryk uden for erythroidt væv. Ingen af disse optræder i denne evidenspakke.

---

## Information om det danske marked

Evidenspakken registrerer **nul markedsføringstilladelser** for darbepoetin alfa og en markedsstatus på "ikke markedsført."

> ⚠️ **Datakonsistensadvarsel**: Dette ser ud til at være inkonsistent med offentligt tilgængelig information. Aranesp® (darbepoetin alfa, Amgen Europe B.V.) har en centraliseret EMA-markedsføringstilladelse (EU/1/01/183/001–020), der er gyldig på tværs af alle EU/EØS-medlemsstater, herunder Danmark, siden 2001. Efterforskere bør bekræfte den aktuelle tilladelsestatus direkte ved:
> - [EMA EPAR for Aranesp](https://www.ema.europa.eu/en/medicines/human/EPAR/aranesp)
> - Det danske Lægemiddelstyrelsens produktdatabase ([laegemiddelstyrelsen.dk](https://www.laegemiddelstyrelsen.dk))
>
> Evidenspakkekandidatens ID bærer et `TW-` præfiks, hvilket tyder på, at regulatoriske data blev hentet fra et taiwansk markedsdatasæt snarere end det danske/EMA-register. Dette skal rettes, før Danmark-specifikke konklusioner drages.

---

## Sikkerhedshensyn

Alle sikkerhedsfelter i evidenspakken er registreret som datakløfter. Ingen advarsels-, kontraindikations- eller medicin–medicin-interaktionsdata er tilgængelige til evaluering inden for denne pakke.

> Venligst se den godkendte Produktinformationsbog (SmPC) for alle darbepoetin alfa-indeholdende produkter for fuldstændig sikkerhedsinformation.

Vigtige sikkerhedsområder, der bør gennemgås i SmPC før enhver genbrugsevaluering, inkluderer:

- **Kardiovaskulær risiko**: Tromboemboliske begivenheder og øget dødelighed er blevet rapporteret, når ESA'er blev brugt til at målsætte hæmoglobinniveauer over det godkendte område
- **Tumorprogrediering**: EPOR udtrykkes på nogle tumorcellelinjer; ESA-brug i onkologiske indstillinger kræver omhyggelig nytte–risiko-vurdering
- **Ren rød celle aplasi (PRCA)**: Sjælden men alvorlig immunrelateret bivirkning; neutraliserende anti-erythropoietin antistof
- **Hypertension**: Nyopdukket eller forværret hypertension er en kendt klasseffekt

---

## Konklusion og næste trin

**Afgørelse: Hold**

**Begrundelse:**
TxGNN-pipelinen returnerede ingen genbrugskandidater for dette lægemiddel, og to uløste datakløfter — en blokering og en høj-alvorlighedsgrad — forhindrer enhver meningsfuld sikkerhed- eller mekanistisk evaluering. Ingen rapportsektioner kan fuldføres baseret udelukkende på den aktuelle evidenspakke.

**For at fortsætte kræves følgende:**

1. **Løs DG001 (Blokering)** — Hent og parse den gældende Produktinformationsbog (EMA Produktinformationsbog for Aranesp® anbefales) for at udvinde advarsler, kontraindikationer og data om specialpopulationer
2. **Løs DG002 (Høj)** — Søg i DrugBank API (`DB00012`) for handlingsmekanisme, primære mål (EPOR, JAK2) og farmakologisk klasse
3. **Ret regulatoriske datakilde** — Erstat `TW-` taiwanske regulatoriske data med data hentet fra EMA/Lægemiddelstyrelses-registeret; udfyld `total_licenses` og `licenses` tilsvarende
4. **Udfyld `original_indications`** — Tilføj de internationalt anerkendte indikationer, så prognose-pipelinen kan bruge dem som grafanker
5. **Kør TxGNN-prognose-pipelinen igen** — Når MOA- og indikationsdata er udfyldt, genexekver både KG- og DL-prognosestrin for at generere rangerede kandidatindikationer
6. **Genovervej** — En fuldstændig L1–L5-evidensvurdering, klinisk forsøgstabel og litteraturgennemgang kan kun fuldføres, når mindst en prognosekandidater returneres

---

*Denne rapport blev genereret den 2026-04-05. Resultaterne er til forskningsformål alene og udgør ikke medicinsk rådgivning. Enhver genbrugskandidater skal gennemgå klinisk validering før brug.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

