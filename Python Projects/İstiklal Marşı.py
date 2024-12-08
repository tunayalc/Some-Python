import os 
import threading 
import time 
import docx 
import pygame 

# Read Istiklal Marsi from the Word document
file = docx.Document("C:/Users/OWNER/Downloads/ödev3.docx")
istiklal = ""

# Combine all paragraphs in the Word document into a single text variable
for paragraph in file.paragraphs:
    istiklal += paragraph.text + "\n"

# Reverse Istiklal Marsi (character-wise)
reversed_istiklal = "".join(reversed(istiklal))

# Initialize Pygame sound system
pygame.mixer.init()

# Add a note sound for each character
notes = {}
for char in set(istiklal.lower()):
    if char.isalpha():  # Only letters have corresponding .wav files
        notes[char] = pygame.mixer.Sound(f"c:/Users/OWNER/Downloads/nota/{char}.wav")

# Function to play the sound of a character
def play_sound(char):
    channel = pygame.mixer.Channel(0)
    channel.play(notes[char])
    time.sleep(0.1)  # Wait for a short period after playing each character

# Thread to play the regular Istiklal Marsi
class PlayRegularIstiklal(threading.Thread): 
    def run(self):
        for char in istiklal:
            char = char.lower()
            if char.isalpha():  # Play only alphabetic characters
                play_sound(char)

# Thread to play the reversed Istiklal Marsi
class PlayReversedIstiklal(threading.Thread): 
    def run(self):
        for char in reversed_istiklal:
            char = char.lower()
            if char.isalpha():  # Play only alphabetic characters
                play_sound(char)

# Start both threads (regular and reversed)
regular = PlayRegularIstiklal()
reversed = PlayReversedIstiklal()
regular.start()
reversed.start()
