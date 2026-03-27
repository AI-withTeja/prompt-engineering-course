# 17 — Safe Prompt Workflow with Constraints & Fallbacks

## What it means

A safe prompt workflow uses multiple safety-oriented prompt rules together so the assistant behaves more predictably.

## Main idea

A stronger workflow usually needs:
- clear role limits
- clear constraints
- safe next-step logic
- fallback behavior
- structured output

## Why this matters

Without a safe workflow, an assistant may:
- overstep its role
- sound too confident
- guess under uncertainty
- provide risky guidance
- return unclear next steps

With a safe workflow, the assistant becomes more reliable and controlled.

## Example use case

An emergency assistance routing assistant should:
- stay within a limited role
- avoid pretending to be a professional responder
- identify urgent cases
- recommend safe immediate next steps
- use fallback behavior when details are unclear

## Key idea

A safe prompt workflow combines constraints and fallback rules so the assistant stays useful without overstepping.