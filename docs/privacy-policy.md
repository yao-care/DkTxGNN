---
layout: default
title: Privatlivspolitik
nav_order: 95
permalink: /privacy-policy/
description: "Privatlivspolitik for DkTxGNN: et statisk site uden konti og formularer; det bruger analysecookies fra Google Analytics 4 til brugsstatistik."
---

# Privatlivspolitik

<div class="key-takeaway">
Dette er et statisk site — ingen registrering og ingen formularer. Det bruger analysecookies fra Google Analytics 4 til at udarbejde brugsstatistik.
</div>

---

## Hvad vi indsamler

<p class="key-answer" data-question="Indsamler DkTxGNN persondata?">
<strong>Kun brugsstatistik via Google Analytics 4.</strong> Dette site hostes på GitHub Pages som et rent statisk site. Der
findes intet kontosystem og ingen formularer, og vi indsamler ikke navne, e-mailadresser eller patientjournaler.
Sitet bruger analysecookies fra Google Analytics 4 til at udarbejde brugsstatistik (viste sider, henvisende site,
rulledybde og tid på siden). Cookies sættes, når en side indlæses; søgeord, formularindhold og
URL-forespørgselsparametre sendes ikke.
</p>

---

## Tredjepartstjenester

Sitet anvender følgende tredjepartsressourcer, som kan logge adgang i henhold til deres egne
politikker:

| Tjeneste | Formål | Privatlivspolitik |
|---------|---------|----------------|
| GitHub Pages | Hosting af sitet | [GitHub Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement) |
| Google Analytics 4 (www.googletagmanager.com, google-analytics.com) | Besøgsstatistik (viste sider, henvisende side); bruger analysecookies. Søgeord, formularindhold og URL-parametre sendes ikke. | [Googles privatlivspolitik](https://policies.google.com/privacy) |
| cdn.jsdelivr.net | Scriptbiblioteker: d3-diagrammer på alle sider; Fuse.js til navnematch og SMART on FHIR-klienten på SMART-siderne og i lægemiddelsøgningen på forsiden | [jsDelivrs privatlivspolitik](https://www.jsdelivr.com/terms/privacy-policy-jsdelivr-net) |
| clinicaltrials.gov | Søgning efter kliniske forsøg på SMART-siderne: kun når du beder om det, sendes lægemidlets og indikationens navn til ClinicalTrials.gov-API’et | [NLM’s webpolitikker](https://www.nlm.nih.gov/web_policies.html) |
| rxnav.nlm.nih.gov | SMART-appen: RxNorm-koderne for de lægemidler, der læses fra din elektroniske patientjournal, sendes til NLM’s RxNav-API for at slå navnet på det aktive stof op (ingen patientidentifikatorer) | [NLM’s webpolitikker](https://www.nlm.nih.gov/web_policies.html) |

Når du aktivt starter SMART on FHIR-appen, henter den medicindata fra dit elektroniske
patientjournalsystem. Patientens identitet og journaldata <strong>sendes ikke til dette sites servere</strong> (det er
et statisk site uden backend) og gemmes ikke af dette site. For at matche lægemiddelnavne sender appen
lægemidlernes RxNorm-koder til RxNav-tjenesten hos det amerikanske National Library of Medicine; koderne
indeholder ingen oplysninger, der identificerer patienten. Når du beder om kliniske forsøg, sendes
lægemiddelnavnet og indikationen til ClinicalTrials.gov.

---

<!-- privacy-law:start（母目錄 .claude/gen_local_pages_20261119.py 產生，勿手改；法規與連結見 .claude/privacy_text_20261119.py）-->
## Gældende lovgivning

For besøgende i Danmark gælder [databeskyttelsesforordningen (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj) og [databeskyttelsesloven](https://www.retsinformation.dk/eli/lta/2018/502); cookies er desuden omfattet af cookiereglerne. Tilsynsmyndigheden er [Datatilsynet](https://www.datatilsynet.dk/). Den dataansvarlige har sæde i Taiwan og intet forretningssted i EU; behandlingen omfatter de brugsdata, Google Analytics 4 indsamler via cookies.

## Dine rettigheder, og hvordan du bruger dem

- Ret til indsigt (artikel 15) og til berigtigelse (artikel 16).
- Ret til sletning (artikel 17) og begrænsning (artikel 18).
- Ret til indsigelse (artikel 21), også mod webanalyse.
- Ret til at klage til Datatilsynet (artikel 77).

Henvendelser: service@yao.care. Da webstedet ikke har konti, kan vi kun handle på data hos Google Analytics, hvis du giver os nok oplysninger (fx dato og sider for dit besøg); du kan også blokere eller slette analysecookies i din browser.

## Ophavsret og datakilder

Webstedets tekster er beskyttet efter [ophavsretsloven](https://www.retsinformation.dk/eli/lta/2023/1093). Webstedets kode er udgivet under MIT-licensen i [GitHub-repositoriet](https://github.com/yao-care/DkTxGNN); rapporttekster er © 藥提醒科技有限公司 (yao.care).

Datakilder på dette websted og deres vilkår:

- **TxGNN**-forudsigelsesdata (Harvard Dataverse): CC0 1.0 (frigivet til public domain); citér Huang et al., *Nature Medicine* 2024.
- **ClinicalTrials.gov** og **PubMed**: US National Library of Medicine; se [vilkårene for ClinicalTrials.gov](https://clinicaltrials.gov/about-site/terms-conditions) og [NCBI's politikker](https://www.ncbi.nlm.nih.gov/home/about/policies/) (nogle PubMed-resuméer er stadig omfattet af forlagets ophavsret).
- **DrugBank**-id'er og -data: efter [DrugBank](https://go.drugbank.com/)s licensvilkår (ikke-kommerciel brug).
- **Lokalt datasæt**: [Lægemiddelstyrelsen: Liste over godkendte lægemidler](https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/), offentliggjort af Lægemiddelstyrelsen; genbrug er underlagt udgiverens vilkår, og dette websted giver ikke yderligere rettigheder.

<!-- privacy-law:end -->

---

## Ændringer af denne politik

Eventuelle ændringer offentliggøres direkte på denne side.

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
