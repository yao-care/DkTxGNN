---
layout: default
title: Canagliflozin
parent: Kun modelforudsigelse (L5)
nav_order: 85
evidence_level: L5
indication_count: 0
---

# Canagliflozin
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **0** stk.
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

# Canagliflozin: Vurdering af lægemiddel til ny indikation – Bevismappe ufuldstændig

## Enlinjet sammendrag

Canagliflozin (DrugBank: DB08907) er en natrium-glukose kotransporter 2 (SGLT2)-inhibitor med etableret anvendelse til type 2-diabetes mellitus og kardiovaskulær/renal beskyttelse.
Den nuværende Bevismappe indeholder dog **ingen TxGNN-prognose indikationer**, og vigtige datafelter, herunder virkningsmekanisme, sikkerhedsadvarsler og godkendelsesoplysninger, mangler.
En fuldstændig vurdering kan ikke foretages på dette stadium; en **standse**-beslutning anbefales, indtil datakløfterne er løst.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke registreret i Bevismappe (kendt fra litteratur: Type 2-diabetes mellitus) |
| Prognose for ny indikation | Ingen – TxGNN-output ikke til stede i denne Bevismappe |
| TxGNN-prognose score | Ikke tilgængelig |
| Bevisniveau | L5 (modelprognosedata mangler; ingen understøttende undersøgelser linket i mappe) |
| Markedsstatus i Danmark | Ikke markedsført (per Bevismappe) |
| Antal godkendelser til markedsføring | 0 (per Bevismappe) |
| Anbefalet beslutning | **Standse** |

---

## Hvorfor er denne prognose rimelig?

Denne Bevismappe indeholder ingen TxGNN-prognose indikation, så en formel mekanistisk begrundelse, der forbinder den oprindelige indikation med en ny målindikation, kan ikke konstrueres.

Baseret på offentligt tilgængelig farmakologisk viden tilhører canagliflozin SGLT2-inhibitor-klassen. Det virker i nyrernes proximale tubul ved at blokere natrium-glukose kotransporter 2, hvorved glukosereabsorption reduceres og urinar glukoseudskillelse øges. Ud over blodsukkerkontrol har SGLT2-inhibitorer demonstreret natriuretiske og hæmodynamiske effekter med implikationer for hjertesvigt og kronisk nyresygdom – områder, der har tiltrukket betydelig interesse for lægemidler til ny indikation.

Indtil TxGNN-prognoseledningen køres igen, og Bevismappe regenereres med et gyldigt `predicted_indications`-array, kan ingen formel mekanistisk associeringsanalyse formelt gennemføres for denne kandidat.

---

## Kliniske forsøgsdata

Der er i øjeblikket ingen beslægtede kliniske forsøgsdata linket i denne Bevismappe.

> **Bemærk:** Dette afspejler fraværet af data i `predicted_indications`-feltet, ikke nødvendigvis fraværet af virkelighedsdata-forsøgsaktivitet for canagliflozin. Når først en målindikation er identificeret af TxGNN-modellen, skal en dedikeret bevisforespørgsel køres mod ClinicalTrials.gov og EU Clinical Trials Register (EudraCT / CTIS).

---

## Litteraturdata

Der er i øjeblikket ingen beslægtede litteraturkilder linket i denne Bevismappe.

> **Bemærk:** Som ovenfor er dette en konsekvens af manglende `predicted_indications`-data, ikke en afspejling af den samlede offentliggjorte litteratur for canagliflozin.

---

## Markedsoplysninger for Danmark

Per Bevismappe har canagliflozin **0 godkendelser til markedsføring** og er registreret som **ikke markedsført**.

> **Vigtig forbehold for anmeldere:** Denne Bevismappe blev genereret fra en regulatorisk datakilde, der muligvis ikke afspejler den nuværende danske/EMA-registreringsstatus. Canagliflozin-holdige produkter (f.eks. Invokana, Vokanamet) har EMA-centraliserede godkendelser til markedsføring, der er gyldige i Danmark. Anmeldere anbefales på det stærkest at bekræfte den nuværende status direkte via:
> - [EMA produktside](https://www.ema.europa.eu/en/medicines/human/EPAR/invokana)
> - [Laegemiddelstyrelsen (DKMA) produktdatabase](https://laegemiddelstyrelsen.dk/)

---

## Sikkerhedsovervejelser

Se det godkendte Sammenfattende produktkarakteristika (SmPC) for fuld sikkerhedsinformation, da der ikke findes sikkerhedsdata i denne Bevismappe.

> Følgende datakløfter er blevet markeret som kræver løsning, før nogen sikkerhedsbaseret vurdering kan fortsættes:
> - **TFDA-etiketadvarsler og kontraindikationer** (Alvorlighed: Blokering) – forhindrer indgang til sikkerhedsscreening fase 1
> - **Virkningsmekanisme-data** (Alvorlighed: Høj) – forhindrer mekanistisk relevansvurdering

---

## Konklusion og næste skridt

**Beslutning: Standse**

**Begrundelse:**
Bevismappe for canagliflozin (DB08907) er kritisk ufuldstændig: der findes ingen TxGNN-prognose indikationer, virkningsmekanisme-data mangler, og alle sikkerhedsfelter er tomme. Uden en prognose målindikation kan der ikke gennemføres en evidensbaseret vurdering af lægemidler til ny indikation, og der kan ikke fremstilles nogen anbefaling vedrørende klinisk udvikling.

**For at fortsætte er følgende nødvendig:**

- [ ] **Kør TxGNN-prognoseledningen igen** for DB08907 for at udfylde `predicted_indications` – dette er den vigtigste blocker
- [ ] **Hent virkningsmekanisme-data** fra DrugBank API for DB08907 (Datakløft DG002, alvorlighed: Høj)
- [ ] **Hent SmPC sikkerhedsdata**, herunder advarsler og kontraindikationer fra den danske/EMA-etiket (Datakløft DG001, alvorlighed: Blokering)
- [ ] **Bekræft markedsstatus i Danmark** mod EMA-centraliseret godkendelsesdatabase og DKMA produktregister, da Bevismappe-værdien "ikke markedsført" synes uoverensstemmende med kendt EMA-godkendelser
- [ ] **Regenerer Bevismappe** med fulde inddata, før en formel evaluering planlægges

---

*Denne rapport blev genereret fra Bevismappe `TW-DB08907-multi` (v4, dataafskæring 2026-04-04). På grund af kritiske datakløfter tjener dette dokument kun som en triagepost og udgør ikke en fuldstændig vurdering af lægemidler til ny indikation. Alle resultater er til forskningsreference og udgør ikke medicinsk rådgivning. Enhver kandidat til ny indikation kræver klinisk validering før anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

