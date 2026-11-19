---
layout: default
title: Brugervejledning
nav_order: 92
permalink: /guide/
description: "Brugervejledning til DkTxGNN: sådan slår du lægemidler op, læser evidensniveauer og fortolker anbefalinger."
---

# Brugervejledning

<div class="key-takeaway">
Se først evidensniveauet, derefter anbefalingen, og læs til sidst kildelitteraturen.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Danmark: et eksempel fra dette websted

En rapport på dette websted læses i tre trin: evidensniveau, lokale markedsdata, kontrollog.

{% assign gx = site.data.local_facts.example %}
{% if gx %}Åbn [{{ gx.t }}]({{ gx.u | relative_url }}): sidehovedet viser evidensniveau **{{ gx.l }}**; den vigtigste forudsagte nye indikation er **{{ gx.i }}**; de lokale data har **{{ gx.lt }}** tilladelser fra Lægemiddelstyrelsen, heraf **{{ gx.lv }}** gyldige; sidens kontrollog har **{{ gx.r }}** poster.{% endif %}

{% if site.data.local_facts.most_reviewed.size > 0 %}Lægemidler med flest poster i kontrolloggen: {% for r in site.data.local_facts.most_reviewed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.r }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Seneste rettelser i kontrolloggen: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## Opslag af et lægemiddel

<ol class="actionable-steps">
<li>Brug søgefeltet øverst på siden (generiske navne på indholdsstoffer giver bedre træf end handelsnavne).</li>
<li>Eller gennemse den fulde liste på <a href="{{ '/drugs/' | relative_url }}">Alle lægemidler</a>.</li>
<li>Du kan også gennemse efter evidensniveau: <a href="{{ '/evidence-high/' | relative_url }}">høj</a>, <a href="{{ '/evidence-medium/' | relative_url }}">moderat</a>, <a href="{{ '/evidence-low/' | relative_url }}">kun modelforudsigelse</a>.</li>
</ol>

---

## Sådan læser du en rapport

<p class="key-answer" data-question="Hvad betyder evidensniveauerne L1 til L5?">
Hver lægemiddelrapport oplister forudsagte nye indikationer, og hver indikation har et evidensniveau
fra L1 til L5. <strong>L1 betyder, at flere randomiserede kontrollerede fase 3-forsøg allerede understøtter den; L5 betyder
kun modelforudsigelse uden evidens fra mennesker.</strong> De fulde kriterier findes på siden
<a href="{{ '/methodology/' | relative_url }}">Metode</a>.
</p>

| Hvis du ser | Betyder det | Foreslået handling |
|-----------|----------|------------------|
| L1 / L2 | Der findes evidens fra kliniske forsøg | Gennemgå de underliggende NCT- og PMID-poster |
| L3 / L4 | Observationsbaseret eller præklinisk evidens | Betragt det som et forskningsspor |
| L5 | Kun modelforudsigelse | Udelukkende hypotesegenerering; ikke til klinisk brug |

---

## Kildehenvisning og sporbarhed

Hvert enkelt stykke evidens i en rapport har en sporbar identifikator:

- **NCT-nummer**: linker til registreringen på ClinicalTrials.gov
- **PMID**: linker til posten i PubMed
- **DrugBank ID**: linker til data om lægemidler og targets

Læs venligst kildelitteraturen for at bekræfte konteksten, før du citerer nogen konklusion fra denne platform.

---

## Ofte stillede spørgsmål

<p class="key-answer" data-question="Kan forudsigelserne bruges klinisk?">
<strong>Nej.</strong> Forudsigelser på denne platform er forskningsspor, ikke klinisk rådgivning. Enhver
klinisk anvendelse af lægemiddelrepositionering skal gennemgå fuld validering i kliniske forsøg og
myndighedsgodkendelse.
</p>

<p class="key-answer" data-question="Hvorfor kan jeg ikke finde et bestemt lægemiddel?">
Et indholdsstof skal kunne mappes til DrugBank-vokabularet for at indgå i forudsigelsen. Planteekstrakter,
vacciner, hjælpestoffer og andet, der ikke er katalogiseret af DrugBank, optræder ikke på denne platform.
</p>

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
