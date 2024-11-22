import random

song_list = ["august", "style", "seven", "dress"]
random_song = random.choice(song_list)
guessedSong = ['_'] * len(random_song)

attempts = 13

print(random_song)

print("---------------Welcome To Taylor Swift Song Guessing Game-------------\n")
print(">Guess the song and Make Taylor Proud!!")
print(">You have 13 attempts to guess the song.")

while attempts > 0:
    print("\nCurrent Song: " + ' '.join(guessedSong))
    user_guess = input("Guess a letter: ")
    if user_guess in random_song:
        for i in range(len(random_song)):
            if random_song[i] == user_guess:
                guessedSong[i] = user_guess
        print("Great choice swiftie!!")
    else:
        attempts -= 1
        print(f"Sorry, you guessed the wrong letter! You have {attempts} attempts left!")

    if '_' not in guessedSong:
            print("Well done you have made Taylor proud!!")
            print("The song is: " + random_song)
            break