import random

# Define the possible choices
CHOICES = ["Rock", "Paper", "Scissors"]

# Base class for AI adversaries
class AIAdversary:
  def __init__(self):
    pass

  def choose_move(self):
    raise NotImplementedError()

# Random AI
class RandomAI(AIAdversary):
  def choose_move(self):
    return random.choice(CHOICES)

# Pattern-matching AI
class PatternMatchingAI(AIAdversary):
  def __init__(self, memory=5):
    super().__init__()
    self.memory = []
    self.opponent_moves = {}

  def choose_move(self):
    # Store opponent's move
    if len(self.memory) >= self.memory:
      self.memory.pop(0)
    self.memory.append(opponent_move)

    # Count opponent's most frequent move and its counter
    opponent_moves_count = {move: 0 for move in CHOICES}
    for move in self.memory:
      opponent_moves_count[move] += 1
    most_frequent_move = max(opponent_moves_count, key=opponent_moves_count.get)
    counter_move = (most_frequent_move + 1) % len(CHOICES)

    return counter_move

# Minimax AI
class MinimaxAI(AIAdversary):
  def choose_move(self):
    # TODO: Implement minimax algorithm

def play_game(human_name, ai_adversary):
  while True:
    # Get human's move
    human_move = input("Enter your move (Rock, Paper, Scissors): ").capitalize()
    if human_move not in CHOICES:
      print("Invalid move. Please enter a valid move.")
      continue

    # Get AI's move
    ai_move = ai_adversary.choose_move()

    # Determine winner
    winner = None
    if human_move == ai_move:
      print(f"It's a tie! Both chose {human_move}")
    elif (human_move + 1) % len(CHOICES) == ai_move:
      winner = human_name
    else:
      winner = "AI"

    # Print results
    print(f"{human_name} chose {human_move}")
    print(f"AI chose {ai_move}")
    if winner:
      print(f"{winner} wins!")
    else:
      print("It's a tie!")

    # Play again?
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
      break

def main():
  human_name = input("Enter your name: ")
  ai_type = input("Choose AI adversary (random, pattern_matching, minimax): ")
  if ai_type == "random":
    ai_adversary = RandomAI()
  elif ai_type == "pattern_matching":
    ai_adversary = PatternMatchingAI()
  elif ai_type == "minimax":
    ai_adversary = MinimaxAI()
  else:
    print("Invalid AI type. Please choose a valid type.")
    return

  play_game(human_name, ai_adversary)

if __name__ == "__main__":
  main()
