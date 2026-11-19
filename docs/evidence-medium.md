---
layout: default
title: Moderat evidens (L3-L4)
nav_order: 22
permalink: /evidence-medium/
description: "70 lægemidler på evidensniveau L3–L4 på dette websted (Danmark), fx Abatacept, Acitretin, Alprazolam, med vigtigste forudsagte indikation, tilladelser fra Lægemiddelstyrelsen og kontrollog for hvert."
---

# Moderat evidens (L3-L4)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Siden viser **{{ site.data.evidence_tier_facts.medium.count }}** af de **{{ site.data.drug_stats.total_drugs }}** lægemidler med en offentliggjort rapport på dette websted ({{ site.data.evidence_tier_facts.medium.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L3 **{{ site.data.evidence_tier_facts.medium.by_level.L3 }}**, L4 **{{ site.data.evidence_tier_facts.medium.by_level.L4 }}**.
Medianandel på L3–L4 på tværs af de 30 TxGNN-websteder: {{ site.data.evidence_tier_facts.medium.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.medium.cross.median_share %}Dette websted ligger over medianen.{% elsif ev_share < site.data.evidence_tier_facts.medium.cross.median_share %}Dette websted ligger under medianen.{% else %}Dette websted ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.medium.count > 0 %}
I de lokale data (tilladelser fra Lægemiddelstyrelsen) har **{{ site.data.evidence_tier_facts.medium.with_current }}** af disse lægemidler mindst én gyldige post, **{{ site.data.evidence_tier_facts.medium.none_current }}** har poster, men ingen gyldige, og **{{ site.data.evidence_tier_facts.medium.without_data }}** findes ikke i de lokale data. **{{ site.data.evidence_tier_facts.medium.with_reviews }}** har poster i kontrolloggen (rettelser af registreringsoplysninger på lægemiddelsiden). **{{ site.data.evidence_tier_facts.medium.cross.unique_drugs }}** har en forudsagt indikation, som intet andet TxGNN-websted angiver for samme lægemiddel.
{% if site.data.evidence_tier_facts.medium.none_current_list.size > 0 %}

Med poster, men ingen gyldige: {% for r in site.data.evidence_tier_facts.medium.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definition af alle niveauer: [Metode]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

{% assign l3_drugs = site.drugs | where: "evidence_level", "L3" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l4_drugs = site.drugs | where: "evidence_level", "L4" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L3 ({{ site.data.evidence_tier_facts.medium.by_level.L3 }} lægemidler)

<!-- tier-table:start L3（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lægemiddel | Niveau | Vigtigste forudsagte nye indikation | tilladelser fra Lægemiddelstyrelsen: gyldige / i alt | Kontrollog | Kun på dette websted |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L3" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L4 ({{ site.data.evidence_tier_facts.medium.by_level.L4 }} lægemidler)

<!-- tier-table:start L4（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lægemiddel | Niveau | Vigtigste forudsagte nye indikation | tilladelser fra Lægemiddelstyrelsen: gyldige / i alt | Kontrollog | Kun på dette websted |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.medium.rows %}{% if r.l == "L4" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
