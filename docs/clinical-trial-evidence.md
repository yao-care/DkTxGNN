---
layout: default
title: "Lægemidler med forsøgsevidens for en ny indikation"
nav_order: 25
permalink: /clinical-trial-evidence/
description: "Lægemidler fra Lægemiddelstyrelsens liste, hvis af TxGNN forudsagte nye indikation har evidens fra kliniske forsøg (L1-L2): indikation, niveau, forsøg."
last_modified_at: 2026-11-03
---
{%- comment -%}
2026-11-03：回答 AI 搜尋常問的「本國藥物中，哪些新適應症有臨床試驗證據」。全表由 Liquid 從藥物頁產生，不寫死藥名或數字。
收錄＝公開藥物頁（排除 id_redirect 與 noindex）中 evidence_level 為 L1 或 L2（本站 evidence-high 標準：L1 多個 Phase 3 RCT／系統性回顧，
L2 單一 RCT 或多個 Phase 2 試驗）。預測新適應症與等級註記取自各藥物頁快速總覽表；下列欄名是本站藥物頁實際用到的寫法（建頁時逐頁核對），
新寫法抓不到時顯示「se rapporten」、等級仍取 front matter。試驗數＝該藥物頁引用的不重複 NCT 編號數。
{%- endcomment -%}
{%- assign ind_labels = "Forudsagt ny indikation" | split: "|" -%}
{%- assign lev_labels = "Evidensniveau" | split: "|" -%}
{%- assign listed = site.drugs | where_exp: "d", "d.layout != 'id_redirect'" | where_exp: "d", "d.noindex != true" -%}
{%- assign l1 = listed | where: "evidence_level", "L1" | sort: "title" -%}
{%- assign l2 = listed | where: "evidence_level", "L2" | sort: "title" -%}
{%- assign trial_drugs = l1 | concat: l2 -%}
{%- assign latest = trial_drugs | sort: "last_modified_at" | last -%}
{%- assign latest_date = latest.last_modified_at | date: "%Y-%m-%d" -%}

# Lægemidler i Danmark med evidens fra kliniske forsøg for en ny indikation

<p class="key-answer" data-question="Hvilke lægemidler i Danmark har evidens fra kliniske forsøg for en ny indikation?">
<strong>{{ trial_drugs.size }}</strong> af de {{ listed.size }} lægemidler med en DkTxGNN-rapport har en ny indikation forudsagt af TxGNN med evidensniveau <strong>L1 eller L2</strong> ({{ l1.size }} på L1, {{ l2.size }} på L2), dvs. at der er fundet evidens fra kliniske forsøg (randomiserede forsøg, fase 2–3-forsøg eller systematiske oversigter).
</p>

Lægemidlerne stammer fra [Lægemiddelstyrelsens](https://laegemiddelstyrelsen.dk/) liste over godkendte lægemidler (lægemidler med markedsføringstilladelse i Danmark; status vises i hver rapport); listen afspejler lægemiddelrapporterne, senest opdateret {{ latest_date }}.

<div class="key-takeaway">
Evidens fra forsøg for en forudsagt indikation er ikke bevis for effekt. Alle kandidater nedenfor <strong>kræver stadig klinisk validering</strong> og myndighedsvurdering før enhver klinisk anvendelse.
</div>

---

## Lægemidler med evidens fra forsøg (L1–L2)

<div class="table-wrapper"><table>
<thead>
<tr><th>Lægemiddel</th><th>Forudsagt ny indikation</th><th>Evidensniveau</th><th>Citerede registrerede forsøg (NCT)</th></tr>
</thead>
<tbody>
{%- for drug in trial_drugs -%}
{%- assign indication = "" -%}
{%- for lab in ind_labels -%}{%- if indication == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign qo = drug.content | split: needle -%}{%- if qo.size > 1 -%}{%- assign indication = qo[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign level_cell = "" -%}
{%- for lab in lev_labels -%}{%- if level_cell == "" -%}{%- assign needle = "<td>" | append: lab | append: "</td>" -%}{%- assign lv = drug.content | split: needle -%}{%- if lv.size > 1 -%}{%- assign level_cell = lv[1] | split: "</td>" | first | split: "<td>" | last | strip -%}{%- endif -%}{%- endif -%}{%- endfor -%}
{%- assign parts = drug.content | split: "NCT" -%}
{%- capture nct_ids -%}{%- for p in parts offset: 1 -%}{%- assign id = p | slice: 0, 8 -%}{%- assign rest = id | remove: "0" | remove: "1" | remove: "2" | remove: "3" | remove: "4" | remove: "5" | remove: "6" | remove: "7" | remove: "8" | remove: "9" -%}{%- if id.size == 8 and rest == "" -%}{{ id }},{%- endif -%}{%- endfor -%}{%- endcapture -%}
{%- assign nct_count = nct_ids | split: "," | uniq | size %}
<tr><td><a href="{{ drug.url | relative_url }}">{{ drug.title }}</a></td><td>{% if indication != "" %}{{ indication }}{% else %}se rapporten{% endif %}</td><td>{{ drug.evidence_level }}{% if level_cell != "" and level_cell != drug.evidence_level %} <a href="{{ drug.url | relative_url }}" title="{{ level_cell | strip_html | escape }}">(med forbehold)</a>{% endif %}</td><td>{{ nct_count }}</td></tr>
{%- endfor %}
</tbody>
</table></div>

## Sådan læses listen

- **Evidensniveau** følger sitets [kriterier]({{ '/evidence-high/' | relative_url }}): L1 = Flere fase 3-RCT'er / systematiske oversigter; L2 = Enkelt RCT eller flere fase 2-forsøg. "(med forbehold)" betyder, at rapporten tager forbehold for niveauet; læs noten i rapporten, før du lægger vægt på det.
- **Forudsagt ny indikation** er hovedforudsigelsen i hver rapport. Indikationer og kontraindikationer, der allerede er registreret i TxGNN-vidensgrafen, er udeladt, men enkelte forudsigelser kan stadig overlappe en etableret anvendelse; rapporten forklarer det, hvor det er relevant.
- **Citerede registrerede forsøg** tæller de ClinicalTrials.gov-numre (NCT), der citeres i rapporten. Rapporterne citerer et udvalg af de fundne forsøg; 0 betyder, at rapporten ikke citerer noget registreret forsøg, og afsnittet om litteraturevidens viser grundlaget for niveauet.
- Se alle niveauer og hele metoden under [Høj evidens (L1-L2)]({{ '/evidence-high/' | relative_url }}), [Alle lægemidler]({{ '/drugs/' | relative_url }}) og [metode]({{ '/methodology/' | relative_url }}).

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
