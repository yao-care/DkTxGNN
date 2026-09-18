---
layout: default
title: Bezlotoxumab
parent: Kun modelforudsigelse (L5)
nav_order: 63
evidence_level: L5
indication_count: 10
---

# Bezlotoxumab
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

# Bezlotoxumab: Fra Clostridioides difficile-infektion til akut kvindelig bækkenbetændelse

## Én-sætnings-resumé

Bezlotoxumab (Zinplava) er et humant monoklonalt antistof, der oprindeligt blev udviklet til at forebygge tilbagefald af *Clostridioides difficile*-infektion (CDI) ved at neutralisere det bakterielle TcdB-toxin.
TxGNN-modellen forudsiger, at det kan være effektivt til behandling af **akut kvindelig bækkenbetændelse**, men denne forudsigelse understøttes af **ingen kliniske forsøg** og **ingen publiceret litteratur**.
Kritisk set indikerer en mekanismisk analyse, at denne forudsigelse højst sandsynligt afspejler en strukturel artefakt i vidensgrafen snarere end en reel terapeutisk mulighed.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Reduktion af tilbagefald af *Clostridioides difficile*-infektion (CDI) hos voksne, der modtager antibakterielbbehandling og har høj risiko for tilbagefald |
| Forudsagt ny indikation | Akut kvindelig bækkenbetændelse |
| TxGNN-forudsigelsesscore | 99.89% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke på markedet |
| Antal markeringsgodkendelser | 0 |
| Anbefalet beslutning | **Afvent** |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede mekanismedata ikke tilgængelige i bevissamlingen. Baseret på kendt farmakologisk information er bezlotoxumab et fuldt humant IgG1-monoklonalt antistof (DrugBank: DB13140), der binder med høj affinitet og specificitet til *Clostridioides difficile*-toxin B (TcdB) og neutraliserer dets cytotoksiske aktivitet. Det har ingen iboende antibakterielle egenskaber og ingen kendt bred anti-inflammatorisk eller immunomodulatorisk virkning. Dets kliniske nytte er snævert defineret: reduktion af CDI-tilbagefald hos højrisikopatienter, der allerede modtager antibiotikumbehandling.

Den mekanismiske forbindelse mellem bezlotoxumab og akut kvindelig bækkenbetændelse vurderes som ekstremt svag. Akut bækkenbetændelse er primært forårsaget af polymikrobial infektion (hyppigst *Neisseria gonorrhoeae*, *Chlamydia trachomatis* og enteriske organismer) — ingen af hvilke involverer *C. difficile* TcdB som en patogen mekanisme. Neutralisering af TcdB ville have ingen forventet biologisk virkning på den inflammatoriske kaskade, peritoneal bakteriel belastning eller vævsskade karakteristisk for bækkenbetændelse.

Ved gennemgang af alle ti forudsagte indikationer i denne bevissamling (rang 1–10) vedrører hver forudsigelse gynækologisk og bækkenanatomi (bækkenbetændelse, tubo-ovariële cyster, tubegraviditet, salpingitis isthmica nodosa, bredt ligament-lidelse). Denne slående anatomiske klyngering tyder stærkt på, at forudsigelserne stammer fra delte "bæken/adnekal inflammation"-noder i TxGNN-vidensgrafen snarere end fra reel mekanismisk rimelighed. Dette mønster stemmer overens med en kendt begrænsning af grafbaserede modeller: anatomisk nærhedsbias, hvor noder forbundet gennem delt anatomisk område genererer urigtigt høje scores. **Disse forudsigelser bør tolkes som modelstøj snarere end genbrugssignaler.**

---

## Klinisk forsøgsbevis

I øjeblikket er der ingen relaterede registrerede kliniske forsøg.

---

## Litteraturbevis

I øjeblikket er der ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Bezlotoxumab markedsføres ikke i øjeblikket i Danmark og har ingen markeringsgodkendelser givet af Lægemiddelstyrelsen eller via EMA's centraliserede procedure, der gælder i Danmark.

> **Notat for klinikere:** I andre jurisdiktioner (f.eks. USA og EU) markedsføres bezlotoxumab som **Zinplava** (Merck Sharp & Dohme) til forebyggelse af CDI-tilbagefald. EMA's centraliserede markeringsgodkendelse (EU/1/16/1136) blev givet i 2017, men er siden blevet trukket tilbage fra EU-markedet. Sundhedspersonale, der kræver adgang i Danmark, bør kontakte Lægemiddelstyrelsen vedrørende muligheder for navngivet patientbehandling eller compassionate use.

---

## Sikkerhedshensyn

Se venligst produktkarakteristikken (SmPC) for sikkerhedsinformation.

> Der blev ikke hentet data om lægemiddel-lægemiddel-interaktioner, vigtige advarsler eller kontraindikationsdata i denne bevissamling. Den kendte kliniske sikkerhedsprofil for bezlotoxumab fra regulatorisk godkendelse (FDA, tidligere EMA) bør gennemgås direkte fra Zinplavas SmPC eller FDA's foreskrivningsinformation forud for enhver klinisk overvejelse.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
Alle ti TxGNN-forudsigelser for bezlotoxumab vedrører gynækologiske bækkentilstande, for hvilke der ikke er mekanismisk grundlag — bezlotoxumab virker udelukkende ved at neutralisere *C. difficile* TcdB-toxin og har ingen kendt antibakterielbegenskaber, anti-inflammatorisk eller hormonal aktivitet relevant for bækkenbetændelse eller adnekal patologi. Den ensartede klyngering af forudsigelser omkring bækkenanatomi er en stærk indikator på vidensgrafs strukturelle bias snarere end et reel genbrugssignal. Der er ingen understøttende klinisk forsøgs- eller litteraturbevis for nogen af de forudsagte indikationer.

**For at fortsætte ville følgende være nødvendigt:**

- **Grundårsagsanalyse af KG-artefakten:** Undersøg hvilke nodeforbindelser i TxGNN-vidensgrafen der driver bækkenanatomi-klyngingen for bezlotoxumab, og anvend en grafniveaukorrektion eller et eksklusionfilter for anatomisk nærhedsbias.
- **Data om virkningsmekanisme (DrugBank):** Hent den fulde MOA-post fra DrugBank (DB13140) for formelt at dokumentere målspecificitet og bekræfte fraværet af off-target-aktivitet relevant for nogen forudsagt indikation.
- **Sikkerhedsdokumentation:** Indhent Zinplavas SmPC (EMA eller FDA) for at fuldføre sikkerhedsprofilen — dette er i øjeblikket markeret som et Blocking data gap (DG001).
- **Alternativ forudsigelsesgennemgang:** Kør TxGNN-forudsigelse igen med bias-korrigerede grafvægte eller et strengere mekanismisk filter for at bestemme, om der findes nogle biologisk plausible genbrugskandidater for bezlotoxumab ud over CDI-indikationsområdet (f.eks. andre *C. difficile*-forbundne komplikationer såsom toksisk megacolon eller post-CDI inflammatoriske tarmsygdomme).
- **Vurdering af regulatorisk vej:** Hvis en reel plausibel indikation identificeres i fremtiden, ville regulatorisk konsultation med Lægemiddelstyrelsen vedrørende en ansøgning om ny markeringsgodkendelse eller linjeudvidelse være påkrævet, givet lægemidlets nuværende fraværelse fra det danske marked.

---

> ⚠️ **Ansvarsfraskrivelse:** Denne rapport er beregnet til forskningsmæssig reference og udgør ikke medicinsk rådgivning. Lægemiddelgenbrugskandidater kræver klinisk validering før anvendelse. Alt indhold bør gennemgås sammen med den fuldt godkendte produktinformation.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

