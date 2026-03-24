"""
Prompting Techniques
Example: Prompt Reuse and Versioning
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

topic = "prompt engineering"
time_available = "1 hour per day"
audience = "a complete beginner with a full-time job"

# Version 1: very basic prompt
prompt_v1 = f"""
Create a 5-day learning plan for {topic}.
"""

# Version 2: improved prompt with more clarity
prompt_v2 = f"""
Role:
You are a beginner-friendly AI coach.

Task:
Create a 5-day learning plan for {topic}.

Context:
The learner is {audience}.
The learner can study only {time_available}.

Constraints:
- Keep the plan simple
- Use beginner-friendly language
- Keep each day realistic
- Focus on practical learning

Output Format:
Day 1: ...
Day 2: ...
Day 3: ...
Day 4: ...
Day 5: ...
"""

response_v1 = get_completion(prompt_v1)
response_v2 = get_completion(prompt_v2)

print("PROMPT VERSION 1")
print("-" * 50)
print(prompt_v1)

print("\nRESPONSE VERSION 1")
print("-" * 50)
print(response_v1)

print("\n" + "=" * 70 + "\n")

print("PROMPT VERSION 2")
print("-" * 50)
print(prompt_v2)

print("\nRESPONSE VERSION 2")
print("-" * 50)
print(response_v2)