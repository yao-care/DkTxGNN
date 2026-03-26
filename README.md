# DkTxGNN - Denmark Drug Repurposing Predictions

Drug repurposing predictions for Denmark using the TxGNN knowledge graph.

## Data Source

- **Lægemiddelstyrelsen** (Danish Medicines Agency)
- Official list of authorised medicines

## Features

- Knowledge graph-based drug repurposing predictions
- FHIR R4 compliant resources
- Evidence collection from ClinicalTrials.gov and PubMed

## Quick Start

```bash
# Install dependencies
uv sync

# Download drug data
python scripts/download_danish_data.py

# Prepare external data
uv run python scripts/prepare_external_data.py

# Run KG prediction
uv run python scripts/run_kg_prediction.py
```

## Disclaimer

This project is for research purposes only and does not constitute medical advice.
Drug repurposing predictions require clinical validation before therapeutic application.

## License

MIT
