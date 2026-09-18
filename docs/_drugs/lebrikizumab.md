---
layout: default
title: Lebrikizumab
parent: Kun modelforudsigelse (L5)
nav_order: 257
evidence_level: L5
indication_count: 10
---

# Lebrikizumab
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

# Lebrikizumab: Fra atopisk dermatitis til svær nonproliferativ diabetisk retinopati

## Resumé i én sætning

Lebrikizumab er et højaffinitets IL-13-målrettet monoklonalt antistof med en omfattende, veletableret klinisk og litteraturbase inden for atopisk dermatitis (29 forsøg, 20 publikationer på fil for kandidaten "dermatitis"). TxGNN-modellens toprangerede prognose er imidlertid **svær nonproliferativ diabetisk retinopati** (score **97,94 %**), en kandidat for hvilken **nul kliniske forsøg og nul publikationer** er på fil — dette er rent algoritmisk signal, ikke en litteratur- eller forsøgsstøttet hypotese.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Original indikation | Atopisk dermatitis *(udledt fra omfattende fase 2/3-forsøg og litteraturoverskrifter i denne dokumentsamling; ikke formelt registreret i medicin-niveau eller danske regulatoriske felter — se note nedenfor)* |
| Prognose for ny indikation | Svær nonproliferativ diabetisk retinopati |
| TxGNN-prognosescore | 97,94 % |
| Evidensniveau | L5 (kun modelprognose — ingen kliniske forsøg eller litteratur identificeret) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

**Note om original indikation:** Dokumentsamlingens `drug.original_indications`-felt er tomt, og der er ingen dansk markedsføringstilladelse (`taiwan_regulatory.licenses` er tomt), så dette er ikke et formelt dokumenteret faktum — det er udledt fra sygdomskonteksten af 29 registrerede forsøg og 20 publikationer forbundet med kandidaten "dermatitis" andetsteds i denne samling (se Bevis fra kliniske forsøg og litteraturbevis for denne kandidat under "Relateret etableret-brugs-bevis" nedenfor).

---

## Hvorfor er denne prognose rimelig?

I øjeblikket er detaljeret data om virkningsmekanisme ikke tilgængelig (`drug.original_moa` = datakløft). Baseret på litteratur forbundet med denne medicin andetsteds i denne dokumentsamling (PMID 36920778, PMID 37310643), er lebrikizumab et højaffinitets IgG4 monoklonalt antistof, der binder interleukin-13 (IL-13) og forhindrer dannelsen af IL-4Rα–IL-13Rα1 heterodimer-receptorsignaleringskomplekset, hvilket blokerer den efterfølgende Th2-drevne inflammatoriske signalering. Denne mekanisme ligger til grund for dets omfattende dokumenterede brug ved atopisk dermatitis.

For den toprangerede kandidat, **svær nonproliferativ diabetisk retinopati**, er feltet `repurposing_rationale.mechanistic_link` i denne dokumentsamling markeret "afventer" — ingen mekanistisk hypotese, der forbinder IL-13-signalering med diabetisk retinal mikrovaskulær patologi, er blevet dokumenteret eller hentet fra litteratur-/forsøgssøgninger (forespørgsels-id'er 3–5, 6–8: alle nul resultater). En anden, ikke-alvorlig form for diabetisk retinopati (rangering 5/6, score 96,84 %) viser det samme mønster, hvilket antyder, at modellen opsamler et retningsorienteret signal omkring retinal sygdom bredt, men dette har ingen ekstern validering i de kilder, der blev undersøgt.

Fordi ingen mekanistisk begrundelse, forsøg eller publikation i øjeblikket understøtter denne specifikke medicin–sygdom-parring, bør denne prognose behandles som en uvalideret hypotese, der genereres rent af TxGNN-algoritmen.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede registrerede kliniske forsøg.

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

---

### Relateret etableret-brugs-bevis (for kontekst)

Ikke en del af prognosebeviser for ny indikation, men til stede i denne samling under kandidaten "dermatitis" (rangering 9/10, score 95,97 %) og direkte relevant for medicinens virkelige profil: **29 kliniske forsøg** (flere afsluttede fase 3 RCT'er, f.eks. NCT04146363, NCT04178967, NCT04250337, NCT05559359) og **20 publikationer** (f.eks. PMID 36920778 — *NEJM*, "Two Phase 3 Trials of Lebrikizumab for Moderate-to-Severe Atopic Dermatitis"; PMID 38186219 — *Allergy*, der noterer EU-godkendelse af lebrikizumab til atopisk dermatitis i 2023) dokumenterer lebrikizumabs efficacy og sikkerhed ved moderat til svær atopisk dermatitis. Dette er inkluderet kun for kontekst, da det ikke eviderer retinopati-prognosen under evaluering.

---

## Markedsinformation for Danmark

Lebrikizumab er i øjeblikket ikke markedsført i Danmark, og ingen markedsføringstilladelser (nationale Lægemiddelstyrelsen eller centraliseret EMA) er på fil i denne dokumentsamling (`total_licenses: 0`).

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation. En struktureret søgning i lægemiddelinteraktionsdatabase (2026-03-24) returnerede ingen interaktioner på fil for lebrikizumab; dette udelukker ikke interaktioner, der endnu ikke er blevet katalogiseret.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Toprangeret prognose (svær nonproliferativ diabetisk retinopati, 97,94 %) har ingen understøttende kliniske forsøg, litteratur eller dokumenteret mekanistisk begrundelse — det opfylder kun L5 (kun modelprognose). Kombineret med medicinens ikke-markedsført status i Danmark og manglende MOA/sikkerhedsdata er der i øjeblikket intet grundlag for at fremme denne kandidat ud over hypotetisk stadium.

**For at fortsætte er følgende nødvendigt:**
- Virkningsmekanisme-data (DrugBank API-forespørgsel) for at vurdere biologisk plausibilitet af IL-13-signalering i diabetisk retinal mikrovaskulær sygdom (datakløft DG002, høj alvorlighed)
- TFDA/SmPC advarsler og kontraindikationer, i øjeblikket en blokerende kløft for enhver S1-sikkerhedsscreening (datakløft DG001, blokering)
- Målrettet litteratur-/præklinisk søgning specifikt på IL-13 og retinal vaskulopati, ud over de sygdomsmatchede forespørgsler, der allerede blev kørt (som returnerede nul resultater)
- En dansk regulatorisk vejledning, da produktet i øjeblikket ikke er markedsført lokalt
- Løbende overvågning af "diabetisk retinopati" og "svær nonproliferativ diabetisk retinopati" TxGNN-signal (begge flagget uafhængigt) for eventuelle nye forsøgsregistreringer

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

