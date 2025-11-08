from openai import OpenAI
import json
import re
import os

# Load API key from environment variable
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def extract_drug_entities(user_input: str):
    """
    Use OpenAI model to extract brand and generic drug names from user input.
    Returns a dictionary:
        {"brand_name": "...", "generic_name": "..."}
    """

    prompt = f"""
    You are a medical entity extraction assistant.
    Given any text, identify the drug names mentioned.
    Distinguish between BRAND NAME and GENERIC NAME.
    If nothing is mentioned, return empty strings.
    If the generic name is not given in the text, do not guess it.

    Examples:
    Input: "Can I take Dolo 650 after food?"
    Output: {{"brand_name": "Dolo 650", "generic_name": "Paracetamol"}}

    Input: "Is it safe to have Atorvastatin with milk?"
    Output: {{"brand_name": "", "generic_name": "Atorvastatin"}}

    Input: "Can I take acetaminophen after tea?"
    Output: {{"brand_name": "", "generic_name": "Acetaminophen"}}

    Input: "I have headache."
    Output: {{"brand_name": "", "generic_name": ""}}

    Now extract for this input:
    "{user_input}"

    Respond only in JSON format with keys: brand_name, generic_name
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=0.2,
    )

    # Extract text safely
    text_output = response.output[0].content[0].text.strip()

    # Remove code fences if present
    text_output = re.sub(r"^```json|```$", "", text_output.strip(), flags=re.MULTILINE).strip("` \n")

    try:
        data = json.loads(text_output)
    except json.JSONDecodeError:
        print("⚠️ Could not parse JSON, model returned:", text_output)
        data = {"brand_name": "", "generic_name": ""}

    # Ensure both keys exist
    data.setdefault("brand_name", "")
    data.setdefault("generic_name", "")

    return data
