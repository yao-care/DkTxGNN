---
layout: default
title: Ganciclovir
parent: Kun modelforudsigelse (L5)
nav_order: 205
evidence_level: L5
indication_count: 0
---

# Ganciclovir
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

# Ganciclovir: Antivirusmiddel (CMV) — Ingen prognoser for genoptagelse af behandling tilgængeligt

## Sammenfatning i én sætning

Ganciclovir er en syntetisk guanosinanalog antivirusmiddel, som primært bruges til forebyggelse og behandling af cytomegalovirusinfektioner (CMV) hos immunsupprimerede patienter (f.eks. efter organtransplantation eller ved HIV/AIDS).
Den aktuelle evidenspakke indeholder **ingen TxGNN-forudsagte nye indikationer**, da prediktionspipeline'en ikke producerede nogen output for denne kandidat.
Kritiske huller i sikkerhedsdata og mekanisme-for-handling-felter forhindrer en fuldstændig evaluering af genoptagelse af behandling på nuværende tidspunkt.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Original indikation | CMV-retinitis; CMV-sygdomsprofylakse hos immunsupprimerede patienter (almene medicinske kundskaber — ingen dansk godkendelse registreret) |
| Forudsagt ny indikation | Ingen tilgængelig |
| TxGNN-prognosescore | N/A |
| Evidensniveau | L5 — ingen prognoser genereret |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markeringsgodkendelser | 0 |
| Anbefalet beslutning | Afvente |

---

## Hvorfor er denne prognose rimelig?

Der er ingen TxGNN-prognose for genoptagelse af behandling tilgængelig for Ganciclovir i denne evidenspakke; mekanistisk anvendelighed for en ny indikation kan derfor ikke vurderes på dette stadium.

Ud fra almene farmakologiske kundskaber er Ganciclovir (DrugBank: DB01004) en prodrug, der aktiveres præferenstielt i CMV-inficerede celler. Viral UL97-kinase fosforyler stoffet til ganciclovir-monofosfat; cellulære kinaserreagerer derefter med at producere trifosfatformen, som konkurrencemæssigt hæmmer viral DNA-polymerase (pUL54) og ved inkorporering i virale DNA-terminates-kædeforlængelse. Selektivitet stammer fra det præferentielle fosforyleringsstrin i inficerede celler. Mekanisme-for-handling-feltet i denne evidenspakke er uudfyldt og kræver hentning fra DrugBank API'en (Datakløft DG002).

Hvis TxGNN-pipeline'en køres igen med succes, kunne potentielle retningslinjer for genoptagelse af behandling omfatte andre herpesvirus-familieinfektioner (EBV, HHV-6, HHV-8), eller sygdomskontekster, hvor CMV-reaktivering spiller en dokumenteret patologisk rolle — såsom glioblastom, inflammatorisk tarmsygdom eller posttransplantationslymfoproliferativ sygdom. Imidlertid er disse retningslinjer spekulativ, indtil modeloutput er tilgængeligt.

---

## Klinisk forsøgsbevis

Intet relateret klinisk forsøg er aktuelt registreret for en genoptagelse af behandling-indikation.

*(Der er ingen predicted_indications-indgang i denne evidenspakke; derfor kan ingen tilknyttede forsøgsdata ekstraheres.)*

---

## Litteraturbevis

Ingen relateret litteratur er aktuelt tilgængelig for en genoptagelse af behandling-indikation.

*(Der er ingen predicted_indications-indgang i denne evidenspakke; derfor kan ingen tilknyttede publikationsdata ekstraheres.)*

---

## Markedsinformation for Danmark

Ingen markeringsgodkendelser er registreret for Ganciclovir i Danmark ifølge de leverede data.

| Markeringsgodkendelsesnummer | Produktnavn | Doseringsform | Godkendt indikation |
|-------|-------------|----------|-------------|
| — | — | — | Ingen godkendelser fundet |

> **Bemærk for ordinatorer:** Ganciclovir (Cymevene®) har en centraliseret EMA-markeringsgodkendelse, der gælder på tværs af EU/EØS. Fraværet af en lokale dansk registreringspost kan afspejle et datakløft snarere end et sandt fravær af tilgængelighed. Klinikere bør bekræfte nuværende status direkte via [EMA-produktdatabasen](https://www.ema.europa.eu/en/medicines) og Laegemiddelstyrelsens produktregister.

---

## Sikkerhedshensyn

Se venligst den godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

> Både nøgleadvarslerne og modindikationerne er uudfyldt i denne evidenspakke (Datakløft DG001 — Blokering alvorlighed). TFDA/Laegemiddelstyrelsens SmPC PDF skal hentes og analyseres, før alle sikkerhedsafhængige evalueringtrin kan fortsætte. Kendende klassesignale omfatter betydelig myelosuppression (neutropeni, trombocytopeni), reproduktiv toksicitet og kancerøsepotentiale, men disse kræver formelt SmPC-bekræftelse før klinisk brug i enhver ny indikation.

---

## Konklusion og næste trin

**Beslutning: Afvente**

**Begrundelse:**
Evidenspakken for Ganciclovir indeholder ingen TxGNN-prognoser for genoptagelse af behandling og mangler to kritiske datafelter (sikkerhedsprofil, mekanisme for handling), hvilket gør det umuligt at gennemføre en meningsfuld evaluering af genoptagelse af behandling eller sikkerhedsprescreening på nuværende tidspunkt.

**For at fortsætte er følgende nødvendigt:**

- **Kør TxGNN-prediktionspipeline igen** for Ganciclovir (DB01004) for at generere sygdomskandidater til genoptagelse af behandling — uden modeloutput kan denne hele evalueringsworkflow ikke avancere
- **Hent MOA-data fra DrugBank API'en** (Datakløft DG002 — Høj alvorlighed) for at muliggøre mekanistisk plausibilitetanalyse
- **Download og analysere SmPC PDF'en** fra Laegemiddelstyrelsen / EMA for at udfylde nøgleadvarsler og modindikationer (Datakløft DG001 — Blokering alvorlighed, påkrævet før S1-sikkerhedsprescreening)
- **Bekræft Danmark/EU-markedsstatus** ved at krydstjekke EMA's centraliserede godkendelsesregister for Cymevene® og eventuelle valganciclovirgodkendelser (prodrug), som kan være klinisk relevante

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

