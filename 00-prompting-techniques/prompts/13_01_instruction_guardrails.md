# 13_01 — Instruction Guardrails

## What it means

Instruction guardrails are clear rules written directly inside the prompt to control how the model should answer.

## What instruction guardrails can control

Instruction guardrails can tell the model:
- what information it is allowed to use
- what it must not invent
- how long the answer should be
- what tone to use
- what fallback line to use if the answer is unclear

## Why this matters

Without instruction guardrails, the model may:
- add extra assumptions
- give long unnecessary answers
- answer in the wrong tone
- behave inconsistently

With instruction guardrails, the model is more controlled and predictable.

## Example use case

A refund policy support assistant should:
- answer only from policy text
- avoid making up rules
- stay short
- guide the user to the next step

## Key idea

Instruction guardrails are prompt-level rules that help shape the model’s behavior before the answer is generated.