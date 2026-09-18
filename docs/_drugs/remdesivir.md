---
layout: default
title: Remdesivir
parent: Kun modelforudsigelse (L5)
nav_order: 371
evidence_level: L5
indication_count: 10
---

# Remdesivir
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

# Remdesivir: Fra COVID-19 til multipel endokrin neoplasi

## Sammenfattelse på én linje

Remdesivir er et intravenøst antiviralt middel (RNA-afhængig RNA-polymerase-inhibitor) etableret til behandling af COVID-19, og det markedsføres ikke i øjeblikket i Danmark. TxGNN-modellens topranget forudsigelse er **multipel endokrin neoplasi** (score **99.50%**), men denne kandidat har **nul understøttende kliniske forsøg eller publikationer**, og evidenspakkens egen mekanistiske gennemgang markerer den som en sandsynlig falsk positiv uden biologisk plausibilitet.

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | COVID-19 (ifølge kliniske forsøgsregistreringer i denne evidenspakke, f.eks. NCT04669990: "Remdesivir har for nylig modtaget fuld godkendelse til COVID-19 af US FDA"); ikke uafhængigt bekræftet via danske regulatoriske ansøgninger, da lægemidlet ikke markedsføres i Danmark |
| Forudsagt ny indikation | Multipel endokrin neoplasi |
| TxGNN-forudsigelsesscore | 99.50% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Afvent |

## Hvorfor er denne forudsigelse rimelig?

Detaljerede mekanismedata for virkningsmekanisme er ikke tilgængelige i det strukturerede `drug.original_moa`-felt (markeret som en blokerende/høj-alvorlighed datakløft i denne pakke). Evidenspakkens egen rationale beskriver dog Remdesivir som et nukleotidanalog-prodrug, der retter sig mod RNA-afhængig RNA-polymerase (RdRp), hvilket giver det aktivitet mod (+)ssRNA-virus såsom SARS-CoV-2 og Ebola.

Multipel endokrin neoplasi (MEN) er et arvelig endokrint tumosyndromen drevet af *RET*- eller *MEN1*-genmutationer — en genetisk onkogen vej uden kendt forbindelse til viral RdRp-inhibition. Evidenspakken karakteriserer eksplicit dette par som en "typisk TxGNN falsk-positiv høj-score-kandidat": modelscoren er høj, men der er ingen understøttende biologisk rationale, og søgning på ClinicalTrials.gov, ICTRP og PubMed for dette lægemiddel-sygdomspar returnerede nul resultater på tværs af alle tre kilder.

Det er også værd at bemærke, at den næstranget kandidat i denne pakke, "HIV-infektionssygdom" (score 99.32%), overfladisk set ser bedre understøttet ud — 23 registrerede forsøg og 20 publikationer. Ved gennemgang fremgår det dog, at hvert citeret forsøg og abstrakt vedrører COVID-19/SARS-CoV-2 (f.eks. WHO Solidarity Trial, ACTT-3, ACTIV-3/TICO), ikke HIV. Remdesivirs RdRp-målende mekanisme gælder ikke for HIV, et retrovirus, der er afhængigt af omvendt transkriptase. Dette stærkt antyder en sygdoms-ontologi-kortlægningsfejl i pipelinen snarere end ægte anti-HIV-bevis, og bør heller ikke læses som understøttende denne angivelsesændring.

## Klinisk forsøgsbevis

I øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

## Markedsinformation for Danmark

Ikke markedsført i Danmark — ingen markedsføringstilladelser er registreret (`total_licenses = 0`).

## Sikkerhedshensyn

Se venligst det godkendte produktinformationsdokument (SmPC) for sikkerhedsinformation. Vigtige advarsler, kontraindikationer og data om lægemiddelvekselvirkninger var ikke tilgængelige i denne evidenspakke (DG001, blokering af høj alvorlighed — data skal hentes fra det officielle produktetiket, før denne kandidat kan indgå i sikkerhedsvurderingsstadiet).

## Konklusion og næste trin

**Afgørelse: Afvent**

**Rationale:**
Den topranget forudsagt indikation (Multipel endokrin neoplasi) har ingen understøttende kliniske forsøg eller litteratur og ingen plausibel mekanistisk forbindelse til Remdesivirs antivirale virkningsmekanisme. Det tilsyneladende bedre dokumenteret alternativ (HIV-infektionssygdom) undermineres af en sandsynlig sygdoms-etiket-uoverensstemmelse — alle tilknyttede forsøg og artikler er COVID-19-studier, ikke HIV-studier.

**For at fortsætte, skal følgende være opfyldt:**
- Ret sygdoms-ontologi-kortlægningen for kandidaten "HIV-infektionssygdom" (bevis ser ud til at være COVID-19-data mislabelt)
- Løs DG001 (Blokering): indhent TFDA/dansk produktinformation-advarsler, kontraindikationer og DDI-data før nogen S1-sikkerhedsvurdering
- Løs DG002 (Høj): indhent bekræftet oprindelig MOA fra DrugBank API
- Verificer Danmark/EU-markedsstatus direkte (EMA centraliseret godkendelse for Veklury findes globalt; denne pakke viser 0 licenser, som skal forenes)
- Fjern dubletter fra den rangerede kandidatliste — ranger 1–2, 3–4, 5–6, 7–8 og 9–10 er hver identiske gentagne poster — før nogen omvurdering eller prioritering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

