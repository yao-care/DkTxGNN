---
layout: default
title: Alle lægemidler
nav_order: 20
permalink: /drugs/
description: "Alle valideringsrapporter for lægemidler og statistik over evidensniveauer i DkTxGNN."
---
{%- comment -%}2026-10-16：列表不含舊 ID 轉址頁與 noindex 頁{%- endcomment -%}
{% assign listed_drugs = site.drugs | where_exp: "d", "d.layout != 'redirect'" | where_exp: "d", "d.noindex != true" %}
{% assign l1_count = listed_drugs | where: "evidence_level", "L1" | size %}
{% assign l2_count = listed_drugs | where: "evidence_level", "L2" | size %}
{% assign l3_count = listed_drugs | where: "evidence_level", "L3" | size %}
{% assign l4_count = listed_drugs | where: "evidence_level", "L4" | size %}
{% assign l5_count = listed_drugs | where: "evidence_level", "L5" | size %}

# Alle lægemidler

{{ listed_drugs.size }} valideringsrapporter for lægemidler

---

## Fordeling på evidensniveau

| Evidensniveau | Lægemidler | Beskrivelse |
|---------|--------|------|
| **L1** | {{ l1_count }} | Flere RCT'er / systematiske oversigter |
| **L2** | {{ l2_count }} | Enkelt RCT / fase 2-forsøg |
| **L3** | {{ l3_count }} | Observationsstudier / store caseserier |
| **L4** | {{ l4_count }} | Prækliniske / mekanistiske studier |
| **L5** | {{ l5_count }} | Kun modelforudsigelse |

---

## Fuld lægemiddelliste

{% assign all_drugs = listed_drugs | sort: 'title' %}

| Lægemiddel | Evidensniveau | Indikationer |
|---------|---------|---------|
{% for drug in all_drugs %}| [{{ drug.title }}]({{ drug.url | relative_url }}) | {{ drug.evidence_level }} | {{ drug.indication_count }} |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
