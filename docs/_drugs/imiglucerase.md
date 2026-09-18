---
layout: default
title: Imiglucerase
parent: Kun modelforudsigelse (L5)
nav_order: 227
evidence_level: L5
indication_count: 10
---

# Imiglucerase
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

# Imigluceras: Fra Gauchers sygdom til Hurlers syndrom

## Sammenfatning i én sætning

Imiglucerase (DrugBank DB00053) er en rekombinant glukocerebrosidaseerstatningsterapi, internationalt etableret som behandling for Gauchers sygdom.
TxGNN-modellen forudsiger, at det kan være effektivt mod **Hurlers syndrom (MPS I)**, med en meget høj lighedsscore, men **uden understøttende kliniske forsøg** og kun **2 generelle baggrundsudgivelser**, hvoraf ingen specifikt undersøger imiglucerase ved Hurlers syndrom.
Lægemidlets egen repurposing-begrundelse markerer denne forudsigelse som sandsynligvis en **falsk positiv** drevet af indlejringslighed på kategoriniveau ("lysosomalt lagringssygdom + enzymersatningsterapi") snarere end ægte biokemisk mekanisme-overlap.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Gauchers sygdom (enzymersatningsterapi)¹ |
| Forudsagt ny indikation | Hurlers syndrom (Mucopolysaccharidose type I) |
| TxGNN-forudsigelsesscore | 99.52% |
| Bevisniveau | L5 (modelforudsigelse alene) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 |
| Anbefalet beslutning | Afhold |

¹ Bevispaklens `drug.original_indications`-felt og `original_moa`-felt er begge tomme/datakløft (se DG002). "Gauchers sygdom" er angivet her baseret på internationalt anerkendt mærkning for imiglucerase (Cerezyme), ikke ud fra data indeholdt i denne bevispakke.

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede virkningsmekanisme-data ikke tilgængelige i denne bevispakke (Datakløft DG002). Baseret på offentligt kendt farmakologi er imiglucerase en rekombinant form af humant glukocerebrosidaseen, brugt som enzymersatningsterapi (ERT) til at nedbryde akkumuleret glukocerebroside i Gauchers sygdom.

Forbindelsen til Hurlers syndrom er dog svag. Hurlers syndrom (alvorlig MPS I) er forårsaget af mangel på **alfa-L-iduronidase (IDUA)**, hvilket fører til akkumulering af heparansulfat og dermatansulfat — et helt anderledes enzym og substrat end glukocerebrosidasen. En sygdomsspecifik ERT (laronidase, Aldurazyme) er allerede godkendt for MPS I. Den høje TxGNN-score afspejler sandsynligvis et delt **indlejringsmønster på klasseniveau** ("lysosomalt lagringssygdom" + "enzymersatningsterapi") snarere end en faktisk delt biokemisk vej, og bør behandles som et **højrisiko-falsk-positivt mønster** snarere end et ægte repurposing-signal.

Understøttende litteratur identificeret i denne bevispakke løser ikke denne bekymring: begge publikationer er generelle oversigter over enzymersatningsterapi på tværs af flere lysosomale lagringssygdomme (nævner Hurlers syndrom kun som et eksempel blandt flere), uden data specifikt for imigluceras' effektivitet i MPS I.

---

## Evidens fra kliniske forsøg

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

| PMID | År | Type | Journal | Vigtige fund |
|------|-----|------|---------|---------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Oversigt/Metode | Proceedings of the National Academy of Sciences | Generel oversigt over PET-billeddannelse til overvågning af enzymersatningsterapi på tværs af lysosomale lagringssygdomme (Gaucher, Fabry, Hurler, Hunter, Maroteaux-Lamy, Pompe); ikke specifik for imigluceras' effektivitet ved Hurlers syndrom |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Oversigt | La Revue de médecine interne | Generel oversigt over enzymersatningsterapi-historie og udvikling på tværs af lysosomale lagringssygdomme, refererer imigluceras (Cerezyme) i sammenhæng med Gauchers sygdom behandling, ikke Hurlers syndrom specifikt |

---

## Markedsinformation for Danmark

Imiglucerase har i øjeblikket **ingen markedsføringsgodkendelse** på rekord i Danmark (`market_status: Not marketed` / Ikke markedsført, `total_licenses: 0`). Der blev ikke fundet nogen Laegemiddelstyrelsen national eller EMA centraliseret godkendelsesposter i denne bevispakke.

---

## Sikkerhedsovervejelser

Se venligst den godkendte sammenfatning af produktegenskaber (SmPC) for sikkerhedsinformation.

*(Bemærk: Denne bevispakke har en blokerende datakløft — DG001 — for etiketadvarsler/kontraindikationer, hvilket betyder sikkerhedsgennemgang (S1-stadie) ikke kan fortsætte, før disse data er indhentet.)*

---

## Konklusion og næste skridt

**Beslutning: Afhold**

**Begrundelse:**
TxGNN-scoren er høj, men lægemidlets egen repurposing-begrundelse identificerer dette som sandsynligvis en indlejringsniveau falsk positiv: imigluceras' målenzym (glukocerebrosidasen) er mekanistisk uafhængig af alfa-L-iduronidase-mangelen, der ligger til grund for Hurlers syndrom, for hvilket en sygdomsspecifik ERT (laronidase) allerede er godkendt. Der er ingen kliniske forsøg og ingen sygdomsspecifik litteratur, der understøtter imiglucerase for denne indikation, og lægemidlet er ikke i øjeblikket markedsført i Danmark. Bevisniveauet er L5 (modelforudsigelse alene) og understøtter ikke progression forbi initial screening.

**For at fortsætte skal følgende være nødvendigt:**
- Oprindelige virkningsmekanisme-data (MOA) for imiglucerase (Datakløft DG002)
- Danmarks/EU-etiket advarsler og kontraindikationer (Datakløft DG001 — Blokering; påkrævet før nogen S1 sikkerhedsgennemgang)
- Bekræftelse af oprindeligt godkendt indikation(er) fra en struktureret regulatorisk kilde
- Enhver preklinisk eller mekanistisk undersøgelse, der direkte tester glukocerebrosidasbaseret ERT i MPS I-modeller, enten at underbygge eller udelukke det forudsagte signal
- En klar klinisk begrundelse for, hvorfor imiglucerase-repurposing ville tilbyde tilføjet værdi, i betragtning af at en specifik godkendt terapi (laronidase) allerede eksisterer for Hurlers syndrom

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

