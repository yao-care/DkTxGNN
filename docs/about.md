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

## Baggrund

<p class="key-answer" data-question="Hvad er DkTxGNN?">
<strong>DkTxGNN</strong> er en forskningsstøtteplatform for lægemiddelrepositionering, bygget på TxGNN-modellen,
som Zitnik Lab ved Harvard University har offentliggjort i <em>Nature Medicine</em>. Platformen forudsiger
udvidelse af indikationer for lægemidler godkendt af DKMA i Danmark. Ud over AI-baserede forudsigelsesscorer
integrerer platformen klinisk evidens fra ClinicalTrials.gov og PubMed, så forskere hurtigt kan vurdere,
hvor troværdig hver enkelt forudsigelse er.
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
model, og dækker integration af nationale lægemiddelregistreringsdata, dobbelt forudsigelse med videngraf og
deep learning, evidensgradering ud fra PubMed / ClinicalTrials samt SMART on FHIR-integration
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
<a href="https://www.nature.com/articles/s41591-023-02233-x">TxGNN</a> er en deep learning-model
udviklet af Zitnik Lab ved Harvard Medical School og offentliggjort i <em>Nature Medicine</em>.
Den forudsiger nye associationer mellem lægemiddel og sygdom og er den første foundation-model til
lægemiddelrepositionering, der er designet specifikt til klinikere.
</p>

<blockquote class="expert-quote">
"TxGNN integrerer en videngraf med 17.080 biomedicinske entiteter og bruger grafbaserede neurale netværk
til at lære komplekse relationer mellem knuder og dermed forudsige lægemidlers potentielle effekt mod
sjældne sygdomme."
<cite>&mdash; Huang et al., Nature Medicine (2023)</cite>
</blockquote>

---

## Datakilder

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Kilde</th><th>Beskrivelse</th></tr>
</thead>
<tbody>
<tr><td>AI-forudsigelse</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Harvards videngrafbaserede forudsigelsesmodel</td></tr>
<tr><td>Kliniske forsøg</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Globalt register over kliniske forsøg</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Database over biomedicinsk litteratur</td></tr>
<tr><td>Lægemiddelinformation</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Database over lægemidler og targets</td></tr>
<tr><td>Registreringsdata</td><td><a href="https://laegemiddelstyrelsen.dk/">DKMA</a></td><td>Data om lægemiddelgodkendelser i Danmark</td></tr>
</tbody>
</table>

---

## Videnskabeligt grundlag

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

---

## Omfang

| Element | Værdi |
|------|-------|
| Lægemiddelrapporter | 739 |
| Lægemiddelmyndighed | DKMA |
| Udrullede sites | 30 lande / regioner |

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
