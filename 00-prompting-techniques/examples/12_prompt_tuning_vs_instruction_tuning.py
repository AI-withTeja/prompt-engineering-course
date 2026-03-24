"""
Prompting Techniques
Example: Prompt Tuning vs Instruction Tuning
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

simple_prompt = """
Explain the difference between prompt engineering, prompt tuning, and instruction tuning
for a complete beginner.

Use this format:
1. Prompt Engineering
2. Prompt Tuning
3. Instruction Tuning
4. Simple Comparison

Keep the explanation short, simple, and practical.
"""

response = get_completion(simple_prompt)

print("PROMPT:")
print("-" * 50)
print(simple_prompt)

print("\nMODEL EXPLANATION:")
print("-" * 50)
print(response)

print("\n" + "=" * 70)
print("IMPORTANT NOTE")
print("-" * 50)
print("Prompt engineering = writing better prompts as a user.")
print("Prompt tuning = training-time method where a learned prompt is optimized.")
print("Instruction tuning = training the model on many instruction-response examples.")
print("So in normal API usage, we are doing prompt engineering, not prompt tuning.")