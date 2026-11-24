---
layout: default
title: Hexaminolevulinate
parent: Kun modelforudsigelse (L5)
nav_order: 408
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-24
description: "Hexaminolevulinate: forudsagt ny indikation Bronkitis (evidensniveau L5). Oprindelig indikation: Ikke oplyst i de indsamlede data (godkendt indikationstekst for Hexvi…"
monitor_inn: "hexaminolevulinate"
predicted_indications: ["bronchitis"]
---

# Hexaminolevulinate
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

## Hexaminolevulinat: Fra diagnostisk billeddannelse ved blærekræft til bronkitis
{: .text-alpha }

## Resumé i én sætning

Hexaminolevulinat er et lysfølsomt stof (fotosensibilisator), der anvendes intravesikalt i Danmark som Hexvix. Det fungerer som optisk kontrastmiddel ved blåt lys-cystoskopi og er knyttet til blæreområdet.
TxGNN-modellen forudsiger, at det kan have effekt ved **bronkitis**, men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter denne retning. Forudsigelsen hviler udelukkende på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i de indsamlede data (godkendt indikationstekst for Hexvix er tom) |
| Forudsagt ny indikation | Bronkitis |
| TxGNN-forudsigelsesscore | 0,9906 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Hexaminolevulinate (uofficiel oversættelse): »Hexaminolevulinat er en ester af hæmprækursoren aminolevulinsyre. Efter instillation i blæren trænger hexaminolevulinat ind i blæreslimhinden og formodes at trænge ind i det intracellulære rum i slimhindecellerne, hvor det anvendes som prækursor i dannelsen af det fotoaktive intermediat protoporfyrin IX (PpIX) og andre fotoaktive porfyriner (PAP'er).« Engelsk originaltekst: "Hexaminolevulinate is an ester of the heme precursor, aminolevulinic acid. After bladder instillation, hexaminolevulinate enters the bladder mucosa and is proposed to enter the intracellular space of mucosal cells where it is used as a precursor in the formation of the photoactive intermediate protoporphyrin IX (PpIX) and other photoactive porphyrins (PAPs)." ([DailyMed: Cysview (hexaminolevulinate hydrochloride) prescribing information, Photocure Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5aeed40d-6841-4adf-8940-f51d439fdfa3), version af 2026-06-03; hentet 2026-11-19). Det er kendt, at hexaminolevulinat er en forstadie (prodrug), som omdannes til protoporfyrin IX (PpIX) i neoplastiske celler. PpIX lyser rødt under blåt lys, hvilket gør det muligt at se tumorvæv ved cystoskopi af blæren.

Der er **ikke** påvist en etableret mekanistisk sammenhæng mellem PpIX-ophobning eller fotodynamiske effekter og bronkitis, som er en inflammatorisk eller infektiøs luftvejstilstand. Mulige spekulative forklaringer, fx fotodynamisk antimikrobiel effekt, understøttes ikke af de foreliggende data. Desuden gives lægemidlet intravesikalt, og levering til bronkietræet er usandsynlig uden en anden formulering. Den høje modelscore bør derfor ses som en statistisk modeludgang og ikke som biologisk dokumentation.

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28103742204 | Hexvix | pulver og solvens til intravesikal opløsning | Hexaminolevulinathydrochlorid | Gyldig |
| 28106611521 | Hexvix | pulver og solvens til intravesikal opløsning | Hexaminolevulinathydrochlorid | Gyldig |
| 28107667226 | Hexvix | pulver og solvens til intravesikal opløsning | Hexaminolevulinathydrochlorid | Gyldig |

Tabellen viser alle 3 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er registreret 2 interaktioner af alvorlighedsgrad *Major* (kilde: DDInter), begge med **valrubicin**. Valrubicin er et intravesikalt kemoterapeutikum, så kombination bør vurderes nøje.

For øvrige sikkerhedsoplysninger henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (evidensniveau L5) uden kliniske forsøg eller publikationer. Der er ingen plausibel mekanistisk sammenhæng med bronkitis, og den intravesikale administrationsvej gør levering til luftvejene urealistisk.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Godkendt indikationstekst og sikkerhedsoplysninger (advarsler og kontraindikationer) fra produktresuméet hos Lægemiddelstyrelsen
- Præklinisk eller mekanistisk evidens for en relevant effekt i luftvejene
- Vurdering af en alternativ formulering eller administrationsvej, hvis forskning i indikationen overvejes

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Cysview (hexaminolevulinate hydrochloride) prescribing information, Photocure Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5aeed40d-6841-4adf-8940-f51d439fdfa3) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

