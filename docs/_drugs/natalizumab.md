---
layout: default
title: Natalizumab
parent: Kun modelforudsigelse (L5)
nav_order: 577
evidence_level: L5
indication_count: 5
last_modified_at: 2026-11-24
monitor_inn: "NATALIZUMAB"
predicted_indications: ["bronchitis", "parapsoriasis", "psoriasis", "severe nonproliferative diabetic retinopathy", "acute lichenoid pityriasis"]
description: "Natalizumab: forudsagt ny indikation Bronkitis (bronchitis) (evidensniveau L5). I Danmark, markedsføringstilladelser: 3 (gyldige: 3)"
---

# Natalizumab
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **5** stk.
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

## Natalizumab: Bronkitis (bronchitis)
{: .text-alpha }

## Resumé

Natalizumab er et monoklonalt antistof, der oprindeligt anvendes til behandling af Crohns sygdom, inflammatorisk tarmsygdom og multipel sklerose.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **bronkitis**,
men der er i øjeblikket **ingen kliniske forsøg** og **ingen publikationer**, der understøtter denne forudsigelse. Den er udelukkende beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Bronkitis (bronchitis) |
| TxGNN-forudsigelsesscore | 0.9946 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Ifølge afsnittet »Mechanism of Action« i den produktinformation, som den amerikanske FDA har godkendt (Prescribing Information), for Natalizumab (uofficiel oversættelse): »Natalizumab binder sig til α4-subenheden af α4β1- og α4β7-integriner, som udtrykkes på overfladen af alle leukocytter undtagen neutrofile, og hæmmer den α4-medierede adhæsion af leukocytter til deres modreceptor(er). Receptorerne for α4-familien af integriner omfatter vaskulært celleadhæsionsmolekyle-1 (VCAM-1), som udtrykkes på aktiveret vaskulært endotel, og mukosalt addressin-celleadhæsionsmolekyle-1 (MAdCAM-1), som findes på vaskulære endotelceller i mave-tarm-kanalen.« Engelsk originaltekst: "Natalizumab binds to the α4-subunit of α4β1 and α4β7 integrins expressed on the surface of all leukocytes except neutrophils, and inhibits the α4-mediated adhesion of leukocytes to their counter-receptor(s). The receptors for the α4 family of integrins include vascular cell adhesion molecule-1 (VCAM-1), which is expressed on activated vascular endothelium, and mucosal addressin cell adhesion molecule-1 (MAdCAM-1) present on vascular endothelial cells of the gastrointestinal tract." ([DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962), version af 2026-10-09; hentet 2026-11-19). Natalizumab er kendt for at blokere alfa-4-integrin-medieret transport af leukocytter (hvide blodlegemer) ind i væv. Denne mekanisme er relevant ved de oprindelige indikationer, hvor betændelsesceller trænger ind i henholdsvis tarm og centralnervesystem.

Den mekanistiske tanke bag forudsigelsen er, at en reduceret rekruttering af inflammatoriske celler til luftvejsvæv teoretisk kunne dæmpe bronkitis. Der er dog hverken kliniske eller litteraturbaserede holdepunkter for dette, og lægemidlets immunsupprimerende virkning kan tværtimod øge risikoen for luftvejsinfektioner. TxGNN-scoren (0,9946) er en ren beregningsmæssig forudsigelse.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig for bronkitis.

---

## Markedsinformation for Danmark

<!-- licenses:begin -->

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Aktive stoffer | Status |
|---------|------|------|------|------|
| 28106803822 | Tyruko | koncentrat til infusionsvæske, opløsning | Natalizumab | Gyldig |
| 28106422220 | Tysabri | injektionsvæske, opløsning i fyldt injektionssprøjte | Natalizumab | Gyldig |
| 28103691204 | Tysabri | koncentrat til infusionsvæske, opløsning | Natalizumab | Gyldig |

Tabellen viser alle 3 markedsføringstilladelser til humane lægemidler med dette aktive stof i Lægemiddelstyrelsens lister over godkendte og afregistrerede lægemidler; gyldige tilladelser står først.

<!-- licenses:end -->

---

## Sikkerhedsovervejelser

- **Kontraindikationer (fra vidensgrafen, ikke produktresuméet)**: Progressiv multifokal leukoencefalopati (PML).
- **Lægemiddelinteraktioner**: Der er identificeret 100 interaktioner. Blandt de vigtigste:
  - **Alvorlige (Major)**: Kortikosteroider (hydrokortison, triamcinolon, dexamethason, betamethason, budesonid, prednisolon, prednison), mercaptopurin, levamisol, trimetrexat samt radioaktive lægemidler og radioimmunoterapi (iobenguan I-131, ibritumomab tiuxetan, tositumomab).
  - **Moderate**: Naltrexon.
  - **Milde (Minor)**: Zinksalte (sulfat, acetat, gluconat, chlorid).
- **Øvrige forhold**: Immunsuppression kan øge risikoen for luftvejsinfektioner, hvilket er særligt relevant ved en luftvejsindikation.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for bronkitis bygger udelukkende på en beregningsmodel uden kliniske forsøg eller publikationer (evidensniveau L5). Den kendte PML-risiko og den immunsupprimerende virkning gør forholdet mellem fordele og risici ugunstigt for en indikation som bronkitis.

**For at komme videre kræves følgende:**
- Data om virkningsmekanismen (MOA) fra DrugBank
- Advarsler og kontraindikationer fra det danske produktresumé (SmPC)
- Præklinisk eller mekanistisk understøttelse af, at alfa-4-integrinblokade er relevant ved bronkitis
- En vurdering af infektionsrisikoen ved en luftvejsindikation

---

## Andre forudsagte indikationer (til orientering)

| Forudsagt indikation | TxGNN-score | Evidensniveau | Anbefaling | Kommentar |
|------|------|------|------|------|
| Parapsoriasis | 0,9937 | L5 | Hold | Kun én case-rapport (PMID 32470781), som beskriver en hudbivirkning, ikke en terapeutisk effekt |
| Psoriasis | 0,9919 | L4 | Forskningsspørgsmål | Modstridende litteratur: en serie på 18 patienter viser bedring (PMID 33589543), mens flere case-rapporter beskriver udløsning eller forværring |
| Svær non-proliferativ diabetisk retinopati | 0,9918 | L5 | Hold | Ingen evidens; PML-risiko gør risiko-nytte-forholdet ugunstigt |
| Akut lichenoid pityriasis | 0,9904 | L5 | Hold | Kun den samme case-rapport (PMID 32470781), som beskriver en bivirkning |

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side. Sætningen om, at data om virkningsmekanismen ikke var tilgængelige, er erstattet med et uddrag fra den angivne officielle produktinformation (med uofficiel oversættelse); modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-19 | Sætningen »data om virkningsmekanismen er ikke tilgængelige« erstattet med uddrag fra den amerikanske produktinformation | Sætning om manglende data om virkningsmekanismen erstattet med et uddrag med kilde | [DailyMed: Tysabri (natalizumab) prescribing information, Biogen Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c5fdde91-1989-4dd2-9129-4f3323ea2962) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

