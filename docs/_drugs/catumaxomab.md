---
layout: default
title: Catumaxomab
parent: Kun modelforudsigelse (L5)
nav_order: 167
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-28
description: "Catumaxomab: forudsagt ny indikation Svær non-proliferativ diabetisk retinopati (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (indikationsteksten for Korjuny er…"
monitor_inn: "Catumaxomab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "drug-induced osteoporosis", "diabetic retinopathy"]
---

# Catumaxomab
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

## Catumaxomab: Fra ikke-angivet oprindelig indikation til svær non-proliferativ diabetisk retinopati
{: .text-alpha }

## Resumé i én sætning

Catumaxomab er et trifunktionelt bispecifikt antistof (anti-EpCAM × anti-CD3), som er markedsført i Danmark under navnet Korjuny. De data, der er indsamlet til denne rapport, angiver dog ingen oprindelig indikation.
TxGNN-modellen forudsiger, at det kan have effekt ved **svær non-proliferativ diabetisk retinopati**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter dette. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (indikationsteksten for Korjuny er tom) |
| Forudsagt ny indikation | Svær non-proliferativ diabetisk retinopati |
| TxGNN-forudsigelsesscore | 0,9964 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Catumaxomab binder EpCAM på tumorceller og CD3 på T-celler, og via Fc-delen rekrutteres yderligere immunceller (accessoriske celler). Dermed omdirigeres immunsystemet mod EpCAM-positive tumorceller. Ifølge farmakologidata er CD3E identificeret som det primære molekylære mål. Detaljerede data om virkningsmekanisme er ellers ikke tilgængelige i de indsamlede data, og der er ikke angivet nogen oprindelig indikation, som forudsigelsen kan forankres i.

Der er ikke påvist nogen mekanistisk sammenhæng mellem catumaxomab og diabetisk retinopati. Sygdommen drives af hyperglykæmi-induceret mikrovaskulær skade, VEGF-medieret karlækage og neovaskularisering og er ikke en EpCAM-drevet eller T-celle-omdirigeringsfølsom sygdom. Der findes desuden veletablerede behandlinger (anti-VEGF, laserfotokoagulation, kortikosteroidimplantater). Systemisk eller intravitreal immunaktivering vil give sikkerhedsmæssige bekymringer, f.eks. cytokinfrigivelse og inflammation i øjet.

TxGNN-scoren er en grafbaseret forudsigelse og skal ikke tolkes som klinisk evidens.

### Øvrige forudsigelser fra modellen

| Forudsagt indikation | TxGNN-score | Evidensniveau | Vurdering |
|------|------|------|------|
| Lægemiddelinduceret osteoporose | 0,9958 | L5 | Ingen plausibel mekanistisk sammenhæng; cytokinfrigivelse (TNF-alfa, IL-6) kan teoretisk fremme knoglenedbrydning |
| Diabetisk retinopati | 0,9947 | L5 | Ingen mekanistisk sammenhæng; ugunstig risk-benefit-profil |

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106834422 | Korjuny (Lindis Biotech GmbH) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i de indsamlede data |

Ifølge farmakologidata blev EMA-godkendelsen til behandling af malign ascites hos patienter med EpCAM-positive kræftformer trukket tilbage i 2017 af kommercielle årsager (under navnet Removab) og genautoriseret i begyndelsen af 2025. Catumaxomab har desuden orphan-status i EU for mavekræft (tildelt 2006).

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Klassifikation | Immunterapi (bispecifikt T-celle-rekrutterende antistof, ATC L01XC09) |
| Myelosuppressionsrisiko | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Monitoreringspunkter | Se produktresuméet (SmPC) for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) for advarsler og forholdsregler |

---

## Sikkerhedsmæssige overvejelser

- **Lægemiddelinteraktioner**: Der er registreret én farmakologisk målinteraktion (CD3e, primært molekylært mål). Der er ikke angivet interaktionsniveau eller klinisk vurdering.
- **Immunaktivering**: Der er en teoretisk risiko for cytokinfrigivelse og inflammation ved anvendelse i nye indikationer, især i øjet.

For øvrige sikkerhedsoplysninger henvises til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelserne er udelukkende modelbaserede (L5) uden kliniske forsøg eller publikationer. For de to øjenindikationer og osteoporose er der ingen plausibel mekanistisk sammenhæng, og risk-benefit er ugunstig.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet (advarsler og kontraindikationer) fra Lægemiddelstyrelsen, som mangler i de indsamlede data
- Fastlæggelse af oprindelig godkendt indikation og detaljerede data om virkningsmekanisme
- For urotelkarcinom: EpCAM-immunhistokemi på sarkomatoide urotelkarcinomprøver samt vurdering af administrationsvej
- Præklinisk eller mekanistisk understøttelse, før øvrige forudsigelser overvejes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

