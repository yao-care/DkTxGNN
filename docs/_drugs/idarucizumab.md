---
layout: default
title: Idarucizumab
parent: Kun modelforudsigelse (L5)
nav_order: 222
evidence_level: L5
indication_count: 10
---

# Idarucizumab
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

# Idarucizumab: Fra dabigatran-antikoagulations-reversering til hemoglobinopati

## Sammenfatning på én sætning

Idarucizumab er et monoklonalt antistof-fragment, hvis eneste etablerede anvendelse er nødvendig reversering af dabigatrans antikoagulant-effekt. TxGNN-modellen forudsiger en mulig effekt på **hemoglobinopati**, men denne forudsigelse understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer**, og modellens egen begrundelse markerer den mekanistiske forbindelse som usandsynlig.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Reversering af dabigatrans (antikoagulant) aktivitet ved nødsituation/livsfarlig blødning — ikke til stede som strukturerede licensdata i dette datasæt (Datagab DG001); angivet her ud fra generel viden om lægemidler alene |
| Forudsagt ny indikation | Hemoglobinopati |
| TxGNN-forudsigelsesscore | 95.66% |
| Bevisniveau | L5 |
| Status på dansk marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljeret dokumentation af virkningsmekanisme for Idarucizumab er ikke tilgængelig i dette datasæt (Datagab DG002). Modellens egen begrundelse for omformål beskriver imidlertid dens eneste kendte farmakologiske virkning: Idarucizumab binder frie og trombinkomplekserede dabigatran-molekyler og neutraliserer deres antikoagulant-aktivitet. Dette er en meget specifik, målbegrænset mekanisme uden kendt forbindelse til hemoglobin-struktur, globin-gen funktion eller rød-celle-patologi.

Hemoglobinopier (f.eks. seglcelleanæmi, andre hemoglobin-strukturelle varianter) opstår fra globin-gen mutationer og unormal hemoglobin-polymerisering — en sygdomsproces, der ikke har nogen beskrevet biokemisk eller farmakologisk overlapning med dabigatran-neutralisering. Bevispaakkens egen analyse karakteriserer denne forudsigelse som et sandsynligt **falsk-positivt signal drevet af knowledge-graph embedding-lighed** snarere end en biologisk funderet hypotese.

Denne vurdering forstærkes af et bredere mønster i forudsigelsessættet: de næste fire højest rangerede kandidater for dette lægemiddel (reumatoid artritis, 16p13.3 deletions-syndrom, beta-thalassæmi og pyruvat kinase-mangel) scorer alle tilsvarende højt, men deler samme mangel på understøttende kliniske forsøg eller litteraturbevis, og hver enkelt er markeret i begrundelsen som manglende en plausibel mekanistisk basis. Tilsammen tyder dette på, at modellens embedding-område for Idarucizumab er dårligt informeret af virkelige bevis på nuværende tidspunkt, snarere end at pege på en autentisk omformålsmulighed.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om dansk marked

Der er i øjeblikket ingen markedsføringstilladelser registreret for Idarucizumab i dette datasæt (markedsstatus: **Ikke markedsført**, 0 licenser på fil). Formelle Summary of Product Characteristics (SmPC) data er ikke hentet for denne kandidat (Datagab DG001).

---

## Sikkerhedshensyn

Se venligst det godkendte Summary of Product Characteristics (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Den forudsagte indikation (hemoglobinopati) har ingen understøttende kliniske forsøg eller litteratur, og modellens egen mekanistiske begrundelse finder ingen plausibel biologisk vej, der forbinder dabigatran-reverserings-aktivitet med hemoglobinopati-patologi — dette er mest sandsynligt et knowledge-graph-artefakt snarere end et autentisk omformålssignal. Derudover er sikkerhedsdokumentation (advarsler, kontraindikationer, lægemiddelinteraktioner) et blokerende datagab (DG001), som uafhængigt udelukker enhver sikkerhedsforkontrol.

**For at gå videre, er følgende nødvendigt:**
- Hentning af det godkendte SmPC / produktetiket (advarsler, kontraindikationer, DDI) for at lukke det blokerende datagab (DG001)
- Bekræftet dokumentation af virkningsmekanisme fra DrugBank eller tilsvarende kilde (DG002)
- Uafhængigt biologisk eller preklinisk bevis, der forbinder Idarucizumab (eller dets Fab-fragment antistof-klasse) til rød-celle/hemoglobin-patologi, før yderligere evaluering er berettiget
- Fornyet gennemgang af TxGNN-forudsigelsessættet for dette lægemiddel, givet at alle toprangerede kandidater deler det zero-bevis, lav-plausibilitetsmønster, der er noteret ovenfor

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

