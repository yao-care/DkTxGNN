---
layout: default
title: "Forudsigelser for L\u00e6gemiddelrepositionering \u2014 Danmark"
nav_order: 1
description: "AI-baserede forudsigelser af ny anvendelse af lægemidler for 807 lægemidler godkendt af Lægemiddelstyrelsen (DKMA). TxGNN-modellen finder mulige nye terapeutiske anvendelser med evidensbaseret validering."
last_modified_at: 2026-11-04
permalink: /
---

# Ny anvendelse af lægemidler: fra AI til evidens

**DkTxGNN** bruger Harvards TxGNN-model til at forudsige kandidater til lægemiddelrepositionering for **{{ site.data.drug_stats.total_drugs }}** lægemidler godkendt af DKMA og finder mulige nye terapeutiske anvendelser.

[Se lægemiddelrapporter](/drugs/){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Læs om metoden](/methodology/){: .btn .fs-5 .mb-4 .mb-md-0 }

---

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Danmark: hvad dette websted dækker

Dette websted offentliggør rapporter om **{{ site.data.drug_stats.total_drugs }}** lægemidler fra registreringsdata fra [DKMA](https://laegemiddelstyrelsen.dk/) (Danmark).

### Lokale data på dette site

| Punkt | Detalje |
|------|---------|
| Datasæt | Liste over godkendte lægemidler (Excel-fil, opdateres dagligt af Lægemiddelstyrelsen) |
| Udgiver | Lægemiddelstyrelsen (DKMA) |
| Download | <https://laegemiddelstyrelsen.dk/LinkArchive.ashx?id=0BD4960F0D7744E3BABC951431681ECC&lang=en> (oversigt: <https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/>) |
| Identifikator | Drugid |
| Opdatering | Automatisk ugentlig download (hver mandag); et lægemiddel, der ikke længere står på listen, beholder sin hidtidige status |

Detaljer: [Datakilder]({{ '/sources/' | relative_url }}).

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

### Lægemidler med højeste evidensniveau på dette websted

| Lægemiddel | Evidensniveau |
|---|---|
| [Bendamustine](/drugs/bendamustine/) | L1 |
| [Busulfan](/drugs/busulfan/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Ribavirin](/drugs/ribavirin/) | L1 |
| [Clofarabine](/drugs/clofarabine/) | L1 |
| [Clomipramine](/drugs/clomipramine/) | L1 |
| [Doxorubicin](/drugs/doxorubicin/) | L1 |
| [Peginterferon Alfa-2B](/drugs/peginterferon-alfa-2b/) | L1 |
| [Tocilizumab](/drugs/tocilizumab/) | L1 |
| [Ketorolac](/drugs/ketorolac/) | L1 |

### Lægemidler, som kun dette websted dækker blandt de 30 TxGNN-websteder

| Lægemiddel | Evidensniveau |
|---|---|
| [Phenprocoumon](/drugs/phenprocoumon/) | L5 |
| [Amprenavir](/drugs/amprenavir/) | L5 |
| [Doramectin](/drugs/doramectin/) | L5 |
| [Amitraz](/drugs/amitraz/) | N/A |
| [Capsaicin](/drugs/capsaicin/) | N/A |
| [Cenegermin](/drugs/cenegermin/) | N/A |
| [Perflutren](/drugs/perflutren/) | N/A |
| [Robenacoxib](/drugs/robenacoxib/) | N/A |
| [Selamectin](/drugs/selamectin/) | N/A |
| [Tepoxalin](/drugs/tepoxalin/) | N/A |
| [Tilmicosin](/drugs/tilmicosin/) | N/A |
| [Tislelizumab](/drugs/tislelizumab/) | N/A |
| [Toripalimab](/drugs/toripalimab/) | N/A |
| [Troxerutin](/drugs/troxerutin/) | N/A |
| [Tylosin](/drugs/tylosin/) | N/A |

<!-- local-home:end -->

## Lægemiddelsøgning

Indtast et **lægemiddelnavn** eller **sygdomsnavn** for at finde forudsigelser om ny anvendelse. Generiske navne, handelsnavne og sygdomsnøgleord understøttes.

<style>
.drug-lookup-container { margin: 1.5rem 0; }
.lookup-search-box { display: flex; gap: 0.5rem; margin-bottom: 1rem; }
.lookup-input-wrapper { flex: 1; position: relative; }
#lookup-input { width: 100%; padding: 0.75rem 2.5rem 0.75rem 1rem; border: 2px solid #ddd; border-radius: 8px; font-size: 1rem; }
#lookup-input:focus { outline: none; border-color: #1976D2; }
.lookup-clear-btn { position: absolute; right: 0.75rem; top: 50%; transform: translateY(-50%); background: none; border: none; cursor: pointer; color: #999; font-size: 1.2rem; }
.lookup-search-btn { padding: 0.75rem 1.5rem; background: #1976D2; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: 600; }
.lookup-search-btn:hover { background: #1565C0; }
.lookup-filters { display: flex; gap: 1rem; align-items: center; flex-wrap: wrap; margin-bottom: 1rem; }
.filter-label { font-weight: 600; color: #666; }
.lookup-filters label { display: flex; align-items: center; gap: 0.25rem; cursor: pointer; }
.lookup-results { margin-top: 1rem; }
</style>

<div class="drug-lookup-container">
  <div class="lookup-search-box">
    <div class="lookup-input-wrapper">
      <input type="text" id="lookup-input" placeholder="Indtast lægemiddel- eller sygdomsnavn..." autocomplete="off">
      <button id="lookup-clear" class="lookup-clear-btn" style="display: none;">✕</button>
    </div>
    <button id="lookup-search" class="lookup-search-btn">Søg</button>
  </div>
  <div class="lookup-filters">
    <span class="filter-label">Evidensniveau:</span>
    <label><input type="checkbox" class="level-filter" value="L1" checked> L1</label>
    <label><input type="checkbox" class="level-filter" value="L2" checked> L2</label>
    <label><input type="checkbox" class="level-filter" value="L3" checked> L3</label>
    <label><input type="checkbox" class="level-filter" value="L4" checked> L4</label>
    <label><input type="checkbox" class="level-filter" value="L5" checked> L5</label>
  </div>
  <div id="lookup-results" class="lookup-results"></div>
</div>

<script src="https://cdn.jsdelivr.net/npm/fuse.js@7.0.0/dist/fuse.min.js" integrity="sha384-PCSoOZTpbkikBEtd/+uV3WNdc676i9KUf01KOA8CnJotvlx8rRrETbDuwdjqTYvt" crossorigin="anonymous"></script>
<script>
  window.DKTXGNN_CONFIG = {
    searchIndexUrl: '{{ "/data/search-index.json" | relative_url }}',
    drugsBaseUrl: '{{ "/drugs/" | relative_url }}'
  };
</script>
<script src="{{ '/assets/js/drug-lookup.js' | relative_url }}"></script>

---

## Hovedfunktioner

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem; margin: 1.5rem 0;">
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #2E7D32;">
    <strong style="font-size: 1.1rem;">Fra forudsigelse til evidens</strong><br>
    <span style="color: #666;">Hver rapport samler ID'er for kliniske forsøg (NCT), litteraturhenvisninger (PMID) og godkendelsesoplysninger fra DKMA, så alt kan spores.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #1976D2;">
    <strong style="font-size: 1.1rem;">Evidensklassificering i fem niveauer</strong><br>
    <span style="color: #666;">Klassificeringen fra L1 (flere fase 3-RCT'er) til L5 (kun AI-forudsigelse) hjælper med at prioritere kandidater til validering.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #FB8C00;">
    <strong style="font-size: 1.1rem;">Dækning af danske lægemidler</strong><br>
    <span style="color: #666;">Fokuserer på {{ site.data.drug_stats.total_drugs }} DKMA-godkendte lægemidler med forudsigelser om ny anvendelse klar til forskning.</span>
  </div>
  <div style="padding: 1.5rem; background: #f8f9fa; border-radius: 8px; border-left: 4px solid #9B59B6;">
    <strong style="font-size: 1.1rem;">FHIR-integration</strong><br>
    <span style="color: #666;">FHIR R4-kompatibelt API og SMART on FHIR-app til integration med elektroniske patientjournaler.</span>
  </div>
</div>

---

## Hurtig navigation

| Kategori | Beskrivelse | Link |
|----------|-------------|------|
| **Høj evidens** | L1-L2, prioriteres til klinisk vurdering | [Se lægemidler](/evidence-high/) |
| **Moderat evidens** | L3-L4, kræver yderligere validering | [Se lægemidler](/evidence-medium/) |
| **AI-forudsigelser** | L5, reference for forskningsretning | [Se lægemidler](/evidence-low/) |
| **Alle lægemidler** | Alle {{ site.data.drug_stats.total_drugs }} lægemidler (søgbar) | [Lægemiddelliste](/drugs/) |
| **Sundhedsnyheder** | Automatisk overvågning af sundhedsnyheder | [Se nyheder](/news/) |
| **FHIR API** | Integrationsendepunkter | [FHIR-metadata](/fhir/metadata) |

---

## Om projektet

DkTxGNN bruger deep learning-modellen **TxGNN**, som Harvards Zitnik Lab har offentliggjort i *Nature Medicine*, til at forudsige mulige nye terapeutiske anvendelser af DKMA-godkendte lægemidler.

> "TxGNN er den første grundmodel designet til klinikercentreret lægemiddelrepositionering; den kombinerer vidensgrafer med deep learning for at forudsige lægemidlers virkning ved sjældne sygdomme."
> <cite>— Huang et al., Nature Medicine (2024)</cite>

### Statistik

| Punkt | Antal |
|------|-------|
| Lægemiddelrapporter | {{ site.data.drug_stats.total_drugs }} |
| Myndighed | Lægemiddelstyrelsen (DKMA) |

[Læs mere](/about/) | [Metode](/methodology/) | [Datakilder](/sources/)

---

## Datakilder

<style>
.data-source-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 1rem; margin: 2rem 0; padding: 1.5rem; background: #f8f9fa; border-radius: 12px; }
.data-source-card { display: flex; flex-direction: column; align-items: center; padding: 1.25rem 1rem; background: white; border-radius: 10px; text-decoration: none; color: #333; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s; }
.data-source-card:hover { transform: translateY(-4px); box-shadow: 0 6px 20px rgba(0,0,0,0.12); }
.data-source-icon { width: 48px; height: 48px; margin-bottom: 0.75rem; display: flex; align-items: center; justify-content: center; border-radius: 12px; font-size: 24px; }
.data-source-card strong { font-size: 0.95rem; margin-bottom: 0.25rem; }
.data-source-card small { font-size: 0.75rem; color: #666; text-align: center; }
</style>

<div class="data-source-grid">
  <a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDE8E8;">🧬</div>
    <strong style="color: #A51C30;">TxGNN</strong>
    <small>Harvard Zitnik Lab</small>
  </a>
  <a href="https://clinicaltrials.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F8;">🏥</div>
    <strong style="color: #205493;">ClinicalTrials.gov</strong>
    <small>NIH's kliniske forsøg</small>
  </a>
  <a href="https://pubmed.ncbi.nlm.nih.gov/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F0F5;">📚</div>
    <strong style="color: #326599;">PubMed</strong>
    <small>Biomedicinsk litteratur</small>
  </a>
  <a href="https://go.drugbank.com/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #FDEDEC;">💊</div>
    <strong style="color: #E74C3C;">DrugBank</strong>
    <small>Lægemiddeldatabase</small>
  </a>
  <a href="https://laegemiddelstyrelsen.dk/" target="_blank" rel="noopener" class="data-source-card">
    <div class="data-source-icon" style="background: #E8F8EE;">🇩🇰</div>
    <strong style="color: #C60C30;">DKMA</strong>
    <small>Lægemiddelstyrelsen</small>
  </a>
</div>

---

<div style="background: #fff3cd; padding: 1rem; border-left: 4px solid #ffc107; border-radius: 4px; margin: 1rem 0;">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er <strong>kun til forskningsformål</strong> og udgør ikke medicinsk rådgivning. Brug af lægemidler bør følge lægens anvisninger. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsvurdering.
<br><br>
<small>Senest opdateret: {{ page.last_modified_at | date: "%Y-%m-%d" }} | Ansvarlig: 藥提醒科技有限公司 (yao.care)</small>
</div>

---

## Om udvikleren

Denne platform er udviklet og drives af **藥提醒科技有限公司** (yao.care). Se siden
<a href="{{ '/about/' | relative_url }}">Om platformen</a> for den fulde baggrund om virksomheden og metoden.
