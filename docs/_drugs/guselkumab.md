---
layout: default
title: Guselkumab
parent: Kun modelforudsigelse (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
---

# Guselkumab
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

# Guselkumab: Fra plaque-psoriasis til lægemiddelinduceret osteoporose

## Sammenfatning i én sætning

Guselkumab (Tremfya®) er et fuldt humant monoklonal antistof, der selektivt blokerer IL-23 p19-underenheden, og som er globalt godkendt til moderat til svær plaque-psoriasis og psoriasisartritis, men i øjeblikket ikke markedsført i Danmark.
TxGNN-modellen tildeler den højeste prognosescore til **lægemiddelinduceret osteoporose** (99.84%), hvilket tyder på en mulig ny terapeutisk retning via IL-23/RANKL-knogleresorptionsvej.
Der er imidlertid i øjeblikket **ingen kliniske forsøg** og **ingen publikationer**, der direkte understøtter denne specifikke indikation, hvilket resulterer i svag samlet evidens for denne lægemiddelgenbrugretning.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke registreret i Danmark; globalt godkendt til moderat til svær plaque-psoriasis (Tremfya®, Janssen) |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose |
| TxGNN-prognosescore | 99.84% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Afvent |

---

## Hvorfor er denne prognose rimelig?

I øjeblikket er detaljerede mekanisme-data fra DrugBank ikke tilgængelige for guselkumab. Baseret på etableret videnskabelig og klinisk viden bindes guselkumab selektivt til p19-underenheden af interleukin-23 (IL-23) og blokerer IL-23/Th17/IL-17-inflammatoriske akse. I psoriasis overudtrykkes IL-23 i læsionshud, driver Th17-celledifferentiering og fremmer sekretion af IL-17A/F og IL-22, som igen udløser keratinocythyperproliferation og epidermal inflammation. Denne mekanisme er direkte valideret af flere gennemførte fase 3-forsøg og udgør grundlaget for guselkumabs FDA/EMA-godkendte terapeutiske virkning.

Den teoretiske forbindelse til lægemiddelinduceret osteoporose bygger på IL-17s nedstrømsrolle i knoglemetabolisme: IL-17 kan opregulere RANKL-ekspression på osteoblaster og stromale celler, hvorved osteoklastedifferentiering og knogleresorption fremmes. Blokering af IL-23 opstrøms kunne teoretisk reducere RANKL-medieret knogletab i en inflammatorisk sammenhæng.

Imidlertid er **lægemiddelinduceret osteoporose** — som en særskilt klinisk enhed — overvejende forårsaget af direkte knoglemetabolismeforstyrrelser fra glucocorticoider (der undertrykker osteoblastogenese, forbedrer osteoklastedifferentiering via RANKL/OPG-ubalance), aromatasehæmmere (østrogenmangel) eller andre midler. Disse patofysiologiske mekanismer fungerer stort set uafhængigt af IL-23/Th17-aksen. Den foreslåede mekanistiske forbindelse er derfor indirekte og spekulativ, og der er i øjeblikket ingen præ-klinisk eller klinisk evidens, der understøtter guselkumabs brug i denne indikation.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for guselkumab i lægemiddelinduceret osteoporose.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig for guselkumab i lægemiddelinduceret osteoporose.

---

## Markedsinformation for Danmark

Guselkumab er ikke registreret i Danmark ifølge det aktuelle datasæt. Lægemiddelstyrelsen har ingen markedsføringstilladelsesrecords i dette system.

> **Bemærkning for klinikere**: Tremfya® (guselkumab) har en centraliseret EMA-markedsføringstilladelse til moderat til svær plaque-psoriasis og aktiv psoriasisartritis hos voksne. Sundhedsfaglige bør verificere den aktuelle Lægemiddelstyrelsen og EMA-markedsføringstilladelsestatus via [EMA-produktsiden](https://www.ema.europa.eu) eller Lægemiddelstyrelsens Medicinpriser-database før ordinering.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste skridt

**Afgørelse: Afvent**

**Begrundelse:**
Selvom TxGNN tildeler en meget høj prognosescore (99.84%) til lægemiddelinduceret osteoporose, stammer den foreslåede mekanisme fra en indirekte IL-23/IL-17/RANKL-vej, som ikke er den primære driver for lægemiddelinduceret knogletab. Fuldstændig mangel på understøttende præ-klinisk data, kliniske forsøg og publiceret litteratur forhindrer fremskridt ud over model-niveau prognose på nuværende tidspunkt.

**For at fortsætte er følgende nødvendigt:**
- Præ-kliniske studier, der demonstrerer IL-23-hemnings virkning specifikt på lægemiddelinduceret (glucocorticoid- eller aromatasehemmininduceret) knogletab, som adskilt fra inflammatorisk knogleeroption
- Mekanisme-data hentet fra DrugBank API for formelt at karakterisere guselkumabs farmakodynamiske profil
- Sikkerhedsdata fra EMA SmPC, herunder advarsler om immunosuppression, infektioner (tuberkulose-reaktivering, alvorlige infektioner) og injektionsstedsreaktioner
- Lægemiddelinteraktionsprofil (aktuel DDI-forespørgsel gav ingen resultater)
- Præcisering af patientpopulationen: om målet er patienter under samtidig immunosuppression, hvor IL-23-hemning kan have en sekundær knoglebeskyttende fordel

---

### Sekundært fund af høj klinisk relevans

> TxGNN-modellen forudsiger også **psoriasis** (rang 5, score 99.75%) med **evidensniveau L1** — understøttet af over 50 registrerede kliniske forsøg og 20 publikationer, herunder flere gennemførte fase 3-RCT'er (VOYAGE 1, VOYAGE 2, NAVIGATE) og netværksmeta-analyser i *JAMA Dermatology*. Anbefalingen for denne indikation er **Fortsæt med sikkerhedsforanstaltninger**.
>
> Dette fund validerer TxGNN-modellens diskriminativ evne: guselkumabs etablerede globale godkendelse for plaque-psoriasis identificeres korrekt som en prognose med høj tillid. For danske sundhedsmyndighedsbeslutningstagere understøtter dette en vej til at evaluere formelle Lægemiddelstyrelsen/EMA-registreringsstatus og refusionsbetragtninger for psoriasis — et handlingskrævende fund, der kræver prioriteret opmærksomhed adskilt fra lægemiddelgenbrugretningen for lægemiddelinduceret osteoporose.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

