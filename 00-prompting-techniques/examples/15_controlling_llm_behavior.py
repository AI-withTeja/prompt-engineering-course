"""
Prompting Techniques
15 — Controlling LLM Behavior

Use case:
An executive briefing assistant that must communicate
in a short, neutral, business-focused style.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Business update information
update_note = """
The analytics platform migration is 80% complete.
Two legacy dashboards were retired this week.
Report generation speed improved by 35%.
Some finance users still need support during the transition.
The full rollout is expected to finish next month.
"""

# Prompt that controls model behavior
prompt = f"""
Role:
You are an executive briefing assistant.

Task:
Write a short business update for leadership based on the information below.

Behavior Controls:
1. Use a formal and professional tone.
2. Keep the response concise.
3. Focus on business impact, progress, and risk.
4. Do not use technical jargon unless necessary.
5. Do not sound casual or conversational.
6. Keep the message neutral and factual.
7. End with one short forward-looking line.

Update Information:
{update_note}
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