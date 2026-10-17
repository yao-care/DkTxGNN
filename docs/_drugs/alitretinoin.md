---
layout: default
title: Alitretinoin
parent: Kun modelforudsigelse (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Alitretinoin: forudsagt ny indikation Amenoré (evidensniveau L5). Oprindelig indikation: Ikke angivet i den danske tilladelsestekst"
monitor_inn: "Alitretinoin"
predicted_indications: ["amenorrhea (disease)", "amenorrhea (disease)", "acne (disease)", "acne (disease)", "atypical coarctation of aorta", "atypical coarctation of aorta", "pregnancy associated osteoporosis", "pregnancy associated osteoporosis", "aortic malformation", "aortic malformation"]
---

# Alitretinoin
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

# Alitretinoin: Fra håndeksem til amenoré (prædiktion)

## Resumé i én sætning

Alitretinoin (9-cis-retinsyre) er et retinoid, som er markedsført i Danmark som bløde kapsler. Ifølge de data, der er sammenstillet til denne rapport, er lægemidlet kendt for behandling af svær kronisk håndeksem og Kaposis sarkom. TxGNN-modellen forudsiger, at det kan have effekt ved **amenoré**, men der er **0 kliniske forsøg** og **0 publikationer** om netop denne indikation. Evidensen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i den danske tilladelsestekst (kendt anvendelse ifølge farmakologidata: svær kronisk håndeksem, der ikke responderer på potente topikale kortikosteroider) |
| Forudsagt ny indikation | Amenoré |
| TxGNN-prædiktionsscore | 99,99 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne prædiktion rimelig?

Data om lægemidlets virkningsmekanisme er ikke tilgængelige i detaljeret form. Farmakologidata viser dog, at alitretinoin binder til retinsyrereceptorerne (RARα, RARβ, RARγ) og retinoid X-receptorerne (RXRα, RXRβ, RXRγ). Det er således en pan-retinoid receptoragonist, som påvirker celledifferentiering.

Der er ingen understøttet mekanistisk begrundelse for, at alitretinoin skulle virke ved amenoré. En påvirkning af reproduktiv endokrin signalering er spekulativ. Den høje score (0,9999) er alene en beregnet forudsigelse. Retinoider er desuden teratogene, hvilket gør en indikation inden for kvinders reproduktive sundhed problematisk uden yderligere begrundelse.

**Øvrige forudsigelser:** Modellen foreslog også akne, atypisk coarctatio aortae, graviditetsassocieret osteoporose og aortamisdannelse. Akne er biologisk plausibelt (retinoider normaliserer keratinocytdifferentiering og dæmper talgkirtelaktivitet), men understøttes kun indirekte af to generelle oversigtsartikler. De øvrige har ingen plausibel behandlingsmekanisme; retinsyresignalering er vigtig for fosterudvikling, men det vedrører teratogenicitet og ikke terapeutisk effekt.

---

## Evidens fra kliniske forsøg

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

For den primære forudsigelse (amenoré) er der på nuværende tidspunkt ingen relateret litteratur. Til sammenligning findes følgende generelle oversigtsartikler for den sekundære forudsigelse akne (kun indirekte støtte):

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [41692081](https://pubmed.ncbi.nlm.nih.gov/41692081/) | 2026 | Oversigtsartikel | Clinics in Dermatology | Gennemgang af vitamin A og retinoider i dermatologi, herunder orale retinoider som isotretinoin, acitretin, alitretinoin og bexaroten |
| [11586072](https://pubmed.ncbi.nlm.nih.gov/11586072/) | 2001 | Oversigtsartikel | Skin Pharmacology and Applied Skin Physiology | Retinoiders virkning via nukleære receptorer og mulige fremtidige dermatologiske indikationer |

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107150024 | Alitretinoin "Nordic Prime" (Nordic Prime ApS) | Kapsler, bløde | Indikationstekst ikke angivet |

---

## Cytotoksicitet

Alitretinoin anvendes ikke primært som cytostatikum i den danske godkendelse, så dette afsnit er udeladt.

---

## Sikkerhedsovervejelser

- **Kontraindikationer (fra vidensgraf, ikke produktresumé):** TxGNN-vidensgrafen (PrimeKG) angiver kontraindikationskanter til mycosis fungoides og varianter, primært kutant T-cellelymfom, follikulotrop mycosis fungoides, lokaliseret pagetoid retikulose og granulomatøs slack skin.
- **Teratogenicitet:** Retinoider er teratogene og kontraindiceret under graviditet. Enhver udvikling kræver strenge graviditetsforebyggende foranstaltninger.
- **Farmakologiske interaktioner:** Alitretinoin binder til RARα/β/γ og RXRα/β/γ samt til VKORC1 (vitamin K-epoxidreduktase), hvilket kan have betydning for samtidig behandling med vitamin K-antagonister. Der er ikke angivet interaktionsniveauer.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Prædiktionen for amenoré bygger udelukkende på en beregnet modelscore (evidensniveau L5) uden kliniske forsøg, litteratur eller plausibel mekanisme. Teratogenicitet gør indikationen yderligere problematisk.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra produktresuméet hos Lægemiddelstyrelsen
- Præklinisk eller klinisk evidens, der specifikt understøtter en terapeutisk effekt ved amenoré
- Alternativt at prioritere akne som forskningsspørgsmål (evidensniveau L4) med strenge graviditetsforebyggende tiltag
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

