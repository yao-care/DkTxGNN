---
layout: default
title: Ritonavir
parent: Kun modelforudsigelse (L5)
nav_order: 383
evidence_level: L5
indication_count: 6
---

# Ritonavir
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **6** stk.
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

# Ritonavir: Fra HIV-1-infektion til Simian Immunodeficiency Virus (SIV)-infektion

## Resumé i én sætning

> Ritonavir er en velkendt HIV-1-proteasehæmmer, der i dag oftest anvendes som en farmakokienetisk booster i kombinerede antiretrovirale behandlingsregimer (strukturerede oprindelige indikationsdata blev ikke returneret af denne bevissamling).
> TxGNN-modellens højest rangerede forudsigelse er **Simian Immunodeficiency Virus (SIV)-infektion** — en lentivirale sygdom hos ikke-menneskelige primater, ikke en menneskelig tilstand —
> med en **forudsigelsesscore på 99,92 %**, men **ingen afsluttede kliniske forsøg** og kun **12 prækkliniske/in vitro-publikationer**, hvoraf ingen etablerer klinisk virkning hos mennesker.

---

## Hurtigt overblik

| Element | Indhold |
|---------|---------|
| Oprindelig indikation | Ikke specificeret i bevissamlingen (Ritonavir er en kendt HIV-1-proteasehæmmer/farmakokienetisk booster — generel farmakologisk viden, ikke hentet fra strukturerede data her) |
| Forudsagt ny indikation | Simian Immunodeficiency Virus (SIV)-infektion *(en ikke-menneskelig primat-sygdom)* |
| TxGNN-forudsigelsesscore | 99,92 % |
| Bevisniveau | L4 (kun prækkliniske/mekanistiske studier — ingen afsluttede kliniske forsøg) |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet beslutning | Udsæt |

---

## Hvorfor er denne forudsigelse rimelig?

Detaljerede data om virkningsmekanisme (MOA) var ikke tilgængelige i denne bevissamling (datafalik DG002). Baseret på generel farmakologisk viden er ritonavir en HIV-1-aspartyl-proteasehæmmer. In vitro- og makak-studier i litteraturen bekræfter, at ritonavir også hæmmer SIV-protease, fordi SIV og HIV begge er lentiviruser med strukturelt homologe protease-enzymer (PMID 12709355, PMID 15040537). Denne krydsreaktivitet forklarer plausibelt, hvorfor TxGNN-modellen forbinder ritonavir med SIV-infektion med en meget høj score.

Denne forudsagte "nye indikation" er imidlertid ikke klinisk brugbar: **SIV-infektion optræder kun hos ikke-menneskelige primater og er ikke en menneskelig sygdom.** Hele understøttende litteratur består af in vitro-modtagelighedsassays eller makak-dyremodeller, der bruges som forskningsværktøjer til HIV-patogenese og antiretroviral forskning — ikke bevis på en behandlingbar menneskelig tilstand. De resterende forudsagte indikationer for ritonavir i denne bevissamling (felin erhvervet immundeficiensyndrom — en sygdom, der kun optræder hos katte — og en sjælden menneskelig neurodevelopmental hvidstofsdisorden uden rationel mekanisme) deler det samme problem: enten er målarten ikke-menneskelig, eller der eksisterer ingen plausibel mekanistisk forbindelse overhovedet.

Dette tyder på, at de nuværende højest rangerede forudsigelser afspejler et ægte mekanistisk signal (protease-krydsreaktivitet på tværs af lentiviruser) snarere end en levedygtig mulighed for menneskelig lægemiddel-genbrug. En klinisk meningsfuld menneskelig indikation for ritonavir skulle identificeres særskilt, højst sandsynligt ved at gennemgå lavere rangerede kandidater eller ved at køre forespørgslen igen mod et kurateret sygdomsvocabularium, der er begrænset til menneskelige tilstande.

---

## Bevis fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret for den højest rangerede forudsagte indikation (SIV-infektion).

*(Bemærk: ét forsøg, [NCT02770508](https://clinicaltrials.gov/study/NCT02770508), blev returneret under den separate kandidat "felin erhvervet immundeficiensyndrom", men det undersøger boostet darunavir + lamivudin hos menneskelige HIV-1-patienter — bevissamlingen selv markerer dette som en tilsyneladende lægemiddel/indikations-uoverensstemmelse i kildedatabasen, ikke ægte understøttende bevis.)*

---

## Bevis fra litteratur

| PMID | År | Type | Tidsskrift | Vigtige resultater |
|------|-----|------|------|---------|
| [12709355](https://pubmed.ncbi.nlm.nih.gov/12709355/) | 2003 | In vitro modtagelighedsstudie | Antimicrobial Agents and Chemotherapy | Ritonavir hemmede SIVmac239-protease (EC50 ≈13 nM), sammenligneligt med dets hæmning af HIV-1 |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In vitro modtagelighedsstudie | Antiviral Therapy | Screenede 16 godkendte anti-HIV-1-lægemidler, herunder ritonavir, mod HIV-2, SIV- og SHIV-stammer |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Dyrestudie (makak-model) | Journal of Virology | Firdobbelt antiretroviral terapi producerede hurtig viral nedbrydning hos SIV-inficerede makaker |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Dyrestudie (neuroimmunn, makak) | mBio | Lentiviral reservoirer forblev i hjernevet trods effektiv antiretroviral terapi |
| [9875393](https://pubmed.ncbi.nlm.nih.gov/9875393/) | 1998 | In vitro farmakologi | Antiviral Chemistry & Chemotherapy | Fluorkinolon-derivat K-12 opretholdt aktivitet mod ritonavir-resistente HIV-1- og SIV-stammer |
| [25033210](https://pubmed.ncbi.nlm.nih.gov/25033210/) | 2014 | Dyrestudie (makak, ART+HDAC) | PLoS ONE | Kombination af cART plus en HDAC-hæmmer undersøgt hos SIV-inficerede resus-makaker for virale reservoir-effekter |
| [17350308](https://pubmed.ncbi.nlm.nih.gov/17350308/) | 2007 | Dyrestudie (SHIV-konstruktion) | Microbes and Infection | Udviklet SHIV bærende HIV-1-protease-gen, brugt som et in vivo-værktøj til test af protease-hæmmere hos makaker |
| [12186895](https://pubmed.ncbi.nlm.nih.gov/12186895/) | 2002 | In vitro virologi | Journal of Virology | Karakteriseret HIV-1-protease-medieret processering af det virale Vif-protein |
| [12951220](https://pubmed.ncbi.nlm.nih.gov/12951220/) | 2003 | Dyrestudie (makak) | Journal of Virological Methods | Oral HAART (herunder lopinavir/ritonavir) evalueret for effekt på CD8-subset hos SHIV-inficerede makaker |
| [11364629](https://pubmed.ncbi.nlm.nih.gov/11364629/) | 1997 | Review/Kommentar | J Int Assoc Physicians AIDS Care | Kort kommentar om chemokinreceptorforskning; minimal direkte relevans |

*(To yderligere lavt relevante poster med ufuldstændig klassificering, PMID 22737073 og PMID 7475727, blev udeladt fra denne tabel.)*

---

## Markedsinformation for Danmark

Ritonavir er i øjeblikket **ikke markedsført** i Danmark ifølge denne bevissamling, med 0 markedsføringstilladelser på fil. Der var ingen Laegemiddelstyrelsen eller EMA-centraliserede godkendelsesrecords til rådighed.

---

## Sikkerhedshensyn

Se venligst det godkendte produktresumé (SmPC) for sikkerhedsinformation.

*(Vigtige advarsler, kontraindikationer og lægemiddel-interaktionsdata var ikke tilgængelige i denne bevissamling — dette er markeret som en blokerende datafalik, se Konklusion nedenfor.)*

---

## Konklusion og næste trin

**Beslutning: Udsæt**

**Begrundelse:**
Den højest rangerede forudsagte indikation, SIV-infektion, er en ikke-menneskelig primat-sygdom og derfor ikke et levedygtigt menneskelig klinisk genbrug-mål, trods en høj TxGNN-score og plausibel protease-krydsreaktivitet-mekanisme. Der eksisterer ingen afsluttede kliniske forsøg for nogen af de højest rangerede kandidater, og sikkerhed/mærkat-data, der er nødvendige selv for en foreløbig sikkerhedsgennemgang, mangler.

**For at fortsætte er følgende nødvendigt:**
- TFDA/SmPC-advarsler og kontraindikationer (blokerende datafalik DG001)
- Bekræftet virkningsmekanisme-data (MOA) (datafalik DG002)
- Omscreening af forudsigelsesindikationslisten for at filtrere ikke-menneskelige sygdomsmål (SIV-infektion, felin AIDS) og identificere en klinisk gyldig menneskelig kandidat
- Undersøgelse af den tilsyneladende lægemiddel/indikations-uoverensstemmelse, der blev markeret for forsøg NCT02770508

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

