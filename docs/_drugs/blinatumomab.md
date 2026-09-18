---
layout: default
title: Blinatumomab
parent: Kun modelforudsigelse (L5)
nav_order: 70
evidence_level: L5
indication_count: 0
---

# Blinatumomab
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

# Blinatumomab: Foreløbig Vurdering — TxGNN-Forudsigelsesdata Ikke Tilgængelige

## Sammenfatning i Én Sætning

Blinatumomab (Blincyto) er et første-i-klasse bispecifikt T-celle-engager (BiTE) antistof godkendt til recidiverende eller refraktær B-celle-forløber akut lymfoblastisk leukæmi (ALL), som virker ved at omdirigere patientens egne T-celler til at ødelægge CD19-udtrykkende kræftceller. Der er i øjeblikket ingen TxGNN-lægemiddelgenbrugelsesforudsigelser tilgængelige for denne kandidat — feltet `predicted_indications` i Evidence Pack er tomt — hvilket betyder, at en fuld genbrugsvurdering ikke kan gennemføres på dette stadium. Denne rapport dokumenterer den aktuelle datastatus, påpeger kritiske huller og anbefaler **Hold** i afventning af genudførelse af forudsigelsespipelinen.

---

## Hurtigt Overblik

| Emne | Indhold |
|------|---------|
| Original-indikation | Recidiverende/refraktær B-celle-forløber akut lymfoblastisk leukæmi (ALL) |
| Forudsagt Ny Indikation | Ikke tilgængelig — TxGNN-forudsigelse afventer |
| TxGNN-Forudsigelsesscore | Ikke tilgængelig |
| Evidensgrad | Ikke bestemmelig |
| Danmarks Markedsstatus | Ikke registreret (0 godkendelser i datasæt — se bemærkning nedenfor) |
| Antal Markedsføringstilladelser | 0 (ifølge datasæt; sandsynligvis et datahentningshul — se bemærkning) |
| Anbefalet Beslutning | **Hold** |

> **⚠️ Datanote om markedsstatus:** Blinatumomab markedsføres som **Blincyto** under EMA centraliseret godkendelse **EU/1/15/1047**, som er gyldig i alle EU/EØS-medlemsstater, herunder Danmark. Nul-licens-resultatet i denne Evidence Pack afspejler sandsynligvis et hul i datahentningspipelinen snarere end fravær fra det danske marked. Manuel verifikation mod Lægemiddelstyrelsen-registeret og EMA EPAR anbefales.

---

## Lægemiddelbaggrund og Kendt Mekanistisk Profil

Selvom der ikke er TxGNN-forudsigelser tilgængelige, gives følgende baggrund for at støtte prioriteringsbeslutninger.

Blinatumomab tilhører klassen bispecifikke T-celle-engagere (BiTE) inden for immunoterapi. Det binder samtidigt **CD19** på B-linje tumorceller og **CD3ε** på cytotoksiske T-celler og danner en kunstig immunologisk synapse, som aktiverer T-celler — uafhængigt af MHC-præsentation — og udløser seriel lysis af CD19+ målceller. Denne mekanisme er strukturelt forskellig fra konventionel kemoterapi og monoklonale antistoffer, hvilket gør den potentielt anvendelig på tværs af en række CD19-udtrykkende hæmatologiske malignitet ud over ALL.

EMA-godkendte indikationer for Blincyto omfatter i øjeblikket:
- Recidiverede eller refraktære (R/R) Philadelphia-kromosom-negative (Ph–) B-celle-forløber ALL hos voksne og pediatriske patienter
- MRD-positiv (minimal rest sygdom) B-celle-forløber ALL hos voksne

Lægemidlets virkningsmekanisme-data blev markeret som **Høj-alvorligt datahul (DG002)** i Evidence Pack. Hentning fra DrugBank API (DB09052) kræves, før mekanistisk rationaleanalyse kan gennemføres formelt.

---

## Cytotoksicitet

Blinatumomab klassificeres som et antineoplastisk middel (immunoterapi). Dette afsnit er inkluderet, da lægemidlet bærer onkologi-indikationsprofilen og specifikke toksicitetsbehandlingskrav, der adskiller sig fra standard systemisk kemoterapi.

| Emne | Indhold |
|------|---------|
| Cytotoksicitetsklassifikation | Målrettet immunoterapi — Bispecifik T-celle-Engager (BiTE-antistof); ikke et konventionelt cytotoksisk middel |
| Myelosuppression-risiko | Moderat til Høj — febril neutropeni, anæmi og trombocytopeni rapporteres almindeligt; tilskrivelig dels til underliggende sygdom og dels til immunaktivering |
| Emetogenicitetsklassifikation | Lav — kvalme kan forekomme men er ikke primært emetogen; standard antiemetisk profylakse ikke rutinemæssigt påkrævet |
| Overvågningspunkter | Fuldt blodtal med differentialtal (hyppigt under cyklus 1–2), leverfunktionsprøver, neurologisk status (dagligt under hospitaliseringsfase), tegn på cytokinudslippelsessyndrom (CRS) og immuneffektorcelle-associeret neurotoksicitetsyndrom (ICANS) |
| Håndteringsbeskyttelse | Administreret som kontinuerlig IV-infusion via bærbar infusionspumpe (op til 4 uger); følger institutionelle biologiske/monoklonale antistof-håndteringsvejledninger — ikke klassificeret som traditionelt farligt cytostatikum, men lokale institutionelle politikker gælder |

---

## Sikkerhedshensyn

Strukturerede sikkerhedsdata (advarsler, kontraindikationer, lægemiddelinteraktioner) blev ikke returneret af datapipelinen for denne Evidence Pack. Se venligst den godkendte Produktresumé (SmPC) for Blincyto, tilgængelig via [EMA-produktsiden for EU/1/15/1047](https://www.ema.europa.eu/en/medicines/human/EPAR/blincyto), med særlig opmærksomhed på:

- **Cytokinudslippelsessyndrom (CRS):** Kræver trinvis dosiseskalering, obligatorisk hospitalisering i de første 9 dage af cyklus 1 og 2, og en dokumenteret CRS-håndteringsprotokal, herunder kortikosteroider og tocilizumab.
- **Neurologisk toksicitet (ICANS/encefalopati):** Kramper, talestyrrelser og nedsat bevidsthed er blevet rapporteret; behandlingsafbrydelseskriterier er defineret i SmPC.
- **Infektionsrisiko:** Opportunistiske infektioner, herunder PML (progressiv multifokale leukoencefalopati), er blevet rapporteret.
- **Tumorlysissyndrom:** Før-behandlingshydrering og urinsyre-håndtering anbefales.
- **Tilberedning og administration:** Kræver specifik IV-posepræparation med stabilisatoropløsning; fejl i præparation medfører alvorlig risiko.

---

## Konklusion og Næste Trin

**Beslutning: Hold**

**Begrundelse:**
Evidence Pack indeholder ingen TxGNN-forudsagte indikationer for blinatumomab, hvilket gør det umuligt at gennemføre en genbrugsvurdering. Uden en målindikation kan hverken klinisk evidenshentning eller en nytterisiko-vurdering gennemføres på meningsfuld vis.

**For at fortsætte er følgende nødvendigt:**

- **[Kritisk]** Genudførelse af TxGNN-forudsigelsespipelinen for `DB09052` (blinatumomab) og udfyldning af `predicted_indications` — dette er en blokerende forudsætning for enhver genbrugsvurdering.
- **[Høj]** Hentning af virkningsmekanisme og farmakologidata fra DrugBank API for `DB09052` for at muliggøre mekanistisk rationaleanalyse.
- **[Blokering]** Hentning af det danske SmPC / sikkerhedsdata: advarsler, kontraindikationer og lægemiddelinteraktionsprofil.
- **[Anbefalet]** Manuel verifikation af dansk markedsføringstilladelsestatus mod Lægemiddelstyrelse-registeret og krydshenvisning med EMA EPAR for Blincyto (EU/1/15/1047) for at korrigere det tilsyneladende datahentningshul, der viser 0 licenser.
- Når en komplet Evidence Pack (v5+) er tilgængelig med udfyldt `predicted_indications`, skal denne rapport genudstedes efter standardevalueringsrammen.

---

> *Denne rapport genereres til forskningsformål alene og udgør ikke medicinsk rådgivning. Alle lægemiddelgenbrugelseskandidater kræver klinisk validering før eventuel terapeutisk anvendelse. Denne side inkluderer en YMYL-ansvarsfraskrivelse: information præsenteret her er foreløbig og må ikke bruges til at informere kliniske beslutningsprocesser.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

