---
layout: default
title: Florfenicol
parent: Kun modelforudsigelse (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Florfenicol
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

# Florfenicol: Fra veterinær bakterieinfektioner til interventrikular septum-aneurisme

## Sammenfatning i én sætning

Florfenicol er et fluorineret antibiotikum af chloramphenicol-klassen, udviklet udelukkende til veterinær brug, uden godkendte indikationer i humanmedicin.
TxGNN-modellen forudsiger, at det kan være effektivt mod **interventrikular septum-aneurisme** med en score på 94.31%;
dog **ingen kliniske forsøg og ingen publiceret litteratur** understøtter denne retning i øjeblikket, hvilket gør dette til en modelforudsigelse alene på evidensniveau L5.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Veterinær bakterieinfektioner (ikke godkendt til humanforbrug) |
| Forudsagt ny indikation | Interventrikular septum-aneurisme |
| TxGNN forudsigelsesscore | 94.31% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Afvente |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige. Baseret på kendt farmakologisk information er Florfenicol et fluorineret derivat af chloramphenicol – et bredt spektrums antibiotikum, der virker ved at hæmme bakteriel proteinsyntes (binding til det 50S ribosomalt underenhed). Det bruges i veterinærmedicin til at behandle bakterieinfektioner hos fisk, kvæg og svin, og er aldrig blevet godkendt til brug hos mennesker i nogen jurisdiktion.

Interventrikular septum-aneurisme (VSA) er en strukturel kardiel defekt – enten medfødt eller erhvervet – der involverer lokaliseret udbuling af den ventrikulære septumvæg. Der er ingen etableret mekanistisk forbindelse mellem proteinsynteteshæmning (antibiotikaets virkningsmekanisme) og kardiel strukturel reparation, ombygging eller fibroseprevention. TxGNN-modellen har sandsynligvis udledt denne association gennem indirekte vidensgrafdveje, der forbinder bakterieinfektioner med kardiel involvering (f.eks. infektiøs endokarditis → kardiel strukturskade → antibiotikabehandling), snarere end en direkte farmakologisk mekanisme.

Det skal bemærkes, at samme forudsigelsesscore (0.9431) vises duplikeret på både rang 1 og rang 2 indgange for samme sygdom, hvilket tyder på et datapipeline-problem snarere end uafhængig evidens. Mekanistisk plausibilitet for Florfenicol i nogen menneskelig kardiel tilstand er i øjeblikket ustøttet, og den veterinær-kun regulatoriske historie skaber en yderligere barriere for menneskelig repurposering.

---

## Klinisk forsøgsevidence

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidence

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

Florfenicol har ingen markedsføringstilladelser i Danmark. Lægemidlet er ikke registreret hos Lægemiddelstyrelsen og har ingen EMA centraliseret godkendelse til humanforbrug. Det er klassificeret som et veterinært lægemiddel uden for omfanget af humanfarmaceutisk regulering.

---

## Sikkerhedshensyn

Venligst se den godkendte produktinformation (SmPC) for sikkerhedsinformation.

> **Bemærk:** Ingen humanforbrug-sikkerhedsdata (advarsler, kontraindikationer eller lægemiddelinteraktioner) blev hentet for Florfenicol, i overensstemmelse med dets status som en veterinær-kun forbindelse. Enhver humanforbrug-sikkerhedsvurdering skulle konstrueres de novo fra veterinær data og chloramphenicol-klassekstrapolering, før yderligere evaluering kunne foregå.

---

## Konklusion og næste trin

**Afgørelse: Afvente**

**Begrundelse:**
Denne kandidat scorer L5 (modelforudsigelse alene) med nul understøttende kliniske forsøg eller publiceret litteratur, og lægemidlet selv har ingen humanregulatorisk historie i noget land. Den mekanistiske forbindelse mellem en bakteriel proteinsynteteshæmmer og en strukturel kardiel defekt er ikke farmakologisk understøttet, og de identiske duplikerede scores på tværs af indikationsranger tyder på et datakvalitetsproblem i det aktuelle pipelineoutput.

**For at fortsætte, ville følgende være nødvendigt:**

- **Etabler grundlæggende menneskelig farmakologi:** Florfenicol har ingen menneskelige PK/PD-data. Preclinisk toksikologi og første-menneske-data ville være påkrævet, før noget repurposering-program kunne initieres.
- **Præciser virkningsmekanismens relevans:** En troværdig mekanistisk hypotese, der forbinder chloramphenicol-klassaktivitet med interventrikular septum-patofysiologi, skal etableres (f.eks. anti-inflammatoriske eller anti-fibrotiske egenskaber påvist i kardielle vævmodeller).
- **Løs duplikerede forudsigelsesindgange:** Rang 1 og 2 er identiske; pipelinen bør deduplicere sygdomsindgange før scoring.
- **Hent fuldstændige MOA-data fra DrugBank:** DrugBank-forespørgsel blev registreret som vellykket, men MOA var ikke udfyldt i Evidence Pack – dette bør hentes for at understøtte enhver mekanistisk analyse.
- **Vurdering af regulatorisk vej:** En formel vurdering af, hvorvidt Florfenicol kunne indgå i menneskelig klinisk udvikling (f.eks. under EMA's repurposering-rammeværk) ville være påkrævet givet dets veterinær-kun-historie.
- **Ingen yderligere evidenssøgning anbefales** før den mekanistiske hypotese styrkes; yderligere databaseforespørgsler på dette tidspunkt er usandsynligt at give nye resultater.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

