---
layout: default
title: Articaine
parent: Kun modelforudsigelse (L5)
nav_order: 78
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Articaine: forudsagt ny indikation Gigt (gout) (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (articain er et lokalanæstetikum…"
---

# Articaine
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

# Articain: Fra lokalbedøvelse til gigt (gout)

## Opsummering i en sætning

Articain er et amidtype-lokalanæstetikum, som er markedsført i Danmark, men hvor den godkendte indikationstekst ikke indgår i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at det kan have effekt ved **gigt (gout)**, men der er **0 kliniske forsøg** og **0 publikationer** til støtte for netop denne retning.
Forudsigelsen er derfor udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (articain er et lokalanæstetikum, bl.a. brugt i tandlægepraksis) |
| Forudsagt ny indikation | Gigt (gout) |
| TxGNN-forudsigelsesscore | 99,58 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 2 |
| Anbefalet beslutning | Hold |

Andre forudsagte indikationer i data: eksostose (99,42 %), allergisk astma (99,38 %) og intrinsisk astma (99,34 %). Alle er på evidensniveau L5 med anbefalingen Hold.

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de indsamlede data. Articain er et amidtype-lokalanæstetikum, som blokerer spændingsstyrede natriumkanaler. Dets virkning som lokalbedøvelse er veletableret, men der er ikke identificeret nogen mekanistisk forbindelse til urinsyrestofskiftet eller til den inflammation, der kendetegner et giftanfald.

Forudsigelsen er derfor en ren beregningsmæssig sammenhæng fra videngrafen. Den høje score (0,996) bør ikke tolkes som klinisk støtte, da den ikke bakkes op af forsøg eller litteratur. Ligheden mellem den oprindelige og den nye indikation er endnu ikke vurderet.

De øvrige forudsagte indikationer er heller ikke understøttet. Der er ingen plausibel mekanisme for eksostose (en knoglevækstlidelse), og for astma er der ingen evidens for, at natriumkanalblokade har en terapeutisk rolle.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der er i øjeblikket ingen relateret litteratur for gigt.

For fuldstændighedens skyld blev der for den forudsagte indikation allergisk astma fundet to publikationer. De handler om overfølsomhedsreaktioner over for lokalanæstetika og er ikke evidens for effekt:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [38404118](https://pubmed.ncbi.nlm.nih.gov/38404118/) | 2024 | Kohortestudie | Pediatric Allergy and Immunology | Vurdering af diagnostiske tests for allergi over for lokalanæstetika hos børn |
| [21507228](https://pubmed.ncbi.nlm.nih.gov/21507228/) | 2011 | Case-rapport/eksperimentelt allergistudie | Allergy, Asthma, and Clinical Immunology | Forsinket allergi over for prilocain; ingen krydsreaktivitet over for bl.a. articain |

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107364425 | Norardent (Laboratorios Normon S.A.) | Injektionsvæske, opløsning | Ikke angivet |
| 28104355908 | Dentocaine (Laboratorios INIBSA, S.A.) | Injektionsvæske, opløsning | Ikke angivet |

---

## Sikkerhedsovervejelser

Oplysninger fra produktresuméet (advarsler og kontraindikationer) mangler i de indsamlede data. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

**Kontraindikationer fra videnbasen (ikke fra produkttekst):** Videngrafen (PrimeKG) markerer bl.a. følgende tilstande som kontraindikationer: hypertension, nyre- og leversygdom, galdeblæresygdom, diabetes og diabetisk ketoacidose, iskæmisk hjertesygdom og tidligere hjerteinfarkt, pludseligt hjertestop, ledningsforstyrrelser i hjertet, kardiomyopati, snævervinklet glaukom, myasthenia gravis, butyrylcholinesterase-mangel, hyperthyroidisme (Graves sygdom, thyreotoksikose), Parkinsons sygdom og hæmoglobinopati. Disse skal verificeres mod produktresuméet.

**Lægemiddelinteraktioner (13 registreret):**
- **Større:** Salpetersyrling (nitrous acid)
- **Moderate:** Liposomal morfin, benzocain (topisk), lidocain (topisk og oftalmisk), oxybuprocain (oftalmisk), cinchocain (topisk), tetracain (topisk og oftalmisk)
- **Mindre:** Hyaluronidase

**Overfølsomhed:** De fundne publikationer viser, at lokalanæstetika kan udløse allergiske reaktioner, hvilket er relevant at overveje hos allergiske patienter.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om gigt bygger udelukkende på modelscoren (evidensniveau L5). Der er hverken kliniske forsøg, litteratur eller en plausibel mekanisme, og de nødvendige sikkerhedsdata fra produktresuméet mangler.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméer fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendte indikationer), da manglen er blokerende for sikkerhedsscreeningen
- Data om virkningsmekanisme fra DrugBank
- En mekanistisk hypotese og præklinisk understøttelse for en rolle i gigt, før en klinisk vurdering overhovedet er relevant
- Vurdering af administrationsvej: articain findes kun som injektionsvæske, og kompatibilitet med den ønskede behandlingsvej er ikke afklaret
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

