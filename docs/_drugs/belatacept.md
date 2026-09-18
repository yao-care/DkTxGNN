---
layout: default
title: Belatacept
parent: Kun modelforudsigelse (L5)
nav_order: 58
evidence_level: L5
indication_count: 0
---

# Belatacept
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

# Belatacept: Forebyggelse af abstodsning efter nyreftransplantation — Ingen forudsigelser for lægemidlets nye indikationer tilgængelige

## Sammenfatning

Belatacept (DrugBank ID: DB06681) er en selektiv T-celle-kostimulatorblokkeder godkendt internationalt under mærkenavnet **Nulojix** til forebyggelse af akut afstødning hos voksne patienter efter nyreftransplantation.
**TxGNN-modellen genererede ingen forudsigelser for nye indikationer** for denne kandidat i nuværende køring, og lægemidlet har ingen registrerede markedsautoriseringer i Danmark.
Kritiske datahul – herunder oplysninger om virkningsmekanisme og formelle sikkerhedsdata – skal løses, før en fuldstændig evaluering kan påbegyndes.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Forebyggelse af akut afstødning hos voksne patienter efter nyreftransplantation (international godkendelse; ingen dansk MA på fil) |
| Forudsagt ny indikation | Ingen forudsigelser genereret |
| TxGNN forudsigelsesscore | N/A |
| Bevisniveau | N/A — Ingen forudsigelser tilgængelige |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsautoriseringer | 0 |
| Anbefalet afgørelse | Afventer |

---

## Hvorfor der blev genereret ingen forudsigelser

TxGNN-pipelinen identificerede med succes Belatacept i DrugBank (query log entry 2, status: `success`), men returnerede nul omdestinerings-kandidat-indikationer. Dette skyldes sandsynligvis en eller flere af følgende:

1. **Tærskelfiltrering for score**: Alle kandidat-sygdoms–lægemiddel-associationsscorer kan være faldet under minimumsværdien i denne forudsigelseskørsel.
2. **Dækning af vidensgrafen for biologiske lægemidler**: Belatacept er et stort fusionsprotein (CTLA-4-Ig), ikke et småmolekyle-lægemiddel. TxGNN-vidensgrafen har historisk færre mekanistiske kanter for biologiske lægemidler, hvilket kan forværre embedding-kvaliteten og reducere forudsagte scorer.
3. **Manglende MOA-data (DG002)**: Uden oplysninger om virkningsmekanisme i grafen er lægemiddelknuden dårligt forbundet, hvilket reducerer rækkevidde af grafbaseret inferens.

En omkørsel efter løsning af datahul DG001 og DG002 – eller med en slækket score-tærskel – kan give kandidat-forudsigelser i en fremtidig cyklus.

---

## Lægemidlets baggrund

Selvom oplysninger om virkningsmekanisme mangler fra Evidence Pack, er Belatacept en velkarakteriseret biologisk agens i international litteratur:

- **Klasse**: Fusionsprotein (CTLA-4-Ig); selektiv T-celle-kostimulatorblokkeder
- **Mekanisme**: Binder CD80 og CD86 på antigen-præsenterende celler, blokerer CD28-kostimuleringssignalet, der er påkrævet for fuldstændig T-celle-aktivering — og undertryker derved alloimmunsvar uden calcineurin-hæmning
- **International godkendelse**: EMA-centraliseret autorisation som **Nulojix** (EU/1/11/694) til forebyggelse af akut afstødning hos voksne nyre-transplanterede; FDA-godkendt siden 2011
- **Administrationsvej**: Intravenøs infusion (hospital-/specialistindstilling)

Kostimuleringsblokkade-mekanismen er biologisk plausibel for indikationer ud over nyre-transplantation — for eksempel andre solid-organ-transplantationer, graft-versus-host-sygdom og visse autoimmun-sygdomme. Imidlertid er der ingen formelle TxGNN-forudsigelser tilgængelige på nuværende tidspunkt, og ingen omdestinerings-anbefaling kan derfor gives.

---

## Markedsinformation for Danmark

Der er ingen markedsautoriseringer for Belatacept registreret i nuværende datasæt for Danmark. Selvom den EMA-centraliserede autorisation for Nulojix er gyldig på tværs af alle EU-medlemsstater, afspejler Evidence Pack, at produktet ikke aktivt markedsføres i Danmark.

| Element | Status |
|---------|--------|
| Nationalt MA (Laegemiddelstyrelsen) | Ingen på fil |
| EMA-centraliseret MA (Nulojix, EU/1/11/694) | Ikke afspejlet i nuværende datasæt — verificer direkte hos EMA |
| Markedsstatus | Ikke markedsført |

Sundhedspersonale, der ønsker adgang i Danmark, bør kontakte Laegemiddelstyrelsen vedrørende named-patient eller hospital-import-programmer.

---

## Sikkerhedshensyn

Der er ingen sikkerhedsdata tilgængelige i nuværende Evidence Pack. Se venligst det godkendte Produktinformationsark (SmPC) for Nulojix for fuldstændig sikkerhedsinformation.

> **Bemærkning for ordinerende læger**: Publicerede internationale SmPCer for Nulojix indeholder en fremtrædende advarsel vedrørende **post-transplantat-lymfoprotliferativ lidelse (PTLD)** — med øget risiko hos EBV-seronegative patienter — og øget modtagelighed over for alvorlige infektioner, herunder progressiv multifokal leukoencefalopatologi (PML). Disse informationer formidles her udelukkende til kontekstuel bevidsthed; det danske SmPC bør konsulteres for lokalt godkendt ordinationsinformation.

---

## Konklusion og næste trin

**Afgørelse: Afventer**

**Begrundelse:**
Der blev genereret ingen TxGNN-forudsigelser for Belatacept i denne køring, og de to blokerende/høj-severity datahul (DG001, DG002) forhindrer selv en foreløbig sikkerhed- og mekanisme-vurdering. Procedering til klinisk evaluering uden forudsigelser eller sikkerhedsdata er ikke berettiget på dette stadium.

**For at kunne fortsætte kræves følgende:**

- **Løs DG002 (Høj)**: Hent fuld MOA- og måldata fra DrugBank-API'en for at forbedre vidensgraf-dækning og muliggøre en forudsigelse-omkørsel
- **Løs DG001 (Blokerend)**: Hent det EMA SmPC for Nulojix (eller lokalt dansk ækvivalent) for at udfylde advarsler, kontraindikationer og DDI-data
- **Omkør TxGNN-forudsigelse**: Efter løsning af datahul, omkør med standard-tærskel; overvej en sensitivitets-omkørsel ved en slækket tærskel for at vurdere, om der findes nogle grænse-kandidater
- **Bekræft dansk markedsstatus**: Kontakt Laegemiddelstyrelsen eller tjek EMA-produktsiden for at bekræfte, om Nulojix er tilgængelig via noget access-program i Danmark
- **Vurder biologisk-specifik vidensgraf-dækning**: Hvis omkørsel stadig ikke giver forudsigelser, eskalér til TxGNN-modelleringsteamet for at gennemgå kant-tæthed i vidensgrafen for biologiske lægemidler

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

