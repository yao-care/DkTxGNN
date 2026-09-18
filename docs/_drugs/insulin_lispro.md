---
layout: default
title: Insulin Lispro
parent: Kun modelforudsigelse (L5)
nav_order: 237
evidence_level: L5
indication_count: 10
---

# Insulin Lispro
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

# Insulin Lispro: Fra Diabetes Mellitus til Autoimmun Oofrit

## Sammenfatning på en sætning

Insulin lispro er et hurtigtvirkende insulinanalog, der bruges til at regulere blodglucose ved diabetes mellitus. TxGNN-modellens topforudsigelse knytter det til **Autoimmun Oofrit** med en meget høj lighedsscore, men **nul kliniske forsøg og nul publikationer** understøtter i øjeblikket dette link, og modellens egen begrundelse antyder, at forbindelsen afspejler et delt autoimmunt comorbiditets-mønster snarere end en ægte farmakologisk genopbygningsmekanisme.

## Hurtigt overblik

| Emne | Indhold |
|------|------|
| Oprindelig indikation | Diabetes mellitus (insulinerstatningsterapi) — baseret på generelt lægemiddelkendskab; ikke bekræftet af danske licensdata, da ingen er tilgængelig i denne bevismappe |
| Forudsagt ny indikation | Autoimmun Oofrit |
| TxGNN-forudsigelsesscore | 99.78% |
| Bevisniveau | L5 |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede virkningsmekanisme-data ikke tilgængelige. Baseret på kendt generel farmakologi er insulin lispro et hurtigtvirkende rekombinant humant insulinanalog; dets effektivitet i glykæmisk kontrol for diabetes mellitus er velkendt, men ingen MOA-data i denne bevismappe understøtter ekstrapolering af en direkte farmakologisk virkning på ovariel autoimmun sygdom.

TxGNN-begrundelsen selv signalerer, at denne forudsigelse er en **comorbiditets-association snarere end en behandlingshypotese**: autoimmun oofrit og type 1-diabetes mellitus er begge hyppige komponenter i Autoimmun Polyglantulær Syndrom type 2 (APS-2), og deler sandsynligvis overlappende genetisk modtagelighed (f.eks. HLA-haplotyper). Dette delte-knude-mønster i vidensgrafen er en plausibel grund til den høje lighedsscore, men der er ingen mekanistisk evidens for, at insulin selv udøver en terapeutisk virkning på ovariel autoimmun inflammation.

Det er også værd at bemærke, at TxGNN fremhævede fire andre kandidat-sygdomme i top 10 (tiamineresponsiv dysfunktionssyndrom, klassisk stiff person-syndrom, fokalt stivt lemmesyndrom og opsismodysplasi) med meget lignende scores. Hver enkelt bærer samme underliggende forbehold i sin begrundelse — forbindelsen opstår fra delt autoimmun, metabolisk eller gen-vej-knuder (f.eks. GAD65-autoimmunitet, SLC19A2/insulin-comorbidittet eller INPPL1–insulin-signalerings-vej-overlap) snarere end en påvist behandlingsvirkning. Dette mønster antyder, at det aktuelle TxGNN-output for insulin lispro bør læses som et signal til hypotesegenerering, ikke en genopbygningskandidat klar til evaluering.

## Klinisk forsøgsbevis

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

## Litteraturbevis

I øjeblikket er der ingen relateret litteratur tilgængelig.

## Information om det danske marked

Ingen markedsføringstilladelse for insulin lispro er i øjeblikket registreret i denne bevismappe for det danske marked (Status på markedet: Ikke markedsført; 0 licenser på fil). Dette kan afspejle en ægte fravær af lokal Lægemiddelstyrelsen/EMA-registrering, eller det kan afspejle et gap i dataindsamlingen — dette bør verificeres direkte mod Lægemiddelstyrelsens produktregister før nogen senere beslutning.

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

*(Bemærk: denne bevismappe signalerer fraværet af SmPC-afledte advarsler/kontraindikationer som et **Blokerende** data-gap — se Konklusion nedenfor.)*

## Konklusion og næste skridt

**Beslutning: Afvent**

**Begrundelse:**
Forudsigelsen hviler helt på TxGNN-modellens score (L5 — ingen kliniske forsøg, ingen litteratur, ingen observationsdata), og den medfølgende mekanistiske begrundelse karakteriserer eksplicit lægemiddel–sygdoms-linket som en comorbiditets/delt-knude-artefakt snarere end en plausibel farmakologisk genopbygningshypotese. Der er i øjeblikket intet grundlag for at føre denne kandidat videre ud over hypotesegenerering.

**For at fortsætte, er følgende nødvendigt:**
- SmPC-advarsler og kontraindikationer for insulin lispro (i øjeblikket et **Høj**-sværhedsgrads data-gap — påkrævet før nogen sikkerhedsvurdering, jf. DG001)
- Verificeret virkningsmekanisme-data fra DrugBank eller anden autorativ kilde (i øjeblikket et **Høj**-sværhedsgrads data-gap, jf. DG002)
- Bekræftelse af dansk/EU-markedsføringstilladelsestatus direkte fra Lægemiddelstyrelsen eller EMA-registret
- Uafhængig mekanistisk eller præ-klinisk evidens, der forbinder insulinsignalering til ovariel autoimmun patologi, ud over den comorbiditets-association, som vidensgrafen identificerede
- Hvis det forfølges yderligere, ekspert-input fra endokrinologi/reproduktiv-immunologi for at vurdere biologisk plausibilitet før nogen investering på forsøgsstadiet

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

