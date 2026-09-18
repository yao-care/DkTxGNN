---
layout: default
title: Pembrolizumab
parent: Kun modelforudsigelse (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Pembrolizumab
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

# Pembrolizumab: Fra Onkologi (PD-1-Checkpoint-Inhibitor) til Gingivitis Fibromatosa

## Sammenfatning i én sætning

Pembrolizumab er en PD-1-immunkontrolpunkt-inhibitor, hvis etablerede biologiske kontekst (ifølge den litteratur, der er vedhæftet denne evidenspakke) er onkologi, herunder indikationer som ikke-småcellet lungecancer og urothelial carcinoma. TxGNN-modellens højest rangerede forudsigelse er **Gingivitis Fibromatosa**, men denne evidenspakke indeholder i øjeblikket **0 kliniske forsøg og 0 publikationer**, som dokumenterer forbindelsen, og modellens egen mekanistiske vurdering angiver, at der ikke er kendt biologisk sammenhæng mellem PD-1-blokering og denne tilstand.

---

## Hurtig oversigt

| Punkt | Indhold |
|-------|---------|
| Oprindelig indikation | Ikke angivet i evidenspakke (`taiwan_regulatory.licenses` og `drug.original_indications` er begge tomme; kontekstuel litteratur henviser til PD-1-checkpoint-blokering inden for onkologi, f.eks. ikke-småcellet lungecancer, urothelial carcinoma) |
| Forudsagt ny indikation | Gingivitis Fibromatosa |
| TxGNN-forudsigelsesscore | 99.40% |
| Bevisniveau | L5 (modelforudsigelse alene — ingen kliniske forsøg eller litteratur) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Bibeholder |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data for virkningsmekanisme ikke tilgængelige for Pembrolizumab i denne evidenspakke (`original_moa` er markeret som et datakløft). Baseret på de informationer, der foreligger andetsteds i pakken, er Pembrolizumab et monoklonalt antistof rettet mod PD-1-immunkontrolpunktet, med etableret onkologisk anvendelse (refererede indikationer omfatter ikke-småcellet lungecancer og urothelial carcinoma). Dets kendte virkningsmekanisme fungerer ved at blokere PD-1/PD-L1-interaktionen for at reaktivere cytotoksisk T-celle-medieret anti-tumorimmunitet.

Gingivitis fibromatosa er derimod en velgørende arveligt bindevævsforstyrrelse (ofte forbundet med gener som *SOS1*), drevet af fibroblastvækst og ekstracellulær matrixophobning. Det er ikke en ondartedhed og involverer ikke immunundvigelse fra tumor — den biologiske proces, som PD-1-checkpoint-blokering er designet til at reversere.

Evidenspakkens egen mekanistiske vurdering er eksplicit på dette punkt: den høje TxGNN-score tilskrives graf-embedding-lighed inden for vidensgrafen snarere end til nogen valideret farmakologisk eller mekanistisk sammenhæng. Ingen kliniske forsøg, litteratur eller mekanistiske studier understøtter denne kandidat, og ingen biologisk mekanisme, der forbinder PD-1-blokering med gingivitis fibromatosa-patologi, er blevet identificeret.

---

## Evidens fra kliniske forsøg

I øjeblikket er der ingen registrerede relaterede kliniske forsøg.

---

## Litteraturbevis

I øjeblikket er der ingen relateret litteratur tilgængelig.

---

## Cytotoksicitet

Pembrolizumab er et antineoplastisk middel (PD-1-immunkontrolpunkt-inhibitor) baseret på den onkologi-kontekst, der er refereret gennem hele denne evidenspakkes litteratur (f.eks. ikke-småcellet lungecancer, behandling af urothelial carcinoma).

| Punkt | Indhold |
|-------|---------|
| Cytotoksicitetsklassificering | Immunterapi (immunkontrolpunkt-inhibitor — anti-PD-1 monoklonalt antistof), ikke et konventionelt cytotoksisk middel |
| Myelosuppressionrisiko | Se venligst advarsler og forsigtighedsregler i Produktresuméet (SmPC) (ingen myelosuppressiondata i denne evidenspakke) |
| Emetogenicitetsklassificering | Se venligst advarsler og forsigtighedsregler i Produktresuméet (SmPC) (ingen emetogenicitetsdata i denne evidenspakke) |
| Overvågningspunkter | Endokrin funktion (skjoldbruskkirtel, hypofyse-binyrebark-akse) — understøttet af en kasuistik andetsteds i denne pakke, der beskriver hypofysær hypoadrenokorticism og hypothyroidisme efter immunokemoterapi; også overvågning for atypiske/hurtig progredierende mønstre ("hyperprogression"), som rapporteret i en separat kasuistikkeserie involverende pembrolizumab |
| Håndteringsbeskyttelse | Som en intravenøs onkologisk biologikum, håndter ifølge institutionelle biologikum-/onkologi-infusionsprotokoller; standardforsigtighedsregler ved cytotoksisk lægemiddelspild er ikke relevante, da pembrolizumab ikke er et konventionelt cytotoksisk middel |

---

## Sikkerhedshensyn

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsinformationer. (`safety.key_warnings`, `safety.contraindications` og `safety.ddi` er alle markeret som datakløfter i denne evidenspakke — se DG001, klassificeret som blokeringsgrad.)

---

## Konklusion og næste skridt

**Beslutning: Bibeholder**

**Begrundelse:**
Den højest rangerede forudsigelse (Gingivitis Fibromatosa) har ingen understøttende kliniske forsøg eller litteratur, og evidenspakkens egen mekanistiske vurdering angiver eksplicit, at der ikke er kendt biologisk sammenhæng mellem PD-1-checkpoint-blokering og denne tilstand. Kombineret med et datakløft med blokeringsgrad på TFDA-svarende mærkning (advarsler/kontraindikationer) og en status som "Ikke markedsført" med 0 tilladelser, er der utilstrækkelig grundlag for at fremme denne kandidat.

**For at fortsætte er følgende nødvendigt:**
- Produktmærkning advarsler og kontraindikationer (DG001, Blokeringsgrad — påkrævet før nogen S1-sikkerhedsscreening kan fortsætte)
- Verificeret virkningsmekanisme-data for Pembrolizumab (DG002)
- Enhver mekanistisk eller præklinisk evidens, der specifikt forbinder PD-1-blokering med gingivitis fibromatosa-patologi (ingen i øjeblikket identificeret)
- Bemærk: en lavere rangeret kandidat i samme evidenspakke, **Lungerodscarcinoma** (score 99.35%, Bevisniveau L4, anbefaling "Research Question"), viser væsentligt højere biologisk plausibilitet givet Pembrolizumabs kendt ikke-småcellet lungecancer-relaterede mekanisme. Dens nuværende litteraturstøtte er begrænset til to kasuistikker, der beskriver bivirkninger (ikke effektivitet) i andre kræfttyper. Det er værd at bekræfte, om dette afspejler en genuint ustuderet indikation eller et data-capture-kløft i forhold til Pembrolizumabs eksisterende omfattende Phase 3-evidens for ikke-småcellet lungecancer, før det behandles som et nyt ombrugnings-signal.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

