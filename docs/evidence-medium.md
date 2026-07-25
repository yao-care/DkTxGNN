---
layout: default
title: Moderat evidens (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "Kandidater til lægemiddelrepositionering på L3-L4 i DkTxGNN, understøttet af observationsbaseret eller præklinisk evidens."
---

# Moderat evidens (L3-L4)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med foreløbig evidens, som kræver yderligere validering
</p>

---

## Kriterier

| Niveau | Definition | Klinisk betydning |
|-------|------------|------------------|
| **L3** | Observationsstudier / store caseserier | Foreløbig understøttelse; kræver yderligere validering |
| **L4** | Prækliniske / mekanistiske studier | Teoretisk understøttelse; langt fra klinisk anvendelse |

---

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | sort: "title" %}

### L3 ({{ l3_drugs.size }} lægemidler)

| Lægemiddel | Indikationer | Link |
|---------|---------|------|
{% for drug in l3_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L4 ({{ l4_drugs.size }} lægemidler)

| Lægemiddel | Indikationer | Link |
|---------|---------|------|
{% for drug in l4_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
