---
layout: default
title: Benazepril
parent: Kun modelforudsigelse (L5)
nav_order: 101
evidence_level: L5
indication_count: 4
monitor_inn: "benazepril"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome"]
last_modified_at: 2026-11-24
description: "Benazepril: forudsagt ny indikation Malign hypertensiv nyresygdom (malignant hypertensive renal disease) (evidensniveau L5). I Danmark kun godkendt som veterinærlægemiddel"
---

# Benazepril
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

## Benazepril: ACE-hæmmer → malign hypertensiv nyresygdom (malignant hypertensive renal disease)
{: .text-alpha }

## Opsummering

Benazepril er en ACE-hæmmer. Ifølge de data, der er indsamlet til denne rapport, forudsiger TxGNN-modellen, at lægemidlet kan have effekt ved **malign hypertensiv nyresygdom (malignant hypertensive renal disease)**. Der er **ingen kliniske forsøg og ingen publikationer**, der direkte undersøger denne sygdom, så forudsigelsen står alene som modelresultat.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Malign hypertensiv nyresygdom (malignant hypertensive renal disease) |
| TxGNN-forudsigelsesscore | 0,9965 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Kun godkendt som veterinærlægemiddel |
| Antal markedsføringstilladelser | 0 (gyldige: 0) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Benazepril (uofficiel oversættelse): »Benazepril og benazeprilat hæmmer angiotensinkonverterende enzym (ACE) hos mennesker og dyr. Benazeprilat har langt større ACE-hæmmende aktivitet end benazepril. ACE er en peptidyldipeptidase, der katalyserer omdannelsen af angiotensin I til det vasokonstriktive stof angiotensin II.« Engelsk originaltekst: "Benazepril and benazeprilat inhibit angiotensin-converting enzyme (ACE) in human subjects and animals. Benazeprilat has much greater ACE inhibitory activity than does benazepril. ACE is a peptidyl dipeptidase that catalyzes the conversion of angiotensin I to the vasoconstrictor substance, angiotensin II." ([DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e), version af 2025-09-30; hentet 2026-11-19). Benazepril tilhører gruppen af ACE-hæmmere, som nedsætter dannelsen af angiotensin II. Det sænker blodtrykket og reducerer trykket i nyrens glomeruli, hvilket biologisk er plausibelt ved hypertensiv nyreskade.

Den høje score (0,9965) afspejler sandsynligvis, at sygdommen ligger tæt på lægemidlets kendte anvendelse ved forhøjet blodtryk i modellens datagrundlag. Det er ikke et bevis for klinisk effekt. Malign hypertension behandles desuden normalt akut med intravenøse midler. En oral ACE-hæmmer ville derfor højst få en rolle i langsigtet nyrebeskyttelse efter stabilisering, ikke som primær behandling.

---

## Dokumentation fra kliniske forsøg

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

<!-- licenses:begin -->

Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler indeholder ingen markedsføringstilladelser til humane lægemidler med dette aktive stof.

Dataene indeholder 15 tilladelser til veterinærlægemidler (ATC-kode Q eller »Vet.« i navnet).

<!-- licenses:end -->

Alle tre tilladelser er for veterinærlægemidler med benazepril som eneste aktive stof. De er ikke godkendt til human brug.

---

## Sikkerhedsovervejelser

Data om lægemiddelinteraktioner foreligger: der er registreret 207 interaktioner. Blandt de viste er alle af moderat grad, bl.a. med:

- **Antidiabetika:** insuliner (humant, aspart, degludec, detemir, glargin, glulisin, lispro), glimepirid, glipizid, glibenclamid, chlorpropamid, acetohexamid, alogliptin, dapagliflozin og exenatid
- **Øvrige:** hydrocortison og glycerin

Kombination med antidiabetika kan forstærke den blodsukkersænkende effekt, så blodsukkeret bør følges.

For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modellen (evidensniveau L5). Der foreligger ingen kliniske forsøg eller litteratur, som direkte undersøger malign hypertensiv nyresygdom. De tre fundne publikationer under andre forudsagte sygdomme er ikke relevante for benazepril.

**For at komme videre kræves:**
- Systematisk litteratursøgning efter ACE-hæmmere ved malign hypertensiv nefropati
- Data om virkningsmekanisme (MOA)
- Sikkerhedsoplysninger fra produktresuméet for humane præparater, da de danske tilladelser kun omfatter veterinærprodukter
- Vurdering af klinisk rolle (langtidsbeskyttelse af nyrerne efter akut stabilisering) af nefrologisk og kardiologisk ekspertise

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Lotensin (benazepril hydrochloride) prescribing information, Validus Pharmaceuticals LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=2abb091b-a53e-46b0-9b84-e5ee8f2bdd8e) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

