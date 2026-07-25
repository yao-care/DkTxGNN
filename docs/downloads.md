---
layout: default
title: Downloads
nav_order: 94
permalink: /downloads/
description: "Åbne data til download fra DkTxGNN: FHIR-ressourcer, forudsigelsesresultater og søgeindeks."
---

# Downloads

<div class="key-takeaway">
Forudsigelserne udgives i FHIR R4-format, klar til integration med EPJ-systemer.
</div>

---

## FHIR-ressourcer

Dette site udgiver forudsigelser som FHIR R4-ressourcer, der kan anvendes direkte af SMART on FHIR-apps:

| Ressource | Sti | Beskrivelse |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Capability statement for FHIR-serveren |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Lægemiddelressourcer |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Forudsagte indikationer |
| Bundle | `/fhir/Bundle/all-predictions.json` | Alle forudsigelser samlet i ét bundle |

---

## Søgeindeks

`/data/search-index.json` leverer et søgeindeks over lægemidler og indikationer, som du kan bruge til at bygge
din egen forespørgselsgrænseflade.

---

## Anvendelsesvilkår

<ol class="actionable-steps">
<li>Data på dette site er <strong>udelukkende til forskningsreference</strong> og må ikke bruges som grundlag for medicinske beslutninger.</li>
<li>Ved citering skal du kreditere DkTxGNN (藥提醒科技有限公司) og citere den oprindelige TxGNN-artikel.</li>
<li>Videreanvendte data er fortsat underlagt licensvilkårene for hver oprindelig kilde (se <a href="{{ '/sources/' | relative_url }}">Datakilder</a>).</li>
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
