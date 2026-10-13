---
layout: default
title: Trandolapril
parent: Kun modelforudsigelse (L5)
nav_order: 848
evidence_level: L5
indication_count: 10
---

# Trandolapril
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

# Trandolapril: Fra hypertension til malign renovaskulær hypertension

## Resumé i én sætning

Trandolapril er en ACE-hæmmer, som oprindeligt anvendes til behandling af hypertension (forhøjet blodtryk).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **malign renovaskulær hypertension**,
men der er i øjeblikket **ingen registrerede kliniske forsøg** og **ingen publikationer** direkte knyttet til denne indikation. Forudsigelsen bygger udelukkende på modellen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Hypertension (forhøjet blodtryk) |
| Forudsagt ny indikation | Malign renovaskulær hypertension |
| TxGNN-forudsigelsesscore | 99,92 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger i øjeblikket ikke detaljerede data om virkningsmekanismen i de data, der er indsamlet til denne rapport. Trandolapril er dog kendt som en ACE-hæmmer (angiotensin-konverterende enzym), og dens effekt ved hypertension er veletableret.

Renovaskulær hypertension er i høj grad drevet af aktivering af renin-angiotensin-systemet. Det gør det biologisk plausibelt, at blokade af dette system kan være gavnlig. Indikationen ligger imidlertid meget tæt på den allerede godkendte anvendelse ved hypertension og er derfor snarere en udvidelse end egentlig repurposing.

Der er også en vigtig forbehold: ACE-hæmmere indebærer en kendt risiko ved bilateral nyrearteriestenose (akut fald i nyrefunktionen), så anvendelse kræver forsigtighed.

**Øvrige forudsagte indikationer** (alle med score omkring 99,9 % og alle med anbefalingen Hold):
- **Malign hypertensiv nyresygdom** (L5): RAS-blokade er mekanistisk relevant ved hypertensiv nefropati, men der foreligger ingen forsøg eller litteratur specifikt for trandolapril.
- **Pulmonal hypertension med uklar multifaktoriel mekanisme** (L5): Sammenhængen mellem ACE-hæmning og pulmonal karremodellering er kun spekulativ. Den høje score afspejler sandsynligvis nærhed til hypertensionsbegreber i netværket.
- **Pulmonal hypertension som følge af lungesygdom og/eller hypoxi** (L4): Kun indirekte, præklinisk støtte (se litteraturafsnittet).
- **Braddock syndrom** (L5): Ingen plausibel mekanistisk sammenhæng kunne fastslås.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for den primære forudsagte indikation.

---

## Litteraturevidens

Der foreligger ingen litteratur for den primære forudsagte indikation (malign renovaskulær hypertension).

For den forudsagte indikation *pulmonal hypertension som følge af lungesygdom og/eller hypoxi* er følgende indirekte litteratur indsamlet:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [8166049](https://pubmed.ncbi.nlm.nih.gov/8166049/) | 1994 | Review | The American Journal of Cardiology | Molekylært grundlag for regression af hjertehypertrofi ved nedsat mekanisk overbelastning |
| [7511729](https://pubmed.ncbi.nlm.nih.gov/7511729/) | 1994 | Præklinisk (dyr) | Journal of Cardiovascular Pharmacology | Trandolapril fik venstre ventrikelhypertrofi til at regrediere hos spontant hypertensive rotter og påvirkede koronar modstand og ventrikulær compliance |
| [9218195](https://pubmed.ncbi.nlm.nih.gov/9218195/) | 1997 | Præklinisk (dyr) | Journal of Hypertension. Supplement | Præklinisk undersøgelse af kombinationen verapamil og trandolapril ved blodtryksreduktion og samtidig kardiovaskulær/metabolisk sygdom |
| [8909991](https://pubmed.ncbi.nlm.nih.gov/8909991/) | 1996 | Præklinisk (dyr) | General Pharmacology | Trandolapril plus verapamil hæmmede hypoxi-induceret koronar vasospasme efter iskæmi-reperfusionsskade hos hunde |
| [17393952](https://pubmed.ncbi.nlm.nih.gov/17393952/) | 2007 | Case report | Journal of the National Medical Association | Hos én patient med seglcellesygdom forsvandt kroniske smerter under ACE-hæmmerbehandling (ikke relateret til pulmonal hypertension) |

Bemærk: Litteraturen vedrører systemisk/koronar karstruktur og hjerteremodellering og ikke pulmonalt tryk. Der er ingen humane forsøg.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107397625 | Gopten (Orifarm A/S) | Kapsler, hårde | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

**Kontraindikationer/risikotilstande fra vidensgrafen** (afledt af TxGNN-vidensgrafen, ikke fra produktresuméets tekst): 
- Nyre- og leversygdom samt galdeblæresygdom
- Angioødem (inkl. arveligt og erhvervet angioødem samt RAAS-blokker-induceret angioødem)
- Neutropeni og agranulocytose
- Aortastenose og andre aortaklapsygdomme
- Hypotension
- Hypertrofisk kardiomyopati
- Nyrearterieobstruktion
- Myasthenia gravis
- Ventrikulær takykardi og atrioventrikulær blok
- Hjerteinsufficiens
- Bindevævs-, knogle- og bruskygdomme

**Lægemiddelinteraktioner** (100 registrerede; udvalgte eksempler):
- **Alvorlige (Major):** Kaliumcitrat og kaliumbikarbonat (risiko for hyperkaliæmi)
- **Moderate:** Metformin, alogliptin, canagliflozin, dapagliflozin, empagliflozin, glimepiride, chlorpropamid, acetylsalicylsyre, morfin, bupropion, dronabinol, hydrocortison, dexamethason, betamethason, triamcinolon, budesonid, picosulfat og polyethylenglycol med elektrolytter

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5) uden kliniske forsøg eller litteratur for malign renovaskulær hypertension. Indikationen ligger tæt på den eksisterende hypertensionsindikation, og ACE-hæmmere indebærer en kendt risiko ved bilateral nyrearteriestenose.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Gennemgang af advarsler og kontraindikationer i produktresuméet fra Lægemiddelstyrelsen (sikkerhedsscreening kan ikke gennemføres uden dette)
- Kliniske data eller relevant litteratur specifikt for trandolapril ved malign renovaskulær hypertension og malign hypertensiv nyresygdom
- Vurdering af nyrefunktions- og nyrearteriestenoserisiko hos den aktuelle patientgruppe
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

