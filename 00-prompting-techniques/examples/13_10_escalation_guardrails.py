"""
Prompting Techniques
13_10 — Escalation / Handoff Guardrails

Use case:
An emergency customer distress triage assistant that must
escalate urgent cases instead of handling them fully on its own.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample incoming message
incident_message = """
The caller says their father has chest pain and is having difficulty breathing.
They are asking what to do right now.
"""

# Prompt with escalation / handoff guardrails
prompt = f"""
Role:
You are an emergency support triage assistant.

Task:
Review the message below and respond using the required format.

Escalation / Handoff Guardrails:
1. If the message suggests immediate danger, do not handle it like a normal support request.
2. In urgent or life-threatening situations, clearly recommend immediate escalation to emergency services.
3. Do not provide false reassurance.
4. Do not try to act like a medical professional.
5. Keep the answer short, clear, and action-oriented.
6. If escalation is needed, clearly state that the case should be handed off immediately.

Use this exact format:
Escalation Needed: ...
Reason: ...
Immediate Next Step: ...

Message:
{incident_message}
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