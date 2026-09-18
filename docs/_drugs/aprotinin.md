---
layout: default
title: Aprotinin
parent: Kun modelforudsigelse (L5)
nav_order: 44
evidence_level: L5
indication_count: 0
---

# Aprotinin
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

# Aprotinin: Ingen genanvendelsesprognoser tilgængelige til vurdering

---

## Enlinjesammenfatning

Aprotinin er en serinproteaseinhibitor (Kunitz-type, bovin-afledt), som historisk set er blevet brugt som et antifibrinolytisk middel til at reducere perioperativt blodtab i hjertechirurgi.
Den nuværende bevispaket indeholder **ingen TxGNN-genanvendelsesprognoser** for denne forbindelse, og aprotinin har ingen markedsapproveringer i Danmark.
Uden prognosedata, kliniske forsøgsbevis eller litteraturbevis i pakken kan en standardvurdering af genanvendelse ikke gennemføres på dette tidspunkt.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Antifibrinolytisk; reduktion af perioperativt blodtab i hjertechirurgi (ikke registreret i Danmark) |
| Forventet ny indikation | Ingen genereret |
| TxGNN-prognosescore | Ikke tilgængelig |
| Bevisniveau | L5 — modelprognoseledningen producerede ingen output |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsapproveringer | 0 |
| Anbefalet beslutning | **Udsæt** |

---

## Hvorfor blev der ikke genereret prognoser

Aprotinin (DrugBank DB06692) er en 58-amino-syre serinproteaseinhibitor afledt af bovint lungevæv. Den hæmmer trypsin, plasmin og plasma kallikrein, og reducerer dermed den fibrinolytiske kaskade og kontaktfaseaktivering, der bidrager til koagulationsforstyrrelser under cardiopulmonary bypass-kirurgi. Markedsført under mærkenavnet Trasylol var det engang det mest brugte antifibrinolytikum i høj-risiko hjerteprocedurer.

Aprotinin blev frivilligt suspenderet fra de fleste markeder i 2007–2008, efter at det canadiske BART-forsøg (Blood conservation using Antifibrinolytics in a Randomized Trial) viste betydeligt højere 30-dages dødelighed sammenlignet med lysin-analogerne tranexaminsyre og aminokapronsyre. Det Europæiske Lægemiddelagentur genoprettede efterfølgende en begrænset godkendelse i 2012, begrænsende brugen til voksne patienter, der undergår isoleret koronar arterieomgåelse (CABG)-kirurgi, når andre antifibrinolytika ikke er egnede, under tæt hæmodynamisk overvågning.

Fraværet af TxGNN-prognoser i denne bevispaket afspejler højst sandsynligt en af følgende:

1. **Vidensgrafs mangel** — Aprotinin er muligvis ikke repræsenteret som en knude i TxGNN-lægemiddel-sygdoms-grafen, eller dets DrugBank-ID blev ikke matchet med en grafenhed.
2. **Under-tærskel-scorer** — Alle kandidatsygdomme-scorer faldt under modellens rapporteringstærskel.
3. **Opstrøms datamangel** — Manglende data om virkningsmekanisme (flagget som datamangel DG002) kan have forværret graf-indlejringskvaliteten, hvilket undertrykkede prognoseoutput.

Forespørgselsloggen bekræfter, at en DrugBank-forespørgsel returnerede et vellykket resultat (`result_status: success`, `result_count: 1`), hvilket indikerer, at forbindelsen blev identificeret, men ingen prognoser blev propageret nedstrøms.

---

## Markedsinformation for Danmark

Aprotinin har i øjeblikket ingen markedsapproveringer i Danmark og er klassificeret som ikke markedsført. Historisk set modtog Trasylol centraliseret EMA-godkendelse, som blev suspenderet i 2007 og delvist genoprettet i 2012 under en begrænset indikation for isoleret CABG-kirurgi. Enhver klinisk brug i Danmark i dag ville kræve en navngivet-patient eller humanitær godkendelse fra Lægemiddelstyrelsen, begrænset af nytte-risiko-dokumentation og institutionel godkendelse.

---

## Sikkerhedshensyn

Ingen struktureret sikkerhedsdata (advarsler, kontraindikationer eller lægemiddelinteraktioner) er tilgængelige i denne bevispaket. Baseret på offentliggjort EMA- og FDA-dokumentation bør klinikere være opmærksomme på følgende vigtige bekymringer før enhver brug:

- **Risiko for øget dødelighed**: Øget 30-dages samlet dødelighed versus lysin-analoger, etableret i BART-forsøget.
- **Alvorlig organskade**: Forøget risiko for akut nyresvigt, myokardieinfarkt og apopleksi hos hjertechirurgi-patienter.
- **Overfølsomhed / anafylaksi**: Risiko øges betydeligt ved geneksponering (tidligere aprotinin-brug inden for 12 måneder er en dokumenteret risikofaktor); en 10.000 KIU-testdosis og præmedicineringsprotokol er påkrævet.
- **Interval for geneksponering**: Et minimumsinterval på 12 måneder mellem eksponeringer anbefales pr. SmPC.

Se venligst det godkendte produktresumeé (SmPC) for Trasylol og EMA-produktinformationen for fuldstændig og aktuel sikkerhedsvejledning.

---

## Konklusion og næste trin

**Beslutning: Udsæt**

**Begrundelse:**
TxGNN-ledningen producerede ingen genanvendelsesprognoser for aprotinin, lægemidlet er ikke godkendt i Danmark, og kritiske inputdata (virkningsmekanisme, godkendte indikationer, sikkerhedsprofil) er fraværende i bevisepakken. Der er ingen kandidatindikation at vurdere på dette tidspunkt.

**For at fortsætte er følgende nødvendigt:**

- **Løs prognosegabet**: Verificer, om aprotinin (DB06692) findes som en knude i TxGNN vidensgrafen; hvis fraværende, anmod grafinklusion før du kører ledningen igen.
- **Hent data om virkningsmekanisme**: Spørg DrugBank-API'et for DB06692 for at få fuld farmakologidata (Datamangel DG002 — alvorlighed: Høj).
- **Hent sikkerhedsprofil**: Download Trasylol SmPC fra EMA-produktdatabasen og analysér advarsler og kontraindikationer (Datamangel DG001 — alvorlighed: Blokerende).
- **Afklár EU-regulatorisk status**: Bekræft nuværende godkendelsestatus for Trasylol hos Lægemiddelstyrelsen eller via EMA-produktdatabasen, givet den komplekse suspensions- og genopretselseshistorie.
- **Kør prognosepipeline igen**: Når grafmedlemskab og data om virkningsmekanisme er bekræftet, kør prognosepipeline igen og generer en ny bevispaket.
- **Hvis prognoser genereres**: Fortsæt til bevisindsamling (ClinicalTrials.gov, PubMed) for den højest-rangerede indikation og genudsted denne rapport på et højere bevisniveau.

---

> **Ansvarsfraskrivelse**: Denne rapport er genereret til referenceformål for forskning og udgør ikke medicinske råd. Alle lægemiddelgenanvendelses-kandidater kræver klinisk validering før brug. Dette dokument erstatter ikke det godkendte produktresumeé eller klinisk vurdering.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

