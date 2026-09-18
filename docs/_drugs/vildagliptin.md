---
layout: default
title: Vildagliptin
parent: Kun modelforudsigelse (L5)
nav_order: 471
evidence_level: L5
indication_count: 10
---

# Vildagliptin
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

# Vildagliptin: Fra type 2-diabetes mellitus til klassisk stiff person-syndrom

## Resumé i én sætning

Vildagliptin er en dipeptidylpeptidase-4 (DPP-4)-hæmmer, en lægemiddelklasse, der internationalt bruges til glykæmisk kontrol ved type 2-diabetes mellitus. TxGNN-modellen forudsiger, at det kan være effektivt mod **klassisk stiff person-syndrom**, men denne retning understøttes i øjeblikket kun af modellens similaritetsscore — **ingen kliniske forsøg og ingen litteratur** er blevet identificeret. Det foreslåede mekanistiske link betragtes også som svagt ifølge modellens egen begrundelsestekst.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Type 2-diabetes mellitus (glykæmisk kontrol) — generel viden om DPP-4-hæmmerklassen; ikke til stede i det leverede regulatoriske datasæt |
| Forudsagt ny indikation | Klassisk stiff person-syndrom |
| TxGNN-forudsigelsesscore | 99.88% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i evidenspakken (markeret som et datakløft med høj alvorlighed). Baseret på generel farmakologisk viden tilhører vildagliptin DPP-4-hæmmerklassen, som øger endogene inkretin-koncentrationer (GLP-1/GIP) for at forbedre glykæmisk kontrol; dets virkning ved type 2-diabetes er blevet etableret i denne sammenhæng.

Klassisk stiff person-syndrom er derimod en autoimmun neurologisk sygdom, hvor anti-GAD65-antistoffer svækker GABAerg neurotransmission og fremkalder muskelstivhed og kramper. Der er ingen etableret overlap mellem inkretin/glucose-metabolisme-vej og GABAerg neurotransmission eller anti-GAD65-medieret autoimmunitet.

Selvom DPP-4 (CD26) har en anerkendt rolle i T-celle-immunregulering, er der i øjeblikket ingen evidens for, at DPP-4-hæmning modulerer anti-GAD65-autoimmun aktivitet eller genopretter GABAerg signalerings-underskud. Modellens egen begrundelse for ombrugning karakteriserer dette som en sandsynlig indirekte association, der stammer fra delt vidensgraf-noder (f.eks. "diabetisk neuropati") snarere end et ægte mekanistisk link, og beskriver eksplicit den mekanistiske evidens som svag.

Det er også værd at bemærke, at TxGNN's top 10-kandidater for dette lægemiddel indeholder kun fem forskellige sygdomme, hver duplikeret (klassisk stiff person-syndrom, fokalt stiv lemme-syndrom, thiamin-responsivt dysfunktionssyndrom, opsismodysplasi og lægemiddelindukeret lokaliseret lipodystrofi), alle med tilsvarende høje men i det væsentlige udifferentierede scores (~99.8–99.9%) og alle bedømt L5/Afvent. Dette mønster er i overensstemmelse med et modelniveau-signal snarere end en kurateret, sygdomsspecifik hypotese.

---

## Klinisk forsøgsevidence

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidence

I øjeblikket er der ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Vildagliptin har i øjeblikket **ingen markedsføringstilladelse i Danmark** — det leverede datasæt angiver 0 licenser og en markedsstatus på "Ikke markedsført." Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) godkendelsesrecords var tilgængelige for dette produkt i evidenspakken.

---

## Sikkerhedsovervejelser

Se venligst den godkendte produktinformation (SmPC) for sikkerhedsinformation.

*Bemærk: Evidenspakken markerer hentning af produktets advarsels-/kontraindikationstekst som et blokerende datakløft (DG001), hvilket betyder, at denne kandidat endnu ikke kan fortsætte til en formel sikkerhedsvurdering (S1).*

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
- Evidensniveauet er L5 — associationen hviler udelukkende på TxGNN-similaritetsscoret, uden identificerede understøttende kliniske forsøg eller litteratur på tværs af alle 10 forudsagte sygdomskandidater for dette lægemiddel.
- Det foreslåede mekanistiske link mellem DPP-4/inkretin-farmakologi og anti-GAD65-medieret autoimmun GABAerg dysfunktion vurderes eksplicit som svagt, hvilket sandsynligvis afspejler en indirekte vidensgraf-association snarere end en plausibel biologisk hypotese.
- Et blokerende datakløft (manglende SmPC-advarsler/kontraindikationer) forhindrer denne kandidat i at komme ind i selv det indledende sikkerhedsscreeningsstadium (S1).
- Lægemidlet er i øjeblikket ikke markedsført i Danmark, så der er ingen eksisterende lokal sikkerhed eller brugserfaringer at trække på.

**For at fortsætte er følgende nødvendigt:**
- Dansk/EU-produktinformation (SmPC) med fulde advarsler, kontraindikationer og lægemiddelinteraktionsdata — påkrævet for at fjerne det blokerende datakløft før enhver sikkerhedsvurdering
- Bekræftet virkningsmekanisme (DrugBank eller primær litteratur) for korrekt at evaluere mekanistisk plausibilitet
- Uafhængig litteratur eller præ-klinisk evidens, der forbinder DPP-4-hæmning til GAD65-medieret autoimmun neurologisk sygdom, hvis denne hypotese skal forfølges videre
- Præcisering af, hvorfor TxGNN returnerede duplikerede/næsten identiske top-kandidater, for at udelukke en model- eller pipeline-artefakt før videre evalueringsressourcer forpligtes til denne kandidat

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

