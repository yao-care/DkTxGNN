---
layout: default
title: Phenprocoumon
parent: Moderat evidens (L3-L4)
nav_order: 350
evidence_level: L4
indication_count: 10
---

# Phenprocoumon
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Phenprocoumon: Fra tromboemboliske lidelser til posteroinferior myokardieinfarkt

## Sammenfatning i én sætning

> Phenprocoumon er en vitamin K-antagonist (VKA) oral antikoagulans; der er ingen strukturerede data om dens oprindeligt godkendt indikation tilgængelig i denne evidenspakke. TxGNN-modellen forudsiger en **99.86%**-score-tilknytning til **Posteroinferior Myokardieinfarkt** — imidlertid er dette en anatomisk undertype-knude for myokardieinfarkt snarere end en distinkt klinisk enhed, og **0 kliniske forsøg** og **0 publikationer** specifikt for phenprocoumon i denne indikation er i øjeblikket registreret.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke specificeret i strukturerede data (`original_indications` er tom). Evidenspakkens begrundelse noter, at phenprocoumon er klinisk brugt som vitamin K-antagonist (VKA) oral antikoagulans, analogt med warfarin |
| Forudsagt ny indikation | Posteroinferior Myokardieinfarkt (anatomisk MI-undertype — ikke en uafhængig klinisk enhed) |
| TxGNN-forudsigelsesscore | 99.86% |
| Evidensniveau | L4 |
| Danmarks markedsstatus | Ikke markedsført |
| Antal marketing-godkendelser | 0 |
| Anbefalet beslutning | Afwait |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige (`original_moa: [Data Gap]`). Baseret på de kontekstuelle oplysninger, der leveres i denne evidenspakkes egne begrundelsesnoter, er phenprocoumon en vitamin K-antagonist (VKA), farmakologisk sammenlignelig med warfarin, og dens etablerede kliniske rolle er langtids oral antikoagulation.

Den toprangerede forudsagte indikation, "Posteroinferior Myokardieinfarkt", er eksplicit markeret i evidenspakken som en **anatomisk lokaliserings-undertype af myokardieinfarkt**, ikke en separat sygdomsenhed. Begrundelsen forklarer, at VKA-klasse mediciner har klasse-niveau (ikke phenprocoumon-specifik) historisk Phase 3 RCT-understøttelse for sekundær prævention af post-MI tromboemboliske begivenheder (f.eks. er WARIS-II, ASPECT-2 refereret som baggrundsforfatterskab, men ingen af forsøgene er inkluderet som struktureret evidens i denne pakke). Den meget høje TxGNN-score afspejler mest sandsynligt en generaliseret "antikoagulans–MI"-graf-tilknytning lært af vidensgrafen snarere end evidens specifikt for denne anatomiske undertype eller for phenprocoumon selv.

Denne evidenspakke lister desuden fire andre kandidat-sygdomme ved tilsvarende høje scores: posterolateral myokardieinfarkt (99.86%), heparin-kofaktor 2-mangel (99.86%, understøttet af 1 review-niveau publikation fra 1989), septalt myokardieinfarkt (99.85%) og faktor 5-overskud med spontan trombose (99.80%, ingen understøttende poster på alt). Bemærk, at flere rækker i de underliggende data (f.eks. rang 1 og rang 3, rang 2 og rang 4) er præcise duplikater af samme sygdom/score-parring — dette bør behandles som et datakvalitetsartefakt til triageformål snarere end uafhængig bekræftelse.

---

## Evidens fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidence

I øjeblikket ingen relateret litteratur tilgængelig.

*(Bemærk: den relaterede kandidat "heparin-kofaktor 2-mangel" — en arvelig trombofili — er understøttet af en 1989 review-niveau publikation, [2483712](https://pubmed.ncbi.nlm.nih.gov/2483712/), som ikke er en direkte forsøg af phenprocoumon i denne MI-undertype og er præsenteret her for transparens alene, ikke som evidens for den primære forudsagte indikation ovenfor.)*

---

## Markedsinformation for Danmark

Phenprocoumon har i øjeblikket **ingen marketing-godkendelse i Danmark** (markedsstatus: Ikke markedsført; 0 registrerede licenser). Ingen Lægemiddelstyrelsen eller EMA-centraliseret produktrekord er tilgængelig for denne evidenspakke.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation. Bemærk: da phenprocoumon ikke er markedsført i Danmark, eksisterer der i øjeblikket ingen dansk SmPC — vigtige advarsler, kontraindikationer og lægemiddelinteraktionsdata er alle registreret som datagab (`DG001`, markeret som **Blokerings**-alvor i denne evidenspakke, da det forhindrer indgang i S1-sikkerhedsforhåndsscreening). Konsulter en EU/anden-jurisdiktions SmPC eller DrugBank/DDI-database direkte, før klinisk brug overvejes.

---

## Konklusion og næste trin

**Beslutning: Afwait**

**Begrundelse:**
Den forudsagte indikation er en anatomisk MI-undertype snarere end en distinkt klinisk enhed, med nul direkte kliniske forsøg eller publikationer, der understøtter phenprocoumon specifikt i denne sammenhæng — den høje TxGNN-score synes at afspejle en generaliseret "antikoagulans–MI"-graf-tilknytning snarere end målrettet evidens. Kombineret med medicinens ikke-markedsførte status i Danmark og et blokerings-alvorligheds sikkerhedsdatagab, opfylder denne kandidat i øjeblikket ikke standarden for at gå videre.

**For at gå videre, er følgende påkrævet:**
- TFDA/dansk SmPC advarsler og kontraindikationer (`DG001`, Blokering — påkrævet før nogen S1-sikkerhedsforhåndsscreening)
- Bekræftet virkningsmekanisme-data fra DrugBank (`DG002`)
- Afklaring af de duplikerede rangeringsindgange på kandidatlisten (datakvalitetskontrol)
- Direkte klinisk forsøgs- eller litteraturevidence for phenprocoumon specifikt i post-MI tromboembolisk prævention, snarere end klasse-niveau VKA-baggrundsforfatterskab
- Præcisering af, hvorvidt Danmark har nogen historisk eller off-label brugssti for phenprocoumon, givet dens nuværende ikke-markedsførte status

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

