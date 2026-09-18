---
layout: default
title: Inotuzumab Ozogamicin
parent: Kun modelforudsigelse (L5)
nav_order: 233
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
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

# Inotuzumab ozogamicin: Fra akut lymfoblastisk leukæmi til lægemiddelinduceret osteoporose

## Et-linjer sammenfatning

Inotuzumab ozogamicin er et anti-CD22 antistof-lægemiddelkonjugat (ADC), etableret globalt til CD22-positive B-celle forløbercelleakut lymfoblastisk leukæmi (ALL); dette specifikke evidenspakke indeholder ikke selv den oprindelige indikation eller etikettekst (datakløft). TxGNN-modellen forudsiger mulig virkning ved **lægemiddelinduceret osteoporose**, men dette understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer**, og evidenspakkens egen mekanistiske gennemgang flagfestiviterer forudsigelsen som en sandsynlig ikke-specifik modelartefakt snarere end et virkeligt farmakologisk signal.

---

## Hurtigt overblik

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | CD22-positive B-celle forløbercel akut lymfoblastisk leukæmi (ALL) — *ikke til stede i det danske registerdata (lægemidlet er ikke markedsført i Danmark); angivet her ud fra generel etikettering, da evidenspakkens eget `original_indications` felt er tomt* |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose |
| TxGNN-forudsigelsesscore | 98,24% |
| Evidensniveau | L5 |
| Status på dansk marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkemekanisme-data for denne kandidat er ikke tilgængelige i evidenspakken (flagget som et højgrads datakløft). Baseret på kendt farmakologi er inotuzumab ozogamicin et antistof-lægemiddelkonjugat, der kombinerer et anti-CD22 monoklonalt antistof med det cytotoksiske payload calicheamicin: binding til CD22 på ondartede B-lymfocytter udløser internalisering af konjugatet, og calicheamicin forårsager derefter DNA-dobbeltstrengsbrud, der dræber målcellen. Denne mekanisme er meget specifik for CD22-eksprimerende hæmatologiske maligniteteter.

Der er ingen etableret farmakologisk eller klinisk forbindelse mellem denne mekanisme og knoglestofskifte (osteoklast/osteoblast-aktivitet), og evidenspakkens egen repurposing-begrundelse siger dette eksplicit: der er ikke identificeret nogen direkte mekanistisk forbindelse mellem CD22/calicheamicin-medieret B-celle-drab og lægemiddelinduceret knogletab.

Den høje TxGNN-score afspejler højst sandsynligt en generisk vidensgrafsassociation snarere end et lægemiddelspecifikt signal — cytotoksiske/kemoterapeutiske lægemiddelknuder er bredt forbundet med knogletabsrelaterede bivirkningsknuder i den underliggende graf, hvilket kan øge lighedsscore for mange cytotoksiske midler uanset deres faktiske målbiologi. Bemærkelsesværdigt viser de andre tophits-kandidater i denne samme evidenspakke (f.eks. HER2-positive og luminal-subtype brystkræft) det samme mønster — ingen CD22-målekspression i det relevante væv, og i ét tilfælde blev det vedhæftede "understøttende litteratur" senere fundet at være en nøgleordsmatching-artefakt (relaterede B-celle/hepatitis-B-papirer matchet via bogstavet "B" i "Luminal B"). Dette tyder på en systematisk mangel på specificitet i denne lægemiddels forudsigelsessæt, ikke blot en isoleret svag kandidat.

---

## Klinisk forsøgsevidence

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidence

I øjeblikket er der ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Inotuzumab ozogamicin har i øjeblikket **ingen markedsføringstilladelse i Danmark** (0 tilladelser på arkiv; markedsstatus: Ikke markedsført). Der er derfor ingen produkt-, doseringsform- eller indikationsniveau-licensdata tilgængelige fra det danske register.

---

## Cytotoxicitet

| Emne | Indhold |
|------|---------|
| Cytotoxicitetsklassificering | Målrettet terapi — Antistof-lægemiddelkonjugat (anti-CD22 antistof, der bærer det cytotoksiske payload calicheamicin) |
| Myelosuppressionsrisiko | Se venligst Produktresumé (SmPC) - advarsler og forsigtighedsregler |
| Emetogenicitetsklassificering | Se venligst Produktresumé (SmPC) - advarsler og forsigtighedsregler |
| Overvågningspunkter | Se venligst Produktresumé (SmPC) - advarsler og forsigtighedsregler |
| Håndteringsbeskyttelse | Payload er et DNA-skadende cytotoksisk middel; standard cytostatika-håndteringsforsigtighedsregler bør gælde afventer bekræftelse via SmPC |

---

## Sikkerhedshensyn

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Selvom TxGNN-scoren er høj, vurderer evidenspakkens egen mekanistiske gennemgang den tophits-forudsigelse (lægemiddelinduceret osteoporose) som værende uden farmakologisk sandsynlighed og sandsynligvis afspejler en generisk graftopologi-artefakt snarere end et lægemiddelspecifikt signal. Der er ingen understøttende klinisk forsøgs- eller litteraturevidence (Evidensniveau L5), lægemidlet har ingen markedsføringstilladelse i Danmark, og etiket-/sikkerhedsdata, der kræves selv for et indledende sikkerhedsscreening (S1), mangler — et blokeringsgrads datakløft.

**For at fortsætte er følgende nødvendig:**
- TFDA/SmPC-etiketadvarsler og kontraindikationer (Blokeringsgrads datakløft: DG001)
- Bekræftet virkemekanisme-detalje, der stammer fra DrugBank eller den godkendte etiket (Højtprioritet datakløft: DG002)
- En uafhængig, biologisk begrundet begrundelse, der forbinder CD22-ADC-farmakologi til knoglestofskifte — eller formal udelukkelse af denne kandidat, hvis ingen kan etableres
- Prækliniske eller real-world-data om knoglemineral-densitetseffekter, hvis denne indikation stadig skal forfølges
- En bredere specificitetgennemgang af dette lægemiddels fulde TxGNN-forudsigelsessæt, givet at andre tophits-kandidater (brystkræftsubtypter) viser det samme fravær af målekspression-begrundelse og i ét tilfælde forureningens litteraturmatches

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

