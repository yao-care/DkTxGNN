---
layout: default
title: Elotuzumab
parent: Kun modelforudsigelse (L5)
nav_order: 160
evidence_level: L5
indication_count: 0
---

# Elotuzumab
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

# Elotuzumab: Multipelt myelomatose — TxGNN-prognoser ikke tilgængelige

## Ét-sætnings-opsummering

Elotuzumab (Empliciti) er en SLAMF7-målrettet immunoterapeutisk monoklonal antistof godkendt til behandling af recidiveret eller refraktær multipelt myelomatose i kombination med lenalidomid eller pomalidomid plus dexamethason.
Den aktuelle bevismappe (v4, kandidat `TW-DB06317-multi`) indeholder **ingen TxGNN-forudsagte nye indikationer** for dette lægemiddel, og to kritiske datahull — detaljer om virkningsmekanisme og regulatoriske sikkerhedsdata — forbliver uløst.
En genbrug-vurdering **kan ikke fuldføres** med de oplysninger, der for øjeblikket er tilgængelige; den anbefalede handling er at afvente datarettelse.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Original indikation | Multipelt myelomatose (recidiveret/refraktær) — i kombination med lenalidomid + dexamethason eller pomalidomid + dexamethason |
| Forudsagt ny indikation | Ikke tilgængelig — ingen TxGNN-prognoser i aktuel bevismappe |
| TxGNN-prognosescore | Ikke tilgængelig |
| Bevisniveau | Kan ikke bestemmes — ingen prognoseoutput genereret |
| Markant status i Danmark | Ikke registreret i spurgt nationalt register |
| Antal markedsføringstilladelser | 0 (spurgt nationalt register); EMA centraliseret godkendelse eksisterer separat |
| Anbefalet beslutning | **Afvente** |

---

## Hvorfor er denne prognose rimelig?

*Dette afsnit giver normalt mekanistisk begrundelse for en TxGNN-forudsagt ny indikation. Fordi der ikke er tilgængelige prognoser i denne bevismappe, dokumenterer det i stedet den nuværende viden om lægemidlet til støtte for fremtidig analyse.*

Elotuzumab er et humaniseret IgG1 monoklonalt antistof, der målretter **SLAMF7** (Signaling Lymphocytic Activation Molecule Family member 7, også kendt som CS1/CRACC/CD319) — et glykoprotein stærkt udtrykt på multipelt myelomatose-celler og natural killer (NK)-celler. Dets doble virkningsmekanisme kombinerer direkte antistofafhængig cellulær cytotoxicitet (ADCC) gennem NK-celleaktivering med direkte opsonisering af ondartede plasmaceller, hvilket etablerer det som en klinisk valideret immunoterapi inden for multipelt myelomatose.

DrugBank-forespørgslen for DB06317 returnerede et succesfuldt resultat, hvilket bekræfter, at lægemiddelregistreringen eksisterer. Detaljerede data om virkningsmekanisme blev imidlertid flagget som et **datahull med høj alvor** (DG002), hvilket betyder at de strukturerede MOA-felter, der kræves til mekanistisk plausibilitetsvurdering, ikke blev udfyldt. Separat blev forespørgslen om regulatoriske sikkerhedsdata — der dækker kontraindikationer og pakningsindsatsvarsler — flagget som et **blokerende datahull** (DG001), hvilket forhindrede standard sikkerhedsforhåndskontrol i at blive fuldført.

Uden TxGNN-prognoseoutput kan en formel genbrug-hypotese ikke evalueres på dette stadium. Fra et biologisk synspunkt er SLAMF7-ekspression blevet rapporteret i visse andre hæmatologiske ondartede sygdomme ud over myelomatose (herunder nogle NK/T-celle-lymfomer og Waldenströms macroglobulinæmi), hvilket foreslår at genbrug-potentiale kan eksistere. Realisering af dette potentiale kræver dog, at modellen producerer rangordnede prognoser og konfidensscorer, før en struktureret vurdering kan fortsætte.

---

## Markedsoplysninger for Danmark

Der blev ikke fundet nationale markedsføringstilladelser i det spurgt regulatoriske register (0 poster; markant status: ikke registreret).

> **Vigtig note for danske ordinatorer:** Elotuzumab er godkendt i Den Europæiske Union under **EMA centraliseret procedure** som **Empliciti** (Bristol-Myers Squibb / AbbVie), godkendt siden 2016. Denne centraliserede godkendelse gælder i alle EU/EØS-medlemsstater, herunder Danmark. Manglen på poster i lokalt spurgt register afspejler datarørledningens dækning, ikke manglende juridisk godkendelse. EMA SmPC for Empliciti er det autoritative sikkerhedsreferencedokument.

---

## Cytotoxicitet

Elotuzumab bruges udelukkende til behandling af multipelt myelomatose, en hæmatologisk ondartedhed. Cytotoxicitets-afsnittet gælder.

| Emne | Indhold |
|------|---------|
| Cytotoxicitetsklassificering | Målrettet immunoterapi — SLAMF7-rettet humaniseret IgG1 monoklonalt antistof |
| Myelosuppression-risiko | Lav for elotuzumab som enkeltbehandling; **Moderat til høj** i standardkombinationsregimer (lenalidomid + dexamethason eller pomalidomid + dexamethason) på grund af partnerlægemidlerne |
| Emetogenicitetsklassificering | Lav |
| Overvågningspunkter | CBC med differentiering (for at overvåge lenalidomid/pomalidomid-associeret neutropeni og trombocytopeni), leverfunktionstests, overvågning af infusionsrelaterede reaktioner (feber, kulderystelser, hypertension — mest almindelig under første infusion), lymfocyttal |
| Håndteringsbeskyttelse | Elotuzumab selv kræver ikke cytotoksisk håndteringsbeskyttelse; kombinationspartnere **lenalidomid og pomalidomid** er teratogene IMiDs underlagt strenge Pregnancy Prevention Programmes (PPP) — ordinatorer skal overholde REVLIMID/IMNOVID REMS-tilsvarende EU-risikostyringsomfattelser |

---

## Sikkerhedshensyn

Begge sikkerhedsdatafelter (nøgleadvarsler og kontraindikationer) er flagget som uløste datahull i den aktuelle bevismappe, og der blev ikke returneret lægemiddel-lægemiddel-interaktionsregister fra DDI-forespørgslen.

> Se venligst den godkendte Summary of Product Characteristics (SmPC) for **Empliciti** (tilgængelig via EMA-produktsiden) for fuldstændig sikkerhedsinformation, herunder styring af infusionsreaktioner, infektionsrisiko, sekundær malignitet-overvågning og embryo-foetale toksicitets-vejledning specifik for kombinationsregimer.

---

## Konklusion og næste trin

**Beslutning: Afvente**

**Begrundelse:**
Bevismappe for Elotuzumab (DB06317) er for øjeblikket ufuldstændig inden for to kritiske områder: der blev ikke genereret TxGNN-prognoseoutput, og både detaljer om virkningsmekanisme og regulatoriske sikkerhedsdata mangler. Uden en forudsagt indikation at evaluere og uden en sikkerhedsforhåndskontrol kan en genbrug-vurdering ikke møde det mindste evidensniveau, der kræves for at gå videre.

**For at fortsætte kræves følgende:**

- **TxGNN-prognoseoutput (Kritisk):** Kør TxGNN-modellen igen for DrugBank ID DB06317 for at generere rangordnede forudsagte indikationer med konfidensscorer. Verificer om `multi`-suffikset i kandidat-ID'et (`TW-DB06317-multi`) indikerer et kendt pipelineprocesseringsproblem.
- **Virkningsmekanisme-data (Høj prioritet — DG002):** Hent strukturerede MOA fra DrugBank API for DB06317, herunder farmakologisk virkning, mål-proteiner og sti-associationer.
- **Regulatoriske sikkerhedsdata (Blokering — DG001):** Download og parse EMA SmPC for Empliciti for at udfylde advarsler, kontraindikationer og vejledning for særlige populationer (nyresygdom/leversygdom, graviditet).
- **EMA-godkendelse krydsreference:** Kortlæg EMA centraliseret markedsføringstilladelsesnummeret for Empliciti til Danmark markedsoplysningssektionen for at give et præcist regulatorisk landskab for danske ordinatorer.
- **DDI-datasupplement:** Hent lægemiddel-lægemiddel-interaktionsdata for elotuzumab i sammenhæng med dets standard kombinationspartnere (lenalidomid, pomalidomid, dexamethason, bortezomib) fra en valideret DDI-ressource (f.eks. DrugBank-interaktioner, SFINX eller Lexi-Interact).

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

