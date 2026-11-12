---
layout: default
title: Corifollitropin Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 221
evidence_level: L5
indication_count: 7
monitor_inn: "Corifollitropin alfa"
predicted_indications: ["gastroduodenitis", "migraine disorder", "peptic ulcer disease", "migraine with brainstem aura", "Raynaud disease", "pulmonary hypertension", "kyphoscoliotic heart disease"]
last_modified_at: 2026-11-06
description: "Corifollitropin Alfa: forudsagt ny indikation Gastroduodenitis (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (teksten om godkendt indikation er…"
---

# Corifollitropin Alfa
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **7** stk.
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

## Corifollitropin alfa: Fra fertilitetsbehandling til gastroduodenitis (kun modelforudsigelse)
{: .text-alpha }

## Resumé i én sætning

Corifollitropin alfa er en langtidsvirkende, rekombinant FSH-agonist, som er registreret i Danmark under handelsnavnet Elonva. Teksten om godkendt indikation i de indsamlede data er tom. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **gastroduodenitis**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter dette. Forudsigelsen er rent beregningsmæssig.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (teksten om godkendt indikation er tom) |
| Forudsagt ny indikation | Gastroduodenitis |
| TxGNN-forudsigelsesscore | 0,9965 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger i øjeblikket ikke detaljerede data om virkningsmekanismen i de indsamlede data. Corifollitropin alfa er ifølge de tilgængelige oplysninger en langtidsvirkende rekombinant FSH-agonist (FSH-beta fusioneret med CTP fra hCG-beta), som virker på FSH-receptoren i gonadevæv.

Der er ikke identificeret nogen sandsynlig biologisk forbindelse mellem FSH-receptoragonisme og inflammation i mavesækkens eller tolvfingertarmens slimhaed. Den høje score (0,9965) stammer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Forudsigelsen bør derfor betragtes som et hypotesegenererende signal og ikke som et holdepunkt for behandling.

Andre forudsigelser for lægemidlet med lignende score og samme mangel på evidens omfatter migræne, mavesår, migræne med hjernestammeaura, Raynauds sygdom, pulmonal hypertension og kyfoskoliotisk hjertesygdom. Ingen af disse har kliniske forsøg eller litteratur, og der er ikke fundet plausible mekanistiske forbindelser.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relevante kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relevant litteratur tilgængelig.

---

## Information om markedet i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104459408 | Elonva (N.V. Organon) | Injektionsvæske, opløsning | Ikke angivet i de indsamlede data |

Der er tale om 2 nationale tilladelser til enkeltstofpræparater. Tilladelserne er gyldige.

<!-- review:begin dk-lic-20261112-corifollitropin_alfa-1 -->

> **Rettelse ved gennemgang (2026-11-12)**: Oprindeligt stod der: "Der er tale om 1 national tilladelse til et enkeltstofpræparat. Tilladelsen er gyldig." Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler: der er 2 tilladelser for dette lægemiddel (heraf 2 enkeltstofpræparater i dataene); det tidligere antal kom fra en ældre version af dataene. De aktuelle tal står i hurtigt overblik. Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261112-corifollitropin_alfa-1 -->

---

## Sikkerhedsovervejelser

Der foreligger ingen sikkerhedsdata i de indsamlede data. Der er heller ikke fundet registrerede lægemiddelinteraktioner. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Det bemærkes, at gonadotropiner er forbundet med kendte risici såsom ovarielt hyperstimulationssyndrom og tromboemboliske hændelser. Disse risici taler for forsigtighed i stedet for terapeutisk gevinst ved de forudsagte kardiovaskulære og vaskulære tilstande.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en grafbaseret model uden kliniske forsøg, uden litteratur og uden plausibel mekanistisk forbindelse. Evidensniveauet er L5.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Godkendt indikationstekst og advarsler/kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen
- Prækliniske eller mekanistiske studier, der kan understøtte en biologisk forbindelse til gastroduodenitis, før der overvejes yderligere vurdering

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-12 | Antal tilladelser: “Der er tale om 1 national tilladelse til et enkeltstofpræparat. Tilladelsen er g” → “Der er tale om 2 nationale tilladelser til enkeltstofpræparater. Tilladelserne e” | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

