# DkTxGNN - Danmark: Repositionering af Laegemidler

[![Website](https://img.shields.io/badge/Website-dktxgnn.yao.care-blue)](https://dktxgnn.yao.care)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Forudsigelser for repositionering af laegemidler (drug repurposing) for Danmark ved hjaelp af TxGNN-modellen.

## Ansvarsfraskrivelse

- Resultaterne af dette projekt er kun til forskningsformaal og udgoer ikke medicinsk raadgivning.
- Kandidater til repositionering af laegemidler kraever klinisk validering foer anvendelse.

## Projektoversigt

| Element | Antal |
|---------|-------|
| **Laegemiddelrapporter** | 501 |
| **Samlede Forudsigelser** | 8,553,242 |

## Forudsigelsesmetoder

### Vidensgraf-metode (Knowledge Graph)
Direkte foresoergsel af laegemiddel-sygdomsrelationer i TxGNN-vidensgrafen, identificering af potentielle repositioneringskandidater baseret paa eksisterende forbindelser i det biomedicinske netvaerk.

### Deep Learning-metode
Anvender den fortraenede TxGNN neurale netvaerksmodel til at beregne forudsigelsesscorer, der vurderer sandsynligheden for nye terapeutiske indikationer for godkendte laegemidler.

## Links

- Hjemmeside: https://dktxgnn.yao.care
- TxGNN-artikel: https://doi.org/10.1038/s41591-023-02233-x
