---
layout: default
title: Damoctocog Alfa Pegol
parent: Kun modelforudsigelse (L5)
nav_order: 126
evidence_level: L5
indication_count: 0
---

# Damoctocog Alfa Pegol
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

# Damoctocog alfa pegol: Evaluering afventende — Ingen TxGNN-repurposingforudsigelser tilgængelige

## Sammenfatning

Damoctocog alfa pegol (DrugBank ID: DB14700) er et PEGyleret rekombinant koagulationsfaktor VIII-biologisk produkt, der i øjeblikket ikke markedsføres i Danmark.
TxGNN-pipelinen returnerede **ingen repurposingkandidater** for dette lægemiddel, og kritiske datapunkter — herunder virkningsmekanisme og sikkerhedsprofil — mangler i det aktuelle bevisudvalg.
En fuldstændig evaluering af lægemiddelrepurposing kan ikke gennemføres, før disse huller bliver udfyldt.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke registreret i bevisudvalget |
| Forudsagt ny indikation | Ingen — TxGNN returnerede ingen kandidater |
| TxGNN-forudsigelsesscore | N/A |
| Evidensniveau | L5 (ingen forudsigelser genereret; evaluering ikke mulig) |
| Markedsstatus for Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Ventetilstand |

---

## Hvorfor blev der ikke genereret forudsigelser?

Forespørgselsjournalen bekræfter, at DrugBank-opslaget var vellykket (DB14700, 1 resultat), hvilket betyder, at lægemidlets identitet blev løst. Men forudsigelsespipelinen returnerede en tom kandidatliste. Dette sker typisk af en af tre grunde:

1. **Knowledge graph-dækningsgab**: TxGNN-vidensgrafen kan ikke indeholde tilstrækkelige forbindelser (kanter), der forbinder damoctocog alfa pegol til sygdomsknuder, fordi det er et stormolekyle-biologisk produkt (PEGyleret rekombinant FVIII) snarere end et småmolekyle-lægemiddel. TxGNNs træningsdata er vægtet mod småmolekyler.

2. **Manglende indikationsfrø**: Feltet `original_indications` er tomt, hvilket betyder, at pipelinen ikke havde nogen godkendt indikationsanker, hvorfra mekanistiske lighedsscore kunne beregnes på tværs af sygdomsrummet.

3. **MOA-data fraværende**: Uden en dokumenteret virkningsmekanisme i bevisudvalget kan modellen ikke udnytte mekanisme-baserede funktionsvektorer til at rangere kandidatindikationer.

Indtil den oprindelige indikation og MOA er udfyldt, kan ingen meningsfuld repurposing-signal ekstraheres fra TxGNN for dette lægemiddel.

---

## Markedsinformation for Danmark

Damoctocog alfa pegol har **ingen markedsføringstilladelser** i Danmark, og er registreret som ikke markedsført. Ingen produktposter er tilgængelige fra Lægemiddelstyrelsen eller det centraliserede EMA-register i dette bevisudvalg.

> **Bemærkning til revieweren**: Damoctocog alfa pegol (handelsnavn Jivi®, BAY 94-9027) har en centraliseret EMA-markedsføringstilladelse til profylakse og behandling af blødning hos voksne med hæmofili A (medfødt faktor VIII-mangel). Hvis dette lægemiddel er beregnet til evaluering, bør trinnet til datahentning i bevisudvalget gentages med opslag af EMA-godkendelser, da den nuværende pakke viser nul poster — dette er sandsynligvis et hentelsesgab snarere end en virkelig mangel på tilladelse.

---

## Sikkerhedsmæssige overvejelser

Ingen sikkerhedsdata blev hentet for dette lægemiddel i det aktuelle bevisudvalg. Se venligst den godkendte Summary of Product Characteristics (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Afgørelse: Ventetilstand**

**Begrundelse:**
Bevisudvalget indeholder ingen TxGNN-forudsigelser, ingen oprindelige indikationsregistreringer, ingen virkningsmekanisme og ingen sikkerhedsdata — de minimale input, der kræves for at generere eller evaluere en repurposing-hypotese, mangler alle.

**For at fortsætte er følgende nødvendigt:**

- **Løs blokeringsdatamangler (DG001)**: Hent den fulde SmPC fra EMA-produktsiden (EMEA/H/C/004178) for at udtrække godkendt indikationstekst, vigtige advarsler og kontraindikationer.
- **Løs høj-alvorlighedsgradsdatamangler (DG002)**: Spørg DrugBank om den dokumenterede MOA for DB14700 (rekombinant faktor VIII-mekanisme — erstatning af deficient koagulationsfaktor VIII).
- **Udfyld `original_indications`**: Indsæt den godkendte EMA-indikation (hæmofili A), så TxGNN-pipelinen har en anker-sygdomsknude.
- **Kør TxGNN-forudsigelsespipelinen igen**, når de tre punkter ovenfor er på plads.
- **Bekræft EMA-licenshentning**: Bekræft, at Lægemiddelstyrelsen / EMA-dataforbindelsen korrekt forespørger centraliserede tilladelser, da resultatet på 0-licens virker uoverensstemmende med lægemidlets kendte godkendelsesstatus i Europa.

---

> ⚠️ **Ansvarsfraskrivelse**: Denne rapport er alene bestemt til forskningsmæssige formål og udgør ikke medicinsk rådgivning. Alle lægemiddelrepurposing-kandidater kræver klinisk validering før terapeutisk anvendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

