---
layout: default
title: Budesonide
parent: Kun modelforudsigelse (L5)
nav_order: 136
evidence_level: L5
indication_count: 10
---

# Budesonide
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **10** stk.
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

# Budesonid: Fra Crohns sygdom og astma til bronkitis

## Resumé i én sætning

Budesonid er en kortikosteroid, der oprindeligt anvendes til Crohns sygdom, inflammatorisk tarmsygdom, astma og allergisk rhinitis.
TxGNN-modellen forudsiger, at lægemidlet også kan have effekt ved **bronkitis** (den bedst understøttede forudsigelse blandt de 10 forudsigelser i de udarbejdede data),
og der er **10 kliniske forsøg** og **20 publikationer** knyttet til denne retning. Størstedelen af dem er dog kun delvist relevante (bronkiolitis, KOL og andre luftvejssygdomme).

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Crohns sygdom, inflammatorisk tarmsygdom, astma og allergisk rhinitis (fra videnbasen; godkendelsesteksterne i Danmark er ikke tilgængelige) |
| Forudsagt ny indikation | Bronkitis (rang 2). Rang 1 er atopisk eksem (score 99,96 %), men den har kun evidensniveau L4 |
| TxGNN-forudsigelsesscore | 99,81 % (bronkitis) |
| Evidensniveau | L2 (bronkitis) |
| Markedsstatus i Danmark | Markedsført |
| Antal markedsføringstilladelser | 3 |
| Anbefalet beslutning | Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger) |

---

## Hvorfor er denne forudsigelse rimelig?

Data om budesonids detaljerede virkningsmekanisme er ikke tilgængelige i de udarbejdede data. Budesonid er dog en potent glukokortikoid med antiinflammatoriske og immunsupprimerende effekter. Det hæmmer inflammatoriske cytokiner og mindsker aktiviteten af eosinofile celler og mastceller.

Den oprindelige brug ved astma og allergisk rhinitis bygger på den samme grundlæggende effekt: dæmpning af slimhindeinflammation i luftvejene. Bronkitis, bronkiolitis og kroniske luftvejssygdomme har overlappende patologi i form af luftvejsinflammation, slimhypersekretion og luftvejshyperreaktivitet. Budesonid/formoterol-kombinationer bruges i forvejen bredt ved KOL, så den mekanistiske plausibilitet og kendskabet til sikkerhed er forholdsvis stærkt.

Der er en vigtig forbehold: Begreberne "bronkitis", "bronkiolitis" og KOL er forskellige, og forsøgene kan derfor ikke slås direkte sammen. Det er også værd at bemærke, at TxGNN-scoren er en modelforudsigelse og ikke i sig selv klinisk evidens.

---

## Klinisk evidens

Tabellen viser de 10 forsøg, der er indgået i dataene. Kun få er direkte relevante.

| Forsøgsnummer | Fase | Status | Antal deltagere | Hovedresultater |
|---------|------|------|------|---------|
| [NCT00202189](https://clinicaltrials.gov/study/NCT00202189) | Fase 4 | Afsluttet | 4 | Akutte effekter af inhalerede kortikosteroider på luftvejsfunktion ved KOL; fysiologisk studie, for lille til effektkonklusioner |
| [NCT00624754](https://clinicaltrials.gov/study/NCT00624754) | Fase 2 | Afsluttet | 32 | Budesonid/formoterol ved bronkiolitis obliterans efter allogen stamcelletransplantation |
| [NCT01560689](https://clinicaltrials.gov/study/NCT01560689) | Fase 2 | Afsluttet | 32 | Åbent studie af inhaleret budesonid/formoterol ved bronkiolitis obliterans efter stamcelletransplantation |
| [NCT00483743](https://clinicaltrials.gov/study/NCT00483743) | Fase 2 | Afsluttet | 62 | Randomiseret, dobbeltblindet 6-ugers studie af inhaleret TPI 1020 mod inhaleret budesonid og placebo ved KOL; fokus på sikkerhed og farmakodynamik |
| [NCT02002715](https://clinicaltrials.gov/study/NCT02002715) | Fase 4 | Afsluttet | 106 | Sammenligning af behandlingsvarighed med inhalerede kortikosteroider ved eosinofil bronkitis |
| [NCT06571942](https://clinicaltrials.gov/study/NCT06571942) | Fase 4 | Ukendt | 128 | Inhalerede tripleterapier og effekt på de små luftveje ved KOL og kronisk bronkitis uden obstruktion |
| [NCT03436225](https://clinicaltrials.gov/study/NCT03436225) | Fase 1 | Ukendt | 80 | Steroidbehandling ved akut bronkiolitis; ikke klart budesonidspecifik |
| [NCT01432080](https://clinicaltrials.gov/study/NCT01432080) | Fase 2 | Afbrudt | 12 | Øget immunsuppression for at forebygge transplantationsassocieret lungesygdom; afbrudt med meget lille stikprøve |

To af de oprindeligt medtagne forsøg er ikke relevante og er udeladt: ibrutinib ved kronisk graft-versus-host-sygdom (NCT04294641) og ivermectin ved COVID-19 (NCT05045937).

---

## Litteraturevidens

| PMID | År | Type | Tidsskrift | Hovedresultater |
|------|-----|------|------|---------|
| [31920296](https://pubmed.ncbi.nlm.nih.gov/31920296/) | 2019 | RCT (forlænget sikkerhedsstudie) | Int J Chron Obstruct Pulmon Dis | Langtidssikkerhed og -effekt af budesonid/glycopyrronium/formoterol hos japanske KOL-patienter |
| [31015757](https://pubmed.ncbi.nlm.nih.gov/31015757/) | 2019 | Metaanalyse | Int J Chron Obstruct Pulmon Dis | Risici ved budesonid/formoterol ved stabil KOL |
| [37954384](https://pubmed.ncbi.nlm.nih.gov/37954384/) | 2023 | Metaanalyse | Heliyon | Inhaleret budesonid og ambroxol hos børn med lungebetændelse og effekt på inflammation |
| [10780759](https://pubmed.ncbi.nlm.nih.gov/10780759/) | 2000 | Klinisk studie (åbent) | Eur Respir J | Luftvejsinflammation, hyperreaktivitet og hoste før og efter inhaleret budesonid ved eosinofil bronkitis |
| [28810628](https://pubmed.ncbi.nlm.nih.gov/28810628/) | 2017 | Klinisk studie | Exp Ther Med | Inhaleret budesonid og terbutalin ved akut astmatisk bronkitis hos børn (n=60) |
| [8620234](https://pubmed.ncbi.nlm.nih.gov/8620234/) | 1996 | Klinisk studie | Arch Pediatr Adolesc Med | Tidlig antiinflammatorisk behandling med vernebliseret cromolyn eller budesonid og færre hvæsende episoder efter bronkiolitis |
| [11129126](https://pubmed.ncbi.nlm.nih.gov/11129126/) | 2000 | Review | Drugs | Budesonid inhalationssuspension til børn og voksne med inflammatoriske luftvejssygdomme |
| [25515181](https://pubmed.ncbi.nlm.nih.gov/25515181/) | 2015 | Retningslinje | Basic Clin Pharmacol Toxicol | Finske retningslinjer for diagnostik og farmakoterapi ved stabil KOL |
| [41654451](https://pubmed.ncbi.nlm.nih.gov/41654451/) | 2026 | Farmakovigilansanalyse | Clin Ther | Realworld-sikkerhed for budesonid/formoterol (FAERS, JADER, CVAR) |
| [9057793](https://pubmed.ncbi.nlm.nih.gov/9057793/) | 1997 | Review | Pediatr Clin North Am | Fremskridt i behandlingen af bronkiolitis og laryngitis |

---

## Markedsinformation i Danmark

Godkendte indikationstekster er ikke tilgængelige i de udarbejdede data.

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28101847396 | Benarhin (McNeil Denmark ApS) | Næsespray, suspension | Ikke angivet |
| 28105358714 | BiResp Spiromax (Teva Pharma B.V.) | Inhalationspulver | Ikke angivet |
| 28106662421 | Riltrava Aerosphere (AstraZeneca AB) | Inhalationsspray, suspension | Ikke angivet |

Alle tre er gyldige enkeltstofpræparater eller præparater med budesonid som del af kombinationen og er markedsført. Ingen er annulleret.

---

## Sikkerhedsovervejelser

- **Kontraindikationer fra videnbasen** (afledt af grafdata, ikke af produktresuméets tekst): hypertension, epilepsi, leversygdom, galdeblæresygdom, hyperglykæmi, mæslinger, kongestiv hjertesvigt, herpes simplex-keratitis, hypofysesvigt og beslægtede væksthormon- og gonadotropinmangeltilstande samt visse stofskiftesygdomme i ureacyklussen (f.eks. citrullinæmi og hyperargininæmi).
- **Lægemiddelinteraktioner**: i alt 1.921 registrerede interaktioner. Blandt de viste er de vigtigste af alvorlig grad **adalimumab** og **fosamprenavir** (Major). Mange er af moderat grad, f.eks. nifedipin, ibuprofen, ketorolac, fluvoxamin, isotretinoin og ethinylestradiol. Interaktionen med formoterol og salbutamol er mindre (Minor).
- **Klasserelaterede signaler fra litteraturen**: binyrebarksuppression ved intranasale kortikosteroider, kontaktallergi og overfølsomhed over for kortikosteroider samt en mulig øget risiko for lungebetændelse ved inhalerede kortikosteroider ved KOL.

Advarsler og kontraindikationer fra produktresuméet er ikke tilgængelige. Se det godkendte produktresumé (SPC) for fuldstændige sikkerhedsoplysninger.

---

## Konklusion og næste skridt

**Beslutning: Proceed with Guardrails (fortsæt med sikkerhedsforanstaltninger)**

**Begrundelse:**
Der er flere fase 2- og fase 4-forsøg samt klinisk litteratur om inhaleret budesonid ved bronkiolitis, eosinofil bronkitis og KOL, og lægemidlet er allerede godkendt og markedsført i Danmark til luftvejssygdom. Evidensen er dog heterogen, består af små forsøg og er ikke specifik for almindelig bronkitis.

De øvrige forudsigelser har svagere evidens: atopisk eksem og "dermatitis, atopic" (som ser ud til at være en dublet) er kun L4 (kun forformuleringsstudier og indirekte litteratur), mens de seks polypforudsigelser (stemmebåndspolyp, mellemøre, epulis, fibroepitelial polyp, livmoderpolyp, polyp i sinus frontalis og ydre øregang) er L5 uden egentlige studier og bør afventer (Hold). Polyp i sinus frontalis er mekanistisk mest plausibel, fordi intranasale kortikosteroider bruges ved kronisk rhinosinuitis med næsepolypper.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresuméets advarsler, kontraindikationer og godkendte indikationer fra Lægemiddelstyrelsen (blokerende datahul for sikkerhedsscreening)
- En klar definition af bronkitis (akut, kronisk, eosinofil) og målrettet søgning efter randomiserede studier med budesonid i netop denne population
- Vurdering af risikoen for lungebetændelse og binyrebarksuppression hos de relevante patientgrupper
- Målrettet litteratursøgning om budesonid ved kronisk rhinosinuitis med næsepolypper, hvis polypgruppen skal undersøges videre
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

