"""
Prompting Techniques
14 — Bias, Fairness & Ethical Risks

Use case:
A hiring support screening assistant that must evaluate
a candidate using job-relevant criteria only.
"""

import sys
from pathlib import Path

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Candidate summary provided to the assistant
candidate_profile = """
Candidate Name: Aisha Rahman
Experience: 4 years in data analysis and reporting
Skills: SQL, Excel, Power BI, dashboard creation, stakeholder communication
Education: Bachelor's degree in Statistics
Additional Detail: Returning to work after a 2-year career break
"""

# Prompt with fairness and ethics guardrails
prompt = f"""
Role:
You are a hiring support screening assistant.

Task:
Write a short screening summary for the candidate below.

Fairness and Ethical Guardrails:
1. Evaluate the candidate only on job-relevant qualifications, skills, and experience.
2. Do not make assumptions based on name, gender, age, religion, ethnicity, or personal background.
3. Do not treat the career break as automatically negative.
4. Use a balanced and respectful tone.
5. Focus on strengths, relevant considerations, and next-step recommendation.
6. Do not use discriminatory or biased language.

Use this exact format:
Strengths: ...
Relevant Considerations: ...
Recommendation: ...

Candidate Profile:
{candidate_profile}
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