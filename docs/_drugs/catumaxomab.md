---
layout: default
title: Catumaxomab
parent: Kun modelforudsigelse (L5)
nav_order: 167
evidence_level: L5
indication_count: 10
---

# Catumaxomab
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

# Catumaxomab: Fra ikke-angivet oprindelig indikation til svær non-proliferativ diabetisk retinopati

## Resumé i én sætning

Catumaxomab er et trifunktionelt bispecifikt antistof (anti-EpCAM × anti-CD3), som er markedsført i Danmark under navnet Korjuny. De data, der er indsamlet til denne rapport, angiver dog ingen oprindelig indikation.
TxGNN-modellen forudsiger, at det kan have effekt ved **svær non-proliferativ diabetisk retinopati**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter dette. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (indikationsteksten for Korjuny er tom) |
| Forudsagt ny indikation | Svær non-proliferativ diabetisk retinopati |
| TxGNN-forudsigelsesscore | 99,64 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Catumaxomab binder EpCAM på tumorceller og CD3 på T-celler, og via Fc-delen rekrutteres yderligere immunceller (accessoriske celler). Dermed omdirigeres immunsystemet mod EpCAM-positive tumorceller. Ifølge farmakologidata er CD3E identificeret som det primære molekylære mål. Detaljerede data om virkningsmekanisme er ellers ikke tilgængelige i de indsamlede data, og der er ikke angivet nogen oprindelig indikation, som forudsigelsen kan forankres i.

Der er ikke påvist nogen mekanistisk sammenhæng mellem catumaxomab og diabetisk retinopati. Sygdommen drives af hyperglykæmi-induceret mikrovaskulær skade, VEGF-medieret karlækage og neovaskularisering og er ikke en EpCAM-drevet eller T-celle-omdirigeringsfølsom sygdom. Der findes desuden veletablerede behandlinger (anti-VEGF, laserfotokoagulation, kortikosteroidimplantater). Systemisk eller intravitreal immunaktivering vil give sikkerhedsmæssige bekymringer, f.eks. cytokinfrigivelse og inflammation i øjet.

TxGNN-scoren er en grafbaseret forudsigelse og skal ikke tolkes som klinisk evidens.

### Øvrige forudsigelser fra modellen

| Forudsagt indikation | TxGNN-score | Evidensniveau | Vurdering |
|------|------|------|------|
| Lægemiddelinduceret osteoporose | 99,58 % | L5 | Ingen plausibel mekanistisk sammenhæng; cytokinfrigivelse (TNF-alfa, IL-6) kan teoretisk fremme knoglenedbrydning |
| Diabetisk retinopati | 99,47 % | L5 | Ingen mekanistisk sammenhæng; ugunstig risk-benefit-profil |
| Diabetisk grå stær | 98,45 % | L5 | Ingen mekanistisk sammenhæng; kirurgi er standardbehandling |
| Sarkomatoid overgangscellekarcinom i nyrebækkenet | 98,29 % | L5 | Biologisk mest plausibel (onkologisk, EpCAM-udtryk i urotelkarcinom), men epitel-mesenkymal transition kan nedsætte EpCAM-udtrykket. Kræver bekræftelse af EpCAM-ekspression og egnet administrationsvej. Betragtes som et forskningsspørgsmål |

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
Forudsigelserne er udelukkende modelbaserede (L5) uden kliniske forsøg eller publikationer. For de to øjenindikationer, osteoporose og diabetisk grå stær er der ingen plausibel mekanistisk sammenhæng, og risk-benefit er ugunstig. Den eneste biologisk plausible hypotese er sarkomatoid overgangscellekarcinom i nyrebækkenet, som bør behandles som et forskningsspørgsmål.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet (advarsler og kontraindikationer) fra Lægemiddelstyrelsen, som mangler i de indsamlede data
- Fastlæggelse af oprindelig godkendt indikation og detaljerede data om virkningsmekanisme
- For urotelkarcinom: EpCAM-immunhistokemi på sarkomatoide urotelkarcinomprøver samt vurdering af administrationsvej
- Præklinisk eller mekanistisk understøttelse, før øvrige forudsigelser overvejes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

