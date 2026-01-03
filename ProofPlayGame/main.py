from game_classes import GameEngine, Level, Question, Player
import random

def build_sample_game():
    # Level 1
    q1 = Question(
        text="What will be the output of the following Python code?\n\nx = 3\ny = 2\nprint(x ** y)",
        options=["6", "9", "5", "8"],
        correct_option="9",
        hint="The ** operator means exponentiation (power), not multiplication.",
        misleading_elements=["8"]
    )
    # Level 2A (calculation path)
    q2a = Question(
        text="If a function returns True only when the input is an even number greater than 10, which of the following will return True?",
        options=["8", "11", "12", "13"],
        correct_option="12",
        hint="Check both conditions: evenness and greater than 10.",
        misleading_elements=[]
    )
    # Level 2B (trap path)
    q2b = Question(
        text="What is the output of: print(2 + 2 * 2)?",
        options=["8", "6", "4", "2"],
        correct_option="6",
        hint="Remember operator precedence: multiplication before addition.",
        misleading_elements=["8"]
    )
    # Level 3 (advanced logic)
    q3 = Question(
        text="Which of the following code snippets will output all even numbers from 1 to 10 (inclusive)?",
        options=[
            "for i in range(1, 11):\n  if i % 2 == 0: print(i)",
            "for i in range(2, 10): print(i)",
            "for i in range(1, 10):\n  if i % 2 == 1: print(i)",
            "for i in range(1, 11):\n  if i % 2 == 1: print(i)"
        ],
        correct_option="for i in range(1, 11):\n  if i % 2 == 0: print(i)",
        hint="Check the range and the condition for even numbers.",
        misleading_elements=["for i in range(1, 11):\n  if i % 2 == 1: print(i)"]
    )

    # Branching: Level 1 → Level 2A (if correct), Level 2B (if trap), else retry
    level1 = Level([q1], branching_paths={
        'B': 1,  # Correct → Level 2A
        'D': 2   # Trap → Level 2B
    })
    level2a = Level([q2a])
    level2b = Level([q2b])
    level3 = Level([q3])
    levels = [level1, level2a, level2b, level3]
    return levels

def main():
    print("Proof of Play Game - Test Run\n")
    name = input("Enter your name: ")
    player = Player(name)
    levels = build_sample_game()
    engine = GameEngine(levels, player)
    engine.start_game()

if __name__ == "__main__":
    main()
