---
layout: default
title: Tenecteplase
parent: Kun modelforudsigelse (L5)
nav_order: 424
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: Fra Udokumenteret Original Indikation til Posterolateral Myokardieinfarkt

## Ét-sætnings Sammenfatning

Tenecteplase (DB00031) er en rekombinant vævsplasminogen-aktivator (TNK-tPA); dens oprindeligt godkendte indikation er ikke dokumenteret i dette bevismappe, og den har i øjeblikket **ingen markedsføringstilladelse i Danmark**. TxGNN-modellens toprangerede forudsigelse er **posterolateral myokardieinfarkt**, med en **99.87%** forudsigelsesscore, men denne specifikke kandidat understøttes af **nul kliniske forsøg og nul litteratur** i bevismappe — det hviler udelukkende på modelscoren.

---

## Hurtig Oversigt

| Element | Indhold |
|---------|---------|
| Original Indikation | Ikke dokumenteret — `taiwan_regulatory.licenses` er tom (ingen dansk MA på fil) og `original_indications` blev ikke udfyldt i denne pakke |
| Forudsagt Ny Indikation | Posterolateral Myokardieinfarkt |
| TxGNN Forudsigelsesscore | 99.87% |
| Bevisniveau | L5 (kun modelforudsigelse, ingen understøttende forsøg eller litteratur) |
| Danmarks Markedsstatus | Ikke markedsført |
| Antal Markedsføringstilladelser | 0 |
| Anbefalet Beslutning | Vent |

---

## Hvorfor er Denne Forudsigelse Rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige (markeret som et data-gap med høj alvorlighed, DG002). Baseret på lægemidlets kendte farmakologiske klasse er tenecteplase en genetisk konstrueret variant af vævsplasminogen-aktivator (TNK-tPA), der katalyserer omdannelsen af plasminogen til plasmin og opløser fibrin-koagula.

Posterolateral myokardieinfarkt er en anatomisk-lokaliseringsubtype af myokardieinfarkt, en tilstand, for hvilken trombolitiske midler i denne klasse er mekanistisk relevante. Bevismappens egen begrundelse for denne kandidat fremgår: denne subtype "er teoretisk konsistent med tenecteplases standard trombolitiske mekanisme, men intet forsøg eller litteratur i dette datasæt understøtter det direkte — kun TxGNN-scoren eksisterer — og det overlapper væsentligt med myokardieinfarkt som en generel tilstand, hvilket rejser muligheden for, at dette er en ontologi-niveau-duplet snarere end en genuint ny indikation."

Med andre ord er den mekanistiske plausibilitet høj, men denne plausibilitet afspejler sandsynligvis tenecteplases allerede etablerede relevans for myokardieinfarkt generelt, snarere end nye beviser specifikt for den posterolaterale subtype. Dette er grunden til, at bevismappen selv scorer denne kandidat L5 og anbefaler **Vent**.

*Bemærkning for kontekst: inden for samme bevismappe har en anden kandidat — **koronarstenos** (rank 9/10) — væsentligt stærkere støtte, inklusive en afsluttet fase 2-RCT (NCT00604695, lav-dosis intracoronar tenecteplase under primær PCI) og 12 litteraturtreff, der når bevisniveauet L2 med en "Fortsæt med sikkerhedsforanstaltninger"-anbefaling. Denne kandidat kan fortjene en separat evaluering.*

---

## Klinisk Forsøgsbevis

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Danmarks Markedsinformation

Tenecteplase har i øjeblikket ingen markedsføringstilladelse i Danmark — `total_licenses` er 0 og ingen licensrecords er på fil i denne bevismappe.

---

## Sikkerhedshensyn

Se venligst det godkendte produktinformationsblad (SmPC) for sikkerhedsinformation. (Vigtige advarsler, kontraindikationer og data om lægemiddelinteraktioner er alle markeret som datahuller i denne bevismappe; DDI-forespørgslen selv returnerede "not found".)

---

## Konklusion og Næste Trin

**Beslutning: Vent**

**Begrundelse:**
Denne kandidat har ingen direkte klinisk-forsøg eller litteraturstøtte i bevismappe — kun en TxGNN-modelscore — og den forudsagte indikation er anatomisk indlejret inden for myokardieinfarkt, en tilstand, der allerede er tæt forbundet med tenecteplases kendt trombolitiske mekanisme. Dette rejser meningsfuld risiko for, at den "nye indikation" er et ontologi-artefakt snarere end en genuine genbrugsmulighed, så det opfylder ikke kriteriet for at fortsætte.

**For at fortsætte er følgende nødvendigt:**
- Original indikation og virkningsmekanisme-data (DG002-remediation, via DrugBank API), for at etablere, om denne kandidat er virkelig forskellig fra tenecteplases eksisterende brug
- TFDA/SmPC-mærkat, advarsler og kontraindikationer (DG001-remediation, i øjeblikket blokeret) før en S1-sikkerhedsgennemgang kan påbegyndes
- Målrettet litteratur-/forsøgssøgning specifik for "posterolateral myokardieinfarkt" (modsat myokardieinfarkt generelt) for at bestemme, om denne subtype er blevet studeret uafhængigt
- Hvis der forfølges genbrugsforsøg på dette lægemiddel, overvej at prioritere kandidaten **koronarstenos** i stedet, som allerede har L2-niveau-evidens, inklusive en afsluttet fase 2-RCT (NCT00604695, lav-dosis intracoronar tenecteplase under primær PCI) og 12 litteraturtreff, der når bevisniveauet L2 med en "Fortsæt med sikkerhedsforanstaltninger"-anbefaling. Denne kandidat kan fortjene en separat evaluering.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

