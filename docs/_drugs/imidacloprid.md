---
layout: default
title: Imidacloprid
parent: Kun modelforudsigelse (L5)
nav_order: 427
evidence_level: L5
indication_count: 9
monitor_inn: "Imidacloprid"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome", "non-syndromic esophageal malformation", "esophageal disease", "mitral valve prolapse (disease)", "neurocirculatory asthenia", "familial mitral valve prolapse", "MVP1"]
last_modified_at: 2026-10-23
description: "Imidacloprid: forudsagt ny indikation Cauda equina-syndrom (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data"
---

# Imidacloprid
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **9** stk.
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

## Imidacloprid: Fra ingen godkendt human indikation til cauda equina-syndrom
{: .text-alpha }

## Resumé i én sætning

Imidacloprid er et neonikotinoid insekticid, som i Danmark kun er registreret som dyrelægemiddel (Advantage Vet. til hund) og ikke har nogen godkendt human terapeutisk anvendelse.
TxGNN-modellen forudsiger, at stoffet kan have effekt ved **cauda equina-syndrom**, men der foreligger **ingen kliniske forsøg** og **ingen publikationer**, som direkte undersøger denne sygdom. Forudsigelsen bygger udelukkende på en grafbaseret model.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (den eneste danske tilladelse er et dyrelægemiddel til hund uden registreret indikationstekst) |
| Forudsagt ny indikation | Cauda equina-syndrom |
| TxGNN-forudsigelsesscore | 0,9999 |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Data om imidacloprids detaljerede virkningsmekanisme er ikke tilgængelige i de indsamlede data. Det er dog kendt, at imidacloprid er et neonikotinoid, der virker som agonist på nikotinerge acetylcholinreceptorer (nAChR) hos insekter. Stoffet er selektivt for insekters receptorer og har kun svag affinitet til pattedyrreceptorer.

Cauda equina-syndrom skyldes kompression af nerverødder i den nederste del af rygmarvskanalen. Der er ingen plausibel mekanisme, der forbinder agonisme af insekt-nAChR med aflastning af nerverodskompression. Stoffets kendte neurotoksiske potentiale hos pattedyr taler desuden imod en gavnlig effekt. Den høje score stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, og er ikke biologisk evidens.

De øvrige forudsagte indikationer (fx obsolet neurogen blære, irritabel tarm-syndrom, esophagussygdom, mitralklapprolaps og neurocirkulatorisk asteni) har samme svaghed: Der findes en løs teoretisk kolinerg forbindelse for nogle af dem, men ingen data, som viser terapeutisk effekt. For de strukturelle og arvelige tilstande (medfødt esophagusmisdannelse og de forskellige former for mitralklapprolaps) er der ingen mekanistisk begrundelse overhovedet.

---

## Evidens fra kliniske forsøg

Der er aktuelt ingen relaterede kliniske forsøg registreret for cauda equina-syndrom.

---

## Litteraturevidens

Der er aktuelt ingen relateret litteratur for cauda equina-syndrom.

Til sammenligning findes der for den femte forudsagte indikation (esophagussygdom) én publikation, som dog er et dyrestudie og ikke kan overføres til mennesker:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [29506575](https://pubmed.ncbi.nlm.nih.gov/29506575/) | 2018 | Veterinært klinisk studie (dobbeltblindet, placebokontrolleret) | Parasites & Vectors | Sammenligning af et spot-on-præparat med imidacloprid og moxidectin (Advocate®) med injicerbart doramectin ved esophageal spirocercose hos hunde. Effekten skyldes antiparasitær aktivitet og er ikke evidens for human esophagussygdom. |

---

## Information om det danske marked

| Tilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101891197 | Advantage Vet. til hund (Elanco Animal Health GmbH) | Kutanopløsning | Ikke angivet |

Der er tale om ét dyrelægemiddel, som er gyldigt og markedsført. Tilladelsen omfatter ikke human anvendelse.

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller lægemiddelinteraktioner for imidacloprid i de indsamlede data. Der er heller ikke fundet registrerede interaktioner.

Det er dog bemærkelsesværdigt, at stoffets kendte neurotoksiske potentiale hos pattedyr udgør en væsentlig sikkerhedsbekymring ved enhver overvejelse af human anvendelse.

Se det godkendte produktresumé (SmPC) for sikkerhedsinformation om det registrerede dyrelægemiddel.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er rent beregningsbaseret (evidensniveau L5) uden kliniske forsøg eller litteratur, der direkte undersøger cauda equina-syndrom. Der er ingen plausibel mekanisme, og stoffets neurotoksiske potentiale hos pattedyr taler imod terapeutisk anvendelse.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen
- Prækliniske data, der kan understøtte en biologisk sammenhæng mellem stoffet og sygdommen
- En grundig toksikologisk vurdering af human eksponering, før der overvejes yderligere undersøgelser
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

