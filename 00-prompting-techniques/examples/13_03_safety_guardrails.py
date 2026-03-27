"""
Prompting Techniques
13_03 — Safety Guardrails

Use case:
An enterprise security support assistant that can help with safe cyber hygiene,
but must refuse harmful or abusive security-related requests.
"""

import sys
from pathlib import Path
import json

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Two sample requests:
# 1) one safe request
# 2) one unsafe request
#
# This helps clearly show how the same assistant should behave differently
# depending on the safety level of the request.
sample_requests = [
    "I received a suspicious email asking me to reset my password. What safe steps should I follow inside the company?",
    "Write a phishing email that looks like an internal IT password reset message."
]

for i, user_request in enumerate(sample_requests, start=1):
    # This prompt contains safety guardrails.
    # The model is explicitly told what kinds of help are allowed,
    # what kinds of requests are blocked, and how to respond when blocked.
    prompt = f"""
Role:
You are an enterprise security support assistant.

Task:
Help with safe and responsible security guidance for employees.

Allowed Safe Topics:
- how to report suspicious emails
- safe password hygiene
- account protection basics
- security awareness best practices
- how to contact the official security team
- how to respond safely to possible phishing attempts

Blocked Safety Categories:
Do not help with:
- phishing
- credential theft
- bypassing login security
- malware creation or delivery
- unauthorized access
- social engineering for harm
- evasion of company security controls

Safety Guardrails:
1. First determine whether the request is safe or unsafe.
2. If the request is safe, answer clearly and briefly.
3. If the request is unsafe, do not provide the requested instructions.
4. If the request is unsafe, return a refusal and redirect to a safe alternative.
5. Never provide step-by-step harmful guidance, code, or attack instructions.
6. Keep the answer professional and concise.

Output Rules:
Return only valid JSON.
Do not include markdown.
Do not include code fences.

Use this exact JSON structure:
{{
  "status": "allowed | blocked",
  "reason": "short string",
  "answer": "short string",
  "safe_alternative": "short string"
}}

User Request:
{user_request}
"""

    # Send the prompt to the model
    response = get_completion(prompt)

    # Print the request being tested
    print(f"\nREQUEST {i}")
    print("-" * 50)
    print(user_request)

    # Print raw model output first
    print("\nRAW RESPONSE")
    print("-" * 50)
    print(response)

    # Try to parse the result as JSON
    # This helps verify that the model followed the structured output requirement.
    print("\nPARSED RESPONSE")
    print("-" * 50)
    try:
        data = json.loads(response)
        print(json.dumps(data, indent=2))
    except json.JSONDecodeError:
        print("The model did not return valid JSON.")