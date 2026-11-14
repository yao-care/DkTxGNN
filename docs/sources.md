---
layout: default
title: Datakilder
nav_order: 93
permalink: /sources/
description: "Datakilderne bag DkTxGNN: registreringsdata fra DKMA, TxGNN, ClinicalTrials.gov, PubMed og DrugBank."
---

# Datakilder

<div class="key-takeaway">
Enhver konklusion kan spores tilbage til en offentlig datakilde — intet er en sort boks.
</div>

---

<!-- site-data:start（母目錄 .claude/gen_page_data_20261116.py 產生，勿手改）-->
## Danmark: data bag dette websted

Dette websted offentliggør rapporter om **{{ site.data.drug_stats.total_drugs }}** lægemidler fra registreringsdata fra [DKMA](https://laegemiddelstyrelsen.dk/) (Danmark).

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

## Oversigt over kilder

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Kilde</th><th>Anvendes til</th></tr>
</thead>
<tbody>
<tr><td>Registreringsdata</td><td><a href="https://laegemiddelstyrelsen.dk/">DKMA</a></td><td>Liste over lægemidler med gældende markedsføringstilladelse i Danmark og deres indholdsstoffer</td></tr>
<tr><td>Forudsigelsesmodel</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Forudsigelse af association mellem lægemiddel og sygdom</td></tr>
<tr><td>Kliniske forsøg</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidensgradering (NCT)</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidensgradering (PMID)</td></tr>
<tr><td>Lægemiddelinformation</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mapning af indholdsstoffer og data om targets</td></tr>
<tr><td>Interaktioner</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Data om lægemiddelinteraktioner</td></tr>
</tbody>
</table>

---

## Lokale data på dette site

Danske lægemidler og deres status kommer fra Lægemiddelstyrelsens liste over godkendte lægemidler
(Excel-fil). Listen omfatter kun lægemidler med gældende tilladelse og har intet selvstændigt statusfelt.

| Punkt | Detalje |
|------|---------|
| Datasæt | Liste over godkendte lægemidler (Excel-fil, opdateres dagligt af Lægemiddelstyrelsen) |
| Udgiver | Lægemiddelstyrelsen (DKMA) |
| Download | <https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=0BD4960F0D7744E3BABC951431681ECC&lang=en> (oversigt: <https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/>) |
| Identifikator | Drugid |
| Opdatering | Automatisk ugentlig download (hver mandag); et lægemiddel, der ikke længere står på listen, beholder sin hidtidige status |

---

## Licensering

Hver kilde har sin egen licens — kontrollér den, før du citerer:

- **TxGNN**: akademisk brug; citér Huang et al. (2024)
- **ClinicalTrials.gov / PubMed**: offentlige data fra US NIH
- **DrugBank**: ikke-kommerciel brug underlagt licensvilkårene
- **DKMA**: underlagt vilkårene for åbne data hos den danske lægemiddelmyndighed

---

## Opdateringsfrekvens

| Data | Frekvens |
|------|-----------|
| Lægemiddelstyrelsens liste over godkendte lægemidler | Ugentligt (hver mandag) |
| Evidens fra forsøg / litteratur | Indsamles på ny med jævne mellemrum |
| Interaktionsdata | Gennemgås kvartalsvist |

---

## Videnskabelig kildehenvisning

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

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
