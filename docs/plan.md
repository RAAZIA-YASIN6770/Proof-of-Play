# Implementation Plan for SRS: Proof of Play Game

## Finalized Game Rules & Mechanics (Phase 1)

**Wrong Answer Policy:**
- If a player submits a wrong answer, they cannot progress to the next level until the correct answer is given.

**Level Reset Logic:**
- After repeated failures (multiple wrong attempts), the current level restarts. This reset is punishment-free (no penalty beyond restarting the level).

**Hint System:**
- A hint becomes available to the player after 3 consecutive failed attempts on a question.

**Game World Freeze:**
- All game interactions are paused (frozen) until the player submits an answer. No actions can be taken during this freeze.

**Randomization:**
- Each player receives a unique experience through randomized questions and branching paths, ensuring no two playthroughs are the same.

This plan is based on the requirements outlined in [Software_Requirements_Specification_game_.docx.md](Software_Requirements_Specification_game_.docx.md).

## 1. Requirement Analysis
- [ ] Review and finalize game rules, mechanics, and level structure
- [ ] List all optional features (mini puzzles, misleading elements, branching paths)
- [ ] Create a game flow diagram

## 2. System Design

### Optional Features to Include

1. **Mini Puzzles:**
	- Logical or system-based challenges embedded within levels to increase engagement and variety.
	- Can be standalone or integrated into main questions.

2. **Misleading Elements:**
	- Trap options or distractors designed to test and improve the player's critical thinking.
	- Appear as plausible but incorrect answers or misleading clues.

3. **Branching Paths:**
	- Multiple possible routes or sequences through the game, determined by player choices or randomization.
	- Ensures each playthrough is unique and increases replayability.

These features should be considered in the class design (GameEngine, Level, Question, Player) and reflected in UML diagrams and implementation.
[//]: # (Game Flow Diagram Section)

## Game Flow Diagram

Below is a text-based Game Flow Diagram outlining the player's journey, level reset and hint triggers, and the integration of branching paths and misleading elements:

```
START
	|
	v
[Game Introduction]
	|
	v
FOR each Level in Game:
		|
		v
	[Present Question or Mini Puzzle]
		|
		v
	[Player Submits Answer]
		|
		+---> [Is Answer Correct?]
						|         |
				 Yes|         |No
						v         v
			[Advance to   [Increment Wrong Attempt Counter]
			 Next Level]        |
						|            +---> [Wrong Attempts >= 3?]
						|                      |         |
						|                   Yes|         |No
						|                      v         v
						|              [Show Hint]   [Allow Retry]
						|                      |
						|                      v
						|              [Wrong Attempts >= Max?]
						|                      |         |
						|                   Yes|         |No
						|                      v         v
						|              [Reset Level]  [Allow Retry]
						|
						v
	[Check for Branching Path or Misleading Element]
						|
						+---> [Branching Path?]
						|         |
				 Yes|         |No
						v         v
	 [Player Chooses   [Continue Linear Path]
		Path/Option]           |
						|             v
						v         [Next Level or End]
	[Follow Chosen Path]
						|
						v
			[Next Level or End]

END (Game Complete)
```

**Key Points:**
- On each wrong answer, the wrong attempt counter increases. After 3 wrong attempts, a hint is shown. If the player reaches the maximum allowed wrong attempts, the level resets.
- Branching paths and misleading elements are checked after each question/mini puzzle, allowing for unique routes and replayability.
- Mini puzzles can appear as part of a level or as standalone challenges.
- The game ends when all levels (or a winning path) are completed.

- [ ] Design class structure: GameEngine, Level, Question, Player
- [ ] Plan hint and reset logic
- [ ] Plan randomization for unique player experience
- [ ] Prepare UML/class diagrams

## 3. Level & Question Design
[//]: # (Draft Question Bank Section)

### Draft Question Bank with Hints, Traps, and Branching

#### Level 1: Basic Logic
**Question:**
What will be the output of the following Python code?

```python
x = 3
y = 2
print(x ** y)
```

**Options:**
- A) 6
- B) 9   ← Correct
- C) 5
- D) 8   ← Trap (confuses ** with *)

**Hint (after 3 failed attempts):**
The `**` operator means exponentiation (power), not multiplication.

**Branching:**
- If player selects B: Go to Level 2A (calculation)
- If player selects D: Go to Level 2B (trap path)
- Any other: Retry Level 1

---

#### Level 2A: Calculation Path
**Question:**
If a function returns `True` only when the input is an even number greater than 10, which of the following will return `True`?

**Options:**
- A) 8
- B) 11
- C) 12   ← Correct
- D) 13

**Hint (after 3 failed attempts):**
Check both conditions: evenness and greater than 10.

**Branching:**
- If player selects C: Go to Level 3 (advanced logic)
- Any other: Retry Level 2A

---

#### Level 2B: Trap Path
**Question:**
What is the output of: `print(2 + 2 * 2)`?

**Options:**
- A) 8   ← Trap (if player ignores operator precedence)
- B) 6   ← Correct
- C) 4
- D) 2

**Hint (after 3 failed attempts):**
Remember operator precedence: multiplication before addition.

**Branching:**
- If player selects B: Go to Level 3 (advanced logic)
- Any other: Retry Level 2B

---

#### Level 3: Advanced Logic
**Question:**
Which of the following code snippets will output all even numbers from 1 to 10 (inclusive)?

**Options:**
- A) `for i in range(1, 11):\n  if i % 2 == 0: print(i)`   ← Correct
- B) `for i in range(2, 10): print(i)`
- C) `for i in range(1, 10):\n  if i % 2 == 1: print(i)`
- D) `for i in range(1, 11):\n  if i % 2 == 1: print(i)`   ← Trap (odd numbers)

**Hint (after 3 failed attempts):**
Check the range and the condition for even numbers.

**Branching:**
- If player selects A: Game Complete (win)
- Any other: Retry Level 3

---

// More questions, traps, and branches can be added for further levels.
- [ ] Create a question bank with system-based questions
- [ ] Design levels and mini puzzles
- [ ] Add misleading elements and branching paths
- [ ] Document level and question design

## 4. Development
- [ ] Implement GameEngine class
- [ ] Implement Level and Question classes
- [ ] Implement Player class
- [ ] Add hint system (available after 3 wrong attempts)
- [ ] Add level reset logic (punishment-free)
- [ ] Add game freeze mechanic
- [ ] Integrate randomization for questions/paths
- [ ] (Optional) Add visual feedback (ASCII/pygame)

## 5. Testing & Debugging
- [ ] Test all core mechanics: rules, resets, hints, randomization
- [ ] Test for unique player experiences
- [ ] Debug and fix issues
- [ ] Prepare test report

## 6. Documentation
- [ ] Write user manual
- [ ] Write developer guide
- [ ] Prepare installation instructions and README

## 7. Optional Enhancements
- [ ] Integrate mini puzzles and branching paths
- [ ] Add visual effects (pygame)
- [ ] Enhance replayability features

---
**Note:** Each task should be checked off as completed. Update this plan as development progresses to ensure all SRS requirements are met.
