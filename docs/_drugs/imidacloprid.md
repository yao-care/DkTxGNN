---
layout: default
title: Imidacloprid
parent: Kun modelforudsigelse (L5)
nav_order: 226
evidence_level: L5
indication_count: 10
---

# Imidacloprid
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

# Imidacloprid: Fra Insekticid (Ingen godkendt humanmedicinsk indikation) til Cauda Equina Syndrom

## Sammenfattelse i én sætning

Imidacloprid (DrugBank ID: DB11421) er et neonikotinoid insekticid uden godkendt human terapeutisk indikation og uden markedsføringstilladelse i Danmark. TxGNN-modellen forudsiger potentiel effektivitet for **Cauda Equina Syndrom**, men denne forudsigelse er i øjeblikket understøttet af **nul kliniske forsøg** og **nul publikationer** — den hviler udelukkende på viden-graf-topologi snarere end på nogen farmakologisk eller klinisk evidens.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Oprindelig indikation | Ingen — Imidacloprid er et landbrugs-/veterinært insekticid; det har ingen godkendt human terapeutisk indikation |
| Forudsagt ny indikation | Cauda Equina Syndrom |
| TxGNN-forudsigelsesscore | 99.99% |
| Evidensniveau | L5 (modelforudsigelse alene, ingen understøttende studier) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data vedrørende Imidacloprids virkningsmekanisme hos mennesker er ikke tilgængelige (**[Data Gap]**). Det, der vides, er, at Imidacloprid virker som et neonikotinoid insekticid ved selektivt at binde sig til insekt-nikotiniske acetylcholin-receptorer (nAChR). Dets affinitet for pattedyr-nAChR er meget lav — dette er netop det farmakologiske grundlag for dens relativt lave toksicitet for mennesker og andre pattedyr, og grunden til, at den bruges som pesticid snarere end som lægemiddel.

Cauda equina syndrom er en akut neurokirurgisk nødsituation forårsaget af kompression af lumbosacral nerverodderne, hvilket typisk kræver øjeblikkelig kirurgisk dekompression. Der er ingen etableret eller plausibel patofysiologisk forbindelse mellem et insekt-selektivt nAChR-virkende insekticid og denne tilstand. Den meget høje TxGNN-score (0,9999) afspejler højst sandsynligt topologisk lighed mellem knuder i vidensgrafen snarere end ægte biologisk plausibilitet.

**Sammenfatning: det mekanistiske grundlag for denne forudsigelse er svagt til fraværende.** Dette bør behandles som et hypotesegenererende signal alene, ikke som bevis på terapeutisk potentiale, og det opfylder i øjeblikket ikke tærsklen for yderligere farmakologisk eller klinisk undersøgelse.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

*(Forespørgsellog bekræfter 0 resultater fra ClinicalTrials.gov og ICTRP for "Imidacloprid" + "cauda equina syndrome", søgt på to separate tidspunkter.)*

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

*(Forespørgsellog bekræfter 0 resultater fra PubMed for "Imidacloprid" + "cauda equina syndrome".)*

---

## Markedsinformation for Danmark

Imidacloprid har **ingen markedsføringstilladelse** i Danmark (Lægemiddelstyrelsen) som human lægemiddelprodukt. Markedsstatus er registreret som **Ikke markedsført**, med 0 samlede licenser på fil. Der eksisterer ingen produkt-, doseringsform- eller godkendt indikationsdata for denne forbindelse i det danske register.

---

## Sikkerhedshensyn

Der er i øjeblikket ingen humane sikkerhedsdata tilgængelige for denne forbindelse:

- **Vigtige advarsler**: Ikke tilgængelige (datakløft)
- **Kontraindikationer**: Ikke tilgængelige (datakløft)
- **Lægemiddelinteraktioner**: Ingen interaktionsdata fundet i DDI-databaseforespørgsel (forespørgselstatus: ikke fundet)

Fordi Imidacloprid ikke har noget godkendt produktresumé (SmPC) som human lægemiddelprodukt i Danmark, eksisterer der intet autoritativt human sikkerhedsreference. Dette er markeret som en **Blokerende** datakløft (DG001) — den forhindrer denne kandidat i at fortsætte til selv en foreløbig (S1) sikkerhedsevaluering.

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
- Den forudsagte indikation (cauda equina syndrom) har **absolut ingen beviser fra kliniske forsøg eller litteratur** (Evidensniveau L5 — modelforudsigelse alene).
- Den foreslåede mekanistiske forbindelse er ikke biologisk plausibel: Imidacloprids terapeutiske rationale som insekticid afhænger af selektivitet for insekt-nAChR over pattedyr-nAChR, hvilket argumenterer *imod* relevant human farmakologisk aktivitet snarere end for det.
- Imidacloprid har ingen godkendt human indikation nogetsteds og ingen markedsføringstilladelse i Danmark (0 licenser), så der er intet eksisterende klinisk brugsmønster at grundfeste ombytte på.
- Humane sikkerhedsdata er helt fraværende, hvilket er en **Blokerende** datakløft (DG001) — den forhindrer denne kandidat i at fortsætte til selv en foreløbig sikkerhedsevaluering (S1).

**For at fortsætte er følgende nødvendigt:**
- Bekræftet virkningsmekanisme (MOA) data i human/pattedyr-systemer (i øjeblikket en høj-alvorligheds datakløft, DG002)
- Human toksikologi/sikkerhedsdata tilstrækkeligt til at understøtte en indledende sikkerhedsevaluering (i øjeblikket en **Blokerende** datakløft, DG001)
- Uafhængig verifikation af disease-node-kortlægningskvalitet (f.eks. bekræft, at dette ikke er en vidensgrafartefakt eller et falsk-positivt signal) før yderligere investering
- Som minimum prekliniske eller mekanistiske studier, der etablerer biologisk plausibilitet, før man overvejer at påbegynde klinisk evidensgenerering

**Bemærk:** Givet den fuldstændige mangel på understøttende bevis, det implausible mekanistiske rationale, og lægemidlets status som et ikke-terapeutisk insekticid uden regulatorisk tilstedeværelse i Danmark, anbefales denne kandidat ikke for yderligere udvikling på nuværende tidspunkt. Denne vurdering er til forskningsreference alene og udgør ikke medicinsk rådgivning.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

