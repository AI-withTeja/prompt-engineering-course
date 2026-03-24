# 10 — JSON Prompting for Structured Outputs

## What it means

JSON prompting means asking the model to return the answer in JSON format instead of normal free text.

## Why this matters

JSON outputs are useful because they are:
- structured
- consistent
- easier to parse in Python
- easier to use in applications

## Basic idea

Instead of asking:
"Give me a learning plan"

ask:
"Return only valid JSON using this exact structure"

## Important techniques

- clearly say: return only valid JSON
- specify the exact keys you want
- specify the data shape
- avoid vague formatting instructions

## Key idea

If you want reliable structured output, do not just ask for JSON.
Also show the model the exact JSON structure you expect.