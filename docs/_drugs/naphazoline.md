---
layout: default
title: Naphazoline
parent: Kun modelforudsigelse (L5)
nav_order: 574
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Naphazoline: forudsagt ny indikation Hypotrichosis simplex i hovedbunden (evidensniveau L5). Oprindelig indikation: Ikke angivet i de data…"
---

# Naphazoline
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

# Naphazolin: Fra øjenrødme til hypotrichosis simplex i hovedbunden

## Resumé i én sætning

Naphazolin er en lokalt virkende alfa-adrenerg vasokonstriktor, som er godkendt i Danmark som øjendråber (Cleareyes) til at mindske rødme i øjnene.
TxGNN-modellen forudsiger, at stoffet kan have effekt på **hypotrichosis simplex i hovedbunden**.
Forudsigelsen er **ikke understøttet af kliniske forsøg eller publikationer** (0 kliniske forsøg og 0 relevante publikationer), og den er derfor udelukkende en modelprognose.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de data, der er indsamlet til denne rapport. Den kliniske anvendelse er lindring af øjenrødme (vasokonstriktion af hævede blodkar i øjet) |
| Forudsagt ny indikation | Hypotrichosis simplex i hovedbunden |
| TxGNN-forudsigelsesscore | 99,83 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ikke detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Naphazolin er kendt som agonist ved alfa-adrenerge receptorer (α1A, α2A og α2C) og virker som vasokonstriktor, der indsnævrer hævede blodkar og dermed mindsker rødme.

Der er ingen oplagt mekanistisk sammenhæng mellem denne virkning og hårvækst ved en genetisk betinget hypotrichosis. Vasokonstriktion i hovedbundens kar ville tværtimod, om noget, kunne forringe follikelperfusionen. Etablerede behandlinger mod hårtab virker via andre mekanismer, f.eks. åbning af kaliumkanaler (minoxidil), hæmning af 5-alfa-reduktase eller immunmodulering, og ingen af disse gælder for naphazolin.

Den høje score (0,998) afspejler sandsynligvis nærhed i vidensgrafen til andre hårrelaterede sygdomsknuder snarere end reel farmakologi. Det understøttes af, at modellen også forudsiger modsatrettede fænotyper (hypotrichosis/alopeci og hypertrichosis) med næsten samme score, hvilket tyder på artefakter i grafen.

### Øvrige forudsigelser med samme begrænsninger

Alle de ti højest rangerede forudsigelser har evidensniveau L5 og anbefalingen Hold. Blandt dem er congenital hypotrichosis milia, diffus alopecia areata, alopeci, primært arveligt glaukom, hypertrichosis, Ambras-type hypertrichosis universalis congenita, åbenvinklet glaukom samt to medfødte misdannelsessyndromer. Ingen af dem har et plausibelt mekanistisk grundlag. For glaukom er der desuden et sikkerhedssignal (se nedenfor).

---

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur for den primære forudsigelse (hypotrichosis simplex i hovedbunden).

For den ottende forudsigelse (åbenvinklet glaukom) blev der fundet én publikation, som dog ikke omhandler naphazolin og ikke er relevant evidens:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [1295525](https://pubmed.ncbi.nlm.nih.gov/1295525/) | 1992 | Andet (laser-/kortikosteroidstudie) | Australian and New Zealand Journal of Ophthalmology | Effekt af topikale kortikosteroider på laserinducerede perifere anteriore synekier efter argon-laser-trabekuloplastik. Omhandler ikke naphazolin |

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105194512 | Cleareyes (Elara Pharmaservices Europe Ltd.) | Øjendråber, opløsning | Indikationsteksten er ikke angivet i de data, der er indsamlet til denne rapport |

---

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer er ikke tilgængelige i de data, der er indsamlet til denne rapport. Vidensgrafen (PrimeKG) indeholder dog kontraindikationsforbindelser mellem naphazolin og følgende sygdomme (dette er ikke tekst fra produktresuméet og skal verificeres):

- **Hjerte-kar:** hypertension (forhøjet blodtryk), hjertesygdom og hjerte-kar-sygdom generelt
- **Stofskifte:** hyperglykæmi, diabetes mellitus, diabetisk ketoacidose
- **Skjoldbruskkirtel:** hyperthyroidisme, Graves' sygdom, thyreotoksikose
- **Øjet:** snævervinklet glaukom (vinkellukningsglaukom), infektiøse øjensygdomme og konjunktivitis

Alfa-agonistisk mydriasis kan udløse vinkellukning, hvorfor stoffet generelt bør anvendes med forsigtighed eller undgås ved snævervinklet glaukom. Dette taler imod repurposing til glaukomindikationer.

**Farmakologiske målproteiner (ikke lægemiddelinteraktioner i klassisk forstand):** α1A-adrenoceptor (ADRA1A), α2A-adrenoceptor (ADRA2A), α2C-adrenoceptor (ADRA2C) og museproteinet TAAR4P/Taar4.

Der henvises i øvrigt til det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er alene baseret på en modelscore uden kliniske forsøg eller relevant litteratur, og der er ingen plausibel mekanisme, der forbinder en alfa-adrenerg vasokonstriktor med hårvækst. Vasokonstriktion kan potentielt være kontraproduktivt, og for glaukomrelaterede forudsigelser er der et sikkerhedssignal.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméet (SmPC) fra Lægemiddelstyrelsen, herunder godkendt indikation, advarsler og kontraindikationer
- Data om virkningsmekanisme (MOA) fra DrugBank
- Præklinisk eller mekanistisk evidens for en eventuel effekt på hårfollikler, før der overvejes kliniske studier
- Afklaring af, om en topikal formulering til hovedbunden overhovedet er relevant, da der kun findes øjendråber på det danske marked
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

