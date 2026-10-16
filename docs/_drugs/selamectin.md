---
layout: default
title: Selamectin
parent: Kun modelforudsigelse (L5)
nav_order: 751
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Selamectin: forudsagt ny indikation Candidiasis (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (indikationsteksten for det dansk…"
---

# Selamectin
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

# Selamectin: Fra veterinær parasitbehandling til candidiasis

## Resumé

Selamectin er et makrocyklisk lakton mod parasitter, som i Danmark er markedsført som spot-on-opløsning til hunde (veterinærlægemiddel). TxGNN-modellen forudsiger, at stoffet kan have effekt mod **candidiasis**, men de data, der er indsamlet til denne rapport, indeholder **ingen kliniske forsøg og ingen publikationer** om denne indikation. Forudsigelsen er alene modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (indikationsteksten for det danske produkt er tom). Stoffet kendes som antiparasitært middel til dyr. |
| Forudsagt ny indikation | Candidiasis |
| TxGNN-forudsigelsesscore | 98,4 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen i de indsamlede data. Det er kendt, at selamectin er et makrocyklisk lakton, som virker på glutamatstyrede kloridkanaler hos hvirvelløse dyr, og at det anvendes mod parasitter hos dyr.

Svampe som *Candida* har ikke disse kanaler, så antifungal virkning kan ikke forventes ud fra den kendte mekanisme. Der er derfor ikke noget mekanistisk grundlag for forudsigelsen i de foreliggende data. Den høje score (0,984) afspejler sandsynligvis nærhed i videngrafen snarere end biologisk sandsynlighed.

**Øvrige forudsigelser fra modellen** har tilsvarende høje scorer, men heller ikke støtte i data:

| Forudsagt indikation | TxGNN-score | Evidensniveau | Bemærkning |
|------|------|------|------|
| Candidiasis | 98,4 % | L5 | Ingen mekanistisk sammenhæng; ingen forsøg eller litteratur |
| Spedalskhed (leprosy) | 98,4 % | L5 | Bakteriel sygdom (*Mycobacterium leprae*); selamectin har ingen kendt antibakteriel virkning |
| Koronararteriesygdom | 98,1 % | L5 | Ingen kendt rolle i koronar vaskulær biologi |
| Myokardieiskæmi | 97,9 % | L5 | Ingen kendt effekt på myokardiets perfusion |
| Hjertesygdom | 97,9 % | L5 | Kun indirekte veterinær litteratur om hjerteorm (se nedenfor) |

---

## Kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er ingen litteratur om candidiasis. Den eneste litteratur i de indsamlede data vedrører den sekundære forudsigelse "hjertesygdom". Den er udelukkende veterinær og viser ikke, at selamectin behandler hjertesygdom hos mennesker.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [29143659](https://pubmed.ncbi.nlm.nih.gov/29143659/) | 2017 | Veterinærstudie | Parasites & Vectors | Effekt af hjerteorm (*Dirofilaria immitis*) og hjerteormsassocieret luftvejssygdom på højre ventrikel hos katte |
| [25288308](https://pubmed.ncbi.nlm.nih.gov/25288308/) | 2014 | Kontrolleret veterinærstudie | Veterinary Parasitology | Lungeskade ved hjerteorminfektion hos katte; en gruppe blev forbehandlet med selamectin lokalt |
| [33664624](https://pubmed.ncbi.nlm.nih.gov/33664624/) | 2021 | Case report | Helminthologia | Livstruende sameksistens af hjerteorm og lungeorm hos en kat i Bulgarien |
| [18556127](https://pubmed.ncbi.nlm.nih.gov/18556127/) | 2008 | Case report | Veterinary Parasitology | Dødelig anæmi og dermatitis hos agutier med lopper; behandlet med propoxur og selamectin (ikke relevant for hjertesygdom) |

Relevansen er kun indirekte: selamectin bruges til dyr som forebyggelse af hjerteorm, hvilket er parasitbekæmpelse og ikke en direkte kardial terapeutisk effekt.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106025117 | Chanhold til hund 10,1 - 20,0 kg (Chanelle Pharmaceuticals Manufacturing Limited) | Spot-on, opløsning | Ikke angivet i de tilgængelige data |

Der er kun én gyldig tilladelse (enkeltstof), og ingen er annulleret. Produktet er et veterinærlægemiddel til hunde, ikke til mennesker.

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller lægemiddelinteraktioner. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5) uden kliniske forsøg eller relevant litteratur. Den kendte virkningsmekanisme (glutamatstyrede kloridkanaler hos hvirvelløse dyr) taler imod antifungal effekt. Desuden er det eneste danske produkt et veterinærlægemiddel.

**For at komme videre kræves følgende:**
- Oplysninger om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen
- Præklinisk (in vitro) dokumentation for aktivitet mod *Candida*, før der overvejes yderligere vurdering
- Vurdering af, om en formulering til mennesker og en passende administrationsvej overhovedet er mulig, da der ikke findes en godkendt human formulering
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

