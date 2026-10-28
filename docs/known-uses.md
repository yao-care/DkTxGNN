---
layout: default
title: "Kun kendte anvendelser (ingen nye forudsigelser)"
nav_order: 24
permalink: /known-uses/
description: "For disse lægemidler er alle kandidater fra TxGNN-modellen allerede kendte anvendelser (registreret i vidensgrafen eller i en markedsføringstilladelse), så…"
---

# Kun kendte anvendelser (ingen nye forudsigelser)

For disse lægemidler er alle kandidater fra TxGNN-modellen allerede kendte anvendelser (registreret i vidensgrafen eller i en markedsføringstilladelse), så der er ingen ny forudsagt indikation. Hver side viser de kendte anvendelser og den lokale markedsstatus.

{% assign known_drugs = site.drugs | where: "evidence_level", "N/A" | sort: "title" %}

**{{ known_drugs.size }} lægemidler**

| Lægemiddel | Rapport |
|------|------|
{% for drug in known_drugs %}| **{{ drug.title }}** | [Se siden]({{ drug.url | relative_url }}) |
{% endfor %}
