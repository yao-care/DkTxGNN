---
layout: default
title: Tislelizumab
parent: Kun modelforudsigelse (L5)
nav_order: 440
evidence_level: L5
indication_count: 10
---

# Tislelizumab
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

# Tislelizumab: Fra kræftbehandling (anti-PD-1) til blandet type autoimmun hæmolytisk anæmi

## Resumé i få sætninger

Tislelizumab er et anti-PD-1-antistof, der markedsføres i Danmark som Tevimbra og bruges til kræftbehandling. TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **blandet type autoimmun hæmolytisk anæmi**. Der er **ingen kliniske forsøg og ingen publikationer** til støtte for forudsigelsen. Mekanismen peger desuden mere mod skade end mod gavn.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Forudsagt ny indikation | Blandet type autoimmun hæmolytisk anæmi |
| TxGNN-forudsigelsesscore | 93,8 % |
| Evidensniveau | L5 (kun modelforudsigelse) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede data om virkningsmekanismen i den foreliggende datapakke mangler. Tislelizumab er et anti-PD-1-antistof, der blokerer PD-1-receptoren og dermed øger T-cellernes aktivitet mod tumorer.

Autoimmun hæmolytisk anæmi er en immunmedieret sygdom, hvor kroppens eget immunsystem nedbryder de røde blodlegemer. Autoimmun hæmolytisk anæmi er en kendt immunrelateret bivirkning ved PD-1-blokade. Lægemidlet er derfor mere sandsynligt en mulig *årsag* til tilstanden end en behandling af den. Forudsigelsen afspejler sandsynligvis nærhed mellem immunrelaterede knuder i vidensgrafen og ikke et reelt terapeutisk signal.

De øvrige topforudsigelser peger i samme retning:

- **Idiopatisk aplastisk anæmi** (93,8 %): sygdommen er T-cellemedieret knoglemarvssvigt. Yderligere T-celleaktivering er mekanistisk kontraproduktivt, og knoglemarvstoksicitet er rapporteret som en immunrelateret bivirkning ved checkpoint-hæmmere.
- **Dermatitis** (93,7 %): litteraturen handler næsten udelukkende om hudbivirkninger forårsaget af tislelizumab, ikke om behandling.
- **Paroksysmal nattlig hæmoglobinuri** (93,7 %): sygdommen er komplementmedieret og skyldes PIGA-mutationer. Der er ingen kendt mekanistisk forbindelse til PD-1-blokade.
- **Lægemiddelinduceret autoimmun hæmolytisk anæmi** (93,7 %): checkpoint-hæmmere er selv rapporterede udløsere af immunmedieret hæmolyse.

---

## Klinisk evidens

Der er aktuelt ingen relaterede kliniske forsøg registreret for den forudsagte indikation.

(For dermatitis er der fundet ét forsøg, [NCT07190027](https://clinicaltrials.gov/study/NCT07190027), fase 1/2, ikke rekrutterende endnu, 246 deltagere. Det undersøger individualiseret timing af immunkemoterapi ved fremskreden ikke-småcellet lungekræft og er ikke et behandlingsforsøg for dermatitis. Det giver ingen virkningsevidens.)

---

## Litteraturevidens

Der er aktuelt ingen relateret litteratur for den forudsagte indikation.

(Litteraturen fundet for dermatitis er hovedsageligt bivirkningsrapporter, fx [40491908](https://pubmed.ncbi.nlm.nih.gov/40491908/), en FAERS-disproportionalitetsanalyse fra 2025, og [37909927](https://pubmed.ncbi.nlm.nih.gov/37909927/), en litteraturanalyse af kutane bivirkninger ved tislelizumab fra 2024. Den understøtter ikke repurposing.)

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28106750222 | Tevimbra (BeOne Medicines Ireland Limited) | Koncentrat til infusionsvæske, opløsning | – |

---

## Cytotoksicitet (antineoplastisk lægemiddel)

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Immunterapi (anti-PD-1 monoklonalt antistof), ikke konventionelt cytotoksisk |
| Risiko for knoglemarvssuppression | Lav som direkte effekt. Hæmatologiske immunrelaterede bivirkninger er dog rapporteret, fx agranulocytose |
| Emetogenicitetsklassifikation | Lav |
| Monitoreringspunkter | Fuldt blodbillede, lever- og nyrefunktion, skjoldbruskkirtelfunktion, hudkontrol |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) |

---

## Sikkerhedsovervejelser

Der er ikke fundet registrerede lægemiddelinteraktioner i de foreliggende data. Litteraturen beskriver følgende alvorlige immunrelaterede bivirkninger ved tislelizumab:

- **Svære hudreaktioner**: Stevens-Johnsons syndrom/toksisk epidermal nekrolyse (SJS/TEN), DRESS-syndrom og psoriasiform dermatitis.
- **Hæmatotoksicitet**: agranulocytose er beskrevet i et case report.

For fuld sikkerhedsinformation, kontraindikationer og advarsler henvises til det godkendte produktresumé (SmPC) fra Lægemiddelstyrelsen.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen bygger udelukkende på en modelscore uden kliniske forsøg eller litteratur. Tislelizumabs mekanisme (øget T-celleaktivitet) og de rapporterede immunrelaterede bivirkninger, herunder hæmolyse og knoglemarvspåvirkning, taler imod en terapeutisk effekt.

**For at komme videre kræves:**
- Hentning og gennemgang af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer) til sikkerhedsscreening
- Detaljerede data om virkningsmekanisme (MOA) fra DrugBank
- Præklinisk eller mekanistisk evidens, der kan modsige den formodede skadelige effekt, før yderligere vurdering overvejes

*Disse resultater er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Repurposing-kandidater kræver klinisk validering før anvendelse.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

