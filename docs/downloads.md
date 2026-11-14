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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Danmark: data bag dette websted

Dette websted offentliggør rapporter om **{{ site.data.drug_stats.total_drugs }}** lægemidler fra registreringsdata fra [DKMA](https://laegemiddelstyrelsen.dk/) (Danmark).

Datasæt: [Lægemiddelstyrelsen: Liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/); det hentes og sammenlignes automatisk hver uge (mandag). Detaljer: [Datakilder]({{ '/sources/' | relative_url }}).

Rapporter efter evidensniveau:

| Evidensniveau | Rapporter | Andel |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

12 forudsagte par af lægemiddel og sygdom på dette websted findes ikke på noget andet af de 30 TxGNN-websteder.

<!-- site-data:end -->

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

Denne platform er udviklet og drives af **藥提醒科技有限公司** (yao.care). Se siden
<a href="{{ '/about/' | relative_url }}">Om platformen</a> for den fulde baggrund om virksomheden og metoden.

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
