---
layout: default
title: Letermovir
parent: Kun modelforudsigelse (L5)
nav_order: 490
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Letermovir: forudsagt ny indikation Vulvovaginal candidiasis (evidensniveau L5). Oprindelig indikation: Cytomegalovirusinfektion (fra vidensgrafen"
monitor_inn: "Letermovir"
predicted_indications: ["vulvovaginal candidiasis", "vulvovaginal candidiasis", "fungal infectious disease", "fungal infectious disease", "tinea nigra", "tinea nigra", "malignant catarrh", "infectious bovine rhinotracheitis", "malignant catarrh", "infectious bovine rhinotracheitis"]
---

# Letermovir
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

# Letermovir: Fra cytomegalovirusinfektion til vulvovaginal candidiasis

## Resumé i én sætning

Letermovir er et antiviralt middel, der oprindeligt anvendes mod **cytomegalovirusinfektion (CMV)**. TxGNN-modellen forudsiger, at det kan være virksomt mod **vulvovaginal candidiasis**, men der er **ingen kliniske forsøg og ingen publikationer**, der understøtter denne retning. Forudsigelsen vurderes som en sandsynlig artefakt i vidensgrafen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Cytomegalovirusinfektion (fra vidensgrafen; indikationsteksten i de danske markedsføringstilladelser er ikke angivet) |
| Forudsagt ny indikation | Vulvovaginal candidiasis |
| TxGNN-prædiktionsscore | 99,88 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

De data, der er indsamlet til denne rapport, indeholder ingen detaljeret beskrivelse af virkningsmekanismen. Letermovir er dog kendt for at hæmme CMV's DNA-terminasekompleks (pUL56/UL89/UL51). Dette kompleks er specifikt for herpesvira og har ingen kendt modpart i *Candida*-arter, som er svampe.

Der er derfor ingen troværdig mekanistisk forbindelse mellem den oprindelige indikation (en virusinfektion) og den forudsagte indikation (en svampeinfektion). Den høje score (0,999) skyldes sandsynligvis, at begge sygdomme ligger tæt på hinanden i vidensgrafens infektionsnetværk, og ikke et fælles biologisk mål.

Øvrige forudsagte indikationer følger samme mønster:

| Forudsagt indikation | Score | Vurdering |
|------|------|------|
| Svampeinfektion (fungal infectious disease) | 98,93 % | Ingen antifungal mekanisme; publikationerne handler om svampeinfektioner som komplikation ved stamcelletransplantation |
| Tinea nigra | 98,62 % | Ingen mekanistisk begrundelse; behandles effektivt med topikale midler |
| Malign katarral feber (veterinær) | 98,48 % | Konceptuelt muligt herpesvirusmål, men aktivitet mod gammaherpesvira er ikke påvist |
| Infektiøs bovin rhinotracheitis (veterinær) | 98,48 % | Aktivitet mod alphaherpesvira er ikke påvist; uden for human repurposing |

---

## Klinisk forsøgsevidens

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for vulvovaginal candidiasis.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur for vulvovaginal candidiasis.

Til orientering er der for den næstbedst rangerede forudsigelse, svampeinfektion, fundet 9 publikationer. De omhandler letermovir i forbindelse med allogen hæmatopoietisk stamcelletransplantation og undersøger, om profylakse eller samtidig brug af triazoler påvirker risikoen for svampeinfektion. De rapporterer ikke antifungal effekt. Udvalgte eksempler:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [41371495](https://pubmed.ncbi.nlm.nih.gov/41371495/) | 2026 | Kohorte | J Infect Chemother | Sammenhæng mellem letermovirprofylakse og forekomst af bakteriæmi og invasive svampeinfektioner efter allogen HCT |
| [42834112](https://pubmed.ncbi.nlm.nih.gov/42834112/) | 2026 | Kohorte | Bone Marrow Transplant | Sikkerhed ved samtidig brug af letermovir og triazoler med hensyn til risiko for invasiv svampeinfektion |
| [33195184](https://pubmed.ncbi.nlm.nih.gov/33195184/) | 2020 | Kohorte | Front Cell Dev Biol | Erfaringer fra et center med CMV-håndtering efter introduktion af letermovir |
| [32245201](https://pubmed.ncbi.nlm.nih.gov/32245201/) | 2020 | Review | J Clin Med | Opdatering om forebyggelse og håndtering af infektioner hos stamcelletransplanterede |
| [33965172](https://pubmed.ncbi.nlm.nih.gov/33965172/) | 2021 | Review | Transplant Cell Ther | Retningslinjer for infektionsprofylakse ved navlestrengsblodstransplantation |

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105938917 | Prevymis (Merck Sharp & Dohme B.V.) | Filmovertrukne tabletter | Ikke angivet i de indsamlede data |

---

## Sikkerhedsmæssige overvejelser

**Lægemiddelinteraktioner** (100 interaktioner registreret; et udpluk):

- **Alvorlige (Major):** eliglustat, naloxegol, cisaprid
- **Moderate:** hydrocortison, dexamethason, betamethason, triamcinolon, budesonid, omeprazol, lansoprazol, aprepitant, clarithromycin, pioglitazon, glimepirid, saxagliptin, chlorpropamid, acetohexamid, naldemedin, nitisinon

Derudover nævner litteraturen, at letermovir interagerer med voriconazol (induktion af CYP2C19, som sænker voriconazoleksponeringen). Det er relevant for sikkerheden, især hvis letermovir kombineres med antimykotika.

Oplysninger om advarsler og kontraindikationer er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen mangler både mekanistisk grundlag og klinisk eller litterær evidens (L5). Letermovirs mål, CMV-terminasekomplekset, findes ikke i svampe, og den høje TxGNN-score skyldes sandsynligvis en artefakt i vidensgrafen. Forudsigelserne for de veterinære indikationer ligger uden for human repurposing.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA), f.eks. fra DrugBank
- Produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen
- Præklinisk *in vitro*-evidens for aktivitet mod *Candida*-arter, før der overvejes yderligere vurdering
- Ingen videre prioritering af de forudsagte indikationer uden et uafhængigt biologisk rationale
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

