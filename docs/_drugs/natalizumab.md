---
layout: default
title: Natalizumab
parent: Kun modelforudsigelse (L5)
nav_order: 577
evidence_level: L5
indication_count: 10
---

# Natalizumab
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

# Natalizumab: Fra Crohns sygdom og multipel sklerose til bronkitis

## Resumé

Natalizumab er et monoklonalt antistof, der oprindeligt anvendes til behandling af Crohns sygdom, inflammatorisk tarmsygdom og multipel sklerose.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **bronkitis**,
men der er i øjeblikket **ingen kliniske forsøg** og **ingen publikationer**, der understøtter denne forudsigelse. Den er udelukkende beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Crohns sygdom, inflammatorisk tarmsygdom, multipel sklerose (angivet i vidensgrafen; indikationsteksten i den danske tilladelse er tom) |
| Forudsagt ny indikation | Bronkitis |
| TxGNN-forudsigelsesscore | 99,46 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i de data, der er indsamlet til denne rapport. Natalizumab er kendt for at blokere alfa-4-integrin-medieret transport af leukocytter (hvide blodlegemer) ind i væv. Denne mekanisme er relevant ved de oprindelige indikationer, hvor betændelsesceller trænger ind i henholdsvis tarm og centralnervesystem.

Den mekanistiske tanke bag forudsigelsen er, at en reduceret rekruttering af inflammatoriske celler til luftvejsvæv teoretisk kunne dæmpe bronkitis. Der er dog hverken kliniske eller litteraturbaserede holdepunkter for dette, og lægemidlets immunsupprimerende virkning kan tværtimod øge risikoen for luftvejsinfektioner. TxGNN-scoren (0,995) er en ren beregningsmæssig forudsigelse.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig for bronkitis.

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106803822 | Tyruko (Sandoz GmbH) | Koncentrat til infusionsvæske, opløsning | Indikationstekst ikke tilgængelig |

---

## Sikkerhedsovervejelser

- **Kontraindikationer (fra vidensgrafen, ikke produktresuméet)**: Progressiv multifokal leukoencefalopati (PML).
- **Lægemiddelinteraktioner**: Der er identificeret 100 interaktioner. Blandt de vigtigste:
  - **Alvorlige (Major)**: Kortikosteroider (hydrokortison, triamcinolon, dexamethason, betamethason, budesonid, prednisolon, prednison), mercaptopurin, levamisol, trimetrexat samt radioaktive lægemidler og radioimmunoterapi (iobenguan I-131, ibritumomab tiuxetan, tositumomab).
  - **Moderate**: Naltrexon.
  - **Milde (Minor)**: Zinksalte (sulfat, acetat, gluconat, chlorid).
- **Øvrige forhold**: Immunsuppression kan øge risikoen for luftvejsinfektioner, hvilket er særligt relevant ved en luftvejsindikation.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for bronkitis bygger udelukkende på en beregningsmodel uden kliniske forsøg eller publikationer (evidensniveau L5). Den kendte PML-risiko og den immunsupprimerende virkning gør forholdet mellem fordele og risici ugunstigt for en indikation som bronkitis.

**For at komme videre kræves følgende:**
- Data om virkningsmekanismen (MOA) fra DrugBank
- Advarsler og kontraindikationer fra det danske produktresumé (SmPC)
- Præklinisk eller mekanistisk understøttelse af, at alfa-4-integrinblokade er relevant ved bronkitis
- En vurdering af infektionsrisikoen ved en luftvejsindikation

---

## Andre forudsagte indikationer (til orientering)

| Forudsagt indikation | TxGNN-score | Evidensniveau | Anbefaling | Kommentar |
|------|------|------|------|------|
| Parapsoriasis | 99,37 % | L4 | Hold | Kun én case-rapport (PMID 32470781), som beskriver en hudbivirkning, ikke en terapeutisk effekt |
| Psoriasis | 99,19 % | L4 | Forskningsspørgsmål | Modstridende litteratur: en serie på 18 patienter viser bedring (PMID 33589543), mens flere case-rapporter beskriver udløsning eller forværring |
| Svær non-proliferativ diabetisk retinopati | 99,18 % | L5 | Hold | Ingen evidens; PML-risiko gør risiko-nytte-forholdet ugunstigt |
| Akut lichenoid pityriasis | 99,04 % | L4 | Hold | Kun den samme case-rapport (PMID 32470781), som beskriver en bivirkning |
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

