---
layout: default
title: Metode
nav_order: 91
permalink: /methodology/
description: "Sådan producerer og validerer DkTxGNN sine forudsigelser: forudsigelse med TxGNN-videngraf, evidensindsamling, gradering fra L1 til L5 og beslutningsanbefalinger."
---

# Metode

<div class="key-takeaway">
Fra AI-forudsigelse til evidensgradering — hver kandidat har et sporbart grundlag for sin vurdering.
</div>

---

## Samlet pipeline

<p class="key-answer" data-question="Hvordan producerer DkTxGNN sine forudsigelser?">
Platformen anvender en pipeline i fire trin: TxGNN-videngrafmodellen forudsiger potentielle
associationer mellem lægemiddel og sygdom, derefter indsamles der automatisk evidens for hvert forudsagt par,
evidensen graderes fra L1 til L5, og til sidst udstedes en beslutningsanbefaling.
</p>

<ol class="actionable-steps">
<li><strong>TxGNN-forudsigelse</strong>: relationer mellem lægemiddel og sygdom forudsiges med en videngraf kombineret med grafbaserede neurale netværk.</li>
<li><strong>Evidensindsamling</strong>: for hvert forudsagt par indsamles evidens fra ClinicalTrials.gov, PubMed, DrugBank og DKMA.</li>
<li><strong>Evidensgradering</strong>: gradering fra L1 til L5, hvor L1 er stærkest (flere fase 3-RCT'er) og L5 kun er en modelforudsigelse.</li>
<li><strong>Beslutningsanbefaling</strong>: Go, Proceed, Consider, Explore eller Hold, baseret på evidensniveauet.</li>
</ol>

---

## Kriterier for evidensgradering

<table class="comparison-table">
<thead>
<tr><th>Niveau</th><th>Definition</th><th>Klinisk betydning</th></tr>
</thead>
<tbody>
<tr><td><strong>L1</strong></td><td>Flere fase 3-RCT'er / systematiske oversigter</td><td>Stærk understøttelse; klinisk anvendelse kan overvejes</td></tr>
<tr><td><strong>L2</strong></td><td>Enkelt RCT eller flere fase 2-forsøg</td><td>Moderat understøttelse; valideringsforsøg kan designes</td></tr>
<tr><td><strong>L3</strong></td><td>Observationsstudier / store caseserier</td><td>Foreløbig understøttelse; kræver yderligere validering</td></tr>
<tr><td><strong>L4</strong></td><td>Prækliniske / mekanistiske studier</td><td>Teoretisk understøttelse; langt fra klinisk anvendelse</td></tr>
<tr><td><strong>L5</strong></td><td>Kun modelforudsigelse</td><td>Hypotesestadie; endnu ingen evidens fra mennesker</td></tr>
</tbody>
</table>

---

## Forudsigelse med dobbelt motor

To metoder kører parallelt, og en konfidensmarkering registrerer, om de er enige:

| Metode | Hastighed | Præcision | Beskrivelse |
|--------|-------|-----------|-------------|
| Videngraf (KG) | Hurtig | Lavere | Inferens over DrugBank-relationer og grafstruktur |
| Deep learning (DL) | Langsom | Højere | TxGNN grafbaseret neuralt netværk |

| Konfidens | Kilde | Betydning |
|------------|--------|---------|
| very_high | KG + DL | Begge metoder er enige |
| high | Kun DL | Højtscorende understøttelse fra deep learning |
| medium | Kun KG | Understøttelse fra videngraf |

---

## Integration af myndighedsdata

Data om lægemiddelgodkendelser i Danmark kommer fra DKMA. Navne på indholdsstoffer mappes til
DrugBank-vokabularet; indholdsstoffer, der ikke kan mappes — planteekstrakter, vacciner, hjælpestoffer
og andet, der ikke er katalogiseret af DrugBank — udelades fra forudsigelsen.

---

## Begrænsninger

<ol class="actionable-steps">
<li>Forudsigelser er statistiske associationer og <strong>indebærer ikke kausalitet eller klinisk effekt</strong>.</li>
<li>En L5-vurdering betyder, at der kun foreligger en modelforudsigelse uden understøttende evidens fra mennesker.</li>
<li>Evidensindsamlingen afhænger af offentlige databaser; upublicerede eller ikke-indekserede studier fanges ikke.</li>
<li>Mapning af indholdsstoffer kan overse elementer på grund af forskelle i navngivning.</li>
</ol>

---

## Om udvikleren

Denne platform er udviklet og drives af **藥提醒科技有限公司** (yao.care, virksomhedsregistreringsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

DkTxGNN er Danmarks-sitet i virksomhedens produktlinje "TxGNN Drug Repurposing".
Det samme system er udrullet i 30 lande og regioner, hver med navnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN og så videre) på `{cc}txgnn.yao.care`.
Produktoversigt: <https://www.yao.care/medical/txgnn/>.

Selve TxGNN-modellen er udviklet af Zitnik Lab ved Harvard Medical School og offentliggjort
i *Nature Medicine*. Denne platform er det produktionssystem, 藥提醒科技有限公司 har bygget oven på den
model, og dækker integration af nationale lægemiddelregistreringsdata, dobbelt forudsigelse med videngraf og
deep learning, evidensgradering ud fra PubMed / ClinicalTrials samt SMART on FHIR-integration
med elektroniske patientjournaler.

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
