---
layout: default
title: Nemolizumab
parent: Kun modelforudsigelse (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Nemolizumab
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

# Nemolizumab: Fra atopisk dermatitis/pruritisk nodularis til diabetisk katarakt

## Resumé i en sætning

Nemolizumab er et monoklonalt antistof mod IL-31-receptorsubstans A (IL-31RA), beskrevet i bevismappe-noterne som godkendt for pruritus og inflammation ved atopisk dermatitis og pruritisk nodularis (en formel, registervurderet oprindelig indikation er ikke registreret). TxGNN-modellen forudsiger, at det kan være effektivt for **diabetisk katarakt**, men denne forudsigelse understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer**, og evidenspakkens egen mekanistiske analyse angiver, at der ikke er kendt biologisk forbindelse mellem IL-31-signalering og diabetisk linsepatologi.

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Atopisk dermatitis / Pruritisk nodularis (nævnt i repurposing-rationalet; ikke bekræftet via officiel dansk registrering — se note nedenfor) |
| Forudsagt ny indikation | Diabetisk katarakt |
| TxGNN-forudsigelsesscore | 98.55% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 |
| Anbefalet beslutning | Afvent |

*Note: `taiwan_regulatory.licenses` er tomt og `drug.original_indications` er ikke udfyldt, derfor er oprindelig indikation ovenfor hentet fra medicinen mekanistiske beskrivelse snarere end fra dansk Lægemiddelstyrelsesregistrering.*

## Hvorfor er denne forudsigelse rimelig?

Nemolizumab blokerer IL-31-signalering gennem IL-31RA, en vej, der er central for pruritus (kløe) og inflammation ved atopisk dermatitis og pruritisk nodularis. Dette er en neuroimmun/inflammatorisk mekanisme, ikke en metabolsk eller okular.

Diabetisk katarakt er derimod drevet af linsespezifikk metabolsk patologi — osmotisk skade fra polyol (sorbitol)-stien, oxidativ stress og ophobning af avancerede glykerings slutprodukter (AGEs). Evidenspakkens eget repurposing-rationale er eksplicit om, at der ikke eksisterer nogen publiceret eller mekanistisk forbindelse mellem IL-31/IL-31RA-blokade og disse linseskadende processer.

Givet dette ser forudsigelsen ud til at være et artefakt af TxGNN's knowledge-graph-embedding-lighed snarere end en biologisk velbegrundet hypotese. Den høje forudsigelsesscore (98.55%) afspejler graphniveaushgelighed, ikke farmakologisk plausibilitet, og samme score deles på tværs af flere urelaterede katarakt-subtyper (diabetisk, tetanisk, kraniostenosis-associeret, umoden, moden), hvilket yderligere tyder på, at modellen grupperer på det generelle "katarakt"-diseasenode snarere end en diabetesspecifik mekanisme.

## Klinisk forsøgsevidensevidence

Aktuelt ingen relaterede kliniske forsøg registreret.

## Litteraturevidensence

Aktuelt ingen relateret litteratur tilgængelig.

## Markedsinformation for Danmark

Nemolizumab har i øjeblikket **ingen markedsføringsgodkendelse** i Danmark (markedsstatus: Ikke markedsført; 0 licenser på fil), så detaljer om national eller centraliseret (EMA) godkendelse er ikke tilgængelige til at rapportere.

## Sikkerhedsovervejelser

Se venligst den godkendte produktresuméet (SmPC) for sikkerhedsinformation. Danmarks mærkningsadvarsler, kontraindikationer og medicin-interaktionsdata er ikke endnu tilgængelige i denne evidenspakke (markeret som en **blokerande** datagab — se Næste trin).

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Forudsigelsesscoreen er høj, men der er nul klinisk forsøg eller litteraturunderstøttelse, og evidenspakkens egen mekanistiske analyse finder eksplicit ingen biologisk forbindelse mellem medicinen godkendte mekanisme (IL-31RA-blokade) og diabetisk katarakt-patologi. Kombineret med fraværet af dansk markedsføringsgodkendelse og manglende SmPC-sikkerhedsdata opfylder denne kandidat ikke standarden for yderligere evaluering på nuværende tidspunkt.

**For at fortsætte kræves følgende:**
- SmPC-advarsler/kontraindikationsdata (aktuelt et blokeringsgab — krævet før enhver S1-sikkerhedsscreening)
- Bekræftet, registervurderet oprindelig indikation og MOA (aktuelt markeret som datagab)
- Uafhængig præklinisk eller mekanistisk evidens, der forbinder IL-31/IL-31RA-signalering til linse/katarakt-patologi, før denne kandidat betragtes for yderligere evidensindsamling

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

