---
layout: default
title: Sonidegib
parent: Kun modelforudsigelse (L5)
nav_order: 404
evidence_level: L5
indication_count: 10
---

# Sonidegib
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

# Sonidegib: Fra basalcellekarcinom til medulloblastom med omfattende nodulitet

## Sammenfatning i en sætning

Sonidegib er en Smoothened (SMO)-antagonist omtalt i denne bevismappe i sammenhæng med behandling af basalcellekarcinom (BCC) (dets strukturerede "original indication"-felt er i sig selv et datahul). TxGNN-modellen forudsiger en **99.90%** score for **medulloblastom med omfattende nodulitet**, en Hedgehog-pathway-drevet pediastrisk hjernekræft-subtype — men denne bevismappe indeholder **nul registrerede kliniske forsøg og nul indekserede publikationer** for det specifikke lægemiddel-sygdom-par.

## Hurtig oversigt

| Post | Indhold |
|------|---------|
| Original indikation | Ikke tilgængelig i struktureret lægemiddelrekord (datahul); omtalt kun indirekte som basalcellekarcinom (BCC) inden for omformål-rationalet |
| Forudsagt ny indikation | Medulloblastom med omfattende nodulitet |
| TxGNN-forudsigelsesscore | 99.90% |
| Bevisniveau | L5 (se forbehold nedenfor) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

**Forbehold vedrørende bevisniveau/beslutning:** pakkens interne scoringsfelt mærker denne kandidat som `L2` / `S2` / "Fortsæt med sikkerhedsforanstaltninger," men dets egne `evidence.clinical_trials` og `evidence.literature` arrays for denne indikation er tomme, og rationalet-teksten angiver eksplicit, at tællefelterne er 0. Hvis man anvender bevis-niveau-reglen bogstaveligt (baseret på faktiske kliniske forsøgs- og litteraturtællinger, ikke det interne mærkat) gives **L5 — modelforudsigelse alene, ingen faktiske studier**. Kombineret med et blokering-alvorligheds datahul (manglende TFDA/SmPC-mærkatdata, hvilket betyder, at sikkerhed-forvurdering ikke engang kan begynde), anbefaler denne rapport **Hold** i stedet for pakkens interne "Fortsæt med sikkerhedsforanstaltninger."

## Hvorfor er denne forudsigelse fornuftig?

Sonidegib er en Smoothened (SMO)-antagonist, der selektivt inhiberer Hedgehog-signalvejen. Denne virkningsmekanisme-detalje kommer fra omformål-rationalet, da lægemidlets eget `original_moa`-felt er et datahul.

SHH-aktiveret medulloblastom — inklusive subtypen "omfattende nodulitet" — er en pediastrisk hjernekræft kendt for at være drevet af aberrant aktivering af Hedgehog-vejen. Mekanistisk set er dette en af de mest direkte forbindelser på hele kandidatlisten: SMO-inhibering bør i princippet virke på den samme driver-vej, der ligger til grund for denne tumorsubtype, på samme måde som den gør i Hedgehog-vej-drevet BCC.

Som kontekst viser pakken også fire andre forudsagte indikationer (xeroderma pigmentosum, annular epidermolytic ichthyosis, epidermolysis bullosa simplex with mottled pigmentation, trichothiodystrophy photosensitive) med tilsvarende høje TxGNN-scorer. Pakkens egen rationale flagget disse som sandsynlige artefakter af knowledge-graph-clustering omkring "sjælden fotosensitiv/genetisk hudsygdom" — ingen har en plausibel Hedgehog-vej-mekanisme, og alle er markeret `Hold`. Dette gør medulloblastom til den eneste mekanistisk troværdige kandidat blandt de ti poster, selvom det på nuværende tidspunkt mangler nogen understøttende klinisk forsøgs- eller litteraturrekord i denne pakke.

## Bevis fra kliniske forsøg

Ingen relaterede kliniske forsøg er i øjeblikket registreret.

## Litteraturbevis

Ingen relateret litteratur er i øjeblikket tilgængelig.

## Markedsinformation for Danmark

Sonidegib har **ingen markedsføringstilladelse i Danmark** (0 licenser på fil; markedsstatus: ikke markedsført). Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) tilladelsesdokumenter er til stede i denne bevismappe.

## Cytotoksicitet

Sonidegib er et antineoplastisk middel (Hedgehog-vej-inhibitor brugt inden for onkologi), så denne sektion er relevant.

| Post | Indhold |
|------|---------|
| Cytotoksicitetsklassificering | Målrettet terapi (SMO/Hedgehog-vej-inhibitor) — ikke et konventionelt cytotoksisk middel |
| Risiko for myelosuppression | Se venligst Produktresumé (SmPC) for advarsler og forholdsregler |
| Emetogenicitetsklassificering | Se venligst Produktresumé (SmPC) for advarsler og forholdsregler |
| Overvågningsposter | Se venligst Produktresumé (SmPC) for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se venligst Produktresumé (SmPC) for advarsler og forholdsregler |

## Sikkerhedsovervejelser

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformation. Ingen vigtige advarsler, kontraindikationer eller lægemiddel-lægemiddel-vekselvirkning-data er tilgængelige i denne bevismappe — DDI-forespørgslen returnerede ingen resultater, og TFDA/SmPC-mærkatdata-posten er flagget som et blokering-datahul (`DG001`), hvilket betyder, at en Stage-1 sikkerhed-forvurdering i øjeblikket ikke kan udføres.

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
- Et blokering-alvorligheds datahul (manglende TFDA/SmPC-mærkatdata) forhindrer enhver Stage-1 sikkerhed-forvurdering, uanset styrken af den mekanistiske begrundelse.
- På trods af en mekanistisk troværdig forbindelse (SMO-inhibering → SHH-drevet medulloblastom), indeholder denne bevismappe nul kliniske forsøg og nul publikationer for dette specifikke lægemiddel-sygdom-par — faktisk bevisniveau er L5, ikke pakkens interne L2-mærkat.
- Sonidegib har ingen markedsføringstilladelse i Danmark, så der er ingen eksisterende regulatorisk eller forsyningsvej at bygge på.

**For at fortsætte kræves følgende:**
- TFDA/SmPC mærkatdata (advarsler, kontraindikationer) for at lukke blokering-datahullet
- Bekræftet original indikation og MOA-data for lægemiddelrekorden (i øjeblikket begge datahul)
- En målrettet litteratur- og forsøgs-søgning specifikt for sonidegib i SHH-aktiveret medulloblastom (f.eks. pediastrisk hjernekræft-consortium-studier), da ingen dukkede op i de automatiske forespørgsler logget her
- Vurdering af administrationsvej/doseringsform-kompatibilitet for den pediastriske population typisk påvirket af denne tumorsubtype (i øjeblikket markeret "afventende" uden data)
- Fuldt DDI-profil (nuværende forespørgsel gav ingen resultater)

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

