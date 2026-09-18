---
layout: default
title: Pretomanid
parent: Kun modelforudsigelse (L5)
nav_order: 359
evidence_level: L5
indication_count: 10
---

# Pretomanid
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

# Pretomanid: Fra multiresistenttuberkulos til candidosis

## Sammenfatning på en linje

> Pretomanid er en nitroimidazooxazin-antimykobakterie, brugt som en del af BPaL/BPaLM-regimet (bedaquiline, pretomanid, linezolid ± moxifloxacin) til ekstensivt lægemiddelresistente og behandlingsintolerant/ikke-responderende multiresistente pulmonal tuberkulose.
> TxGNN-modellen forudsiger, at det kan være effektivt for **candidosis**, men dette er en **ren modelforudsigelse uden understøttende kliniske forsøg eller litteratur**, og bevispakkens egen mekanistiske gennemgang markerer det som biologisk implausibelt.

---

## Hurtig oversigt

| Element | Indhold |
|--------|----------|
| Oprindelig indikation | Multiresistent/ekstensivt lægemiddelresistent pulmonal tuberkulose (som led i BPaL/BPaLM-regimet) — ikke registreret i strukturerede `taiwan_regulatory` data |
| Forudsagt ny indikation | Candidosis |
| TxGNN-forudsigelsesscore | 99.69% |
| Bevisniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markeringsgodkendelser | 0 |
| Anbefalet afgørelse | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om Pretomanids virkningsmekanisme er ikke tilgængelige i denne bevispakke (markeret som et alvorligt datahul). Baseret på kendt information er Pretomanid et nitroimidazooxazin-prodrug, der kræver aktivering af det mycobakterie-specifik deazaflavin-afhængig nitroreduktase (Ddn)/F420 kofaktorsystem for at udøve sin baktericid virkning — en vej, der er specifik for *Mycobacterium*-slægten.

*Candida*-arter besidder ikke denne Ddn/F420-aktiveringsvej, og der er ingen kendt antifungal-mekanisme for Pretomanid. Bevispakkens egen mekanistiske vurdering bemærker eksplicit, at denne forudsigelse afspejler **vidensgraf-lighed i stedet for biologisk plausibilitet**, og at den mangler en troværdig farmakologisk begrundelse.

For kontekst blev andre toprangerede TxGNN-kandidater i denne bevispakke (spedalskhed, koronar arterie-sygdom, myokardieinfarkt, ALCAPA) vurderet under den samme synsvinkel: spedalskhed har en vis mekanistisk logik på slægtniveauet (både *M. leprae* og *M. tuberculosis* er mycobakterier), men modsiges direkte af *in vitro*-beviser, der viser, at *M. leprae* er naturligt resistente over for PA-824/Pretomanid; de kardiovaskulære forudsigelser har ingen plausibel mekanisme og modsætter i stedet Pretomanids kendt QT-forlængelsesrisiko. Ingen af kandidaterne i denne pakke overholder i øjeblikket en grundlæggende mekanistisk plausibilitetsgræns.

---

## Klinisk forsøgsbeviser

I øjeblikket ingen relaterede kliniske forsøg registreret

---

## Litteraturbeviser

I øjeblikket ingen relateret litteratur tilgængelig

---

## Markedsoplysninger om Danmark

Pretomanid har i øjeblikket ingen markeringsgodkendelse i Danmark (0 licenser; markedsstatus: ikke markedsført).

---

## Sikkerhedshensyn

Venligst henvises til det godkendte produktresuméet (SmPC) for sikkerhedsoplysninger.

*Note: strukturerede `key_warnings`, `contraindications` og DDI-data var ikke tilgængelige for denne bevispakke (forespørgselsstatus: not_found). Separat henviser bevispakkens mekanistiske noter for andre forudsagte indikationer til et kendt QT-forlængelsessignal for Pretomanid — dette bør bekræftes mod SmPC før videre evaluering.*

---

## Konklusion og næste skridt

**Afgørelse: Afvent**

**Begrundelse:**
Candidosis-forudsigelsen understøttes kun af en TxGNN-similaritetsscore (L5, ingen kliniske forsøg, ingen litteratur), og bevispakkens egen mekanistiske gennemgang finder ingen plausibel antifungal-vej for et mycobakterie-specifikt prodrug. Kombineret med et Blocking-alvorlighedsdatahul på SmPC-advarsler/kontraindikationer, opfylder denne kandidat ikke tærsklen for at gå videre forbi S0.

**For at kunne gå videre er følgende nødvendigt:**
- TFDA/dansk SmPC-etiketdata (advarsler, kontraindikationer) — i øjeblikket et Blocking-datahul (DG001)
- Bekræftet virkningsmekanisme (DG001/DG002) for korrekt at kunne vurdere relevans for nogen ikke-mycobakteriel indikation
- Enhver *in vitro*- eller preklinisk evidens for Pretomanid-aktivitet mod *Candida*-arter før videre investering
- Hvis spedalskhedsignalet i stedet er af interesse, skal det bemærkes, at det modsiges direkte af eksisterende *in vitro*-resistensdata (PMID 17005816) og ville også kræve dedikeret revurdering

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

