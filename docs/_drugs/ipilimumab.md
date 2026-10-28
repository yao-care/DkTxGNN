---
layout: default
title: Ipilimumab
parent: Kun modelforudsigelse (L5)
nav_order: 451
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-14
monitor_inn: "IPILIMUMAB"
predicted_indications: ["choroideremia"]
description: "Ipilimumab: forudsagt ny indikation Choroideremi (choroideremia) (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Ipilimumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **1** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

## Ipilimumab: Choroideremi (choroideremia)
{: .text-alpha }

## Resumé

Ipilimumab er et antistof, der blokerer CTLA-4, og som oprindeligt anvendes til behandling af metastatisk melanom. TxGNN-modellen forudsiger, at det kan være effektivt mod **choroideremi** (en arvelig nethindesygdom). Der er dog **ingen kliniske forsøg og ingen publikationer**, der understøtter denne forudsigelse, og der er ingen plausibel biologisk sammenhæng.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Choroideremi (choroideremia) |
| TxGNN-forudsigelsesscore | 0.9906 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de indsamlede data. Ipilimumab er dog kendt som et CTLA-4-blokerende antistof, der fjerner en hæmmende kontrol på T-celler og dermed forstærker immunsystemets angreb på tumorer. Denne mekanisme er veldokumenteret ved melanom.

Choroideremi er en arvelig degeneration af nethinden, forårsaget af funktionstabsmutationer i CHM-genet (REP1-mangel). Sygdommen er ikke drevet af en hæmmet immunrespons, og der er ingen kendt sammenhæng mellem CTLA-4-blokade og sygdommens patogenese. Tværtimod kan øget immunaktivering give risiko for øjenbetændelse (f.eks. uveitis), som er en kendt immunrelateret bivirkning.

Den høje TxGNN-score synes derfor at være et modelartefakt og ikke et troværdigt signal. Forudsigelsen optræder desuden to gange i modellens output og bør dedupliceres.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104713610 | Yervoy (Bristol-Myers Squibb Pharma EEIG) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Immunterapi (immuncheckpoint-hæmmer, anti-CTLA-4); ikke et konventionelt cytotoksisk middel |
| Risiko for myelosuppression | Ikke belyst i de indsamlede data; se produktresuméet (SmPC) |
| Emetogenicitet | Ikke belyst i de indsamlede data; se produktresuméet (SmPC) |
| Monitorering | Se produktresuméet (SmPC). Typisk følges leverfunktion, thyreoideafunktion og tegn på immunrelaterede bivirkninger |
| Håndtering og beskyttelse | Se produktresuméet (SmPC) for krav til håndtering og tilberedning |

---

## Sikkerhedsovervejelser

Oplysninger om advarsler og kontraindikationer fra produktresuméet er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

**Immunrelateret risiko ved denne indikation:** Immunaktivering kan give øjenbetændelse (f.eks. uveitis), hvilket er særligt uønsket hos patienter med en eksisterende nethindesygdom.

**Lægemiddelinteraktioner:** Der er identificeret 100 interaktioner, hvoraf de første 20 er gennemgået her.

- **Alvorlige (Major):** Antikoagulantia, herunder apixaban, betrixaban, bivalirudin, dalteparin, desirudin, edoxaban, argatroban og danaparoid.
- **Moderate:** Kortikosteroider (hydrocortison, triamcinolon, dexamethason, betamethason, budesonid, prednisolon, prednison), metronidazol, tinidazol, naltrexon, rosuvastatin og simvastatin.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen mangler enhver klinisk eller litteraturmæssig støtte (evidensniveau L5), og der er ingen plausibel mekanistisk sammenhæng mellem CTLA-4-blokade og choroideremi. Desuden er der en teoretisk risiko for øjenbetændelse.

**For at komme videre kræves:**
- Præklinisk eller mekanistisk dokumentation for en sammenhæng mellem CTLA-4-blokade og CHM/REP1-relateret nethindedegeneration, hvis forudsigelsen skal forfølges.
- Vurdering af øjensikkerhed (risiko for uveitis) hos patienter med arvelige nethindesygdomme.
- Hentning af advarsler og kontraindikationer fra produktresuméet (SmPC) samt data om virkningsmekanisme.
- Fjernelse af den dublerede forudsigelse i modellens output.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

