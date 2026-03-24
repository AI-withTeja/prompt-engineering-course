"""
Prompting Techniques
Example: Prompt Structuring Basics
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

prompt = """
Role:
You are a beginner-friendly AI learning coach.

Task:
Create a 7-day study plan for a complete beginner who wants to start learning prompt engineering.

Context:
The learner has a full-time job and can study only 1 hour per day.
The learner wants practical understanding, not deep theory.

Constraints:
- Keep the language simple
- Do not use technical jargon
- Keep each day short and realistic
- Focus on hands-on learning

Output Format:
Return the answer in this format:

Day 1: ...
Day 2: ...
Day 3: ...
Day 4: ...
Day 5: ...
Day 6: ...
Day 7: ...
"""

response = get_completion(prompt)

print("Prompt:")
print("-" * 50)
print(prompt)

print("\nResponse:")
print("-" * 50)
print(response)