---
layout: default
title: Necitumumab
parent: Kun modelforudsigelse (L5)
nav_order: 307
evidence_level: L5
indication_count: 10
---

# Necitumumab
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

# Necitumumab: Fra pladecellet ikke-småcellet lungekræft til gingival fibromatose

## Resumé i én sætning

Necitumumab er et antistof mod EGFR (epidermal vækstfaktorreceptor), som er godkendt til behandling af pladecellet ikke-småcellet lungekræft (NSCLC).
TxGNN-modellen forudsiger, at det kan have effekt ved **gingival fibromatose**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen.
Forudsigelsen er sandsynligvis et artefakt i vidensgrafen og bør ikke føres videre uden yderligere dokumentation.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Pladecellet NSCLC (fremgår af evidenspakkens mekanistiske vurdering, ikke af de danske markedsføringsdata) |
| Forudsagt ny indikation | Gingival fibromatose (fibromatosis, gingival) |
| TxGNN-forudsigelsesscore | 99,92 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i evidenspakken. Necitumumab er et EGFR-hæmmende antistof, og dets virkning ved pladecellet NSCLC bygger på, at EGFR er overudtrykt i mange tumorer af denne type. Mekanistisk kan det anvendes ved sygdomme, hvor EGFR-signalering spiller en afgørende rolle.

Gingival fibromatose er en fibroblastdrevet overvækst af tandkødet, som oftest er arvelig eller lægemiddelinduceret. En rolle for EGFR-signalvejen er spekulativ, og EGFR-blokade er ikke en etableret behandlingsstrategi. Forudsigelsen skyldes sandsynligvis lægemidlets nærhed til lungetumor-knuder i vidensgrafen. Den må derfor vurderes som et sandsynligt vidensgraf-artefakt.

De øvrige forudsigelser med høj score er samlet herunder (dubletter er fjernet):

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| Gingival fibromatose | 99,92 % | Intet klart mekanistisk link, sandsynligt artefakt (Hold) |
| Hamartom i lungen | 99,91 % | Godartet læsion, ingen kendt EGFR-afhængighed (Hold) |
| Karcinom i lungehilum | 99,91 % | Biologisk plausibelt, men kan i vid udstrækning overlappe med den eksisterende pladecellede NSCLC-indikation (Forskningsspørgsmål) |
| Fibrom i lungen | 99,91 % | Sjælden godartet tumor, behandles kirurgisk (Hold) |
| Pulmonær sulcus-neoplasme (Pancoast) | 99,90 % | Oftest NSCLC i lungeapeks, sandsynligvis en delmængde af den godkendte indikation (Forskningsspørgsmål) |
| Germinalcelletumor i lungen | 99,90 % | Meget sjælden, behandles med platinbaseret kemoterapi, ikke EGFR-drevet (Hold) |

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Indehaver |
|---------|------|------|-----------|
| 28105547314 | Portrazza | Koncentrat til infusionsvæske, opløsning | Eli Lilly Netherland B.V. |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (monoklonalt antistof mod EGFR), ikke konventionelt cytotoksisk |
| Risiko for myelosuppression | Generelt lav for antistoffer af denne type. Se produktresuméet (SmPC) for specifikke data |
| Emetogenicitetsklassifikation | Lav. Se produktresuméet (SmPC) |
| Monitoreringspunkter | Elektrolytter (især magnesium), hudreaktioner, tegn på tromboemboliske hændelser samt blodtal og lever- og nyrefunktion efter klinisk vurdering |
| Håndteringsbeskyttelse | Følg lokale retningslinjer for håndtering af antineoplastiske lægemidler. Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

Evidenspakken indeholder ingen registrerede advarsler, kontraindikationer eller lægemiddelinteraktioner. Den mekanistiske vurdering nævner dog følgende kendte toksiciteter ved necitumumab:

- Hypomagnesæmi
- Hudtoksicitet
- Tromboemboliske hændelser

Det vil være vanskeligt at begrunde et systemisk biologisk lægemiddel med disse bivirkninger til godartede tilstande som gingival fibromatose, lungefibrom eller lungehamartom.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for gingival fibromatose hviler alene på modellen (L5), uden kliniske forsøg, litteratur eller et plausibelt mekanistisk link. Risikoprofilen for et systemisk EGFR-antistof er desuden uforholdsmæssig i forhold til en godartet tilstand. Forudsigelserne for lungehilum-karcinom og Pancoast-tumor er biologisk plausible, men er sandsynligvis dækket af den eksisterende NSCLC-indikation og er derfor forskningsspørgsmål snarere end nye indikationer.

**For at gå videre kræves følgende:**
- Sikkerhedsoplysninger (advarsler og kontraindikationer) fra Lægemiddelstyrelsens produktresumé for Portrazza
- Detaljerede data om virkningsmekanismen (MOA) fra DrugBank
- Afklaring af histologi og EGFR-status for de lungekræftrelaterede forudsigelser, så det kan vurderes, om de udgør en ny indikation eller en delmængde af den godkendte
- Præklinisk eller mekanistisk dokumentation for EGFR-involvering ved gingival fibromatose, før en sådan forudsigelse kan prioriteres

*Resultaterne er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepurposing kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

