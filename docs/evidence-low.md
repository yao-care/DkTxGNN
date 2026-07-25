---
layout: default
title: Kun modelforudsigelse (L5)
nav_order: 23
permalink: /evidence-low/
description: "L5-kandidater i DkTxGNN: kun modelforudsigelse, endnu uden klinisk evidens eller litteraturevidens."
---

# Kun modelforudsigelse (L5)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater med kun modelforudsigelse og endnu ingen evidens fra mennesker
</p>

---

## Kriterier

| Niveau | Definition | Klinisk betydning |
|-------|------------|------------------|
| **L5** | Kun modelforudsigelse | Hypotesestadie; endnu ingen evidens fra mennesker |

---

{% assign l5_drugs = site.drugs | where: "evidence_level", "L5" | sort: "title" %}

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
