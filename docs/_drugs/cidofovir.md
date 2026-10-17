---
layout: default
title: Cidofovir
parent: Kun modelforudsigelse (L5)
nav_order: 193
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-14
description: "Cidofovir: forudsagt ny indikation Skleroserende kolangitis (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (godkendelsesteksten er tom)"
monitor_inn: "cidofovir"
predicted_indications: ["sclerosing cholangitis", "rheumatoid arthritis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome"]
---

# Cidofovir
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **4** stk.
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

# Cidofovir: Fra antiviral behandling til skleroserende kolangitis

## Resumé i én sætning

Cidofovir er et antiviralt lægemiddel (en acyklisk nukleotidanalog), som markedsføres i Danmark som koncentrat til infusionsvæske. Det er hovedsageligt kendt for behandling af virusinfektioner såsom cytomegalovirus (CMV); den godkendte indikationstekst er dog ikke tilgængelig i de data, der er indsamlet til denne rapport.
TxGNN-modellen forudsiger, at det kan have effekt ved **skleroserende kolangitis**,
men der er **0 kliniske forsøg** og **0 publikationer** til støtte for denne forudsigelse. Forudsigelsen er alene modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (godkendelsesteksten er tom) |
| Forudsagt ny indikation | Skleroserende kolangitis |
| TxGNN-forudsigelsesscore | 99,94 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger på nuværende tidspunkt ingen detaljerede data om virkningsmekanisme. Cidofovir er kendt som en acyklisk nukleotidanalog med aktivitet mod DNA-vira (bl.a. CMV, adenovirus, HPV og poxvira), men dette er ikke understøttet af mekanismedata i det foreliggende datagrundlag.

Skleroserende kolangitis er en kronisk, overvejende immunmedieret og kolestatisk sygdom i galdevejene. Der er ikke noget oplagt mekanistisk link mellem cidofovirs antivirale virkning og denne patologi. En spekulativ forbindelse kunne være virale udløsere eller CMV-associeret galdevejssygdom hos immunsvækkede patienter (f.eks. AIDS-kolangiopati), men dette er ikke understøttet af data.

Hertil kommer, at cidofovir har en betydelig risiko for nyretoksicitet, hvilket er et bekymrende forhold ved lever- og galdevejssygdom. Den høje modelscore skal derfor tolkes forsigtigt og kan afspejle en artefakt i vidensgrafen.

Øvrige forudsagte indikationer i datagrundlaget (alle med evidensniveau L5 og anbefalingen Hold):

| Rang | Sygdom | TxGNN-score | Bemærkning |
|------|------|------|------|
| 2 | Reumatoid artrit | 99,82 % | De fundne artikler handler om leflunomid mod CMV og viser ingen effekt af cidofovir ved reumatoid artrit |
| 3 | Kolobomatøs mikroftalmi-rhizomel dysplasi-syndrom | 99,62 % | Sjælden medfødt udviklingsforstyrrelse uden plausibel mekanistisk rationale |
| 4 | Brakydaktyli-syndaktyli-syndrom | 99,49 % | Medfødt lemmemalformation; sandsynligvis en artefakt i vidensgrafen |

---

## Dansk markedsinformation

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28107018623 | Cidofovir Carefarm (Orifarm A/S) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i de tilgængelige data |

---

## Cytotoksicitet

Cidofovir er et antiviralt middel og ikke et antineoplastisk lægemiddel; derfor er dette afsnit ikke relevant.

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra vidensgraf (ikke fra produktresumé)**: TxGNN-vidensgrafen (PrimeKG) angiver kontraindikationskanter til nyresygdom, pyouretær, acidose og erhvervet laktatacidose. Disse stammer ikke fra produkttekst og bør verificeres mod produktresuméet.
- **Lægemiddelinteraktioner**: Der er identificeret 60 interaktioner i alt. Blandt de angivne er mange af sværhedsgraden *Major*, især med andre potentielt nefrotoksiske stoffer:
  - Amphotericin B (inkl. lipidkompleks, kolesterylsulfat og liposomal form)
  - Aminoglykosider: kanamycin, neomycin, streptomycin
  - Polymyxin B og vancomycin
  - Mesalazin, balsalazid, olsalazin og sulfasalazin
  - Deferasirox og deferoxamin
  - Kontrastmidler/radiofarmaka: diatrizoat, iodipamid, iobenguan (I-131)
  - Moderat sværhedsgrad: exenatid og trospium
- **Øvrige oplysninger**: Nefrotoksicitet og neutropeni er i de indsamlede data nævnt som væsentlige risici i den kliniske vurdering.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for skleroserende kolangitis bygger udelukkende på en vidensgrafmodel uden kliniske forsøg eller publikationer (evidensniveau L5). Der er intet klart mekanistisk link, og cidofovirs nyretoksicitet vejer tungt.

**For at komme videre er følgende nødvendigt:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé (SmPC) fra Lægemiddelstyrelsen med advarsler, kontraindikationer og godkendt indikation
- Prækliniske eller mekanistiske studier, der kan underbygge et link til skleroserende kolangitis
- Litteratur- og forsøgsgennemgang, der specifikt søger evidens for cidofovir ved galdevejssygdom
- Vurdering af administrationsvej og nyresikkerhed ved lever- og galdevejssygdom
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

