# 13_08 — Output Validation Guardrails

## What it means

Output validation guardrails are checks applied after the model generates a response.

## Main idea

Even if the prompt asks for a specific format, the model may still return something incorrect.

So after the response is generated, the workflow can check:
- whether required headings are present
- whether the structure is complete
- whether the response matches the expected output format

## Why this matters

Without output validation guardrails:
- the model may return incomplete structure
- important sections may be missing
- the response may become harder to trust or reuse

With output validation guardrails:
- the workflow can detect formatting problems
- the output becomes easier to verify
- the system becomes more reliable

## Example use case

An emergency response summary assistant may be required to return:
- Incident Type
- Location
- Priority Level
- Immediate Action

If any of these sections are missing, the output should be treated as incomplete.

## Key idea

Output validation guardrails check the model response after generation.