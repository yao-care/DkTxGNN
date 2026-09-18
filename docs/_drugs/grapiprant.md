---
layout: default
title: Grapiprant
parent: Kun modelforudsigelse (L5)
nav_order: 213
evidence_level: L5
indication_count: 10
---

# Grapiprant
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

# Grapiprant: Fra Canin Artrose-relateret Smerte til Amenorrhea

## Et-sætnings Resume

Grapiprant (Galliprant) er en EP4-prostaglandinreceptorantagonist, der i øjeblikket udelukkende er godkendt som veterinærmedicin til smerte og inflammation forbundet med artrose hos hunde.
TxGNN-modellen forudsiger, at det kan være relevant for **Amenorrhea**, med en forudsigelsesscore på **98.91%**.
Der er dog i øjeblikket **ingen kliniske forsøg og ingen publiceret litteratur**, der understøtter denne retning, hvilket gør dette til en ren modelforudsigelse, der kræver betydelig forsigtighed — især da den mekanistiske begrundelse indeholder en iboende modsigelse.

---

## Hurtigt Overblik

| Punkt | Indhold |
|------|---------|
| Oprindelig Indikation | Smerte og inflammation forbundet med artrose hos hunde (kun til veterinærbrug) |
| Forudsagt Ny Indikation | Amenorrhea |
| TxGNN-forudsigelsesscore | 98.91% |
| Bevisniveau | L5 |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Grapiprant fungerer som en selektiv antagonist af EP4-prostaglandinreceptoren, blokerende downstream-signalering af prostaglandin E2 (PGE2) ved denne specifikke receptorsubtype. I modsætning til traditionelle NSAIDs, der hæmmer cyclooxygenase-enzymer opstrøms, målretter Grapiprant udelukkende én receptor i prostanoidstien, som i veterinærbrug oversættes til analgesi og anti-inflammatoriske effekter med potentielt mere målrettet bivirkningsprofil.

Den mekanistiske forbindelse til amenorrhea hviler på den kendte rolle af PGE2–EP4-signalering i ovulationsregulering. Eksperimentelle data fra EP4-knockout-mus viser, at fravær af EP4-receptorfunktion resulterer i ovulationssvigt, hvilket tyder på, at denne receptor er nødvendig for succesfuld follikelsprængning. TxGNN-modellen kan have identificeret denne biologiske forbindelse som et potentielt terapeutisk mål.

Imidlertid bliver ræsonnementet her selvmodsigende: hvis EP4-signalering er *nødvendig* for ovulation, så ville en EP4-*antagonist* forventes at svække ovulation og potentielt fremkalde — snarere end at behandle — amenorrhea. Den mekanistiske retning er derfor omvendt i forhold til et terapeutisk formål. Desuden er amenorrhea en klinisk heterogen tilstand med et bredt spektrum af årsager (hypothalamus-nedsat, hypofyse-nedsat, ovarial, anatomisk), hvoraf langt størstedelen ikke har etableret forbindelse til EP4-overaktivering.

---

## Bevis fra Kliniske Forsøg

Der er i øjeblikket ingen registrerede kliniske forsøg, der er relateret til dette.

---

## Bevis fra Litteratur

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Status på det danske Marked

Grapiprant har ingen markedsføringsgodkendelser i Danmark. Lægemidlet er ikke registreret hos Lægemiddelstyrelsen og har ingen EMA-centraliseret godkendelse til humant brug. Det er godkendt i EU som et veterinærmedicinalprodukt (Galliprant, til hunde), men denne godkendelse strækker sig ikke til humant terapeutisk brug.

---

## Sikkerhedsovervejelser

Detaljerede sikkerhedsdata fra mennesker til Grapiprant er ikke tilgængelige i denne Bevissamling, da lægemidlet ikke er blevet evalueret i humane kliniske registreringsprogrammer. Der blev ikke hentet data om lægemiddel-lægemiddel-interaktioner. Der er ingen registrerede kontraindikationer eller vigtige advarsler til humant brug i det aktuelle datasæt.

Se venligst den veterinære Oversigt over Produktegenskaber (SmPC) for Galliprant som den nærmeste tilgængelige reference, og bemærk, at ekstrapolation til humant brug medfører væsentlige usikkerhedsfaktorer.

To mekanistisk-afledte sikkerhedssignaler fortjener proaktiv opmærksomhed:

- **Protrombotisk potentiale**: PGE2–EP4-signalering bidrager til vasodilatation og endotelial anti-trombotisk beskyttelse. EP4-blokering kan skifte hæmostatisk balance mod en prokoagulant tilstand, hvilket er særligt relevant, givet at to af de øvrige toprangerede TxGNN-forudsigelser involverer koagulationsforstyrrelser (heparin-cofaktor-2-mangel, antithrombin-mangel type 2), hvor EP4-antagonisme er mekanistisk kontraindiceret.
- **Reproduktive effekter**: Som nævnt ovenfor kan EP4-blokering forstyrre ovulation — relevant for alle kvindelige patienter i reproduktiv alder.

---

## Konklusion og Næste Trin

**Beslutning: Afvent**

**Begrundelse:**
Dette kandidatlægemiddel er et veterinær-udelukkende lægemiddel uden humanklinikal data, ingen registrerede forsøg, ingen understøttende litteratur og en mekanistisk hypotese, der peger i den modsatte retning af det terapeutiske mål for den topforudsagte indikation. TxGNN-scoren afspejler en statistisk association i videngrafen, ikke klinisk gennemførbarhed. At gå videre til nogen humanevalueringsfase ville kræve løsning af fundamentale mekanistiske og regulatoriske barrierer.

**Før denne kandidat kan blive genovervejet, er følgende nødvendig:**

- **Vurdering af regulatorisk vej**: Præciser, om genbrug af et veterinær-udelukkende EP4-antagonist til humant brug er levedygtigt under EMA/Lægemiddelstyrelsen-rammer, og hvilken preklinisk pakke, der ville være påkrævet
- **Mekanistisk afklaring**: Bestem, om der eksisterer en sygdomssubtype af amenorrhea, hvor EP4-*overaktivering* er den patologiske drivkraft (hvilket ville justere mekanismen); hvis ingen sådan subtype identificeres, bør denne indikation nedprioriteres
- **Humane sikkerhedsdata**: Et fase 1 første-menneskes sikkerhedsstudie ville være en forudsætning for enhver effektivitetsvurdering; der eksisterer i øjeblikket ingen human farmakokinetik, tolerabilitet eller sikkerhedsprofil
- **MOA-dokumentation**: Indhent fulde DrugBank-farmakologidata (DG002) for at gennemføre den mekanistiske analyse
- **Alternative indikationsvurdering**: De øvrige toprangerede forudsigelser (infektiøs bovint rhinotracheitis, ondartede katarr) er veterinærsygdomme, hvilket yderligere tyder på, at dette TxGNN-kørt kunne drage fordel af et menneskelig-sygdomsfiltreret forudsigelsessæt før klinisk prioritering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

