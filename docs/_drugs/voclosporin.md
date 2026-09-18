---
layout: default
title: Voclosporin
parent: Kun modelforudsigelse (L5)
nav_order: 473
evidence_level: L5
indication_count: 10
---

# Voclosporin
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

# Voclosporin: Fra immunosuppressiv terapi til primær frigivelsesforstyrrelse af blodplader

## Sammenfatning i én sætning

> Voclosporin er en calcineurin-inhibitor immunsuppressivum (klassekammerat af cyclosporin og tacrolimus); ingen specifik oprindeligt godkendt indikation er dokumenteret i denne evidenspakke, og lægemidlet er **ikke i øjeblikket markedsført i Danmark**.
> TxGNN-modellens højest rangerede forudsigelse forbinder det til **primær frigivelsesforstyrrelse af blodplader**, med en **95,4% forudsigelsesscore**, men **nul understøttende kliniske forsøg og nul litteratur**, og modellens egen mekanistiske begrundelse fastslår, at dette link er biologisk implausibelt.

---

## Hurtigt overblik

| Emne | Indhold |
|------|--------|
| Oprindelig indikation | Ikke dokumenteret i denne evidenspakke (ingen `original_indications` på fil; lægemidlet er endnu ikke markedsført i Danmark) |
| Forudsagt ny indikation | Primær frigivelsesforstyrrelse af blodplader |
| TxGNN forudsigelsesscore | 95.42% |
| Evidensniveau | L5 |
| Status på dansk marked | Ikke markedsført |
| Antal markedsføringsgodkendelser | 0 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede mekanisme-for-handling-data for voclosporin er ikke tilgængelige på lægemiddelniveau i denne evidenspakke (`original_moa: [Data Gap]`). Dog indikerer litteratur- og begrundelsesindgange knyttet til andre kandidatindikatorer i denne samme pakke, at voclosporin tilhører **calcineurin-inhibitor (CNI)**-klassen sammen med cyclosporin og tacrolimus. Ifølge en review fanget i denne pakke (PMID 41361657) virker CNI'er ved at inhibere det calciumafhængige phosphatase calcineurin, blokere defosforylering/kernestranslokation af NFAT og undertrykkelse af IL-2-transkription — og derved svækker T-celle-aktivering. Dette er standard immunsuppressiv farmakologi, ikke en valideret oprindelig indikation for voclosporin specifikt.

For modellens højest rangerede forudsigelse — **primær frigivelsesforstyrrelse af blodplader** — er evidenspakkens egen mekanistiske vurdering eksplicit negativ: dette er en **arvelig defekt i blodpladeernes tætgranula-sekretion**, en strukturel/genetisk blodpladestyrrelse med patofysiologi uden relation til T-celle-aktivering eller calcineurin-stien. Pakken fastslår klart, at der "目前無任何臨床或文獻證據支持" (ikke er nogen klinisk eller litteraturmæssig evidens, der understøtter dette), og klassificerer associationen som en udelukkende-forudsigelse-artefakt, der "未達可驗證假說門檻" (ikke har nået tærskelværdien for en testbar hypotese).

Kort sagt: TxGNN-similaritetsscore (95.4%) er høj, men den medfølgende begrundelse — genereret fra samme evidenspakke — understøtter ikke en plausibel biologisk mekanisme. En høj embedding-similaritetsscore uden mekanistisk eller empirisk støtte bør fortolkes forsigtigt; det kan afspejle grafklynge-effekter blandt blodpladerelaterede sygdomsknuder snarere end et autentisk farmakologisk forhold.

---

## Evidens fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Oplysninger om dansk marked

Voclosporin har i øjeblikket **ingen markedsføringsgodkendelse på fil i Danmark** (`market_status`: Not marketed; `total_licenses`: 0). Ingen Lægemiddelstyrelsen national godkendelse eller EMA centraliseret godkendelsesrecord er til stede i denne evidenspakke.

---

## Sikkerhedsovervejelser

Se venligst den godkendte produktinformationssamling (SmPC) for sikkerhedsinformation.

*(Bemærk: denne evidenspakkes eget data-gap-log markerer de manglende etiketterings-/advarselsdata — punkt DG001, "Lægemiddelstyrelsen pakkeindlæg advarsler/kontraindikationer" — som et **blokerende** alvorligheds-gap, hvilket betyder, at denne kandidat endnu ikke kan fortsætte til sikkerhedsgennemgangsstadiet (S1), før etikettingsdata er hentet.)*

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
- Evidensniveauet er **L5** — udelukkende modelforudsigelse, uden kliniske forsøg, uden litteratur og uden observationsdata, der understøtter en forbindelse mellem voclosporin og primær frigivelsesforstyrrelse af blodplader.
- Evidenspakkens egen mekanistiske begrundelse modsiger eksplicit biologisk plausibilitet: defekter i blodpladeernes tætgranula-sekretion er ikke kendt for at involvere calcineurin/T-celle-aktiverings-stien, som voclosporin sigter mod.
- To data-gaps blokerer yderligere progression: **DG001** (danske/EU SmPC advarsler og kontraindikationer — blokerende, forhindrer adgang til sikkerhedsgennemgangsstadium S1) og **DG002** (bekræftet virkningsmekanisme — høj, nødvendig for mekanistisk validering).

**For at kunne fortsætte er følgende nødvendigt:**
- Hent den godkendte SmPC (dansk/EU-etiket) for voclosporin for at løse DG001, før nogen sikkerhedsgennemgang kan begynde
- Bekræft virkningsmekanisme via DrugBank eller primære farmakologikilder for at løse DG002
- Enhver præklinisk eller mekanistisk litteratur, der direkte forbinder calcineurin-inhibering til frigivelse af blodpladeernes tætgranula, ville være påkrævet før denne kandidat kunne bevæge sig ud over Hold
- **Til overvejelse**: denne samme evidenspakke indeholder en lavere rangeret, men bedre understøttet kandidat — **dermatitis** (TxGNN-score 94.2%, evidensniveau L3, beslutningsstadium S1 "Research Question") — understøttet af 2 litteraturreviews (PMID 37307993, PMID 41361657), der diskuterer off-label dermatologisk brug af systemiske calcineurin-inhibitorer, herunder voclosporin. Denne kandidat har en kohærent class-effect mekanistisk begrundelse og kan være værd at følge op på som prioritet foran den højest rangerede, men mekanistisk usupported blodpladestyrrelse-forudsigelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

