---
layout: default
title: Loperamide
parent: Kun modelforudsigelse (L5)
nav_order: 506
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Loperamide: forudsagt ny indikation Akut smitsom konjunktivitis (evidensniveau L5). Oprindelig indikation: Diarré og dysenteri (ifølge TxGNN-vidensgrafen"
monitor_inn: "loperamide"
predicted_indications: ["acute contagious conjunctivitis", "amebic dysentery", "conjunctivitis", "gastroduodenitis", "pseudomembranous conjunctivitis", "chronic follicular conjunctivitis", "conjunctival folliculosis", "serous conjunctivitis except viral", "parasitic conjunctivitis", "Angelucci syndrome"]
---

# Loperamide
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

## Loperamid: Fra diarré og dysenteri til akut smitsom konjunktivitis
{: .text-alpha }

## Resumé

Loperamid er et opioidlignende middel mod diarré, der oprindeligt bruges til behandling af diarré og dysenteri.
TxGNN-modellen forudsiger, at det kan være effektivt mod **akut smitsom konjunktivitis**, men der er **ingen kliniske forsøg** og **ingen publikationer** til støtte for denne forudsigelse.
Den høje score vurderes at skyldes et artefakt i vidensgrafen og ikke reel biologi.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Diarré og dysenteri (ifølge TxGNN-vidensgrafen; indikationstekst i de danske markedsføringstilladelser er ikke tilgængelig) |
| Foreslået ny indikation | Akut smitsom konjunktivitis |
| TxGNN-prædiktionsscore | 99,97 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 2 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger i de data, der er sammenstillet til denne rapport, ingen detaljerede oplysninger om loperamids virkningsmekanisme. Ud fra almindelig farmakologisk viden er loperamid en perifer mu-opioidreceptoragonist, der virker på de myenteriske neuroner i tarmen og nedsætter tarmmotiliteten. Det behandler symptomet diarré, ikke den underliggende infektion.

Der er ikke identificeret nogen plausibel mekanistisk forbindelse mellem denne virkning og betændelse eller infektion på øjets overflade. Den høje score skyldes sandsynligvis, at sygdomme i vidensgrafen ligger tæt på hinanden (infektiøs diarré og dysenteri), og ikke lægemiddelspecifik biologi. Dette understøttes af, at flere undertyper af konjunktivitis har identiske scorer.

De øvrige forudsigelser i rangeringen (bl.a. konjunktivitis, pseudomembranøs konjunktivitis, kronisk follikulær konjunktivitis, parasitær konjunktivitis og Angelucci syndrom) er ligeledes uden kliniske forsøg eller litteratur og uden mekanistisk grundlag. Alle er vurderet til evidensniveau L5 og anbefalingen Hold.

---

## Dokumentation fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for akut smitsom konjunktivitis.

---

## Litteraturevidens

Der foreligger i øjeblikket ingen relateret litteratur for den primære forudsigelse (akut smitsom konjunktivitis).

Til orientering er der for den næstrangerede forudsigelse, amøbedysenteri, identificeret følgende litteratur, som tyder på skade snarere end gavn:

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case report | Journal of Travel Medicine | Fulminant amøbekolitis efter kraftig brug af loperamid; langsommere tarmpassage kan have forværret forløbet (toksisk megakolon) |
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | The American Journal of Medicine | Oversigt over ikke-væskebaseret behandling og kemoprofylakse ved akut diarré |

For gastroduodenitis (rang 4) findes en case report fra 2026 ([PMID 41924411](https://pubmed.ncbi.nlm.nih.gov/41924411/), Cureus) om loperamidinduceret respirationsdepression ved svær gastrointestinal inflammation efter kemoterapi. Det er et sikkerhedssignal og ikke tegn på effekt.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101397090 | Imodium (McNeil Denmark ApS) | Tabletter | Ikke tilgængelig |
| 28103925806 | Imodium Plus (McNeil Denmark ApS) | Tabletter | Ikke tilgængelig |

---

## Sikkerhedsovervejelser

- **Kontraindikationer (fra TxGNN-vidensgrafen, ikke fra produktresuméet):** leversygdom, galdeblæresygdom, paralytisk ileus, tarmobstruktion, familiær visceral myopati, dysenteri, diarrésygdom, infektiøs diarré og infektiøs tarmsygdom.
- **Lægemiddelinteraktioner:** I alt er der registreret 842 interaktioner. Eksempler på **alvorlige (Major)** interaktioner: abirateron, ranitidin, fosamprenavir og gemfibrozil. Eksempler på **moderate** interaktioner: kodein, dihydrokodein, tramadol, ethanol, cetirizin, chlorphenamin, salbutamol og galantamin.
- **Sikkerhedssignal:** Ved svært beskadiget tarmslimhinde kan den systemiske eksponering stige, med risiko for centrale opioidvirkninger som respirationsdepression (case report fra 2026).

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige oplysninger om advarsler og kontraindikationer.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om akut smitsom konjunktivitis bygger udelukkende på en modelscore uden kliniske forsøg, litteratur eller plausibel mekanisme, og den skyldes sandsynligvis et artefakt i vidensgrafen. Der er desuden sikkerhedssignaler for loperamid ved infektiøse og inflammatoriske tilstande.

**For at komme videre kræves følgende:**
- Oplysninger om virkningsmekanisme (MOA) fra DrugBank
- Advarsler og kontraindikationer fra det danske produktresumé hos Lægemiddelstyrelsen
- Prækliniske eller mekanistiske data, der kan underbygge en rolle ved øjenoverfladesygdom
- Vurdering af, om en egnet administrationsvej (f.eks. øjendråber) overhovedet er mulig; den eneste godkendte form i Danmark er tabletter
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

