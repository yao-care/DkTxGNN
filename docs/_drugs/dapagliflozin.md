---
layout: default
title: Dapagliflozin
parent: Kun modelforudsigelse (L5)
nav_order: 127
evidence_level: L5
indication_count: 0
---

# Dapagliflozin
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

# Dapagliflozin: Vurdering af kandidat til omformål — Bevissamling ufuldstændig

## Ét-linjers sammenfatning

Dapagliflozin (Forxiga®) er en selektiv SGLT2-inhibitor med godkendte indikationer for Type 2-diabetes mellitus, hjertesvigt og kronisk nyrésygdom på tværs af EU, herunder Danmark. TxGNN-modellen har **ikke genereret nogen forudsigelser om omformål** for dette lægemiddel i den aktuelle bevissamling, da listen over forudsagte indikationer er tom. En **Udsæt**-beslutning er påkrævet, indtil pipelinen køres på ny med fuldstændige inputdata.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Type 2-diabetes mellitus; hjertesvigt; kronisk nyrésygdom *(hentet fra generel viden — ikke til stede i bevissamlingen)* |
| Forudsagt ny indikation | Ikke tilgængelig — TxGNN-forudsigelse blev ikke udført |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Evidensniveau | L5 — Ingen forudsigelse eller understøttende undersøgelser hentet |
| Markedsstatus i Danmark | Data ikke hentet *(se note nedenfor)* |
| Antal markedsføringstilladelser | 0 *(dataindsamling mislykkedes — se note nedenfor)* |
| Anbefalet beslutning | **Udsæt** |

> **⚠️ Bemærkning om markedsdata for Danmark:** Bevissamlingen rapporterer nul markedsføringstilladelser og "ikke markedsført"-status. Dette afspejler næsten sikkert en **fejl ved dataindsamling**, ikke faktisk fraværelse fra markedet. Dapagliflozin er centralt godkendt i EU under **Forxiga® (EU/1/12/795)** af AstraZeneca, med fuld gyldighed i Danmark. Pipelinen for regulatoriske data bør køres på ny mod EMA-produktdatabasen og Lægemiddelstyrelsens register.

---

## Hvorfor er denne forudsigelse rimelig?

Der er ikke genereret nogen TxGNN-forudsigelse om omformål for dapagliflozin i denne bevissamling, så den standardmæssige mekanistiske begrundelse for en specifik ny indikation kan ikke gives.

Fra etableret farmakologisk viden: Dapagliflozin inhiberer selektivt **natrium-glukose-cotransporter 2 (SGLT2)** i nyrernes proksimale tubuli, blokerer cirka 90% af filtreret glukosereabsorption og driver urinal glukoseudskillelse. Ud over glykæmisk kontrol reducerer SGLT2-inhibering tubuloglomerulær feedback, sænker intraglomerulært tryk og reducerer natrium-reabsorption i proksimal tubuli — mekanismer, der betyder nyrybeskyttelse uafhængigt af blodglukose. Den resulterende natriurese og plasmavolumen-kontraktion reducerer kardial forbelastning og efterbelastning, hvilket forklarer lægemidlets kardiovaskulære fordele ved hjertesvigt.

Disse pleiotrope virkninger — metaboliske, hæmodynamiske, antiinflammatoriske og antifibrotiske — gør dapagliflozin til en mekanistisk rig kandidat til omformålsforskning. Aktuelle undersøgelsesområder omfatter non-alkoholisk fedtlever (NASH/MAFLD), polycystisk ovariesyndom (PCOS), hyperurikæmi og søvnrelateret vejrtrækningsproblemer. Men **ingen TxGNN-modeloutput er tilgængeligt i denne bevissamling** til at understøtte en struktureret omformålsanalyse, og ingen indikationsspecifikke evidenstabeller kan præsenteres.

---

## Klinisk prøveevidence

Der er ingen TxGNN-forudsagt indikation til stede i denne bevissamling. Indikationsspecifik klinisk prøveindsamling blev ikke udført.

> Der er i øjeblikket ikke knyttet relevant klinisk prøveevidence til et omformålsmål for denne kandidat.

---

## Litteraturevidence

Der er ingen TxGNN-forudsagt indikation til stede i denne bevissamling. Indikationsspecifik litteraturindsamling blev ikke udført.

> Der er i øjeblikket ikke knyttet relevant litteratur til et omformålsmål for denne kandidat.

---

## Markedsinformation for Danmark

Der blev ikke hentet markedsføringstilladelelsesdata for Danmark i denne bevissamling.

**Kendt regulatorisk kontekst (fra generel viden):** Dapagliflozin markedsføres i Danmark som **Forxiga®** under EMA-centraliseret godkendelse **EU/1/12/795** (AstraZeneca). SmPC og EPAR er offentligt tilgængelige via EMA-webstedet. Datapipelinen bør genindsamle denne godkendelse og eventuelle nationale registre fra Lægemiddelstyrelsen.

---

## Sikkerhedshensyn

Der blev ikke hentet sikkerhedsdata i denne bevissamling — vigtige advarsler og kontraindikationer blev ikke udfyldt, og der blev ikke fundet lægemiddel-lægemiddel-interaktionsregistre.

> Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation. Forxiga SmPC (EU/1/12/795) er tilgængelig på [https://www.ema.europa.eu](https://www.ema.europa.eu).

---

## Konklusion og næste trin

**Beslutning: Udsæt**

**Begrundelse:**
Denne bevissamling er kritisk ufuldstændig — TxGNN-modellen producerede ingen forudsigelser om omformål, regulatoriske data for Danmark blev ikke hentet, og alle sikkerhedsfelter er tomme. Ingen meningsfuld klinisk vurdering kan foretages på dette grundlag.

**For at fortsætte er følgende nødvendigt:**

- **Kør TxGNN-forudsigelse på ny** for dapagliflozin (DB06292) for at generere `predicted_indications` med kandidatsygdomme, scores, kliniske prøver og litteratur
- **Genindsaml EMA/danske regulatoriske data**: hent Forxiga® EU/1/12/795-godkendelsesdetaljer, godkendte indikationer og aktuel markedsstatus fra Lægemiddelstyrelsen
- **Hent fuldstændige SmPC-sikkerhedsdata**: vigtige advarsler, kontraindikationer, særlige populationer (nyreinsufficiens, graviditet, ældre) og lægemiddel-interaktionsprofil — især med diuretika, insulin og andre antidiabetiske stoffer
- **Indhent DrugBank MOA-data** for DB06292 for at udfylde mekanisme-for-virkning-feltet
- **Kør pipelinen for den fulde bevissamling på ny** (v5 eller senere) med alle datakilder bekræftet som aktive input, ikke kun `drugbank`
- Når en gyldig forudsagt indikation er identificeret, bestil en struktureret klinisk og regulatorisk gennemførlighedsreview med dansk hospitalsfarmaci og endokrinologi-input

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

