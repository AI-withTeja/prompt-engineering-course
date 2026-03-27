# 13_13 — Combined Guardrail Workflow

## What it means

A combined guardrail workflow uses multiple guardrails together in one assistant flow.

## Main idea

In real applications, guardrails are often layered instead of used one at a time.

A single workflow may combine:
- input guardrails
- scope guardrails
- safety guardrails
- behavior guardrails
- output-format guardrails
- fallback or escalation guardrails

## Why this matters

Using only one guardrail is often not enough for real workflows.

A stronger system usually needs:
- topic boundaries
- safety rules
- behavior control
- structured output
- escalation logic

## Example use case

A workplace safety incident intake assistant may need to:
- stay within workplace incident scope
- avoid dangerous advice
- communicate professionally
- return a fixed structure
- escalate urgent cases

## Key idea

A combined guardrail workflow brings multiple control layers together in one practical prompt.