---
layout: default
title: Høj evidens (L1-L2)
nav_order: 21
permalink: /evidence-high/
description: "44 lægemidler på evidensniveau L1–L2 på dette websted (Danmark), fx Bendamustine, Busulfan, Clofarabine, med vigtigste forudsagte indikation, tilladelser fra Lægemiddelstyrelsen og kontrollog for hvert."
---

# Høj evidens (L1-L2)

<!-- tier-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
{% assign ev_share = site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs %}
Siden viser **{{ site.data.evidence_tier_facts.high.count }}** af de **{{ site.data.drug_stats.total_drugs }}** lægemidler med en offentliggjort rapport på dette websted ({{ site.data.evidence_tier_facts.high.count | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }} %): L1 **{{ site.data.evidence_tier_facts.high.by_level.L1 }}**, L2 **{{ site.data.evidence_tier_facts.high.by_level.L2 }}**.
Medianandel på L1–L2 på tværs af de 30 TxGNN-websteder: {{ site.data.evidence_tier_facts.high.cross.median_share }} %. {% if ev_share > site.data.evidence_tier_facts.high.cross.median_share %}Dette websted ligger over medianen.{% elsif ev_share < site.data.evidence_tier_facts.high.cross.median_share %}Dette websted ligger under medianen.{% else %}Dette websted ligger på medianen.{% endif %}

{% if site.data.evidence_tier_facts.high.count > 0 %}
I de lokale data (tilladelser fra Lægemiddelstyrelsen) har **{{ site.data.evidence_tier_facts.high.with_current }}** af disse lægemidler mindst én gyldige post, **{{ site.data.evidence_tier_facts.high.none_current }}** har poster, men ingen gyldige, og **{{ site.data.evidence_tier_facts.high.without_data }}** findes ikke i de lokale data. **{{ site.data.evidence_tier_facts.high.with_reviews }}** har poster i kontrolloggen (rettelser af registreringsoplysninger på lægemiddelsiden). **{{ site.data.evidence_tier_facts.high.cross.unique_drugs }}** har en forudsagt indikation, som intet andet TxGNN-websted angiver for samme lægemiddel.
{% if site.data.evidence_tier_facts.high.none_current_list.size > 0 %}

Med poster, men ingen gyldige: {% for r in site.data.evidence_tier_facts.high.none_current_list %}[{{ r.t }}]({{ r.u | relative_url }}){% unless forloop.last %}, {% endunless %}{% endfor %}.{% endif %}
{% endif %}

Definition af alle niveauer: [Metode]({{ '/methodology/' | relative_url }}).
<!-- tier-facts:end -->

<p style="font-size: 1.25rem; color: #666; margin-bottom: 1.5rem;">
Kandidater, der kan prioriteres til klinisk vurdering
</p>

Hvilke af disse lægemidler har evidens fra forsøg for deres forudsagte nye indikation, og hvor mange registrerede forsøg citeres? Se [Lægemidler i Danmark med evidens fra kliniske forsøg for en ny indikation]({{ '/clinical-trial-evidence/' | relative_url }}).

---

## Kriterier

| Niveau | Definition | Klinisk betydning |
|-------|------------|------------------|
| **L1** | Flere fase 3-RCT'er / systematiske oversigter | Stærk understøttelse; klinisk anvendelse kan overvejes |
| **L2** | Enkelt RCT eller flere fase 2-forsøg | Moderat understøttelse; valideringsforsøg kan designes |

---

{% assign l1_drugs = site.drugs | where: "evidence_level", "L1" | where_exp: "d", "d.noindex != true" | sort: "title" %}
{% assign l2_drugs = site.drugs | where: "evidence_level", "L2" | where_exp: "d", "d.noindex != true" | sort: "title" %}

### L1 ({{ site.data.evidence_tier_facts.high.by_level.L1 }} lægemidler)

<!-- tier-table:start L1（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lægemiddel | Niveau | Vigtigste forudsagte nye indikation | tilladelser fra Lægemiddelstyrelsen: gyldige / i alt | Kontrollog | Kun på dette websted |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L1" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

### L2 ({{ site.data.evidence_tier_facts.high.by_level.L2 }} lægemidler)

<!-- tier-table:start L2（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->

| Lægemiddel | Niveau | Vigtigste forudsagte nye indikation | tilladelser fra Lægemiddelstyrelsen: gyldige / i alt | Kontrollog | Kun på dette websted |
|---|---|---|---|---|---|
{% for r in site.data.evidence_tier_facts.high.rows %}{% if r.l == "L2" %}| [{{ r.t | replace: '|', '/' }}]({{ r.u | relative_url }}) | {{ r.l }} | {{ r.i | replace: '|', '/' }} | {% if r.lt %}{{ r.lv }} / {{ r.lt }}{% else %}—{% endif %} | {{ r.r }}{% if r.rs and r.rs != '' %}: {{ r.rs | replace: '|', '/' }}{% endif %} | {% if r.x and r.x > 0 %}ja ({{ r.x }}){% else %}—{% endif %} |
{% endif %}{% endfor %}

<!-- tier-table:end -->

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
