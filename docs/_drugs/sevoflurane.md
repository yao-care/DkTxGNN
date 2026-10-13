---
layout: default
title: Sevoflurane
parent: Kun modelforudsigelse (L5)
nav_order: 759
evidence_level: L5
indication_count: 10
---

# Sevoflurane
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

# Sevofluran: Fra generel anæstesi til Prinzmetal-angina

## Resumé i én sætning

Sevofluran er en inhalationsanæstesi, som anvendes til generel anæstesi. De data, der er indsamlet til denne rapport, indeholder dog ingen godkendt indikationstekst fra den danske registrering. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **Prinzmetal-angina**, men der findes **0 kliniske forsøg** og **0 publikationer** for denne indikation. Forudsigelsen er derfor udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (anvendes generelt til generel anæstesi) |
| Forudsagt ny indikation | Prinzmetal-angina |
| TxGNN-forudsigelsesscore | 99,78 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen. Sevofluran tilhører gruppen af flygtige anæstetika, og dets effekt ved generel anæstesi er veldokumenteret. Mekanistisk er det ikke etableret, at det kan anvendes til Prinzmetal-angina.

Flygtige anæstetika har kendte karudvidende effekter og påvirker calciumkanaler i vaskulær glat muskulatur. Det kunne teoretisk hænge sammen med koronar vasospasme, som er kernen i Prinzmetal-angina. Der er dog hverken kliniske forsøg eller litteratur, der understøtter dette.

Sevofluran er ikke en etableret behandling af Prinzmetal-angina. Hos patienter med vasospastisk angina er det et perioperativt hensyn og ikke en terapi. Forudsigelsen bør derfor ses som en hypotese.

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for Prinzmetal-angina.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig for Prinzmetal-angina.

### Øvrige forudsagte indikationer (til orientering)

TxGNN forudsagde yderligere ni indikationer. Ingen af dem har kliniske forsøg, og litteraturen vedrører overvejende anæstesiforløb og ikke behandling af sygdommen.

| Forudsagt indikation | Score | Evidensniveau | Kommentar |
|------|------|------|------|
| Tourette syndrom | 99,50 % | L5 | Ingen data; en generel anæstetikum er upraktisk ved en kronisk lidelse |
| Fibromyalgi | 99,42 % | L4 | Kun én case-rapport om anæstesiforløb ([26419112](https://pubmed.ncbi.nlm.nih.gov/26419112/), 2015) |
| Tendinitis | 99,41 % | L4 | Ni publikationer om anæstesi ved seneoperationer, bl.a. et RCT, der sammenligner propofol og sevofluran ([38233786](https://pubmed.ncbi.nlm.nih.gov/38233786/), 2024); ikke sygdomsrettet |
| Myositis fibrosa | 99,41 % | L5 | Ingen data |
| Idiopatisk granulomatøs myositis | 99,41 % | L5 | Ingen data |
| Nefrogent syndrom med uhensigtsmæssig antidiurese | 99,40 % | L5 | Ingen data; sevoflurans renale effekter taler for forsigtighed |
| Trikotillomani | 99,33 % | L5 | Ingen data |
| Migræne | 99,23 % | L4 | Kun en retrospektiv kohorte om sevofluran-anæstesi til MR hos børn ([31852450](https://pubmed.ncbi.nlm.nih.gov/31852450/), 2019) |
| Inklusionslegememyositis | 99,09 % | L4 | Kun én case-rapport om anæstesi ([27247916](https://pubmed.ncbi.nlm.nih.gov/27247916/), 2016) |

---

## Oplysninger om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106657021 | Petrem Vet. | Væske til inhalationsdamp | Ikke angivet i de tilgængelige data |

Indehaver: Piramal Critical Care B.V. Status: gyldig. Bemærk, at produktnavnet "Vet." tyder på et veterinærlægemiddel; dette bør verificeres.

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: 172 interaktioner er registreret. Blandt de viste er følgende klassificeret som **alvorlige (Major)**: adrenalin, dolasetron og cisaprid. Mange andre er moderate, bl.a. ondansetron, palonosetron, clarithromycin, levofloxacin, morfin, famotidin, loperamid og exenatid, og metronidazol er mindre (Minor).
- **Mulige kontraindikationer fra vidensgrafen** (afledt af TxGNN-grafen og ikke fra produktresuméet): epilepsi, nyresygdom, leversygdom, galdeblæresygdom, hypotension, malign hypertermi, intrakraniel hypertension, pseudotumor cerebri, Duchennes og Beckers muskeldystrofi, muskeldystrofi, proteinuri og pyoureter.

Se i øvrigt det godkendte produktresumé (SPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for Prinzmetal-angina bygger udelukkende på modelscore (L5) uden kliniske forsøg eller litteratur. Sevofluran er en generel anæstesi og er uegnet som kronisk behandling af angina; desuden kan flere af de forudsagte indikationer ikke ses som terapeutiske muligheder.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer og godkendt indikation)
- Data om virkningsmekanisme (f.eks. fra DrugBank)
- Verificering af, om den danske tilladelse (Petrem Vet.) er et human- eller veterinærlægemiddel
- Præklinisk eller mekanistisk dokumentation for effekt på koronar vasospasme
- Vurdering af, om en anden administrationsvej eller behandlingsform er relevant, da inhalationsanæstesi ikke er egnet til kronisk brug
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

