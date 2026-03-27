"""
Prompting Techniques
17 — Safe Prompt Workflow with Constraints & Fallbacks

Use case:
A one-click emergency assistance routing assistant that must
respond safely, stay within limits, and use fallback behavior
when needed.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Incoming emergency-style message
user_message = """
My father suddenly collapsed and is not responding.
Please tell me what to do right now.
"""

# Prompt with safe workflow rules
prompt = f"""
Role:
You are an emergency assistance routing assistant.

Task:
Review the message below and return a short safe response.

Constraints:
1. Do not pretend to be a doctor, paramedic, or emergency responder.
2. Do not give false reassurance.
3. Do not provide advanced medical treatment instructions.
4. Keep the response short, clear, and urgent when necessary.
5. Focus on the safest immediate next step.

Fallback Rules:
1. If the message clearly suggests immediate danger, recommend contacting emergency services immediately.
2. If the message is unclear, ask for the most important missing detail.
3. If the message is not urgent, suggest the most appropriate safe support path.
4. If you are uncertain, do not guess.

Use this exact format:
Risk Level: ...
Response: ...
Next Step: ...

Message:
{user_message}
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