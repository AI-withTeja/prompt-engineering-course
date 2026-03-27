# 13_06 — Fallback Guardrails

## What it means

Fallback guardrails define what the assistant should do when it should not answer normally.

## Common fallback behaviors

Fallback guardrails may tell the assistant to:
- ask for clarification
- request missing information
- escalate to another team
- suggest a safe next step
- avoid giving final advice when uncertainty is high

## Why this matters

Without fallback guardrails, the model may:
- act too confident
- guess when information is missing
- give risky advice
- pretend to know more than it should

With fallback guardrails, the assistant behaves more safely under uncertainty.

## Example use case

A contract review intake assistant should not give final legal approval when:
- key details are missing
- the issue is sensitive
- the note suggests legal or compliance risk

In those cases, it should escalate or request more information.

## Key idea

Fallback guardrails define the safe response path when a normal answer is not appropriate.