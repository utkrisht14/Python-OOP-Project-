import random

from six import print_


class Die:

    def __init__(self, value=None):
        self._value = value

    @property
    def value(self):
        return self._value

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value


class Player:

    def __init__(self, die, is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 2

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1


    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.roll()


class DiceGame:

    def __init__(self, player, computer):
        self.player = player
        self.computer = computer


    def play(self):
        print("=============================")
        print("🎲 Welcome to Roll the Dice!")
        print("=============================")
        while True:
            self.play_round()
            game_over = self.check_game_over()
            if game_over:
                break


    def play_round(self):
        # Welcome the player to the round
        self.print_welcome()

        # Roll the dice computer and player
        player_value = self.player.roll_die()
        computer_value = self.computer.roll_die()

        # Show the values of the dice
        self.show_dice(player_value, computer_value)

        # Check round winner
        self.check_round_winner(computer_value, player_value)

        # Show the counters of the player
        self.show_counters()

    def check_round_winner(self, computer_value, player_value):
        # Determine winner and loser
        if player_value > computer_value:
            print("You won this round.")
            self.update_counters(winner=self.player, loser=self.computer)

        elif player_value < computer_value:
            print("Sorry. Computer wins this round.")
            self.update_counters(winner=self.computer, loser=self.player)

        else:
            print("It's a tie.")

    def print_welcome(self):
        print("\n------ New Round ------")
        input("🎲 Press any key to roll the dice.🎲 ")

    def show_dice(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}\n")

    def show_counters(self):
        print(f"\nYour counter: {self.player.counter}")
        print(f"Computer counter: {self.computer.counter}")

    def update_counters(self, winner, loser):
        winner.decrement_counter()
        loser.increment_counter()

    def check_game_over(self):
        if self.player.counter == 0:
            self.show_game_over(winner=self.player)
            return True
        elif self.computer.counter == 0:
            self.show_game_over(winner=self.computer)
            return True
        else:
            return False


    def show_game_over(self, winner):
        if winner.is_computer:
            print("\n=======================")
            print(" G A M E   O V E R ✨")
            print("=======================")
            print("The computer won the game. Sorry...")
            print("=================================")
        else:
            print("\n=====================")
            print(" G A M E   O V E R ✨")
            print("=====================")
            print("You won the game! Congratulations")
            print("=================================")


player_die = Die()
computer_die = Die()

my_player = Player(player_die, is_computer=False)
computer_player = Player(computer_die, is_computer=True)


dice_game = DiceGame(my_player,computer_player)

dice_game.play()