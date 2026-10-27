---
layout: default
title: Hypromellose
parent: Kun modelforudsigelse (L5)
nav_order: 415
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Hypromellose: forudsagt ny indikation Hepatisk veno-okklusiv sygdom med immundefekt-syndrom (evidensniveau L5). Oprindelig indikation: Ikke angivet i de tilgængelige data (lægemiddelstyrelsens godken…"
monitor_inn: "Hypromellose"
predicted_indications: ["hepatic veno-occlusive disease-immunodeficiency syndrome", "hepatic veno-occlusive disease-immunodeficiency syndrome", "pancytopenia due to IKZF1 mutations", "pancytopenia due to IKZF1 mutations", "hepatic veno-occlusive disease", "hepatic veno-occlusive disease", "combined immunodeficiency due to CRAC channel dysfunction", "combined immunodeficiency due to CRAC channel dysfunction", "absent thumb-short stature-immunodeficiency syndrome", "absent thumb-short stature-immunodeficiency syndrome"]
---

# Hypromellose
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

## Hypromellose: Fra øjenlubrikant til hepatisk veno-okklusiv sygdom med immundefekt (modelprædiktion)
{: .text-alpha }

## Resumé

Hypromellose er et cellulosederivat, der bruges som viskositetsfremmende hjælpestof og som lubrikant i øjendråber. Det er registreret i Danmark i produktet Artelac. TxGNN-modellen forudsiger, at stoffet kan have effekt på **hepatisk veno-okklusiv sygdom med immundefekt-syndrom**, men der er **ingen kliniske forsøg og ingen publikationer**, der understøtter forudsigelsen.

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de tilgængelige data (lægemiddelstyrelsens godkendelsestekst er tom). Anvendes som øjendråber (lubrikant). |
| Foreslået ny indikation | Hepatisk veno-okklusiv sygdom med immundefekt-syndrom |
| TxGNN-prædiktionsscore | 98,3 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

Andre forudsigelser med tilsvarende høje scorer (alle L5, alle Hold):

| Forudsagt indikation | TxGNN-score |
|------|------|
| Pancytopeni på grund af IKZF1-mutationer | 98,2 % |
| Hepatisk veno-okklusiv sygdom | 98,1 % |
| Kombineret immundefekt på grund af CRAC-kanaldysfunktion | 98,0 % |
| Syndrom med manglende tommelfinger, lav vækst og immundefekt | 97,9 % |

## Hvorfor er denne forudsigelse (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanisme. Hypromellose er et farmakologisk inaktivt, cellulosebaseret hjælpestof og viskositetsmiddel, som bruges i øjenlubrikanter, tabletovertræk og kapselskaller. Stoffet optages kun ubetydeligt systemisk.

Den forudsagte sygdom er en sjælden, autosomal recessiv primær immundefekt forårsaget af SP110-mutationer. Der er ingen troværdig mekanistisk forbindelse mellem et inert hjælpestof og denne sygdom. Scoren på 0,983 er sandsynligvis drevet af netværkstopologien i vidensgrafen snarere end af biologi.

De øvrige forudsigelser mangler ligeledes et farmakologisk grundlag:
- **IKZF1-pancytopeni:** hypromellose har ingen kendt virkning på Ikaros-transkriptionsfaktoren eller bloddannelsen.
- **Hepatisk veno-okklusiv sygdom:** sygdommen skyldes endotelskade i leverens sinusoider. Hypromellose har ingen kendt endotelbeskyttende eller antikoagulerende virkning, og den etablerede behandling (defibrotid) virker via en anden mekanisme.
- **CRAC-kanaldysfunktion:** sygdommen skyldes ORAI1- eller STIM1-mutationer, som svækker calciumindstrømning i lymfocytter. Hypromellose har ingen kendt interaktion med calciumsignalering.
- **Syndrom med manglende tommelfinger:** der er tale om et ultrasjældent genetisk syndrom uden identificerbar mekanisme.

## Klinisk evidens

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur tilgængelig.

## Oplysninger om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101959797 | Artelac | Øjendråber, opløsning, enkeltdosisbeholder | Ikke angivet |

Produktet markedsføres af Bausch & Lomb Ireland Limited og har gyldig status.

## Sikkerhedsovervejelser

Der er ikke registreret interaktioner i de data, der er indsamlet til denne rapport, og vidensgrafen indeholder ingen kontraindikationer. Sikkerhedsdata fra produktresuméet mangler dog. Se det godkendte produktresumé (SPC) for sikkerhedsoplysninger.

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en grafbaseret model (evidensniveau L5). Der er hverken kliniske forsøg, litteratur eller en plausibel mekanisme, og hypromellose er et inert hjælpestof uden systemisk aktivitet. Den høje score bør ikke tolkes som et klinisk signal.

**Hvis arbejdet skal fortsættes, kræves følgende:**
- Hentning af produktresumé med advarsler og kontraindikationer fra Lægemiddelstyrelsen
- Data om virkningsmekanisme fra DrugBank
- Kritisk vurdering af, om et hjælpestof overhovedet er et relevant kandidatstof til drug repurposing
- Vurdering af administrationsvej, da kun øjendråber er markedsført, mens de forudsagte sygdomme er systemiske
- Et uafhængigt litteratur- og forsøgsstudie, før en eventuel ny vurdering
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

