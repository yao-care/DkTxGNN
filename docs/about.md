---
layout: default
title: Om platformen
nav_order: 90
permalink: /about/
description: "DkTxGNN er en platform til forudsigelse af lægemiddelrepositionering udviklet af 藥提醒科技有限公司 (yao.care), bygget på Harvards TxGNN-model og dækkende DKMA-godkendte lægemidler i Danmark."
---

# Om platformen

<div class="key-takeaway">
Vi accelererer evidensvalidering af lægemiddelrepositionering med AI — fra forudsigelse til evidens på ét blik.
</div>

---

<!-- local-facts:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改）-->
## Danmark: webstedets data i tal

Lokale data: [Lægemiddelstyrelsen: Liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/). De lokale data er Lægemiddelstyrelsens liste over godkendte lægemidler og listen over afregistrerede lægemidler. Afregistrerede tilladelser tælles ikke som gyldige.

| Punkt | Værdi |
|---|---|
| Lægemidler med offentliggjort rapport | {{ site.data.local_facts.drugs_total }} |
| Lægemidler i de lokale data | {{ site.data.local_facts.licence.drugs_with_data }} |
| …med mindst én gyldige post | {{ site.data.local_facts.licence.drugs_with_current }} |
| …med poster, men ingen gyldige | {{ site.data.local_facts.licence.drugs_none_current }} |
| Lægemidler uden for de lokale data | {{ site.data.local_facts.licence.drugs_without_data }} |
| Lokale poster (tilladelser fra Lægemiddelstyrelsen) | {{ site.data.local_facts.licence.items_total }} |
| …heraf gyldige | {{ site.data.local_facts.licence.items_current }} |
| Poster i kontrolloggen | {{ site.data.local_facts.reviews.records }} |
| Lægemiddelsider med kontrollog | {{ site.data.local_facts.reviews.public_pages_with_records }} |
| Forudsagte par af lægemiddel og sygdom, som intet andet TxGNN-websted har | {{ site.data.local_facts.cross.unique_pairs }} |

{% if site.data.local_facts.top_licensed.size > 0 %}Lægemidler med flest gyldige tilladelser fra Lægemiddelstyrelsen: {% for r in site.data.local_facts.top_licensed %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.lv }}){% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}

{% if site.data.local_facts.recent_reviews.size > 0 %}Seneste rettelser i kontrolloggen: {% for r in site.data.local_facts.recent_reviews limit: 8 %}[{{ r.t }}]({{ r.u | relative_url }}) ({{ r.d }}): {{ r.s }}{% unless forloop.last %}; {% endunless %}{% endfor %}{% endif %}

Eksempler på forudsigelser, som intet andet TxGNN-websted har for samme lægemiddel: [Amprenavir]({{ '/drugs/amprenavir/' | relative_url }}) → Felint ervervet immundefektsyndrom, [Doramectin]({{ '/drugs/doramectin/' | relative_url }}) → Insomni, [Isocarboxazid]({{ '/drugs/isocarboxazid/' | relative_url }}) → paranoid personality disorder, [Phenprocoumon]({{ '/drugs/phenprocoumon/' | relative_url }}) → Heparin cofactor 2-mangel.

<!-- local-facts:end -->

## Baggrund

<p class="key-answer" data-question="Hvad er DkTxGNN?">
<strong>DkTxGNN</strong> er en forskningsstøtteplatform for lægemiddelrepositionering, bygget på TxGNN-modellen,
som Zitnik Lab ved Harvard University har offentliggjort i <em>Nature Medicine</em>. Platformen forudsiger
udvidelse af indikationer for lægemidler godkendt af DKMA i Danmark. Ud over AI-baserede forudsigelsesscorer
integrerer platformen klinisk evidens fra ClinicalTrials.gov og PubMed, så forskere hurtigt kan vurdere,
hvor troværdig hver enkelt forudsigelse er.
</p>

<p>
Se <a href="{{ '/guide/' | relative_url }}">Brugervejledningen</a> for, hvordan du slår et lægemiddel op
og fortolker evidensniveauerne i en rapport.
</p>

---

## Om udvikleren

Denne platform er udviklet og drives af **藥提醒科技有限公司** (yao.care, virksomhedsregistreringsnummer
83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

DkTxGNN er Danmarks-sitet i virksomhedens produktlinje "TxGNN Drug Repurposing".
Det samme system er udrullet i 30 lande og regioner, hver med navnet `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN og så videre) på `{cc}txgnn.yao.care`.
Produktoversigt: <https://www.yao.care/medical/txgnn/>.

Selve TxGNN-modellen er udviklet af Zitnik Lab ved Harvard Medical School og offentliggjort
i *Nature Medicine*. Denne platform er det produktionssystem, 藥提醒科技有限公司 har bygget oven på den
model, og dækker integration af nationale lægemiddelregistreringsdata, forudsigelse med deep learning, hvor anvendelser, der allerede står i vidensgrafen, er udelukket, evidensgradering ud fra PubMed / ClinicalTrials samt SMART on FHIR-integration
med elektroniske patientjournaler.

---

## Hvad er lægemiddelrepositionering?

<p class="key-answer" data-question="Hvad er lægemiddelrepositionering?">
<strong>Lægemiddelrepositionering</strong> vil sige at finde nye terapeutiske anvendelser for eksisterende lægemidler.
Sammenlignet med at udvikle et nyt lægemiddel fra bunden — 10 til 15 år og 1&ndash;2 mia. USD —
tager repositionering 3 til 5 år og 100&ndash;300 mio. USD, og der findes allerede sikkerhedsdata fra mennesker,
så risikoen for fiasko er lavere.
</p>

<table class="comparison-table">
<thead>
<tr><th>Aspekt</th><th>Udvikling af nyt lægemiddel</th><th>Lægemiddelrepositionering</th></tr>
</thead>
<tbody>
<tr><td>Tid</td><td>10&ndash;15 år</td><td>3&ndash;5 år</td></tr>
<tr><td>Omkostning</td><td>1&ndash;2 mia. USD</td><td>100&ndash;300 mio. USD</td></tr>
<tr><td>Sikkerhedsdata</td><td>Skal etableres</td><td>Data fra mennesker foreligger allerede</td></tr>
<tr><td>Risiko for fiasko</td><td>Meget høj (&gt;90 %)</td><td>Lavere</td></tr>
</tbody>
</table>

---

## Hvad er TxGNN?

<p class="key-answer" data-question="Hvad er TxGNN?">
<a href="https://www.nature.com/articles/s41591-024-03233-x">TxGNN</a> er en deep learning-model
udviklet af Zitnik Lab ved Harvard Medical School og offentliggjort i <em>Nature Medicine</em>.
Den forudsiger nye associationer mellem lægemiddel og sygdom og er den første foundation-model til
lægemiddelrepositionering, der er designet specifikt til klinikere.
</p>

<blockquote class="expert-quote">
"TxGNN integrerer en vidensgraf med 17.080 sygdomme og bruger grafbaserede neurale netværk
til at lære komplekse relationer mellem knuder og dermed forudsige lægemidlers potentielle effekt mod
sjældne sygdomme."
<cite>&mdash; Huang et al., Nature Medicine (2024)</cite>
</blockquote>

---

## Datakilder

Platformens datakilder (TxGNN-forudsigelse, kliniske forsøg, litteratur, DrugBank og den lokale
lægemiddelliste) samt deres licenser og opdateringsfrekvens er beskrevet på siden
<a href="{{ '/sources/' | relative_url }}">Datakilder</a>.

---

## Videnskabeligt grundlag

> Huang, K., et al. (2024). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-024-03233-x](https://doi.org/10.1038/s41591-024-03233-x)

---

## Omfang

| Element | Værdi |
|------|-------|
| Lægemiddelrapporter | {{ site.data.drug_stats.total_drugs }} |
| Lægemiddelmyndighed | DKMA |
| Udrullede sites | 30 lande / regioner |

---

## Ofte stillede spørgsmål

<p class="key-answer" data-question="Kan man downloade et gratis datasæt med forudsigelser om lægemiddelrepositionering?">
<strong>Nej, ikke som én samlet fil.</strong> DkTxGNN er bygget til at blive brugt rapport for rapport, ikke som et
bulk-datasæt til download. Al evidens er gratis tilgængelig direkte fra kilden: åbn en lægemiddelrapport
og klik videre til de tilknyttede forsøg på ClinicalTrials.gov eller artikler på PubMed for at se den
underliggende dokumentation for netop den forudsigelse.
</p>

---

## Kontakt

- **GitHub Issues**: <https://github.com/yao-care/DkTxGNN/issues>
- **Udvikler**: 藥提醒科技有限公司 (<https://www.yao.care>, service@yao.care)
- **Produktoversigt**: <https://www.yao.care/medical/txgnn/>

---

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
