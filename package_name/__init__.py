import os
import sys
import time


def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)

    time.sleep(1)


def matrix():
    os.system("cls")
    typewriter("Wake up, Neo...")
    os.system("cls")
    typewriter("The Matrix has you...")
    os.system("cls")
    typewriter("Follow the white rabbit.")
    os.system("cls")
