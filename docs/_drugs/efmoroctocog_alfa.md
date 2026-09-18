---
layout: default
title: Efmoroctocog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 156
evidence_level: L5
indication_count: 10
---

# Efmoroctocog Alfa
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

# Efmoroctocog Alfa: Fra Hemofili A til Pseudo-von Willebrand-sygdom

## Resumé i en sætning

Efmoroctocog alfa er et rekombinant koagulationsfaktor VIII Fc-fusionsprotein (rFVIIIFc), godkendt i flere lande (f.eks. EU som Elocta, USA som Eloctate) til forebyggelse og behandling af blødningsepisoder hos patienter med hemofili A.
TxGNN-modellen forudsiger, at det kan være effektivt for **Pseudo-von Willebrand-sygdom**, en sjælden blødningsforstyrrelse af blodpladetype, der er mekanistisk forbundet med faktoren VIII–von Willebrand-faktor (vWF)-aksen.
I øjeblikket er der **ingen kliniske forsøg** og **ingen publikationer**, der specifikt undersøger efmoroctocog alfa i denne indikation, hvilket betyder, at denne forudsigelse alene understøttes af modelinferens.

---

## Hurtigt overblik

| Punkt | Indhold |
|-------|---------|
| Original indikation | Hemofili A (medfødt faktor VIII-mangel) — forebyggelse og behandling af blødningsepisoder |
| Forudsagt ny indikation | Pseudo-von Willebrand-sygdom |
| TxGNN-forudsigelsesscore | 99.997% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Efmoroctocog alfa (rFVIIIFc) er et rekombinant faktor VIII smeltet sammen med Fc-regionen af human IgG1, hvilket forlænger dets cirkulerende halveringstid cirka 1.5-fold sammenlignet med standard faktor VIII-produkter. Dens primære godkendte mekanisme er at midlertidigt erstatte den manglende eller fraværende endogen FVIII hos patienter med hemofili A og dermed gendanne normal sekundær hemostase. Kritisk vigtig er, at faktor VIII ikke virker isoleret: den cirkulerer i plasma bundet til von Willebrand-faktor (vWF), som både beskytter FVIII mod for tidlig proteolytisk nedbrydning og leverer den til steder med vaskulær skade.

Pseudo-von Willebrand-sygdom (blodpladetype vWD) er forårsaget af en gain-of-function mutation i blodpladeglykoprotein Ibα (GPIbα)-receptoren, som binder vWF med unormalt høj affinitet. Dette fører til spontan blodplateklumpning, forbrug af høj-molekylvægt vWF-multimerer og sekundær reduktion i plasma FVIII-niveauer — fordi FVIII mister sin vWF-chaperone. Den resulterende fænotype er derfor en kombineret blodpladeog sekundær koagulationsdefekt, med lav FVIII-aktivitet som en klinisk egenskab i alvorlige tilfælde. Tilsætning af eksogen rFVIIIFc kunne teoretisk kompensere for FVIII-komponenten i denne kombinerede defekt.

TxGNN knowledge-graph-modellen har sandsynligvis identificeret denne forbindelse gennem den delte biologiske node af vWF og co-forekomsten af FVIII-mangel som en nedstrøms-konsekvens af pseudo-vWD. Selvom den mekanistiske begrundelse er biologisk sammenhængende, håndteres pseudo-vWD i øjeblikket primært med blodpladetransfusioner eller desmopressin (DDAVP), og der er ingen etableret klinisk præcedens for at anvende FVIII-koncentrat som en terapeutisk strategi i denne indikation. Forudsigelsen bør derfor begrunde eksplorativ undersøgelse snarere end øjeblikkelig klinisk translation.

---

## Evidens fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteratur

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Sikkerhedsmæssige overvejelser

Se venligst det godkendte produktresumékarakteristika (SmPC) for sikkerhedsinformation.

> **Bemærk:** Ingen data om lægemiddelinteraktion, kontraindikationer eller vigtige advarsler kunne hentes fra det aktuelle evidensomfang. Før enhver klinisk brug skal den fulde SmPC for Elocta/Eloctate (efmoroctocog alfa) konsulteres med særlig opmærksomhed på immunogenicitetsrisiko (inhibitorudvikling mod FVIII), overfølsomhedsreaktioner og kardiovaskulær overvågning i befolkningsgrupper med øget risiko.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
TxGNN-modellen giver en ekstremt høj forudsigelsesscore (99.997%), og den biologiske forbindelse mellem faktor VIII, vWF og pseudo-von Willebrand-sygdom er mekanistisk sammenhængende; der er dog i øjeblikket nul klinisk forsøgs- eller offentliggjort litteraturbevis for efmoroctocog alfa i denne indikation, hvilket klassificerer dette som en ren modelforudsigelse (L5). En Hold-beslutning er passende, indtil der mindst er præ-kliniske eller case-series-data tilgængelige til at retfærdiggøre ressourceinvestering.

**For at gå videre kræves følgende:**

- **Bekræftelse af virkningsmekanisme:** Indhent formelle MOA-data fra DrugBank (DB11607) for at dokumentere FVIII–vWF-interaktionsvejene og deres potentielle relevans for pseudo-vWD-patofysiologi.
- **Ekspertklinikeropinion:** Konsultér en hæmatolog eller koagulationsspecialist for at vurdere, om supplementering af FVIII i pseudo-vWD er fysiologisk rationel givet den primære blodpladeGPIbα-defekt.
- **Gennemgang af regulatorisk historie:** Bekræft, om nogen compassionat brug, navngivet-patient-behandling eller off-label brug af FVIII-koncentrater i pseudo-vWD er dokumenteret i EU/EMA- eller Laegemiddelstyrelsen-registre.
- **Afhjælpning af evidensgab:** Gennemfør en målrettet litteraturgennemgang med bredere søgetermer (f.eks. "Factor VIII concentrate AND pseudo-von Willebrand disease", "platelet-type vWD AND factor replacement") for at udelukke uoffentliggjort eller grå litteraturbevis, der blev overset af de automatiserede indsamlere.
- **Markedsadgangssti i Danmark:** Da efmoroctocog alfa i øjeblikket ikke er registreret i Danmark, ville en markedsføringstilladelsessti via EMA's centraliserede procedure (Elocta er EMA-godkendt) eller en ansøgning om navngivet-patient-import være påkrævet, hvis klinisk evaluering fortsætter.
- **Indsamling af sikkerhedsdata:** Download og parse produktinformationen fra TFDA/EMA for at færdiggøre sikkerhedsprofilen, før noget klinisk program initieres.

---

> ⚠️ **Ansvarsfraskrivelse:** Denne rapport er genereret til formål med forskningsreference alene og udgør ikke lægeligt råd. Alle lægemiddelgenbrugskandidater kræver klinisk validering før anvendelse. Dataafskæring: 2026-04-05.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

