---
layout: default
title: Pegvisomant
parent: Kun modelforudsigelse (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Pegvisomant
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

# Pegvisomant: Fra akromegali til borderline seøs ovarium-tumor

## Resumé på én sætning

> Pegvisomant (DrugBank DB00082) er en rekombinant væksthormon (GH) receptorantagonist, der oprindeligt blev udviklet til behandling af **akromegali** ved at blokere GH-drevet IGF-1-produktion.
> TxGNN-modellen forudsiger en mulig effekt på **Borderline seøs ovarium-tumor**, med en forudsigelsesscore på **98.63%**, men **ingen kliniske forsøg og ingen litteratur** understøtter i øjeblikket denne specifikke forbindelse — dette er en ren knowledge-graph-forudsigelse.

> **Bemærkning om datakilde:** Evidenspakkens egne felter `original_moa` og `original_indications` er markeret som datahuller (DG002). "Akromegali" oprindelig indikation og GH-receptorantagonist-mekanisme, der er angivet ovenfor, kommer fra etableret offentlig lægemiddelinformation (Pegvisomant/Somavert), ikke fra kildepakken, og bør bekræftes mod det officielle produktresumé (SmPC) før brug.

---

## Hurtigoversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Akromegali (væksthormon-overskud) — *ikke til stede i kildepakke; baseret på etableret lægemiddelinformation, afventer bekræftelse* |
| Forventet ny indikation | Borderline seøs ovarium-tumor |
| TxGNN-forudsigelsesscore | 98.63% |
| Bevisniveau | L5 (kun modelforudsigelse — ingen kliniske forsøg, ingen litteratur) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Tilbageholdt |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljeret, kildeverificeret virkningsmekanisme-data er ikke tilgængelig i evidenspakken (markeret som et alvorligt datahul, DG002). Baseret på rationale tilknyttet denne forudsigelse, forstås Pegvisomant at virke som en **GH-receptorantagonist**, der reducerer IGF-1-produktion — mekanismen bag dets etablerede brug i akromegali.

Det foreslåede link til Borderline seøs ovarium-tumor hviler på generel onkologi-baggrundsviden om, at GH/IGF-1-aksen kan bidrage til proliferativ signalering i nogle ovarium-epitheliale tumorer, så en GH-receptorantagonist kunne teoretisk bremse IGF-1-drevet tumorvækst. Imidlertid karakteriserer evidenspakken eksplicit dette som en **indirekte, mekanisme-baseret slutning**: der er ingen forsøg eller publikation, der direkte forbinder Pegvisomant til denne specifikke tumortype, og den høje TxGNN-score kan ikke skelne et genuint biologisk signal fra en knowledge-graph-klyngningseffekt.

Denne forsigtighed forstærkes af, at fire af de ti bedste forudsigelser fra denne kørsel er ovarium-tumorsubtyper (borderline seøs tumor, rete ovarii cystadenoma, papillær cystadenoma og malign Brenner-tumor) med næsten identiske pointer (0.9856–0.9863), hvilket tyder på, at modellen grupperer disse sygdomme sammen i embeddings-rum snarere end producerer et individuelt valideret signal for nogen af dem. En femte top-10-forudsigelse — pyelonefritis, en bakteriel infektion uden kendt mekanistisk link til GH-receptorblokade — er markeret i selve pakken som en sandsynlig falsk-positiv artefakt og overvejes ikke yderligere i denne rapport.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen registrerede relaterede kliniske forsøg.

---

## Evidens fra litteratur

Der er i øjeblikket ingen tilgængelig relateret litteratur.

---

## Markedsinformation for Danmark

Pegvisomant har i øjeblikket **ingen markedsføringstilladelser** i Danmark (markedsstatus: Ikke markedsført; 0 licenser på record i kildepakken). Ingen data fra Lægemiddelstyrelsen eller centraliseret EMA-godkendelse er tilgængelig til at opsummere doseringsform eller godkendt indikationstekst for dette marked.

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

*(Bemærk: Dette er ikke blot en placeholder — vigtige advarsler, kontraindikationer og lægemiddelinteraktionsdata er markeret som et blokerende-alvorligheds datahul, DG001, hvilket betyder, at denne kandidat i øjeblikket ikke kan gå ind i sikkerhedsvurderingsfasen S1.)*

---

## Konklusion og næste skridt

**Beslutning: Tilbageholdt**

**Begrundelse:**
- Bevisnivenau er L5 — forudsigelsen understøttes kun af TxGNN-modellen, med nul kliniske forsøg og nul publikationer specifikt for denne indikation.
- Forudsigelsen sidder inden for en klynge af næsten identiske pointer på tværs af flere uafhængige ovarium-tumorsubtyper, hvilket giver anledning til bekymring for, at det afspejler strukturel lighed i knowledge-grafen snarere end et valideret farmakologisk signal.
- Et blokerende-alvorligheds datahul (manglende dansk/EU produktresumé-advarsler og kontraindikationer) betyder, at denne kandidat i øjeblikket ikke kan gå videre til sikkerhedsvurdering (S1), uafhængigt af effektivitsspørgsmålet.
- Pegvisomant markedsføres i øjeblikket ikke i Danmark (0 godkendelser), hvilket tilføjer en regulerings- eller adgangsbarriere oven på den evidentielle.

**For at gå videre kræves følgende:**
- Officielt produktresumé (SmPC) (advarsler, kontraindikationer, lægemiddelinteraktioner) for at rydde det blokerende datahul (DG001) og tillade sikkerhedsvurdering
- Bekræftet, kildeverificeret virkningsmekanisme og originale indikationsdokumentation (DG002)
- Prekliniske eller mekanistiske studier, der specifikt undersøger GH/IGF-1-aksen i borderline seøse ovarium-tumorer, snarere end generel onkologi-baggrundsviden
- Enhver første klinisk eller case-niveau evidens, der forbinder Pegvisomant til denne indikation, før yderligere ressourceinvesteringer
- Revurdering af de andre klyngede ovarium-tumor-forudsigelser som en gruppe, da de kan repræsentere en underliggende (ubekræftet) hypotese snarere end fire uafhængige signaler

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

