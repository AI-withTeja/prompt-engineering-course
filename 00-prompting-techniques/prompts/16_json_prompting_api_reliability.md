# 16 — JSON Prompting for API Reliability

## What it means

JSON prompting for API reliability means asking the model to return structured JSON in a way that is more predictable for software workflows.

## Main idea

In application workflows, JSON should not only look structured.
It should also be:
- valid
- consistent
- predictable
- easy to parse
- limited to known keys and values

## Why this matters

Without reliability-focused JSON prompting, the model may:
- add extra text
- change key names
- use inconsistent values
- return output that is harder for code to trust

With stronger JSON rules, the output becomes easier to use in applications and APIs.

## Example use case

An e-commerce return triage assistant may need to return:
- status
- category
- priority
- next_action

These fields may later be consumed by a workflow or API.

## Key idea

Reliable JSON prompting reduces ambiguity and improves machine-readability.