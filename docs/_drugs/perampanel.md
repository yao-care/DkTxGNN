---
layout: default
title: Perampanel
parent: Kun modelforudsigelse (L5)
nav_order: 647
evidence_level: L5
indication_count: 1
monitor_inn: "PERAMPANEL"
predicted_indications: ["beta-ketothiolase deficiency"]
last_modified_at: 2026-11-24
description: "Perampanel: forudsagt ny indikation Beta-ketothiolase-mangel (evidensniveau L5). Oprindelig indikation: Partiel epilepsi"
---

# Perampanel
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

## Perampanel: Fra partiel epilepsi til beta-ketothiolase-mangel
{: .text-alpha }

## Resumé

Perampanel er et lægemiddel, der oprindeligt anvendes til behandling af partiel epilepsi (registreret i vidensgrafen som partiel epilepsi og partiel motorisk epilepsi).
TxGNN-modellen forudsiger, at det kan have effekt ved **beta-ketothiolase-mangel**,
men der er i de data, der er indsamlet til denne rapport, **ingen kliniske forsøg** og **ingen publikationer**, der understøtter denne retning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Partiel epilepsi (relation registreret i vidensgrafen; godkendelsesteksten i den danske registrering er ikke tilgængelig) |
| Forudsagt ny indikation | Beta-ketothiolase-mangel |
| TxGNN-forudsigelsesscore | 0,9979 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 7 af 7) |
| Antal markedsføringstilladelser | 7 (gyldige: 7) |
| Anbefalet beslutning | Hold |

---

## Hvorfor kan forudsigelsen være rimelig?

De indsamlede data understøtter ikke en direkte mekanistisk sammenhæng. Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Perampanel (uofficiel oversættelse): »Perampanel er en non-kompetitiv antagonist af den ionotrope α-amino-3-hydroxy-5-methyl-4-isoxazolpropionsyre (AMPA)-glutamatreceptor på postsynaptiske neuroner. Glutamat er den primære excitatoriske neurotransmitter i centralnervesystemet og er impliceret i en række neurologiske lidelser forårsaget af neuronal overexcitation.« Engelsk originaltekst: "Perampanel is a non-competitive antagonist of the ionotropic α-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA) glutamate receptor on post-synaptic neurons. Glutamate is the primary excitatory neurotransmitter in the central nervous system and is implicated in a number of neurological disorders caused by neuronal over excitation." ([DailyMed: Fycompa (perampanel) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122), version af 2022-12-28; hentet 2026-11-19). Ud fra almen viden er perampanel en selektiv, ikke-kompetitiv antagonist af AMPA-type glutamatreceptorer, hvilket forklarer virkningen ved partielle anfald.

Beta-ketothiolase-mangel (ACAT1/T2-mangel) er en arvelig forstyrrelse af isoleucinnedbrydning og ketonstofudnyttelse, som giver episodisk ketoacidose. En mulig, men spekulativ kobling er, at svær metabolisk dekompensation kan give neurologisk skade eller krampeanfald, hvor AMPA-antagonisme teoretisk kunne give symptomatisk neurobeskyttelse. Det vil dog ikke adressere den underliggende enzymdefekt.

Den meget høje score (0,9979) er alene en modelforudsigelse og understøttes ikke af kliniske forsøg eller litteratur.

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28104931211 | Fycompa | filmovertrukne tabletter | Perampanel | Gyldig |
| 28104931311 | Fycompa | filmovertrukne tabletter | Perampanel | Gyldig |
| 28104930811 | Fycompa | filmovertrukne tabletter | Perampanel | Gyldig |
| 28104930911 | Fycompa | filmovertrukne tabletter | Perampanel | Gyldig |
| 28104931011 | Fycompa | filmovertrukne tabletter | Perampanel | Gyldig |

Tabellen viser 5 af 7 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

Antal godkendelser: 1 (enkeltstofpræparat, gyldig).

---

## Sikkerhedsmæssige overvejelser

**Lægemiddelinteraktioner:** Der er identificeret 56 mulige interaktioner. Blandt de viste er hovedparten af moderat sværhedsgrad, bl.a. med:
- Opioider: morfin (også liposomal), codein, hydrocodon, opium, difenoxin, diphenoxylat
- Cannabinoider: dronabinol, nabilone
- Sederende stoffer og antihistaminer: promethazin, chlorpheniramin, azelastin (nasal)
- Andre: ethanol, dexamethason, metoclopramid, sibutramin, chloroquin, hydroxychloroquin, dextromethorphan

Interaktionen med clarithromycin er klassificeret som mindre. Mange af de moderate interaktioner vedrører additiv sedation eller påvirkning af centralnervesystemet.

For advarsler og kontraindikationer henvises til det godkendte produktresumé (SmPC), da disse data ikke er tilgængelige i de indsamlede data.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden støtte fra kliniske forsøg eller publikationer, og der er ingen påvist mekanistisk sammenhæng med den underliggende enzymdefekt. Evidensniveauet er L5.

**For at komme videre kræves følgende:**
- Systematisk litteratur- og forsøgsgennemgang for perampanel ved beta-ketothiolase-mangel eller beslægtede organiske acidurier
- Data om virkningsmekanisme fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen
- Præklinisk eller mekanistisk belæg for, at AMPA-antagonisme kan påvirke de neurologiske konsekvenser af sygdommen
- Vurdering af, om sygdommens sjældne karakter gør et kontrolleret forsøg realistisk

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Fycompa (perampanel) prescribing information, Eisai Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

