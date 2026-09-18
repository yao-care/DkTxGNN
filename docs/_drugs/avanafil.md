---
layout: default
title: Avanafil
parent: Kun modelforudsigelse (L5)
nav_order: 50
evidence_level: L5
indication_count: 0
---

# Avanafil
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **0** stk.
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

# Avanafil: Ingen TxGNN-oldingslægeprognoser genereret

## Ét-sætnings oversigt

Avanafil (DB06237) er en selektiv fosfodiesterase type 5 (PDE5)-hæmmer kendt internationalt for behandlingen af erektil dysfunktion, markedsført som Stendra og Spedra på forskellige markeder.
TxGNN-pipelinen genererede ingen oldingslægeforudsigelser for dette lægemiddel i det aktuelle kørselsløb (v4, dataindsamling: 4. april 2026).
To uløste datakløfter — manglende virkningsmekanisme og manglende sikkerhedsdata — forhindrer gennemførelse af standard-oldingslægeevalueringen; **denne rapport fungerer derfor som en datakløft-vurdering snarere end en fuldstændig oldingslægeanbefaling.**

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Erektil dysfunktion (stammende fra generel farmakologisk viden; ikke registreret i det aktuelle Evidence Pack) |
| Forudsagt ny indikation | Ingen prognoser tilgængelige |
| TxGNN-prognoseresultat | Ikke applicable |
| Evidensniveau | L5 — pipeline producerede ingen kandidater |
| Markedsstatus i Danmark | Ikke fundet i kildedatabase |
| Antal markedsføringstilladelser | 0 (i kildedatabasen) |
| Anbefalet beslutning | Afvente |

> **⚠ Vigtig forbehold vedrørende markedsstatus:** Kildedata til dette Evidence Pack stammer fra en taiwansk regulatorisk database. Avanafil er autoriseret i Den Europæiske Union under den centraliserede procedure som **Spedra (EU/1/13/841)** til behandling af erektil dysfunktion hos voksne mænd. Danske sundhedsfagpersoner bør verificere den aktuelle status direkte hos Lægemiddelstyrelsen eller EMA's produktdatabase, da indgangen "ikke fundet" sandsynligvis er en artefakt af kildedatabasens omfang, ikke en nøjagtig afspejling af danske markeds tilgængelighed.

---

## Hvorfor blev der ikke genereret nogen prognose

TxGNN-modellen returnerede ingen oldingslægekandidater for avanafil i dette kørselsløb. To mulige forklaringer bør undersøges, før der konkluderes, at der ikke findes noget oldingslægesignal:

1. **Vidensgrafs afbildningskløft.** Hvis avanafil ikke blev succesfuldt afbildet på en DrugBank- eller sygdomsknude i vidensgrafen, kan der ikke scoreS kandidatkanter. Forespørgselslisten bekræfter, at DrugBank-opslaget returnerede et resultat (succes), men upstream-afbildning ind i TxGNN-grafnodesammensætningen kan stadig være ufuldstændig.

2. **Manglende indikationsdata.** Feltet `original_indications` er tomt i Evidence Pack'et. TxGNN's grafbaserede scoring er delvis afhængig af eksisterende godkendt indikationskanter. Uden en seedindikationsknude kan visse inferenssti blive undertrykt.

**Hvad der kendes fra farmakologi:** Avanafil hæmmer selektivt cyclic GMP-specifik PDE5, hvilket fremmer glat muskelslappelse og vasodilatation via stofskiftet nitric oxide–cGMP. Denne mekanisme er blevet udforsket ud over erektil dysfunktion i lægemiddelklasser, herunder pulmonal arteriel hypertension (sildenafil, tadalafil) og Raynauds fænomen. Hvorvidt avanaifils højere PDE5-selektivitet og kortere halveringstid omsætter sig til en særskilt oldingslægeprofil i forhold til PDE5-hæmmere fra første generation, forbliver et åbent forskningsspørgsmål — men dette kan ikke vurderes, før pipelinens datakløfter er løst.

---

## Sikkerhedshensyn

Sikkerhedsdata mangler i det aktuelle Evidence Pack. Henviser til den godkendt Produktresumé (SmPC) for **Spedra (avanafil)** for fuldstændig præskriberingsinformation. Vigtige områder, der skal gennemgås, omfatter:

- **Absolutte kontraindikationer:** Samtidig brug med enhver form for organisk nitrat eller nitrogenoxidgiver (risiko for alvorlig blodtryksfald)
- **Kardiovaskulære forsigtighedsregler:** Risikovurdering for patienter med underliggende kardiovaskulær sygdom før ordinering
- **Lægemiddelinteraktioner:** Avanafil omsættes primært af CYP3A4; stærke CYP3A4-hæmmere (f.eks. ketoconazol, ritonavir) øger avanafil-eksponeringen betydeligt
- **Visuelle/auditive bivirkninger:** I overensstemmelse med PDE5-hæmmerklassen

---

## Konklusion og næste trin

**Beslutning: Afvente**

**Begrundelse:**
TxGNN-pipelinen returnerede ingen oldingslægekandidater, og to datakløfter — manglende sikkerhedsdata (alvorlighed: Blokerende) og manglende virkningsmekanisme (alvorlighed: Høj) — forhindrer evalueringen i at avancere gennem standard-S1-screeningporten.

**For at fortsætte er følgende nødvendigt:**

- [ ] **Løs DG002 (MOA):** Spørg DrugBank API'et for DB06237 for at hente farmakologi, virkningsmekanisme og lægemiddelklassifikationer
- [ ] **Løs DG001 (sikkerhed):** Indhent Spedra SmPC fra EMA's produktdatabase eller Lægemiddelstyrelsen for at udfylde advarsler og kontraindikationer
- [ ] **Undersøg TxGNN-afbildning:** Verificer, om avanafil (DB06237) er korrekt afbildet på en knude i TxGNN-vidensgrafen (`data/external/drugbank_vocab.csv`); hvis fraværende, tilføj manuelt og kør prediktionspipelinen igen
- [ ] **Bekræft markedsstatussen i Danmark:** Krydsreferencer Spedra EU/1/13/841 mod Lægemiddelstyrelsens register for at rette Evidence Pack-markedsstatus-feltet, inden den endelige rapport genereres
- [ ] **Kør Evidence Pack-generering igen** efter at alle datakløfter er løst, målrettet Evidence Pack v5 eller senere

---

*Denne rapport genereres til forskningsformål alene og udgør ikke medicinsk rådgivning. Alle oldingslægekandidater kræver klinisk validering, før nogen terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

