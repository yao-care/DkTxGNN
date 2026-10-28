---
layout: default
title: Tropicamide
parent: Kun modelforudsigelse (L5)
nav_order: 862
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-14
description: "Tropicamide: forudsagt ny indikation Cauda equina-syndrom (evidensniveau L5). Oprindelig indikation: Cycloplegi (fra videnbasen"
monitor_inn: "tropicamide"
predicted_indications: ["cauda equina syndrome", "obsolete neurogenic bladder (disease)", "irritable bowel syndrome"]
---

# Tropicamide
{: .fs-9 }

Evidensniveau: **L5** | Forudsagte indikationer: **3** stk.
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

## Tropicamid: Fra cycloplegi til cauda equina-syndrom
{: .text-alpha }

## Resumé i én sætning

Tropicamid er et antimuskarint middel, der oprindeligt bruges til at lamme øjets akkommodation (cycloplegi) og udvide pupillen.
TxGNN-modellen forudsiger, at det kan være effektivt ved **cauda equina-syndrom**,
men der er **0 kliniske forsøg** og **0 publikationer**, der understøtter denne retning. Forudsigelsen er udelukkende beregningsbaseret.

---

## Hurtigt overblik

| Punkt | Indhold |
|------|------|
| Oprindelig indikation | Cycloplegi (fra videnbasen; de danske markedsføringstilladelser indeholder ingen indikationstekst) |
| Forudsagt ny indikation | Cauda equina-syndrom |
| TxGNN-forudsigelsesscore | 0.9953 |
| Evidensniveau | L5 |
| Markedsstatus i Danmark | Markedsført (gyldige tilladelser: 3 af 3) |
| Antal markedsføringstilladelser | 3 (gyldige: 3) |
| Anbefalet beslutning | Hold |

---

## Hvorfor er denne forudsigelse rimelig?

Der foreligger i øjeblikket ingen detaljerede data om virkningsmekanismen i de indsamlede data. Tropicamid er dog kendt som en muskarin receptorantagonist med relativt M4-selektivitet. Det blokerer acetylcholins virkning i øjets lukkemuskel og akkommodationsmuskel, hvilket giver pupiludvidelse og cycloplegi.

Forbindelsen til cauda equina-syndrom er spekulativ. Antimuskarin virkning kunne i teorien dæmpe detrusoroveraktivitet ved den blæredysfunktion, der ledsager syndromet. Den underliggende årsag er imidlertid mekanisk kompression af lumbosakrale nerverødder, som kræver kirurgisk dekompression, og antimuskarine midler behandler ikke dette. Tropicamid findes desuden kun som øjenpræparater med minimal systemisk eksponering.

De to næstbedst rangerede forudsigelser er mekanistisk mere plausible på klasseniveau, men uden data for tropicamid selv:
- **Neurogen blære** (score 0,9913): Muskarin antagonisme er en valideret mekanisme ved neurogen detrusoroveraktivitet (fx oxybutynin, tolterodin, solifenacin). Tropicamid har ingen oral eller intravesikal formulering, og etablerede antimuskarine midler dækker allerede indikationen. Sygdomstermen er markeret som forældet og bør tilknyttes en aktuel ontologiterm.
- **Irritabel tarm-syndrom** (score 0,9912): Antispasmodiske midler som hyoscin og dicyclomin bruges mod mavesmerter og kramper, men tropicamid har ingen klinisk evidens og negligerbar eksponering i tarmen.

---

## Evidens fra kliniske forsøg

Der er i øjeblikket ingen relaterede kliniske forsøg registreret.

---

## Evidens fra litteraturen

Der er i øjeblikket ingen relateret litteratur tilgængelig.

---

## Markedsinformation for Danmark

| Markedsføringstilladelse | Produktnavn | Lægemiddelform | Godkendt indikation |
|---------|------|------|-----------|
| 28100599271 | Mydriacyl (Alcon Nordic A/S) | Øjendråber, opløsning | Ikke angivet i de indsamlede data |
| 28103905906 | Mydriasert (Laboratoires Thea S.A.S.) | Øjenlamel | Ikke angivet i de indsamlede data |
| 28105410714 | Mydrane (Laboratoires Thea S.A.S.) | Injektionsvæske, opløsning | Ikke angivet i de indsamlede data |

Alle tre tilladelser er gyldige enkeltstofpræparater.

---

## Sikkerhedsovervejelser

Produktresuméets advarsler og kontraindikationer indgår ikke i de indsamlede data. Se det godkendte produktresumé (SmPC) for fuldstændige sikkerhedsoplysninger.

- **Mulige kontraindikationer fra videnbasen** (fra lægemiddel-sygdomsrelationer i TxGNN-videnbasen, ikke fra produktresuméet): snævervinklet/lukketvinklet glaukom, åbenvinklet glaukom, okulær hypertension, hypertension, diabetes mellitus, diabetisk ketoacidose, pludseligt hjertestop, hjerteledningsforstyrrelser, hyperthyreoidisme (inkl. Graves' sygdom og thyreotoksikose), myokardieiskæmi og koronarsygdom.
- **Lægemiddelinteraktioner**: 16 mulige interaktioner er identificeret, alle uden angivet alvorlighedsgrad. Blandt de anførte lægemidler er atropin, brimonidin, lidocain, warfarin, fluconazol, simvastatin, prednisolon, famotidin, vancomycin og kaliumchlorid. Klinisk betydning skal vurderes ud fra produktresuméet.

---

## Konklusion og næste skridt

**Beslutning: Hold**

**Begrundelse:**
Forudsigelsen hviler alene på en computermodel (L5) uden kliniske forsøg eller publikationer. Den biologiske sammenhæng er svag, fordi cauda equina-syndrom skyldes mekanisk nervekompression, og tropicamid kun findes som øjenpræparater med minimal systemisk eksponering.

**For at komme videre kræves:**
- Data om virkningsmekanisme (MOA) fra DrugBank
- Produktresuméer fra Lægemiddelstyrelsen med advarsler og kontraindikationer (blokerende datamangel for sikkerhedsscreening)
- Præklinisk eller mekanistisk evidens for tropicamid i den forudsagte indikation
- Afklaring af egnet administrationsvej og systemisk eksponering
- Kortlægning af den forældede sygdomsterm (neurogen blære) til en aktuel ontologi, hvis denne forudsigelse skal vurderes videre
## Ansvarsfraskrivelse

Dette indhold er kun til forskningsformål og udgør ikke medicinsk rådgivning.
Klinisk validering er påkrævet før enhver klinisk anvendelse.

---

