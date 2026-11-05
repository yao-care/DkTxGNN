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

## Den registreredes rettigheder

Dette site har ingen konti og gemmer ingen personoplysninger på egne servere (det har ingen). Brugsstatistikken
indsamles af Google Analytics 4; du kan blokere eller slette dets cookies i dine browserindstillinger.
Har du spørgsmål til denne politik, kan du kontakte service@yao.care.

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
