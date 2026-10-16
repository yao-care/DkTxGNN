---
layout: default
title: Propafenone
parent: Kun modelforudsigelse (L5)
nav_order: 690
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-14
description: "Propafenone: forudsagt ny indikation Manisk bipolar lidelse (rang 1) (evidensniveau L5). Oprindelig indikation: Atrieflimren og ventrikulær takykardi (fra videngrafen"
monitor_inn: "propafenone"
predicted_indications: ["manic bipolar affective disorder", "catecholaminergic polymorphic ventricular tachycardia", "periodic paralysis with transient compartment-like syndrome", "Prinzmetal angina", "incessant infant ventricular tachycardia", "arrhythmogenic right ventricular cardiomyopathy", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania"]
---

# Propafenone
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **8** stk.
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

# Propafenon: Fra atrieflimren og ventrikulær takykardi til katekolaminerg polymorf ventrikulær takykardi (CPVT)

## Sammenfatning

Propafenon er et klasse IC-antiarytmikum (natriumkanalblokker), som oprindeligt anvendes til behandling af atrieflimren og ventrikulær takykardi.
TxGNN-modellen forudsiger en række nye indikationer. Den bedst underbyggede er **katekolaminerg polymorf ventrikulær takykardi (CPVT)** (score 99,79 %), støttet af **0 registrerede kliniske forsøg** og **10 publikationer** (primært prækliniske data og case-niveau data).
Den højest scorende forudsigelse, **manisk bipolar lidelse**, støttes ikke af data, og litteraturen peger snarere på skade end gavn.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Atrieflimren og ventrikulær takykardi (fra videngrafen; indikationsteksten i det danske markedsføringstilladelsesregister er ikke angivet) |
| Forudsagt ny indikation | Manisk bipolar lidelse (rang 1); klinisk mest relevante: katekolaminerg polymorf ventrikulær takykardi (rang 2) |
| TxGNN-forudsigelsesscore | 99,80 % (manisk bipolar lidelse); 99,79 % (CPVT) |
| Evidensniveau | L4 (manisk bipolar lidelse); L3 (CPVT) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold (manisk bipolar lidelse); Proceed with Guardrails ved en målrettet forskningsundersøgelse af CPVT |

---

## Hvorfor er forudsigelsen rimelig?

Data om lægemidlets detaljerede virkningsmekanisme foreligger ikke i de data, der er indsamlet til denne rapport. Propafenon er dog kendt som klasse IC-antiarytmikum, og dets effekt ved atrieflimren og ventrikulær takykardi er veletableret.

**CPVT (rang 2):** Der er et stærkt mekanistisk rationale. CPVT skyldes typisk mutationer i ryanodinreceptor 2 (RyR2) eller calsequestrin, som giver spontane Ca²⁺-bølger. Prækliniske studier viser, at klasse IC-midler som flecainid og R-propafenon hæmmer RyR2-kanaler og undertrykker disse Ca²⁺-bølger (PMID 21270101, 26121139, 21798265). Et case-studie beskriver 35 års effektiv behandling med propafenon (PMID 30820400). Flecainid er dog det bedst etablerede klasse IC-middel ved CPVT.

**Manisk bipolar lidelse (rang 1):** Der er ikke påvist nogen plausibel terapeutisk mekanisme. Litteraturen beskriver tværtimod propafenon som mulig årsag til mani (case-rapport, 1985) og psykose ved interaktion med venlafaxin (2001). Den høje modelscore modsiges derfor af det kliniske signal.

**Øvrige forudsigelser:**
- *Vedvarende ventrikulær takykardi hos spædbørn (rang 5):* Natriumkanalblokade er i overensstemmelse med lægemidlets virkning, og der findes ældre pædiatriske data, men de er små og ikke specifikke. Risiko for proarytmi hos børn skal vurderes nøje.
- *Arytmogen højre ventrikel-kardiomyopati (rang 6):* Sikkerhedssignaler dominerer (QRS-udvidelse og vedvarende VT udløst af propafenon). Anvendelse er ikke støttet.
- *Periodisk paralyse, Prinzmetal-angina, nefrogent syndrom med uhensigtsmæssig antidiurese og trikotillomani (rang 3, 4, 7, 8):* Kun modelforudsigelse (L5) uden litteratur eller forsøg. For Prinzmetal-angina er der ingen kendt antivasospastisk mekanisme.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for nogen af de forudsagte indikationer.

---

## Litteraturevidens

Udvalgt for CPVT (de mest relevante publikationer):

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [30820400](https://pubmed.ncbi.nlm.nih.gov/30820400/) | 2019 | Case-rapport | HeartRhythm Case Reports | 35 års effektiv behandling af CPVT med propafenon |
| [21270101](https://pubmed.ncbi.nlm.nih.gov/21270101/) | 2011 | Præklinisk | Circ Arrhythm Electrophysiol | RyR2-hæmning bestemmer effekten af klasse I-antiarytmika ved CPVT |
| [26121139](https://pubmed.ncbi.nlm.nih.gov/26121139/) | 2015 | Præklinisk | PLoS One | RyR2-aktivitet bestemmer styrke og effekt af flecainid og R-propafenon mod arytmogene Ca²⁺-bølger |
| [21798265](https://pubmed.ncbi.nlm.nih.gov/21798265/) | 2011 | Præklinisk | J Mol Cell Cardiol | Screening af klasse I-antiarytmika mod Ca²⁺-bølger i myocytter uden calsequestrin |
| [35892906](https://pubmed.ncbi.nlm.nih.gov/35892906/) | 2022 | Systematisk review | Life (Basel) | Kliniske karakteristika og arytmiudfald ved CPVT i Kina (ikke propafenon-specifik) |
| [39564160](https://pubmed.ncbi.nlm.nih.gov/39564160/) | 2024 | Kohorte | Ann Pediatr Cardiol | Langtidsforløb ved CPVT (ikke propafenon-specifik) |

Udvalgt for andre forudsagte indikationer:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [2579063](https://pubmed.ncbi.nlm.nih.gov/2579063/) | 1985 | Case-rapport | J Clin Psychiatry | Mani som bivirkning til propafenon (manisk bipolar lidelse) |
| [11949740](https://pubmed.ncbi.nlm.nih.gov/11949740/) | 2001 | Case-rapport | Int J Psychiatry Med | Organisk psykose ved venlafaxin-propafenon-interaktion |
| [8237821](https://pubmed.ncbi.nlm.nih.gov/8237821/) | 1993 | Kohorte/case-serie | Am J Cardiol | Oral propafenon ved vedvarende supraventrikulær og ventrikulær takykardi hos børn |
| [2114081](https://pubmed.ncbi.nlm.nih.gov/2114081/) | 1990 | Case-serie | Arch Mal Coeur Vaiss | Vedvarende idiopatisk VT hos spædbørn; intravenøs flecainid eller propafenon hos de mest kritisk syge |
| [33194879](https://pubmed.ncbi.nlm.nih.gov/33194879/) | 2020 | Case-rapport (bivirkning) | Front Pediatr | Propafenon-induceret QRS-udvidelse hos et barn med ARVC |
| [8316922](https://pubmed.ncbi.nlm.nih.gov/8316922/) | 1993 | Case-serie (bivirkning) | S Afr Med J | Propafenon udløste vedvarende VT trods normal venstre ventrikelfunktion |

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101107082 | Rytmonorm (Viatris ApS) | Filmovertrukne tabletter | Indikationstekst ikke angivet i de indsamlede data |

---

## Sikkerhedsovervejelser

**Kontraindikationer/risikotilstande (fra videngrafen, ikke fra produktresuméet):** Langt QT-syndrom (herunder familiær form), torsades de pointes, nyre- og leversygdom, galdeblæresygdom, kaliummangel, lavt blodtryk, myokardieinfarkt, koronararteriesygdom og åreforkalkning, myasthenia gravis og andre sygdomme i den neuromuskulære overgang, hæmoglobinopati samt agranulocytose og neutropeni (herunder kongenitte former).

**Lægemiddelinteraktioner:** I alt 198 interaktioner er registreret. Blandt de viste er to af alvorlig grad (**Major**): **dolasetron** og **eliglustat**. Flere moderate interaktioner omfatter bl.a. clarithromycin, levofloxacin, ondansetron, palonosetron, cimetidin, famotidin, bupropion, aprepitant, loperamid og alosetron.

**Særlige forhold fra litteraturen:** Risiko for QRS-udvidelse og proarytmi (inkl. vedvarende VT) ved strukturel hjertesygdom og hos børn samt psykiatriske bivirkninger (mani, psykose).

Oplysninger om advarsler i det godkendte produktresumé (SmPC) mangler; se SmPC for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold** (samlet) — med mulighed for **Proceed with Guardrails** for en målrettet forskningsundersøgelse af CPVT.

**Begrundelse:**
- Den højest scorende forudsigelse (manisk bipolar lidelse) modsiges af litteraturen, som peger på skade. For CPVT er der et stærkt mekanistisk rationale og et langtidscase, men evidensen er overvejende præklinisk, og flecainid er det bedre dokumenterede alternativ. Flere øvrige forudsigelser har kun modelstøtte eller overvejende negative sikkerhedssignaler.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet (SmPC) for advarsler og kontraindikationer (blokerende datamangel)
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Klinisk data, helst kontrollerede studier, der sammenligner propafenon med flecainid ved CPVT
- Vurdering af proarytmirisiko, især ved strukturel hjertesygdom og hos børn
- Gennemgang af interaktioner for den aktuelle patientgruppe, især QT-forlængende lægemidler
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

