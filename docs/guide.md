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

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Danmark: data bag dette websted

Dette websted offentliggør rapporter om **{{ site.data.drug_stats.total_drugs }}** lægemidler fra registreringsdata fra [DKMA](https://laegemiddelstyrelsen.dk/) (Danmark).

Datasæt: [Lægemiddelstyrelsen: Liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/); det hentes og sammenlignes automatisk hver uge (mandag). Detaljer: [Datakilder]({{ '/sources/' | relative_url }}).

Rapporter efter evidensniveau:

| Evidensniveau | Rapporter | Andel |
|---|---|---|
| L1 | {{ site.data.drug_stats.level_counts.L1 }} | {{ site.data.drug_stats.level_counts.L1 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L2 | {{ site.data.drug_stats.level_counts.L2 }} | {{ site.data.drug_stats.level_counts.L2 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L3 | {{ site.data.drug_stats.level_counts.L3 }} | {{ site.data.drug_stats.level_counts.L3 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L4 | {{ site.data.drug_stats.level_counts.L4 }} | {{ site.data.drug_stats.level_counts.L4 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
| L5 | {{ site.data.drug_stats.level_counts.L5 }} | {{ site.data.drug_stats.level_counts.L5 | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |
{% assign na = site.data.drug_stats.total_drugs | minus: site.data.drug_stats.level_counts.L1 | minus: site.data.drug_stats.level_counts.L2 | minus: site.data.drug_stats.level_counts.L3 | minus: site.data.drug_stats.level_counts.L4 | minus: site.data.drug_stats.level_counts.L5 %}{% if na > 0 %}| N/A | {{ na }} | {{ na | times: 100.0 | divided_by: site.data.drug_stats.total_drugs | round: 1 }}% |{% endif %}

12 forudsagte par af lægemiddel og sygdom på dette websted findes ikke på noget andet af de 30 TxGNN-websteder.

<!-- site-data:end -->

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
