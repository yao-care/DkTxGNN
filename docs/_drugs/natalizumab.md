---
layout: default
title: Natalizumab
parent: Kun modelforudsigelse (L5)
nav_order: 305
evidence_level: L5
indication_count: 10
---

# Natalizumab
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

# Natalizumab: Fra multipel sklerose til bronkitis

## Resumé i en sætning

Natalizumab er et monoklonalt antistof; bevissamlingen indeholder ikke bekræftede danske regulatoriske indikationsdata, men den understøttende litteratur identificerer konsekvent dets etablerede anvendelse som tilbagefaldende-remitterende multipel sklerose. TxGNN-modellen forudsiger en mulig ny indikation for **bronkitis**, men denne forudsigelse er i øjeblikket bakket op af **0 kliniske forsøg** og **0 publikationer** — det er et rent modeloutput uden understøttende kliniske eller mekanistiske beviser.

## Hurtig oversigt

| Emne | Indhold |
|------|--------|
| Oprindelig indikation | Ikke tilgængelig i regulatoriske data (`taiwan_regulatory.licenses` er tom); litteraturorammen (se evidenscitater nedenfor) angiver anvendelse for tilbagefaldende-remitterende multipel sklerose |
| Forudsagt ny indikation | Bronkitis |
| TxGNN-forudsigelsesscore | 99.46% |
| Bevisniveau | L5 (kun modelforudsigelse, ingen kliniske forsøg eller litteratur) |
| Danmarks markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Vent |

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanisme-data er ikke tilgængelige for natalizumab i denne bevissamling (markeret som datamangel med høj alvorlighetsgrad). Baseret på kendt farmakologi, der er refereret på tværs af den understøttende litteratur, er natalizumab et monoklonalt antistof mod α4-integrin (VLA-4), der blokerer leukocyt-migration på tværs af blod-hjerne-barrieren og tarmslimhinden, brugt i behandlingen af tilbagefaldende-remitterende multipel sklerose.

For den højest rangerede kandidat, **bronkitis**, gives der ingen mekanistisk eller klinisk begrundelse i bevissamlingen. Bronkitis er overvejende en infektionsmæssig/irriterende luftvejstilstand, og der er ingen etableret patofysiologisk forbindelse til α4-integrin-blokering. Hvis noget, ville natalizumabs systemiske immunosuppressive virkning forventes at *øge* modtageligheden for luftvejsinfektioner snarere end at behandle det — bevisretningen går imod repurposing-hypotesen.

Det er også værd at bemærke, at flere lavere-rangerede kandidater i denne bevissamling (parapsoriasis, psoriasis, akut lichenoid pityriasis) returnerede litteraturtreff, men næsten alle af disse beskriver, at natalizumab **inducerer eller forværrer** disse hudsygdomme som uønskede lægemiddelreaktioner (f.eks. PMID 30323758, PMID 35646438, PMID 23096069), ikke behandling af dem. Kun en rapport (PMID 33589543) beskriver komorbid psoriasis, der forbedres under natalizumab-behandling. Dette mønster — høje TxGNN-lighedsscore forbundet med litteratur, der peger på skade snarere end gavnlige effekter — svækker yderligere tilliden til modellens dermatologiske og respiratoriske forudsigelser for dette lægemiddel og understøtter en forsigtig, bevisførste tilgang før nogen repurposing-overvejelse.

## Klinisk forsøgsbeviser

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

## Litteraturbeviser

I øjeblikket er der ingen relateret litteratur tilgængelig for bronkitis-indikationen specifikt.

## Danmarks markedsinformation

Der er i øjeblikket ingen markedsføringstilladelser i arkiverne for natalizumab i Danmark i denne bevissamling (`total_licenses: 0`, markedsstatus: ikke markedsført).

## Sikkerhedshensyn

Se venligst det godkendte Produktinformationsdokument (SmPC) for sikkerhedsinformation — strukturerede advarsler, kontraindikationer og DDI-data er ikke tilgængelige i denne bevissamling (`[Data Gap]` for alle tre felter; DDI-søgning returnerede ingen resultater).

**Litteratursignal (supplerende, ikke fra strukturerede sikkerhedsdata):** En væsentlig andel af den litteratur, der er dukket op på tværs af dette lægemiddels kandidatindikationer, vedrører progressiv multifokal leukoencefalopati (PML), en alvorlig JC-virus-relateret CNS-komplikation forbundet med natalizumab (f.eks. PMID 20298966, 19647202, 24136456, 30324046, 36283150, 22082208). Selvom disse data blev hentet i sammenhæng med søgninger efter ikke-relaterede sygdomsforudsigelser snarere end en formel sikkerhedsforespørgsel, er det et klinisk væsentligt signal, som enhver gennemganger bør være klar over før yderligere evaluering.

## Konklusion og næste trin

**Beslutning: Vent**

**Begrundelse:**
Den højest rangerede forudsagt indikation (bronkitis) har nul støttende kliniske forsøg eller litteratur (Bevisniveau L5), ingen troværdig mekanistisk forbindelse, og lægemidlet er i øjeblikket ikke markedsført i Danmark. Relaterede dermatologiske kandidater i samme bevissamling viser litteraturevidence, der peger på uønskede lægemiddelreaktioner snarere end terapeutisk nytte, hvilket bekræfter, at denne bevissamling ikke i øjeblikket støtter progression.

**For at fortsætte er følgende nødvendigt:**
- Bekræftet oprindelig indikation og godkendt SmPC-tekst (i øjeblikket ikke tilgængelig — regulatoriske licensdata er tomme)
- Virkningsmekanisme-detaljer fra DrugBank eller SmPC (DG002)
- TFDA/Danske Lægemiddelstyrelse labeladvarsler og kontraindikationer (DG001, Blocking)
- Enhver preklinisk eller mekanistisk begrundelse, der specifikt forbinder α4-integrin-blokering til bronkitis-patofysiologi
- Revurdering hvis fremtidige kliniske forsøg eller litteratur specifik for bronkitis dukker op

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

