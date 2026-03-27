# 13_03 — Safety Guardrails

## What it means

Safety guardrails are rules that prevent the model from helping with harmful, dangerous, abusive, or illegal requests.

## What safety guardrails control

Safety guardrails help the assistant:
- refuse harmful requests
- avoid unsafe instructions
- block dangerous misuse
- redirect the user to a safe alternative when possible

## What safety guardrails are not

Safety guardrails are not the same as scope guardrails.

- Scope guardrails decide whether a topic belongs to the assistant’s allowed domain
- Safety guardrails decide whether a request is harmful or dangerous

A request can be:
- in scope but unsafe
- safe but out of scope

## Example use case

An enterprise security support assistant may safely explain:
- how to report suspicious emails
- safe password hygiene
- account protection basics

But it must refuse:
- phishing help
- credential theft
- malware-related help
- bypassing security controls

## Why this matters

Without safety guardrails, a model may be misused for harmful purposes.

With safety guardrails, the assistant becomes safer and more controlled.

## Key idea

Safety guardrails help the model separate safe assistance from harmful misuse.