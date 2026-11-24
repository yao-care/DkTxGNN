---
layout: default
title: Codeine
parent: Kun modelforudsigelse (L5)
nav_order: 217
evidence_level: L5
indication_count: 3
monitor_inn: "codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
last_modified_at: 2026-11-24
description: "Codeine: forudsagt ny indikation Næsehulesygdom (nasal cavity disease) (evidensniveau L5). I Danmark, markedsføringstilladelser: 9 (gyldige: 9)"
---

# Codeine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
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

## Codein: opioid (svagt opioid-receptoragonist) → Næsehulesygdom (nasal cavity disease)
{: .text-alpha }

## Kort resumé

Codein er et opioid, som i Danmark er markedsført som oral opløsning. Den primære TxGNN-forudsigelse er **Næsehulesygdom (nasal cavity disease)**. Der foreligger **ingen kliniske forsøg** og kun **1 publikation**, som er en case-rapport om en uheldig hændelse og ikke dokumenterer nogen behandlingseffekt.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Næsehulesygdom (nasal cavity disease) |
| TxGNN-forudsigelsesscore | 0,9993 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 9 af 9) |
| Antal markedsføringstilladelser | 9 (gyldige: 9) |
| Anbefalet beslutning | Hold |

## Hvorfor er denne forudsigelse (ikke) rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Codeine (uofficiel oversættelse): »Codeinsulfat er en opioidagonist, der er relativt selektiv for mu-opioidreceptoren, men med en meget svagere affinitet end morfin. Det er blevet antaget, at codeins analgetiske egenskaber skyldes dets omdannelse til morfin, selvom den nøjagtige analgetiske virkningsmekanisme fortsat er ukendt.« Engelsk originaltekst: "Codeine sulfate is an opioid agonist relatively selective for the mu-opioid receptor, but with a much weaker affinity than morphine. The analgesic properties of codeine have been speculated to come from its conversion to morphine, although the exact mechanism of analgesic action remains unknown." ([DailyMed: codeine sulfate prescribing information, Lannett Company, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5819bdf7-300e-45b8-8f3a-447b53656293), version af 2026-01-16; hentet 2026-11-19). Codein er et opioid, der generelt anvendes til smertelindring og hostedæmpning.

Den høje score (0,9993) afspejler sandsynligvis nærheden i modellens netværk til øvre luftvejstilstande, hvor codein indgår i kombinationspræparater til symptomlindring. Der er ikke noget belæg for en terapeutisk mekanisme i sygdomme i næsehulen. Den eneste fundne publikation beskriver en usædvanlig årsag til næsesten (rhinolit), hvor en fremmedlegeme bestod af en hærdet blanding af codein og opium. Det er en skadelig hændelse og ikke en gavnlig effekt.

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case-rapport | Ear, Nose & Throat Journal | Usædvanlig rhinolit hos en 21-årig mand, dannet omkring et indkapslet fremmedlegeme af codein og opium ("opioma"). Beskriver en skade, ikke en behandlingseffekt. |

## Information om markedet i Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28100726176 | Kodein "DAK" | filmovertrukne tabletter | CODEINPHOSPHATHEMIHYDRAT | Gyldig |
| 28104675410 | Kodein "EQL Pharma" | filmovertrukne tabletter | CODEINPHOSPHATHEMIHYDRAT | Gyldig |
| 28107282124 | Kodein "ExtractumPharma" | tabletter | CODEINPHOSPHATHEMIHYDRAT | Gyldig |
| 28107282224 | Kodein "ExtractumPharma" | tabletter | CODEINPHOSPHATHEMIHYDRAT | Gyldig |
| 28107282324 | Kodein "ExtractumPharma" | tabletter | CODEINPHOSPHATHEMIHYDRAT | Gyldig |

Tabellen viser 5 af 9 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Der er registreret i alt 552 interaktioner. Blandt de vigtigste af alvorlig grad (Major) er **alvimopan** og **bupropion**. Blandt interaktioner af moderat grad er bl.a. atropin, cimetidin, dexamethason, glycopyrronium, hyoscyamin, loperamid, granisetron og dronabinol.

For øvrig sikkerhedsinformation henvises til det godkendte produktresumé (SmPC).

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen understøttes ikke af nogen studier, der direkte undersøger codein ved sygdomme i næsehulen, og den eneste publikation beskriver en skadelig hændelse. Evidensniveauet er derfor L5.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme
- Kontrollerede studier, der direkte undersøger codein ved sygdomme i næsehulen
- Gennemgang af produktresuméets advarsler og kontraindikationer, som ikke var tilgængelige i de indsamlede data

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: codeine sulfate prescribing information, Lannett Company, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5819bdf7-300e-45b8-8f3a-447b53656293) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

