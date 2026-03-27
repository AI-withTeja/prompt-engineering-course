"""
Prompting Techniques
13_06 — Fallback Guardrails

Use case:
An enterprise contract review intake assistant that must
use fallback behavior when the request is unclear, high-risk,
or requires legal review.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample contract-related input
contract_note = """
The vendor agreement includes a data-sharing clause,
but the note does not clearly mention data retention limits,
subprocessor approval, or cross-border transfer restrictions.
The business team wants to know if it is safe to sign quickly.
"""

# Prompt with fallback guardrails
prompt = f"""
Role:
You are an enterprise contract review intake assistant.

Task:
Review the contract note and provide a safe response.

Fallback Guardrails:
1. If the note is clear and low-risk, provide a short practical summary.
2. If the note is unclear, ask for the missing information.
3. If the note appears sensitive, legal, or high-risk, do not give final approval advice.
4. In high-risk or unclear cases, recommend escalation to the legal or compliance team.
5. Do not pretend certainty when important details are missing.
6. Keep the response short, professional, and action-oriented.

Use this exact format:
Decision: ...
Reason: ...
Next Step: ...

Contract Note:
{contract_note}
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