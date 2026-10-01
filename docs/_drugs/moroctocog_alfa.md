---
layout: default
title: Moroctocog Alfa
parent: Kun modelforudsigelse (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Moroctocog Alfa
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

# Moroctocog alfa: Fra hæmofili A til primær frigørelsesforstyrrelse i blodplader

## Resumé i én sætning

Moroctocog alfa er rekombinant koagulationsfaktor VIII (B-domæne-deleteret), som anvendes til faktor VIII-substitution ved hæmofili A.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **primær frigørelsesforstyrrelse i blodplader** (primary release disorder of platelets).
Forudsigelsen er rent beregningsbaseret: der er **ingen direkte relevante kliniske forsøg** og **ingen publikationer** for denne indikation.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hæmofili A (ud fra lægemidlets kendte anvendelse; den danske licensdata indeholder ingen indikationstekst) |
| Forudsagt ny indikation | Primær frigørelsesforstyrrelse i blodplader |
| TxGNN-prædiktionsscore | 99,97 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen. Moroctocog alfa erstatter faktor VIII, som er en kofaktor i tenase-komplekset i koagulationskaskaden, og lægemidlets effekt ved hæmofili A er veletableret.

Primære frigørelsesforstyrrelser i blodplader (defekter i granula-lagring og sekretion) er primære trombocytfunktionsforstyrrelser. Her er faktor VIII-niveauet normalt, og substitution med faktor VIII korrigerer ikke den underliggende defekt. Den meget høje TxGNN-score afspejler sandsynligvis nærhed mellem koagulations- og trombocytknuder i vidensgrafen snarere end en valideret mekanisme.

Konklusionen er, at forudsigelsen ikke har noget biologisk eller klinisk grundlag i dag. Den bør betragtes som en modelartefakt, indtil andet er påvist.

---

## Evidens fra kliniske forsøg

Der er ingen direkte relevante forsøg for denne indikation. En dublet af forudsigelsen indeholder seks forsøg, men alle er vurderet som grad C (indirekte eller urelaterede), og ingen tester lægemidlet ved trombocytfrigørelsesforstyrrelser:

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT07400848](https://clinicaltrials.gov/study/NCT07400848) | N/A | Rekrutterer | 200 | Laboratorie- og symptomstudie ved post-COVID-19-vaccinationssyndrom; ikke relateret til lægemidlet |
| [NCT07343687](https://clinicaltrials.gov/study/NCT07343687) | N/A | Ikke startet rekruttering | 80 | Observationsstudie af hæmatologiske og koagulationsprofiler ved akut myeloid leukæmi |
| [NCT01913405](https://clinicaltrials.gov/study/NCT01913405) | Fase 3 | Afsluttet | 30 | PEGyleret rFVIII (BAX 855) ved svær hæmofili A og kirurgiske indgreb; ikke trombocytsygdom |
| [NCT07329036](https://clinicaltrials.gov/study/NCT07329036) | N/A | Rekrutterer | 25 | Kunstigt leverstøttesystem ved akut-på-kronisk leversvigt; ikke relateret |
| [NCT04161495](https://clinicaltrials.gov/study/NCT04161495) | Fase 3 | Afsluttet | 159 | rFVIIIFc-VWF-XTEN (BIVV001) ved svær hæmofili A hos patienter ≥12 år |
| [NCT04759131](https://clinicaltrials.gov/study/NCT04759131) | Fase 3 | Afsluttet | 74 | rFVIIIFc-VWF-XTEN (BIVV001) ved svær hæmofili A hos børn <12 år |
| [NCT07439939](https://clinicaltrials.gov/study/NCT07439939) | N/A | Rekrutterer | 45 | Udforskning af systemisk og portal hæmostase ved TIPS-anlæggelse |

---

## Litteraturevidens

Der findes i øjeblikket ingen relateret litteratur for denne indikation.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103002398 | ReFacto (Pfizer Europe MA EEIG) | Pulver og solvens til injektionsvæske, opløsning | Ikke angivet i det modtagne datagrundlag |

---

## Sikkerhedsmæssige overvejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger. Der er ikke fundet registrerede lægemiddelinteraktioner i den anvendte kilde.

---

## Øvrige forudsigelser fra TxGNN

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|---------|------|------|-----------|
| Pseudo-von Willebrands sygdom | 99,97 % | L5 | Hold. Defekten er GP1BA-gain-of-function, og behandlingen retter sig mod VWF/blodplader, ikke faktor VIII alene |
| Glanzmanns trombasteni | 99,96 % | L5 | Hold. Defekt i GPIIb/IIIa; faktor VIII afhjælper den ikke. Kun et hæmofili-orienteret naturhistorisk register ([NCT04398628](https://clinicaltrials.gov/study/NCT04398628)) og en case-serie fra 1964 ([PMID 14179492](https://pubmed.ncbi.nlm.nih.gov/14179492/)) er knyttet hertil, begge uden direkte relevans |
| Erhvervet koagulationsfaktormangel | 99,88 % | L5 | Forskningsspørgsmål. Biologisk mest plausibel, men sygdomsklassen er bred. Ved erhvervet hæmofili A neutraliserer autoantistoffer faktor VIII |
| Scotts syndrom | 99,86 % | L5 | Hold. Defekten ligger i trombocytoverfladen (TMEM16F/ANO6), ikke i faktor VIII-niveauet |

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger kun på modellen (L5). Der er hverken kliniske forsøg eller publikationer, der tester lægemidlet ved denne sygdom, og mekanismen taler imod effekt, fordi faktor VIII-substitution ikke korrigerer en primær trombocytfunktionsdefekt.

**For at gå videre kræves følgende:**
- Oplysninger om lægemidlets virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra det danske produktresumé fra Lægemiddelstyrelsen
- Den godkendte indikationstekst for ReFacto i Danmark
- Et konkret, afgrænset forskningsspørgsmål, f.eks. den veldefinerede undergruppe af erhvervet hæmofili A med lave inhibitortitre, før der overvejes prækliniske eller kliniske studier

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelserne kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

