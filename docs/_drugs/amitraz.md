---
layout: default
title: Amitraz
parent: Moderat evidens (L3-L4)
nav_order: 34
evidence_level: L4
indication_count: 10
---

# Amitraz
{: .fs-9 }

Evidensniveau: **L4** | Forudsagte indikationer: **10** stk.
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

# Amitraz: Fra akaricid (ingen human indikation oplyst) til alopeci

## Resumé i én sætning

Amitraz er et akaricid (middemiddel), og i Danmark er det kun registreret i produktet Apivar, en strip til bistader. Der er ingen godkendt human indikation i datagrundlaget. TxGNN-modellen forudsiger, at amitraz kan have effekt ved **alopeci**, men der er **0 kliniske forsøg** og kun **dyrelitteratur** bag forudsigelsen. Litteraturen viser, at amitraz behandler den mideinfestation, der forårsager hårtab hos dyr, ikke at det genopretter hårvækst hos mennesker.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Ikke oplyst i datagrundlaget (det danske produkt Apivar er en bistadestrip, hvilket tyder på veterinær brug uden for mennesker) |
| Forudsagt ny indikation | Alopeci |
| TxGNN-forudsigelsesscore | 98,42 % |
| Evidensniveau | L4 |
| Status på det danske marked | Markedsført |
| Antal markedsføringstilladelser | 1 |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse (ikke) rimelig?

Detaljerede mekanismedata for amitraz mangler i DrugBank. Amitraz er et formamidin-akaricid. Hos mider virker det som agonist på oktopaminreceptorer, og hos pattedyr som alfa-2-adrenerg agonist.

Litteraturen kobler kun amitraz til alopeci indirekte. Hårtab er et symptom på infestation med Demodex, Sarcoptes og Chorioptes hos dyr, og amitraz behandler miden, ikke hårtabet. Efter behandling kommer håret tilbage, fordi den underliggende årsag er fjernet. Det er ikke dokumentation for effekt ved human alopeci (androgenetisk, areata m.fl.).

Den høje score (0,984) understøttes derfor ikke af en direkte biologisk mekanisme for hårvækst. Alfa-2-agonisme hos pattedyr giver desuden sikkerhedsbekymringer (sedation, bradykardi, hypotension, hyperglykæmi).

De øvrige forudsigelser er kun modelbaserede (L5), uden forsøg eller litteratur, og de er sandsynligvis artefakter fra grafspredning i fænotypeklyngen alopeci/hypotrichose:

- **Hypotrichosis simplex i hovedbunden** (98,32 %): en genetisk lidelse i hårsækkene uden plausibel kobling til amitraz.
- **Kongenital hypotrichose med milia** (98,24 %): en sjælden udviklingsforstyrrelse uden biologisk begrundelse.
- **Benign prostatahyperplasi** (98,04 %): godkendte lægemidler er alfa-1-antagonister, mens amitraz er alfa-2-agonist, så mekanismen understøtter ikke gavn.
- **Diffus alopecia areata** (98,02 %): en autoimmun sygdom, hvor amitraz ikke har nogen kendt relevant immunmodulerende virkning.

---

## Klinisk evidens fra forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidens

Alle publikationer er dyrestudier (hund, kat, alpaka, fritte, hamster m.fl.). Ingen omhandler mennesker. Der er ingen RCT'er. Tabellen viser de 10 mest relevante af 15 fundne.

| PMID | År | Type | Tidsskrift | Hovedfund |
|------|-----|------|------|---------|
| [22488596](https://pubmed.ncbi.nlm.nih.gov/22488596/) | 2012 | Review | Compendium | Opdatering om behandling af hundens demodikose. Amitraz-skyl (0,025 %) eller makrocykliske laktoner virker. Højere koncentration og hyppigere brug øger både succesrate og risiko for bivirkninger |
| [22167167](https://pubmed.ncbi.nlm.nih.gov/22167167/) | 2011 | Review | Tierarztl Prax Ausg K | Evidensbaseret gennemgang af behandling af hundens demodikose. Alopeci er et kendetegn ved sygdommen |
| [6504010](https://pubmed.ncbi.nlm.nih.gov/6504010/) | 1984 | Review | Modern Veterinary Practice | Demodikose hos katte med ikke-kløende alopeci. Behandlet med topisk kalksvovlopløsning |
| [8833611](https://pubmed.ncbi.nlm.nih.gov/8833611/) | 1996 | Review (jf. klassificering) | Veterinary Quarterly | Demodikose hos to ilder med lokal alopeci. Amitraz-behandling var effektiv uden mærkbare bivirkninger |
| [32814497](https://pubmed.ncbi.nlm.nih.gov/32814497/) | 2021 | Case-rapport | N Z Vet J | Sarkoptisk og chorioptisk fnat hos en flok alpakaer, behandlet med topisk amitraz og subkutan ivermectin |
| [17610494](https://pubmed.ncbi.nlm.nih.gov/17610494/) | 2007 | Case-rapport | Vet Dermatol | Tre alpakaer med sarkoptisk fnat, som ikke responderede på eprinomectin og doramectin, blev behandlet med succes med amitraz |
| [19265536](https://pubmed.ncbi.nlm.nih.gov/19265536/) | 2009 | Ikke klassificeret (case) | Parasit Vectors | Amitraz + metaflumizon (spot-on) mod generaliseret demodikose hos hund |
| [25648673](https://pubmed.ncbi.nlm.nih.gov/25648673/) | 2015 | Ikke klassificeret (udbrudsrapport) | J Vet Med Sci | Udbrud af sarkoptisk fnat hos maraer i zoo. Fuld bedring efter koloniomfattende akaricidbehandling |
| [34644900](https://pubmed.ncbi.nlm.nih.gov/34644900/) | 1995 | Ikke klassificeret (case) | Vet Dermatol | Chihuahua med demodexmider. Efter 4 måneders amitraz-bade var hudskrab negative, og håret voksede ud igen |
| [7492657](https://pubmed.ncbi.nlm.nih.gov/7492657/) | 1995 | Case-rapport | J Vet Med Sci | Demodikose hos guldhamster. Amitraz i kombination med selensulfid var ikke fuldt effektivt, og coumaphos gav fuld helbredelse |

---

## Oplysninger om det danske marked

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28105938717 | Apivar (Veto Pharma SAS) | Bistadestrip | Ikke oplyst i datagrundlaget |

---

## Sikkerhedsovervejelser

Der er ingen tilgængelige data om advarsler, kontraindikationer eller lægemiddelinteraktioner i datagrundlaget. Se det godkendte produktresumé (SmPC) for sikkerhedsoplysninger.

Ud fra amitraz' farmakologi (alfa-2-agonisme) er der en teoretisk risiko for sedation, bradykardi, hypotension og hyperglykæmi. Ved forgiftning kan der desuden ses CNS-depression og urinretention. Disse oplysninger stammer fra mekanistisk vurdering, ikke fra produktresuméet.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Evidensen er på niveau L4. Den består udelukkende af dyrestudier, hvor amitraz behandler mideinfestation og derved indirekte løser hårtab, og den kan ikke overføres til human alopeci. Der er ingen kliniske forsøg, ingen mekanistisk kobling til hårvækst og en relevant sikkerhedsprofil for et systemisk alfa-2-agonistisk stof.

**For at komme videre kræves:**
- Produktresumé og indlægsseddel fra Lægemiddelstyrelsen (blokerende datahul: advarsler og kontraindikationer mangler, så sikkerhedsscreening ikke kan gennemføres)
- Mekanismedata (MOA) fra DrugBank
- Præklinisk eller mekanistisk evidens for en effekt på hårsækkene eller relevante veje ved human alopeci
- Vurdering af ruteforenelighed og human sikkerhed ved topisk eller systemisk brug, herunder alfa-2-relaterede bivirkninger

*Resultaterne er kun til forskningsbrug og udgør ikke medicinsk rådgivning. Forudsigelser fra TxGNN kræver klinisk validering, før de kan anvendes.*
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

