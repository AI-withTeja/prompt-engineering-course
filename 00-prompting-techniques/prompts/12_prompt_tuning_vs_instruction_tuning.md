# 12 — Prompt Tuning vs Instruction Tuning

## What this topic means

This topic explains the difference between:
- prompt engineering
- prompt tuning
- instruction tuning

These are related, but they are not the same thing.

## 1. Prompt Engineering

Prompt engineering means writing better prompts as a user.

Examples:
- clearer instructions
- better structure
- examples in the prompt
- output formatting

This is what we are doing in this course most of the time.

## 2. Prompt Tuning

Prompt tuning is a training-time technique.

Instead of manually writing a better text prompt each time, model developers learn a special prompt representation during training.

This is not the same as normal prompting done by users.

## 3. Instruction Tuning

Instruction tuning means training the model on many examples of instructions and good responses.

This helps the model follow instructions better in general.

This is one reason modern chat models are easier to use than older base models.

## Simple comparison

- Prompt engineering = user-side prompt writing
- Prompt tuning = model-side learned prompt optimization
- Instruction tuning = model-side training on instruction-response pairs

## Key idea

As a beginner using an API, you are usually doing prompt engineering, not prompt tuning.