"""
Core class structure for Proof of Play Game
Reflects SRS and Game Flow Diagram
"""

class GameEngine:
    """
    Manages main game loop, rules, and level initialization
    """
    def __init__(self, levels, player):
        self.levels = levels  # List of Level objects
        self.player = player  # Player object
        self.current_level_index = 0

    def start_game(self):
        print(f"Welcome, {self.player.name}! Game is starting...")
        while self.current_level_index < len(self.levels):
            level = self.levels[self.current_level_index]
            level.randomize()
            print(f"\n--- Level {self.current_level_index + 1} ---")
            next_level = level.play(self.player)
            if next_level is not None:
                # Branching: jump to specific level index if defined
                self.current_level_index = next_level
            else:
                self.current_level_index += 1
        print("\nCongratulations! You have completed the game.")

    def reset_level(self):
        print("Level is being reset. Attempts and progress for this level are cleared.")
        self.player.reset_level()

    def show_hint(self, question):
        if question.should_show_hint():
            print(f"Hint: {question.hint}")
        else:
            print("No hint available yet.")

class Level:
    """
    Handles level randomization and branching paths
    """
    def __init__(self, questions, branching_paths=None):
        self.questions = questions  # List of Question objects
        self.branching_paths = branching_paths or []  # Possible next levels

    def randomize(self):
        import random
        random.shuffle(self.questions)

    def get_next_path(self, choice):
        # Branching: return the next level index based on player's answer/choice
        if self.branching_paths and choice in self.branching_paths:
            return self.branching_paths[choice]
        return None

    def play(self, player):
        # For simplicity, assume one question per level for now
        question = self.questions[0]
        while True:
            print(f"Question: {question.text}")
            for idx, opt in enumerate(question.options):
                print(f"  {chr(65+idx)}) {opt}")
            answer = input("Your answer (A/B/C/D): ").strip().upper()
            if not answer or answer not in ['A','B','C','D']:
                print("Invalid input. Please enter A, B, C, or D.")
                continue
            result = question.check_answer(answer)
            player.record_attempt(result)
            if result:
                print("Correct!")
                # Branching: check if this answer leads to a specific path
                next_path = self.get_next_path(answer)
                return next_path
            else:
                print("Incorrect.")
                if question.should_show_hint():
                    print(f"Hint: {question.hint}")
                if question.attempts >= 5:
                    print("Too many wrong attempts. Level will reset.")
                    player.reset_level()
                    question.attempts = 0
                    continue

class Question:
    """
    Stores question text, hints, and misleading elements
    """
    def __init__(self, text, options, correct_option, hint, misleading_elements=None):
        self.text = text
        self.options = options  # List of possible answers
        self.correct_option = correct_option
        self.hint = hint
        self.misleading_elements = misleading_elements or []
        self.attempts = 0


    def check_answer(self, answer):
        self.attempts += 1
        idx = ord(answer) - 65
        if idx < 0 or idx >= len(self.options):
            return False
        selected = self.options[idx]
        return selected == self.correct_option

    def should_show_hint(self):
        return self.attempts >= 3

class Player:
    """
    Tracks player progress, wrong attempts, and level resets
    """
    def __init__(self, name):
        self.name = name
        self.progress = []  # List of completed levels/questions
        self.wrong_attempts = 0
        self.level_resets = 0


    def record_attempt(self, correct):
        if correct:
            self.progress.append('level_complete')
            self.wrong_attempts = 0
        else:
            self.wrong_attempts += 1

    def reset_level(self):
        self.level_resets += 1
        self.wrong_attempts = 0
