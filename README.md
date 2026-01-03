# Proof of Play Game

A logic and programming puzzle game with branching paths, randomized questions, and a dynamic hint/reset system. Designed for critical thinking and replayability.

## Features
- **Branching Paths:** Each answer can lead to a different path, making every playthrough unique.
- **Randomized Logic:** Questions and routes are shuffled for each player.
- **Hint System:** Hints are revealed after 3 incorrect attempts, encouraging learning.
- **Punishment-Free Level Reset:** Levels reset after repeated failures, but without penalty.
- **Game Freeze Mechanic:** The game pauses for input, ensuring focus on each question.

## Installation
1. Clone this repository:
   ```sh
   git clone <your-repo-url>
   ```
2. Navigate to the project folder:
   ```sh
   cd ProofPlayGame
   ```
3. Run the game (Python 3.8+ required):
   ```sh
   python -m ProofPlayGame.main
   ```

## How to Play
- Enter your name to start.
- Answer each question by typing A, B, C, or D.
- After 3 wrong attempts, a hint will appear.
- Too many wrong attempts will reset the level (no penalty).
- Some answers will branch you to different levels or paths.
- Complete all levels to win!

## Project Structure
- `ProofPlayGame/game_classes.py` — Core game logic and classes
- `ProofPlayGame/main.py` — Entry point and sample game session
- `docs/plan.md` — Design plan and question bank
- `docs/Software_Requirements_Specification_game_.docx.md` — SRS

## Contributing
Pull requests and suggestions are welcome! Please open an issue first to discuss changes.

## License
This project is open source and available under the MIT License.
