---
layout: default
title: Letrozole
parent: Høj evidens (L1-L2)
nav_order: 491
evidence_level: L1
indication_count: 10
last_modified_at: 2026-10-14
description: "Letrozole: forudsagt ny indikation Kvindelig brystkræft (rang 1) (evidensniveau L1). Oprindelig indikation: Ikke angivet i de indsamlede data (godkendt indikationstekst er tom)"
monitor_inn: "letrozole"
predicted_indications: ["female breast carcinoma", "nipple carcinoma", "estrogen-receptor negative breast cancer", "Ehrlich tumor carcinoma", "estrogen-receptor positive breast cancer", "hormone-resistant breast carcinoma", "bilateral breast carcinoma", "breast carcinoma by gene expression profile", "breast fibrocystic disease", "benign mammary dysplasia"]
---

# Letrozole
{: .fs-9 }

Evidensniveau: **L1** | Forudsagte indikationer: **10** stk.
{: .fs-6 .fw-300 }

---

## Indholdsfortegnelse
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Farmaceutens vurderingsrapport

</div>

# Letrozol: Fra brystkræft til østrogenreceptor-positiv brystkræft

## Resumé i én sætning

Letrozol er en aromatasehæmmer, der i Danmark er markedsført som filmovertrukne tabletter. Den primære forudsigelse fra TxGNN-modellen er **kvindelig brystkræft** (rangeret som nr. 1), og den mest veldokumenterede forudsigelse er **østrogenreceptor-positiv brystkræft** (rangeret som nr. 5). Disse er i praksis allerede etablerede anvendelser og ikke egentlig nyt repurposing. Evidensen omfatter **39 registrerede kliniske forsøg** for den primære forudsigelse samt adskillige fase 3-RCT'er og en metaanalyse for den østrogenreceptor-positive forudsigelse.

*Bemærkning: De data, der er indsamlet til denne rapport, indeholder ingen godkendt indikation for lægemidlet, og virkningsmekanismen mangler. Rapporten tager derfor udgangspunkt i den højest rangerede forudsigelse og i den bedst understøttede forudsigelse (østrogenreceptor-positiv brystkræft). Den ukorrigerede originalindikation bør rettes i grunddata.*

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke angivet i de indsamlede data (godkendt indikationstekst er tom) |
| Forudsagt ny indikation | Kvindelig brystkræft (rang 1); bedst understøttet: østrogenreceptor-positiv brystkræft (rang 5) |
| TxGNN-forudsigelsesscore | 99,98 % (kvindelig brystkræft); 99,75 % (østrogenreceptor-positiv brystkræft) |
| Evidensniveau | L1 |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Proceed with Guardrails |

---

## Hvorfor er forudsigelsen rimelig?

Detaljerede data om virkningsmekanismen er ikke tilgængelige i de indsamlede data. Ud fra kendt farmakologi er letrozol en ikke-steroid aromatasehæmmer, der blokerer omdannelsen af androgener til østrogener og dermed nedsætter den østrogendrevne tumorvækst i hormonreceptor-positiv brystkræft.

Forudsigelsen er derfor biologisk konsistent. Brystkræft med positiv østrogenreceptor afhænger af østrogen for at vokse, og sænkning af østrogenniveauet er den etablerede behandlingsstrategi. Den meget høje TxGNN-score afspejler denne kendte biologi.

Det er vigtigt at bemærke, at forudsigelsen om **østrogenreceptor-negativ brystkræft** (rang 3) ikke er mekanistisk understøttet: Aromatasehæmning forudsætter østrogenafhængig vækst, og de fundne forsøg omhandler HR-positiv sygdom. Mærkatet skyldes sandsynligvis termmapping. Øvrige forudsigelser (fx Ehrlich-tumor, brystfibrocystisk sygdom, benign mammadysplasi) har kun præklinisk eller ingen evidens og bør ikke tillægges vægt.

---

## Evidens fra kliniske forsøg

De mest relevante forsøg for brystkræft (kvindelig brystkræft og østrogenreceptor-positiv brystkræft):

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT02941926](https://clinicaltrials.gov/study/NCT02941926) | Fase 3 | Afsluttet | 3246 | Ribociclib + letrozol ved HR+/HER2- fremskreden brystkræft uden tidligere hormonbehandling; indsamling af sikkerheds- og effektdata |
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Fase 3 | Afsluttet | 666 | Palbociclib + letrozol vs. placebo + letrozol ved ER+/HER2- fremskreden brystkræft (PALOMA-2) |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Fase 3 | Afsluttet | 131 | Adgang til palbociclib + letrozol hos postmenopausale kvinder med HR+/HER2- sygdom |
| [NCT03425838](https://clinicaltrials.gov/study/NCT03425838) | Fase 3 | Aktiv, rekrutterer ikke | 1050 | SONIA: CDK4/6-hæmmer i første vs. andet behandlingsforløb sammen med aromatasehæmmer |
| [NCT06760637](https://clinicaltrials.gov/study/NCT06760637) | Fase 3 | Aktiv, rekrutterer ikke | 1035 | PF-07220060 + letrozol sammenlignet med CDK4/6-hæmmer + letrozol (FOURLIGHT-3) |
| [NCT00908531](https://clinicaltrials.gov/study/NCT00908531) | Fase 3 | Afbrudt | 123 | Dansk DBCG-forsøg: 4 måneders letrozol før operation vs. operation først |
| [NCT00382070](https://clinicaltrials.gov/study/NCT00382070) | Fase 3 | Ukendt | 3966 | Fem års letrozol vs. placebo efter fem års hormonbehandling ved HR+ brystkræft |
| [NCT04568616](https://clinicaltrials.gov/study/NCT04568616) | Fase 2 | Aktiv, rekrutterer ikke | 178 | Neoadjuverant letrozol ved ER+/HER2- brystkræft hos postmenopausale kvinder (NAOMI) |
| [NCT04272801](https://clinicaltrials.gov/study/NCT04272801) | Fase 2 | Aktiv, rekrutterer ikke | 84 | Præoperativ endokrin behandling hos ældre kvinder for at vejlede strålebehandling |
| [NCT01439711](https://clinicaltrials.gov/study/NCT01439711) | Fase 2 | Afsluttet | 108 | Neoadjuverant letrozol ved ER+ duktalt carcinoma in situ |

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [27959613](https://pubmed.ncbi.nlm.nih.gov/27959613/) | 2016 | RCT | N Engl J Med | Palbociclib + letrozol ved ER+/HER2- fremskreden brystkræft (PALOMA-2) |
| [27717303](https://pubmed.ncbi.nlm.nih.gov/27717303/) | 2016 | RCT | N Engl J Med | Ribociclib som førstelinjebehandling ved HR+ fremskreden brystkræft |
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT | N Engl J Med | Samlet overlevelse med ribociclib + letrozol ved fremskreden brystkræft |
| [38507751](https://pubmed.ncbi.nlm.nih.gov/38507751/) | 2024 | RCT | N Engl J Med | Ribociclib + endokrin behandling ved tidlig brystkræft |
| [38729566](https://pubmed.ncbi.nlm.nih.gov/38729566/) | 2024 | RCT | Ann Oncol | Abemaciclib + ikke-steroid aromatasehæmmer: endelige overlevelsesresultater (MONARCH 3) |
| [35123662](https://pubmed.ncbi.nlm.nih.gov/35123662/) | 2022 | Metaanalyse | Lancet Oncol | Aromatasehæmmere vs. tamoxifen hos præmenopausale kvinder med ovarie-suppression (7030 kvinder) |
| [30475668](https://pubmed.ncbi.nlm.nih.gov/30475668/) | 2019 | Langtidsopfølgning | J Clin Oncol | Adjuverende letrozol og tamoxifen alene eller sekventielt (BIG 1-98) |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT | Ann Oncol | Opdaterede resultater fra MONALEESA-2 |
| [38252901](https://pubmed.ncbi.nlm.nih.gov/38252901/) | 2024 | RCT | J Clin Oncol | Samlet overlevelse med palbociclib + letrozol ved fremskreden brystkræft |
| [25524798](https://pubmed.ncbi.nlm.nih.gov/25524798/) | 2015 | RCT (fase 2) | Lancet Oncol | Palbociclib + letrozol vs. letrozol alene som førstelinjebehandling (PALOMA-1) |

---

## Markedsinformation i Danmark

| Markedsføringstilladelsesnummer | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28104319308 | Letrozol "Accord" (Accord Healthcare B.V.) | Filmovertrukne tabletter | Indikationstekst ikke tilgængelig i de indsamlede data |

---

## Cytotoksicitet

| Punkt | Indhold |
|------|------|
| Cytotoksicitetsklassifikation | Hormonbehandling (aromatasehæmmer); ikke konventionelt cytotoksisk, men anvendes ofte sammen med målrettet behandling (CDK4/6-hæmmere) |
| Myelosuppressionsrisiko | Lav for letrozol alene; ved kombination med CDK4/6-hæmmere kan neutropeni forekomme |
| Emetogenicitetsklassifikation | Lav |
| Monitoreringspunkter | Knogletæthed, lipider, leverfunktion; blodtal (CBC) ved kombination med CDK4/6-hæmmere |
| Håndteringsbeskyttelse | Se produktresuméet (SmPC) for krav til håndtering |

---

## Sikkerhedsovervejelser

- **Sygdomme med kontraindikationssignal i vidensgrafen (ikke mærkningstekst):** leversvigt, skrumpelever, osteoporose (inkl. postmenopausal), hyperbilirubinæmi (inkl. arvelig og Gilberts syndrom) samt cerebrovaskulær sygdom.
- **Lægemiddelinteraktioner:** 350 interaktioner er registreret. Den eneste med angivet sværhedsgrad er aprepitant (moderat). Øvrige omfatter bl.a. calcitriol, glimepirid, lansoprazol, dolasetron, granisetron, famotidin, acetylsalicylsyre, pantoprazol, morfin og metformin (sværhedsgrad ukendt).
- **Bivirkninger beskrevet i litteraturen:** letrozol-relateret makulopati (case report) og tumor-flare/tumorlysesyndrom (case report).

For advarsler og kontraindikationer henvises i øvrigt til det godkendte produktresumé (SmPC).

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails**

**Begrundelse:**
- Flere afsluttede fase 3-RCT'er (bl.a. PALOMA-2, MONALEESA-2, MONARCH 3) og en metaanalyse understøtter letrozolbaseret endokrin behandling ved HR+ brystkræft. Der er tale om en etableret anvendelse og ikke et nyt repurposing-fund. Forudsigelserne for ER-negativ sygdom, Ehrlich-tumor samt benigne brysttilstande bør afvises eller holdes (Hold) på grund af manglende evidens.

**For at komme videre kræves:**
- Rettelse af grunddata: oprindelig indikation og virkningsmekanisme mangler
- Hentning af produktresuméet fra Lægemiddelstyrelsen (advarsler og kontraindikationer mangler; markeret som blokerende datahul)
- Retningslinjer (guardrails): postmenopausal status eller ovarie-suppression, monitorering af knogletæthed samt opmærksomhed på toksicitetsprofilen for kombinerede CDK4/6-hæmmere
- Yderligere vurdering af den hormonresistente brystkræft (rang 6) som forskningsspørgsmål, da effekten primært skyldes kombinationspartneren
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

