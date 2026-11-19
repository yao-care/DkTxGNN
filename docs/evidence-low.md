---
layout: default
title: Kun modelforudsigelse (L5)
nav_order: 23
permalink: /evidence-low/
description: "632 lægemidler på evidensniveau L5 på dette websted (Danmark), fx Acyclovir, Adalimumab, Aflibercept, med vigtigste forudsagte indikation, tilladelser fra Lægemiddelstyrelsen og kontrollog for hvert."
---

# Kun modelforudsigelse (L5)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Siden viser **{{ site.data.evidence_tier_facts.low.count }}** af de **{{ site.data.drug_stats.total_drugs }}** lægemidler med en offentliggjort rapport på dette websted ({{ site.data.evidence_tier_facts.low.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L5 **{{ site.data.evidence_tier_facts.low.by_level.L5 }}**.
Medianandel på L5 på tværs af de 30 TxGNN-websteder: {{ site.data.evidence_tier_facts.low.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.low.cross.median_share %}Dette websted ligger over medianen.{% elsif ev_share < site.data.evidence_tier_facts.low.cross.median_share %}Dette websted ligger under medianen.{% else %}Dette websted ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.low.count > 0 %}
I de lokale data (tilladelser fra Lægemiddelstyrelsen) har **{{ site.data.evidence_tier_facts.low.with_current }}** af disse lægemidler mindst én gyldige post, **{{ site.data.evidence_tier_facts.low.none_current }}** har poster, men ingen gyldige, og **{{ site.data.evidence_tier_facts.low.without_data }}** findes ikke i de lokale data. **{{ site.data.evidence_tier_facts.low.with_reviews }}** har poster i kontrolloggen (rettelser af registreringsoplysninger på lægemiddelsiden). **{{ site.data.evidence_tier_facts.low.cross.unique_drugs }}** har en forudsagt indikation, som intet andet TxGNN-websted angiver for samme lægemiddel.
{% if site.data.evidence_tier_facts.low.none_current_list.size > 0 %}

Med poster, men ingen gyldige: {% for r in site.data.evidence_tier_facts.low.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}

Lægemidler med en gyldige lokal post vises først.
{% endif %}

Definition af alle niveauer: [Metode]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

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

### L5 ({{ site.data.evidence_tier_facts.low.by_level.L5 }} lægemidler)

<!-- tier-table:start L5（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lægemiddel | Niveau | Vigtigste forudsagte nye indikation | tilladelser fra Lægemiddelstyrelsen: gyldige / i alt | Kontrollog | Kun på dette websted |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.low.rows %}{% if r.l == "L5" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
