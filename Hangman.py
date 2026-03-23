import random
words = {
    "python": "A popular programming language",
    "apple": "A fruit",
    "tiger": "A wild animal",
    "india": "A country",
    "table": "Used to keep things"
}
word = random.choice(list(words.keys()))
hint = words[word]
guessed_letters = []
attempts = 6
print("🎮 Welcome to Hangman!")
print("Hint:", hint)
while attempts > 0:
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    if "_" not in display:
        print("🎉 You guessed the word!")
        break
    guess = input("Enter a letter: ").lower()
    if guess in guessed_letters:
        print("⚠ Already guessed!")
        continue
    guessed_letters.append(guess)
    if guess not in word:
        attempts -= 1
        print(f"❌ Wrong! Attempts left: {attempts}")
    else:
        print("✅ Correct!")
if attempts == 0:
    print("💀 You lost! The word was:", word)