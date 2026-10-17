---
layout: default
title: Necitumumab
parent: Kun modelforudsigelse (L5)
nav_order: 579
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Necitumumab: forudsagt ny indikation Gingival fibromatose (evidensniveau L5). Oprindelig indikation: Ikke-småcellet lungekræft (NSCLC)"
monitor_inn: "Necitumumab"
predicted_indications: ["fibromatosis, gingival", "fibromatosis, gingival", "hamartoma of lung", "hamartoma of lung", "lung hilum carcinoma", "lung hilum carcinoma", "fibroma of lung", "fibroma of lung", "pulmonary sulcus neoplasm", "lung germ cell tumor"]
---

# Necitumumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

# Necitumumab: Fra ikke-småcellet lungekræft til gingival fibromatose

## Resumé

Necitumumab er et monoklonalt antistof mod EGFR (epidermal vækstfaktorreceptor), som oprindeligt er udviklet til behandling af ikke-småcellet lungekræft.
TxGNN-modellen forudsiger, at det kan have effekt ved **gingival fibromatose**, men der er **ingen registrerede kliniske forsøg** og **ingen publikationer**, der understøtter denne retning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke-småcellet lungekræft (NSCLC) |
| Forudsagt ny indikation | Gingival fibromatose |
| TxGNN-forudsigelsesscore | 99,92 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

De data, der er indsamlet til denne rapport, indeholder ikke en detaljeret beskrivelse af virkningsmekanismen. Necitumumab er dog kendt som et anti-EGFR-antistof, og dets effekt ved planocellulær NSCLC er den etablerede anvendelse.

Der er ikke påvist en EGFR-drevet mekanisme ved gingival fibromatose. Forudsigelsen hviler udelukkende på den høje TxGNN-score, som sandsynligvis afspejler nærhed i vidensgrafen til EGFR-relaterede fibroproliferative signalveje snarere end en valideret mekanisme. Koblingen må derfor betragtes som spekulativ.

Modellen forudsiger også andre indikationer med samme evidensgrundlag (kun modelscore, ingen forsøg eller litteratur):

| Forudsagt indikation | TxGNN-score | Vurdering |
|------|------|------|
| Hamartom i lungen | 99,91 % | Godartet mesenkymal læsion; ingen EGFR-afhængig mekanisme; toksicitetsprofilen vil næppe kunne forsvares |
| Karcinom i lungehilus | 99,91 % | Biologisk mest plausibel (overlap med planocellulær NSCLC), men sandsynligvis blot en underklassifikation af den godkendte indikation |
| Fibrom i lungen | 99,91 % | Ingen etableret EGFR-mekanisme |
| Neoplasi i sulcus pulmonalis (Pancoast) | 99,90 % | Anatomisk undergruppe af NSCLC snarere end en reel ny indikation |
| Germinalcelletumor i lungen | 99,90 % | Sjælden; EGFR er ikke en etableret drivkraft; svag kobling |

---

## Kliniske forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret for den forudsagte indikation.

---

## Litteratur

Der er aktuelt ingen relateret litteratur tilgængelig for den forudsagte indikation.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105547314 | Portrazza | Koncentrat til infusionsvæske, opløsning | Indikationsteksten er ikke tilgængelig i de indsamlede data |

Indehaver af tilladelsen: Eli Lilly Netherland B.V. Status: gyldig.

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Målrettet behandling (monoklonalt anti-EGFR-antistof), ikke konventionelt cytotoksisk |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC); de indsamlede data peger ikke på specifikke punkter, men for EGFR-antistoffer overvåges typisk elektrolytter (herunder magnesium) |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

Se advarsler og forsigtighedsregler i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

**Lægemiddelinteraktioner** (5 poster i de indsamlede data):

- **Thalidomid**: Alvorlig (Major)
- **Palifermin**: Moderat
- **Idelalisib**: Moderat
- **Gemcitabin**: Mindre (Minor)

Derudover er EGFR registreret som lægemidlets farmakologiske mål.

Vurderingen af en godartet indikation bør desuden tage højde for, at EGFR-antistoffer generelt er forbundet med hudtoksicitet, hypomagnesiæmi og tromboemboliske hændelser. Det er ikke dokumenteret i de indsamlede data og skal verificeres i produktresuméet.

Oplysninger om advarsler og kontraindikationer foreligger ikke; se det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på modelscore (evidensniveau L5) uden kliniske forsøg eller publikationer, og der er ingen plausibel EGFR-drevet mekanisme ved gingival fibromatose. De mest plausible af de øvrige forudsigelser (lungehilus- og Pancoast-tumorer) ligger inden for den eksisterende NSCLC-indikation og er ikke egentlig repurposing.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) og en biologisk begrundelse for EGFR's rolle ved gingival fibromatose
- Præklinisk eller litteraturbaseret evidens for den forudsagte indikation
- Indikationstekst, advarsler og kontraindikationer fra det danske produktresumé (SmPC) hos Lægemiddelstyrelsen
- Vurdering af nytte/risiko, da en godartet tilstand næppe vil opveje toksiciteten ved et EGFR-antistof
- Afklaring af, om lungehilus- og Pancoast-forudsigelserne blot kan håndteres inden for den eksisterende NSCLC-indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

