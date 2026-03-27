# 13_10 — Escalation / Handoff Guardrails

## What it means

Escalation or handoff guardrails define when the assistant should stop handling a case on its own and pass it to a human or specialist team.

## Main idea

Not every request should be handled fully by the assistant.

Some situations require:
- human judgment
- emergency response
- specialist review
- regulated handling

## Why this matters

Without escalation guardrails, the assistant may:
- continue when it should stop
- act too confidently in serious situations
- delay the right response path
- fail to route the case properly

With escalation guardrails, the workflow can hand off high-risk cases more safely.

## Example use case

An emergency support triage assistant should escalate immediately if the message suggests:
- life-threatening symptoms
- immediate physical danger
- urgent human intervention

## Key idea

Escalation guardrails define when the assistant should hand over responsibility instead of continuing normally.