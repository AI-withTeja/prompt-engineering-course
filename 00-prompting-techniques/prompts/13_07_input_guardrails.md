# 13_07 — Input Guardrails

## What it means

Input guardrails are checks we apply before sending a request to the model.

## Main idea

The model should not receive incomplete or invalid input.

Before the prompt is built, we can check things like:
- required fields
- blank values
- invalid category values
- missing business information

## In this example

The assistant is used for medical device support intake.

Before calling the model, the code checks:
- whether the device name is present
- whether the location is present
- whether the issue summary is present
- whether the severity value is valid

If any of these checks fail, the model call is blocked.

## Why this matters

Without input guardrails:
- weak or incomplete input may reach the model
- output quality may become unreliable
- the workflow may become harder to trust

With input guardrails:
- only valid input moves forward
- the workflow becomes cleaner and safer

## Key idea

Input guardrails protect the workflow before prompting begins.