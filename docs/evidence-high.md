---
layout: default
title: Høj evidens (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "Kandidater til lægemiddelrepositionering på L1-L2 i DkTxGNN, understøttet af kliniske forsøg eller systematiske oversigter."
---

# Høj evidens (L1-L2)

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater, der kan prioriteres til klinisk vurdering
</p>

---

## Kriterier

| Niveau | Definition | Klinisk betydning |
|-------|------------|------------------|
| **L1** | Flere fase 3-RCT'er / systematiske oversigter | Stærk understøttelse; klinisk anvendelse kan overvejes |
| **L2** | Enkelt RCT eller flere fase 2-forsøg | Moderat understøttelse; valideringsforsøg kan designes |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | sort: "title" %}

### L1 ({{ l1_drugs.size }} lægemidler)

| Lægemiddel | Indikationer | Link |
|---------|---------|------|
{% for drug in l1_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

### L2 ({{ l2_drugs.size }} lægemidler)

| Lægemiddel | Indikationer | Link |
|---------|---------|------|
{% for drug in l2_drugs %}| **{{ drug.title }}** | {{ drug.indication_count }} | [Se rapport]({{ drug.url | relative_url }}) |
{% endfor %}

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
