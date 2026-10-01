---
layout: default
title: Lecanemab
parent: Kun modelforudsigelse (L5)
nav_order: 259
evidence_level: L5
indication_count: 10
---

# Lecanemab
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

# Lecanemab: Fra [original indikation er ikke angivet i datagrundlaget] til diabetisk grå stær

## Resumé i én sætning

Lecanemab er et monoklonalt antistof rettet mod amyloid-beta-protofibriller. Evidence Pack'en angiver ikke den oprindelige indikation, og feltet er tomt både i datagrundlaget og i den danske registrering. TxGNN-modellen forudsiger, at lecanemab kan have effekt på **diabetisk grå stær (diabetic cataract)**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i datagrundlaget (godkendelsesteksten i den danske registrering er tom) |
| Forudsagt ny indikation | Diabetisk grå stær (diabetic cataract) |
| TxGNN-forudsigelsesscore | 98,5 % |
| Evidensniveau | L5 (kun modelforudsigelse) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i Evidence Pack'en. Lecanemab er et anti-amyloid-beta-protofibril-antistof, og det er den eneste mekanistiske oplysning, vi har.

Den eneste tænkelige sammenhæng er, at aggregering af amyloid-beta eller fejlfoldning af proteiner i øjets linse kan bidrage til grå stær. Det er en spekulativ hypotese uden dokumentation i datagrundlaget.

Diabetisk grå stær drives hovedsageligt af polyolvejen og oxidativt stress, og det adresserer lecanemabs mekanisme ikke. Et systemisk indgivet antistof har desuden ingen etableret vej til linsen. Den høje score skyldes sandsynligvis nærhed i vidensgrafen til andre katarakt-noder og ikke en reel farmakologisk sammenhæng. Systemiske sikkerhedssignaler (f.eks. ARIA) taler yderligere imod en indikation i en benign tilstand.

### Øvrige forudsagte indikationer (alle L5, Hold)

Alle andre forudsigelser i Evidence Pack'en er også former for grå stær. De har lignende scorer og samme evidensniveau, og dubletter er slået sammen.

| Forudsagt indikation | TxGNN-score | Kommentar |
|------|------|------|
| Diabetisk grå stær | 98,5 % | Polyolvej og oxidativt stress adresseres ikke af mekanismen |
| Moden grå stær | 98,4 % | Fremskreden, uigennemsigtig fase, behandles kirurgisk. Ingen evidens for reversering |
| Umoden grå stær | 98,4 % | Hypotetisk. Kræver prækliniske linsemodeller først |
| Tetanisk grå stær | 98,4 % | Skyldes forstyrret calciumhomøostase, ingen forbindelse til mekanismen |
| Grå stær ved type 2-diabetes | 98,4 % | Hyperglykæmi, glykering og oxidativt stress, ikke et mål for lecanemab |
| Kraniostenose-katarakt | 98,4 % | Sjælden syndromisk eller medfødt form med sandsynlig genetisk årsag |

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret (hverken i ClinicalTrials.gov eller ICTRP).

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse nr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106902923 | LEQEMBI (Eisai GmbH) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i datagrundlaget |

Lægemidlet gives som infusion (injicerbar administrationsvej). Evidence Pack'en oplyser ikke, om tilladelsen er national eller centraliseret.

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner:** Ingen interaktioner fundet i forespørgslen (0 resultater).
- **Systemisk risiko:** Evidence Pack'ens mekanistiske vurdering nævner ARIA (amyloidrelaterede billedanomalier) som et systemisk sikkerhedssignal for antistofklassen. Det vejer tungt mod brug ved en benign øjentilstand.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore (evidensniveau L5) uden kliniske forsøg eller publikationer. Den er sandsynligvis en artefakt i vidensgrafen, da lecanemabs mekanisme ikke adresserer katarakts patofysiologi, og et systemisk antistof har ingen kendt vej til linsen. Sikkerhedsprofilen (bl.a. ARIA) opvejer ikke et uddokumenteret potentiale i en benign tilstand.

**For at komme videre kræves:**
- Fuldstændige data om oprindelig indikation og virkningsmekanisme (DrugBank)
- Sikkerhedsoplysninger fra produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer), som er en blokerende datamangel for sikkerhedsscreening
- Prækliniske studier i linsemodeller, der undersøger, om amyloid-beta-aggregering bidrager til katarakt, og om antistoffet kan nå linsen
- En litteratur- og forsøgsgennemgang, der kan løfte evidensniveauet over L5

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser fra repurposing-modeller skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

