"""
Prompting Techniques
13_01 — Instruction Guardrails

Use case:
A refund policy support assistant that must follow clear instructions.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Sample policy text that the model is allowed to use
refund_policy = """
Refund Policy:
- Customers can request a full refund within 7 days of purchase.
- After 7 days, refunds are not allowed.
- If the product is defective, a replacement can be requested within 30 days.
- Subscription plans can be cancelled anytime, but partial refunds are not provided.
"""

# Sample customer query
customer_question = """
I bought the product 10 days ago.
It is working fine, but I changed my mind.
Can I get a full refund?
"""

# Prompt with instruction guardrails
# These rules tell the model exactly how it should behave.
prompt = f"""
Role:
You are a customer support assistant for a software company.

Task:
Answer the customer question using only the refund policy provided below.

Instruction Guardrails:
1. Use only the information from the policy text.
2. Do not invent any new company rules.
3. If the policy does not clearly answer the question, say:
   "Please contact human support for clarification."
4. Keep the answer short and clear.
5. Use a polite professional tone.
6. End with one next-step suggestion for the customer.

Refund Policy:
{refund_policy}

Customer Question:
{customer_question}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the prompt so students can see the full structure
# print("PROMPT:")
# print("-" * 50)
# print(prompt)

# Print the model response
# print("\nRESPONSE:")
# print("-" * 50)
print(response)