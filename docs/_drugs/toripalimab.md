---
layout: default
title: Toripalimab
parent: Kun modelforudsigelse (L5)
nav_order: 442
evidence_level: L5
indication_count: 10
---

# Toripalimab
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

# Toripalimab: Fra onkologi (PD-1-checkpoint-inhibitor) til blandet-type autoimmun hæmolytisk anæmi

## Opsummering på én sætning

Toripalimab er en PD-1-checkpoint-inhibitor; formelle danske licensregistre opfører ingen bekræftet oprindelig indikation, men lægemidlets kendte virkemåde bruges inden for onkologi til at forbedre anti-tumor-T-celle-aktivitet. TxGNN-modellen forudsiger en mulig effekt på **blandet-type autoimmun hæmolytisk anæmi (AIHA)**, men denne forudsigelse understøttes af **nul kliniske forsøg og nul publikationer**, og den medfølgende mekanistiske analyse markerer eksplicit en **biologisk modsigelse** i stedet for en plausibel genbrug-rationalet.

---

## Kort overblik

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Ikke på fil (ingen danske licenser registreret; generelle mekanisme-data indikerer onkologi-brug som en PD-1-checkpoint-inhibitor) |
| Forudsagt ny indikation | Blandet-type autoimmun hæmolytisk anæmi |
| TxGNN-forudsigelsesscore | 93.76% |
| Bevisniveau | L5 (kun modelforudsigelse — ingen kliniske forsøg, ingen litteratur) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Vent |

---

## Hvorfor er denne forudsigelse rimelig?

For øjeblikket er detaljerede virkemåde-data for Toripalimab ikke tilgængelige i den formelle lægemiddelregistrering (MOA-felt er uudfyldt). Baseret på oplysninger, der er tilgængelige andre steder i bevisematerialet, er Toripalimab en PD-1-checkpoint-inhibitor, hvis farmakologisk virkning er at **frigive immunbremserne og forbedre T-celle-cytotoksisk aktivitet**, en tilgang, der bruges inden for onkologi til at hjælpe immunsystemet med at angribe tumorceller.

Blandet-type autoimmun hæmolytisk anæmi er derimod en tilstand, hvor immunsystemet allerede over-angriber kroppens egne røde blodlegemer; standardbehandling afhænger af **immunsuppression**, ikke immune-aktivering. Bevisematerialets egen mekanistiske vurdering markerer dette direkte: anti-PD-1-midler er klinisk kendt for at *forårsage* AIHA og relaterede cytopeniaer som immunrelaterede bivirkninger (irAE), snarere end at behandle dem. Det samme mønster gentages på tværs af de andre højtscorende kandidater i denne pakke — idiopatisk aplastisk anæmi, dermatitis, paroxysmal nattlig hemoglobinuri og lægemiddelinduceret AIHA — som alle bærer den samme annotation: den forudsagte indikation er en *kendt bivirkning* af PD-1-inhibering, ikke et terapeutisk mål.

Den mest sandsynlige forklaring er, at TxGNNs høje score afspejler **semantisk nærhed i embedrummet** (autoimmun/hæmatologisk sygdomsklynge) snarere end en ægte, biologisk understøttet behandlingsforhold. Dette er et tilfælde, hvor forudsigelsen bør behandles som en modelleringsartefakt, indtil uafhængige mekanistiske eller kliniske beviser fremkommer.

---

## Bevis fra kliniske forsøg

For øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Bevis fra litteratur

For øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Toripalimab har for øjeblikket ingen markedsføringstilladelse registreret i Danmark (0 licenser; markedsstatus: ikke markedsført). Ingen produkt-, doseringsform- eller godkendt-indikation-data er tilgængelige for rapportering.

---

## Cytotoksicitet

Toripalimab er en PD-1-checkpoint-inhibitor, en klasse af antineoplastisk immunterapi.

| Punkt | Indhold |
|-------|---------|
| Cytotoksicitetsklassificering | Immunterapi (PD-1-checkpoint-inhibitor) — ikke et konventionelt cytotoksisk middel |
| Myelosuppression-risiko | Se venligst Produktinformationens sammenfatning (SmPC) advarsler og forholdsregler |
| Emetogenicitetsklassificering | Se venligst Produktinformationens sammenfatning (SmPC) advarsler og forholdsregler |
| Overvågningspunkter | Se venligst Produktinformationens sammenfatning (SmPC) advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se venligst Produktinformationens sammenfatning (SmPC) advarsler og forholdsregler |

Bemærkning: i modsætning til konventionel kemoterapi har checkpoint-inhibitorer som klasse en risiko for immunrelaterede uønskede begivenheder (irAE) — herunder immun hæmolytisk anæmi, dermatitis og andre autoimmun-mønster-toksiciteter — som er direkte relevant for denne kandidat, da den forudsagte nye "indikation" overlapper med kendte irAE for denne lægemiddelklasse.

---

## Sikkerhedshensyn

Se venligst den godkendte Produktinformationens sammenfatning (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Afgørelse: Vent**

**Rationalet:**
Denne kandidat hviler på et L5-modelscores-kun-signal uden understøttende kliniske forsøg eller litteratur, og bevisematerialets egen mekanistiske analyse identificerer en direkte biologisk modsigelse — PD-1-inhibering er mere plausibelt en årsag til den forudsagte tilstand end en behandling for den. Et blokeringsdata-hul (manglende TFDA/SmPC-sikkerhedsdata) forhindrer også denne kandidat i formelt at indgå i S1-sikkerhedsvurderingsstadiet.

**For at fortsætte er følgende nødvendig:**
- Officiel SmPC/etiket-sikkerhedsdata (advarsler, kontraindikationer, DDI) — for øjeblikket et blokeringsdata-hul
- Bekræftet virkemåde-dokumentation fra DrugBank — for øjeblikket et høj-alvorlighed-datahul
- Uafhængigt præklinisk eller case-niveau-bevis specifikt støttende PD-1-inhibering i autoimmun cytopeni, da ingen findes for øjeblikket
- I betragtning af den mekanistiske modsigelse bør du overveje at deprioritere dette signal til fordel for andre TxGNN-kandidater med stærkere biologisk plausibilitet

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

