---
layout: default
title: Moxidectin
parent: Kun modelforudsigelse (L5)
nav_order: 301
evidence_level: L5
indication_count: 10
---

# Moxidectin
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

# Moxidectin: Fra onchocerciasis til polyklonal hyperviskøsitetssyndrom

## Resumé i en sætning

Moxidectin er et antiparasitært middel af anden generation (makrocyklisk lakton), godkendt internationalt (FDA 2018, EMA) til behandling af onchocerciasis (flodblindhed), men er for øjeblikket ikke autoriseret i Danmark.
TxGNN-modellen forudsiger, at det kan være effektivt over for **polyklonal hyperviskøsitetssyndrom** som den højest rangerede kandidat, med **0 kliniske forsøg** og **0 publikationer**, der i øjeblikket understøtter denne retning.
Alle fem unikke forudsagte indikationer på hele prognoselistenen ligger på evidensniveau **L5** — udelukkende beregningsmodeloutput — og den overordnede anbefaling for hver er **Afvente**.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Onchocerciasis (flodblindhed) — baseret på etablerede FDA/EMA-godkendelser; ingen dansk autorisation registreret |
| Forudsagt ny indikation | Polyklonal hyperviskøsitetssyndrom |
| TxGNN-prognosescore | 98,06% |
| Evidensniveau | L5 (modelprognose alene — ingen kliniske forsøg, observationsstudier eller identificeret litteratur) |
| Markedsstatus i Danmark | Ikke på markedet |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvente |

---

## Hvorfor er denne prognose rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i denne bevismappe. Baseret på etableret farmakologisk viden er moxidectin et makrocyklisk lakton (milbemycin-underklasse) antiparasitikum, som virker ved selektivt at potentialisere glutamatgestyrte kloridkanaler (GluCl) fundet udelukkende i invertebratnervesystem og muskulatur. Dette forårsager vedvarende hyperpolarisering og lammelse af parasiten (*Onchocerca volvulus*), hvilket fører til dets død. Da pattedyrets nervevæv mangler GluCl-kanaler, har stoffet et gunstigt terapeutisk indeksspil hos mennesker.

Polyklonal hyperviskøsitetssyndrom drives af patologisk overproduktion af polyklonale immunglobuliner (IgG, IgA eller IgM) fra unormalt prolifererende plasmaceller eller B-lymfocytter, hvilket resulterer i markant forhøjet serumviskositet. Den grundlæggende patologiske vej — B-celleceptorsignalering, immunglobulinklasseskift og plasmaceldifferentiering — har ingen etableret skæringspunkt med GluCl-kanalfarmakolgi. Nogle makrocykliske laktoner, herunder det tæt beslægtede ivermectin, er blevet noteret at have ikke-specifik immunomodulatoriske effekter i observationelle sammenhænge, men der er ingen beskrevet mekanistisk basis, der forbinder moxidectin til immunglobulinregulering eller B-cellebiologi i fagfællebedømt litteratur.

Den høje TxGNN-score er mest sandsynlig tilskrivelig multi-hop-grafgennemkrydsningsst ø j i vidensgraf — for eksempel en forbindelsesvej som moxidectin → kloridkanal → neuroinflamation → IL-vej → B-celleaktivering → hyperviskositet — snarere end en direkte farmakologisk forhold. Denne type fjernt-nodebartefakt er en anerkendt begrænsning af prognose for grafneuronetværk, især når intermediære sygdomsknudepunkter med høj tilslutning fungerer som utilsigtede broer.

---

## Klinisk forsøgsbevis

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturbevis

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedinformation for Danmark

Moxidectin har for øjeblikket **ingen markedsføringstilladelser i Danmark**. Hverken en national tilladelse gennem Lægemiddelstyrelsen eller en centraliseret EMA-tilladelse med dansk dækning er blevet identificeret i denne bevismappe (data cut-off: 2026-04-04). Stoffet er kommercielt tilgængeligt i andre jurisdiktioner (f.eks. moxidectin 8 mg tabletter under mærkenavnet *Moxi* i USA; *Mavenclad*-klasse EMA-godkendelse er en separat forbindelse), men har ikke opnået markedsadgang i Danmark.

Enhver klinisk brug i Danmark ville i øjeblikket kræve enten en ansøgning om navngivet patient/humanitær brug eller en fuldstændig ny markedsføringstilladelse ansøgning via EMA centraliseret procedure eller en national procedure med Lægemiddelstyrelsen.

---

## Alle unikke TxGNN-forudsagte indikationer — oversigt

Følgende tabel opsummerer alle fem unikke indikationer forudsagt af TxGNN-modellen. Alle har evidensniveau L5 og en **Afvente**-anbefaling.

| Rang | Forudsagt indikation | TxGNN-score | Evidensniveau | Mekanistisk plausibilitets-vurdering | Beslutning |
|------|---------------------|-------------|----------------|--------------------------------------|----------|
| 1 | Polyklonal hyperviskøsitetssyndrom | 98,06% | L5 | Meget lav — GluCl-kanalmodulering har ingen kendt skæring med immunglobulinsyntes eller B-cellsignalering | Afvente |
| 2 | Hyperamylasæmi | 98,06% | L5 | Meget lav — sekundær biokemisk markør (ikke en primær sygdomsenhed); pankreatisk acinøs skademekanisme uden relation til GluCl-farmakolgi | Afvente |
| 3 | Medfødt analbuminæmi | 97,90% | L5 | Meget lav — ultrasjælden genetisk lidelse (ALB-mutation, <100 tilfælde globalt); moxidectin har ingen kendt effekt på albumingenekspression eller hepatisk syntese | Afvente |
| 4 | Stafylokkal scalded skin syndrome (SSSS) | 97,83% | L5 | Svag — fjern analogi til ivermectins begrænsede antimikrobielle litteratur; ingen direkte in vitro- eller in vivo-data for moxidectin mod *S. aureus* eller eksfoliativ giftstoffer; mest eksplorativ af de fem | Afvente |
| 5 | Variola minor-infektion | 97,78% | L5 | Ikke relevant — årsagsvirus (Variola) udryddet globalt siden 1980; naturlig infektion umulig; klinisk undersøgelse etisk og praktisk ikke mulig | Afvente |

---

## Sikkerhedsovervejelser

Se venligst det godkendte produktresumé (SmPC) — FDA-receptinformation eller EMA-produktinformation — for fuldstændig sikkerhedsinformation, herunder advarsler, forholdsregler og kontraindikationer.

> **Bemærkning for danske recepitorer:** Der er ingen dansk SmPC tilgængelig, da moxidectin ikke er autoriseret i Danmark. FDA-godkendt etiket (2018) og eventuelle EMA-evalueringsrapporter er de relevante referencedokumenter. Nøgleadvarsler i den godkendte etiket omfatter neurologiske bivirkninger (svimmelhed, søvnighed, tremor) og risiko for behandling efter reaktioner hos patienter med høj *Onchocerca volvulus* mikrofilariekbyrde (Mazzotti-lignende reaktioner).

---

## Konklusion og næste trin

**Beslutning: Afvente**

**Begrundelse:**
Alle fem TxGNN-forudsagte indikationer ligger på det laveste bevisslag (L5 — beregningsignal alene), med nul understøttende kliniske forsøg, observationsstudier eller fagfællebedømt publikationer identificeret på tværs af alle forespurgte datakilder (ClinicalTrials.gov, ICTRP, PubMed). De mekanistiske forbindelser mellem moxidectins etablerede GluCl-kanalfarmakolgi og de forudsagte sygdomsområder er enten fraværende (polyklonal hyperviskøsitet, hyperamylasæmi, medfødt analbuminæmi, variola minor) eller i bedste fald svagt teoretisk (stafylokkal scalded skin syndrome). Moxidectin er endvidere ikke autoriseret i Danmark, hvilket tilføjer en væsentlig regulatorisk barriere til enhver klinisk anvendelse.

**For at fortsætte er følgende nødvendigt:**

- **MOA-bekræftelse:** Hent fuld mekanistisk profil fra DrugBank (DB11431) for at muliggøre formel mekanisme-til-indikationskortlægning
- **SmPC-sikkerhedsgennemgang:** Download og fortolk FDA-receptinformationen og EMA-videnskabelig diskussions-dokumenter for at udfylde advarsler, kontraindikationer og lægemiddelinteraktionsdata (for øjeblikket alle markeret som datagab)
- **Præ-klinisk mulighedsvurdering:** For stafylokkal scalded skin syndrome specifikt — den eneste indikation med et svagt teoretisk grundlag — inden for målrettet in vitro antimikrobiel aktivitetsstudier for moxidectin mod *S. aureus* og eksfoliativ toksinstof ET-A/ET-B-hæmning før yderligere investering
- **KG-revision:** Gennemgå vidensgraf-kantstier, der genererer disse prognoser, for at identificere og filtrere multi-hop-støjartefakter; det identiske rangeringsmønster (ranger 1&4, 2&3, 5&6, 7&8, 9&10 identisk) foreslår en systematisk scoringsartefakt, der kræver teknisk gennemgang
- **Regulatorisk vejkortlægning:** Hvis nogen indikation avancerer til pre-klinisk fase, start en regulatorisk pre-submission-møde med Lægemiddelstyrelsen eller EMA for at definere autoriseringsvej for Danmark
- **Variola minor:** Fjern fra aktiv overvejelse — klinisk undersøgelse er ikke mulig for en udryddet patogen; behold kun til historisk dokumentation

---

*Denne rapport er genereret til forskningsformål alene og udgør ikke medicinsk rådgivning. Alle kandidater til lægomvendelse kræver stringent klinisk validering før enhver terapeutisk anvendelse. Rapport genereret: 2026-04-04. Beviscut-off: 2026-04-04.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

