---
layout: default
title: Iopromide
parent: Kun modelforudsigelse (L5)
nav_order: 449
evidence_level: L5
indication_count: 9
monitor_inn: "iopromide"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-11-06
description: "Iopromide: forudsagt ny indikation Osteoartrose (evidensniveau L5). Oprindelig indikation: Ikke oplyst i de indsamlede data (godkendelsens indikationstekst er t…"
---

# Iopromide
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **9** stk.
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

## Iopromid: Fra kontrastmiddel til osteoartrose
{: .text-alpha }

## Resumé

Iopromid er et jodholdigt, ikke-ionisk røntgenkontrastmiddel, som markedsføres i Danmark under handelsnavnet Ultravist. Den oprindelige godkendte anvendelse fremgår ikke af de data, der er indsamlet til denne rapport. TxGNN-modellen forudsiger, at stoffet kan have effekt på **osteoartrose**, men der er **ingen kliniske forsøg** og **ingen publikationer**, der understøtter forudsigelsen.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i de indsamlede data (godkendelsens indikationstekst er tom) |
| Forudsagt ny indikation | Osteoartrose |
| TxGNN-forudsigelsesscore | 0,9953 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 4 af 4) |
| Antal markedsføringstilladelser | 4 (gyldige: 4) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger på nuværende tidspunkt ikke detaljerede data om virkningsmekanismen. Iopromid er et jodholdigt, ikke-ionisk radiografisk kontrastmiddel, der anvendes til billeddiagnostik. Stoffet har ingen kendt antiinflammatorisk eller bruskbeskyttende farmakologi.

Der er derfor ikke påvist nogen mekanistisk sammenhæng mellem stoffets kendte anvendelse og osteoartrose. Den høje score (0,9953) stammer fra TxGNN-modellen (deep learning) og kan afspejle ligheder, som modellen har lært mellem beslægtede sygdomme, ikke biologisk evidens.

Øvrige forudsigelser i datagrundlaget (reumatoid artrit, brachyolmi, akromesomel dysplasi af Hunter-Thompson-typen, brachyolmi-amelogenesis imperfecta-syndrom, alopeci, myosklerose, hæmoglobinopati og pseudoachondroplasi) har alle evidensniveau L5 og mangler ligeledes mekanistisk begrundelse. Ved hæmoglobinopati bør det bemærkes, at jodholdige kontrastmidler kan give sikkerhedsovervejelser ved visse tilstande (f.eks. seglcelleanæmi), så forudsigelsen er ikke terapeutisk understøttet.

---

## Dokumentation fra kliniske forsøg

Der er for øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er for øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101272286 | Ultravist (Bayer AB) | Injektions-/infusionsvæske, opløsning | Indikationstekst ikke tilgængelig |

Der er tale om 4 gyldige tilladelser for enkeltstofspræparater. Administration sker som injektion/infusion.

<!-- review:begin dk-lic-20261112-iopromide-1 -->

> **Rettelse ved gennemgang (2026-11-12)**: Oprindeligt stod der: "Der er tale om én gyldig tilladelse for et enkeltstofspræparat." Rettet efter Lægemiddelstyrelsens liste over godkendte lægemidler: der er 4 tilladelser for dette lægemiddel (heraf 4 enkeltstofpræparater i dataene); det tidligere antal kom fra en ældre version af dataene. De aktuelle tal står i hurtigt overblik. Kilde: [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/).

<!-- review:end dk-lic-20261112-iopromide-1 -->

---

## Sikkerhedsovervejelser

- **Lægemiddelinteraktioner**: Der er registreret 286 interaktioner i alt. De vigtigste af sværhedsgraden "Major" omfatter:
  - Metformin
  - Amphotericin B (herunder lipidkompleks, kolesterylsulfat og liposomal formulering)
  - Aminoglykosider: kanamycin, neomycin og streptomycin
  - Vancomycin og polymyxin B
  - Mesalazin, balsalazid, olsalazin og sulfasalazin
- Mannitol er registreret med sværhedsgraden "Moderate".

Oplysninger om advarsler og kontraindikationer fra produktresuméet er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen om osteoartrose er udelukkende baseret på en beregningsmæssig model uden understøttende kliniske forsøg, publikationer eller kendt virkningsmekanisme. Evidensniveauet er L5.

**For at komme videre kræves følgende:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresumé med advarsler, kontraindikationer og godkendt indikation fra Lægemiddelstyrelsen
- Prækliniske eller mekanistiske studier, der undersøger iopromid ved osteoartrose
- Vurdering af, om forudsigelsen blot er en artefakt af kontrastmidlets anvendelse ved artrografi

<!-- review:begin log -->

## Gennemgangslog

Nedenfor er gennemgangsloggen for denne side: udsagn kontrolleret mod Lægemiddelstyrelsens liste over godkendte lægemidler. Rettelser er begrænset til grundlæggende faktuelle udsagn; modelforudsigelser, evidensniveauer og konklusioner er ikke omskrevet.

| Gennemgået | Punkt | Handling | Kilde |
|------|------|------|------|
| 2026-11-12 | Antal tilladelser: “Der er tale om én gyldig tilladelse for et enkeltstofspræparat.” → “Der er tale om 4 gyldige tilladelser for enkeltstofspræparater.” | Rettet | [Lægemiddelstyrelsen: liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/) |

<!-- review:end log -->

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

