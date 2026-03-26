#!/usr/bin/env python3
"""Danish Medicines Agency drug data loader.

This module loads drug data from the Danish Medicines Agency (Lægemiddelstyrelsen).
Data is obtained from official Excel files at:
https://laegemiddelstyrelsen.dk/en/sideeffects/find-medicines/lists-with-information-about-medicines/

Data source: Authorised medicinal products list (updated daily)
"""

import re
from pathlib import Path
from typing import Optional

import pandas as pd


def load_danish_excel(filepath: Path) -> pd.DataFrame:
    """Load Danish medicines Excel file.

    Args:
        filepath: Path to danish_medicines.xlsx

    Returns:
        DataFrame with Danish medicines data
    """
    # The Excel file has header row
    df = pd.read_excel(filepath, engine="openpyxl")
    return df


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names for consistency.

    Danish Excel columns:
    - Drugid: Drug identifier
    - Navn: Medicine name
    - Lægemiddelform: Dosage form
    - Styrketekst: Strength
    - AktiveSubstanser: Active substances
    - MftIndehaver: Manufacturer
    - ATC-kode: ATC code
    """
    # Map Danish column names to standard names
    column_map = {
        "Drugid": "License_Number",
        "Navn": "Product_Name",
        "Lægemiddelform": "Dosage_Form",
        "Styrketekst": "Strength",
        "AktiveSubstanser": "Active_Ingredients",
        "MftIndehaver": "Manufacturer",
        "ATC-kode": "ATC_Code",
    }

    df = df.rename(columns=column_map)
    return df


def extract_ingredient(name: str) -> str:
    """Extract active ingredient from medicine name.

    Danish names may be like "Paracetamol Krka 500 mg"
    We extract the first word(s) before dosage.
    """
    if pd.isna(name):
        return ""

    name = str(name)

    # Remove dosage patterns like "500 mg", "10 ml", etc.
    name = re.sub(r"\s+\d+[\.,]?\d*\s*(mg|ml|mcg|g|iu|%).*$", "", name, flags=re.IGNORECASE)

    # Remove content in parentheses
    name = re.sub(r"\s*\([^)]*\)", "", name)

    # Remove common brand suffixes
    name = re.sub(r"\s+(tablet|capsule|injection|syrup|cream|ointment|solution|film-coated).*$", "", name, flags=re.IGNORECASE)

    # Clean up
    name = name.strip()

    return name


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load and process Danish drug data.

    This is the main entry point, compatible with the standard TxGNN interface.

    Args:
        filepath: Optional path to Danish data file. If not provided,
                  looks for data in standard locations.

    Returns:
        DataFrame with columns:
            - License_Number: Marketing Authorization number
            - Product_Name: Drug product name
            - Active_Ingredients: Active ingredients
    """
    base_dir = Path(__file__).parent.parent.parent.parent
    data_dir = base_dir / "data"
    raw_dir = data_dir / "raw"

    # Try to find Danish data file
    if filepath is None:
        possible_files = [
            raw_dir / "danish_medicines.xlsx",
            data_dir / "danish_medicines.xlsx",
        ]

        for f in possible_files:
            if f.exists():
                filepath = f
                break

    if filepath is None or not filepath.exists():
        print("Warning: No Danish medicines data found.")
        print("Please run: python scripts/download_danish_data.py")
        print("Expected file: data/raw/danish_medicines.xlsx")
        return pd.DataFrame(columns=["License_Number", "Product_Name", "Active_Ingredients"])

    print(f"Loading Danish medicines from: {filepath}")

    # Load and process
    df = load_danish_excel(filepath)
    df = normalize_columns(df)

    # Use Active_Ingredients if available, otherwise extract from product name
    if "Active_Ingredients" in df.columns:
        df["Active_Ingredients"] = df["Active_Ingredients"].fillna("")
        # For empty ingredients, try to extract from product name
        if "Product_Name" in df.columns:
            mask = df["Active_Ingredients"] == ""
            df.loc[mask, "Active_Ingredients"] = df.loc[mask, "Product_Name"].apply(extract_ingredient)
    elif "Product_Name" in df.columns:
        # Fallback: extract from medicine names
        df["Active_Ingredients"] = df["Product_Name"].apply(extract_ingredient)
    else:
        df["Active_Ingredients"] = ""

    # Also add to 'ingredients' column for compatibility
    df["ingredients"] = df["Active_Ingredients"]
    if "Product_Name" in df.columns:
        df["brand_name"] = df["Product_Name"]

    # Ensure required columns exist
    required_cols = ["License_Number", "Product_Name", "Active_Ingredients"]
    for col in required_cols:
        if col not in df.columns:
            df[col] = ""

    # Remove duplicates by ingredient
    df = df[df["Active_Ingredients"].notna() & (df["Active_Ingredients"] != "")]
    df = df.drop_duplicates(subset=["Active_Ingredients"]).reset_index(drop=True)

    print(f"  Total medicines: {len(df)}")
    print(f"  Unique ingredients: {df['Active_Ingredients'].nunique()}")

    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """Filter active drugs with valid ingredients.

    Args:
        df: Drug DataFrame

    Returns:
        Filtered DataFrame
    """
    col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    active = df[df[col].notna() & (df[col] != "")].copy()
    active = active.reset_index(drop=True)
    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """Get drug data summary statistics.

    Args:
        df: Drug DataFrame

    Returns:
        Summary statistics dictionary
    """
    all_ingredients = set()
    ing_col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    name_col = "Product_Name" if "Product_Name" in df.columns else "brand_name"

    for ing_str in df[ing_col].dropna():
        all_ingredients.add(str(ing_str).strip())

    return {
        "total_count": len(df),
        "with_ingredient": df[ing_col].notna().sum(),
        "unique_products": df[name_col].nunique() if name_col in df.columns else 0,
        "unique_ingredients": len(all_ingredients),
    }


def get_unique_ingredients(df: pd.DataFrame) -> list[str]:
    """Extract unique ingredients from loaded data."""
    all_ingredients = []

    col = "Active_Ingredients" if "Active_Ingredients" in df.columns else "ingredients"
    for ing_str in df[col].dropna():
        all_ingredients.append(str(ing_str).strip())

    return sorted(set(all_ingredients))


if __name__ == "__main__":
    # Test loading
    df = load_fda_drugs()
    print(f"\nLoaded {len(df)} drugs")

    if len(df) > 0:
        ingredients = get_unique_ingredients(df)
        print(f"Unique ingredients: {len(ingredients)}")
        print(f"\nSample ingredients: {ingredients[:10]}")
