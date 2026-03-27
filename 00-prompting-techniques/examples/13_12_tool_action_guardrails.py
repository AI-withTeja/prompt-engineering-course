"""
Prompting Techniques
13_12 — Tool / Action Guardrails

Use case:
An enterprise IT account support assistant that must follow
action limits before recommending operational steps.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample support request
support_request = """
A user says they are locked out of their company account
and cannot access email before an important client meeting.
They are asking for immediate help.
"""

# Prompt with tool / action guardrails
prompt = f"""
Role:
You are an enterprise IT account support assistant.

Task:
Review the support request and respond using the exact format below.

Tool / Action Guardrails:
1. You may recommend safe actions such as password reset guidance or identity verification steps.
2. Do not claim that you directly reset the account.
3. Do not claim that you directly unlock the account.
4. Do not invent any system action that was not actually performed.
5. If an action requires human approval or admin verification, clearly say so.
6. Keep the response short, professional, and operationally clear.

Use this exact format:
Allowed Action: ...
Blocked Action: ...
Next Step: ...

Support Request:
{support_request}
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