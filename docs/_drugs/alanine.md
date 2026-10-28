---
layout: default
title: Alanine
parent: Kun modelforudsigelse (L5)
nav_order: 30
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-28
description: "Alanine: forudsagt ny indikation Gastroparese (evidensniveau L5). Oprindelig indikation: Ikke angivet i de data…"
monitor_inn: "alanine"
predicted_indications: ["gastroparesis (disease)"]
---

# Alanine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **1** stk.
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

## Alanin: Fra ernæringsterapi til gastroparese
{: .text-alpha }

## Opsummering i én sætning

Alanin er en ikke-essentiel aminosyre, som indgår i en række parenterale ernæringsprodukter (infusionsvæsker) på det danske marked.
TxGNN-modellen forudsiger, at alanin kan have effekt på **gastroparese**,
men der er **ingen registrerede kliniske forsøg** og kun **3 publikationer** med indirekte relevans, så evidensen er meget svag.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de data, der er indsamlet til denne rapport (godkendelsesteksterne er tomme). Alanin indgår i produkter til parenteral ernæring |
| Forudsagt ny indikation | Gastroparese |
| TxGNN-forudsigelsesscore | 0,9937 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: mindst 20) |
| Antal markedsføringstilladelser | 20 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Data om alanins virkningsmekanisme er ikke tilgængelige. Alanin er en ikke-essentiel aminosyre, der indgår i glukose-alanin-cyklussen og i leverens glukoneogenese. Alanin er her en bestanddel af aminosyreopløsninger og kombinerede ernæringsprodukter. Dets rolle er næringstilførsel, ikke en kendt lægemiddelvirkning på mavetarmkanalen.

Der er ikke påvist en troværdig mekanistisk sammenhæng mellem alanin og gastroparese. Den høje score (0,9937) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens. Scoren er alene en beregnet forudsigelse. Den fundne litteratur handler om lever- og mave-tarm-komplikationer ved diabetes og terminal nyresvigt (fx diabetisk hepatosklerose og glykogenhepatopati), hvor gastroparese nævnes som samtidig tilstand. Forbindelsen til alanin er derfor højst indirekte, via diabetesrelateret stofskifte- og leverpatologi. Intet studie viser, at alanin påvirker mavesækkens motilitet, tømningshastighed eller gastroparesesymptomer.

---

## Kliniske forsøg

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [10926110](https://pubmed.ncbi.nlm.nih.gov/10926110/) | 2000 | Review | Advances in Renal Replacement Therapy | Gennemgang af mave-tarm- og leversygdomme ved terminal nyresvigt og nyretransplantation; gastroparese er hyppigere ved kronisk nyresvigt. Omtaler ikke alanin |
| [26315331](https://pubmed.ncbi.nlm.nih.gov/26315331/) | 2016 | Review | Diabetic Medicine | Diabetisk hepatosklerose som mulig mikrovaskulær komplikation til diabetes. Ingen direkte relation til alanin eller gastroparese |
| [33763324](https://pubmed.ncbi.nlm.nih.gov/33763324/) | 2021 | Review (case) | Cureus | Case om glykogenhepatopati hos en type 1-diabetiker, der også havde gastroparese. Ingen direkte relation til alanin |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105502614 | Nutriflex Omega Plus | Infusionsvæske, emulsion | Ikke angivet |
| 28103074999 | Aminoven 10% | Infusionsvæske, opløsning | Ikke angivet |
| 28107044823 | Maapliv | Infusionsvæske, opløsning | Ikke angivet |
| 28105461714 | Nutriflex Omega Special elektrolytfri | Infusionsvæske, emulsion | Ikke angivet |
| 28105186912 | Aminoplasmal | Infusionsvæske, opløsning | Ikke angivet |

Der er i alt 20 gyldige tilladelser (alle enkeltstofprodukter); her vises de 5 første. Øvrige produkter omfatter bl.a. Vamin, Amiped, Nutrineal PD4 (peritonealdialysevæske), Numeta, Vaminolac, Clinimix, Olimel, SmofKabiven og Kabiven.

---

## Sikkerhedsovervejelser

Der foreligger ingen produktresumédata om advarsler, kontraindikationer eller interaktioner i de data, der er indsamlet til denne rapport.

Videngrafen (PrimeKG) angiver dog mulige kontraindikationer mellem alanin og følgende tilstande. Disse stammer ikke fra produktresuméer og bør verificeres:
- **Nyre**: nyresygdom, kronisk nyresygdom, kronisk nyresvigt, terminal nyresvigt, nefrolithiasis, nefrokalcinose, akut uratnefropati
- **Kalk- og fosfatstofskifte**: hyperkalcæmi, human maligenitetsrelateret hyperkalcæmi, sarkoidose, fosforstofskiftesygdom
- **Hjerte-kar**: hjertesygdom, kardiovaskulær sygdom, ventrikelflimren, digitalisforgiftning
- **Stofskifte**: fenylketonuri og forstyrrelser i fenylalaninstofskiftet

Se i øvrigt det godkendte produktresumé for de enkelte produkter.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (evidensniveau L5), uden kliniske forsøg og uden en plausibel mekanisme. Litteraturen er indirekte og belyser ikke alanins effekt på gastroparese. Desuden er sikkerhedsdata ufuldstændige.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) og en vurdering af, om alanin kan påvirke mavesækkens motilitet
- Præklinisk eller eksplorativ klinisk dokumentation for effekt på gastroparese
- Produktresuméer med advarsler og kontraindikationer samt gennemgang af de kontraindikationer, videngrafen angiver (især nyre- og hjertesygdom)
- Afklaring af godkendte indikationer, administrationsvej og dosering (nuværende produkter er infusionsvæsker; gastroparese behandles normalt enteralt)
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

