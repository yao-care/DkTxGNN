---
layout: default
title: Theophylline
parent: Kun modelforudsigelse (L5)
nav_order: 820
evidence_level: L5
indication_count: 6
monitor_inn: "theophylline"
predicted_indications: ["thrombotic disease", "nasal cavity disease", "laryngotracheitis", "tracheal disease", "pharyngitis", "acute laryngopharyngitis"]
last_modified_at: 2026-10-30
description: "Theophylline: forudsagt ny indikation Trombotisk sygdom (evidensniveau L5). Oprindelig indikation: Astma, bronkitis, lungeemfysem og andre luftvejssygdomme"
---

# Theophylline
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

## Theophyllin: Fra astma til trombotisk sygdom
{: .text-alpha }

## Resumé

Theophyllin er en bronkodilator, der oprindeligt bruges til behandling af astma og andre kroniske lungesygdomme (relationer registreret i videnbasen).
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **trombotisk sygdom**,
men der er **ingen kliniske forsøg** og **ingen publikationer, der direkte undersøger denne anvendelse**.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Astma, bronkitis, lungeemfysem og andre luftvejssygdomme (relationer registreret i videnbasen; de danske tilladelser indeholder ingen indikationstekst) |
| Forudsagt ny indikation | Trombotisk sygdom |
| TxGNN-forudsigelsesscore | 0,9962 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen rimelig?

Der foreligger ikke data om virkningsmekanisme i de data, der er indsamlet til denne rapport. Theophyllin er dog kendt som en uselektiv phosphodiesterasehæmmer og adenosinreceptorantagonist. Hæmning af phosphodiesterase øger cAMP i blodplader, hvilket teoretisk kan dæmpe trombocytaggregation. Der er således en mekanistisk begrundelse for forudsigelsen.

Samtidig er retningen af effekten usikker: Adenosinantagonisme kan modvirke hæmning af blodplader. Ingen af de fundne publikationer tester theophyllin som antitrombotisk middel. De handler om ticlopidins farmakokinetik, analyser af trombocytmarkører, antikoagulation ved prøvehåndtering og en theophyllinsensor. Den høje score er en beregnet forudsigelse uden klinisk støtte.

## Kliniske forsøg

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Ingen af de fundne publikationer undersøger theophyllin som behandling af trombotisk sygdom. Nedenfor er de mest relevante, som alle kun er indirekte relateret.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [8055680](https://pubmed.ncbi.nlm.nih.gov/8055680/) | 1994 | Review | Clinical Pharmacokinetics | Farmakokinetik for ticlopidin (anden trombocythæmmer), ikke theophyllin |
| [6771102](https://pubmed.ncbi.nlm.nih.gov/6771102/) | 1980 | Review | CRC Critical Reviews in Biochemistry | Prostaglandiner, blodplader og aterosklerose; prostacyclin hæmmer aggregation via cAMP |
| [8981060](https://pubmed.ncbi.nlm.nih.gov/8981060/) | 1996 | Laboratorie­studie | General Pharmacology | Milrinon og adenosin hæmmer trombocytrespons via cAMP |
| [29254574](https://pubmed.ncbi.nlm.nih.gov/29254574/) | 2018 | Analytisk | Analytica Chimica Acta | Elektrokemisk sensor til måling af theophyllin; ingen trombosedata |
| [32824700](https://pubmed.ncbi.nlm.nih.gov/32824700/) | 2020 | Metode | Cells | Antikoagulation og prøvehåndtering ved måling af mikroRNA i blod |
| [25856065](https://pubmed.ncbi.nlm.nih.gov/25856065/) | 2015 | Metode | Platelets | Måling af opløseligt CLEC-2 som markør for trombocytaktivering |

## Information om det danske marked

De to tilladelser er begge til lægemidler med theophyllin som eneste aktive stof. Der foreligger ingen godkendt indikationstekst i de indsamlede data.

| Tilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101004478 | Theo-dur (Karo Pharma AB) | Depottabletter | Ikke oplyst |
| 28101164083 | Unixan (Ennogen Healthcare (Europe) Ltd) | Depottabletter | Ikke oplyst |

## Sikkerhedsovervejelser

- **Interaktioner med andre lægemidler**: 530 kendte interaktioner er registreret. Blandt de angivne er bupropion en **alvorlig** (Major) interaktion. Moderate interaktioner omfatter bl.a. famotidin, ranitidin, cimetidin, omeprazol, rabeprazol, clarithromycin, doxycyclin, tetracyclin, minocyclin samt kortikosteroider (hydrocortison, dexamethason, betamethason, triamcinolon, budesonid).
- **Kontraindikationer registreret i videnbasen (ikke produkttekst)**: bl.a. hypertension, leversvigt, epilepsi, porfyri, nyresygdom, hypothyreoidisme, mavesår, glaukom, diabetes, diabetisk ketoacidose, godartet prostataforstørrelse, neutropeni og agranulocytose.
- Lægemidlet har et snævert terapeutisk indeks, og serumkoncentrationen skal overvåges.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

## Andre forudsagte indikationer (til orientering)

| Forudsagt indikation | Score | Evidensniveau | Bemærkning |
|------|------|------|------|
| Næsehulesygdom | 0,9953 | L5 | Ét lille forsøg fra 1998 (PMID 9648963) med depot-theophyllin ved allergisk rhinitis, men ingen forsøg med den forudsagte sygdom som sådan; evidensen er indirekte |
| Laryngotracheitis | 0,9951 | L5 | Ingen forsøg eller litteratur |
| Trakealsygdom | 0,9949 | L5 | Kun prækliniske og veterinære data samt indirekte forsøg; ingen humane studier |
| Faryngitis | 0,9946 | L5 | Ingen relevant litteratur om theophyllin |
| Akut laryngofaryngitis | 0,9935 | L5 | Ingen forsøg eller litteratur |

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler alene på en beregnet score. Der findes ingen kliniske forsøg og ingen studier af theophyllin ved trombotisk sygdom, og adenosinantagonisme kan virke imod den ønskede effekt. Lægemidlets snævre terapeutiske indeks og mange interaktioner øger den sikkerhedsmæssige byrde.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) og en vurdering af, om effekten på blodplader går i den ønskede retning
- Prækliniske studier af theophyllins effekt på trombocytaggregation og trombedannelse
- Gennemgang af produktresuméer fra Lægemiddelstyrelsen for godkendte indikationer, advarsler og kontraindikationer
- Sikkerhedsplan for lægemiddelinteraktioner og overvågning af serumkoncentration, hvis klinisk afprøvning overvejes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

