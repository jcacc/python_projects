"""Hacking minigame"""
"""to be a clone of the Hacking game from Fallout 3"""
import random, sys

GARBAGE_CHARS = '~!@#$%^&*()_+-{}[]|;:,.<>?/'


with open('seven-letter-words.txt') as wordListFile:
    WORDS = wordListFile.readlines()
for i in range (len(WORDS)):
    WORDS[i] = WORDS[i].strip.upper()

def main():
    print('''Hacking minigame, by Joe Accardi joe@accardi.xyz
    Find the password in the computer's memory. You are given clues after
    each guess. For example, if the secret password is MONITOR but the
    player guessed CONTAIN, they are given the hint that 2 out of 7 letters
    were correct, because both MONITOR and CONTAIN have the letter O and N
    as their 2nd and 3rd letter. You get four guesses.\n''')
    input('Press ENTER to begin...')

    gameWords = getWords()
    computerMemory = getComputerMemoryString(gameWords)
    secretPassword = random.choice(gameWords)

    print(computerMemory)
    for triesRemaining in range(4, 0, -1):
        playerMove = askForPlayerGuess(gameWords, triesRemaining)
        if playerMove == secretPassword:
            print('𝐀 𝐂 𝐂 𝐄 𝐒 𝐒   𝐆 𝐑 𝐀 𝐍 𝐓 𝐄 𝐃')
            return
        else:
            numMatches = numMatchingLetters(secretPassword, playerMove)
            print('Access Denied ({}/7 correct)'.format(numMatches))
        print('Out of tries. Secret password was {}.'.format(secretPassword))

def getWords():
    secretPassword = random.choice(WORDS)
    words = [secretPassword]

    while




