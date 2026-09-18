---
layout: default
title: Amphotericin B
parent: Kun modelforudsigelse (L5)
nav_order: 35
evidence_level: L5
indication_count: 0
---

# Amphotericin B
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

# Amphotericin B: Evaluering af genfinding af lægemiddel — Ingen TxGNN-prognoser genereret

---

## Sammenfatning i en sætning

Amphotericin B er et velkendt polyenantimykotikum, der bruges til alvorlige invasive svampeinfektioner. **Ingen TxGNN-genfindingsprognoser blev genereret** for dette lægemiddel i den aktuelle evalueringscyklus, da kritiske datahuller i pipelinen forhindrede prognosegenerering. Denne rapport dokumenterer den nuværende datastatus og skitserer de afhjælpningstrin, der kræves, før en formel evalueringsprocedure kan fortsætte.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Alvorlige invasive svampeinfektioner *(baseret på etableret farmaceutisk viden; ingen licensdata hentet fra Laegemiddelstyrelsen)* |
| Forudsagt ny indikation | Ikke tilgængelig — ingen TxGNN-prognoser genereret |
| TxGNN-prognosescore | Ikke tilgængelig |
| Evidensniveau | Ikke vurderbart |
| Markedsstatus i Danmark | Ikke markedsført *(jf. bevissamling — se vigtig bemærkning herunder)* |
| Antal markedsføringstilladelser | 0 *(jf. bevissamling)* |
| Anbefalet beslutning | **Afvent** |

> **⚠️ Vigtig bemærkning om markedsstatus i Danmark:** Bevissamlingen registrerer nul danske markedsføringstilladelser. Imidlertid har liposomal amphotericin B (AmBisome®) en gyldig centraliseret EMA-markedsføringstilladelse (EU/1/97/049), som direkte gælder for Danmark, og konventionelle amphotericin B-deoxycholat-produkter har historisk været tilgængelige via hospitalsindkøb. Resultatet med nul-licens afspejler næsten helt sikkert et **databehandlingshul** snarere end den faktiske reguleringsmæssige situation og skal verificeres mod Laegemiddelstyelsens produktdatabase, før der drages reguleringsmæssige konklusioner.

---

## Hvorfor er denne prognose rimelig?

Da der ikke blev genereret nogen TxGNN-prognose i denne evalueringscyklus, kan dette afsnit ikke udfyldes i standardsammenligningsformatet. Manglen på prognoser er et pipelineproblem, ikke en afspejling af lægemidlets genfindingspotentiale.

For kontekst: Amphotericin B (DrugBank ID: DB00681) er et polyenmakrolidantibiotikum, der først blev isoleret fra *Streptomyces nodosus* i 1950'erne. Detaljerede virkningsmekanisme-data blev ikke hentet i denne evalueringscyklus. På grundlag af etableret farmakologisk viden virker Amphotericin B ved selektivt at binde sig til ergosterol i svampecellemembranen, indsætte sig i lipiddobeltlaget og danne transmembrane porer. Dette forårsager irreversibel lækkage af intracellulære ioner og metabolitter, hvilket fører til osmotisk ustabilitet og cellødød. Dets selektivitet for ergosterol frem for pattedyrkolesterol ligger til grund for dets kliniske nytte.

Anerkendte områder af potentiel genfinding diskuteret i det videnskabelige litteratur — herunder antileishmaniel aktivitet (visceral leishmaniasis, allerede en godkendt indikation for liposomalformen), antivirale anvendelser og immunmodulatoriske effekter i onkologiske indstillinger — kan ikke formelt rangeres eller evalueres uden TxGNN-prognoseoutput. Genindkørsel af prognose-pipelinen med korrigerede inputdata er det nødvendige første trin.

---

## Sikkerhedsovervejelser

Sikkerhedsdata (vigtige advarsler og kontraindikationer) blev ikke hentet fra Laegemiddelstyrelsen i denne evalueringscyklus. På grundlag af etableret klinisk sikkerhedsprofil for Amphotericin B:

- **Nefrotoksicitet**: Dosisafhængig nyresvækkelse er den primære dosisgrænsende toksicitet for den konventionelle deoxycholatformulering. Liposomale formuleringer (f.eks. AmBisome®) reducerer nefrotoksisk risiko væsentligt. Baseline og regelmæssig overvågning af serum-kreatinin, urinstof og elektrolytter er vigtig.
- **Infusionsrelaterede reaktioner**: Feber, rysteture, kulderystelser, lavt blodtryk og bronkospasme kan forekomme under intravenøs administration; premedicinering er standard praksis.
- **Elektrolytforstyrrelser**: Hypokaliæmi og hypomagnesæmi er almindeligt og kræver overvågning og supplementering.
- **Hæmatologiske effekter**: Normokrom normocytær anæmi kan udvikle sig ved længerevarende behandling.

Venligst se det godkendte Produktresumé (SmPC) — tilgængeligt via European Medicines Agency (EMA) produktside for AmBisome® — for fuldstændig og autoritative sikkerhedsinformationer, herunder alle kontraindikationer og lægemiddelinteraktionsdata.

---

## Konklusion og næste trin

**Beslutning: Afvent**

**Begrundelse:**
TxGNN-prognose-pipelinen producerede ingen genfindingskandidater for Amphotericin B, og to uløste datahuller — en klassificeret som Blokerende, én som Høj alvor — forhindrer evalueringen i at skride til indledende sikkerhedsscreening eller klinisk evidensgennemgang. Ingen meningsfuld genfindingsanbefaling kan afgives på dette trin.

**For at fortsætte er følgende nødvendigt:**

1. **[Blokerende]** Løs fejl ved hentning af licensdata fra Laegemiddelstyelsen og genfyld `taiwan_regulatory` med korrekte danske autorisationsregistre, herunder EMA's centraliserede autorisation for AmBisome® (EU/1/97/049)
2. **[Blokerende]** Genindkør TxGNN-prognose-pipelinen når inputdata er korrigeret, for at generere rangerede genfindingskandidater med tillidsscores
3. **[Høj]** Hent Virkningsmekanisme (MOA) data via DrugBank API for DrugBank ID DB00681 for at understøtte analyse af mekanistisk plausibilitet
4. **[Høj]** Download og parse det aktuelle Produktresumé (via EMA eller Laegemiddelstyrelsen) for at udfylde vigtige advarsler, kontraindikationer og lægemiddelinteraktionsdata til indledende sikkerhedsscreening
5. Når prognoser er tilgængelige, genindkør den fulde evidensindsamlingspipeline (ClinicalTrials.gov, PubMed, EudraCT) for den højest rangerede forudsagte indikation

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

