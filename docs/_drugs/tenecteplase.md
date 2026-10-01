---
layout: default
title: Tenecteplase
parent: Kun modelforudsigelse (L5)
nav_order: 426
evidence_level: L5
indication_count: 10
---

# Tenecteplase
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

# Tenecteplase: Fra fibrinolyse (oprindelig indikation ikke angivet i data) til posterolateralt myokardieinfarkt

## Resumé

Tenecteplase er et fibrinspecifikt trombolytisk lægemiddel, som i Danmark er markedsført som Metalyse. Datapakken indeholder ingen registreret oprindelig indikation.
TxGNN-modellen forudsiger, at lægemidlet kan have effekt ved **posterolateralt myokardieinfarkt** (score 99,87 %), men der er **0 kliniske forsøg** og **0 publikationer** specifikt for denne undergruppe.
Forudsigelsen skyldes sandsynligvis en overlapning med den kendte brug ved myokardieinfarkt og er ikke en reel ny indikation.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i data (godkendt indikationstekst er tom i Lægemiddelstyrelsens data) |
| Forudsagt ny indikation | Posterolateralt myokardieinfarkt |
| TxGNN-prædiktionsscore | 99,87 % |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen (MOA) er ikke tilgængelige i datapakken. Tenecteplase er et fibrinspecifikt plasminogenaktivatorprotein, der opløser blodpropper. Det er den patofysiologi, som ligger bag akut koronar okklusion.

Posterolateralt myokardieinfarkt er en anatomisk undertype af myokardieinfarkt. Fibrinolytika er allerede etableret ved ST-elevationsinfarkt (STEMI). Den høje score afspejler derfor sandsynligvis en relation i vidensgrafen til det overordnede begreb "myokardieinfarkt" og ikke en ny terapeutisk anvendelse. Den oprindelige indikation og MOA mangler i inputtet og bør afklares først, så man kan afgøre, om der reelt er tale om "repurposing" eller om en allerede godkendt anvendelse.

### Øvrige forudsagte indikationer i datapakken

Datapakken indeholder yderligere fire unikke forudsigelser (dubletter er slået sammen):

| Forudsagt indikation | Score | Evidensniveau | Vurdering |
|------|------|------|------|
| Posteroinferiort myokardieinfarkt | 99,87 % | L5 | Samme begrundelse som posterolateralt MI. Ingen undergruppespecifik evidens. |
| Septalt myokardieinfarkt | 99,85 % | L4 | Kun indirekte litteratur (lungeemboli, der efterlignede septalt MI). |
| Medfødt koronararterieanomali | 99,61 % | L4 | Svag mekanistisk sammenhæng. Eneste rapport beskriver mislykket fibrinolyse ved spontan koronardissektion. Fibrinolyse kan indebære risiko ved dissektion. |
| Koronar stenose | 99,53 % | L2 | Eneste indikation med et randomiseret forsøg (Fase 2). Se nedenfor. |

---

## Klinisk evidens

Der er på nuværende tidspunkt ingen relaterede kliniske forsøg registreret for posterolateralt myokardieinfarkt.

For en anden forudsagt indikation (koronar stenose) findes ét forsøg:

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00604695](https://clinicaltrials.gov/study/NCT00604695) | Fase 2 | Afsluttet | 40 | Randomiseret forsøg med lavdosis intrakoronar tenecteplase under primær PCI ved STEMI (ICE T). Formålet var foreløbige angiografiske data om effekten. Forsøget løb fra 2008-07 til 2011-11. |

Forsøgets population er STEMI-patienter i primær PCI, og administrationsvejen er intrakoronar og ikke den almindelige intravenøse, så relevansen for koronar stenose er kun delvis. Der er ikke angivet EudraCT-numre i datapakken.

---

## Litteraturevidens

Der er på nuværende tidspunkt ingen relateret litteratur for posterolateralt myokardieinfarkt.

Udvalgt litteratur for øvrige forudsagte indikationer:

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [31870492](https://pubmed.ncbi.nlm.nih.gov/31870492/) | 2020 | Klinisk forsøg (gennemførlighed/sikkerhed) | Am J Cardiol | ICE T-TIMI 49: 40 PPCI-patienter randomiseret til intrakoronar tenecteplase 4 mg (n=20) eller saltvand. Vurderer gennemførlighed og sikkerhed. (Koronar stenose) |
| [16053952](https://pubmed.ncbi.nlm.nih.gov/16053952/) | 2005 | Forsøg (type ikke klassificeret) | J Am Coll Cardiol | CAPITAL AMI: tenecteplase-faciliteret angioplastik versus tenecteplase alene ved højrisiko-STEMI. Resultater fremgår ikke af datapakken. (Koronar stenose) |
| [16139127](https://pubmed.ncbi.nlm.nih.gov/16139127/) | 2005 | Case-serie | J Am Coll Cardiol | Intrakoronar fibrinspecifik trombolyse som hjælp til perkutan rekanalisering af kronisk total okklusion. (Koronar stenose) |
| [23975441](https://pubmed.ncbi.nlm.nih.gov/23975441/) | 2014 | Oversigt/serie | J Thromb Thrombolysis | Effekt og sikkerhed af vægtjusteret tenecteplase hos 30 patienter med akut lungeemboli. (Septalt MI, indirekte) |
| [18183355](https://pubmed.ncbi.nlm.nih.gov/18183355/) | 2009 | Case-rapport | J Thromb Thrombolysis | Massiv lungeemboli, der efterlignede septalt MI, behandlet med tenecteplase. (Septalt MI, indirekte) |
| [32854905](https://pubmed.ncbi.nlm.nih.gov/32854905/) | 2021 | Case-rapport | Ann Cardiol Angeiol | Spontan koronardissektion hos ung mand med STEMI, hvor fibrinolyse var mislykket og blev kompliceret af kardiogent shock. (Medfødt koronaranomali) |

---

## Markedsinformation for Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28103119499 | Metalyse (Boehringer Ingelheim Int. GmbH) | Pulver og solvens til injektionsvæske, opløsning | Ikke angivet i data |

---

## Sikkerhedsovervejelser

Der findes ingen registrerede interaktioner i datapakken. Oplysninger om advarsler og kontraindikationer er ikke tilgængelige. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Fibrinolytika er i øvrigt forbundet med blødningsrisiko. Det bør vurderes specifikt ved brug i nye populationer eller ved ændret administrationsvej, fx intrakoronar.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen for posterolateralt myokardieinfarkt har kun modelstøtte (L5) uden undergruppespecifikke forsøg eller publikationer. Den er sandsynligvis en overlapning med den kendte brug ved myokardieinfarkt og ikke en reel ny indikation. Sikkerhedsscreening kan ikke gennemføres, fordi oplysninger fra Lægemiddelstyrelsens produktresumé mangler (blokerende datamangel).

**For at komme videre kræves:**
- Hente og indlæse produktresuméet fra Lægemiddelstyrelsen (advarsler, kontraindikationer, godkendt indikation).
- Hente virkningsmekanisme (MOA) fra DrugBank.
- Afklare den oprindelige godkendte indikation og vurdere, om posterolateralt og posteroinferiort MI allerede er dækket af den eksisterende indikation.
- For koronar stenose (L2): bekræfte ICE T-forsøgets primære endepunkter og blødningsresultater samt afgrænse populationen præcist. Der foreligger ingen Fase 3-data.

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Kandidater til lægemiddelrepurposing kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

