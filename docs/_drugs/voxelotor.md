---
layout: default
title: Voxelotor
parent: Kun modelforudsigelse (L5)
nav_order: 475
evidence_level: L5
indication_count: 10
---

# Voxelotor
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

# Voxelotor: Fra seglcellesygdom til arvelig trombocytopeni med normale blodplader

## Sammenfatning på en sætning

Voxelotor er en hemoglobin-iltaffinitet-modulator kendt for sin kliniske anvendelse til seglcellesygdom (denne oprindelige indikation er ikke bekræftet af strukturerede registerdata i denne pakke – se nedenstående note – men er beskrevet i den medfølgende mekanistiske rationale). TxGNN-modellen forudsiger potentiel effektivitet for **arvelig trombocytopeni med normale blodplader**, med en meget høj forudsigelsesscore (**99.58%**) men i øjeblikket **nul kliniske forsøg** og **nul publikationer**. Evidenspakkens egen analyse markerer denne forudsigelse som et sandsynligt knowledge-graph-clustering-artefakt snarere end et ægte farmakologisk signal.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Seglcellesygdom (udledt fra virkningsmekanisme-beskrivelse i evidensrationalet; ikke bekræftet af strukturerede regulatoriske data – se Datakløft DG002) |
| Forudsagt ny indikation | Arvelig trombocytopeni med normale blodplader |
| TxGNN forudsigelsesscore | 99.58% |
| Evidensniveau | L5 (modelforudsigelse alene, ingen kliniske forsøg eller litteratur) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvente |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanisme-data for voxelotor er formelt markeret som et **Datakløft (DG002, høj-sværhedsgrad)** i denne evidenspakke – ingen bekræftet DrugBank/SmPC-virkningsmekanisme-record blev hentet. Rationaleteksten, der ledsager TxGNN-forudsigelserne, beskriver imidlertid konsekvent voxelotor som en **hemoglobin-iltaffinitet-modulator, der hæmmer polymerisering af sickel-hemoglobin (HbS)**, hvilket er mekanismen bag dets kendte kliniske anvendelse til seglcellesygdom. Denne beskrivelse bør behandles som baggrundskontekst alene, ikke som bekræftede strukturerede data, indtil den er bekræftet via en ordentlig DrugBank/regulatorisk forespørgsel.

Den forudsagte nye indikation – arvelig trombocytopeni med normale blodplader – er en sjælden arveligt betinget blodplade-funktionsforstyrelse. Dens underliggende biologi involverer megakaryocyt-udvikling og blodplade-signaleringsveje, som er mekanistisk forskellig fra voxelotors røde-blodlegeme-målrettede, hemoglobin-polymeriserings-mekanisme. Evidenspakkens egen repurposing-rationale angiver eksplicit, at der er **ingen direkte biologisk forbindelse** mellem de to tilstande.

Bemærkelsesværdigt er fire af de fem forskellige sygdomme blandt de 10 bedste TxGNN-forudsigelser for voxelotor blodplade-relaterede eller trombocytopeni-tilstande, alle med score inden for et snævert bånd (0.9951–0.9958). Evidenspakkens forfattere tolker dette som en mulig **knowledge-graph-indlejring-cluster-effekt** snarere end et medicin-specifikt signal. En yderligere forvirrende faktor er noteret: patienter med seglcellesygdom præsenterer sig ofte med samtidig blodplade-antal-abnormaliteter (f.eks. på grund af milt-dysfunktion), hvilket kan have fået modellen til at lære en komorbiditets-association snarere end et ægte behandlings-forhold. I fuldstændig mangel på klinisk forsøgs- eller litteraturstøtte bør denne forudsigelse behandles som alene hypotese-genererende.

---

## Evidens fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret (søgninger på ClinicalTrials.gov og ICTRP for voxelotor mod denne indikation returnerede begge nul resultater).

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig (PubMed-søgning for voxelotor mod denne indikation returnerede nul resultater).

---

## Danmarks markedsinformation

Voxelotors markedsstatus i Danmark er registreret som **Ikke markedsført**, med **0** registrerede markedsføringstilladelser i datasættet. Ingen produktnavn, doseringsform eller godkendt indikations-information er derfor tilgængelig.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation. (Vigtige advarsler, kontraindikationer og stof-stof-vekselvirkningsdata er alle markeret som Datakløfter i denne evidenspakke; TFDA/regulatorisk etiket-information, der kræves til en fuldstændig sikkerhedsvurdering – Datakløft DG001, blokeringssværhedsgrad – er endnu ikke opnået.)

---

## Konklusion og næste skridt

**Beslutning: Afvente**

**Rationale:**
Dette er et L5, modelforudsigelse-alene-signal uden understøttende kliniske forsøg, ingen understøttende litteratur, og ingen bekræftet mekanistisk forbindelse – evidenspakkens egen analyse foreslår, at scoren kan afspejle et knowledge-graph-clustering-artefakt blandt blodplade-lidelse-knudepunkter snarere end et ægte medicin-sygdom-forhold. Voxelotor er også ikke markedsført i Danmark, og et blokeringssværhedsgrad sikkerhedsdatakløft forhindrer enhver foreløbig sikkerhedsvurdering.

**For at fortsætte er følgende nødvendig:**
- Regulatorisk etiket / SmPC sikkerhedsdata (advarsler, kontraindikationer, DDI) – i øjeblikket blokeringssværhedsgrad Datakløft (DG001)
- Bekræftet virkningsmekanisme-data fra DrugBank – i øjeblikket høj-sværhedsgrad Datakløft (DG002)
- Uafhængig bekræftelse af, at TxGNN-scoren ikke er et artefakt fra indlejringsrums-clustering blandt blodplade-lidelse-knudepunkter
- Præ-kliniske eller mekanistiske studier, der specifikt evaluerer enhver forbindelse mellem hemoglobin-polymeriserings-modulation og blodplade-lidelse-patofysiologi, før yderligere klinisk evaluering overvejes

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

