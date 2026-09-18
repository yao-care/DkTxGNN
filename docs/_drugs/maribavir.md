---
layout: default
title: Maribavir
parent: Kun modelforudsigelse (L5)
nav_order: 279
evidence_level: L5
indication_count: 0
---

# Maribavir
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

# Maribavir: Vurdering af medicinsgenbrug — bevissamling ufuldstændig

## Resumé på en sætning

Maribavir (DrugBank ID: DB06234) er en første-i-klassen antivirusmiddel, kendt fra offentligt tilgængelige kilder til at målrette cytomegalovirus (CMV) UL97-kinase, godkendt i USA (Livtencity®) til post-transplantations-CMV-infektion refraktær over for tidligere terapi. Den nuværende bevissamling indeholder **ingen TxGNN-forudsagte medicinsgenbrug-indikationer**, og tre kritiske datafelter — oprindelig indikation, virkemekanisme og sikkerhedsinformation — er fraværende eller uløst. **En fuld vurdering af medicinsgenbrug kan ikke gennemføres på dette stadium** før de identificerede datakløfter er udbedret.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | Ikke registreret i bevissamlingen |
| Forudsagt ny indikation | Ingen — `predicted_indications`-array'et er tomt |
| TxGNN-forudsigelsesscore | I.v.t. |
| Bevisgrad | L5 — ingen forudsigelser tilgængelige |
| Status på det danske marked | Ikke markedsført |
| Antal markeringsgodkendelser | 0 |
| Anbefalet afgørelse | **Udsat** |

---

## Hvorfor en fuldstændig vurdering ikke kan fortsætte

Bevissamlingen indeholder to blokkerende og en alvorlig datakløft, som tilsammen forhindrer enhver vurdering af medicinsgenbrug i at blive gennemført:

**Ingen TxGNN-forudsagte indikationer (blokkerende).** `predicted_indications`-array'et er tomt. Dette er det grundlæggende input for enhver rapport om medicinsgenbrug — uden mindst én modelprognosticeret målindikation, er der ingen genbrugshypotese at evaluere, ingen bevis at vurdere og ingen go/no-go-anbefaling at give for en specifik ny brug.

**Manglende sikkerhedsdata (blokkerende).** Alle vigtige advarsler og kontraindikationer er uløst. Sikkerhedsforskal er et obligatorisk trin før enhver genbrug-udviklingsvej kan avanceres. Denne kløft alene ville forhindre rapporten i at nå en klinisk anbefaling, selv hvis forudsigelser var tilgængelige.

**Manglende virkemekanisme (alvorlig).** Mekanistisk plausibilitet er en kernestøtte i genbrug-vurdering. Uden MOA-data er det umuligt at vurdere, om Maribavir's farmakologi kan anvendes på nogen kandidatindikation.

---

## Medicinsinformationer for Danmark

Maribavir **markedsføres ikke i øjeblikket i Danmark** ifølge bevissamlingen. Der er ingen aktive markeringsgodkendelser registreret hos Lægemiddelstyrelsen eller via EMA's centraliserede procedure.

> **Vigtig verifikation nødvendig:** Maribavir (Livtencity®, Takeda) modtog EMA centraliseret markeringsgodkendelse til behandling af post-transplantations-CMV-infektion hos voksne. Hvis en gyldig EU-godkendelse eksisterer, bør den fremgå af Danmarks regulatoriske sektion. Fraværet af registreringer her skyldes sandsynligvis en datakølektgab snarere end en reel fravær af godkendelse. Dette skal verificeres direkte via [EMA's medicindatabase](https://www.ema.europa.eu/en/medicines) før enhver regulatorisk vurdering foretages.

---

## Sikkerhedsovervejelser

Alle sikkerhedsdatafelter i bevissamlingen er uløst. Intet sikkerhedsresumé kan genereres fra de nuværende data.

> Se venligst Produktoversigten (SmPC) for sikkerhedsinformation. SmPC for Livtencity® er tilgængelig via EMA's hjemmeside.

---

## Konklusion og næste trin

**Afgørelse: Udsat**

**Begrundelse:**
Bevissamlingen er ufuldstændig og indeholder ikke minimumindtastningerne for en vurdering af medicinsgenbrug. TxGNN-prognosepipeline har ikke produceret resultater for denne kandidat, og alle sikkerhedsdata mangler. Ingen klinisk anbefaling af nogen art kan gives, før disse kløfter er løst.

**For at fortsætte, er følgende nødvendig:**

- [ ] **Kør TxGNN-prognose-pipeline igen** for Maribavir (DB06234) for at udfylde `predicted_indications` — dette er det enkelte vigtigste trin
- [ ] **Hent virkemekanisme fra DrugBank API** (DB06234) for at løse datakløft DG002
- [ ] **Download og analysér SmPC** fra EMA's medicindatabase for at løse datakløft DG001 (advarsler, kontraindikationer, interaktioner)
- [ ] **Verificer EMA centraliseret godkendelsestatus** for Livtencity® og opdatér Danmarks regulatoriske sektion i overensstemmelse hermed
- [ ] **Generer bevissamlingen igen (v5)** når ovenstående kløfter er løst, og fortsæt derefter med fuld vurdering

---

> ⚠️ **Ansvarsfraskrivelse:** Denne rapport er til forskningsformål kun og udgør ikke medicinsk rådgivning. Enhver medicinsgenbrug-kandidat identificeret af TxGNN kræver klinisk validering før anvendelse.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

