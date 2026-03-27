# 13_12 — Tool / Action Guardrails

## What it means

Tool or action guardrails are rules that define what actions the assistant is allowed to recommend, simulate, or trigger.

## Main idea

An assistant should not behave as if it performed restricted actions when it did not.

Tool / action guardrails help control:
- what actions are allowed
- what actions are blocked
- what actions require approval
- when human or admin involvement is required

## Why this matters

Without tool / action guardrails, the assistant may:
- pretend to perform actions it cannot perform
- suggest unsafe operational steps
- overstep approval boundaries
- create confusion about what actually happened

With tool / action guardrails, the workflow becomes more reliable and controlled.

## Example use case

An IT account support assistant may:
- recommend password reset steps
- request identity verification
- route the case to an admin

But it should not:
- claim it already unlocked the account
- claim it reset the account directly
- invent actions that never happened

## Key idea

Tool / action guardrails define the operational boundaries of what the assistant may do or recommend.