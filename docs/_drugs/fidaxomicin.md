---
layout: default
title: Fidaxomicin
parent: Kun modelforudsigelse (L5)
nav_order: 189
evidence_level: L5
indication_count: 10
---

# Fidaxomicin
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

# Fidaxomicin: Fra Clostridioides difficile-infektion til Staphylococcal Scalded Skin Syndrome

## Sammenfattelse i én sætning

Fidaxomicin er en snævert-spektret makrolid-antibiotikum godkendt i EU (markedsført som Dificlir) til behandling af *Clostridioides difficile*-associeret diarré (CDAD), der virker primært i gastrointestinal-systemet på grund af minimal systemisk absorption.
TxGNN-modellen forudsiger, at det kan være effektivt til **Staphylococcal Scalded Skin Syndrome (SSSS)**, sammen med flere andre gram-positive bakterielle og toksine-medierede infektioner, som den højest-rangerede nye indikation.
Der er dog **ingen kliniske forsøg og ingen offentliggjort litteratur**, der i øjeblikket understøtter nogen af disse forudsagte indikationer, og de mekanistiske beviser for translation til klinisk brug betragtes som svage.

---

## Kort oversigt

| Emne | Indhold |
|------|---------|
| Original indikation | *Clostridioides difficile*-associeret diarré (CDAD) |
| Forudsagt ny indikation | Staphylococcal Scalded Skin Syndrome |
| TxGNN-forudsigelsesscore | 99.71% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringsautoriseringer | 0 |
| Anbefalet beslutning | Vent |

---

## Hvorfor er denne forudsigelse rimelig?

Fidaxomicin udøver sin antibakteriell effekt ved selektivt at hæmme bakteriel RNA-polymerase — den samme mekanisme som rifamyciner, men binding til et særskilt sted. Dette giver potent aktivitet mod gram-positive anaerober, især *Clostridioides difficile*, med praktisk talt ingen systemisk absorption efter oral administration (biotilgængelighed <1%). Dets kliniske værdi ligger præcis i at opnå meget høje intestinale koncentrationer, mens man skåner det systemiske mikrobiom.

Staphylococcal Scalded Skin Syndrome (SSSS) forårsages af eksfoliativ-toksiner (ETA/ETB) produceret af *Staphylococcus aureus* — en gram-positiv patogen. TxGNN-modellen har sandsynligvis fanget denne taksonomiske overlapning gennem lighed mellem noder i knowledge graph'en: både *C. difficile* og *S. aureus* er gram-positive patogener, mod hvilke fidaxomicin har demonstrerbar *in vitro*-aktivitet. Den samme logik gælder for de øvrige top-rangerede indikationer (bullæus impetigo, impetigo og botulisme), som alle involverer gram-positive eller anærobe patogener inden for Clostridiales eller Staphylococcaceae-familierne.

Imidlertid bryder den mekanistiske forbindelse sammen på det farmakokinetiske niveau. SSSS og de andre forudsagte hud- og toksine-medierede infektioner kræver betydningsfulde systemiske lægemiddelkoncentrationer for at nå infektionssteder (hud, neuromuskulær junction, lunge), som fidaxomicin ikke kan give. Desuden er patologien i toksine-medierede sygdomme såsom SSSS og botulisme drevet af allerede frigivet toksiner; antibiotika-drab af bakterien spiller kun en understøttende rolle, og den primære behandling forbliver antitoksin-terapi eller systemisk anti-stafylokkok-præparater. TxGNN-modellens høje scores her afspejler strukturel lighed i knowledge graph'en — ikke klinisk translatabilitet.

---

## Klinisk forsøgsbevis

Der er ikke registreret kliniske forsøg for fidaxomicin i nogen af de forudsagte indikationer.

*Der er i øjeblikket ingen relaterede kliniske forsøg registreret.*

---

## Litteraturbevis

Ingen offentliggjort litteratur er blevet identificeret, der forbinder fidaxomicin til nogen af de forudsagte indikationer.

*Der er i øjeblikket ingen relateret litteratur tilgængelig.*

---

## Markedsinformation for Danmark

Fidaxomicin er **ikke registreret i Danmark** og har ingen markedsføringsautoriseringer hos Lægemiddelstyrelsen.

> **Bemærk:** Fidaxomicin er godkendt i Den Europæiske Union under centraliseret procedure som **Dificlir** (fidaxomicin 200 mg filmovertrukne tabletter; EU/1/11/736) til behandling af *C. difficile*-infektioner hos voksne og børn ≥6 måneder. Dette produkt markedsføres ikke i øjeblikket i Danmark. Danske læger, der ønsker adgang, skal forfølge en enkeltpatient- eller compassionate use-ordning.

---

## Sikkerhedshensyn

Sikkerhedsdata specifikt for den danske/EU-regulatoriske kontekst blev ikke hentet som del af denne evidenspakke. For fuldstændig sikkerhedsinformation — herunder advarsler, kontraindikationer og særlige populationer — konsulteres venligst:

> Venligst henvis til det godkendte Produktresumé (SmPC) for Dificlir tilgængeligt via [EMA produktsiden](https://www.ema.europa.eu/en/medicines/human/EPAR/dificlir) for sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Vent**

**Begrundelse:**
Alle fem forudsagte indikationer er udelukkende understøttet af TxGNN-modelforudsigelse (Bevisniveau L5), med nul kliniske forsøg og nul publikationer identificeret. Kritisk er farmakokinetisk profil af fidaxomicin — næsten-nul systemisk biotilgængelighed — som skaber en fundamental mekanistisk barriere for behandling af nogen infektion uden for gastrointestinal-lumen, hvilket dækker alle de forudsagte indikationer.

**Følgende ville være nødvendigt, før denne kandidat kunne gå videre:**

- **Farmakokinetisk revurdering:** Demonstrer, om nogen alternativ administrationsrute (fx topisk, inhaleret) kunne opnå terapeutisk relevante vævskoncentrationer på målstedet
- **In vitro susceptibiliteetsdata:** Bekræft fidaxomicin MIC-værdier for de specifikke involverede patogener (*S. aureus* ETA/ETB-producerende stammer, *C. botulinum*) under forhold relevant for den forudsagte indikation
- **Mekanismsfeasibility-studie:** Adressér, om toksine-medierede patologi i SSSS og botulisme kan være meningsfuldt ændret af bakteriel RNA-polymerase-hæmning efter toksinfrigivelse
- **MOA-dokumentation:** Indhent fuld DrugBank mekanismisk profil (i øjeblikket opført som datahuller) for at understøtte eller modsige knowledge graph-forudsigelser
- **SmPC / Regulatoriske data:** Indhent fuldstændig advarsel- og kontraindikationsdata fra det godkendte EU SmPC før nogen klinisk hypotese kan indgå sikkerhedsscreening (S1)

I betragtning af omfanget af det farmakokinetiske mismatch, **anbefales omformål af fidaxomicin til systemiske eller hudinfektion ikke som en nær-termet prioritet** uden en ny leveringsinnovation (fx nanopartikel-indkapslet topisk formulering). TxGNN-forudsigelserne her ser ud til at afspejle taksonomisk nærhed i knowledge graph'en snarere end en sand klinisk mulighed.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

