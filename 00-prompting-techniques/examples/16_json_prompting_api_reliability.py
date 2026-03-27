"""
Prompting Techniques
16 — JSON Prompting for API Reliability

Use case:
An e-commerce return triage assistant that returns
predictable JSON for workflow/API usage.
"""

import sys
from pathlib import Path
import json

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Return request input
return_request = """
Order ID: 882341
Product: Wireless Earbuds
Issue: The left earbud is not charging.
Customer Request: Wants a replacement as soon as possible.
Purchase Age: 4 days
"""

# Prompt with reliable JSON requirements
prompt = f"""
Role:
You are an e-commerce return triage assistant.

Task:
Read the return request below and return only valid JSON.

API Reliability Rules:
1. Return only valid JSON.
2. Do not include markdown.
3. Do not include code fences.
4. Use exactly these keys:
   "status", "category", "priority", "next_action"
5. Use only one of these values for "status":
   "approved", "needs_review", "rejected"
6. Use only one of these values for "category":
   "replacement", "refund", "technical_issue"
7. Use only one of these values for "priority":
   "low", "medium", "high"
8. Keep "next_action" short and operational.

Return this exact JSON structure:
{{
  "status": "approved | needs_review | rejected",
  "category": "replacement | refund | technical_issue",
  "priority": "low | medium | high",
  "next_action": "string"
}}

Return Request:
{return_request}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt
print("PROMPT:")
print("-" * 50)
print(prompt)

# Print raw response
print("\nRAW RESPONSE:")
print("-" * 50)
print(response)

# Parse JSON to check reliability
print("\nPARSED JSON:")
print("-" * 50)
data = json.loads(response)
print(json.dumps(data, indent=2))