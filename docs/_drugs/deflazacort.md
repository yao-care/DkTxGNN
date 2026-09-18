---
layout: default
title: Deflazacort
parent: Kun modelforudsigelse (L5)
nav_order: 134
evidence_level: L5
indication_count: 0
---

# Deflazacort
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

# Deflazacort: Vurdering af lægemiddelrepurposing – Ingen TxGNN-forudsigelser tilgængelige

---

## Ét-sætnings-resumé

Deflazacort (DrugBank ID: DB11921) er en oxazolin-afledt glukokortikoid godkendt i USA til Duchenne Muskeldystrofi (DMD) og bruges i flere lande til en række inflammatoriske og immunvermittede tilstande.
Denne evidenspakke indeholder **ingen TxGNN-forudsagte nye indikationer** for dette lægemiddel, og kritiske datahuller — herunder detaljer om virkningsmekanisme og dansk regulatorisk sikkerhedsinformation — forhindrer en fuldstændig vurdering af repurposing på dette stadium.
En **Hold**-beslutning anbefales, indtil de manglende data er indsamlet, og TxGNN-forudsigelser er genereret.

---

## Hurtigt overblik

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Ingen godkendte indikationer registreret i denne evidenspakke (lægemiddel ikke registreret i Danmark; USA-indikation: Duchenne Muskeldystrofi) |
| Forudsagt ny indikation | Ingen forudsigelser genereret |
| TxGNN-forudsigelsesscore | Ikke tilgængelig |
| Evidensniveau | L5 – Ingen forudsigelser eller understøttende studier returneret af denne pipeline-kørsel |
| Danmarks markedsstatus | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | **Hold** |

---

## Hvorfor der ikke er forudsigelser tilgængelige

TxGNN-forudsigelsespipelinen returnerede en tom kandidatliste (`predicted_indications: []`) for dette lægemiddel. Dette er et atypisk resultat, der kan opstå fra en eller flere af følgende årsager:

1. **Videnskabsgrafdækning**: DrugBank ID DB11921 kan endnu ikke være linket til sygdomsknuderne i TxGNN-vidensgrafen, hvilket resulterer i, at ingen scorede lægemiddel-sygdomspar udsendes.
2. **Scoretrærfiltrering**: Forudsigelsesscores for alle kandidatindikationer kan være faldet under det konfidensinterval, der blev anvendt under efterbehandling.
3. **Pipelinestatus**: Forudsigelseskørslen kan have været ufuldstændig på det tidspunkt, hvor denne evidenspakke blev genereret (dataskæringsdato: 2026-04-05).

Fordi der ikke blev hentet mekanistiske data (MOA) — markeret som en **høj-alvorlig** datakløft — kan en narrativ forklaring på, hvorfor en forudsagt indikation kan være farmakologisk rimelig, ikke gives på dette stadium.

---

## Danmarks markedsinformation

Deflazacort har i øjeblikket **ingen markedsføringstilladelser** i Danmark (Lægemiddelstyrelsen) og er ikke anført som et markedsført produkt. Der er ingen nationale eller EMA-centraliserede autorisationsregistre i denne evidenspakke.

> **Bemærkning til revisorer:** Deflazacort er kommercielt tilgængeligt i andre jurisdiktioner under mærkenavnet **Emflaza** (USA-FDA godkendt, 2017, til DMD hos patienter i alderen ≥ 5 år). Et EMA/centraliseret markedsføringsgodkendelsessøg bør udføres for at bekræfte, hvorvidt der eksisterer en paneuropæisk status.

---

## Sikkerhedsmæssige overvejelser

Venligst se det godkendte produktresumé (SmPC) for fuld sikkerhedsinformation. Ingen lokale sikkerhedsdata kunne ekstraheres fra denne evidenspakke på grund af følgende blokerende datahuller:

| Datakløft-ID | Punkt | Alvorlighed | Påvirkning |
|--------------|-------|-------------|-----------|
| DG001 | SmPC-advarsler og kontraindikationer | **Blokerende** | Kan ikke fuldføre S1 sikkerhedsforkontrol |
| DG002 | Virkningsmekanisme (MOA) | **Høj** | Kan ikke udføre mekanistisk relevansanalyse |

---

## Konklusion og næste trin

**Beslutning: Hold**

**Begrundelse:**
Denne vurdering kan ikke rykke frem til vurderingsstadiet for repurposing, fordi TxGNN-modellen returnerede ingen forudsagte indikationer for Deflazacort, og to uløste datahuller forhindrer både sikkerhedskontrol og mekanistisk analyse. At fortsætte uden disse input ville ikke opfylde minimumsevidentærsklen for en meningsfuld repurposing-anbefaling.

**For at fortsætte er følgende nødvendigt:**

- **Kør TxGNN-forudsigelsespipelinen igen** for DrugBank ID DB11921 og bekræft, at lægemiddelknuden er korrekt repræsenteret i vidensgrafen (bekræft nodeposition i `data/node.csv`)
- **Indhent MOA-data** via DrugBank API-forespørgsel for DB11921 (Datakløft DG002 – Høj alvorlighed)
- **Download og parse SmPC / produktmonografi** for at ekstrahere godkendte advarsler, kontraindikationer og lægemiddelinteraktioner (Datakløft DG001 – Blokerende alvorlighed); kilde: EMA-produktside eller USA FDA-label for Emflaza
- **Bekræft EMA/centraliseret autorisationsstatus** for at bestemme, hvorvidt Deflazacort har nogle EU-brede markedsføringstilladelser, der kan være relevante i Danmark
- **Gennemgå danske særlige adgangsformer** (f.eks. navngivet patient eller barmhjertighedsbrug) i betragtning af, at Deflazacort er godkendt i USA til en sjælden sygdom (DMD) med uopfyldt behov

---

> *Denne rapport er genereret til forskningsreferencebrug alene og udgør ikke medicinsk rådgivning. Alle lægemiddelrepurposing-kandidater kræver klinisk validering før enhver terapeutisk anvendelse.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

