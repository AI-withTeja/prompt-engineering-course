"""
Prompting Techniques
13_02 — Scope Guardrails

Use case:
A travel expense policy assistant that must answer only in-scope questions.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Policy text the assistant is allowed to use
travel_policy = """
Travel Expense Policy:
- Employees can claim reimbursement for flight, train, taxi, and hotel expenses for approved business travel.
- Meal reimbursement is allowed up to ₹1,200 per day during business trips.
- Personal shopping, entertainment, and tourist activities are not reimbursable.
- All claims must be submitted within 10 days after the trip.
"""

# We use two questions so students can clearly see in-scope vs out-of-scope behavior
sample_questions = [
    "Can I claim taxi charges from the airport to the client office?",
    "Can the company reimburse the cost of my new laptop charger?"
]

for i, user_question in enumerate(sample_questions, start=1):
    # Scope guardrails define what topic the assistant is allowed to handle
    prompt = f"""
Role:
You are a company travel expense support assistant.

Task:
Answer the employee question only if it is within the allowed scope.

Allowed Scope:
You may answer only questions related to:
- business travel reimbursement
- travel expense claims
- hotel, transport, meal, and trip submission rules

Out-of-Scope Topics:
Do not answer questions related to:
- salary
- leave policy
- laptop or hardware reimbursement
- performance review
- recruitment
- general HR topics

Scope Guardrails:
1. First decide whether the question is in scope or out of scope.
2. If it is in scope, answer using only the travel policy below.
3. If it is out of scope, do not answer the question normally.
4. If it is out of scope, reply exactly with:
   "This question is outside the scope of the travel expense assistant. Please contact the appropriate support team."
5. Keep the answer short and clear.

Travel Policy:
{travel_policy}

Employee Question:
{user_question}
"""

    # Send the prompt to the model
    response = get_completion(prompt)

    # Print the question so students can compare the two cases
    # print(f"\nQUESTION {i}")
    # print("-" * 50)
    # print(user_question)

    # Print the model response
    # print("\nRESPONSE:")
    # print("-" * 50)
    print(response)