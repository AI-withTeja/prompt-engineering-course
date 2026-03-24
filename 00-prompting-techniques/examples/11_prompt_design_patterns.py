"""
Prompting Techniques
Example: Prompt Design Patterns
"""

import sys
from pathlib import Path

# allow importing from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

review_text = """
I bought this laptop last month. The performance is very fast and the battery backup is excellent.
However, the laptop gets slightly warm after long usage.
Overall, I am happy with the purchase.
"""

# Pattern 1: Classification
classification_prompt = f"""
Classify the sentiment of the following review as Positive, Negative, or Neutral.

Review:
{review_text}
"""

# Pattern 2: Extraction
extraction_prompt = f"""
Extract the following details from the review.

Return the answer in this format:
- Product:
- Positive Points:
- Negative Points:
- Overall Opinion:

Review:
{review_text}
"""

# Pattern 3: Transformation
transformation_prompt = f"""
Rewrite the following customer review in a more professional tone.

Review:
{review_text}
"""

# Pattern 4: Generation
generation_prompt = f"""
Based on the following review, generate a short reply from a customer support team.

Review:
{review_text}
"""

classification_response = get_completion(classification_prompt)
extraction_response = get_completion(extraction_prompt)
transformation_response = get_completion(transformation_prompt)
generation_response = get_completion(generation_prompt)

print("PATTERN 1 — CLASSIFICATION")
print("-" * 50)
print(classification_response)

print("\nPATTERN 2 — EXTRACTION")
print("-" * 50)
print(extraction_response)

print("\nPATTERN 3 — TRANSFORMATION")
print("-" * 50)
print(transformation_response)

print("\nPATTERN 4 — GENERATION")
print("-" * 50)
print(generation_response)