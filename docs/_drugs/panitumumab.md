---
layout: default
title: Panitumumab
parent: Kun modelforudsigelse (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Panitumumab
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

# Panitumumab: Fra kolorektal cancer til lægemiddelinduceret osteoporose

## Resumé

Panitumumab er et monoklonalt antistof mod EGFR, der anvendes i kræftbehandling (kolorektal cancer). Dette fremgår ikke af den danske indikationstekst i datagrundlaget, som er tom, men er almen viden om lægemidlet. TxGNN-modellen forudsiger, at det kan have effekt ved **lægemiddelinduceret osteoporose**, men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter forudsigelsen. Evidensen er udelukkende modelbaseret, og en skadelig effekt kan ikke udelukkes.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de danske data (almen viden: kolorektal cancer) |
| Forudsagt ny indikation | Lægemiddelinduceret osteoporose |
| TxGNN-forudsigelsesscore | 99,13 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen (ikke) rimelig?

Der foreligger ingen detaljerede data om virkningsmekanismen i datagrundlaget. Panitumumab er et antistof mod EGFR (epidermal vækstfaktorreceptor), og dets effekt i den oprindelige indikation bygger på hæmning af EGFR-signalering i tumorceller.

EGFR-signalering menes at understøtte osteoblastaktivitet og knogleomsætning. Hæmning af EGFR sammen med de kendte bivirkninger hypomagnesæmi og hypocalcæmi i denne lægemiddelklasse kan derfor i princippet **forværre** knoglesundheden i stedet for at behandle osteoporose. Den høje score er dermed ikke understøttet af en mekanistisk forklaring.

De øvrige forudsigelser i top 10 er alle på evidensniveau L5 og har samme svage grundlag. Dubletter i listen er slået sammen:

- **Svær ikke-proliferativ diabetisk retinopati (99,05 %) og diabetisk retinopati (98,96 %):** Der findes en teoretisk rolle for EGFR i retinal angiogenese og inflammation. Panitumumab er et systemisk IgG2-antistof med begrænset øjenpenetration og kendte øjen- og hudbivirkninger. Standardbehandling (anti-VEGF, laser) er langt bedre dokumenteret.
- **Diabetisk katarakt (98,90 %), nukleær senil katarakt og kortikal katarakt (begge 98,81 %):** Der er ikke påvist nogen mekanisme. Scorerne afspejler sandsynligvis nærhed i vidensgrafen og ikke et selvstændigt signal. Et systemisk onkologisk antistof er desuden ikke realistisk til en langsomt fremadskridende tilstand, der kan behandles kirurgisk.

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Information om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103945506 | Vectibix (Amgen Europe BV) | Koncentrat til infusionsvæske, opløsning | Ikke angivet i de tilgængelige data |

Præparatet gives som injektion/infusion.

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Målrettet behandling (monoklonalt antistof mod EGFR), ikke konventionel cytotoksisk kemoterapi |
| Risiko for myelosuppression | Se produktresuméet (SmPC) |
| Emetogenicitetsklassifikation | Se produktresuméet (SmPC) |
| Monitoreringspunkter | Se produktresuméet (SmPC). Ud fra lægemiddelklassen er det relevant at overveje elektrolytter (især magnesium og calcium) samt hud- og øjenstatus. |
| Håndteringsbeskyttelse | Følg lokale retningslinjer for håndtering af onkologiske lægemidler. Se SmPC. |

---

## Sikkerhedsovervejelser

Datagrundlaget indeholder ingen registrerede advarsler, kontraindikationer eller interaktioner. Det er en mangel, som skal afhjælpes, før en sikkerhedsvurdering er mulig.

Ud fra lægemiddelklassen er følgende dog relevant for de forudsagte indikationer:

- **Hypomagnesæmi og hypocalcæmi:** Kan potentielt forværre knoglesundheden.
- **Øjen- og hudtoksicitet** (f.eks. keratitis og øjenlidelser): Taler imod anvendelse ved øjensygdomme.

Se i øvrigt det godkendte produktresumé (SmPC) for sikkerhedsinformation.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelserne er udelukkende modelbaserede (L5), uden kliniske forsøg eller litteratur. For den højest rangerede indikation, osteoporose, taler mekanismen og lægemiddelklassens kendte bivirkninger snarere imod end for en gavnlig effekt. De øvrige forudsigelser (retinopati og katarakt) har heller ingen defineret mekanisme og en uhensigtsmæssig risiko-nytte-profil.

**For at komme videre kræves følgende:**
- Danske advarsler og kontraindikationer fra Lægemiddelstyrelsens produktresumé (blokerende datamangel)
- Detaljerede data om virkningsmekanismen (f.eks. fra DrugBank)
- Den godkendte indikationstekst for Vectibix i Danmark
- Prækliniske data, der understøtter en gavnlig effekt af EGFR-hæmning ved de forudsagte sygdomme, især en afklaring af, om retningen er skadelig ved osteoporose
- En systematisk litteratur- og forsøgssøgning efter dokumentation for de forudsagte indikationer

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelomplacering kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

