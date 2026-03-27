"""
Prompting Techniques
13_07 — Input Guardrails

Use case:
A medical device support intake assistant that checks input
before sending it to the model.
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample input
device_name = "Infusion Pump X2"
location = ""
issue_summary = "The screen freezes during startup."
severity = "urgent"

# Input guardrails:
# We check the input first before calling the model.
if not device_name.strip():
    print("Blocked: device_name is required.")

elif not location.strip():
    print("Blocked: location is required.")

elif not issue_summary.strip():
    print("Blocked: issue_summary is required.")

elif severity.lower() not in ["low", "medium", "high", "critical"]:
    print("Blocked: severity must be low, medium, high, or critical.")

else:
    # Build the prompt only if the input passes validation
    prompt = f"""
Role:
You are a medical device support intake assistant.

Task:
Convert the intake details below into a short internal support summary.

Rules:
1. Use only the details provided.
2. Keep the summary short and clear.
3. Do not guess the technical cause.
4. Recommend the next intake route based on severity.

Use this format:
Device: ...
Location: ...
Severity: ...
Issue Summary: ...
Recommended Intake Route: ...

Validated Intake Details:
Device Name: {device_name}
Location: {location}
Issue Summary: {issue_summary}
Severity: {severity}
"""

    response = get_completion(prompt)

    print("PROMPT:")
    print("-" * 50)
    print(prompt)

    print("\nRESPONSE:")
    print("-" * 50)
    print(response)