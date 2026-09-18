---
layout: default
title: Tipranavir
parent: Kun modelforudsigelse (L5)
nav_order: 436
evidence_level: L5
indication_count: 10
---

# Tipranavir
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

# Tipranavir: Fra HIV-1-infektion til Simian Immunodeficiency Virus-infektion

## Samlet opsummering i én sætning

Tipranavir er en non-peptidisk HIV-1-proteasehæmmer, som historisk set har været brugt i antiretroviral terapi til behandlingserfarne patienter med multiresistent HIV-1-infektion (denne forbindelse til den oprindelige indikation er udledt fra evidence pack'ets interne begrundelsesnoter, da formelle indikations-/licenstekster ikke er tilgængelige). TxGNN-modellens højest rangerede forudsigelse er **Simian Immunodeficiency Virus (SIV)-infektion**, en dyremodelsygdom med en **99.99% forudsigelsesscore**, men **nul understøttende kliniske forsøg eller litteratur**. Evidence pack'ets egen analyse flagrer dette som en høj-score/lav-klinisk-værdi forudsigelse drevet af lentivirusfamiliens semantiske lighed, ikke et ægte genbrugssignal.

---

## Hurtig oversigt

| Element | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i formelle licensdata (0 danske autorisationer); ifølge interne begrundelsesnoter er tipranavir en non-peptidisk HIV-1-proteasehæmmer brugt i antiretroviral terapi |
| Forudsagt ny indikation | Simian Immunodeficiency Virus (SIV)-infektion |
| TxGNN-forudsigelsesscore | 99.99% |
| Evidensniveau | L5 (modelforsigelse kun, ingen klinisk eller litteraturstøtte) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringsautoriseringer | 0 |
| Anbefalet beslutning | Afvente |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme for tipranavir er markeret som et datagap på lægemiddelniveau. Evidence pack'ets egen genbrugsbegrundelsestekst identificerer dog tipranavir som en non-peptidisk HIV-1-proteasehæmmer, der virker ved at blokere det virale proteasenzym, som er påkrævet for modning af infektiøse virale partikler.

Den højest rangerede forudsigelse, SIV-infektion, er eksplicit flagret i evidence pack'et som et output med lav klinisk værdi: SIV er en primatmodellevirus i samme *Lentivirus*-slægt som HIV, så proteasehæmmingsmekanismen er teoretisk overførbar — men SIV-infektion er en dyresygdom, ikke en menneskelig klinisk indikation, og der findes ingen forsøg eller litteraturbevis, der understøtter det. Det samme mønster gentager sig for de næste få rangerede forudsigelser (felint immunodeficiensyndrom — endnu en dyresygdom; en sjælden neuroudviklingsforstyrrelse uden kendt mekanistisk forbindelse; og en forældet hyperlipidemibetegnelse, der faktisk modsiger tipranavirs kendt dyslipidemi-bivirkningsprofil). Evidence pack'et karakteriserer disse som modelstøj fra semantisk klyngning omkring "retroviral infektion" snarere end ægte genbrugskandidater.

Inden for denne pakke når de eneste forudsigelser til et avanceret internt beslutningsstadium (S1, "Forskningsspørgsmål") **AIDS-relateret kompleks** (rang 9) og **medfødt HIV-infektion** (rang 10) — som begge repræsenterer en udvidelse af tipranavirs allerede etablerede antiretrovirale mekanisme langs HIV-sygdomsspekteret, snarere end en ny genbrugshypotese. Medfødt HIV-infektion understøttes endvidere af 9 identificerede kliniske forsøg, selvom de fleste vedrører andre antiretrovirale regimer snarere end tipranavir specifikt (se nedenfor).

---

## Klinisk forsøgsbeviser

For den højest rangerede forudsigelse (SIV-infektion): i øjeblikket ingen relaterede kliniske forsøg registreret.

*Kontekstnotat: andre steder i denne evidence pack blev 9 kliniske forsøg identificeret under den lavere rangerede "medfødt HIV-infektion"-forudsigelse (L4/S1, pack'ets mest avancerede kandidat). Kun ét (NCT00042289, IMPAACT P1026s — antiretroviral farmakokinetik i graviditet/postpartum) er klassificeret som relevansgrad B; de resterende 8 er klassificeret som C, da de evaluerer andre antiretrovirale regimer (dolutegravir, cabotegravir/rilpivirine osv.) snarere end tipranavir direkte. Ingen tester specifikt tipranavir.*

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Ingen markedsføringsautoriseringer er registreret for tipranavir i denne evidence pack (0 autorisationer; markedsstatus: Ikke markedsført).

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

*Bemærk: indhentelse af TFDA/lokale etiketsadvarsler og kontraindikationer er flagret i denne evidence pack som et **blokerende** datagap (DG001) — sikkerhedsdata skal være indhentet, før denne kandidat kan undergå formel sikkerhedspre-vurdering (S1).*

---

## Konklusion og næste trin

**Beslutning: Afvente**

**Begrundelse:**
Den højest TxGNN-rangerede forudsigelse (SIV-infektion) er en dyresygdom med L5-bevis — modelforsigelse kun, ingen kliniske forsøg, ingen litteratur og ingen plausibel klinisk udviklingsvej. Lægemidlet har heller ingen markedsføringsautoriserering i Danmark og mangler virkningsmekanisme- og SmPC-sikkerhedsdata, hvilket blokerer enhver formel sikkerhedspre-vurdering.

**For at fortsætte er følgende nødvendig:**
- Lokalt SmPC/regulatorisk etiket (advarsler, kontraindikationer) — i øjeblikket et blokerende datagap
- Bekræftet virkningsmekanisme-dokumentation
- Hvis genbrugsforsøg forfølges yderligere, skal fokus omdirigeres væk fra de højest rangerede dyremodels-forudsigelser mod pack'ets mere klinisk begrundede kandidater — AIDS-relateret kompleks og medfødt HIV-infektion (begge L4/S1) — og søge tipranavir-specifikt forsøgs- eller litteraturbevis for disse indikationer

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

