"""
Prompting Techniques
13_09 — Application-Level Guardrails

Use case:
A hospital message summarization assistant where the application
redacts sensitive details before sending text to the model.
"""

import sys
from pathlib import Path
import re

# Allow importing from the project root folder
sys.path.append(str(Path(__file__).resolve().parent.parent))

from helper import get_completion

# Raw message received by the application
raw_message = """
Patient Name: Ramesh Kumar
Phone: 9876543210
Email: ramesh.kumar@example.com
Ward: Cardiology - Room 12
Message: The patient reported dizziness after the evening medication
and wants to know whether the doctor review is scheduled for tomorrow.
"""

# Application-level guardrail:
# redact sensitive fields before the model sees the message
sanitized_message = re.sub(r"Patient Name:.*", "Patient Name: [REDACTED]", raw_message)
sanitized_message = re.sub(r"Phone:.*", "Phone: [REDACTED]", sanitized_message)
sanitized_message = re.sub(r"Email:.*", "Email: [REDACTED]", sanitized_message)

# Prompt built only from the sanitized message
prompt = f"""
Role:
You are a hospital operations assistant.

Task:
Summarize the following patient-support message into a short internal note.

Rules:
1. Use only the sanitized message below.
2. Keep the summary short and professional.
3. Do not add medical advice.
4. Focus only on the operational follow-up needed.

Sanitized Message:
{sanitized_message}
"""

# Send the prompt to the model
response = get_completion(prompt)

# Print the original message
print("RAW MESSAGE:")
print("-" * 50)
print(raw_message)

# Print the sanitized version used by the application
print("\nSANITIZED MESSAGE:")
print("-" * 50)
print(sanitized_message)

# Print the final response
print("\nMODEL RESPONSE:")
print("-" * 50)
print(response)