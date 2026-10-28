---
layout: default
title: Regadenoson
parent: Kun modelforudsigelse (L5)
nav_order: 707
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-28
monitor_inn: "REGADENOSON"
predicted_indications: ["anaphylaxis", "food-dependent exercise-induced anaphylaxis", "esotropia", "pseudoallergy"]
description: "Regadenoson: forudsagt ny indikation Anafylaksi (anaphylaxis) (evidensniveau L5). Oprindelig indikation: Ikke registreret i de lokale data"
---

# Regadenoson
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

## Regadenoson: Anafylaksi (anaphylaxis)
{: .text-alpha }

## Resumé

Regadenoson er en selektiv A2A-adenosinreceptoragonist, som anvendes som diagnostisk middel ved myokardieperfusionsscintigrafi (MPI). TxGNN-modellen forudsiger, at stoffet kan have effekt ved **anafylaksi**, men der er **ingen registrerede kliniske forsøg** og **ingen publikationer**, der understøtter denne retning. Forudsigelsen hviler udelukkende på en computerberegning.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke registreret i de lokale data |
| Forudsagt ny indikation | Anafylaksi (anaphylaxis) |
| TxGNN-prædiktionsscore | 0.9985 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Hold |

Øvrige forudsagte indikationer (alle L5, alle Hold): fødeafhængig anstrengelsesudløst anafylaksi (0.9974), esotropi (0.9912) og pseudoallergi (0.9912).

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger i de indsamlede data ikke en detaljeret beskrivelse af virkningsmekanismen. Regadenoson er dog kendt som selektiv agonist ved A2A-adenosinreceptoren (ADORA2A) og binder ifølge farmakologidata også A1-, A2B- og A3-receptorer.

Aktivering af A2A-receptorer på mastceller og andre immunceller kan teoretisk dæmpe frisætningen af inflammatoriske mediatorer, hvilket giver et muligt antiallergisk rationale. Det er imidlertid en hypotese, som ikke er testet for regadenoson.

Der er væsentlige forbehold. Adenosinsignalering er kontekstafhængig, og A2A-agonisme giver vasodilatation og blodtryksfald, hvilket kan være skadeligt ved anafylaksi, hvor cirkulatorisk kollaps er den største fare. Stoffets korte halveringstid og bolusanvendelse passer desuden dårligt til akut behandling, som kræver adrenalin. Den høje score kommer fra TxGNN-modellen (deep learning) og afspejler sandsynligvis ligheder, modellen har lært mellem beslægtede sygdomme, snarere end biologisk evidens.

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnr. | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104535109 | Rapiscan (Rapidscan Pharma Solutions EU Lt) | Injektionsvæske, opløsning | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Sikkerhedsovervejelser

**Kontraindikationer fra vidensgraf (ikke produktresumétekst):** TxGNN-vidensgrafen (PrimeKG) angiver kontraindikationskanter til bl.a.:
- Hjerte-kar: hypertension, hypotension, aortastenose, mitralstenose, atrioventrikulært blok, sick sinus-syndrom, koronararteriesygdom, perikarditis, perikardieeffusion, carotisstenose
- Luftveje: astma (inkl. allergisk og intrinsic), kronisk obstruktiv lungesygdom (KOL), bronkialsygdom
- Neurologi: epilepsi, transitorisk iskæmisk anfald, vertebrobasilær insufficiens, autonome nervesystemsygdomme, Horners syndrom

Disse er modelbaserede og skal verificeres mod produktresuméet. Bemærk, at astma og hypotension er særligt relevante ved anafylaksi.

**Lægemiddelinteraktioner (moderat niveau):**
- Koffein
- Dipyridamol
- Dyphyllin
- Theophyllin
- Aminophyllin
- Oxtriphyllin

Metylxanthiner (koffein, theophyllin m.fl.) er adenosinreceptorantagonister og kan modvirke regadenosons effekt. Dipyridamol kan forstærke adenosinvirkninger.

Derudover er overfølsomhedsreaktioner rapporteret for regadenoson selv, hvilket taler for forsigtighed. Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen er udelukkende modelbaseret (L5) uden kliniske forsøg eller litteratur. Stoffets vasodilaterende og blodtryksnedsættende effekt kan desuden være direkte skadelig ved anafylaksi, og de øvrige forudsagte indikationer (især esotropi) mangler biologisk rationale.

**For at komme videre kræves:**
- Præklinisk evidens for A2A-medieret hæmning af mastcelleaktivering i relevante modeller
- Data om virkningsmekanisme (MOA) fra DrugBank
- Gennemgang af produktresuméet for advarsler og kontraindikationer (mangler i de indsamlede data)
- Vurdering af sikkerhed ved hypotension og bronkospasme i en anafylaksisammenhæng
- Afklaring af administrationsvej og dosering i forhold til den nye indikation
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

