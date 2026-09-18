---
layout: default
title: Penciclovir
parent: Kun modelforudsigelse (L5)
nav_order: 344
evidence_level: L5
indication_count: 10
---

# Penciclovir
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

# Penciclovir: Fra herpes simplex virus-infektioner til fasciolosis

## Sammenfatning på en sætning

> Penciclovir er et guanin-nukleosidanalogen antiviralt lægemiddel, farmakologisk brugt mod herpes simplex virus (HSV)-infektioner ved at kræve viral thymidinkinase (TK) til aktivering.
> TxGNN-modellen forudsiger, at det kan være effektivt mod **fasciolosis** (leverflueinfektioner), med en forudsigelsesscore på **99.06%**,
> men i øjeblikket **ingen kliniske forsøg og ingen publiceret litteratur** understøtter denne retning, og modellens egen mekanistiske begrundelse argumenterer imod biologisk plausibilitet.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Herpes simplex virus (HSV)-infektioner (mekanisme udledt fra bevismappe-begrundelse; strukturerede registreringer over indikationer ikke tilgængelige — se bemærkning nedenfor) |
| Forudsagt ny indikation | Fasciolosis |
| TxGNN-forudsigelsesscore | 99.06% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 |
| Anbefalet beslutning | Hold |

**Bemærkning om oprindelig indikation:** Bevismappe-feltene `original_indications` og `taiwan_regulatory.licenses` er begge tomme, så tekst fra godkendelsesregister til oprindelig indikation er ikke tilgængelig. Indikationen ovenfor er udledt udelukkende fra den mekanistiske beskrivelse indlejret i bevismappe-rationalet (guanin-nukleosidanalogen aktiveret af viral thymidinkinase — den kanoniske Penciclovir/HSV-mekanisme). Dette bør verificeres mod det officielle produktinformationsblad (SmPC) før brug i enhver beslutningsdokument.

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanisme-data for lægemiddelhandling (MOA) markeret som en datakløft (`[Data Gap]`) i den strukturerede lægemiddelpost. Bevismappe-rationalet indeholder dog en delvis mekanistisk beskrivelse: Penciclovir er et guanin-nukleosidanalogen, hvis antivirale virkning afhænger af første-trin-fosforylering af en **virus-specifik thymidinkinase (TK)** — en mekanisme, der er specifik for herpesviruser såsom HSV.

I modsætning til en typisk genfunktioneringskandidat **understøtter** den mekanistiske analyse inkluderet i denne bevismappe **ikke** den forudsagte nye indikation. Fasciolosis er forårsaget af trematoden *Fasciola hepatica/gigantica* (leverflue), en helmint uden kendt virus-type TK-afhængig aktiverings-vej. Rationalet anfører eksplicit, at der er "ingen kendt eller hypotetiseret nukleosid-metabolisme-interferens-mekanisme", der understøtter antiparasitisk aktivitet for Penciclovir, og konkluderer, at den høje TxGNN-similaritetsscore højst sandsynligt er drevet af **videns-graf-indlejrings-nærhed** (f.eks. delte graf-naboer med andre antiparasitiske midler) snarere end ægte farmakologisk plausibilitet.

Med andre ord er dette et tilfælde, hvor modellens kvantitative score (99.06%) er høj, men de kvalitative mekanistiske beviser — hentet fra samme bevismappe — aktivt argumenterer imod klinisk relevans. Denne kombination (høj score, modsidet mekanisme, nul ekstern bevis) er det primære grundlag for "Hold"-anbefalingen nedenfor.

---

## Øvrige forudsagte indikationer (samme bevismappe)

Bevismappen indeholder fire yderligere forskellige forudsagte indikationer for Penciclovir, alle scoret lignende højt af TxGNN men ligeledes uden understøttelse af kliniske forsøg, litteratur eller en plausibel mekanisme:

| Rang | Sygdom | TxGNN-score | Bevisniveau | Anbefaling | Mekanistisk bemærkning |
|------|--------|-------------|------------|-----------|----------------------|
| 3–4 | Cysticercose | 98.99% | L5 | Hold | Ingen overlap med standard albendazol/praziquantel-mekanismer (mikrotubuli-/kalcium-kanal-målgrupper) |
| 5–6 | Coenurose | 98.75% | L5 | Hold | Samme helmint-klasse-begrundelse som cysticercose; sandsynligvis graftstruktur-artefakt |
| 7–8 | Intestinal helminthasis | 98.70% | L5 | Hold | Ingen publiceret in vitro/in vivo anti-helminthisk aktivitetsdata for Penciclovir |
| 9–10 | Ondart pleural mesotheliom | 98.51% | L5 | Hold | Penciclovirs kinase-specificitet er meget selektiv for HSV TK, med meget lav affinitet for pattedyr- (herunder tumor-) kinaser; ingen cellelinje- eller dyremodeldata understøtter antiproliferativ brug |

Alle fem forudsigelser deler samme profil: ingen kliniske forsøg, ingen litteratur, L5-bevis (kun modelforudsigelse), og en mekanistisk begrundelse, der eksplicit advarer imod at tolke scoren som farmakologisk meningsfuld.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

*(Forespørgselslog bekræfter, at ClinicalTrials.gov og WHO ICTRP-søgninger blev udført for alle fem forudsagte sygdomme på 2026-03-24, med nul resultater.)*

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

*(Forespørgselslog bekræfter, at PubMed-søgninger blev udført for alle fem forudsagte sygdomme på 2026-03-24, med nul resultater.)*

---

## Markedsinformation for Danmark

Penciclovir har i øjeblikket **ingen markedsføringsgodkendelser registreret** i denne bevismappe (`total_licenses: 0`, markedsstatus: Ikke markedsført). Detaljer om nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) godkendelser er ikke tilgængelige at liste.

---

## Sikkerhedsmæssige overvejelser

Henvises til det godkendte produktinformationsblad (SmPC) for sikkerhedsoplysninger.

**Vigtigt:** Denne bevismappe flag en **blokerende** datakløft (DG001) — TFDA/mærke-advarsler og kontraindikationer kunne ikke hentes, hvilket i sig selv forhindrer progression til en formel sikkerhedsvurdering (S1). En lægemiddelinteraktions (DDI) forespørgsel returnerede også ingen resultater (`not_found`), hvilket betyder, at fraværet af interaktioner ikke bør antages — det afspejler en datatilgængelighedskløft, ikke en bekræftet ren interaktionsprofil.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
- Alle fem forudsagte indikationer hviler på **L5-bevis** (kun modelforudsigelse) uden nogen understøttende kliniske forsøg eller litteratur.
- Bevismappens egen mekanistiske analyse for den toprangerede forudsigelse (fasciolosis) konkluderer eksplicit, at den høje similaritetsscore sandsynligvis afspejler et videns-graf-indlejrings-artefakt snarere end ægte farmakologisk plausibilitet — den samme begrundelse gælder for de øvrige fire kandidater.
- En **blokerende** datakløft (manglende SmPC/mærke-advarsler og kontraindikationer) forhindrer enhver sikkerhedsvurdering (S1) uanset effektivitetsbevis.
- Penciclovir markedsføres i øjeblikket ikke i Danmark (0 markedsføringsgodkendelser), så der findes ingen lokal doseringform eller godkendt-indikations-vej, der i øjeblikket kan understøtte selv guardrail-baseret off-label-brug.

**For at fortsætte er følgende nødvendig:**
- Hent det officielle SmPC / mærke-advarsler og kontraindikationer (løser DG001, Blokering)
- Få bekræftet mekanisme-data for lægemiddelhandling (MOA) fra DrugBank eller primær litteratur (løser DG002, Høj)
- Gennemfør eller identificer in vitro/in vivo-studier, der tester Penciclovir mod *Fasciola*, *Taenia*-arter eller mesotheliom-cellelinjer, før yderligere bevisniveauopgradering overvejes
- Kør kliniske forsøgs- og litteratursøgninger regelmæssigt igen, da nuværende søgninger (2026-03-24) returnerede nul hits for alle fem kandidatindikationer

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

