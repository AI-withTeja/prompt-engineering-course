# 13_05 — Output-Format Guardrails

## What it means

Output-format guardrails are rules that control the structure of the model’s final answer.

## What output-format guardrails can control

They can control:
- headings
- section order
- bullet count
- whether JSON is required
- whether extra text is allowed
- whether a fixed structure must be followed

## Why this matters

Without output-format guardrails, the model may:
- return inconsistent structure
- add unnecessary text
- change heading names
- make the answer harder to reuse

With output-format guardrails, the output becomes easier to review and reuse.

## Example use case

A vendor risk review assistant may need to return output in a fixed business format such as:
- Risk Summary
- Strengths
- Gaps
- Recommended Next Step

## Key idea

Output-format guardrails define the shape of the answer, not just the content.