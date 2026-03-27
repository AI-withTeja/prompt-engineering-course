"""
Prompting Techniques
13_05 — Output-Format Guardrails

Use case:
A vendor risk review assistant that must return output
in a fixed enterprise review format.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample vendor review input
vendor_note = """
The vendor stores customer data in the cloud.
They have multi-factor authentication enabled for admin accounts.
Their disaster recovery process is documented.
However, they have not shared evidence of annual penetration testing yet.
"""

# Prompt with output-format guardrails
prompt = f"""
Role:
You are a vendor risk review assistant.

Task:
Review the vendor note below and return the result using the exact format provided.

Output-Format Guardrails:
1. Use exactly these headings and in this exact order:
   Risk Summary:
   Strengths:
   Gaps:
   Recommended Next Step:
2. Under Strengths, provide exactly 2 bullet points.
3. Under Gaps, provide exactly 1 bullet point.
4. Keep each bullet point short.
5. Do not add any extra headings.
6. Do not return JSON.
7. Do not add an introduction or conclusion outside the required format.

Vendor Note:
{vendor_note}
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