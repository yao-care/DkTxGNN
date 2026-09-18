---
layout: default
title: Nitrofurantoin
parent: Kun modelforudsigelse (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
---

# Nitrofurantoin
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

# Nitrofurantoin: Fra urinvejsinfektioner til reumatoid artritis

## Sammenfattelse i én sætning

Nitrofurantoin er en nitrofuran-klassens antibakteriel, etableret som første linje oral behandling for ukomplicate urinvejsinfektioner (UTI); denne specifikke indikation er ikke til stede i det aktuelle bevisemne, så det er anført her ud fra etableret farmakologisk viden snarere end kildedata. TxGNN-modellen forudsiger, at det kan være effektivt for **reumatoid artritis**, men det nuværende beviisgrundlag består af **0 kliniske forsøg** og **11 litteraturopslag**, næsten helt udelukkende beskrivende läkemedels-induceret toksicitet (lungefibrose, hepatitis) hos RA-patienter snarere end terapeutisk effektivitet — dette er en alene modelscoring-baseret forudsigelse med muligt sikkerhedssignal, ikke en effektivitetsfinding.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Original indikation | Urinvejsinfektion (UTI) — ikke registreret i bevisemnen; baseret på etableret farmakologi |
| Forudsagt ny indikation | Reumatoid artritis |
| TxGNN-forudsigelsesscore | 99.89% |
| Bevisniveau | L5 |
| Danske markeds status | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Gennemgår |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme er ikke i øjeblikket tilgængelige (datakløft DG002). Baseret på etableret farmakologi reduceres nitrofurantoin af bakterielle flavoproteiner til reaktive mellemtrin, der beskadiger bakterielt DNA, ribosomale proteiner og andre makromolekyler — en uspecifik antibakteriel mekanisme uden etableret immunomodulatorisk eller anti-revmatisk aktivitet.

Urinvejsinfektion og reumatoid artritis hører til ikke-relaterede sygdomskategorier (infektiøs vs. autoimmun/revmatologisk), i modsætning til typiske repurposingpar, der deler organ system eller stivejsoverlap. Der er ingen mekanistisk eller farmakologisk rationelle forbinder de to indikationer til stede i dette bevisemne.

De 11 litteraturopslag, der returneres for denne parring, understøtter **ikke** en terapeutisk rationel. De er næsten udelukkende kasuistikker og reviews, der beskriver nitrofurantoin-induceret pulmonal og hepatisk toksicitet, der opstår *hos* RA-patienter (f.eks. en dødelig interaktion med methotrexat), plus en observationsstudie om antibiotika og RA-anfald, der ikke er specifik for nitrofurantoin. Med andre ord cluster litteraturen omkring nitrofurantoin som en **risikofaktor** hos RA-patienter, ikke som en **behandling** for RA. Dette bør læses som en høj TxGNN-lighedsscore uden understøttende biologisk eller klinisk support — sammenligneligt med modellens andre lavfidusforudsigelser uden bevis i dette samme output (f.eks. L5/gennemgår-klassifikationerne for de to syndromiske diagnoser ved ranger 3–4 og 9–10).

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

| PMID | År | Type | Tidsskrift | Vigtige resultater |
|------|-----|------|------|---------|
| [31222078](https://pubmed.ncbi.nlm.nih.gov/31222078/) | 2019 | Observationel (selvkontrolleret kasuistikkserie) | Scientific Reports | Analyse af 31.992 nydiagnosticerede RA-patienter (UK CPRD GOLD), der undersøger antibiotikaeksponering timing vs. RA-anfald; ikke nitrofurantoin-specifik effektivitetsdata |
| [15195196](https://pubmed.ncbi.nlm.nih.gov/15195196/) | 2004 | Review | Saudi Medical Journal | Oversigt over lægemiddelinduceret lungefibrose; viser nitrofurantoin blandt årsagsfremkaldende midler og bemærker RA som en prædisponerende tilstand for fibrose |
| [35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/) | 2022 | Kasuistik | Cureus | Irreversibel lungefibrose hos en 94-årig RA-patient fra kombineret methotrexat + nitrofurantoin-terapi — et toksicitets-/interaktionssignal, ikke effektivitetsbevis |
| [25362778](https://pubmed.ncbi.nlm.nih.gov/25362778/) | 2014 | Review | La Revue du praticien | Oversigt over lægemiddelinduceret interstitiel lungesygdom; nitrofurantoin angivet blandt årsagsfremkaldende antibiotika |
| [3335140](https://pubmed.ncbi.nlm.nih.gov/3335140/) | 1988 | Kasuistikkeserie | Chest | Kohort af 57 hospitaliserede RA-patienter med interstitiel lungefibrose; beskriver RA-associeret lungesygdom, evaluerer ikke nitrofurantoin som behandling |
| [11937933](https://pubmed.ncbi.nlm.nih.gov/11937933/) | 2002 | Kasuistik | Annales de dermatologie et de venereologie | Phenylbutazon-induceret spytkirtelinflammation kasuistik; nitrofurantoin nævnt kun som et andet lægemiddel associeret med spytkirtelinflammation, urelated til RA-behandling |
| [899886](https://pubmed.ncbi.nlm.nih.gov/899886/) | 1977 | Observationel | Acta Medica Scandinavica | Korttidsnitrofurantoin-terapi for bakteriuri hos kvinder i midten af livet; urelated til RA |
| [41635325](https://pubmed.ncbi.nlm.nih.gov/41635325/) | 2026 | Kasuistik | Cureus | Autoimmun hepatitis kasuistik; nitrofurantoin er et af flere lægemidler udelukket som årsag til lægemiddelinduceret leverbeskadigelse, RA nævnt kun som differentialdiagnose |
| [8104358](https://pubmed.ncbi.nlm.nih.gov/8104358/) | 1993 | Kasuistik | Revue de pneumologie clinique | Guldalt-induceret pneumonitis/alveolitis kasuistik hos patient på anti-revmatisk terapi; nitrofurantoin ikke direkte impliceret |
| [4608019](https://pubmed.ncbi.nlm.nih.gov/4608019/) | 1974 | Review | Der Internist | Generel oversigt over alveolitis og lungefibrosemekanismer |

**Bemærk:** Dette litteratursæt er domineret af nitrofurantoin **toksicitet hos RA-patienter**, ikke bevis for terapeutisk nytte for RA.

---

## Danske markedsoplysninger

Der er ikke fundet markedsføringstilladelser. Nitrofurantoin er i øjeblikket **ikke markedsført** i Danmark ifølge de tilgængelige data (0 licenser på record).

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumésamfund (SmPC) for sikkerhedsoplysninger (vigtige advarsler, kontraindikationer og DDI-data er ikke tilgængelige i dette bevisemne — markeret som blokerende datakløft DG001).

**Bemærk fra litteraturgennemgang:** En kasuistik ([PMID 35145797](https://pubmed.ncbi.nlm.nih.gov/35145797/)) beskriver irreversibel lungefibrose hos en RA-patient fra kombineret methotrexat og nitrofurantoin-brug — dette interaktionssignal bør tages i betragtning før yderligere evaluering af nitrofurantoin hos RA-patienter.

---

## Konklusion og næste trin

**Beslutning: Gennemgår**

**Begrundelse:**
Der eksisterer ingen kliniske forsøg for denne parring, ingen MOA-data er tilgængelige, og den tilknyttede litteratur beskriver toksicitetsrisiko hos RA-patienter snarere end terapeutisk effektivitet. TxGNN-scoren på 99.89% afspejler kun modellighedsscore (bevisniveau L5) og er ikke understøttet af nogen biologisk eller klinisk rationel — dette er ikke tilstrækkeligt til at retfærdiggøre yderligere investering på nuværende tidspunkt.

**For at fortsætte er følgende nødvendigt:**
- Dansk SmPC / advarsler og kontraindikationsdata (blokerende kløft, DG001)
- DrugBank-mekanisme for handlingsdata (DG002)
- En målrettet litteratur- eller præklinsik søgning specifikt for immunomodulatorisk/anti-inflammatorisk aktivitet af nitrofurantoin, da ingen i øjeblikket eksisterer
- Præcisering af lægemiddelinteraktionsrisiko med methotrexat (almindelig RA-terapi) før nogen klinisk overvejelse
- Bekræftelse af dansk markeds-/registreringsstatus, da lægemidlet er i øjeblikket umarkedsført med 0 tilladelser på record

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

