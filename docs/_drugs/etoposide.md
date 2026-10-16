---
layout: default
title: Etoposide
parent: Kun modelforudsigelse (L5)
nav_order: 337
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Etoposide: forudsagt ny indikation Ewing-sarkom (evidensniveau L5). Oprindelig indikation: Småcellet lungekræft, testikelkræft/kimcelletumorer (fra vidensgrafen"
---

# Etoposide
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

# Etoposid: Fra småcellet lungekræft og kimcelletumorer til Ewing-sarkom

## Opsummering

Etoposid er et kemoterapeutisk middel (topoisomerase II-hæmmer), som oprindeligt anvendes til småcellet lungekræft og kimcelletumorer i testiklerne.
TxGNN-modellen forudsiger, at det kan være effektivt ved **Ewing-sarkom** (det stærkest underbyggede af de forudsagte områder), med **33 registrerede kliniske forsøg** og **20 publikationer** i datamaterialet. Der er desuden en forudsigelse for **rabdomyosarkom** med både forsøg og litteratur. Bemærk, at etoposid allerede indgår i standardbehandlingen af Ewing-sarkom, så det er ikke en egentlig ny anvendelse.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Småcellet lungekræft, testikelkræft/kimcelletumorer (fra vidensgrafen; godkendt indikationstekst i den danske tilladelse er ikke angivet) |
| Forudsagt ny indikation | Ewing-sarkom (rang 1 i datamaterialet er "veldifferentieret føtalt adenokarcinom i lungen"; her præsenteres Ewing-sarkom som den bedst underbyggede forudsigelse) |
| TxGNN-score | 99,85 % (Ewing-sarkom); 99,94 % for rang 1 |
| Evidensniveau | L1 (Ewing-sarkom) |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails (Ewing-sarkom og rabdomyosarkom); Hold for øvrige forudsigelser |

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i datamaterialet. Etoposid er dog kendt som en topoisomerase II-hæmmer, der forårsager DNA-dobbeltstrengsbrud og dermed hæmmer celledeling i hurtigt prolifererende kræftceller.

Småcellet lungekræft og kimcelletumorer er kemosensitive tumorer, hvor etoposid er veletableret. Ewing-sarkom er også stærkt følsomt over for genotoksiske stoffer som etoposid. Etoposid anvendes i kombination med ifosfamid (IE) sammen med VDC-regimet (vincristin, doxorubicin, cyclophosphamid), og randomiserede fase 3-forsøg og konsensusanbefalinger understøtter brugen.

Ved rabdomyosarkom anvendes etoposid typisk sammen med ifosfamid i intermediær- og højrisikoregimer. Et studie viste, at ifosfamid/etoposid var bedre end vincristin/melphalan ved metastatisk sygdom hos børn.

## Klinisk forsøgsevidens (Ewing-sarkom)

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Fase 3 | Ukendt | Ikke angivet | EICESS 92: randomiseret sammenligning af kombinationskemoterapi plus kirurgi/strålebehandling |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Fase 3 | Ukendt | 1200 | EURO-E.W.I.N.G.99: kemoterapi med/uden strålebehandling og stamcellestøtte |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Fase 3 | Afsluttet | 587 | Kemoterapiintensivering via intervalkomprimering |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Fase 3 | Afsluttet | 642 | Tilføjelse af vincristin-topotecan-cyclophosphamid til standard 5-lægemiddelregime inkl. etoposid |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Fase 3 | Afsluttet | 278 | Dosisintensivering ved ikke-metastatisk Ewing-sarkom |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Fase 3 | Aktiv, rekrutterer ikke | 312 | Ganitumab tilføjet multiagens-kemoterapi ved metastatisk Ewing-sarkom |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Fase 2 | Afsluttet | 155 | Højdosiskemoterapi, strålebehandling og vedligeholdelse ved metastatisk Ewing-sarkom |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Fase 2 | Afsluttet | Ikke angivet | Kombinationskemoterapi inkl. etoposid og ifosfamid efterfulgt af resektion og strålebehandling |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Fase 2 | Aktiv, rekrutterer ikke | 83 | Irinotecan og temozolomid tillagt højdosis alkylerende kemoterapi |
| [NCT07194044](https://clinicaltrials.gov/study/NCT07194044) | Fase 1 | Rekrutterer | 15 | Gennemførlighed af intensiveret skema ved udbredt metastatisk Ewing-sarkom |

Til rabdomyosarkom er der blandt andet fase 3-forsøget [NCT00003052](https://clinicaltrials.gov/study/NCT00003052) (EIA-kemoterapi med etoposid, ifosfamid og doxorubicin plus hypertermi ved højrisiko-bløddelssarkomer hos voksne, 340 deltagere, afsluttet) og fase 3-forsøget [NCT00876031](https://clinicaltrials.gov/study/NCT00876031) (oral vedligeholdelse med etoposid, idarubicin og trofosfamid, 195 deltagere, afsluttet).

For de øvrige forudsigelser (lungeblastom, primært pulmonalt lymfom, øvrige rabdomyosarkom-subtyper) er der ingen registrerede kliniske forsøg.

## Litteraturevidens (Ewing-sarkom)

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Tilføjelse af ifosfamid og etoposid til standardkemoterapi ved nydiagnosticeret Ewing-sarkom/PNET |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (fase 3) | Lancet | EE2012: sammenligning af to kemoterapiregimer |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Intervalkomprimeret kemoterapi ved lokaliseret Ewing-sarkom |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (fase 3) | J Clin Oncol | Ganitumab med intervalkomprimeret kemoterapi ved metastatisk sygdom |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | RCT-protokol | Trials | Protokol for EURO EWING 2012 |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Konsensusretningslinje | Cancer | Konsensusanbefalinger fra National Ewing Sarcoma Tumor Board |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | Nuværende behandling og fremtidigt samarbejde |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Overlevelse ca. 75 % ved lokaliseret sygdom, dårlig prognose ved metastaser |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Retrospektiv analyse | Sarcoma | Oral etoposid ved recidiverende/refraktær Ewing-sarkom hos unge og voksne (33 patienter) |
| [29513652](https://pubmed.ncbi.nlm.nih.gov/29513652/) | 2018 | Grundforskning | Nature | Ewing-sarkom er meget følsomt over for etoposid pga. EWS-FLI1-medierede R-loops og hæmmet BRCA1-reparation |

Til rabdomyosarkom: [11846301](https://pubmed.ncbi.nlm.nih.gov/11846301/) (2001, ifosfamid/etoposid bedre end vincristin/melphalan ved metastatisk sygdom) og [26503200](https://pubmed.ncbi.nlm.nih.gov/26503200/) (2016, J Clin Oncol, intensivt regime med dosiskomprimeret ifosfamid/etoposid ved højrisiko-sygdom).

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105221213 | Etoposid "Accord" (Accord Healthcare B.V.) | Koncentrat til infusionsvæske, opløsning | Indikationstekst ikke angivet i de indsamlede data |

Den eneste tilladelse er til injicerbar form. Hvis en anvendelse kræver oral administration (fx oral etoposid ved recidiv), er ruteforenelighed ikke vurderet.

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Konventionelt cytostatikum (topoisomerase II-hæmmer, epipodophyllotoxin) |
| Risiko for myelosuppression | Høj (knoglemarvssuppression er kendt; vidensgrafen peger på neutropeni, trombocytopeni, leukopeni og anæmi) |
| Emetogenicitet | Lav til moderat (iht. lægemiddelklassen; bekræft i produktresuméet) |
| Monitorering | Fuldt blodbillede med differentialtælling, lever- og nyrefunktion, elektrolytter |
| Beskyttelse ved håndtering | Skal håndteres efter gældende regler for cytostatika |

Se i øvrigt produktresuméet (SmPC) for advarsler og forholdsregler.

## Sikkerhedsovervejelser

- **Kontraindikationer/risici fra vidensgrafen** (ikke fra produktteksten): trombocytopeni, neutropeni, agranulocytose, leukopeni, anæmi (inkl. makrocytær), interstitiel lungesygdom, lungefibrose, nedsat nyrefunktion, acidose/metabolisk acidose og lægemiddelinduceret leverskade.
- **Lægemiddelinteraktioner**: 656 interaktioner er registreret. Blandt de moderate er aprepitant, rolapitant, metronidazol, tinidazol, eliglustat, rosuvastatin og simvastatin. Levofloxacin er mindre betydende.
- **Kombinationsrelateret**: Risiko for sekundær leukæmi og myelosuppression samt toksicitet fra samgivne midler (fx ifosfamid) skal overvåges.

Officielle advarsler og kontraindikationer fra det danske produktresumé indgik ikke i datamaterialet. Se det godkendte produktresumé (SmPC).

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails** (Ewing-sarkom og rabdomyosarkom). **Hold** for lungeblastom (kun case reports, forskningsspørgsmål), primært pulmonalt lymfom, veldifferentieret føtalt lungeadenokarcinom og sjældne rabdomyosarkom-subtyper (galdegang, parameningeal, prostata, vagina).

**Begrundelse:**
- Ewing-sarkom har flere fase 3-RCT'er og konsensusretningslinjer (L1). Etoposid er dog allerede standardbehandling, og effekten kan ikke tilskrives etoposid alene, da al evidens er baseret på kombinationsregimer. Rabdomyosarkom har et fase 3-forsøg og flere fase 2-studier, men fordelen er regimeafhængig og stærkest ved intermediær-/højrisiko eller metastatisk sygdom.

**For at komme videre kræves:**
- Godkendt indikationstekst, advarsler og kontraindikationer fra det danske produktresumé (blokerende datamangel)
- Data om virkningsmekanisme fra DrugBank
- Afklaring af, om den danske tilladelse dækker de relevante indikationer, og om en oral formulering er nødvendig
- Plan for sikkerhedsmonitorering (blodbillede, sekundær malignitet, kombinationstoksicitet)
- Dedikerede studier, før der overvejes brug ved de sjældne subtyper med kun case reports eller ingen evidens
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

