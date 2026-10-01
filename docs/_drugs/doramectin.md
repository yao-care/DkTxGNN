---
layout: default
title: Doramectin
parent: Kun modelforudsigelse (L5)
nav_order: 148
evidence_level: L5
indication_count: 10
---

# Doramectin
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

# Doramectin: Fra veterinært antiparasitmiddel til insomni (søvnløshed)

## Resumé i få sætninger

Doramectin er et antiparasitært middel af avermectin-klassen, og i Danmark er det kun registreret som veterinærlægemiddel (Dectomax, pour-on).
TxGNN-modellen forudsiger, at det kan have effekt ved **insomni**, men forudsigelsen bygger udelukkende på modellen: der er **0 kliniske forsøg** og **0 publikationer** for netop denne indikation.
Det eneste indirekte fund er to prækliniske rottestudier om **angst**, som ikke kan overføres direkte til mennesker.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig anvendelse | Veterinært antiparasitmiddel (pour-on til dyr) |
| Foreslået ny indikation | Insomni (insomnia) |
| TxGNN-score | 99,2 % |
| Evidensniveau | L5 (kun modelforudsigelse). For angst er niveauet L4 (prækliniske data) |
| Markedsstatus i Danmark | Markedsført (som veterinærlægemiddel) |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor kan forudsigelsen give mening?

Der foreligger ingen detaljerede data om virkningsmekanismen (MOA) i Evidence Pack. Doramectin tilhører avermectin-klassen, og for denne klasse er det kendt, at stofferne kan potensere GABA-A-receptorer hos pattedyr. Det kunne i teorien give en beroligende effekt og dermed en mulig forbindelse til søvnforstyrrelser. Det er dog spekulativt og ikke understøttet af data for insomni.

Der er også tungtvejende modargumenter. Doramectin er designet til dyr, og P-glykoprotein begrænser stoffets passage over blod-hjerne-barrieren hos pattedyr. Neurotoksicitetsrisikoen er ikke kvantificeret. Lægemidlet har desuden ingen registrerede oprindelige humane indikationer, så der er ikke noget klinisk udgangspunkt at sammenligne med.

TxGNN forudsagde følgende, hvor dubletter i datasættet kun er talt én gang:

| Forudsagt indikation | Score | Evidensniveau | Anbefaling |
|------|------|------|------|
| Insomni | 99,2 % | L5 | Hold |
| Søvnforstyrrelse (indsovning og søvnvedligeholdelse) | 92,3 % | L5 | Hold |
| Angst | 91,8 % | L4 | Forskningsspørgsmål |
| Agorafobi | 91,8 % | L5 | Hold |
| Angstlidelse | 91,2 % | L5 | Hold |

Søvnforstyrrelse er næsten synonym med insomni og deler samme spekulative GABAerge begrundelse, så den udgør ikke selvstændig støtte.

---

## Kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for nogen af de forudsagte indikationer.

---

## Litteratur

For insomni er der ingen relateret litteratur. Der findes dog to prækliniske studier under indikationen **angst**, som kun er indirekte kontekst:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [11246508](https://pubmed.ncbi.nlm.nih.gov/11246508/) | 2000 | Præklinisk dyrestudie (rotte) | Comp Biochem Physiol Toxicol Pharmacol | Doramectin (100, 300 og 1000 µg/kg s.c.) undersøgt i angstmodeller, krampetærskel og neurotransmittere. Forfatterne beskriver angstlignende og antikonvulsive effekter via GABAerg påvirkning |
| [12184502](https://pubmed.ncbi.nlm.nih.gov/12184502/) | 2002 | Præklinisk dyrestudie (rotte, beslægtet stof ivermectin) | Vet Res Commun | Mulige angstdæmpende effekter af ivermectin hos rotter. Henviser til tidligere fund for doramectin |

Der er ingen humane data, og der er heller ingen dosis- eller sikkerhedsdata for brug i centralnervesystemet.

---

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Indehaver |
|---------|------|------|-----------|
| 28104654310 | Dectomax | Pour-on, opløsning | Zoetis Animal Health ApS |

Produktet er et veterinærlægemiddel. Der er ingen centrale (EMA) tilladelser i datasættet. Administrationsvejen (pour-on på huden) er desuden ikke vurderet i forhold til en eventuel human indikation.

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller interaktioner (interaktionsopslaget gav ingen resultater).
Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Da der er tale om et veterinærlægemiddel, er der ikke vurderet humane sikkerhedsdata.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for insomni er ren modelforudsigelse (L5) uden kliniske forsøg eller litteratur. Den eneste indirekte støtte er to rottestudier om angst, og et veterinært middel med begrænset hjernepenetration og ukendt neurotoksicitet kan ikke tages videre uden en grundig sikkerhedsvurdering. Angst kan højst betragtes som et forskningsspørgsmål.

**For at komme videre kræves:**
- Produktresumé/indlægsseddel fra Lægemiddelstyrelsen med advarsler og kontraindikationer. Dette er en blokerende datamangel, da sikkerhedsscreening ikke kan gennemføres uden.
- Data om virkningsmekanisme (MOA), fx fra DrugBank.
- Prækliniske data om blod-hjerne-barriere-passage og neurotoksicitet hos pattedyr, herunder P-glykoprotein-effekter.
- Vurdering af, om en human formulering og administrationsvej overhovedet er mulig.
- Evt. et målrettet litteraturstudie af avermectiner og GABA-A-modulering, før der overvejes forsøg.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelserne skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

