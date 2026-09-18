---
layout: default
title: Metreleptin
parent: Kun modelforudsigelse (L5)
nav_order: 287
evidence_level: L5
indication_count: 10
---

# Metreleptin
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

# Metreleptin: Fra Generaliseret Lipodystrofi til Familiær Generaliseret Lentiginosis

## Resumé i en sætning

Metreleptin er et rekombinant analogon af humant leptin, godkendt i andre jurisdiktioner som leptin-erstatningsterapi for patienter med medfødt eller erhvervet generaliseret lipodystrofi.
TxGNN-modellen forudsiger, at det kan være effektivt mod **Familiær Generaliseret Lentiginosis** med en forudsigelsesscore på **99.71%**.
Der findes dog **ingen kliniske forsøg og ingen publiceret litteratur**, der understøtter denne retning, hvilket placerer denne forudsigelse på det laveste bevisniveau (L5).

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig Indikation | Generaliseret lipodystrofi (leptin-mangelerstatterterapi) |
| Forudsagt Ny Indikation | Familiær Generaliseret Lentiginosis |
| TxGNN-forudsigelsesscore | 99.71% |
| Bevisniveau | L5 |
| Danmarks Markedsstatus | Ikke markedsført |
| Antal Markedsføringstilladelser | 0 |
| Anbefalet Beslutning | Afvent |

---

## Hvorfor er Denne Forudsigelse Rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i denne evidenspakke. Baseret på kendt farmakologi er metreleptin et rekombinant methionyl-human leptin-analogon, der virker som en leptin-receptor (LEP-R) agonist. Dets primære terapeutiske rolle er at erstatte deficient endogent leptin hos patienter med generaliseret lipodystrofi, hvorved nedstrøms signalering gennem JAK2–STAT3- og PI3K–AKT-veje genoprettes for at regulere energihomeostase, insulinfølsomhed og appetit.

Familiær generaliseret lentiginosis er en sjælden genetisk lidelse karakteriseret ved udbredt kutant hyperpigmentering forårsaget af mutationer i RAS/MAPK-signaleringsveje (almindeligvis *PTPN11*). Den patologiske mekanisme er fundamentalt forskellig fra leptin-mangel: den involverer aberrant melanocyt-proliferation drevet af dårligt reguleret RAS–RAF–MEK–ERK-signalering, uden nogen etableret direkte overgang til leptin-receptor-signalering. Selvom leptin-signalering (via JAK-STAT3) og RAS/MAPK-vejkomponenter teoretisk deler nogle nedstrøms konvergenspunkter, er der ingen publiceret præ-klinisk eller klinisk evidens, der understøtter en terapeutisk forbindelse.

Den høje TxGNN-forudsigelsesscore afspejler sandsynligvis indirekte graf-nærhedseffekter inden for vidensgrafenen, hvor metreleptins forbindelser til sjælden metabolisk og genetisk syndrom-knuder får det til at klynge tæt på sjælden pigmenterings-lidelser såsom familiær generaliseret lentiginosis, gastrokutan syndrom og Moynahan-syndrom (LEOPARD-syndrom). Dette er en anerkendt begrænsning for graf-baserede forudsigelser for meget forbundne hub-knuder: scoren afspejler nettopologi snarere end en valideret mekanistisk hypotese.

---

## Evidens fra Kliniske Forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteratursevidens

I øjeblikket ingen relateret litteratur tilgængelig.

---

## Danmarks Markedsinformationer

Metreleptin er ikke i øjeblikket godkendt eller markedsført i Danmark. Ingen nationale (Lægemiddelstyrelsen) eller centraliserede (EMA) markedsføringstilladelser er registreret i dette datasæt.

> **Bemærkning for anmeldere:** Metreleptin markedsføres som **Myalepta** (handelsnavn) af Amryt Pharmaceuticals i nogle europæiske lande under EMA's centraliserede procedure for generaliseret lipodystrofi. Ordinatorer bør bekræfte nuværende EMA/Lægemiddelstyrelsen-godkendelsesstatus direkte før eventuel klinisk overvejelse.

---

## Sikkerhedshensyn

Sikkerhedsdata (vigtige advarsler, kontraindikationer og lægemiddelinteraktioner) er ikke tilgængelige i denne evidenspakke.

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformationer.

---

## Konklusion og Næste Trin

**Beslutning: Afvent**

**Begrundelse:**
Der er ingen klinisk forsøgseviddens, ingen publiceret litteratur og intet etableret mekanistisk grundlag, der forbinder metreleptin til familiær generaliseret lentiginosis. TxGNN-forudsigelsesscore på 99.71% ser ud til at afspejle indirekte vidensgraf-topologi (nærhed blandt sjælden genetisk syndrom-knuder) snarere end en biologisk plausibel genanvendelseshypotese. Lægemidlet er heller ikke godkendt i Danmark, hvilket tilføjer en yderligere regulatorisk barriere. At fortsætte uden grundlæggende evidens ville ikke være ansvarlig anvendelse af forskningsressourcer.

**For at fortsætte kræves følgende:**

- **Mekanistisk validering**: Fastslå, om der eksisterer en direkte eller indirekte overgang mellem leptin-receptor (JAK-STAT3) signalering og RAS/MAPK–melanocyt-aksen, der er impliceret i familiær generaliseret lentiginosis, ideelt gennem vejanalyse eller celle-linje-studier.
- **Udvidelse af litteratursøgning**: Gennemfør en målrettet PubMed/EMBASE-søgning med bredere MeSH-termer (f.eks. "leptin AND pigmentation", "leptin AND RAS/MAPK") for at identificere eventuel tangentiel evidens.
- **MOA-data-hentning**: Indhent fuldt DrugBank-opslag for metreleptin (DB09046) for at bekræfte virkningsmekanisme, farmakodynamiske mål og kendte off-target-interaktioner.
- **Sikkerhedsprofil-gennemgang**: Hent det fulde Produktresumé/produktetiket fra EMA eller en autoriserende myndighed for at vurdere kontraindikationer, advarsler og lægemiddelinteraktionsprofil før yderligere evaluering.
- **Regulatorisk vejvurdering**: Hvis mekanistisk plausibilitet senere etableres, konsultér Lægemiddelstyrelsen vedrørende den regulatoriske vej for et ikke-godkendt lægemiddel i Danmark (f.eks. navngivet patient / medlidende brug eller fuldstændig MA-ansøgning).
- **Genvurdering af forudsigelseskontekst**: Overvej, om TxGNN-høj-score-klyngen (familiær generaliseret lentiginosis, gastrokutan syndrom, Moynahan-syndrom) afspejler et ægte biologisk signal eller en grafartefakt — fagfællebedømmelse af vidensgraf-undergrafen omkring *LEP-R* og disse syndrom-knuder anbefales.

---

> *Denne rapport er genereret til forskningsreferencebrug alene og udgør ikke medicinsk rådgivning. Genanvendelseskandidater for lægemidler kræver klinisk validering før enhver anvendelse. Alt indhold bør gennemgås af kvalificerede sundhedsfaglige personer før enhver klinisk eller regulatorisk beslutning træffes.*

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

