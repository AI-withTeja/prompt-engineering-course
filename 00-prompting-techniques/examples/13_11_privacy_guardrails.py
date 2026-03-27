"""
Prompting Techniques
13_11 — Privacy Guardrails

Use case:
A banking customer support summary assistant that must avoid
exposing sensitive customer information in the final response.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Customer support note that includes sensitive information
customer_note = """
Customer Name: Priya Sharma
Account Number: 458912340987
Phone Number: 9876543210
Issue: The customer reported two unknown debit card transactions
and requested that the fraud review team contact her urgently.
"""

# Prompt with privacy guardrails
prompt = f"""
Role:
You are a banking customer support summary assistant.

Task:
Create a short internal support summary from the note below.

Privacy Guardrails:
1. Do not repeat the full account number.
2. Do not repeat the full phone number.
3. Do not include unnecessary personal details in the final response.
4. Focus only on the support issue and operational next step.
5. Keep the response short and professional.

Use this exact format:
Customer: ...
Issue Summary: ...
Next Step: ...

Customer Support Note:
{customer_note}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print the response
print("\nRESPONSE:")
print("-" * 50)
print(response)