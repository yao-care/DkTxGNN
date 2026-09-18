---
layout: default
title: Altrenogest
parent: Kun modelforudsigelse (L5)
nav_order: 31
evidence_level: L5
indication_count: 10
---

# Altrenogest
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

# Altrenogest: Fra veterinær progestogen til orofacial spaltesyndromer

## Ét-sætnings sammenfatning

Altrenogest er en synthetisk progestogen, der udelukkende bruges inden for veterinærmedicin (primært til at undertrykke østrus og opretholde graviditet hos hopper og søer), uden godkendt human indikation og uden markedsføringstilladelse i Danmark.
TxGNN-modellen forudsiger, at det kan være effektivt for **orofacial spaltesyndromer** som dets toprangerede indikation med en forudsigelsesscore på **98.06%**.
Der er dog **ingen kliniske forsøg og ingen publiceret litteratur**, der understøtter denne retning, og analyse af mekanistisk rationale antyder stærkt, at denne forudsigelse repræsenterer en **falsk positiv model** snarere end en ægte terapeutisk mulighed.

---

## Hurtig oversigt

| Emne | Indhold |
|------|---------|
| Oprindelig indikation | Ingen godkendt human indikation — veterinær progestogen (østrusundertrykkelse, gravideopretholding hos dyr) |
| Forudsagt ny indikation | Orofacial spaltesyndromer |
| TxGNN forudsigelsesscore | 98.06% |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Ikke markedsført |
| Antal markedsføringstilladelser | 0 |
| Anbefalet afgørelse | Afvent |

---

## Hvorfor er denne forudsigelse rimelig?

Altrenogest er en potent synthetisk progestogen, der tilhører 19-nor-testosteron-klassen af progestiner. Dets primære etablerede brug er inden for veterinærmedicin — specifikt til at synkronisere østrus hos gylte og til at opretholde graviditet hos hopper ved at supplere endogene progesteronniveauer via progesteronreceptor (PR) agonisme. Det har ingen godkendt human indikation, og human eksponering anses for at være en betydelig sikkerhedsrisiko (det er klassificeret som en hudabsorptions-hazard i arbejdsmiljøer).

TxGNN-modellens toprangerede forudsigelser for Altrenogest — orofacial spaltesyndromer, interventrikular septum-aneurisme, Jeune-syndrom med situs inversus og varianter af Pierre Robin-syndrom — er alle medfødte strukturelle defekter. Kritisk set er forbindelsen mellem progestogener og orofacial spalter dokumenteret i den videnskabelige litteratur et **teratogent risikosignal**, ikke en terapeutisk. Tidlige observationsstudier rejste bekymringer om, at gestationel progestogeneksponering kan øge risikoen for ganespalte; knowledge graph'et synes at have mislært denne "lægemiddel-uønsket effekt/risikofaktor"-kant som en "lægemiddel-behandling"-relation, hvilket genererer en falsk høj-konfidenscore.

Fra et biologisk synspunkt har ingen af de forudsagte tilstande — kraniofaciale strukturelle malformationer, kardiale septale anomalier, ciliopati-drevet thorakal dystrofi eller kromosomalt-drevet mandibulær hypoplasi — nogen anerkendt farmakologisk mekanisme, hvorigennem progesteronreceptor-agonisme kunne give behandlingsforbedring. Dette er faste anatomiske eller genetisk-drevne defekter, for hvilke hormonsuplementering ingen etableret korrektiv vej har. Konsensus på tværs af alle fem unikke forudsagte indikationer er, at disse forudsigelser meget sandsynligt er falske positiver, som stammer fra topologiske artefakter i knowledge graph'et, snarere end ægte lægemiddel-sygdoms terapeutiske relationer.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Litteraturevidence

Der er i øjeblikket ingen relateret litteratur til rådighed.

---

## Sikkerhedshensyn

Detaljerede humane sikkerhedsdata (vigtige advarsler, kontraindikationer og lægemiddelinteraktioner) er ikke tilgængelige i den aktuelle Evidence Pack. Se venligst den godkendte produktresumé (SmPC) og relevante retningslinjer for arbejdsmiljøsikkerhed for sikkerhedsinformation. Bemærk, at Altrenogest har en velkendt **transdermal absorptions-hazard** i arbejdsmiljøer og anses for at være potentielt skadelig for mennesker ved hudkontakt; dette bør tages i betragtning, hvis nogen forsøgsvis human brug nogensinde blev overvejet.

---

## Konklusion og næste trin

**Afgørelse: Afvent**

**Begrundelse:**
Alle ti forudsagte indikationer (fem unikke sygdomme, hver optræder to gange i rangeringen) har et L5-evidensniveau — hvilket betyder, at forudsigelserne hviler udelukkende på TxGNN-modeloutputtet uden bekræftende kliniske forsøg eller publiceret litteratur. Desuden identificerer mekanistisk analyse for hver forudsagt indikation de høje scores som sandsynligvis falske positiver, som stammer fra et teratogent signal, der bliver fejlklassificeret som en terapeutisk relation i knowledge graph'et. Altrenogest har ingen godkendt human indikation, markedsføres ikke i Danmark og er primært en veterinær forbindelse med kendte humane sikkerhedsrisici. Der er i øjeblikket ingen videnskabelig rationale til at retfærdiggøre fremskridt af denne kandidat.

**For at fortsætte ville følgende være nødvendig:**
- Uafhængig ekspertgennemgang for formelt at vurdere, om TxGNN-forudsigelserne repræsenterer graph-topologi artefakter (falske positiver) og, hvis så, flag DB11372 til udelukkelse fra humane repurposing-pipelines
- Hentning af fulde virkningsmekanismedata fra DrugBank (DG002) og humane sikkerhedsdata / kontraindikationsdata (DG001) før yderligere evaluering
- Hvis en fremtidig hypotese blev genereret ved en alternativ metode (ikke de aktuelle TxGNN top-10), ville en de novo litteraturgennemgang og prospektiv biologisk plausibilitets-vurdering være påkrævet før nogen forsøgstrin
- Vurdering af, hvorvidt Altrenogest bør udelukkes fra repurposing-kandidatpuljen givet dets veterinær-kun status og kendt human hazard-profil

---

> **Ansvarsfraskrivelse:** Denne rapport er genereret til forskningsreferenceformål alene og udgør ikke medicinsk rådgivning. Alle lægemiddel-repurposing-kandidater kræver klinisk validering før anvendelse i humanmedicin.

## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

