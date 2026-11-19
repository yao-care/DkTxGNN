---
layout: default
title: Downloads
nav_order: 94
permalink: /downloads/
description: "Åbne data til download fra DkTxGNN: FHIR-ressourcer, forudsigelsesresultater og søgeindeks."
---

# Downloads

<div class="key-takeaway">
Forudsigelserne udgives i FHIR R4-format, klar til integration med EPJ-systemer.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Danmark: hvad filerne indeholder nu

| Fil | Indhold nu |
|---|---|
| `/data/search-index.json` | {{ site.data.local_facts.files.search_index }} lægemidler med deres forudsagte indikationer |
| `/data/drugs.json` | {{ site.data.local_facts.files.drugs_json }} lægemidler med evidensniveau og oprindelig indikation |
| `/fhir/MedicationKnowledge/` | {{ site.data.local_facts.fhir.medication_knowledge }} MedicationKnowledge-ressourcer (én pr. lægemiddel) |
| `/fhir/ClinicalUseDefinition/` | {{ site.data.local_facts.fhir.clinical_use_definition }} ClinicalUseDefinition-ressourcer (én pr. forudsagt indikation) |

Genbrug af det lokale datasæt: [Lægemiddelstyrelsen: Liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/), offentliggjort af Lægemiddelstyrelsen; genbrug er underlagt udgiverens vilkår, og dette websted giver ikke yderligere rettigheder.

{% if site.data.local_facts.top_licensed.size > 0 %}Lægemidler med flest gyldige tilladelser fra Lægemiddelstyrelsen: {% for r in site.data.local_facts.top_licensed limit: 5 offset: 3 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Seneste rettelser i kontrolloggen: {% for r in site.data.local_facts.recent_reviews limit: 8 offset: 16 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

<!-- local-facts:end -->

## FHIR-ressourcer

Dette site udgiver forudsigelser som FHIR R4-ressourcer, der kan anvendes direkte af SMART on FHIR-apps:

| Ressource | Sti | Beskrivelse |
|----------|------|-------------|
| CapabilityStatement | `/fhir/metadata` | Capability statement for FHIR-serveren |
| MedicationKnowledge | `/fhir/MedicationKnowledge/` | Lægemiddelressourcer |
| ClinicalUseDefinition | `/fhir/ClinicalUseDefinition/` | Forudsagte indikationer |
| Bundle | `/fhir/Bundle/all-predictions.json` | Alle forudsigelser samlet i ét bundle |

---

## Søgeindeks

`/data/search-index.json` leverer et søgeindeks over lægemidler og indikationer, som du kan bruge til at bygge
din egen forespørgselsgrænseflade.

---

## Anvendelsesvilkår

<ol class="actionable-steps">
<li>Data på dette site er <strong>udelukkende til forskningsreference</strong> og må ikke bruges som grundlag for medicinske beslutninger.</li>
<li>Ved citering skal du kreditere DkTxGNN (藥提醒科技有限公司) og citere den oprindelige TxGNN-artikel.</li>
<li>Videreanvendte data er fortsat underlagt licensvilkårene for hver oprindelig kilde (se <a href="{{ '/sources/' | relative_url }}">Datakilder</a>).</li>
</ol>

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
