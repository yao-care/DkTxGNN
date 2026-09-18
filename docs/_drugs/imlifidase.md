---
layout: default
title: Imlifidase
parent: Kun modelforudsigelse (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
---

# Imlifidase
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

# Imlifidase: Fra Transplantationsdesensibilisering (Ubekræftet) til Diabetisk Grå Stær

## Et-sætnings Resumé

> Imlifidase (DrugBank DB15258) har ingen bekræftet oprindelig indikation i det aktuelle bevispakke — baggrundsviden antyder brug som en før-transplantations IgG-nedbrydende desensibiliseringsagent, men dette er **ikke hentet fra dette datasæt** og kræver manuel verifikation.
> TxGNN-modellen forudsiger potentiel relevans til **Diabetisk Grå Stær**, men dette understøttes af **0 kliniske forsøg** og **0 publikationer**, og modellens egen begrundelse markerer resultatet som muligvis en vidensgraf-klynge-artefakt snarere end et ægte farmakologisk signal.

---

## Hurtig Oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig Indikation | Ikke etableret i dette bevispakke — `original_indications` er tom og `original_moa` er markeret som et datahuller |
| Forudsagt Ny Indikation | Diabetisk Grå Stær |
| TxGNN Forudsigelsesscore | 98.75% |
| Evidensniveau | L5 (modelforudsigelse kun, ingen understøttende studier) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal Markedsføringstilladelser | 0 |
| Anbefalet Beslutning | **Vent** |

---

## Hvorfor er denne Forudsigelse Rimelig?

Detaljerede virkningsmekanisme-data er ikke tilgængelige for Imlifidase i dette bevispakke (`original_moa` = datahuller), og ingen oprindelig indikation er registreret. Baggrundsfarmakologisk viden — **ikke hentet fra dette datasæt og kræver uafhængig verifikation** — beskriver Imlifidase som en IgG-nedbrydende cystein-protease, der bruges til antistof-desensibilisering før organransplantation hos højt sensibiliserede patienter. Denne baggrund er inkluderet her kun fordi modellens egen repurposing-begrundelse præsenterer den; den bør bekræftes mod DrugBank/EMA/SmPC-kilder, før den er pålidelig.

Kritisk set er den modelgenererede begrundelse for denne forudsigelse selv skeptisk: den fastslår, at diabetisk grå stær-patologi drives af linse-proteinglykering, sorbitol-vejens akkumulation og oxidativ stress — mekanismer med **ingen kendt forbindelse** til IgG-spaltning eller komplementmedierede immunveje. Begrundelsen noterer eksplicit, at den høje TxGNN-score kan afspejle en **klynge-artefakt** i vidensgraf-rummet (sygdomsknuder for forskellige grå stær-subtyper indlejret tæt sammen) snarere end et ægte farmakologisk signal.

Dette understøttes af strukturen på den rangerede kandidatliste: 8 af de top 10 forudsigelser er grå stær-subtyper/varianter (diabetisk, kraniostenose, modne, tetanisk, umodne, type-2-diabetes-associerede) klynget på næsten identiske score (~98,7–98,75%), herunder eksakte dubletter. Dette mønster er konsistent med en embeddings-rum-artefakt, der påvirker en hel sygdomsklynge, snarere end en specifik, differentiet biologisk hypotese for Imlifidase. I betragtning af fravær af nogen mekanistisk, præklinkisk eller klinisk støtte bør denne forudsigelse behandles som udelukkende eksplorativ.

---

## Bevis fra Kliniske Forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om Dansk Marked

Imlifidase har i øjeblikket **ingen markedsføringstilladelse i Danmark** (`market_status`: Ikke markedsført; 0 registrerede licenser). Ingen produkt-, doseringsform- eller godkendt-indikationsdata er tilgængelig fra Laegemiddelstyrelsen eller EMA centraliserede poster i dette bevispakke.

---

## Sikkerhedsmæssige Overvejelser

Venligst se det godkendte Produktresumé (SmPC) for sikkerhedsinformation.

*(Bemærk: der blev ikke fundet data om lægemiddel-lægemiddel-interaktioner; vigtige advarsler og kontraindikationer er i øjeblikket utilgængelige og er markeret som et blokerande datahuller — se Næste Trin.)*

---

## Konklusion og Næste Trin

**Beslutning: Vent**

**Begrundelse:**
- Forudsigelsen har ingen bevis fra kliniske forsøg eller litteratur (Evidensniveau L5), og modellens egen mekanistiske begrundelse sætter spørgsmålstegn ved biologisk plausibilitet, hvilket tyder på en mulig vidensgraf-embeddings-artefakt, der påvirker en hel grå stær-subtype-klynge snarere end en specifik, troværdig hypotese.
- Oprindelig indikation og virkningsmekanisme-data mangler begge fra dette bevispakke, og et **blokerande** datahuller (manglende TFDA/lokal etiket-advarsler og kontraindikationer) forhindrer selv en foreløbig (S1) sikkerhedsvurdering.

**For at fortsætte er følgende nødvendig:**
- Bekræftet oprindelig indikation og virkningsmekanisme for Imlifidase (DG002, høj alvorlighed — forespørg DrugBank API)
- Lokale regulatoriske etiket-advarsler, kontraindikationer og sikkerhedsdata til at løse det blokerande huller (DG001 — indhent og parse SmPC/etiket PDF)
- Uafhængig farmakologisk vurdering af, hvorvidt der kan bestå nogen plausibel mekanistisk forbindelse mellem IgG-nedbrydende protease-aktivitet og diabetisk grå stær-patologi
- Afklaring af dublette/næsten-identiske rangerede kandidater, før dette signal betragtes som adskilt fra en bredere "grå stær-klynge"-artefakt
- Hvis forfølges videre, præklinkisk eller case-niveau-bevis, før nogen klinisk investering vurderes

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

