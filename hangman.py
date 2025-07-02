import random

# Predefined list of words
word_list = ["apple", "banana", "orange", "grapes", "mango"]

# Pick a random word
word = random.choice(word_list)
word_letters = list(word)  # break into letters
guessed_letters = []       # store guessed letters
tries = 6                  # number of wrong tries allowed

print("🕹️ Welcome to Hangman!")
print(f"Hint: The word has {len(word)} letters.")

while tries > 0:
    display_word = ""
    for letter in word_letters:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord:", display_word.strip())

    # Check if all letters have been guessed
    if all(letter in guessed_letters for letter in word_letters):
        print("🎉 You guessed it! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word_letters:
        tries -= 1
        print(f"❌ Incorrect! Tries left: {tries}")
    else:
        print("✅ Good guess!")

else:
    print("💀 You ran out of tries! The word was:", word)
