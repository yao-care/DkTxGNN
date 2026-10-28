---
layout: default
title: Pseudoephedrine
parent: Kun modelforudsigelse (L5)
nav_order: 694
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-14
description: "Pseudoephedrine: forudsagt ny indikation Sygdomme i næsehulen (nasal cavity disease) (evidensniveau L4). Oprindelig indikation: Allergisk rhinitis, vasomotorisk rhinitis, faryngitis…"
monitor_inn: "pseudoephedrine"
predicted_indications: ["nasal cavity disease", "allergic urticaria"]
---

# Pseudoephedrine
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **2** stk.
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

## Pseudoefedrin: Fra allergisk rhinitis til sygdomme i næsehulen
{: .text-alpha }

## Resumé i én sætning

Pseudoefedrin er et sympatomimetikum, der oprindeligt anvendes til behandling af tilstoppet næse ved allergisk rhinitis, forkølelse og beslægtede luftvejslidelser.
TxGNN-modellen forudsiger, at lægemidlet kan være virksomt ved **sygdomme i næsehulen**, men der er **ingen registrerede kliniske forsøg** og kun **7 publikationer** (primært dyremodeller og oversigtsartikler). Forudsigelsen er i høj grad en omformulering af den eksisterende indikation snarere end en reel ny anvendelse.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Allergisk rhinitis, vasomotorisk rhinitis, faryngitis, forkølelse m.fl. (den danske indikationstekst i godkendelserne er ikke tilgængelig) |
| Forudsagt ny indikation | Sygdomme i næsehulen (nasal cavity disease) |
| TxGNN-forudsigelsesscore | 0,9975 |
| Evidensniveau | L5 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 2 af 2) |
| Antal markedsføringstilladelser | 2 (gyldige: 2) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

De data, der er indsamlet til denne rapport, indeholder ikke detaljerede oplysninger om virkningsmekanismen. Pseudoefedrin er dog et velkendt sympatomimetikum, der virker på alfa-adrenerge receptorer i næseslimhinden. Det giver vasokonstriktion og nedsat blodgennemstrømning i slimhinden og dermed aftagende næsetilstopning.

Den forudsagte indikation "sygdomme i næsehulen" er en bred kategori, der i vid udstrækning overlapper med de allerede kendte anvendelsesområder (allergisk rhinitis, vasomotorisk rhinitis, rhinitis, forkølelse og nasofaryngitis). Forudsigelsen er derfor mere en gentagelse af den eksisterende indikation end et egentligt nyt repurposing-spor.

To andre forudsigelser er svagere understøttet:
- **Allergisk urticaria** (score 0,9914, L5): Den fundne litteratur handler om antihistaminer, ikke pseudoefedrin. Urticaria er histaminmedieret, og pseudoefedrin har ingen antihistaminvirkning. Den høje score skyldes sandsynligvis kombinationspræparater (antihistamin + pseudoefedrin) og ikke et reelt terapeutisk signal.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [22794679](https://pubmed.ncbi.nlm.nih.gov/22794679/) | 2012 | Oversigtsartikel | Allergy and Asthma Proceedings | Gennemgang af ikke-allergisk rhinitis (inflammatoriske og ikke-inflammatoriske årsager) |
| [11345158](https://pubmed.ncbi.nlm.nih.gov/11345158/) | 2001 | Komparativt farmakologisk studie | American Journal of Rhinology | Sammenligning af oral og topisk afsvulmende effekt af phenylpropanolamin og d-pseudoefedrin målt ved akustisk rhinometri |
| [19769798](https://pubmed.ncbi.nlm.nih.gov/19769798/) | 2009 | Dyremodel (kat) | American Journal of Rhinology & Allergy | Loratadin og montelukast i kombination afsvulmer; d-pseudoefedrin indgik som sammenligning |
| [12962193](https://pubmed.ncbi.nlm.nih.gov/12962193/) | 2003 | Dyremodel (hund) | American Journal of Rhinology | Model for allergisk næsetilstopning hos hunde sensibiliseret med ragweed |
| [12387934](https://pubmed.ncbi.nlm.nih.gov/12387934/) | 2002 | Dyremodel (hund) | J Pharmacol Toxicol Methods | Farmakologisk karakterisering af en ikke-invasiv hundemodel for næsetilstopning |
| [11895194](https://pubmed.ncbi.nlm.nih.gov/11895194/) | 2002 | Dyremodel (hund) | American Journal of Rhinology | Akustisk rhinometri som model for næsetilstopning |
| [24492651](https://pubmed.ncbi.nlm.nih.gov/24492651/) | 2014 | Dyremodel | J Pharmacol Exp Ther | Selektive α2c-adrenerge agonister i dyremodeller for næsetilstopning |

Bemærk: Der er ingen randomiserede kontrollerede forsøg blandt de fundne publikationer. For allergisk urticaria drejer de fundne artikler sig om antihistaminer og ikke om pseudoefedrin, og de er derfor ikke medtaget som evidens.

---

## Oplysninger om det danske marked

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103985806 | Aerinaze (N.V. Organon) | Tabletter med modificeret udløsning | Ikke angivet |
| 28101715494 | Clarinase (Merck Sharp & Dohme B.V.) | Depottabletter | Ikke angivet |

Begge godkendelser er gyldige og omfatter enkeltstofpræparater i registret.

---

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer er ikke tilgængelige i de indsamlede data. Der henvises til det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

- **Sygdomme, der i videngrafen er knyttet til kontraindikation** (ikke fra produkttekst, men fra TxGNN-videngrafen): hypertension, hjertesvigt, koronarsygdom, slagtilfælde/cerebrovaskulære lidelser, epilepsi, KOL, lever- og nyresygdom, hypothyreoidea, diabetes mellitus, diabetisk ketoacidose, benign prostatahyperplasi, mavesår, inflammatorisk tarmsygdom, pancreatitis, galdeblæresygdom, koagulationsforstyrrelser, rabdomyolyse, stofmisbrug/afhængighed m.fl.
- **Lægemiddelinteraktioner:** 219 interaktioner er registreret. De viste eksempler er hovedsageligt af moderat niveau og omfatter antidiabetika (fx acarbose, glimepirid, glipizid, glibenclamid, insulinpræparater, GLP-1-agonister som exenatid og dulaglutid, SGLT2-hæmmere som dapagliflozin, empagliflozin og canagliflozin, samt alogliptin) og diethylpropion. Askorbinsyre er registreret som mindre interaktion.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om sygdomme i næsehulen overlapper i høj grad med allerede godkendte indikationer og er kun støttet af dyremodeller og oversigtsartikler (L4), uden kliniske forsøg. De øvrige forudsigelser (laryngofaryngitis, allergisk urticaria) har kun modelstøtte (L5), og urticaria-signalet skyldes sandsynligvis kombinationspræparater. Der er desuden et stort antal sygdomme med mulig kontraindikation, og de officielle sikkerhedsoplysninger mangler i de indsamlede data.

**For at komme videre kræves følgende:**
- Hentning og gennemgang af produktresuméer (SmPC) for Aerinaze og Clarinase, herunder godkendte indikationer, advarsler og kontraindikationer
- Detaljerede data om virkningsmekanismen (fx fra DrugBank)
- Afklaring af, om "sygdomme i næsehulen" repræsenterer en reel ny indikation eller blot en omformulering af eksisterende indikationer
- Humane kliniske data (kontrollerede forsøg) for enhver egentlig ny indikation
- En sikkerhedsvurdering for patienter med hjerte-kar-sygdom, hypertension og diabetes
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

