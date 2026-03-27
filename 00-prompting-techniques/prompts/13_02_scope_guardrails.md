# 13_02 — Scope Guardrails

## What it means

Scope guardrails define what topics the model is allowed to help with.

## Main idea

A model should not try to answer every question.
Sometimes it should answer only within a specific domain.

## What scope guardrails control

Scope guardrails help define:
- allowed topics
- out-of-scope topics
- when to refuse
- when to redirect the user elsewhere

## Why this matters

Without scope guardrails, the model may:
- answer unrelated questions
- mix domains
- create confusion
- behave like a general assistant when it should behave like a focused assistant

## Example use case

A travel expense assistant should answer:
- reimbursement questions
- claim submission questions
- hotel, meal, and transport policy questions

It should not answer:
- salary questions
- laptop reimbursement questions
- leave policy questions

## Key idea

Scope guardrails define the boundary of what the assistant is allowed to do.