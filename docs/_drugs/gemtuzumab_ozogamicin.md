---
layout: default
title: Gemtuzumab Ozogamicin
parent: Kun modelforudsigelse (L5)
nav_order: 208
evidence_level: L5
indication_count: 0
---

# Gemtuzumab Ozogamicin
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

# Gemtuzumab ozogamicin: Genenbrugsvurdering blokeret — Datahuller kræver løsning

---

## Ét-linjes opsummering

Gemtuzumab ozogamicin (DrugBank ID: DB00056) blev identificeret i pipelinen, men kunne ikke vurderes for genenbrugspotentiale i denne cyklus. TxGNN-modellen genererede ingen forudsagte indicationer, da to opstrøms datahuller — manglende reguleringsmæssige etikettata og manglende virkningsmekanisme — forhindrede forudsigelsespipelinen i at køre. Denne rapport dokumenterer hullerne og definerer de iværksætningstrin, der kræves, før vurderingen kan fortsætte.

---

## Hurtig oversigt

| Post | Indhold |
|------|----------|
| Oprindelig indikation | Ikke tilgængelig |
| Forudsagt ny indikation | Ingen forudsigelse genereret |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Bevisniveau | L5 — kun modelforudsigelse, uden understøttende studier |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Afvent** |

---

## Hvorfor kunne der ikke genereres nogen forudsigelse?

TxGNN-genenbrugspipelinen kræver to inputter for at fungere: en bekræftet virkningsmekanisme (for at lokalisere lægemiddel-noden i vidensgrafen) og mindst en godkendt indikation (for at etablere lægemidlets eksisterende sygdomsassociationer).

For gemtuzumab ozogamicin er begge inputter fraværende i den aktuelle Evidenspakke. MOA-feltet blev ikke udfyldt fra DrugBank (DG002), og der blev ikke hentet data om oprindelige indikationer (DG001 — ingen reguleringsmæssig etiket). Uden disse ankerpunkter kan vidensgrafen ikke placere lægemidlet i sin korrekte terapeutiske kontekst, og forudsigelsesmodellen kan ikke producere meningsfuldt output.

Fra INN-suffikskonventionen betegner "-ozogamicin" et calicheamicin-konjugeret antistof-lægemiddel-konjugat (ADC). Denne navngivningskonvention placerer gemtuzumab ozogamicin inden for klassen af cytotoksiske antineoplastiske lægemidler. Dette strukturelle slutningsresultat udledt fra INN-suffikset alene er dog ikke tilstrækkeligt til at drive TxGNN-forudsigelsen — bekræftede indikatie- og MOA-data skal indlæses først. Når disse datahuller er løst, bør pipelinen køres igen.

---

## Cytotoksicitet

> Dette afsnit er inkluderet, fordi INN-suffikset "-ozogamicin" identificerer denne forbindelse som et calicheamicin-konjugeret antistof-lægemiddel-konjugat — en kendt cytotoksisk antineoplastisk klasse.

| Post | Indhold |
|------|----------|
| Cytotoksicitetsklassificering | Antistof-lægemiddel-konjugat (ADC) — calicheamicin-konjugat (udledt fra INN-suffiks; bekræftelse fra DrugBank/SmPC påkrævet) |
| Myelosuppressionsrisiko | Se venligst det godkendte sammendrag af produktets karakteristika (SmPC) — calicheamicin-ADCer er typisk forbundet med betydelig hæmatologisk toksicitet |
| Emetogenicitetsklassificering | Se venligst SmPC'en |
| Overvågningspunkter | Se venligst SmPC'en — omfatter typisk fuldstændig blodprocent (CBC med differentiering), leverprøver og overvågning af hepatisk veno-oklusiv sygdom |
| Håndteringsbeskyttelse | Skal følge bestemmelser om håndtering af cytotoksiske lægemidler — behandles som cytotoksisk, indtil SmPC bekræfter andet |

---

## Sikkerhedshensyn

Se venligst det godkendte sammendrag af produktets karakteristika (SmPC) for sikkerhedsinformation.

Der var ingen vigtige advarsler, kontraindikationer eller lægemiddelinteraktionsdata tilgængelige i denne Evidenspakke. Alle sikkerhedsfelter returnerades som huller (DG001). Hentning af den reguleringsmæssige etiket er klassificeret som et blokerende datahul, før der kan iværksættes nogen sikkerhedsscreening.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
To datahuller — et klassificeret som Blokering (DG001: reguleringsmæssig etiket) og et som høj alvorlighed (DG002: MOA) — forhindrer TxGNN-forudsigelsespipelinen i at generere noget output. Indtil disse er løst, kan intet genenbrugssignal vurderes, og ingen sikkerhedsscreening kan gennemføres.

**For at fortsætte er følgende nødvendigt:**

- **[DG001 — Blokering]** Hent produktetiketten (SmPC) fra Laegemiddelstyrelsen eller EMA's centraliserede database. Bemærk: gemtuzumab ozogamicin kan have en centraliseret EMA-godkendelse (Mylotarg®, Pfizer); resultatet med 0 licenser i den aktuelle Evidenspakke skal verificeres mod EMA's produktregister, før man konkluderer, at lægemidlet ikke er til stede på det danske marked.
- **[DG002 — Høj]** Forespørg DrugBank API'en (DB00056) for at udfylde virkningsmekanisme-feltet — specifikt antistofmålet og den cytotoksiske nyttelast-forbindelse.
- **Kør forudsigelsespipelinen igen** efter at begge felter er udfyldt, og generer en ny Evidenspakke-version.
- **Bekræft markedsstatus** ved at krydstjekke Laegemiddelstyrelsen og EMA's EPAR-database for eventuelle aktive eller historiske centraliserede markedsføringstilladelser, der dækker Danmark.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

