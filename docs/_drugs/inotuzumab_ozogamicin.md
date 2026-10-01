---
layout: default
title: Inotuzumab Ozogamicin
parent: Kun modelforudsigelse (L5)
nav_order: 234
evidence_level: L5
indication_count: 10
---

# Inotuzumab Ozogamicin
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

# Inotuzumab ozogamicin: Fra B-celle-leukæmi til lægemiddelinduceret osteoporose

## Resumé

Inotuzumab ozogamicin er et antistof-lægemiddelkonjugat rettet mod CD22 med en cytotoksisk calicheamicin-del. Det markedsføres i Danmark som Besponsa og er kendt som et kræftlægemiddel til B-celleleukæmi (oplysningen er ikke angivet i datagrundlaget).
TxGNN-modellen forudsiger, at det kan have effekt på **lægemiddelinduceret osteoporose** med en score på 98,2 %. Der er dog **ingen kliniske forsøg og ingen relevant litteratur** bag forudsigelsen, og den er sandsynligvis en artefakt i vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i datagrundlaget (godkendelsesteksten er tom). Efter almen viden: CD22-positiv B-celle-prækursor akut lymfatisk leukæmi |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose |
| TxGNN-forudsigelsesscore | 98,2 % |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i datagrundlaget. Ud fra kendt information er inotuzumab ozogamicin et CD22-rettet antistof koblet til calicheamicin. CD22 er en markør på B-linjeceller, og stoffet virker ved at dræbe CD22-positive celler.

Der er **ingen plausibel biologisk sammenhæng** mellem CD22-målrettet behandling og knogleopbygning. CD22 har ingen kendt rolle i knogleremodellering. Cytotoksisk kemoterapi og de omkringliggende behandlinger (transplantation og steroider) kan tværtimod nedsætte knogletætheden. Lægemidlet kan derfor bidrage til tilstanden i stedet for at behandle den. Den høje score er et resultat af nærhed i vidensgrafen uden klinisk støtte.

Modellen har også foreslået flere brystkræftsubtyper. Forudsigelserne er dubletter, der er slået sammen, og ingen af dem har støtte i data:

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| HER2-positivt brystkarcinom | 97,8 % | Andre antistof-lægemiddelkonjugater er etableret i HER2-positiv brystkræft, men de rammer HER2, ikke CD22. CD22 er ikke et anerkendt mål i brystepitelsvulster |
| Normal breast-like subtype af brystkarcinom | 96,8 % | Ingen påvist CD22-ekspression eller -afhængighed. Sandsynligvis grafnærhed til andre brystkræftknuder |
| Progesteronreceptor-positiv brystkræft | 96,8 % | Ingen mekanistisk forbindelse mellem CD22-målretning og hormonreceptor-positiv brystkræft |
| Brysttumor luminal A eller B | 96,8 % | Se afsnittet om litteratur. De hentede artikler er støj |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur for den primære forudsigelse (lægemiddelinduceret osteoporose).

Til den sidste forudsigelse (brysttumor luminal A eller B) blev der hentet 19 publikationer. De er falske positive søgetræf på bogstavet "B" og handler om B-cellebiologi, hepatitis B-vacciner, HLA-B og bakterieklorofyl b. Ingen af dem omhandler brystkræft eller inotuzumab ozogamicin, og de tæller ikke som evidens.

---

## Oplysninger om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105771516 | Besponsa (Pfizer Europe MA EEIG) | Pulver til koncentrat til infusionsvæske, opløsning | Ikke angivet i datagrundlaget |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet cytotoksisk behandling (antistof-lægemiddelkonjugat med calicheamicin som cytotoksisk del) |
| Risiko for myelosuppression | Forventet forhøjet for cytotoksiske konjugater. Se produktresuméet for præcise tal |
| Emetogenicitetsklassifikation | Se produktresuméet |
| Monitoreringspunkter | Fuldt blodbillede med differentialtælling, lever- og nyrefunktion |
| Håndteringsbeskyttelse | Skal håndteres efter reglerne for cytotoksiske lægemidler |

Se produktresuméets (SmPC) advarsler og forsigtighedsregler for fuldstændige oplysninger.

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Advarsler og kontraindikationer fra Lægemiddelstyrelsens produktinformation mangler i datagrundlaget. Det er en blokerende mangel for videre sikkerhedsscreening. Der blev ikke fundet interaktionsdata.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler udelukkende på en modelscore uden kliniske forsøg eller relevant litteratur. Der er ingen plausibel mekanisme, og lægemidlet og den omgivende behandling kan reducere knogletætheden. Det samme gælder de forudsagte brystkræftindikationer.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af Lægemiddelstyrelsens produktresumé (advarsler, kontraindikationer og godkendt indikation)
- Data om virkningsmekanisme fra DrugBank
- Målrettet litteratursøgning med korrekte søgetermer, da de nuværende træf er irrelevante
- Biologisk belæg for en rolle for CD22 i knogle- eller brystvæv, før der overvejes prækliniske eller kliniske studier

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelomplacering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

