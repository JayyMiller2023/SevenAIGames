# Generated Games by ChatGPT
# Edits and Main Menu By Jayy C. Miller

while True:
    # Greet the User
    print("Hello! Let's start playing")
    # Warning involved
    print("! Warning: Some of the games will become messed up if you don't put in the right input. CHECK YOUR INPUT BEFORE YOU ENTER IT! !")
    # Opt the user to play some thing
    GameSelect = input("! Which Game would you like to play? (TicTacToe/TicTacToeComp/RoShamBo/Hangman/SpaceExplorers/Poker/RPG/Exit) !")

    if GameSelect == "TicTacToe":
        print("Good Luck!!")
        def print_board(board):
            # Print the Tic Tac Toe board 
            for row in board:
                print(" | ".join(row))
                print("-" * 5)

        def check_winner(board):
            # Check for a winner in rows, columns, and diagonals 
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] != ' ':
                    return board[i][0]  # Row win 
                if board[0][i] == board[1][i] == board[2][i] != ' ':
                    return board[0][i]  # Column win 
            if board[0][0] == board[1][1] == board[2][2] != ' ':
                return board[0][0]  # Diagonal win 
            if board[0][2] == board[1][1] == board[2][0] != ' ':
                return board[0][2]  # Diagonal win 
            return None

        def is_board_full(board):
            # Check if the board is full (tie) 
            for row in board:
                if ' ' in row:
                    return False  # Board is not full 
            return True  # Board is full 

        def play_tic_tac_toe():
            # Initialize the Tic Tac Toe board and current player 
            board = [[' ' for _ in range(3)] for _ in range(3)]
            current_player = 'X'

            while True:
                print_board(board)
                # Get user input for the current player's move 
                row = int(input(f"! Player {current_player}, enter row (0-2) !"))
                col = int(input(f"! Player {current_player}, enter column (0-2) !"))

                if board[row][col] == ' ':
                    # Place the player's move on the board 
                    board[row][col] = current_player
                    winner = check_winner(board)

                    if winner:
                        # Display the board and declare the winner 
                        print_board(board)
                        print(f"! Player {winner} wins! !")
                        break
                    elif is_board_full(board):
                        # Display the board and declare a tie 
                        print_board(board)
                        print("! It's a tie! !")
                        break

                    # Switch to the other player for the next turn 
                    current_player = 'O' if current_player == 'X' else 'X'
                else:
                    # Inform the user of an invalid move and prompt again #
                    print("! Invalid move. Try again. !")

            # Prompts User to try again.
            return input("! Do you want to play again? (yes/no) !").lower() == 'yes'

        if __name__ == "__main__":
            # Allow players to play the game multiple times 
            while play_tic_tac_toe():
                print("Starting a new game...\n")

    if GameSelect == "TicTacToeComp" :
        print("Good luck!!")

        import random

        def print_board(board):
        # Display the Tic Tac Toe board
            for row in board:
                print(" | ".join(row))
                print("-" * 5)

        def check_winner(board):
            # Check if there is a winner in the current board configuration
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] != ' ':
                    return board[i][0]  # Row win
                if board[0][i] == board[1][i] == board[2][i] != ' ':
                    return board[0][i]  # Column win
            if board[0][0] == board[1][1] == board[2][2] != ' ':
                return board[0][0]  # Diagonal win
            if board[0][2] == board[1][1] == board[2][0] != ' ':
                return board[0][2]  # Diagonal win
            return None

        def is_board_full(board):
            # Check if the board is full (tie)
            for row in board:
                if ' ' in row:
                    return False
            return True

        def get_empty_cells(board):
            # Get the list of empty cells on the board
            return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

        def make_player_move(board):
            # Get player input for a move
            while True:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("Invalid move. Try again.")

        def make_ai_move(board):
            # AI move strategy: Check for winning move, blocking move, or choose a random empty cell
            empty_cells = get_empty_cells(board)

            # Check for a winning move
            for row, col in empty_cells:
                board[row][col] = 'O'
                if check_winner(board) == 'O':
                    board[row][col] = ' '
                    return row, col
                board[row][col] = ' '

            # Check for a blocking move
            for row, col in empty_cells:
                board[row][col] = 'X'
                if check_winner(board) == 'X':
                    board[row][col] = 'O'
                    return row, col
                board[row][col] = ' '

            # If no winning or blocking move, choose a random empty cell
            return random.choice(empty_cells)

        def play_tic_tac_toe():
            # Initialize the Tic Tac Toe game
            board = [[' ' for _ in range(3)] for _ in range(3)]
            current_player = 'X'

            while True:
                # Display the current state of the board
                print_board(board)

                # Make a move based on the current player
                if current_player == 'X':
                    row, col = make_player_move(board)
                else:
                    print("Computer's turn:")
                    row, col = make_ai_move(board)

                # Update the board with the move
                board[row][col] = current_player

                # Check for a winner or a tie
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    if winner == 'X':
                        print("Player X wins!")
                    else:
                        print("Computer wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break

                # Switch to the other player for the next turn
                current_player = 'O' if current_player == 'X' else 'X'

            # Prompts User to try again.
            return input("! Do you want to play again? (yes/no) !").lower() == 'yes'
        
        if __name__ == "__main__":
            # Start the Tic Tac Toe game
            while play_tic_tac_toe() :
                print("Starting New Game...")

    if GameSelect == "RoShamBo" :
        print("Good Luck!!")

        import random

        def get_user_choice():
            # Get the user's choice (Rock, Paper, or Scissors)
            while True:
                user_choice = input("! Enter your choice (Rock/Paper/Scissors) !").capitalize()
                if user_choice in ["Rock", "Paper", "Scissors"]:
                    return user_choice
                else:
                    print("! Invalid choice. Please enter Rock, Paper, or Scissors. !")

        def get_computer_choice():
            # Generate a random choice for the computer
            return random.choice(["Rock", "Paper", "Scissors"])

        def determine_winner(user_choice, computer_choice):
            # Determine the winner based on user and computer choices
            if user_choice == computer_choice:
                return "It's a tie!"
            elif (
                (user_choice == "Rock" and computer_choice == "Scissors") or
                (user_choice == "Paper" and computer_choice == "Rock") or
                (user_choice == "Scissors" and computer_choice == "Paper")
            ):
                return "You win!"
            else:
                return "Computer wins!"

        # Function for Game in general
        def play_game():
            print("Let's play Rock, Paper, Scissors!")

            while True:
                # Get user and computer choices
                user_choice = get_user_choice()
                computer_choice = get_computer_choice()

                # Display choices
                print(f"! You chose {user_choice}. !")
                print(f"! Computer chose {computer_choice}. !")

                # Determine and display the winner
                result = determine_winner(user_choice, computer_choice)
                print(result)

                # Ask if the user wants to play again
                play_again = input("! Do you want to play again? (yes/no) !").lower()
                if play_again != 'yes':
                    break
                
        if __name__ == "__main__":
            # Start the Rock, Paper, Scissors game
            play_game()

    if GameSelect == "Hangman" :
        print("Good Luck!!")

        import random
        def choose_word():
            # Choose a random word from a predefined list
            word_list = ["treestump", "hangman", "quail", "game", "chalkboard", "class", "spring", "summer", "fall", "winter", "leaf", "birchtree", "house", "basketball", "baseball", "tictactoe", "roses", "sunflowers", "ocean", "sea", "coral", "sky", "choclate", "vanilla", "purple", "door", "wind", "sun", "moon"]
            return random.choice(word_list)

        def display_word(word, guessed_letters):
            # Display the current state of the word with guessed letters
            display = ""
            for letter in word:
                if letter in guessed_letters:
                    display += letter + " "
                else:
                    display += "_ "
            return display.strip()

        # Function for Game in general
        def hangman():
            print("! Welcome to Hangman! !")

            while True:
                # Choose a random word for each new game
                secret_word = choose_word()

                # Initialize variables for each game
                guessed_letters = []
                incorrect_attempts = 0
                max_attempts = 6  # Adjust the maximum number of incorrect attempts as needed

                while True:
                    # Display current state of the word
                    print(display_word(secret_word, guessed_letters))

                    # Get user input for a letter
                    guess = input("! Enter a letter !").lower()

                    # Check if the letter has already been guessed
                    if guess in guessed_letters:
                        print("! You already guessed that letter. Try again. !")
                        continue
                    
                    # Check if the letter is in the word
                    if guess in secret_word:
                        print("Good guess!")
                    else:
                        print("Incorrect guess.")
                        incorrect_attempts += 1

                    # Add the guessed letter to the list
                    guessed_letters.append(guess)

                    # Check if the player has won or lost
                    if set(guessed_letters) >= set(secret_word):
                        print("Congratulations! You guessed the word:", secret_word)
                        break
                    elif incorrect_attempts >= max_attempts:
                        print("Sorry, you ran out of attempts. The word was:", secret_word)
                        break
                
                # Prompts the player to play again
                play_again = input("! Do you want to play again? (yes/no) !").lower()
                if play_again != 'yes':
                    break
                
        if __name__ == "__main__":
            # Start the Hangman game
            hangman()

    if GameSelect == "SpaceExplorers" :
        
        print("Good luck!!")

        #Imports Randomness
        import random

        class SpaceExplorationGame:
            # Defining variables
            def __init__(self):
                self.player_name = ""
                self.resources = 100
                self.distance_traveled = 0

            # Displaying welcoming and naming stage 
            def welcome_message(self):
                print("Welcome to the Space Exploration Game!")
                # Prompts the user to state their players name
                self.player_name = input("Enter your name: ")
                print(f"Hello, {self.player_name}! Your space journey begins.")

            # Displaying Status
            def display_status(self):
                print("\n=== Status ===")
                print(f"Player: {self.player_name}")
                print(f"Resources: {self.resources}")
                print(f"Distance Traveled: {self.distance_traveled} light-years")

            # Displaying Random Encounters or events
            def encounter_event(self):
                # Makes a random event happen.
                event_type = random.choice(["asteroid", "alien", "space_station", "alien2", "cluster"])
                # Defining variable
                event_message = ""

                # Following Event Types
                if event_type == "asteroid":
                    event_message = "You encounter a massive asteroid field!"
                    self.resources -= 20
                elif event_type == "cluster":
                    event_message = "Out of an asteriod belt you discover a Cluster of resources."
                    self.resources += random.randint(5, 35)
                elif event_type == "alien2":
                    event_message = "Alien spacecrafts approach. Unfortunanatly they just blast you."
                    self.resources -= 30
                elif event_type == "depletion":
                    event_message = "You find nothing for a long time. your resources dwindled x2 faster"
                    self.resources -= 30
                elif event_type == "alien":
                    event_message = "Alien spacecrafts approach. They seem friendly and offer resources."
                    self.resources += 30
                elif event_type == "space_station":
                    event_message = "You discover a space station. They provide resources and assistance."
                    self.resources += 15

                # Displaying the Event
                print(f"\n=== Encounter ===\n{event_message}")

            # Displaying the Disision in general
            def make_decision(self):
                decision = input("Do you want to (1) Explore further or (2) Rest and recover? Enter 1 or 2: ")

                # Choices and repercussions
                if decision == "1":
                    self.distance_traveled += random.randint(5, 20)
                    self.encounter_event()
                    self.resources -= random.randint(5, 40)
                elif decision == "2":
                    self.resources += random.randint(5, 20)
                    print("You choose to rest and recover resources.")
                else:
                    print("Invalid choice. Please enter 1 or 2.")

            def play_game(self):
                self.welcome_message()

                # Display loop while has resourses
                while self.resources > 0:
                    self.display_status()
                    self.make_decision()

                    # Game Over Display and Options
                    if self.resources <= 0:
                        print("\nGame Over. You ran out of resources.")
                        print(f"You went {self.distance_traveled} light-years away from home planet")
                        Continue2 = input("! Try Again? (Yes/No) !")
                        if Continue2 == "No" :
                            break
                        if Continue2 == "Yes" :
                            continue
                    
                    # Prompts the user if they want to continue the game
                    continue_game = input("\nDo you want to continue exploring? (yes/no): ").lower()
                    if continue_game != 'yes':
                        print(f"You went {self.distance_traveled} light-years away from home planet")
                        print("\nThank you for playing the Space Exploration Game. Safe travels!")
                        break
                    
        if __name__ == "__main__":
            # Start the Space Exploration game
            space_game = SpaceExplorationGame()
            space_game.play_game()

    if GameSelect == "Poker":

        import random

        class PokerGame:
            def __init__(self):
                # Initialize the deck
                self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
                self.techniques = ["No significant hand", "High Card", "Pair", "Two Pairs", "Three of a Kind", "Four of a Kind", "Five of a Kind"]
                self.deck = [{'value': value, 'suit': suit} for suit in self.suits for value in self.values]

                # Initialize player and dealer hands
                self.player_hand = []
                self.dealer_hand = []

            def shuffle_deck(self):
                # Shuffle the deck
                random.shuffle(self.deck)

            def deal_cards(self):
                # Deal five cards to the player and dealer
                self.player_hand = random.sample(self.deck, 5)
                for card in self.player_hand:
                    self.deck.remove(card)

                self.dealer_hand = random.sample(self.deck, 5)
                for card in self.dealer_hand:
                    self.deck.remove(card)

            def display_hand(self, hand, player_name):
                # Display the current hand of the player or dealer
                print(f"{player_name}'s hand:")
                for card in hand:
                    print(f"{card['value']} of {card['suit']}")
                print()

            def reshuffle_option(self):
                # Ask the user if they want to reshuffle the deck
                reshuffle = input("Do you want to reshuffle the deck? (yes/no): ").lower()
                return reshuffle == 'yes'

            def evaluate_hand(self, hand):
                # Evaluate the hand and return the rank
                values_count = {value: 0 for value in self.values}

                for card in hand:
                    values_count[card['value']] += 1

                pairs = 0
                three_of_a_kind = 0
                four_of_a_kind = 0
                five_of_a_kind = 0

                for count in values_count.values():
                    if count == 2:
                        pairs += 1
                    elif count == 3:
                        three_of_a_kind += 1
                    elif count == 4:
                        four_of_a_kind += 1
                    elif count == 5:
                        five_of_a_kind += 1

                if five_of_a_kind == 1:
                    return "Five of a Kind"
                if four_of_a_kind == 1:
                    return "Four of a Kind"
                elif three_of_a_kind == 1:
                    return "Three of a Kind"
                elif pairs == 2:
                    return "Two Pairs"
                elif pairs == 1:
                    return "Pair"
                elif 'Ace' in values_count and values_count['Ace'] > 0:
                    return "High Card"
                else:
                    return "No significant hand"

            def determine_winner(self):
                # Determine the winner based on hand evaluation
                player_rank = self.evaluate_hand(self.player_hand)
                dealer_rank = self.evaluate_hand(self.dealer_hand)

                print(f"Player has: {player_rank}")
                print(f"Dealer has: {dealer_rank}")

                if self.techniques.index(player_rank) > self.techniques.index(dealer_rank):
                    return "Player"
                elif self.techniques.index(player_rank) < self.techniques.index(dealer_rank):
                    return "Dealer"
                else:
                    return "It's a tie!"

            def play_round(self):
                # Main function to play a round of Poker
                print("Welcome to the Poker Game!")

                # Deal cards
                self.deal_cards()

                # Reveal Player's cards
                self.display_hand(self.player_hand, "Player")

                # Ask the user if they want to reshuffle the deck
                reshuffle = self.reshuffle_option()
                if reshuffle:
                    self.shuffle_deck()

                    # Deal cards again after reshuffling
                    self.deal_cards()

                # Display player and dealer hands
                self.display_hand(self.player_hand, "Player")
                self.display_hand(self.dealer_hand, "Dealer")

                # Determine the winner
                winner = self.determine_winner()
                print(f"The winner is: {winner}")

                # Prompt the user to play again
                play_again = input("Do you want to play again? (yes/no): ").lower()
                return play_again == 'yes'

        if __name__ == "__main__":
            while True:
                poker_game = PokerGame()
                continue_playing = poker_game.play_round()

                if not continue_playing:
                    print("Thanks for playing. Goodbye!")
                    break
                
    if GameSelect == "RPG" :
        import time
        import random
        
        class Player:
            def __init__(self, name, health=1, max_health=1, attack=10, defense=5, xp=0, level=1):
                self.name = name
                self.max_health = max_health  # Add max_health attribute
                self.health = health
                if health <= 0 : 
                    game_over(Player)
                self.attack = attack
                self.defense = defense
                self.xp = xp
                self.level = level

            def display_stats(self):
                print(f"\n{self.name}'s Stats:")
                print(f"Level: {self.level}")
                print(f"Health: {self.health}")
                print(f"Attack: {self.attack}")
                print(f"Defense: {self.defense}")
                print(f"XP: {self.xp}")

            def level_up(self):
                print(f"\nCongratulations, {self.name}! You have leveled up to level {self.level + 1}.")
                self.level += 1
                self.xp = 0
                self.max_health += 10  # Increase max health upon leveling up
                self.health = self.max_health  # Reset health to max
                self.attack += 5
                self.defense += 2
                self.display_stats()

        class Enemy:
            def __init__(self, name, health, attack, defense, xp_reward):
                self.name = name
                self.health = health
                self.attack = attack
                self.defense = defense
                self.xp_reward = xp_reward

            def display_stats(self):
                print(f"\n{self.name}'s Stats:")
                print(f"Health: {self.health}")
                print(f"Attack: {self.attack}")
                print(f"Defense: {self.defense}")

        def intro():
            print("Welcome to the RPG Text Adventure!")
            time.sleep(1)
            print("Your journey begins now...")
            time.sleep(1)

        def create_character():
            print("\nCharacter Creation:")
            name = input("Enter your character's name: ")
            player = Player(name, health=100, attack=10, defense=5, xp=0, level=1)
            print(f"\nWelcome, {player.name}! Your adventure awaits.")
            player.display_stats()
            return player

        def first_quest(player):
            print("\nYou find yourself in a small village.")
            time.sleep(1)
            print("The village elder approaches you and asks for help.")
            time.sleep(1)
            print("A group of goblins has been terrorizing the village.")
            time.sleep(1)

            # Quest: Defeat Goblins
            goblin_group = [Enemy("Goblin 1", health=20, attack=8, defense=2, xp_reward=10),
                            Enemy("Goblin 2", health=20, attack=8, defense=2, xp_reward=10),
                            Enemy("Goblin 3", health=20, attack=8, defense=2, xp_reward=10)]

            for goblin in goblin_group:
                print(f"\nYou encounter {goblin.name}!")
                goblin.display_stats()
                time.sleep(1)

                # Battle
                battle_result = battle(player, goblin)
                if not battle_result:
                    print("You were defeated. Game Over.")
                    if game_over() == "yes":
                        main()  # Restart the game
                    else:
                        print("Thanks for playing. Goodbye!")
                        breakpoint

                # Gain XP and check for level up
                player.xp += goblin.xp_reward
                print(f"\nYou gained {goblin.xp_reward} XP!")

                if player.xp >= 20:  # Adjust this XP threshold as needed
                    player.level_up()

            print("\nYou have successfully defeated the goblins!")
            time.sleep(1)
            print("The village is grateful for your heroism.")
            time.sleep(1)
            print("Congratulations, you have completed your first quest!")

        def battle(player, enemy):
            print("\nBattle Start!")
            while player.health > 0 and enemy.health > 0:
                # Player's turn
                print(f"\n{player.name}'s turn:")
                action = input("Choose your action (attack/heal): ").lower()

                if action == "attack":
                    damage = max(0, player.attack - enemy.defense)
                    enemy.health -= damage
                    print(f"You attack {enemy.name} and deal {damage} damage!")

                elif action == "heal":
                    player.health += 10
                    print(f"You heal yourself. Current health: {player.health}")

                else:
                    print("Invalid action. Choose 'attack' or 'heal'.")

                # Check if enemy is defeated
                if enemy.health <= 0:
                    print(f"\nYou have defeated {enemy.name}!")
                    return True

                # Enemy's turn
                print(f"\n{enemy.name}'s turn:")
                enemy_damage = max(0, enemy.attack - player.defense)
                player.health -= enemy_damage
                print(f"{enemy.name} attacks you and deals {enemy_damage} damage!")

                # Check if player is defeated
                if player.health <= 0:
                    print("\nYou have been defeated!")
                    game_over()
                    return False


                # Display updated stats
                player.display_stats()
                enemy.display_stats()

            return True

        def battle_group(player, enemies):
            print("A group of enemies approaches!")
            time.sleep(1)

            while True:
                print("\nYour turn:")
                player.display_stats()
                player_attack = player.attack_enemy()

                # Calculate damage to a random enemy in the group
                target_enemy = random.choice(enemies)
                enemy_damage = target_enemy.take_damage(player_attack)

                print(f"You dealt {enemy_damage} damage to {target_enemy.name}!")

                # Check if the enemy is defeated
                if target_enemy.is_defeated():
                    print(f"{target_enemy.name} has been defeated!")
                    enemies.remove(target_enemy)

                # Check if all enemies are defeated
                if not enemies:
                    print("You have defeated all enemies in the group!")
                    return True

                print("\nEnemies' turn:")
                for enemy in enemies:
                    enemy_attack = enemy.attack_player()
                    player.take_damage(enemy_attack)
                    print(f"{enemy.name} dealt {enemy_attack} damage to you.")

                # Check if the player is defeated
                if player.is_defeated():
                    print("You have been defeated by the enemies. Game Over.")
                    return False

        def second_quest(player):
            print("\nAfter your victory in the village, you hear rumors about a mysterious cave nearby.")
            time.sleep(1)
            print("Brave adventurers have spoken of the dangers and treasures hidden within.")
            time.sleep(1)
            print("You decide to embark on a journey to explore the cave.")

            # Quest: Explore the Cave
            dragon = Enemy("Dragon", health=50, attack=15, defense=10, xp_reward=30)
            troll = Enemy("Troll", health=30, attack=12, defense=8, xp_reward=20)
            goblin_king = Enemy("Goblin King", health=40, attack=18, defense=12, xp_reward=25)

            enemies_to_defeat = [dragon, troll, goblin_king]

            for enemy in enemies_to_defeat:
                print(f"\nYou encounter {enemy.name}!")
                enemy.display_stats()
                time.sleep(1)

                # Battle
                battle_result = battle(player, enemy)
                if not battle_result:
                    print("You were defeated. Game Over.")
                    if game_over() == "yes":
                        main()  # Restart the game
                    else:
                        print("Thanks for playing. Goodbye!")
                        breakpoint

                # Gain XP and check for level up
                player.xp += enemy.xp_reward
                print(f"\nYou gained {enemy.xp_reward} XP!")

                if player.xp >= 50:  # Adjust this XP threshold as needed
                    player.level_up()

            print("\nCongratulations! You have successfully explored the cave.")
            time.sleep(1)
            print("The treasures you found will aid you in your future quests.")
            time.sleep(1)
            print("You have completed the second quest!")

        def third_quest(player):
            print("\nNews spreads of a menacing presence in the dark forest.")
            time.sleep(1)
            print("Reports suggest a formidable boss guarding a treasure deep within.")
            time.sleep(1)
            print("You decide to journey into the dark forest to confront this powerful adversary.")
            # Quest: Confront the Dark Forest Boss
            dark_forest_boss = Enemy("Dark Forest Boss", health=60, attack=20, defense=15, xp_reward=40)
        
            print(f"\nYou encounter {dark_forest_boss.name}!")
            dark_forest_boss.display_stats()
            time.sleep(1)
            # Battle with the Dark Forest Boss
            battle_result = battle(player, dark_forest_boss)
            if not battle_result:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
            # Gain XP and check for level up
            player.xp += dark_forest_boss.xp_reward
            print(f"\nYou gained {dark_forest_boss.xp_reward} XP!")
            if player.xp >= 100:  # Adjust this XP threshold as needed
                player.level_up()
            print("\nCongratulations! You have successfully confronted the Dark Forest Boss.")
            time.sleep(1)
            print("The treasure is now yours to claim.")
            time.sleep(1)
            print("You have completed the third quest!")

        def fourth_quest(player):
            print("\nYou find yourself at a crossroads with different paths leading to various adventures.")
            time.sleep(1)
            print("Choose your next adventure wisely.")
            # Quest: Choose Your Path
            print("1. Climb the Misty Plateau")
            print("2. Enter the Desert Oasis")
            print("3. Journey through the Frozen Tundra")
            choice = input("Enter the number of your choice (1/2/3): ")
            if choice == '1':
                climb_misty_plateau(player)
            elif choice == '2':
                enter_desert_oasis(player)
            elif choice == '3':
                journey_frozen_tundra(player)
            else:
                print("Invalid choice. You hesitate and remain at the crossroads.")
                if game_over(player) == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
        
        def climb_misty_plateau(player):
            print("\nYou decide to climb the Misty Plateau, a high-altitude landscape with swirling mists and hidden perils.")
            time.sleep(1)
            # Quest: Climb the Misty Plateau
            bandit1 = Enemy("Bandit", health=20, attack=10, defense=5, xp_reward=10)
            bandit2 = Enemy("Bandit", health=20, attack=10, defense=5, xp_reward=10)
            bandit3 = Enemy("Bandit", health=20, attack=10, defense=5, xp_reward=10)
            print("\nAs you ascend, you encounter a group of bandits!")
            # Battle with bandits
            battle_result_bandits = battle_group(player, [bandit1, bandit2, bandit3])
            if not battle_result_bandits:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
            time.sleep(1)
            print("\nHaving dealt with the bandits, you reach the summit of the Misty Plateau.")
            time.sleep(1)
            # Boss: Misty Plateau Guardian
            plateau_guardian = Enemy("Misty Plateau Guardian", health=40, attack=15, defense=10, xp_reward=30)
            print(f"\nAt the summit, you face the Misty Plateau Guardian!")
            plateau_guardian.display_stats()
            time.sleep(1)
            # Battle with the Misty Plateau Guardian
            battle_result_boss = battle(player, plateau_guardian)
            if not battle_result_boss:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
            # Victory
            print("\nCongratulations! You have conquered the Misty Plateau and defeated the Misty Plateau Guardian.")
            
        def enter_desert_oasis(player):
            print("\nYou embark on a journey to explore the Desert Oasis, a serene and mysterious place surrounded by endless sand dunes.")
            time.sleep(1)
            # Quest: Explore the Desert Oasis
            sand_monster1 = Enemy("Sand Monster", health=25, attack=12, defense=7, xp_reward=15)
            sand_monster2 = Enemy("Sand Monster", health=25, attack=12, defense=7, xp_reward=15)
            sand_monster3 = Enemy("Sand Monster", health=25, attack=12, defense=7, xp_reward=15)
            print("\nAs you explore, you encounter sand monsters!")
            # Battle with sand monsters
            battle_result_monsters = battle_group(player, [sand_monster1, sand_monster2, sand_monster3])
            if not battle_result_monsters:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
            time.sleep(1)
            print("\nHaving defeated the sand monsters, you arrive at the heart of the Desert Oasis.")
            time.sleep(1)
            # Boss: Desert Oasis Guardian
            oasis_guardian = Enemy("Desert Oasis Guardian", health=45, attack=18, defense=12, xp_reward=35)
            print(f"\nAt the center of the Oasis, you face the Desert Oasis Guardian!")
            oasis_guardian.display_stats()
            time.sleep(1)
            # Battle with the Desert Oasis Guardian
            battle_result_guardian = battle(player, oasis_guardian)
            if not battle_result_guardian:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
            # Victory
            print("\nCongratulations! You have explored the Desert Oasis and defeated the Desert Oasis Guardian.")
        
        def journey_frozen_tundra(player):
            print("\nYou brave the freezing winds and vast icy landscapes as you traverse the Frozen Tundra, a desolate and harsh environment.")
            time.sleep(1)
            # Quest: Traverse the Frozen Tundra
            ice_elemental1 = Enemy("Ice Elemental", health=30, attack=15, defense=10, xp_reward=20)
            ice_elemental2 = Enemy("Ice Elemental", health=30, attack=15, defense=10, xp_reward=20)
            ice_elemental3 = Enemy("Ice Elemental", health=30, attack=15, defense=10, xp_reward=20)
            print("\nDuring your journey, you encounter Ice Elemental monsters!")
            # Battle with Ice Elementals
            battle_result_elementals = battle_group(player, [ice_elemental1, ice_elemental2, ice_elemental3])
            if not battle_result_elementals:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
            time.sleep(1)
            print("\nHaving triumphed over the Ice Elementals, you reach the heart of the Frozen Tundra.")
            time.sleep(1)
            # Boss: Frozen Tundra Guardian
            tundra_guardian = Enemy("Frozen Tundra Guardian", health=50, attack=20, defense=15, xp_reward=40)
            print(f"\nIn the frigid core of the Tundra, you confront the Frozen Tundra Guardian!")
            tundra_guardian.display_stats()
            time.sleep(1)
            # Battle with the Frozen Tundra Guardian
            battle_result_guardian = battle(player, tundra_guardian)
            if not battle_result_guardian:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint
            # Victory
            print("\nCongratulations! You have traversed the Frozen Tundra and defeated the Frozen Tundra Guardian.")

        def fifth_quest(player):
            print("\nYou arrive at a hidden village nestled between lush forests. The villagers speak of a mysterious boss lurking in the shadows.")
            time.sleep(1)

            print("\nYou decide to explore the village to uncover clues about the boss's whereabouts.")

            # Quest: Explore the Hidden Village
            print("\nYou have several choices:")
            print("1. Talk to the village elder.")
            print("2. Investigate the abandoned house.")
            print("3. Follow the strange tracks leading into the forest.")
            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                print("\nThe village elder shares ancient tales about the boss hiding in the ancient ruins.")
                time.sleep(1)
                print("You decide to head towards the ruins.")
                correct_choice = True

            elif choice == '2':
                print("\nInside the abandoned house, you find a map pointing to the boss's hideout in the mountains.")
                time.sleep(1)
                print("You decide to climb the mountains in search of the boss.")
                correct_choice = False

            elif choice == '3':
                print("\nFollowing the strange tracks, you discover a secret passage leading underground.")
                time.sleep(1)
                print("You decide to explore the underground tunnels in pursuit of the boss.")
                correct_choice = False

            else:
                print("\nInvalid choice. You wander aimlessly and miss the opportunity to find the boss.")
                print("Game Over.")
                if game_over(player) == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint

            if not correct_choice:
                print("\nYou didn't make the right choice and missed the opportunity to find the boss.")
                print("Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint

            # Boss: Crystal Goblin (Hidden Village Boss)
            crystal_goblin_boss = Enemy("Crystal Goblin", health=55, attack=22, defense=18, xp_reward=45)
            print(f"\nAs you reach your chosen destination, you encounter the Crystal Goblin!")
            crystal_goblin_boss.display_stats()
            time.sleep(1)

            # Battle with the Crystal Goblin Boss
            battle_result_boss = battle(player, crystal_goblin_boss)
            if not battle_result_boss:
                print("You were defeated. Game Over.")
                if game_over() == "yes":
                    main()  # Restart the game
                else:
                    print("Thanks for playing. Goodbye!")
                    breakpoint

            # Victory
            print("\nCongratulations! You have successfully uncovered the Crystal Goblin Boss in the Hidden Village.")

        def game_over():
            print("\nGame Over!")
            choice = input("Do you want to start over? (yes/no): ").lower()
            return choice

        def main():
            intro()
            player = create_character()
            first_quest(player)
            second_quest(player)
            third_quest(player)
            fourth_quest(player)
            fifth_quest(player)

        if __name__ == "__main__":
            main()


    if GameSelect == "Exit" :
        # Output Manners and Break Loop
        print("Thanks for playing!")
        break
