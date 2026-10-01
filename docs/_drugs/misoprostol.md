---
layout: default
title: Misoprostol
parent: Kun modelforudsigelse (L5)
nav_order: 297
evidence_level: L5
indication_count: 4
---

# Misoprostol
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

# Misoprostol: Fra en ikke angivet oprindelig indikation til amenoré

## Resumé i få sætninger

Misoprostol er en prostaglandin E1-analog og er i Danmark markedsført som tabletter (Angusta). Den godkendte indikationstekst indgår ikke i datagrundlaget. TxGNN-modellen forudsiger, at stoffet kan være relevant ved **amenoré**, men der er **ingen registrerede kliniske forsøg** og kun **7 publikationer**. Ingen af dem viser, at misoprostol behandler amenoré. Den høje modelscore afspejler sandsynligvis nærhed til graviditet og abort i vidensgrafen og bør ikke læses som et terapeutisk signal.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i datagrundlaget |
| Forudsagt ny indikation | Amenoré |
| TxGNN-prædiktionsscore | 99,64 % |
| Evidensniveau | L4 (iht. Evidence Pack). Litteraturen understøtter ikke effekt ved amenoré. |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ikke detaljerede data om virkningsmekanisme. Misoprostol er en prostaglandin E1-analog med uterotoniske virkninger og effekt på modning af livmoderhalsen. Stoffet bruges til at fremkalde livmoderblødning og udstødning ved graviditetsafbrydelse. Der er derfor ingen etableret mekanisme, der taler for behandling af amenoré.

Den høje TxGNN-score (0,996) skyldes sandsynligvis, at amenoré i litteraturen ofte nævnes som et tegn på graviditet. Det gør sygdommen "nabo" til abort og graviditet i vidensgrafen. Forudsigelsen bør derfor ikke tolkes som et reelt behandlingssignal.

Modellen foreslår også **atypisk coarctatio aortae** (score 99,30 %). Der er ingen klinisk evidens for dette. Den eneste tænkelige forbindelse er en hypotese om klasseeffekt: PGE1 (alprostadil) bruges til at holde ductus arteriosus åben hos nyfødte med duktusafhængig aortaobstruktion. Det er ikke et stofspecifikt fund. Misoprostol er oralt, har uterotoniske og teratogene effekter og anvendes ikke til dette formål. Indikationerne optrådte to gange i input, og dubletterne er slået sammen.

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [27678099](https://pubmed.ncbi.nlm.nih.gov/27678099/) | 2017 | RCT | Reproductive Sciences | Lavdosis mifepriston med selvadministreret misoprostol til ultratidlig medicinsk abort (744 kvinder). Amenoré er her inklusionskriterium (graviditet), ikke behandlingsmål. |
| [25394644](https://pubmed.ncbi.nlm.nih.gov/25394644/) | 2015 | RCT (dosisfinding) | Reproductive Sciences | 2.500 kvinder med ultratidlig graviditet fik mifepriston i faldende doser efterfulgt af 200 µg oralt misoprostol. Primært endepunkt var komplet abort uden kirurgi. |
| [26405260](https://pubmed.ncbi.nlm.nih.gov/26405260/) | 2015 | Prospektivt gennemførlighedsstudie | Human Reproduction | Forebyggelse af uønsket graviditet med lavdosis mifepriston og misoprostol før forventet menstruation. |
| [29974571](https://pubmed.ncbi.nlm.nih.gov/29974571/) | 2018 | Prospektivt studie | J Obstet Gynaecol Res | Sikkerhed og effekt af selvadministreret misoprostol med lavdosis mifepriston ved tidlig graviditetsafbrydelse. |
| [1486304](https://pubmed.ncbi.nlm.nih.gov/1486304/) | 1992 | Review/klinisk rapport | BMJ | Medicinsk håndtering af missed abortion og anembryonal graviditet. Abstract mangler. |
| [26001691](https://pubmed.ncbi.nlm.nih.gov/26001691/) | 2015 | Review | J Obstet Gynaecol Can | Endometrieablation ved abnorm uterin blødning. Omhandler ikke misoprostol. |
| [37113350](https://pubmed.ncbi.nlm.nih.gov/37113350/) | 2023 | Case report | Cureus | Akut fedtlever i graviditeten. Amenoré er blot et præsentationssymptom, og artiklen handler ikke om misoprostols effekt. |

Samlet vurdering: Publikationerne handler om graviditetsafbrydelse eller graviditetsrelaterede tilstande. Ingen undersøger misoprostol som behandling af amenoré.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Producent |
|---------|------|------|-----------|
| 28105745216 | Angusta | Tabletter (oral) | Norgine B.V. |

---

## Sikkerhedsovervejelser

Der foreligger ikke sikkerhedsdata i datagrundlaget. Se det godkendte produktresumé (SmPC) for sikkerhedsinformation. Pakkeindlægget fra Lægemiddelstyrelsen er endnu ikke indhentet.

Misoprostol har uterotoniske og teratogene effekter. Det er særligt relevant, hvis stoffet overvejes til kvinder i den fødedygtige alder.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
- Evidensen består af indirekte litteratur om graviditetsafbrydelse og ingen kliniske forsøg. Der er ingen plausibel mekanisme for behandling af amenoré.
- Den høje modelscore er mest sandsynligt et artefakt af vidensgrafens struktur.
- Sikkerhedsscreeningen kan ikke gennemføres, før produktresuméet er indhentet.

**For at komme videre kræves:**
- Hentning og analyse af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer). Dette er en blokerende datamangel.
- Detaljerede data om virkningsmekanisme, f.eks. via DrugBank.
- Angivelse af den godkendte indikationstekst for Angusta, så den oprindelige indikation kan sammenholdes med den forudsagte.
- Mekanistisk og klinisk begrundelse for, at misoprostol kan være relevant ved amenoré, ud over graviditetsrelateret nærhed i grafen.
- Gennemgang af, om forudsigelsen skyldes graviditetsrelaterede termer, før den tillægges værdi.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelomplacering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

