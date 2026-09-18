---
layout: default
title: Migalastat
parent: Kun modelforudsigelse (L5)
nav_order: 291
evidence_level: L5
indication_count: 10
---

# Migalastat
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

# Migalastat: Fra Fabry-sygdom til Idiopatisk Kobberassocieret Cirrhose

## Sammenfattelse i én sætning

Migalastat (Galafold) er et oralt farmakologisk chaperone godkendt til Fabry-sygdom — en sjælden lysosomål lagringssygdom forårsaget af mutationer i *GLA*-genet, der koder for alfa-galaktosidase A.
TxGNN-modellen forudsiger, at det kan være effektivt til **Idiopatisk Kobberassocieret Cirrhose**, med en forudsigelsesscore på **98.85%**.
Der er dog **ingen kliniske forsøg og ingen publiceret litteratur**, der i øjeblikket understøtter denne retning, og mekanistisk analyse tyder på, at forbindelsen er meget svag.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Fabry-sygdom (alfa-galaktosidase A-mangel, GLA-modtagelige mutationer) |
| Forudsagt ny indikation | Idiopatisk kobberassocieret cirrhose |
| TxGNN-forudsigelsesscore | 98.85% |
| Bevisniveau | L5 |
| Status på dansk marked | Ikke markedsført |
| Antal markeringsgodkendelser | 0 |
| Anbefalet beslutning | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er der ikke detaljerede data om virkningsmekanisme tilgængelige i denne bevispaket. Baseret på kendt information er Migalastat et oralt farmakologisk chaperone, der selektivt binder til og stabiliserer forkert foldet alfa-galaktosidase A (GLA) hos patienter med modtagelige *GLA*-mutationer. Ved at gendanne korrekt lysosomalt transport af GLA reduceres den patologiske ophobning af globotriaosylceramid (Gb3) og relaterede glykosfingolipider i vaskulær endotel, kardiomyocytter og podocytter — det karakteristiske læsion ved Fabry-sygdom.

Den forudsagte indikation, idiopatisk kobberassocieret cirrhose, omfatter en fundamentalt forskellig metabolisk vej. Kobber-homeostase reguleres primært af ATP7B (Wilson-sygdoms kobberforter) og relaterede proteiner såsom COMMD1 og ATOX1; ingen af disse skærer direkte ind i GLA/Gb3 lysosomale stof. Selvom lysosomalt dysfunktion teoretisk kan påvirke intracellulær metaludveksling gennem LAMP2-relaterede mekanismer, er der ingen publiceret evidens for, at Migalastat udøver nogen effekt på kobbermetabolisme eller hepatisk kobberakumulering.

Den mest sandsynlige forklaring på den høje TxGNN-score er en **graftclusteringartefakt**: TxGNN-vidensgrafen har muligvis grupperet "hepatisk lysosomål lagringssygdom" som en delt hub-knude, hvilket får Migalastat til at score højt mod kobberrelaterede leversygdomme på trods af, at der ikke er nogen biologisk plausibel behandlingsbegrundelse. Alle fem unikke forudsagte indikationer i denne paket deler samme score (98.85%) og samme bevisudgangspunkt (nul forsøg, nul publikationer), hvilket yderligere understøtter denne fortolkning af systematisk overprognoser i grafen for sjælden leversygdom.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for nogen af de forudsagte indikationer.

---

## Litteraturevidence

Der er i øjeblikket ingen relateret litteratur tilgængelig for nogen af de forudsagte indikationer.

---

## Oplysninger om dansk marked

Migalastat (Galafold) har i øjeblikket **ingen nationale markeringsgodkendelser** registreret i Lægemiddelstyrelsens database, og lægemidlet er opført som ikke markedsført i Danmark på tidspunktet for denne rapport (datakutoff: 2026-04-04).

> **Bemærk for anmeldere:** Galafold modtog en centraliseret markeringsgodkendelse fra Det Europæiske Lægemiddelagentur (EU/1/16/1085) til Fabry-sygdom i maj 2016. Hvis denne EMA-godkendelse ikke afspejles i kildedata, bør den regulatoriske status verificeres direkte via siden for [EMA-produkter](https://www.ema.europa.eu/en/medicines/human/EPAR/galafold) og [Lægemiddelstyrelsens produktdatabase](https://produktresume.dk/), før der drages konklusioner om tilgængelighed på det danske marked.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresuméet (SmPC) for sikkerhedsinformation.

> Sikkerhedsdata — herunder vigtige advarsler, kontraindikationer og lægmiddel-lægmiddel interaktioner — var ikke tilgængelige i denne bevispaket og blev ikke hentet fra TFDA/DrugBank-kilder på tidspunktet for dataindsamling (2026-03-24). Før eventuel klinisk brug skal du konsultere det aktuelle Galafold-produktresuméet, der er tilgængeligt gennem EMA eller den nationale lægemiddelstyrelse.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
TxGNN-modellen tildeler en høj score (98.85%) til alle forudsagte indikationer, men dette ser ud til at afspejle en grafclusteringartefakt snarere end ægte farmakologisk plausibilitet. Der er ingen evidens fra kliniske forsøg, ingen understøttende litteratur, ingen etableret mekanistisk forbindelse mellem GLA-målrettet farmakologisk chaperoning og kobbermetabolisme eller hepatisk vaskulær patologi, og Migalastat har ingen nuværende markeringsgodkendelse registreret i Danmark. Med et L5-bevisniveau og en svag mekanistisk begrundelse på tværs af alle fem forudsagte sygdomsomfang er det ikke begrundet at fremme denne kandidat på dette stadium.

**For at gå videre er følgende nødvendigt:**

- **Mekanistisk data**: Hent og gennemgå fuldt Migalastat MOA fra DrugBank (DB05018) og primær litteratur for formelt at udelukke enhver indirekte kobberbehandlings- eller lysosomalt-hepatisk forbindelse.
- **Regulatorisk præcisering**: Bekræft, om den centraliserede EMA-godkendelse (EU/1/16/1085) er aktiv og gyldig for Danmark, og indhent det aktuelle produktresuméet med fulde sikkerhedsdata.
- **TxGNN-modelrevision**: Undersøg, hvorfor alle top-10-prognoser deler en identisk score (0.9885) og kortlægges til sjælden hepatiske tilstande. Dette afspejler sandsynligvis en undergrafs-niveau bias og bør markeres for modelmaintenance-teamet til omkalibrering.
- **Bredere indikationssøgning**: Revurder Migalastat-kandidater uden for det hepatiske sjælden-sygdoms undergraff — for eksempel Fabry-tilstødende indikationer (nefropati, kardiomyopati, cerebrovaskulær sygdom), hvor GLA/Gb3-forbindelsen er velestableret, og klinisk forsøgsevidence kan eksistere.
- **Sikkerhedsvurdering**: Udfyld det blokerende datahul (DG001) ved at downloade og analysere produktresumeet/receptinformationen fra EMA eller en reference regulatorisk myndighed, før eventuel sikkerhedsvurdering af ompurposering kan fortsætte.

---

*Denne rapport er kun til forskningsmæssige formål og udgør ikke medicinsk rådgivning. Alle omjusterede lægemiddelkandidater kræver klinisk validering før terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

