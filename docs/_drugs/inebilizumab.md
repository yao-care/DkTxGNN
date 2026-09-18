---
layout: default
title: Inebilizumab
parent: Kun modelforudsigelse (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
---

# Inebilizumab
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

# Inebilizumab: Fra B-celle-depletionsterapi til lægemiddelinduceret osteoporose

## Resumé på en sætning

Inebilizumab er et humaniseret anti-CD19-monoklonalt antistof, der depleterer en bred B-celle-linje (herunder plasmacellepræcursorer); denne evidenspakke indeholder ingen registrerede oprindelige indikationer eller godkendt produktinformation til Danmark, og virkningsmekanisme er markeret som en datakløft. TxGNN-modellen forudsiger, at det kan være effektivt for **lægemiddelinduceret osteoporose**, men denne retning understøttes i øjeblikket af **0 kliniske forsøg** og **0 publikationer** — det er et modelbaseret, uverificeret signal.

---

## Kort oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ikke tilgængelig — ingen godkendt indikation på filen (lægemiddel ikke markedsført i Danmark; `original_indications` tom) |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose |
| TxGNN-forudsigelsesscore | 96.44% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Vent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede virkningsmekanisme-data ikke tilgængelige (markeret som højalvorligt datakløft i denne evidenspakke). Baseret på hvad den understøttende litteratur og rationale-tekster i denne pakke etablerer, er inebilizumab et humaniseret **anti-CD19-monoklonalt antistof**, der depleterer en bred B-celle-linje, som strækker sig længere ind i plasmacellepræcursor-kompartimentet end CD20-målrettede midler såsom rituximab.

Den forudsagte nye indikation, lægemiddelinduceret osteoporose, er patofysiologisk drevet af osteoklast-aktivering og RANKL/OPG-ubalance (klassisk set med glukokortikoid-induceret knogletab). B-celler er kendt for at sekretere både RANKL og OPG og kan modulere knogleombygning, hvilket er den mekanistiske sammenhæng, som TxGNN's videngraf synes at følge.

Imidlertid bør denne forbindelse læses som spekulativ snarere end etableret: virkningen (knoglebeskyttende vs. knogletab-forværrende) er ikke fastslået i litteraturen, og der er ingen evidens, der knytter B-celle-depletion specifikt til den "lægemiddelinducerede" etiologi for osteoporose (i modsætning til andre årsager). Evidenspakken selv karakteriserer dette som en kandidat med lav tillid, der stammer fra indirekte videngraf-klynger snarere end en sygdomsspecifik mekanistisk begrundelse, og den bærer det svageste understøttede evidensniveau (L5) blandt de ti rangerede kandidater i denne pakke.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Der er i øjeblikket ingen markedsføringstilladelser registreret for inebilizumab i Danmark — evidenspakken registrerer markedsstatus som "Ikke markedsført" med 0 samlede licenser.

---

## Sikkerhedsovervejelser

Se venligst produktinformation (SmPC) for godkendt sikkerhedsinformation. (Nøgleadvarsler, kontraindikationer og lægemiddel-lægemiddelinteraktions-data er alle markeret som datakløfter eller ikke fundet i denne evidenspakke — især betyder det blokeringskritiske datakløft DG001 vedrørende etiketadvarsler/kontraindikationer, at denne kandidat ikke endnu kan bestå en indledende sikkerhedsscreening.)

---

## Konklusion og næste skridt

**Beslutning: Vent**

**Begrundelse:**
Denne kandidat har ingen understøttende kliniske forsøg eller litteratur (0/0), ligger på modelforudsigelse-baseret evidensniveau (L5), og dens egen mekanistiske begrundelse markerer lægemiddel-sygdom-forbindelsen som indirekte og retningsbestemt usikker. Kombineret med lægemidlets uregistrerede status i Danmark og et blokeringskritisk sikkerhedsdatakløft, er der intet grundlag for at fremme denne indikation ud over hypotesegenerering på nuværende tidspunkt.

**For at fortsætte kræves følgende:**
- TFDA/Lægemiddelstyrelsen-etiketter: advarsler og kontraindikationer (DG001, Blokeringstype — påkrævet før enhver S1-sikkerhedsscreening kan påbegyndes)
- Bekræftet virkningsmekanisme-data via DrugBank (DG002, Høj alvorlighed — nødvendig for korrekt at vurdere mekanistisk relevans for knoglestofskifte)
- Prækliniske eller mekanistiske studier, der specifikt adresserer B-celle-depletions virkning på osteoklast/RANKL-OPG-aktivitet i lægemiddelinduceret (vs. anden-etiologi) osteoporose-kontekst
- Løbende overvågning for ethvert fremtidigt forsøg eller case-report-signal, da ingen i øjeblikket eksisterer

*Bemærk: Den samme evidenspakke indeholder en betydeligt bedre-understøttet kandidat — plasmacelle-myelom (rang 7/8, score 92.75%, evidensniveau L3, "Research Question"-stadium) — understøttet af et afsluttet fase 1-forsøg (NCT01861340) og 2 PubMed-poster. Hvis en rapport om denne indikation ønskes i stedet, skal du give mig besked og jeg vil producere den.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

