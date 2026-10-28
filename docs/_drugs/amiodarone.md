---
layout: default
title: Amiodarone
parent: Høj evidens (L1-L2)
nav_order: 52
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-28
description: "Amiodarone: forudsagt ny indikation katekolaminerg polymorf ventrikulær takykardi (evidensniveau L1). Oprindelig indikation: Ventrikelflimren"
monitor_inn: "amiodarone"
predicted_indications: ["catecholaminergic polymorphic ventricular tachycardia", "incessant infant ventricular tachycardia", "ventricular tachycardia", "obsolete bundle branch block", "rheumatoid arthritis", "brachydactyly-syndactyly syndrome", "heparin cofactor 2 deficiency", "trichotillomania", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "gout"]
---

# Amiodarone
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Farmaceutens vurderingsrapport

</div>

## Amiodaron: Fra ventrikelflimren til katekolaminerg polymorf ventrikulær takykardi
{: .text-alpha }

## Resumé i én sætning

Amiodaron er et antiarytmisk middel, som oprindeligt anvendes til behandling af ventrikelflimren.
TxGNN-modellen forudsiger, at det også kan være effektivt ved **ventrikulær takykardi**, som er tæt beslægtet med den oprindelige indikation.
Forudsigelsen understøttes af **18 kliniske studier** og **20 publikationer**, herunder to afsluttede fase 3-forsøg (AVID og ALPS).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ventrikelflimren (de danske markedsføringstilladelser indeholder ingen indikationstekst i de data, der er indsamlet til rapporten) |
| Forudsagt ny indikation | Ventrikulær takykardi |
| TxGNN-prædiktionsscore | 0,9978 |
| Evidensniveau | L1 |
| Status på det danske marked | Markedsført (gyldige tilladelser: 1 af 1) |
| Antal markedsføringstilladelser | 1 (gyldige: 1) |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanisme er ikke tilgængelige i de data, der er indsamlet til rapporten. Ud fra kendt viden er amiodaron en multikanalblokker (kalium-, natrium- og calciumkanaler) med betaadrenerg antagonisme. Det forlænger repolarisationen og dæmper re-entry-arytmier i ventriklerne.

Ventrikulær takykardi og ventrikelflimren er nært beslægtede livstruende ventrikulære arytmier og har overlappende mekanismer. Der er derfor reelt tale om en etableret brug snarere end en egentlig ny repurposing.

Bemærk, at de øvrige forudsigelser i modellen (fx katekolaminerg polymorf ventrikulær takykardi, inkessant ventrikulær takykardi hos spædbørn, leddegigt og urinsyregigt) har svagere eller ingen evidens. Denne rapport fokuserer på den bedst understøttede forudsigelse.

---

## Evidens fra kliniske studier

| Studienummer | Fase | Status | Antal deltagere | Hovedfund |
|---------|------|------|------|---------|
| [NCT00000531](https://clinicaltrials.gov/study/NCT00000531) | Fase 3 | Afsluttet | Ikke oplyst | AVID: antiarytmika (primært amiodaron) vs. implanterbar defibrillator hos patienter med overlevet pludselig hjertedød |
| [NCT01401647](https://clinicaltrials.gov/study/NCT01401647) | Fase 3 | Afsluttet | 3.024 | Amiodaron vs. lidokain vs. placebo ved præhospitalt hjertestop pga. VF/VT |
| [NCT00383799](https://clinicaltrials.gov/study/NCT00383799) | Fase 4 | Afbrudt | 302 | PROCAMIO: i.v. amiodaron vs. procainamid ved veltolereret bredkomplekset takykardi |
| [NCT03299517](https://clinicaltrials.gov/study/NCT03299517) | Fase 4 | Ukendt | 80 | Amiodaron vs. lidokain ved stabil VT på skadestue |
| [NCT00257959](https://clinicaltrials.gov/study/NCT00257959) | Fase 4 | Afsluttet | 400 | OPTIC: amiodaron + betablokker vs. sotalol vs. betablokker alene til forebyggelse af ICD-stød |
| [NCT02830360](https://clinicaltrials.gov/study/NCT02830360) | Fase 4 | Afsluttet | 416 | Kateterablation vs. antiarytmisk behandling ved VT efter myokardieinfarkt |
| [NCT01722942](https://clinicaltrials.gov/study/NCT01722942) | Ikke relevant | Ukendt | 1.100 | CHAGASICS: amiodaron vs. ICD ved Chagas-kardiomyopati og non-vedvarende VT |
| [NCT03734562](https://clinicaltrials.gov/study/NCT03734562) | Ikke relevant | Afsluttet | 180 | Substratablation vs. antiarytmika ved iskæmisk kardiomyopati og VT |
| [NCT03855826](https://clinicaltrials.gov/study/NCT03855826) | Fase 4 | Ukendt | 756 | Nifekalant vs. amiodaron ved VT/VF (amiodaron sandsynligvis komparator) |
| [NCT02303639](https://clinicaltrials.gov/study/NCT02303639) | Fase 4 | Ukendt | 120 | Medicinsk antiarytmisk behandling vs. radiofrekvensablation ved iskæmisk VT |

Flere yderligere studier (bl.a. NCT01097330, NCT02114528, NCT04208997) blev afbrudt eller trukket tilbage med meget få deltagere og bidrager derfor kun lidt.

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [27354046](https://pubmed.ncbi.nlm.nih.gov/27354046/) | 2017 | RCT | European Heart Journal | PROCAMIO: sikkerhed og effekt af i.v. procainamid vs. amiodaron ved veltolereret bredkomplekset takykardi |
| [20730062](https://pubmed.ncbi.nlm.nih.gov/20730062/) | 2010 | Review | Vascular Health and Risk Management | Amiodaron er førende antiarytmikum til terminering og forebyggelse af VT/VF |
| [9137212](https://pubmed.ncbi.nlm.nih.gov/9137212/) | 1997 | Review | J Am Coll Cardiol | Gennemgang af farmakologi og effekt af i.v. amiodaron ved maligne ventrikulære arytmier |
| [30084131](https://pubmed.ncbi.nlm.nih.gov/30084131/) | 2018 | Kohorte | Emergency Medicine Australasia | Sikkerhed og effekt af amiodaron givet af paramedicinere ved stabil VT |
| [41217320](https://pubmed.ncbi.nlm.nih.gov/41217320/) | 2026 | Substudie af RCT | J Am Coll Cardiol | VANISH2: kateterablation vs. sotalol eller amiodaron ved VT |
| [37380314](https://pubmed.ncbi.nlm.nih.gov/37380314/) | 2023 | Sekundær analyse | JACC Clin Electrophysiol | VT- og ICD-byrde ved ablation vs. eskaleret antiarytmisk behandling |
| [36878200](https://pubmed.ncbi.nlm.nih.gov/36878200/) | 2023 | Review | Cardiology | Farmakoterapi ved ventrikulære arytmier |
| [28900864](https://pubmed.ncbi.nlm.nih.gov/28900864/) | 2017 | Review | Curr Cardiol Rep | Valg mellem medicin og ablation ved VT med ICD-stød; antiarytmika har begrænset effekt og ugunstig bivirkningsprofil |
| [12028602](https://pubmed.ncbi.nlm.nih.gov/12028602/) | 2002 | Review | Heart Disease | ICD-behandling er overlegen medicinsk behandling i flere studier, hvor amiodaron eller sotalol var komparator |
| [8258259](https://pubmed.ncbi.nlm.nih.gov/8258259/) | 1993 | Casebeskrivelse | Clinical Pharmacy | Amiodaron-induceret thyroideadysfunktion hos patient med recidiverende VT |

---

## Information om det danske marked

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105965717 | Amiodaron "Hameln" | Koncentrat til injektions-/infusionsvæske, opløsning | Indikationstekst ikke tilgængelig i de indsamlede data |

Produktet er en injicerbar formulering fremstillet af hameln pharma GmbH og har gyldig status.

---

## Cytotoksicitet

Ikke relevant: amiodaron er ikke et antineoplastisk lægemiddel.

---

## Sikkerhedsovervejelser

- **Kontraindikationer (fra vidensgraf, ikke fra produktresumé):** Vidensgrafen peger på bl.a. langt QT-syndrom, torsades de pointes, atrioventrikulært blok, sick sinus-syndrom, leversygdom, skjoldbruskkirtelsygdomme (hypo- og hyperthyroidisme), interstitiel lungesygdom, overfølsomhedspneumonitis, optikusneuritis, perifer neuropati, kaliummangel og hornhindeaflejringer.
- **Lægemiddelinteraktioner:** 397 kendte interaktioner er registreret. Blandt de større er amphotericin B (alle formuleringer), clarithromycin, cisaprid, clotrimazol, dexamethason, hydrocortison, dolasetron, eliglustat og agalsidase beta. Moderate interaktioner omfatter bl.a. famotidin, cimetidin, aprepitant og budesonid.
- **Overvågning (ud fra litteratur og kontraindikationsprofil):** Thyroidea-, lunge-, lever- og øjentoksicitet samt QT-forlængelse og proarytmi bør monitoreres.

Se i øvrigt det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger, da advarsler og kontraindikationer fra produktresuméet ikke er tilgængelige i de indsamlede data.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
Ventrikulær takykardi er tæt knyttet til den oprindelige indikation, og der foreligger to afsluttede fase 3-forsøg (AVID og ALPS) samt flere fase 4-sammenligninger. Evidensen er stærk, men amiodarons omfattende toksicitetsprofil og mange interaktioner kræver tæt monitorering.

**For at komme videre kræves:**
- Gennemgang af produktresuméet for Amiodaron "Hameln" for godkendt indikation, advarsler og kontraindikationer
- Data om virkningsmekanisme (MOA) fra DrugBank
- Plan for monitorering af thyroidea-, lunge-, lever- og øjenfunktion samt QT-interval
- Systematisk interaktionsscreening mod patientens øvrige medicin
- Vurdering af, om den injicerbare formulering dækker behovet, eller om en oral formulering er nødvendig til forebyggende behandling
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

