# MetisCode - Model

Contains all files related to the machine learning model for MetisCode.

## Problem Definition

### State Representation (S)

We expand the state space to include historical trends and behavioral analytics:

1. Time Taken for the last 5 problems (moving window).
2. Average Number of Test Cases Passed First Try.
3. Total Number of Attempts per Problem.
4. Number of Hints Used.
5. Problem Difficulty Level assigned in past sessions.
6. User Fatigue Level (recent attempts variance).
7. Streak Information (winning streak vs. struggling pattern).

### Action Space (A)

- Select a problem difficulty level from a continuous range (0–10).
- Determine whether to give a hint immediately (binary).
- Adjust difficulty scaling factor dynamically.

### Reward Function (R)

*𝑅 = 𝛼 × 𝑃 − 𝛽 × 𝑇 − 𝛾 × 𝐴 − 𝛿 × 𝐻 − 𝜆 × 𝐹*

Where:

- P = percentage of test cases passed.
- T = time taken (scaled).
- A = number of attempts.
- H = hints used.
- F = fatigue metric.
