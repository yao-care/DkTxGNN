---
layout: default
title: Mupirocin
parent: Kun modelforudsigelse (L5)
nav_order: 303
evidence_level: L5
indication_count: 10
---

# Mupirocin
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

# Mupirocin: Fra topisk antibakteriel behandling til pleuraempyem

## Resumé i én sætning

Mupirocin er et topisk antibiotikum, som i Danmark markedsføres som Bactroban salve.
TxGNN-modellen forudsiger, at det kan have effekt ved **pleuraempyem**, men der er **0 kliniske forsøg** og **0 publikationer** for denne indikation.
Forudsigelsen er derfor ren modelforudsigelse (evidensniveau L5).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Pleuraempyem |
| TxGNN-forudsigelsesscore | 99,49 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig (eller ikke)?

Oplysninger om lægemidlets virkningsmekanisme (MOA) er i øjeblikket ikke tilgængelige i datagrundlaget. Ud fra almen farmakologi, som ikke stammer fra de leverede data, hæmmer mupirocin bakteriens isoleucyl-tRNA-syntetase og virker primært mod grampositive kokker. Pleuraempyem skyldes ofte netop sådanne bakterier, og det kan forklare modellens høje score.

Der er dog et afgørende praktisk problem: Mupirocin er et topisk præparat (salve), og der er ingen plausibel vej for en salve til pleurahulen. Pleuraempyem behandles i praksis med systemisk antibiotika og drænage. Forholdet mellem den oprindelige og den nye indikation kan derfor ikke vurderes som understøttet, og administrationsvejens forenelighed er ikke afklaret.

Scoren er høj, men uden kliniske data eller litteratur er den ikke tilstrækkelig til at begrunde en videre udvikling.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for pleuraempyem.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur for pleuraempyem.

---

## Øvrige forudsagte indikationer

Evidenspakken indeholder flere forudsigelser (rang 1-10), hvoraf nogle er dubletter. Her er de unikke indikationer:

| Indikation | TxGNN-score | Evidensniveau | Vurdering |
|------|------|------|------|
| Pleuraempyem | 99,49 % | L5 | Kun modelforudsigelse. Topisk præparat har ingen vej til pleurahulen. |
| Punktformet epitelial keratokonjunktivitis | 99,10 % | L5 | Ingen klar rationale, da tilstanden ofte er viral eller ikke-infektiøs. |
| Neurotrofisk keratopati | 98,48 % | L5 | Nervedegeneration i hornhinden. Ingen tydelig antibakteriel mekanisme. |
| Kutan candidiasis | 98,27 % | L4 | Svag, men den eneste indikation med et direkte litteratursignal (se nedenfor). |
| Vaginal udflåd | 96,01 % | L5 | Det tilknyttede forsøg er ikke relevant (se nedenfor). |

**Kutan candidiasis** har de to publikationer, der er tættest på en reel evidens:

| PMID | År | Type | Tidsskrift | Hovedpunkter |
|------|-----|------|------|---------|
| [1678836](https://pubmed.ncbi.nlm.nih.gov/1678836/) | 1991 | Klinisk rapport (design kan ikke verificeres ud fra titlen) | Lancet | "Efficacy of mupirocin in cutaneous candidiasis". Eneste direkte signal. Der er intet abstract, så design og størrelse er ukendt. |
| [24021363](https://pubmed.ncbi.nlm.nih.gov/24021363/) | 2013 | Case-rapport | Dermatology Online Journal | Perianal og periumbilikal dermatitis hos en kvinde med gruppe G-streptokokinfektion. Kun indirekte evidens. |

Mupirocin er ikke et klassisk antimykotikum. En mulig forklaring er behandling af bakteriel samtidig infektion eller superinfektion ved intertriginøs eller perianal dermatitis, eller en beskeden direkte svampehæmmende effekt. Da mupirocin er et markedsført topisk middel med kendt sikkerhedsprofil, er et lille, velkontrolleret studie realistisk. Et sådant studie bør skelne mellem antibakteriel og antimykotisk effekt.

**Vaginal udflåd** er knyttet til ét forsøg, som ikke understøtter indikationen:

| Forsøgsnummer | Fase | Status | Inkluderede | Hovedpunkter |
|---------|------|------|------|---------|
| [NCT07142408](https://clinicaltrials.gov/study/NCT07142408) | Fase 3 | Rekrutterer | 848 | Præoperativ bakteriel dekolonisering (Hibiclens-sæbe og mupirocin i næsen) for at nedsætte postoperativ infektion ved lårbens- og underbenssår hos patienter, der opereres for hudkræft. |

Forsøget handler om en helt anden population og et andet endepunkt end vaginal udflåd. Koblingen ligner en mapping-artefakt. Fase 3-betegnelsen må **ikke** tolkes som L1-evidens for denne indikation.

---

## Information om markedet i Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Indehaver |
|---------|------|------|-----------|
| 28101502892 | Bactroban | Salve | GlaxoSmithKline Pharma A/S |

---

## Sikkerhedsovervejelser

Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Den højest rangerede forudsigelse (pleuraempyem) bygger kun på modellens score uden kliniske forsøg eller litteratur, og et topisk præparat har ingen plausibel vej til pleurahulen. Af de øvrige kandidater er kutan candidiasis (L4) den eneste med et direkte, men svagt og uverificeret, litteratursignal.

**For at komme videre kræves følgende:**
- Hent og gennemgå produktresuméet fra Lægemiddelstyrelsen for advarsler og kontraindikationer. Det er en blokerende datamangel.
- Hent oplysninger om virkningsmekanisme (MOA) fra DrugBank.
- Afklar administrationsvejens forenelighed for pleuraempyem (nuværende data: ingen).
- Skaf og vurdér fuldteksten til Lancet-rapporten fra 1991 om kutan candidiasis (PMID 1678836) for at afgøre design og stikprøvestørrelse.
- Overvej om kutan candidiasis kan formuleres som et lille, kontrolleret forskningsspørgsmål, der adskiller antibakteriel fra antimykotisk effekt.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepositionering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

