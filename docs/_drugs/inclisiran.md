---
layout: default
title: Inclisiran
parent: Kun modelforudsigelse (L5)
nav_order: 230
evidence_level: L5
indication_count: 10
---

# Inclisiran
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

# Inclisiran: Fra PCSK9-målrettet lipidterapi til kaliummangelsygdom

## Resumé i en sætning

Inclisiran er en lille interfererende RNA (siRNA), der dæmper PCSK9 mRNA i hepatocytter; den specifikke oprindelige indikationstekst er ikke tilgængelig i denne bevisemappe. TxGNN-modellen forudsiger en mulig forbindelse til **kaliummangelsygdom** med en meget høj tillidsværdi, men **ingen kliniske forsøg og ingen litteratur** understøtter i øjeblikket denne retning, og bevisemappens egen mekanistiske gennemgang markerer forudsigelsen som sandsynligvis en **falsk positiv**.

---

## Hurtigt overblik

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Ikke dokumenteret i bevisemappe (ingen `original_indications` eller `original_moa` data tilgængelige; DrugBank-post eksisterer, men MOA-felt er en datamangel) |
| Forudsagt ny indikation | Kaliummangelsygdom |
| TxGNN forudsigelsesscore | 99.93% |
| Bevisniveau | L5 (kun modelforudsigelse — ingen kliniske forsøg eller litteratur identificeret) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Vent |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme for Inclisiran ikke tilgængelige som et struktureret felt i denne bevisemappe. Teksten med begrundelse for genbrug forbundet med denne forudsigelse identificerer dog Inclisiran som en siRNA, der målrettes PCSK9 mRNA, og som virker på hepatisk lipoproteinstofskifte.

Baseret på denne mekanistiske beskrivelse konkluderer bevisemappens egen analyse, at der er **ingen kendt overlapning** mellem PCSK9/hepatisk lipoproteinvejen og kalium-homeostase (nyrens håndtering, aldosteronakse eller kaliumtransportører). Der blev ikke fundet litteratur, der understøtter en forbindelse mellem PCSK9-inhibering og nyre-tubulær kaliumregulering. Begrundelsen karakteriserer dette eksplicit som **"en høj-score forudsigelse uden mekanistisk forbindelse — en sandsynlig falsk positiv."**

Denne vurdering forstærkes af mønsteret på tværs af alle toprangerede forudsigelser i denne bevisemappe: spiserørssygdom, ikke-syndromisk spiserørsmisdannelse, atypisk aortakoarktation og migræne er også rangeret med meget høje TxGNN-score (99.8–99.9%), men hver enkelt bærer samme mekanistiske ansvarsfraskrivelse — ingen plausibel biologisk vej, der forbinder PCSK9-medieret lipidstofskifte til disse tilstande, og ingen understøttende forsøg eller publikationer for nogen af dem. Dette antyder, at de høje TxGNN-score i dette kandidatset kan afspejle en systematisk scoringsartefakt snarere end ægte biologisk signal, og hver kandidat bør fortolkes med forsigtighed.

---

## Klinisk forsøgsbeviser

I øjeblikket er der ingen relaterede kliniske forsøg registreret.

---

## Litteraturbeviser

I øjeblikket er der ingen relateret litteratur tilgængelig.

---

## Markedsinformation Danmark

Der er i øjeblikket ingen markedsføringstilladelser registreret for Inclisiran i Danmark (markedsstatus: **Ikke markedsført**, 0 licenser på fil).

---

## Sikkerhedshensyn

Se venligst det godkendte produktsammenfattende karakteristika (SmPC) for sikkerhedsinformation.

*Bemærk: Der eksisterer en kritisk datamangel — Lægemiddelstyrelses label-advarsler/kontraindikationer er endnu ikke hentet, hvilket forhindrer denne kandidat i at indgå i sikkerhedsscreening (S1).*

---

## Konklusion og næste trin

**Afgørelse: Vent**

**Begrundelse:**
- Bevisniveauet er L5 — forudsigelsen hviler helt på TxGNN-modelscoret, uden nogen bekræftende kliniske forsøg eller litteratur.
- Bevisemappens egen mekanistiske begrundelse argumenterer **mod** biologisk plausibilitet, eksplicit markeret som en sandsynlig falsk positiv, og samme mønster gentages på tværs af alle andre toprangerede kandidater for dette lægemiddel.
- En kritisk datamangel (SmPC-advarsler/kontraindikationer) betyder, at denne kandidat endnu ikke kan indgå i sikkerhedsscreening (S1) uanset forudsagt-indikationsstyrke.

**For at kunne gå videre er følgende nødvendigt:**
- Hent Lægemiddelstyrelses label-advarsler og kontraindikationer (kritisk datamangel, DG001)
- Hent verificeret virkningsmekanismedata fra DrugBank (DG002)
- Bekræft lægemidlets faktiske oprindelige indikation(er), som i øjeblikket mangler fra denne bevisemappe
- Uafhængig mekanistisk eller præ-klinisk beviser, der specifikt forbinder PCSK9 mRNA-dæmpning til kalium-homeostase, før yderligere investering i denne kandidat
- I betragtning af den konsistente mangel på mekanistisk understøttelse på tværs af dette lægemiddels fulde kandidatliste, overvej at re-evaluere TxGNN-scoreoutputtet for dette lægemiddel som mulig systematisk scoringsartefakt snarere end at evaluere hver kandidat enkeltvis

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

