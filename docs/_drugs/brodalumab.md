---
layout: default
title: Brodalumab
parent: Kun modelforudsigelse (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Brodalumab: forudsagt ny indikation Strongyloidiasis (evidensniveau L5). Oprindelig indikation: Ikke oplyst i de indsamlede data"
monitor_inn: "Brodalumab"
predicted_indications: ["strongyloidiasis", "strongyloidiasis", "eye disease", "eye disease", "vitamin deficiency disorder", "vitamin deficiency disorder", "von Hippel anomaly", "von Hippel anomaly", "optic perineuritis", "recurrent idiopathic neuroretinitis"]
---

# Brodalumab
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

# Brodalumab: Fra psoriasis (IL-17RA-hæmmer) til strongyloidiasis

## Resumé

Brodalumab er et biologisk lægemiddel (en IL-17-receptor A-antagonist), der markedsføres i Danmark under navnet Kyntheum. Der foreligger ingen godkendt indikationstekst i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at lægemidlet kan være effektivt mod **strongyloidiasis**, men der er **0 kliniske forsøg** og **0 publikationer** til støtte for denne retning. Forudsigelsen vurderes som biologisk ikke understøttet.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i de indsamlede data |
| Forudsagt ny indikation | Strongyloidiasis |
| TxGNN-forudsigelsesscore | 99,84 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Brodalumab er kendt som en antagonist af IL-17-receptor A (IL-17RA), som blokerer signalering fra flere IL-17-cytokiner.

Kontrol af *Strongyloides*-infektion afhænger hovedsageligt af Th2-respons (IL-4, IL-5, IL-13) og eosinofile celler, med et vist bidrag fra IL-17-medieret slimhindeimmunitet. Hæmning af IL-17 kan teoretisk set svække værtens forsvar eller forværre infektionen. Den høje modelscore (0,998) understøttes derfor ikke af biologien, og forudsigelsen kan ikke forankres mekanistisk.

### Øvrige forudsigelser i datasættet

Samme billede gælder for de øvrige topforudsigelser. Nogle forekommer i datasættet flere gange med identiske data.

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Strongyloidiasis | 99,84 % | L5 | Ingen mekanistisk sammenhæng; mulig forværring af infektion |
| Øjensygdom (eye disease) | 99,82 % | L4 | Indirekte plausibilitet via IL-17 ved uveitis/Behçet, men litteraturen peger mere på en sikkerhedsrisiko end på gavnlig effekt |
| Vitaminmangeltilstand | 99,80 % | L5 | Ingen plausibel mekanisme; sandsynligvis artefakt i vidensgrafen |
| Von Hippel-anomali | 99,77 % | L5 | Ingen mekanistisk begrundelse; tilstanden er uklart defineret |
| Optisk perineuritis | 99,76 % | L5 | Kun løs konceptuel sammenhæng; normalt steroidfølsom |
| Recidiverende idiopatisk neuroretinitis | 99,76 % | L5 | Kun løs konceptuel sammenhæng; ingen evidens |

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for strongyloidiasis.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur for strongyloidiasis.

Til sammenligning blev der for den næstplacerede forudsigelse (øjensygdom) fundet tre publikationer, som ikke viser gavnlig effekt:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [42576218](https://pubmed.ncbi.nlm.nih.gov/42576218/) | 2026 | Præklinisk (dyremodel) | Journal of Translational Medicine | IL-17-receptorhæmning med brodalumab begrænser eksperimentel periodontitis (ikke en øjensygdom) |
| [41770262](https://pubmed.ncbi.nlm.nih.gov/41770262/) | 2026 | Case report | Rheumatology International | Behçets sygdom opstod som paradoks reaktion efter start af brodalumab hos en patient med kronisk non-bakteriel osteitis |
| [41916603](https://pubmed.ncbi.nlm.nih.gov/41916603/) | 2026 | Farmakovigilansanalyse | Canadian Journal of Ophthalmology | Analyse af uveitis som bivirkning ved systemiske lægemidler |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105697815 | Kyntheum (LEO Pharma A/S) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgraf (ikke produktresumé):** Crohns sygdom, inflammatorisk tarmsygdom og Crohns colitis. Disse stammer fra TxGNN-vidensgrafen (PrimeKG) og ikke fra godkendt produkttekst.
- **Lægemiddelinteraktioner:** 68 interaktioner er registreret. Blandt de vigtigste:
  - **Alvorlige (Major):** adalimumab, baricitinib, certolizumab pegol, BCG-levende vaccine (Tice-stammen)
  - **Moderate:** roflumilast, alefacept, alemtuzumab, anakinra, canakinumab, tetanustoksoid samt flere levende eller inaktiverede vacciner (bl.a. miltbrand, kolera, adenovirus)
  - **Mindre (Minor):** zinksalte (acetat, gluconat, sulfat, chlorid)
- **Andre signaler:** Case report om paradoks udløsning af Behçets sygdom samt farmakovigilansdata om uveitis tyder på en mulig sikkerhedsbekymring ved øjenrelaterede tilstande.

For øvrige advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om strongyloidiasis har kun modelstøtte (L5), ingen kliniske forsøg eller litteratur, og biologien taler snarere imod (IL-17-hæmning kan svække værtsforsvaret). Der mangler desuden data om virkningsmekanisme, oprindelig indikation og sikkerhedsoplysninger fra produktresuméet.

**For at komme videre er følgende nødvendigt:**
- Indhentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer, godkendt indikation)
- Mekanismedata (MOA) fra DrugBank
- Prækliniske eller kliniske data, der kan understøtte en sammenhæng mellem IL-17RA-blokade og den forudsagte indikation
- En særskilt sikkerhedsvurdering af risikoen for infektioner og for paradokse inflammatoriske reaktioner (herunder øjenmanifestationer)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

