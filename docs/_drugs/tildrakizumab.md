---
layout: default
title: Tildrakizumab
parent: Kun modelforudsigelse (L5)
nav_order: 829
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-14
description: "Tildrakizumab: forudsagt ny indikation Svær ikke-proliferativ diabetisk retinopati (evidensniveau L5). Oprindelig indikation: Ikke angivet i de indsamlede data (den danske godkendelse har ingen i…"
monitor_inn: "Tildrakizumab"
predicted_indications: ["severe nonproliferative diabetic retinopathy", "severe nonproliferative diabetic retinopathy", "diabetic retinopathy", "diabetic retinopathy", "diabetic cataract", "diabetic cataract", "drug-induced osteoporosis", "drug-induced osteoporosis", "nuclear senile cataract", "cortical cataract"]
---

# Tildrakizumab
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

# Tildrakizumab: Fra psoriasis til svær ikke-proliferativ diabetisk retinopati

## Opsummering i en sætning

Tildrakizumab er et monoklonalt antistof, der hæmmer interleukin-23 (IL-23, p19-underenheden), og som er markedsført i Danmark under handelsnavnet Ilumetri. Data indeholder ingen godkendt indikationstekst for det danske produkt.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **svær ikke-proliferativ diabetisk retinopati**, men der er **0 kliniske forsøg** og **0 publikationer**, som understøtter denne retning. Forudsigelsen er udelukkende modelbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (den danske godkendelse har ingen indikationstekst) |
| Forudsagt ny indikation | Svær ikke-proliferativ diabetisk retinopati |
| TxGNN-forudsigelsesscore | 99,63 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

Bemærk: Datasættet indeholder dublerede poster for de samme forudsigelser. Disse er her samlet, så hver indikation kun nævnes én gang.

---

## Hvorfor er forudsigelsen rimelig?

Der foreligger i øjeblikket ikke detaljerede data om virkningsmekanismen i de indsamlede data. Tildrakizumab er dog kendt som et anti-IL-23 p19-antistof. IL-23/IL-17-aksen er central i visse kroniske inflammatoriske sygdomme, og lægemidlet virker ved at dæmpe denne signalvej.

Kronisk lavgradig inflammation og cytokinsignalering, herunder IL-23/IL-17-aksen, er blevet foreslået at bidrage til skade på nethindens kar ved diabetisk retinopati. Denne sammenhæng er dog spekulativ, og der er ingen direkte evidens for, at hæmning af IL-23 p19 virker ved tilstanden. Gængs behandling (anti-VEGF, laser og kortikosteroider) virker via andre mekanismer.

Den høje score (0,996) er et rent modelresultat og bør ikke tolkes som klinisk evidens.

### Øvrige forudsigelser i datasættet

| Forudsagt indikation | TxGNN-score | Evidensniveau | Vurdering |
|------|------|------|------|
| Diabetisk retinopati | 99,53 % | L5 | Muligt inflammatorisk link, men ingen direkte evidens |
| Diabetisk grå stær | 99,21 % | L5 | Biologisk usandsynlig; skyldes primært polyol-signalvej, osmotisk og oxidativ stress |
| Lægemiddelinduceret osteoporose | 99,20 % | L5 | Løs teoretisk begrundelse via IL-23/IL-17 og knoglenedbrydning; veletablerede alternativer findes |
| Nuklear senil grå stær | 98,91 % | L5 | Intet plausibelt link identificeret |
| Kortikal grå stær | 98,91 % | L5 | Intet anerkendt link til IL-23; sandsynligvis grafnærhed til andre grå stær-termer |

Alle forudsigelser har Hold som anbefaling.

---

## Dansk markedsinformation

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105927417 | Ilumetri (Almirall, S.A.) | Injektionsvæske, opløsning i fyldt injektionssprøjte | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Oplysninger om advarsler og kontraindikationer er ikke tilgængelige i de indsamlede data. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

**Lægemiddelinteraktioner:** Der er identificeret 78 mulige interaktioner. Blandt de viste er følgende af størst betydning:

- **Alvorlige (Major):** adalimumab, baricitinib, certolizumab pegol og cladribin. Der er tale om kombination med andre immunsuppressive eller immunmodulerende midler.
- **Moderate:** bl.a. roflumilast, tacrolimus, azathioprin, ciclosporin, anakinra, canakinumab, alemtuzumab, alefacept og denosumab. Der er desuden moderate interaktioner med visse vacciner (tetanustoksoid, miltbrandvaccine og levende kolera-vaccine).
- **Mindre (Minor):** zinksalte (sulfat, acetat, glukonat, chlorid).

Kun en delmængde af de 78 interaktioner indgår i de indsamlede data.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelserne støttes kun af modelscore (evidensniveau L5), uden registrerede kliniske forsøg eller litteratur. Det mekanistiske link til diabetisk retinopati er spekulativt, og for flere af de øvrige forudsigelser (grå stær) er det biologisk usandsynligt.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) og den godkendte indikationstekst fra produktresuméet
- Gennemgang af advarsler og kontraindikationer i SmPC (blokerende datahul for sikkerhedsvurdering)
- Prækliniske data eller mekanistiske studier, der understøtter en rolle for IL-23 i diabetisk retinopati
- Systematisk litteratursøgning og søgning i forsøgsregistre efter relevante studier
- Vurdering af administrationsvej, da en øjenindikation kan kræve en anden indgivelsesform end subkutan injektion
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

