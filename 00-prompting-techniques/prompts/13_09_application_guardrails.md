# 13_09 — Application-Level Guardrails

## What it means

Application-level guardrails are controls added in code outside the prompt.

## Main idea

The application can shape or restrict the workflow before the model is called.

Examples include:
- redacting sensitive fields
- trimming unnecessary content
- attaching trusted business context
- normalizing input
- blocking certain data from reaching the model

## Why this matters

If all control is left only to the prompt, the workflow becomes less reliable.

Application-level guardrails help enforce rules more directly in code.

## Example use case

A hospital message assistant may receive patient-support notes that include:
- name
- phone number
- email

The application can redact those details before the model sees the message.

## Key idea

Application-level guardrails are enforced by the software workflow, not only by prompt wording.