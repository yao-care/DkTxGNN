---
layout: default
title: Pyridostigmine
parent: Kun modelforudsigelse (L5)
nav_order: 696
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "pyridostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly"]
description: "Pyridostigmine: forudsagt ny indikation Autoimmune disease of peripheral nervous system (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Pyridostigmine
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

## Pyridostigmine: Autoimmune disease of peripheral nervous system
{: .text-alpha }

## Opsummering i en sætning

Pyridostigmin er en acetylcholinesterasehæmmer, der oprindeligt anvendes til symptomatisk behandling af myasthenia gravis og andre sygdomme i den neuromuskulære overgang. TxGNN-modellen forudsiger, at lægemidlet kan være effektivt ved **myasthenia gravis med thymushyperplasi**. Forudsigelsen understøttes af **3 publikationer** (en oversigtsartikel, en case report og en kohortestudie) og **ingen registrerede kliniske forsøg**. Der er reelt tale om en undertype af den allerede kendte indikation og ikke om egentlig ny anvendelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Autoimmune disease of peripheral nervous system |
| TxGNN-forudsigelsesscore | 0.9975 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er denne forudsigelse rimelig?

Pyridostigmin er en reversibel acetylcholinesterasehæmmer. Den øger mængden af acetylcholin ved den neuromuskulære overgang og kompenserer dermed for det reducerede antal fungerende acetylcholinreceptorer ved myasthenia gravis. Detaljerede mekanismedata var ikke tilgængelige i de data, der er indsamlet til denne rapport, så beskrivelsen bygger på almen farmakologisk viden.

Myasthenia gravis med thymushyperplasi er en undertype af den sygdom, pyridostigmin allerede anvendes til. Mekanismen er symptomatisk og afhænger ikke af, om thymus er forstørret. Det er derfor mekanistisk rimeligt, at lægemidlet virker i denne undergruppe.

Den tilgængelige litteratur består af observationelle data, som ikke isolerer pyridostigmins effekt. Forudsigelsen bør derfor ses som en bekræftelse af en kendt anvendelse og ikke som et nyt terapeutisk fund.

---

## Evidens fra kliniske forsøg

Der er for tiden ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [34225443](https://pubmed.ncbi.nlm.nih.gov/34225443/) | 2021 | Oversigtsartikel | Molecular Medicine Reports | Genomiske, fænotypiske og epigenetiske aspekter af myasthenia gravis, herunder autoimmunitet og patologi |
| [25683765](https://pubmed.ncbi.nlm.nih.gov/25683765/) | 2015 | Kohortestudie | Journal of Neurology | Todelt opfølgning efter thymektomi hos 39 patienter med sent debuterende, ikke-thymomassocieret myasthenia gravis |
| [18053719](https://pubmed.ncbi.nlm.nih.gov/18053719/) | 2008 | Case report | Neuromuscular Disorders | MuSK-positiv myasthenia gravis med thymushyperplasi og fremtrædende "dropped head"-syndrom |

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100123355 | Mestinon (Viatris ApS) | Overtrukne tabletter (oral) | Indikationstekst ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra videngrafen** (ikke fra produktresumeet): nyresygdom, pyoureter, astma (herunder intrinsisk og allergisk astma) og urinvejsobstruktion.
- **Lægemiddelinteraktioner:** 108 interaktioner er registreret. Alle de viste er af moderat sværhedsgrad. De vigtigste grupper er:
  - Kortikosteroider: hydrokortison, prednison, prednisolon, dexamethason, betamethason, triamcinolon og budesonid.
  - Antikolinerge midler: atropin, hyoscyamin, scopolamin, glycopyrronium, methscopolamin, dicyclomin, clidinium, trospium, mepenzolat og propantelin.
  - Aminoglykosider: neomycin, kanamycin og paromomycin.

Produktresuméets advarsler og kontraindikationer var ikke tilgængelige. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
- Pyridostigmin er allerede markedsført i Danmark og anvendes mekanistisk korrekt ved myasthenia gravis, så undertypen er i praksis dækket af den kendte anvendelse. Evidensen for netop thymushyperplasi er dog kun observationel (L3), uden kliniske forsøg.

**For at komme videre kræves:**
- Gennemgang af det danske produktresumé for godkendt indikation, advarsler og kontraindikationer.
- Bekræftelse af, at anvendelsen er dækket af den eksisterende indikation, eller afklaring af behovet for yderligere dokumentation.
- Data om virkningsmekanismen fra DrugBank.
- Klinisk vurdering af kontraindikationer fra videngrafen (astma, nyresygdom, urinvejsobstruktion) og af interaktioner med kortikosteroider, antikolinergika og aminoglykosider.

---

## Øvrige forudsagte indikationer (kort oversigt)

| Rang | Forudsagt indikation | Score | Evidensniveau | Anbefaling | Kommentar |
|------|------|------|------|------|------|
| 3 | Autoimmun sygdom i det perifere nervesystem | 0,9975 | L5 | Research Question | Bred kategori; mekanismen gælder kun neuromuskulære overgangssygdomme og ikke fx demyeliniserende neuropatier |
| 5 | Sygdom i receptoraktivitet | 0,9973 | L4 | Hold | Meget bred term; litteraturen er uensartet og understøtter ikke en samlet indikation |
| 6 | Hypersplenisme | 0,9930 | L5 | Hold | Ingen mekanistisk forbindelse og ingen evidens; sandsynligvis en grafbaseret artefakt |
| 7 | Atypisk hæmolytisk-uræmisk syndrom med faktor B-anomali | 0,9922 | L5 | Hold | Pyridostigmin virker ikke på komplementsystemet; ingen evidens |
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

