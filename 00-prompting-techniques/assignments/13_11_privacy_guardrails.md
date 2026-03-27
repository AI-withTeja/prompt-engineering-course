# 13_11 — Privacy Guardrails

## What it means

Privacy guardrails are rules that protect personal, sensitive, or confidential information.

## Main idea

The assistant should not expose more personal data than necessary.

Privacy guardrails help control:
- what sensitive details should not be repeated
- what personal information should be minimized
- how to keep outputs privacy-aware

## Why this matters

Without privacy guardrails, the model may:
- repeat full account numbers
- repeat phone numbers
- expose confidential details unnecessarily
- create privacy risks in internal summaries or customer workflows

With privacy guardrails, the output becomes safer and more appropriate.

## Example use case

A banking support summary assistant may receive:
- customer name
- account number
- phone number
- issue details

The final summary should focus on the issue and next step, not repeat unnecessary sensitive details.

## Key idea

Privacy guardrails help reduce unnecessary exposure of sensitive information.