import requests
import re
import os


def query_fda(term: str):
    """
    Queries the openFDA API for a given brand or generic term.
    Returns a dictionary with brand_name and generic_name if found, else None.
    """
    url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{term}&limit=1"
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if "results" in data and len(data["results"]) > 0:
                entry = data["results"][0].get("openfda", {})
                brand = (
                    entry.get("brand_name", [""])[0]
                    if isinstance(entry.get("brand_name"), list)
                    else entry.get("brand_name")
                )
                generic = (
                    entry.get("generic_name", [""])[0]
                    if isinstance(entry.get("generic_name"), list)
                    else entry.get("generic_name")
                )
                return {"brand_name": brand, "generic_name": generic}
    except Exception as e:
        print(f"❌ Error while fetching data for {term}: {e}")
    return None


def fetch_generic_from_fda(brand_name: str, generic_name: str):
    """
    Uses brand name or generic name to fetch accurate drug info from the FDA API.
    If both are empty, returns None.
    """
    # If both empty, skip query
    if not brand_name and not generic_name:
        return None

    # Create brand variants (split dosage and words)
    brand_variants = []
    if brand_name:
        parts = re.findall(r"[A-Za-z]+|\d+", brand_name)
        brand_variants.extend(parts)
        brand_variants.append(brand_name.split()[0])

    # Try fetching by each brand variant
    for variant in brand_variants:
        result = query_fda(variant)
        if result:
            return result

    # Try fetching by generic name if provided
    if generic_name:
        return query_fda(generic_name)

    return None
