---
layout: default
title: Parecoxib
parent: Kun modelforudsigelse (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Parecoxib
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

# Parecoxib: Fra postoperativ smerte til migræne

*(Bemærk: Evidenspakken registrerer ikke en oprindelig indikation for Parecoxib — `original_indications` er tom. "Postoperativ smerte" afspejler Parecoxibs offentligt kendte godkendt anvendelse som en injicerbar COX-2-hæmmer-prodrug af valdecoxib; det kommer ikke fra denne Evidenspakke og bør verificeres mod den officielle SmPC.)*

## Resumé på en sætning

Parecoxib er en parenteral, selektiv COX-2-hæmmer (prodrug af valdecoxib); dens oprindelige godkendte indikation er ikke dokumenteret i denne Evidenspakke, og den har i øjeblikket **0 markedsføringstilladelser** i Danmark ("Ikke markedsført"). TxGNN-modellen forudsiger, at den kan være effektiv for **Migræneforstyrrelse** med en forudsigelsesscore på **99.55%**, men denne højest rangerede kandidat har **ingen direkte tilknyttede kliniske forsøg eller litteratur** — understøttende evidens er indirekte, hentet fra en tæt beslægtet "Hovedpineforstyrrelse"-klynge (samme TxGNN-scorefamilie, ét pilot-RCT).

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ikke dokumenteret i Evidenspakken (almen viden: korttidsbehandling af postoperativ smerte) |
| Forudsagt ny indikation | Migræneforstyrrelse |
| TxGNN-forudsigelsesscore | 99.55% |
| Evidensniveau | L3 (ifølge pakkeberegning; baseret på indirekte evidens, ikke direkte forsøg/litteratur for denne enhed) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afventer |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede mekanisme-for-handling-data for Parecoxib er ikke tilgængelige i denne Evidenspakke (blokering/høj-alvorlighed datakløft: DG002). Baseret på generel farmakologisk viden er Parecoxib en selektiv COX-2-hæmmer administreret parenteralt og hurtigt hydrolyseret in vivo til sit aktive metabolit, valdecoxib. COX-2-hæmning reducerer produktionen af prostaglandin E2 (PGE2), som er mekanismen bag dens etablerede analgetiske anvendelse.

Migrænefysiologi involverer neurogen inflammation og meningeale vasodilatation, processer delvis medieret af COX-2/PGE2-banen. Teoretisk kunne COX-2-hæmning reducere PGE2-induceret vasodilatation og smertesensitivisering, komplementering triptaner (som virker på 5-HT1B/1D-receptorer til at forårsage vasokonstriktion). Denne begrundelse er dokumenteret i genbrugsevidensfakta for den tæt beslægtet "Hovedpineforstyrrelse"-kandidat (samme sygdomsenhedsfamilie, TxGNN-score 0.9955), hvor et pilot-RCT (PMID 21996647) direkte sammenlignede parecoxib med sumatriptan og rizatriptan i akutte migræneangreb.

Vigtigvis har denne specifikke "Migræneforstyrrelse"-indgang **nul direkte tilknyttede kliniske forsøg eller litteratur** — den mekanistiske sag hviler på indirekte forbindelse til den nabobeliggende "Hovedpineforstyrrelse"-klynge, ikke på evidens genereret for migræne selv.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

*Indirekte bemærkning: den relaterede "Hovedpineforstyrrelse"-kandidat lister 3 forsøg (NCT01930318, NCT03823846, NCT06623513), alle klassificeret som "C" relevans — ingen målretter migræne/hovedpine direkte; de involverer postoperativ eller periproceduralsmertesettinger.*

---

## Bevis fra litteratur

I øjeblikket ingen relateret litteratur tilgængelig.

*Indirekte bemærkning: PMID [21996647](https://pubmed.ncbi.nlm.nih.gov/21996647/) (2011, RCT, Clinical Neuropharmacology, Tier 1) — et pilotstudium sammenlignende IV parecoxib 40mg, SC sumatriptan og oral rizatriptan for akutte migræneangreb — er tilknyttet "Hovedpineforstyrrelse"-kandidaten, ikke direkte til denne "Migræneforstyrrelse"-indgang.*

---

## Markedsinformation for Danmark

Ikke markedsført i Danmark; 0 markedsføringstilladelser i øjeblikket registreret i denne Evidenspakke.

---

## Sikkerhedshensyn

Se venligst den godkendte Produktinformation (SmPC) for sikkerhedsinformation.

*(Vigtige advarsler, kontraindikationer og lægemiddelinteraktionsdata er alle markeret som datakløfter i denne Evidenspakke — DG001 er et blokering-alvorlighed-kløft: TFDA/label advarsler og kontraindikationer er uløst, hvilket forhindrer en S1-sikkerhedsforvurdering.)*

---

## Konklusion og næste trin

**Beslutning: Afventer**

**Begrundelse:**
- Den højest rangerede kandidat (Migræneforstyrrelse) har ingen direkte klinisk forsøgs- eller litteraturunderstøttelse; den mekanistiske sag hviler på indirekte forbindelse til en nabobeliggende sygdomsklynge og et enkelt lille pilot-RCT.
- Parecoxib er i øjeblikket ikke markedsført i Danmark (0 tilladelser), og et blokering-datakløft (label advarsler/kontraindikationer, DG001) forhindrer selv en indledende sikkerhedsvurdering.

**For at fortsætte er følgende nødvendigt:**
- Dansk/EU SmPC eller godkendt label — advarsler og kontraindikationer (løser DG001, blokering)
- Bekræftet dokumentation af mekanisme-for-handling og oprindelig godkendt indikation (løser DG002)
- Direkte kliniske forsøg eller litteratur, der evaluerer Parecoxib specifikt i migræne (ikke kun den tilstødende "Hovedpineforstyrrelse"-klynge)
- Vurdering af administrationsvej/præparationsforms egnethed til akut migrænebehandling (Parecoxibs kendt formulering er parenteral; egnethed til ambulant/selvadministreret migrænebehandling kræver vurdering)

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

