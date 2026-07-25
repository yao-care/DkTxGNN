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

## Oversigt over kilder

<table class="comparison-table">
<thead>
<tr><th>Type</th><th>Kilde</th><th>Anvendes til</th></tr>
</thead>
<tbody>
<tr><td>Registreringsdata</td><td><a href="https://laegemiddelstyrelsen.dk/">DKMA</a></td><td>Liste over godkendte lægemidler og indholdsstoffer i Danmark</td></tr>
<tr><td>Forudsigelsesmodel</td><td><a href="https://zitniklab.hms.harvard.edu/projects/TxGNN/">TxGNN</a></td><td>Forudsigelse af association mellem lægemiddel og sygdom</td></tr>
<tr><td>Kliniske forsøg</td><td><a href="https://clinicaltrials.gov/">ClinicalTrials.gov</a></td><td>Evidensgradering (NCT)</td></tr>
<tr><td>Litteratur</td><td><a href="https://pubmed.ncbi.nlm.nih.gov/">PubMed</a></td><td>Evidensgradering (PMID)</td></tr>
<tr><td>Lægemiddelinformation</td><td><a href="https://go.drugbank.com/">DrugBank</a></td><td>Mapning af indholdsstoffer og data om targets</td></tr>
<tr><td>Interaktioner</td><td><a href="https://ddinter2.scbdd.com/">DDInter</a></td><td>Data om lægemiddelinteraktioner</td></tr>
</tbody>
</table>

---

## Licensering

Hver kilde har sin egen licens — kontrollér den, før du citerer:

- **TxGNN**: akademisk brug; citér Huang et al. (2023)
- **ClinicalTrials.gov / PubMed**: offentlige data fra US NIH
- **DrugBank**: ikke-kommerciel brug underlagt licensvilkårene
- **DKMA**: underlagt vilkårene for åbne data hos den danske lægemiddelmyndighed

---

## Opdateringsfrekvens

| Data | Frekvens |
|------|-----------|
| Registreringsdata | Efterhånden som myndigheden offentliggør dem |
| Evidens fra forsøg / litteratur | Indsamles på ny med jævne mellemrum |
| Interaktionsdata | Gennemgås kvartalsvist |

---

## Videnskabelig kildehenvisning

> Huang, K., et al. (2023). A foundation model for clinician-centered drug repurposing. *Nature Medicine*.
> [DOI: 10.1038/s41591-023-02233-x](https://doi.org/10.1038/s41591-023-02233-x)

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

<div class="disclaimer">
<strong>Ansvarsfraskrivelse</strong><br>
Denne rapport er udelukkende til akademisk forskningsreference og <strong>udgør ikke medicinsk rådgivning</strong>. Følg altid din læges anvisninger; juster aldrig din medicin på egen hånd. Enhver beslutning om lægemiddelrepositionering kræver fuld klinisk validering og myndighedsgodkendelse.
<br><br>
<small>Gennemgået af: 藥提醒科技有限公司 (yao.care)</small>
</div>
