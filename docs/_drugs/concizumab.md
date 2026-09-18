---
layout: default
title: Concizumab
parent: Kun modelforudsigelse (L5)
nav_order: 121
evidence_level: L5
indication_count: 10
---

# Concizumab
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

# Concizumab: Fra Hæmofili til Diabetisk Katarakt

## Resumé på én sætning

Concizumab er et humaniseret monoklonalt antistof, der retter sig mod Tissue Factor Pathway Inhibitor (TFPI), og er under klinisk udvikling for hæmofili A og B, hvor det genskaber trombin-generering ved at inhibere TFPI-medieret bremsning af koagulation.
TxGNN-modellen forudsiger, at det kan være effektivt for **Diabetisk Katarakt**, med **0 kliniske forsøg** og **0 publikationer**, der i øjeblikket understøtter denne retning.
Denne forudsigelse er klassificeret som **L5** (kun modelforudsigelse) og medfører en **Hold**-anbefaling, der afventer mekanistisk plausibilitetsgennemgang og præcisering af sikkerhed.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Hæmofili A og B (under undersøgelse; ingen godkendt indikation registreret i Danmark) |
| Forudsagt ny indikation | Diabetisk Katarakt |
| TxGNN-forudsigelsesscore | 98,27% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanisme-data er ikke tilgængelige i det aktuelle Evidence Pack. Baseret på oplysninger indlejret i begrundelsesfelterne for omformål er concizumab et anti-TFPI-antistof, der har en **prokoagulant** effekt — det blokerer TFPI og derved aflaster inhibitionen af den eksrinse koagulationsvej og genskaber hemostase hos patienter med hæmofili.

Diabetisk katarakt er forårsaget af en helt anden patofysiologisk proces: kronisk hyperglykæmi driver sorbitol-ophobning i linsen via aldosreduktase-vejen, genererer avancerede glykerings-slutprodukter (AGE'er) og skaber oxidativt stress, der gradvist denaturerer linseprotein-krystalliner. **Der er ingen etableret mekanistisk forbindelse** mellem TFPI-inhibition eller koagulationsvejs-modulering og linseprotein-ophobning eller oxidativ skade.

Den høje TxGNN-score (98,27%) afspejler sandsynligvis en **graf-strukturel artefakt**: vidensgrafen indeholder en tæt forbundet "diabetes" komorbiditets-hub, og modellen udbreder signal indirekte fra Concizumab → hæmofili → diabetes-komplikationer → diabetisk katarakt-knuder, uden at dette repræsenterer en direkte farmakologisk forhold. En yderligere bekymring er, at Concizumabs prokoagulante egenskaber kan være **usikre** hos diabetiske patienter, som allerede har forhøjet mikrovaskular tromboserisiko; brug kunne teoretisk forværre retinal venetrombose eller andre okkulare mikrovaskulære komplikationer.

---

## Kliniske forsøgsbevis

Ingen relaterede kliniske forsøg er i øjeblikket registreret for concizumab i nogen katarakt-indikation.

---

## Litteraturbevis

Ingen relateret litteratur er i øjeblikket tilgængelig for concizumab i nogen katarakt-indikation.

---

## Markedsinformation for Danmark

Concizumab har ingen markedsføringstilladelser i Danmark (hverken nationale Laegemiddelstyrelsen eller centraliserede EMA-godkendelser). Medicinen markedsføres ikke i øjeblikket i Danmark.

---

## Sikkerhedshensyn

Se venligst den godkendte produktresumé (SmPC) og forskerbrochuren (IB) for fuldstændig sikkerhedsinformation, da ingen mærket sikkerhedsdata var tilgængelige i dette Evidence Pack.

Baseret på lægemidlets farmakologiske klasse opregnes følgende potentielle bekymringer til kendskab:

- **Prokoagulant risiko hos diabetiske patienter**: Concizumab øger trombin-generering. Diabetiske patienter har en iboende forhøjet trombose- og hyperkoagulabel tilstand; administration af et anti-TFPI-antistof i denne befolkning kan øge risikoen for mikrovaskulære trombotiske hændelser, herunder retinal venetrombose.
- **Blødnings-/trombosebalance**: Som et middel, der skifter hemostase mod koagulation, kræver enhver brug uden for dets tilsigtede hæmofili-indikation nøje hæmatologisk risikoevaluering.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
TxGNN-forudsigelsesscore er høj, men mekanistisk analyse indikerer ingen plausibel biologisk forbindelse mellem TFPI-inhibition og katarakt-dannelse; forudsigelsen er sandsynligvis en graf-strukturel falsk positiv, der opstår fra delte diabetes-komorbitidets-knuder i vidensgrafen. Desuden rejser Concizumabs prokoagulante mekanisme specifikke sikkerhedsproblemer i målpopulationen af diabetiske patienter, og der er fuldstændig mangel på understøttende kliniske eller prækliniske bevis (L5).

**For at fortsætte ville følgende være nødvendigt:**

- **Biologisk plausibilitets-undersøgelse**: Identifikation af hypoteser eller prækliniske data i peer-reviewed litteratur, der forbinder TFPI eller koagulationsvejs-komponenter med linse-oxidativt stress eller krystallin-ophobning — ingen findes i øjeblikket.
- **MOA-data-hentning**: Fuldstændige DrugBank og publicerede farmakologi-data for concizumab for at bekræfte eller udelukke eventuelt off-target okkulære mekanismer.
- **Sikkerhedsevaluering i diabetisk befolkning**: Dedikeret koagulationsrisiko-modellering før yderligere evaluering hos patienter med diabetes mellitus.
- **Præcisering af regulatorisk status**: Bekræft nuværende klinisk udviklingsfase og om nogen EMA-markedsføringstilladelsesansøgning er planlagt, for at vurdere den realistiske vej til et dansk omformål-forsøg.
- **Genevaluering af TxGNN-output**: I betragtning af, at rangering 1–10 helt optages af katarakt-undertyper med næsten identiske score (0,9816–0,9827), bør denne klynge formelt gennemgås som en potentiel systematisk modelartefakt, før den fremsættes som et omformål-signal.

> **Ansvarsfraskrivelse:** Denne rapport er til brug som forskningsreference og udgør ikke medicinsk rådgivning. Kandidater til medicin-omformål kræver klinisk validering før nogen terapeutisk anvendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

