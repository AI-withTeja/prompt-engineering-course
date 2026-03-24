# 07 — System, User & Assistant Roles

## What it means

Role-based prompting separates instructions into different layers.

## The three roles

### System role
Sets the behavior, tone, rules, or personality of the model.

### User role
Contains the actual request or question.

### Assistant role
Represents the model’s response.

## Important note

In Gemini chat history, the assistant role is commonly shown as `model` in code examples.

## Why this matters

Role separation makes prompts:
- cleaner
- easier to control
- easier to reuse
- more reliable in multi-turn conversations

## Key idea

The system role guides how the model should behave.
The user role asks what should be done.
The assistant/model role is the response produced by the model.