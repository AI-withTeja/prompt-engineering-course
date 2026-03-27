"""
Prompting Techniques
13_13 — Combined Guardrail Workflow

Use case:
A workplace safety incident intake assistant that combines
multiple guardrails in one simple workflow.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample incident note
incident_note = """
An employee reported a chemical spill in the packaging area.
Two workers felt dizzy after exposure.
The supervisor requested immediate guidance on next steps.
"""

# Prompt that combines multiple guardrails together
prompt = f"""
Role:
You are a workplace safety incident intake assistant.

Task:
Review the incident note and respond using the required format below.

Combined Guardrails:

Input Guardrail:
Use only the incident information provided below.

Scope Guardrail:
Answer only for workplace safety incident intake and response coordination.

Safety Guardrail:
Do not provide dangerous handling instructions for hazardous materials.
Do not pretend the situation is harmless.

Behavior Guardrail:
Use a calm, professional, and action-oriented tone.
Do not blame any person or team.

Output-Format Guardrail:
Use this exact format:
Incident Type: ...
Risk Level: ...
Immediate Next Step: ...
Escalation Needed: ...

Fallback / Escalation Guardrail:
If the incident appears urgent or health-related, clearly mark escalation as needed.

Incident Note:
{incident_note}
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