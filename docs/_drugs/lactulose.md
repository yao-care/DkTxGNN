---
layout: default
title: Lactulose
parent: Kun modelforudsigelse (L5)
nav_order: 253
evidence_level: L5
indication_count: 10
---

# Lactulose
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

# Lactulose: Fra etableret brug som laxativum til obstruktiv ikterus

## Resumé på én sætning

Lactulose er et syntetisk, ikke-absorberbar disaccharid med længe etableret brug som osmotisk laxativum og ved hepatisk encefalopati. Blandt fem kandidat-indikationer genereret af TxGNN-modellen, **obstruktiv ikterus** er den eneste med troværdig understøttende evidens — **1 klinisk forsøg** og **20 publikationer**, herunder én multicenter RCT — mens modellens toprangerede kandidater (akut urat-nefropati, nyresten) blev vurderet af den underliggende evidens-pipeline som manglende enhver plausibel mekanistisk forbindelse og er sandsynligvis statistisk støj.

> **Bemærkning om kandidat-valg**: Evidenspakken returnerede fem forskellige sygdomskandidater (med duplikerede rækker). To af dem — *akut urat-nefropati* og *nyresten* — har nul kliniske forsøg, nul litteratur, og er eksplicit markeret i kildedata som manglende "ingen identificerbar mekanistisk forbindelse" / "sandsynligvis forudsigelsestøj." Denne rapport fokuserer derfor på **obstruktiv ikterus**, kandidaten med den stærkeste og mest tolkelig evidensbasis. *Galdevejssygdom* og *bilieledssygdom* er relateret men svagere, indirekte udvidelser af samme signal og er kort opsummeret for kontekst.

---

## Hurtig oversigt

| Punkt | Indhold |
|------|---------|
| Original indikation | Ikke dokumenteret i denne evidenspakke (ingen `taiwan_regulatory.licenses` poster). Lactulose er generisk etableret til kronisk obstipation og hepatisk encefalopati. |
| Forudsagt ny indikation | Obstruktiv ikterus |
| TxGNN-forudsigelsesscore | 99.53% |
| Evidensniveau | L3 (observationel / kohorte-evidens, inkl. én multicenter RCT med blandet replikering) |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afhold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede virkningsmekanisme-data er ikke tilgængelige i denne evidenspakke (`original_moa: [Data Gap]`). Baseret på etableret farmakologisk viden er lactulose et ikke-absorberbart disaccharid (osmotisk laxativum-klasse), der når kolon stort set uabsorberet, hvor det fermenteres af kolonale bakterier til kortkædede fedtsyrer. Dette forsyrler kolonium-lumen og undertrykker urease-producerende flora, hvilket reducerer ammoniakproduktion i kolonium og absorption af ammoniak og bakteriel endotoxin — den samme mekanisme, der ligger til grund for dens etablerede rolle ved hepatisk encefalopati.

Ved obstruktiv ikterus fører mangel på galtes salte i tarmen til nedsat funktion af tarmslimhindelbarrieren, hvilket prædisponerer patienter til bakteriel translokation og endotoksæmi. Denne endotoxin-belastning er impliceret i postoperative komplikationer, herunder nyrefunktionsnedsættelse efter galekanalkirurgi. Det foreslåede link — lactulose reducerer tarmstammende endotoxin-absorption for at mindske denne kaskade — er mekanistisk sammenhængende og er ikke blot en statistisk artefakt af indlejringsrummet, i modsætning til akut urat-nefropati og nyresten-kandidaterne, som ikke har nogen plausibel farmakologisk forbindelse til lactulose's virkemåde.

Imidlertid testede den stærkeste disponible evidens (en 1991 multicenter RCT, se nedenfor) lactulose som et **perioperativt nyrebeskyttelses-hjælpestof** hos gulsotramte kirurgiske patienter, ikke som behandling af obstruktiv ikterus i sig selv. En 1997 oversigt (Vogt & Frey) bemærker eksplicit, at denne nyrebeskyttende effekt "ikke er blevet påvist endegyldigt" i kliniske studier, og et 1989 dyreforsøg (Shibayama) fandt, at lactulose **ikke** forhindrede galekanalings-induceret hepatisk skade. Evidensbasis er derfor virkelig men blandet, understøttende en forskningsmæssig hypotese snarere end en bekræftet terapeutisk effekt.

---

## Evidens fra kliniske forsøg

| Forsøgsnummer | Fase | Status | Rekruttering | Vigtigste resultater |
|----------|------|--------|------|---------|
| [NCT01090193](https://clinicaltrials.gov/study/NCT01090193) | Fase 4 | Afsluttet | 20 | Observationel histopatologisk undersøgelse af nyre-ændringer ved akut obstruktiv ikterus; tester **ikke** lactulose som intervention — giver kun baggrund for sygdomsmekanisme. |

---

## Evidens fra litteraturen

| PMID | År | Type | Tidsskrift | Vigtigste resultater |
|------|-----|------|------|---------|
| [2032107](https://pubmed.ncbi.nlm.nih.gov/2032107/) | 1991 | RCT (multicenter) | Br J Surg | 102 patienter, der undergik kirurgi for obstruktiv ikterus, blev randomiseret til lactulose, galtes salte eller kontrol for at forhindre postoperativ nyrefunktionsnedsættelse. |
| [3768644](https://pubmed.ncbi.nlm.nih.gov/3768644/) | 1986 | Kohorte/Eksperimentel | Br J Surg | Oralt lactulose reducerede perioperativ portal og postoperativ systemisk endotoksæmi hos kirurgiske patienter med obstruktiv ikterus (P<0.05). |
| [12957136](https://pubmed.ncbi.nlm.nih.gov/12957136/) | 2003 | Kohorte/Oversigt | J Surg Res | Lactulose evalueret i en kanin-galekanalings-ligerings-model for at forhindre systemisk endotoksæmi efter obstruktiv ikterus-kirurgi. |
| [15782993](https://pubmed.ncbi.nlm.nih.gov/15782993/) | 2005 | Kohorte | Hepatogastroenterology | Argumenterer for, at præoperativ hydrering plus lactulose er nødvendig for at forhindre postoperativ nyrefunktionsnedsættelse ved akut obstruktiv ikterus-kirurgi. |
| [9145459](https://pubmed.ncbi.nlm.nih.gov/9145459/) | 1997 | Oversigt | Scand J Gastroenterol Suppl | Bemærker, at den hypoteserede nyrebeskyttende effekt af lactulose ved obstruktiv ikterus-kirurgi "ikke er blevet påvist endegyldigt" i kliniske studier. |
| [12598962](https://pubmed.ncbi.nlm.nih.gov/12598962/) | 2002 | Dyreforsøg | Pediatr Surg Int | Melatonin + lactulose reducerede lever-/nyre-histopatologisk skade hos rotter med galekanalings-ligation. |
| [2311978](https://pubmed.ncbi.nlm.nih.gov/2311978/) | 1990 | In vitro | Gut | Lactulose hemmede endotoxin-induceret TNF-produktion af monocytter, et foreslået mekanistisk grundlag for dets effekt. |
| [2614579](https://pubmed.ncbi.nlm.nih.gov/2614579/) | 1989 | Dyreforsøg | J Pathol | Negativt fund: lactulose forhindrede **ikke** galde-infarktion eller transaminase-stigning hos galekanalings-ligerede rotter. |
| [23297639](https://pubmed.ncbi.nlm.nih.gov/23297639/) | 2012 | Kohorte | Zh Mikrobiol Epidemiol Immunobiol | Kombineret galekanalings-dekompression + lactulose studeret for intestinal mikro-økologi ved mekanisk ikterus. |
| [29428098](https://pubmed.ncbi.nlm.nih.gov/29428098/) | 2018 | Oversigt | HBPD Int | Generel oversigt over patofysiologi ved obstruktiv ikterus og perioperativ styring (baggrund, ikke lactulose-specifik). |

---

## Markedsinformation for Danmark

Lactulose er i øjeblikket **ikke markedsført** i Danmark under denne evidenspakke (`market_status: Not marketed`, 0 markedsføringstilladelser på fil). Ingen Laegemiddelstyrelsen eller EMA-centraliseret godkendelse-registreringer blev fundet.

---

## Sikkerhedsovervejelser

Ingen sikkerhedsdata (vigtige advarsler, kontraindikationer eller lægemiddelinteraktioner) er i øjeblikket tilgængelige i denne evidenspakke — dette er markeret som et **blokerende** datahul (DG001), der forhindrer indgang til det indledende sikkerhedsvurderingsstadium.

> Se venligst de godkendte Produktoplysninger (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste trin

**Beslutning: Afhold**

**Begrundelse:**
- Den mekanistiske begrundelse for obstruktiv ikterus er sammenhængende (endotoxin-reduktion via tarmflora-modulering) og understøttet af én multicenter RCT, men det forsøg testede et perioperativt nyrebeskyttelses-slutpunkt snarere end behandling af obstruktiv ikterus i sig selv, og en efterfølgende oversigt og et dyreforsøg fandt effekten inkonsistent eller fraværende.
- Lactulose har ingen nuværende markedsføringstilladelse i Danmark, og sikkerhed/etiket-data (advarsler, kontraindikationer, lægemiddelinteraktioner) er helt utilgængeligt — et blokerende hul for nogen S1 sikkerhedsvurdering.

**For at fortsætte er følgende nødvendig:**
- TFDA/SmPC-niveau advarsler, kontraindikationer og lægemiddelinteraktions-data (DG001, blokering)
- Bekræftet virkningsmekanisme-dokumentation (DG002)
- En direkte klinisk evaluering af lactulose som terapi for obstruktiv ikterus (ikke blot som et perioperativt nyrebeskyttelses-hjælpestof)
- Vurdering af vej til dansk/EU markedsføringstilladelse, givet at lægemidlet i øjeblikket er uregistreret på dette marked

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

