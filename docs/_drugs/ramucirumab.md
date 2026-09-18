---
layout: default
title: Ramucirumab
parent: Kun modelforudsigelse (L5)
nav_order: 365
evidence_level: L5
indication_count: 10
---

# Ramucirumab
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

# Ramucirumab: Fra avancerede solide tumorer til adenokarcinom af livmoderligamenter

## Sammenfatning i én sætning

Ramucirumab er et anti-VEGFR2 monoklonalt antistof, hvis antitumøreffekt gennem blokering af tumorangiogenese er etableret ved mavekræft, NSCLC, hepatocellulært karcinom og kolorektal kræft (ifølge det mekanistiske rationale i denne bevissamling; ikke uafhængigt bekræftet via strukturerede indikationsdata i denne samling). TxGNN-modellen forudsiger, at det kan være effektivt ved **adenokarcinom af livmoderligamenter**, men i øjeblikket støtter **0 kliniske forsøg** og **0 publikationer** denne specifikke retning – dette er et signal fra modelforudsigelse alene.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|--------|
| Oprindelig indikation | Ikke bekræftet i denne bevissamling (struktureret felt er tomt); mekanistisk rationale henviser til etableret brug ved mavekræft, NSCLC, hepatocellulært karcinom og kolorektal kræft |
| Forudsagt ny indikation | Adenokarcinom af livmoderligamenter |
| TxGNN-forudsigelsesscore | 99.95% |
| Bevisniveau | L5 |
| Markeds status i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Feltet `original_moa` for Ramucirumab er ikke udfyldt i denne bevissamling (markeret som et datakløft med høj alvorlighed, DG002 – afventer DrugBank API-opslag). Den tilknyttede omformålsrationale til den øverste forudsigelse beskriver dog Ramucirumab som et anti-VEGFR2 monoklonalt antistof, der hæmmer tumorangiogenese, en mekanisme der allerede er valideret på tværs af flere solide tumorer, herunder mavekræft, NSCLC, hepatocellulært karcinom og kolorektal kræft.

Adenokarcinom af livmoderligamenter er en sjælden gynækologisk malignitet. Det mekanistiske link, der foreslås her, er en bred ekstrapolation fra anti-angiogenetisk aktivitet i andre solide tumorer snarere end et sygdomsspecifikt fund – bevissamlingen noterer eksplicit, at der ikke er direkte data om VEGFR2-ekspression eller angiogenese-afhængighed i denne specifikke tumortype, så forbindelsen "kan ikke etableres som et specifikt link" ud over generel klasse-niveau-plausibilitet.

Da der ikke er nogen kliniske forsøg eller publikationer, der tester Ramucirumab i denne indikation, står det mekanistiske argument i øjeblikket alene som hele bevisgrundlaget for forudsigelsen.

---

## Klinisk forsøgsbevis

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Ramucirumab har i øjeblikket **ingen markedsføringstilladelser registreret** i denne bevissamling (`total_licenses: 0`, `market_status: Not marketed` / Ikke markedsført). Der kan ikke produceres en licenstabel.

---

## Cytotoksicitet

Ramucirumab er et antineoplastisk monoklonalt antistof (anti-VEGFR2, anti-angiogenetisk klasse), så dette afsnit gælder.

| Punkt | Indhold |
|------|--------|
| Cytotoksicitetsklassificering | Målrettet terapi (anti-VEGFR2 monoklonalt antistof, anti-angiogenetisk) |
| Risiko for myelosuppression | Se venligst Produktinformationen (SmPC) for advarsler og forholdsregler |
| Emetogenicitetsklassificering | Se venligst Produktinformationen (SmPC) for advarsler og forholdsregler |
| Overvågningspunkter | Se venligst Produktinformationen (SmPC) for advarsler og forholdsregler |
| Sikkerhed ved håndtering | Se venligst Produktinformationen (SmPC) for advarsler og forholdsregler |

---

## Sikkerhedsovervejelser

Se venligst den godkendte Produktinformation (SmPC) for sikkerhedsoplysninger. Bemærk: bevissamlingen markerer et datakløft med **Blocking**-alvorlighed (DG001) – TFDA/SmPC-niveau advarsler og kontraindikationer er ikke endnu tilgængelige, hvilket i sig selv forhindrer denne kandidat i at gå ind i S1-sikkerhedsforvurderingsfasen.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Rationale:**
- Bevisniveauet er L5 (kun modelforudsigelse) – der er nul kliniske forsøg og nul publikationer, der understøtter Ramucirumab ved adenokarcinom af livmoderligamenter, og det mekanistiske link er en generisk klasse-niveau-ekstrapolation snarere end et sygdomsspecifikt fund. Kombineret med et datakløft med høj sikkerhedsalvorlighed kan kandidaten på nuværende tidspunkt ikke gå videre.

**Følgende er nødvendigt for at kunne fortsætte:**
- TFDA/SmPC-baserede advarsler og kontraindikationer (DG001, Blocking) – påkrævet før enhver S1-sikkerhedsforvurdering
- Bekræftet virkningsmekanisme fra DrugBank (DG002)
- Sygdomsspecifikt understøttende bevis (præklinisk, kasuistikker eller forsøg) for VEGFR2/angiogenese-relevans ved adenokarcinom af livmoderligamenter specifikt, givet dets sjældenhed og mangel på registrerede forsøg
- Afklaring af Ramucirumabs bekræftede oprindelige indikation(er), da det strukturerede `original_indications`-felt i denne samling i øjeblikket er tomt

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

