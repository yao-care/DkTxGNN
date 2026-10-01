---
layout: default
title: Sonidegib
parent: Kun modelforudsigelse (L5)
nav_order: 406
evidence_level: L5
indication_count: 10
---

# Sonidegib
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

# Sonidegib: Fra basalcellekarcinom til medulloblastom med udbredt nodularitet

> Evidence Pack'en angiver ingen original indikation. Basalcellekarcinom er den generelt kendte indikation for sonidegib som Hedgehog-hæmmer.

## Resumé i få sætninger

Sonidegib er en Hedgehog-hæmmer (SMO-hæmmer), som generelt kendes fra behandling af basalcellekarcinom.
TxGNN-modellen forudsiger, at det kan have effekt ved **medulloblastom med udbredt nodularitet**.
Forudsigelsen bygger kun på modellen: der er **0 kliniske forsøg** og **0 publikationer** i datagrundlaget.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Original indikation | Ikke angivet i de leverede data |
| Forudsagt ny indikation | Medulloblastom med udbredt nodularitet |
| TxGNN-forudsigelsesscore | 99,90 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

## Hvorfor er forudsigelsen rimelig?

Der foreligger ingen detaljerede data om virkningsmekanisme i Evidence Pack'en. Sonidegib hæmmer dog Smoothened (SMO) og blokerer dermed Hedgehog-signalvejen. Det er en kendt klasseegenskab.

Medulloblastom med udbredt nodularitet tilhører typisk SHH-undergruppen, hvor Hedgehog-signalvejen er drivende. Der er derfor et plausibelt rationale på signalvejsniveau.

Et eventuelt udbytte afhænger sandsynligvis af tumorens SHH-status, fx forandringer i SMO eller PTCH1. Scoren på 0,999 er en beregnet forudsigelse og ikke et klinisk resultat.

### Øvrige forudsigelser

Modellen foreslår yderligere fire sygdomme, alle uden kliniske forsøg eller litteratur og alle på evidensniveau L5. De er vurderet som Hold:

- **Xeroderma pigmentosum** (99,87 %): Kun en indirekte kobling via den høje forekomst af Hedgehog-drevet basalcellekarcinom. Sonidegib ville ramme hudkræften og ikke selve sygdommen.
- **Annulær epidermolytisk ichthyosis** (99,83 %): En keratinsygdom (KRT1/KRT10) uden synlig Hedgehog-/SMO-sammenhæng. Koblingen ligner en artefakt i vidensgrafen.
- **Epidermolysis bullosa simplex med spættet pigmentering** (99,79 %): En KRT5-relateret hudfragilitetssygdom uden understøttet mekanistisk kobling til SMO-hæmning.
- **Trichothiodystrofi, fotosensitiv** (99,77 %): En nukleotid-excisionsreparationssygdom uden klar Hedgehog-baseret begrundelse og uden den stærke disposition for basalcellekarcinom, der ses ved xeroderma pigmentosum.

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

## Evidens fra litteratur

Der er i øjeblikket ingen relateret litteratur tilgængelig.

## Markedsinformation i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105426514 | Odomzo (SUN Pharmaceutical Industries Europe BV) | Kapsler, hårde | Ikke angivet i de leverede data |

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (Hedgehog-/SMO-hæmmer) |
| Risiko for knoglemarvssuppression | Se produktresuméet (SmPC) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC) |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

Se SmPC's afsnit om advarsler og forsigtighedsregler.

## Sikkerhedsovervejelser

- **Klasseeffekter:** Systemisk SMO-hæmning er forbundet med kendte klassetoksiciteter, herunder muskeltoksicitet og teratogenicitet. Disse er svære at begrunde uden et stærkt mekanistisk rationale, som fx for annulær epidermolytisk ichthyosis.

Der er ikke fundet registrerede lægemiddelinteraktioner i datagrundlaget. Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændig sikkerhedsinformation, herunder advarsler og kontraindikationer.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er rent beregnet (L5) uden kliniske forsøg eller litteratur, og de manglende data om virkningsmekanisme og sikkerhed begrænser vurderingen. Medulloblastom med udbredt nodularitet har det stærkeste mekanistiske rationale og bør behandles som et forskningsspørgsmål. De øvrige forudsigelser er svagt understøttede.

**For at komme videre kræves:**
- Hent advarsler og kontraindikationer fra Lægemiddelstyrelsens produktresumé, så sikkerhedsscreeningen kan gennemføres.
- Hent data om virkningsmekanisme (MOA) fra DrugBank.
- Foretag en systematisk litteratur- og forsøgsgennemgang for sonidegib ved SHH-medulloblastom.
- Afklar relevansen af SHH-status (SMO/PTCH1) som biomarkør.
- Vurder sikkerhed hos den relevante population, især med hensyn til muskeltoksicitet og teratogenicitet.
- Afklar administrationsvej og lægemiddelform i forhold til den forudsagte indikation.

*Dette resultat er udelukkende til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser skal valideres klinisk, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

