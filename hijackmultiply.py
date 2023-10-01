import time
import random

class Game:
    def __init__(self):
        self.players = {}
        self.top_score = 0
        self.top_player = ""

    def register_player(self): 
        self.name = input("Enter player name: ")
        if self.name not in self.players.keys():
            self.players[self.name] = 0
        return self.name

    def play(self, name):
        total_score = 0  # Reset score to 0 at the beginning of each game
        for _ in range(10):  # Ask 10 questions
            score = 10000  # Increase base score
            num1 = random.randint(1, 12)  # Increase range of random numbers
            num2 = random.randint(1, 12) 
            correct_ans = num1 * num2
            prompt = f"What is {num1} * {num2}?"

            while True:
                print(prompt)
                print(f"Potential points for this question: {score}")
                start_time = time.time()
                answer = int(input())
                end_time = time.time()
                time_elapsed = int(end_time - start_time)
                print(f"You took {time_elapsed} seconds to answer")
                if answer == correct_ans:
                    score -= time_elapsed * 200  # Increase decrement value
                    total_score += score
                    print(f"\nCorrect! {name}'s current score: {total_score}")
                    break
                else:
                    print(f"\nIncorrect. Try again! {name}'s potential points for this question: {score}")
                    score = max(1, score - 500)  # Increase penalty for wrong answers

            self.update_high_score(name, total_score)
        self.players[name] = total_score  

    def update_high_score(self, name, score):
        if score > self.top_score:
            self.top_score = score
            self.top_player = name

    def leaderboard(self):
        sorted_players = sorted(self.players.items(), key=lambda x: x[1], reverse=True)
        print("\nLeaderboard:")
        for i, player in enumerate(sorted_players, start=1):
            print(f"{i}. {player[0]}: {player[1]}")
        print(f"\nThe top score ever is {self.top_score} by {self.top_player}")
                
game = Game()

while True:
    player_name = game.register_player()
    game.play(player_name)
    game.leaderboard()