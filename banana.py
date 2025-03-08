# Pseudocode
# 1. Print introduction
# 2. Ask user for name and store it
# 3. Present fruit choices: Apple, Banana, Orange
# 4. Ask user to pick one
# 5. If user picks Banana, they lose because it's a bomb
# 6. Otherwise, they win
# 7. End game with a win or lose message

# Introduction
print("Welcome to the Bomb Squad!")
name = input("First whats is your name, new employe? ")
print(f"Hello {name}, This will be your first misson. We received intell that one of these fruits has a bomb inside it, Choose wisely!")

# Game loop
game_over = False
while not game_over:
    print("Pick a fruit: An Apple, Banana, or Orange")
    choice = input("Which fruit do you pick? ")
    
    if choice in ["banana", "the banana", "Banana"]:
        print("BOOM! The banana had a bomb inside! You lose!")
        game_over = True
    elif choice in ["apple", "the apple", "Apple", "orange", "the orange", "Orange"]:
        print("Congratulations! You picked the safe fruit and survived!")
        game_over = True
    else:
        print("Choose one of the fruits. Try again.")
        continue

print("Game Over. You died to a BANANA!")
print("No offense...")
