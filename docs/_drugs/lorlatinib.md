---
layout: default
title: Lorlatinib
parent: Kun modelforudsigelse (L5)
nav_order: 270
evidence_level: L5
indication_count: 10
---

# Lorlatinib
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

# Lorlatinib: Fra ALK-positiv NSCLC til Gingival Fibromatose

## Ét-sætnings sammenfatning

Lorlatinib er en tredje generations ALK/ROS1 tyrosinkinase-hæmmer (TKI), oprindeligt udviklet til ALK-positive (og ROS1-positive) avanceret ikke-småcellet lungekræft (NSCLC). TxGNN-modellens højest rangerede forudsigelse for dette lægemiddel er **Gingival Fibromatose**, men i øjeblikket **ingen kliniske forsøg** og **ingen publikationer** støtter denne specifikke forudsigelse — det er et rent beregningsmæssigt signal (TxGNN score 99.81%) uden mekanistisk bekræftelse.

---

## Hurtig oversigt

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | ALK-positive avanceret ikke-småcellet lungekræft (NSCLC) — udledt fra evidenspakkens rationale tekst; ikke bekræftet via en formelt dansk regulatorisk registrering i denne pakke |
| Forudsagt ny indikation | Gingival Fibromatose |
| TxGNN-prognosescore | 99.81% |
| Bevisniveau | L5 (kun modelforudsigelse, ingen klinisk eller litteraturstøtte) |
| Status på det danske marked | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Afvente |

---

## Hvorfor er denne forudsigelse rimelig?

I øjeblikket er detaljerede data om virkningsmekanisme ikke tilgængelige i struktureret form (datakløft). Baseret på rationalet indlejret i denne evidenspakke er Lorlatinib kendt for at virke som en ALK/ROS1 tyrosinkinase-hæmmer, og dets effektivitet ved ALK-positiv NSCLC er velbelyst.

For denne højest rangerede forudsigelse underminerer pakkens egen analyse imidlertid direkte den mekanistiske argumentation: gingival fibromatose er patologisk drevet af SOS1-genmutationer eller bindevævsfibroseveje, som ikke har nogen kendt forbindelse til ALK/ROS1-signalering. TxGNN tildelte en meget høj lighedsscore (99.81%), men der er ingen biologisk eller klinisk begrundelse for at forbinde Lorlatinibs kendt farmakologi til denne indikation — dette er en network-embedding artefakt snarere end et underbygget genanvendelsesenal.

For transparence: denne evidenspakke indeholder også andre kandidatindikationer for Lorlatinib (lungekarcinoma ved hilum, godartede lungesvulster), som har faktisk litteratur. Disse berettiger også til forsigtighed — lungekarcinoma ved hilum understøttes kun af en enkelt kasuistik, og de 20 publikationer knyttet til "godartede lungesvulster" handler, ifølge pakkens egen annotation, udelukkende om maligne ALK-positive NSCLC (Lorlatinibs allerede godkendt indikation), hvilket tyder på en sygdomsontologi-kortlægningsfejl i TxGNN snarere end et ægte nyt indikationsenal. Ingen af denne litteratur gælder for gingival fibromatose-forudsigelsen diskuteret her.

---

## Bevis fra kliniske forsøg

I øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Bevis fra litteratur

I øjeblikket ingen tilgængelig relateret litteratur.

---

## Markedsinformation for Danmark

Lorlatinib har i øjeblikket ingen markedsføringstilladelse i Danmark (0 licenser registreret); markedsstatus er "ikke markedsført."

---

## Cytotoxicitet

| Element | Indhold |
|---------|---------|
| Cytotoxicitetsklassificering | Målrettet terapi (ALK/ROS1 tyrosinkinase-hæmmer) |
| Risiko for knoglemarvsundertrykkelse | Se venligst Produktresumé (SmPC) for advarsler og forholdsregler |
| Emetogenitetsklassificering | Se venligst Produktresumé (SmPC) for advarsler og forholdsregler |
| Overvågningselementer | Se venligst Produktresumé (SmPC) for advarsler og forholdsregler |
| Håndteringsbeskyttelse | Som oralt cytostatikum håndteles efter institutionelle forholdsregler for farlige lægemidler; se SmPC for specifikke håndteringsinstruktioner |

---

## Sikkerhedsovervejelser

Se venligst det godkendte Produktresumé (SmPC) for sikkerhedsoplysninger. (Ingen strukturerede vigtige advarsler, kontraindikationer eller lægemiddel-lægemiddel-interaktionsdata kunne hentes for denne evidenspakke; lokale etiketadvarsler er markeret som et blokeringsdatakløft.)

---

## Konklusion og næste trin

**Beslutning: Afvente**

**Begrundelse:**
Den højest rangerede forudsigelse (gingival fibromatose) har ingen klinisk forsøg eller litteraturstøtte og har, ifølge pakkens egen mekanistiske analyse, ingen plausibel biologisk forbindelse til Lorlatinibs ALK/ROS1-farmakologi — dette er et L5-signal, udelukkende fra modellen.

**For at gå videre er følgende nødvendigt:**
- Danske/lokale etiketadvarsler og kontraindikationer (i øjeblikket et blokeringsdatakløft)
- Formelle DrugBank-data for virkningsmekanisme (i øjeblikket et datakløft med høj alvorlighed)
- Præklinisk eller mekanistisk evidens, som direkte forbinder ALK/ROS1-inhibering til gingival fibromatose-patologi, før denne kandidat kan avancere forbi S0
- Løsning af den tilsyneladende TxGNN-sygdomsontologi-kortlægningsfejl, der påvirker "godartede lungesvulster"-kandidaten i samme pakke, før den kandidat bliver særskilt evalueret

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

