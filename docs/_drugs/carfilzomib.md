---
layout: default
title: Carfilzomib
parent: Kun modelforudsigelse (L5)
nav_order: 94
evidence_level: L5
indication_count: 10
---

# Carfilzomib
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

# Carfilzomib: Fra myelomatose til melanom (CMM7 og relaterede melanomformer)

## Resumé

Carfilzomib er en proteasomhæmmer, som i Danmark markedsføres som Kyprolis. Lægemidlet er kendt som behandling af myelomatose, men indikationsteksten mangler i de danske registreringsdata. TxGNN-modellen forudsiger, at det kan have effekt ved **CMM7** (en uklar melanom-relateret post) og andre melanomformer. Der er **0 kliniske forsøg** og kun **5 publikationer** bag forudsigelsen, og de er alle prækliniske eller beregningsmæssige.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske licensdata. Carfilzomib er generelt kendt som lægemiddel mod myelomatose. |
| Forudsagt ny indikation | CMM7 (rang 1, uklar betegnelse). Den bedst understøttede forudsigelse er melanom (rang 9). |
| TxGNN-forudsigelsesscore | 99,37 % (CMM7). Melanom: 99,03 %. |
| Evidensniveau | L5 for CMM7. L4 for melanom (kun prækliniske data). |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold (afvent) |

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger ingen detaljerede mekanismedata i datasættet. Ud fra almen farmakologi er carfilzomib en irreversibel hæmmer af 20S-proteasomet (kymotrypsinlignende aktivitet). Hæmning af proteasomet kan give ophobning af misfoldede proteiner og aktivere apoptose i kræftceller. Det er den mekanistiske forklaring på, at modellen kobler lægemidlet til melanomtyper.

Sammenhængen mellem myelomatose og melanom er svag. Koblingen bygger på ligheder i vidensgrafen og på den generelle tanke om, at kræftceller er følsomme over for proteasomhæmning. Der er ikke vist nogen direkte klinisk sammenhæng mellem sygdommene.

Forudsigelserne er samlet her (dubletter i inputtet er kun medtaget én gang):

| Forudsagt indikation | TxGNN-score | Evidens | Bemærkning |
|------|------|------|------|
| CMM7 | 99,37 % | L5 | Betegnelsen er uklar og bør verificeres, før der arbejdes videre. |
| Pædiatrisk leptomeningeal melanom | 99,30 % | L5 | Carfilzombs evne til at nå CNS er ikke dokumenteret, og der er ingen pædiatriske data. |
| Epiteloidcellet uvealt melanom | 99,23 % | L5 | Anden drivende biologi (fx GNAQ/GNA11) end kutant melanom, så data overføres ikke direkte. |
| Vulvamelanom | 99,19 % | L5 | Ingen stedspecifik evidens. |
| Melanom | 99,03 % | L4 | Kun prækliniske og beregningsmæssige data. |

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Litteraturen hører til forudsigelsen for **melanom**. Der er ingen litteratur for de øvrige forudsagte indikationer.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [33671902](https://pubmed.ncbi.nlm.nih.gov/33671902/) | 2021 | Præklinisk in vitro | Biology | Carfilzomib sammen med bortezomib øgede apoptose i murine B16-F1-melanomceller via aktivering af flere caspaser (3, 8, 9 og 12). |
| [36134605](https://pubmed.ncbi.nlm.nih.gov/36134605/) | 2023 | Beregningsmæssig (docking/simulering) | J Biomol Struct Dyn | Drug repurposing-studie af kemoterapeutika mod kinasemål i ti kræftformer, herunder melanom. Studiet er ikke specifikt for carfilzomib. |
| [31540997](https://pubmed.ncbi.nlm.nih.gov/31540997/) | 2019 | Præklinisk mekanistisk | Mol Cancer Res | Genet ZFAND2A (AIRAPL) regulerer cellernes overlevelse i humant melanom via E3-ligasen cIAP2. Studiet er relateret til proteasomvejen. |
| [29581547](https://pubmed.ncbi.nlm.nih.gov/29581547/) | 2018 | Præklinisk mekanistisk | Leukemia | BET-PROTAC'er var aktive i myelomatosemodeller. Studiet handler ikke om melanom, så relevansen er begrænset. |
| [27016342](https://pubmed.ncbi.nlm.nih.gov/27016342/) | 2016 | Præklinisk mekanistisk | Matrix Biol | Bortezomib og carfilzomib øgede heparanaseudtrykket via NF-κB og kan give en mere aggressiv tumorfænotype. Studiet handler om myelomatose, og fundet kan tale imod anvendelsen. |

Kun ét af de fem studier undersøger carfilzomib direkte i melanomceller, og det er et musecelle-studie. Det kan ikke dokumentere effekt eller sikkerhed hos mennesker.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| MA 28105849116 | Kyprolis (Amgen Europe BV) | Pulver til infusionsvæske, opløsning | Ikke angivet i data |

Det fremgår ikke af datasættet, om tilladelsen er national eller centraliseret (EMA). Produktet gives som infusion.

---

## Cytotoksicitet

Carfilzomib er et antineoplastisk lægemiddel. Datasættet indeholder ingen toksicitetsdata, så oplysningerne nedenfor bygger på almen farmakologisk viden og skal verificeres i produktresuméet (SmPC).

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet terapi (proteasomhæmmer) |
| Risiko for myelosuppression | Middel (trombocytopeni og neutropeni forekommer hyppigt) |
| Emetogenicitetsklassifikation | Lav |
| Monitoreringspunkter | Fuldstændigt blodbillede med differentialtælling, lever- og nyrefunktion, elektrolytter samt hjerte-kar-status |
| Beskyttelse ved håndtering | Følg gældende regler for håndtering af cytostatika |

Se i øvrigt advarsler og forsigtighedsregler i produktresuméet (SmPC).

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold (afvent)**

**Begrundelse:**
Forudsigelserne er alene modelbaserede (L5), og den bedst understøttede indikation, melanom, har kun prækliniske data (L4). Der er ingen kliniske forsøg. Sikkerhedsdata fra Lægemiddelstyrelsen mangler og blokerer den videre sikkerhedsscreening.

**For at komme videre kræves:**
- Verificering af, hvad "CMM7" dækker over i sygdomsontologien.
- Sikkerhedsoplysninger (advarsler, kontraindikationer) fra det danske produktresumé (SmPC).
- Dokumenteret oprindelig indikation og mekanismedata (MOA) fra DrugBank.
- Prækliniske data i humane melanommodeller, herunder vurdering af den mulige heraparanase-relaterede risiko for en mere aggressiv tumorfænotype.
- For uvealt og leptomeningealt melanom: data om biologiske forskelle og evne til at nå CNS.
- Forud for eventuelle kliniske forsøg: en systematisk litteratur- og forsøgssøgning.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Lægemiddelkandidater til nye anvendelser kræver klinisk validering, før de kan tages i brug.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

