---
layout: default
title: Eprinomectin
parent: Kun modelforudsigelse (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Eprinomectin
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

# Eprinomectin: Fra Veterinær Antiparasitikum til Kandidose

## Sammenfatning på en sætning

Eprinomectin er et semi-syntetisk avermectin (makrocyklisk lacton) fra avermectin-klassen, som i øjeblikket udelukkende bruges som veterinært antiparasitikum til husdyr, uden nogen godkendt menneskelig indikation i Danmark eller andre steder.
TxGNN-modellen forudsiger, at det kan være effektivt mod **Kandidose**, baseret på indirekte mekanistiske hypoteser, der involverer interferens med ergoserolutbygning og immunomodulation.
Der er i øjeblikket **0 kliniske forsøg** og **0 publikationer**, der direkte understøtter denne omplaceringsvej, hvilket betyder, at forudsigelsen udelukkende er baseret på computationel modellering.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Original indikation | Veterinært antiparasitikum (ingen menneskelig indikation registreret) |
| Forudsagt ny indikation | Kandidose |
| TxGNN forudsigelsesscore | 98.89% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er der ikke tilgængelige detaljerede virkningsmekanisme-data fra Evidenspakken. Baseret på kendt farmakologisk klasseinformation tilhører Eprinomectin avermectin-klassen (makrocykliske lactoner), som udøver sin primære antiparasitiske virkning ved at aktivere glutamat-gated chlorid (GluCl) kanaler i invertebrat nervevæv og muskelsvæv — et mål der ikke eksisterer i svampe. Lægemidlet har dokumenteret effektivitet mod ektoparasitter og endoparasitter hos kvæg, og dets strukturelt nært beslægtede analog ivermectin er blevet mere omfattende studeret i humane medicin.

Den mekanistiske forbindelse til Kandidose foreslået af TxGNN-modellen er baseret på flere indirekte hypoteser: (1) avermectin-klasseforbindelser kan potentielt interferere med fungale ergoserolutbygningsveje (ivermectin er blevet rapporteret in vitro til at inhibere ergoserolsyntese i *Candida*); (2) værtsorganismens IL-4/IL-13 immunomodulation kunne teoretisk ændre det mucosale Th2/Th17 immunmiljø, hvilket indirekte påvirker *Candida*-kolonisering; og (3) inhibering af ABC-transportere (P-glycoprotein) kunne teoretisk forhindre fungale fluconazol efflux-pumper, potentielt virkende som supplement til azolbehandling.

Disse veje forbliver imidlertid helt hypotetiske for Eprinomectin specifikt. Der er aldrig blevet testet nogen direkte antimykotisk aktivitet af Eprinomectin mod *Candida*, og dets sikkerhedsprofil hos menneskelige forsøgspersoner er ikke blevet evalueret. Den biologiske plausibilitet er svag, og enhver mekanistisk forbindelse ville kræve omfattende grundforskning, før klinisk undersøgelse kunne overvejes.

---

## Kliniske forsøgsbeviser

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Eprinomectin (DrugBank ID: DB11405) har ingen markedsføringstilladelser hos Lægemiddelstyrelsen og ingen centraliseret EMA-godkendelse til menneskelig brug. Det er ikke registreret som lægemiddel til menneskelig brug i Danmark.

---

## Sikkerhedshensyn

Se venligst Produktresumé (SmPC) for sikkerhedsinformation. Ingen humane sikkerhedsdata (advarsler, kontraindikationer eller lægemiddel-lægemiddelinteraktioner) var tilgængelige i Evidenspakken for Eprinomectin.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
TxGNN-modellen tildeler en høj forudsigelsesscore (98.89%) til Kandidose-indikationen, men dette afspejler knowledge-graph-forbindethed snarere end biologisk eller klinisk validering. Med nul understøttende kliniske forsøg, nul understøttende publikationer, ingen humane farmakokinetiske data, ingen menneskelig sikkerhedsprofil, ingen dansk eller EMA markedsføringstilladelse, og en mekanistisk forbindelse, der er helt indirekte og ubekræftet, er der utilstrækkelig grundlag til at avancere denne kandidat på nuværende tidspunkt.

**For at fortsætte er følgende nødvendig:**

- **Præcisering af virkningsmekanisme**: Bekræft, hvorvidt Eprinomectin har nogen direkte eller indirekte antimykotisk aktivitet i validerede *in vitro* forsøg mod *Candida* spp.
- **Humane sikkerhedsdata**: Indhent eller generer Phase 1 farmakokinetiske og sikkerhedsdata hos mennesker, da der i øjeblikket ikke findes nogen
- **Formuleringsfeasibilitet**: Evaluer, hvorvidt en klinisk levedygtig administrationsrute (oral, topisk mucosa) eksisterer til menneskelig antimykotisk brug
- **Komparativ benchmark**: Vurder, hvorvidt den forudsagte antimykotisk effekt, hvis bekræftet, ville tilbyde meningsfyldt klinisk fordel i forhold til velkendte azoler, echinocandiner eller polyener
- **DrugBank MOA-data**: Hent fuldstændige mekanisme-, target- og toksicitetsdata fra DrugBank (DB11405) for at muliggøre korrekt mekanistisk og sikkerhedsanalyse
- **Regulatorisk vej-vurdering**: Bestem, hvorvidt en omplaceringsansøgning til EMA eller Lægemiddelstyrelsen ville være mulig givet forbindelsens eksklusivt veterinære status

> ⚠️ **Kun til forskningsbrug**: Forudsigelserne og analysen i denne rapport er beregnet udelukkende til forskningsformål og udgør ikke medicinsk rådgivning. Omplaceringskandidater til lægemidler kræver klinisk validering, før nogen terapeutisk anvendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

