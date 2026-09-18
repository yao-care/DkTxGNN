---
layout: default
title: Etodolac
parent: Kun modelforudsigelse (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Etodolac
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

# Etodolac: Fra Smerte/Inflammation (NSAID) til Spondyloartropati

## En-sætnings-sammenfatning

Etodolac er et non-steroidal anti-inflammatorisk lægemiddel (NSAID) med COX-2-præferenciel selektivitet, oprindeligt brugt til osteoartritis og reumatoid artritis.
TxGNN-modellen forudsiger, at det kan være effektivt for **Spondyloartropati** (blandt andre tilstande),
med **0 kliniske prøver** og **0 publikationer** i øjeblikket identificeret for de specifikke forudsagte indikationer — selvom bevis på klasseniveau for NSAID'er ved spondyloartropati er velkendt.

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Osteoartritis, reumatoid artritis, smerte (NSAID) |
| Forudsagt ny indikation | Acromesomelic dysplasi, Hunter-Thompson type (rang 1); **Spondyloartropati** (rang 7, mest klinisk relevant) |
| TxGNN-forudsigelsesscore | 99.97% (rang 1); 99.96% (spondyloartropati) |
| Bevisniveau | L5 (rang 1, kun modelforudsigelse); L4 (spondyloartropati, bevis på klasseniveau for mekanisme) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Vent (samlet); Fortsæt med forbehold (kun spondyloartropati) |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i denne bevissamling. Baseret på kendt farmakologi er etodolac et pyrancarboksylsyre-derivat NSAID, der foretrukket hæmmer cyclooxygenase-2 (COX-2), og dermed reducerer prostaglandin E2 (PGE2)-syntese og dets nedstrøms pro-inflammatoriske effekter. Dets COX-2-selektivitet giver en mere gunstig sikkerhedsprofil for mave-tarmkanalen sammenlignet med ikke-selektive NSAID'er, hvilket gør den egnet til kroniske muskel-skelet-tilstande.

TxGNN-modellen genererede fem unikke forudsagte indikationer for etodolac. De højestrangerede forudsigelser (acromesomelic dysplasi Hunter-Thompson type, brachyolmia-amelogenesis imperfecta syndrom, brachyolmia) er ultra-sjældne genetiske skeletdysplasier forårsaget af specifikke genmutationer (GDF5, TRPV4, PAPSS2 osv.). Den mekanistiske forbindelse mellem COX-2-hæmning og korrektion af medfødte knoglevækstdefekter er ekstremt svag (vurderet til 1/5 stjerner). Disse høje TxGNN-scores afspejler sandsynligvis grafstrukturel nærhed mellem knoglevæv/bindevævsygdoms-knuder snarere end ægte terapeutisk potentiale.

Den mest klinisk meningsfulde forudsigelse er **spondyloartropati** (rang 7, score 99.96%). NSAID'er er etableret førstelinjebehandling for spondyloartropati (herunder ankyloserende spondylitis) ifølge ASAS/EULAR-retningslinjer. Etodolacs COX-2-præferencielle hæmning adresserer direkte ledebetændelse, smerte og morgentstivhed hos disse patienter. Historiske kliniske studier fra 1990'erne–2000'erne har evalueret etodolac ved ankyloserende spondylitis, hvilket giver bevis på klasseniveau. **Myosklerose** (rang 5, score 99.97%) udgør en svag men teoretisk interessant forbindelse via NF-kB-medieret fibrose-modulering, værdig til yderligere forskning.

---

## Sammenfatning af forudsagte indikationer

Da ingen kliniske prøver eller litteratur blev fundet for nogen af de specifikke forudsagte indikationer, opsummerer følgende tabel alle unikke TxGNN-forudsigelser:

| Rang | Forudsagt indikation | TxGNN-score | Bevisniveau | Mekanistisk forbindelse | Anbefaling |
|------|---------------------|-------------|-----------|----------------------|------------|
| 1 | Acromesomelic dysplasi, Hunter-Thompson type | 99.97% | L5 | Meget svag (1/5) — sjælden genetisk knoglesygdom; NSAID kan ikke korrigere GDF5-mutationer | Vent |
| 3 | Brachyolmia-amelogenesis imperfecta syndrom | 99.97% | L5 | Meget svag (1/5) — sjælden genetisk sygdom af knoglevæv og emailleudvikling | Vent |
| 5 | Myosklerose | 99.97% | L5 | Svag (2/5) — teoretisk NF-kB/fibrose-forbindelse; ingen præ-klinisk bevis | Forskeringsspørgsmål |
| **7** | **Spondyloartropati, modtagelighed for** | **99.96%** | **L4** | **Stærk (4/5) — NSAID'er er førstelinjebehandling for spondyloartropati (ASAS/EULAR)** | **Fortsæt med forbehold** |
| 9 | Brachyolmia | 99.96% | L5 | Meget svag (1/5) — overlapper med rang 3; sandsynligvis redundant grafforudsigelse | Vent |

---

## Klinisk prøvebevis

I øjeblikket ikke identificeret nogen relaterede kliniske prøver registreret for etodolac i nogen af de specifikke forudsagte indikationer.

*Bemærk: Selvom der ikke blev identificeret prøver for de eksakte sygdomsbegreber, som blev søgt, eksisterer bevis på klasseniveau for NSAID'er (herunder etodolac) ved spondyloartropati. En bredere søgning ved hjælp af begreber som "ankyloserende spondylitis" eller "aksial spondyloartropati" kombineret med "etodolac" ville sandsynligvis give relevante resultater.*

---

## Litteraturbeviser

I øjeblikket ingen relateret litteratur tilgængelig for etodolac i nogen af de specifikke forudsagte indikationer.

*Bemærk: Som med kliniske prøver eksisterer offentliggjorte studier om etodolac ved ankyloserende spondylitis og relaterede spondyloartropati i den bredere litteratur, men blev ikke indsamlet af de sygdomsspecifikke søgebegreber, som blev brugt.*

---

## Markedsinformation for Danmark

Etodolac er i øjeblikket **ikke markedsført** i Danmark. Ingen markedsføringstilladelser (hverken nationale Lægemiddelstyrelsen eller centraliserede EMA) blev identificeret.

*Bemærk: Etodolac er blevet markedsført i andre lande (f.eks. USA som Lodine; Japan; Indien), men har i øjeblikket ingen gyldig markedsføringstilladelse i Danmark. Enhver gen-indikering-overvejelse ville først kræve regulatorisk vej-vurdering for markedsadgang.*

---

## Sikkerhedsovervejelser

Se venligst den godkendte produktresumé (SmPC) for sikkerhedsinformation.

*Da etodolac ikke er markedsført i Danmark, skal produktresumé (SmPC) fra et referenceland (f.eks. FDA-etiket for Lodine) konsulteres. Vigtige sikkerhedsproblemer, der er fælles for alle NSAID'er, omfatter:*
- *Kardiovaskulære trombotiske begivenheder*
- *Mave-tarm-blødning, sår og perforation*
- *Nyreproblemer*
- *Leverproblemer*
- *Alvorlige hudreaktioner (Stevens-Johnson syndrom, toksisk epidermale nekrolyse)*

---

## Konklusion og næste trin

**Beslutning: Vent** (samlet); **Fortsæt med forbehold** (kun spondyloartropati)

**Begrundelse:**
Størstedelen af TxGNN-forudsigelserne (4 ud af 5 unikke indikationer) målretter ultra-sjældne genetiske knoglesygdomme, for hvilke en NSAID-mekanisme ikke tilbyder noget plausibelt terapeutisk potentiale — disse er klassificeret som "Vent". Spondyloartropati-forudsigelsen, selvom den er rangeret 7. efter TxGNN-score, er den eneste klinisk handlingsorienteret kandidat, støttet af stærk bevis på klasseniveau for mekanisme og etablerede retningslinjer. Men da etodolac ikke er markedsført i Danmark, og ingen indikationsspecifikke prøver blev identificeret, er yderligere trin nødvendige før fremskridtlighed.

**For at fortsætte er følgende nødvendigt:**
- Detaljerede data om virkningsmekanisme for etodolac (DrugBank API-forespørgsel til løsning af datagab DG002)
- Sikkerhedsdata fra produktresumé (SmPC) fra en referencereguleringsmyndighed (til løsning af datagab DG001)
- Bredere litteratursøgning for etodolac ved ankyloserende spondylitis/aksial spondyloartropati (ved hjælp af udvidede søgebegreber)
- Regulatorisk vej-vurdering for markedsadgang i Danmark (import/compassionate use/klinisk prøve)
- Interaktionsprofil for lægemidler (aktuelle DDI-data returnerede ingen resultater)
- For myosklerose-forudsigelsen: præ-klinisk vurdering af NSAID'ers anti-fibrose-effekter før yderligere overvejelse

---

*Denne rapport blev genereret den 2026-04-05 baseret på bevissamling v4 (datakutoff: 2026-04-05). Resultaterne er til forskningsformål og udgør ikke medicinsk rådgivning. Alle lægemiddel-gen-indikeringer kræver klinisk validering før anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

