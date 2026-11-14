---
layout: default
title: Kun modelforudsigelse (L5)
nav_order: 23
permalink: /evidence-low/
description: "L5-kandidater i DkTxGNN: kun modelforudsigelse, endnu uden klinisk evidens eller litteraturevidens."
---

# Kun modelforudsigelse (L5)

<!-- page-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
{% assign pd_m = site.data.drug_stats.level_counts.L5 %}
Siden viser **{{ pd_m }}** af de **{{ site.data.drug_stats.total_drugs }}** lægemidler med en offentliggjort rapport på dette websted ({{ pd_m | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %). Definition af niveauerne: [Metode]({{ '/methodology/' | relative_url }}).
<!-- page-data:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med kun modelforudsigelse og endnu ingen evidens fra mennesker
</p>

---

## Kriterier

| Niveau | Definition | Klinisk betydning |
|-------|------------|------------------|
| **L5** | Kun modelforudsigelse | Hypotesestadie; endnu ingen evidens fra mennesker |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L5 ({{ l5_drugs.size }} lægemidler)

| Lægemiddel | Indikationer | Link |
|---------|---------|------|
{% for drug in l5_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
