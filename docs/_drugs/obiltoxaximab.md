---
layout: default
title: Obiltoxaximab
parent: Kun modelforudsigelse (L5)
nav_order: 316
evidence_level: L5
indication_count: 10
---

# Obiltoxaximab
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

# Obiltoxaximab: Fra inhalationsmiltbrand til postinfektiøs vaskulitis

## Resumé i én sætning

Obiltoxaximab er et monoklonalt antistof, der bruges mod inhalationsmiltbrand (*Bacillus anthracis*).
TxGNN-modellen forudsiger, at det kan have effekt ved **postinfektiøs vaskulitis**, men forudsigelsen er rent modelbaseret og understøttes af **0 kliniske forsøg** og **0 publikationer**.
Den vurderes derfor som **Hold**.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Inhalationsmiltbrand (fremgår af de kliniske forsøg; indikationsteksten er ikke angivet i de danske registerdata) |
| Forudsagt ny indikation | Postinfektiøs vaskulitis |
| TxGNN-forudsigelsesscore | 99,74 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede mekanismedata for lægemidlet er ikke tilgængelige i datagrundlaget. Ud fra den kendte virkningsmekanisme binder obiltoxaximab det beskyttende antigen (PA) fra *Bacillus anthracis* og blokerer dermed miltbrandtoksinets indtrængen i cellerne. Midlet er altså målrettet et specifikt bakterielt toksin.

Postinfektiøs vaskulitis er typisk immunkompleks- eller autoimmunt medieret og drives ikke af PA-afhængig toksinaktivitet. Der er derfor ikke et troværdigt mekanistisk led mellem den oprindelige og den forudsagte indikation. Den høje score (0,997) er udelukkende en grafbaseret forudsigelse fra TxGNN.

---

## Dokumentation fra kliniske forsøg

For den primære forudsigelse (postinfektiøs vaskulitis) er der i øjeblikket ingen relaterede kliniske forsøg registreret.

Til sammenligning har forudsigelsen nr. 5, **postbakteriel lidelse**, fire forsøg. Alle vedrører miltbrand eller sikkerhed og farmakokinetik hos raske frivillige, ikke effekt ved postbakterielle lidelser:

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT03088111](https://clinicaltrials.gov/study/NCT03088111) | Fase 4 | Ukendt | 100 | Åbent feltstudie af klinisk gavn, sikkerhed og farmakokinetik ved behandling af inhalationsmiltbrand. Kun indirekte støtte. |
| [NCT01932242](https://clinicaltrials.gov/study/NCT01932242) | Fase 1 | Afsluttet | 70 | Dobbeltblindet, placebokontrolleret studie af sikkerhed, tolerabilitet og farmakokinetik ved gentagen dosering hos voksne frivillige |
| [NCT01929226](https://clinicaltrials.gov/study/NCT01929226) | Fase 1 | Afsluttet | 280 | Dobbeltblindet, placebokontrolleret studie af sikkerhed og farmakokinetik ved enkeltdosis hos voksne frivillige |
| [NCT00138411](https://clinicaltrials.gov/study/NCT00138411) | Fase 1 | Afsluttet | 36 | Dosiseskalering, sikkerhed og farmakokinetik samt mulig interaktion med ciprofloxacin |

Forsøgene giver nyttig baggrundsviden om sikkerhed og farmakokinetik, men ingen indikationsspecifik effektdokumentation. Sammenfaldet synes at skyldes etiketten "bakteriel" og ikke en fælles mekanisme.

---

## Litteraturdokumentation

Der foreligger i øjeblikket ingen relateret litteratur.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28106295319 | NYXTHRACIS | Koncentrat til infusionsvæske, opløsning (intravenøs) | SFL Pharmaceuticals Deutschland GmbH |

---

## Øvrige forudsigelser fra TxGNN

Ingen af disse har kliniske forsøg eller litteratur, bortset fra postbakteriel lidelse (se ovenfor). Alle vurderes som **Hold**.

| Forudsagt indikation | Score | Evidensniveau | Vurdering af mekanistisk sammenhæng |
|------|------|------|---------|
| Postinfektiøs vaskulitis | 99,74 % | L5 | Ingen troværdig sammenhæng |
| Postinfektiøst syndrom | 99,74 % | L5 | Ingen plausibelt mål for et toksinneutraliserende antistof |
| Postbakteriel lidelse | 99,74 % | L4 | Kun indirekte; kobling via den generelle etiket "bakteriel" |
| Infektiøs uretrastriktur | 99,74 % | L5 | Fibrotisk tilstand, der primært behandles kirurgisk eller endoskopisk |
| Otitis externa | 99,71 % | L5 | Lokalt behandlelig tilstand, som skyldes bakterier uden PA-afhængig toksinvirkning |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ikke fundet registrerede lægemiddelinteraktioner i datagrundlaget.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende baseret på en grafmodel (L5) uden kliniske forsøg eller litteratur for postinfektiøs vaskulitis. Obiltoxaximabs kendte mekanisme, neutralisering af miltbrandtoksinets PA, har ingen plausibel kobling til tilstanden.

**For at komme videre kræves følgende:**
- Advarsler og kontraindikationer fra produktresuméet fra Lægemiddelstyrelsen (blokerende datamangel)
- Detaljerede data om virkningsmekanisme fra DrugBank
- Evt. en ny, mekanistisk velbegrundet kandidatindikation, før der investeres i yderligere evidensindsamling

*Dette resultat er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepurposing skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

