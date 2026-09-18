---
layout: default
title: Firocoxib
parent: Kun modelforudsigelse (L5)
nav_order: 191
evidence_level: L5
indication_count: 0
---

# Firocoxib
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

# Firocoxib: Veterinær COX-2-hæmmer — Ingen prognose for genvending tilgængelig

## Resumé på en sætning

Firocoxib (DrugBank DB09217) er en COX-2-selektiv NSAID godkendt til veterinær brug (hos hunde og heste) til smertelindring og inflammationskontrol. TxGNN-modellen returnerede **ingen forudsagte nye indikationer** for denne forbindelse, sandsynligvis på grund af utilstrækkelige data om humane lægemidler i vidensgrafen. Med nul danske markedstilladelser, kritiske datakløfter inden for virkningsmekanisme- og sikkerhedsinformation samt intet understøttende bevis, kan en fuldstændig genvendingsevaluering ikke gennemføres på nuværende tidspunkt.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Veterinær brug — osteoarthritis og smertelindring hos hunde (Previcox) og heste (Equioxx) |
| Forudsagt ny indikation | Ingen prognose genereret af TxGNN |
| TxGNN-prognosescore | Ikke tilgængelig |
| Bevisniveau | L5 (kun modelprognose — ikke engang relevant; ingen prognose returneret) |
| Dansk markedsstatus | Ikke markedsført |
| Antal markedstilladelser | 0 |
| Anbefalet afgørelse | Afvent |

---

## Hvorfor er denne prognose rimelig?

Ingen TxGNN-prognose blev genereret for Firocoxib. Dette skyldes sandsynligvis, at forbindelsen er klassificeret som et veterinært lægemiddel og er fraværende fra de menneskelige lægemiddelknuder i TxGNN-vidensgrafen, som hovedsageligt er trænet på data fra humane lægemidler.

Mekanistiske data (virkningsmekanisme) er i øjeblikket ikke tilgængelige i bevissamlingen. Baseret på farmakologisk klasse tilhører Firocoxib COX-2-selektiv NSAID-familien — den samme klasse som celecoxib og etoricoxib — og udøver sin virkning ved selektivt at hæmme cyclooxygenase-2, hvilket reducerer prostaglandinsyntese og inflammation. Principielt er COX-2-hæmning blevet udforsket inden for humane onkologi (kemoprævention af kolorektal cancer) og kroniske inflammatoriske sygdomme. Adaptationen af et veterinært lægemiddel til human genvendingesstrategi kræver imidlertid dedikerede sikkerhedsfarmakologiske og toksikologistudier, som ikke er blevet identificeret.

Uden en TxGNN-prognose til at ankre denne evaluering, og uden menneskelig klinisk erfaring eller virkningsmekanisme-dokumentation i den aktuelle bevissamling, kan mekanistisk rationalet ikke formelt vurderes på nuværende tidspunkt.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relevante registrerede kliniske forsøg.

---

## Litteraturbevis

Der er i øjeblikket ingen relevant litteratur tilgængelig.

---

## Danske markedsoplysninger

Firocoxib har ingen markedstilladelser i Danmark (hverken nationale Lægemiddelstyrelsen-tilladelser eller centraliserede EMA-tilladelser). Forbindelsen er ikke godkendt til human brug i nogen EU-medlemsstat.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation. Bemærk, at det eksisterende produktresumé (SmPC) kun dækker veterinær brug; menneskelige sikkerhedsdata skulle genereres de novo, før nogen klinisk udvikling kunne foregå.

---

## Konklusion og næste trin

**Afgørelse: Afvent**

**Begrundelse:**
Firocoxib er en udelukkende veterinær forbindelse uden danske markedstilladelser, ingen TxGNN-forudsagt menneskelig indikation, og kritiske datakløfter både i virkningsmekanisme-dokumentation og menneskelig sikkerhedsprofil. Der er i øjeblikket intet bevisgrundlag til at støtte en genvendingshypotese for humane lægemidler.

**For at komme videre er følgende påkrævet:**

- **TxGNN-genforsøg**: Bekræft, om Firocoxib er til stede i TxGNN-vidensgrafen som en lægemiddelknude; hvis den er fraværende, overvej at tilføje den via DrugBank-til-KG-mapping før genkørsel af prognosepipeline'en
- **Virkningsmekanisme-dokumentation**: Hent fuld virkningsmekanisme fra DrugBank API (afhjælpning noteret i DG002) for at muliggøre mekanistisk plausibilitetanalyse
- **Menneskelige sikkerhedsdata**: Foretag en systematisk litteraturgennemgang for eventuelle rapporter om human farmakokinetik, toksikologi eller off-label-brug
- **Gennemgang af regulatorisk landskab**: Tjek EMA-, FDA- og PMDA-databaser for eventuelle ventende eller historiske ansøgninger om human-brug
- **Generering af indikationshypotese**: Hvis et humant sygdomsmål foreslås, foretag manuel litteraturudvinding (PubMed, ICTRP) for at vurdere, om der kan etableres et genvendingsrationalet uafhængigt af TxGNN-resultat

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

