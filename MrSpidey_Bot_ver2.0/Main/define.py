#GUI-----------------------Defines_-----------#
# Set up the display
import pygame
from openai import OpenAI
import pyttsx3

width, height = 790, 420
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ver 0.1')


#images
mic_img = pygame.image.load('pics\\mainmic.png')
Setting_img = pygame.image.load('pics\\setting.png')
stop_image = pygame.image.load('pics\\cross.png')
image_mic = mic_img.get_rect()
image_mic.topleft = (10, 82)
image_setting = Setting_img.get_rect()
image_setting.topleft = (10, 200)
image_stop = stop_image.get_rect()
image_stop.topleft = (32,330)

Play_Image = pygame.image.load('pics\\play.png')
Exit_Image = pygame.image.load('pics\\exit.png')
image_play = Play_Image.get_rect()
image_play.topleft = (300, 150)
image_exit = Exit_Image.get_rect()
image_exit.topleft = (300, 250)

Player_Image = pygame.image.load('pics\\player.png')
metor_Image = pygame.image.load('pics\\meteor2.png')
metor_Image1 = pygame.image.load('pics\\meteor2.png')
metor_Image3 = pygame.image.load('pics\\meteor2.png')
metor_Image2 = pygame.image.load('pics\\meteor2.png')
hearts = pygame.image.load('pics\\hearts.png')

music = 'data\\bg.mp3'
damage = 'data\\damage.wav'

# Colors
ORANGE = (255, 169, 0, 1)
BLUE = (0, 198, 255, 1)
BLACK = (0,0,0)
Black = (0,0,0)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
client = OpenAI(
api_key = "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"
)

#languages
languages = [
    'Hindi (India): hi-IN',
    'English (India): en-IN',
    'Bengali (India): bn-IN',
    'Telugu (India): te-IN',
    'Marathi (India): mr-IN',
    'Tamil (India): ta-IN',
    'Urdu (India): ur-IN',
    'Gujarati (India): gu-IN',
    'Kannada (India): kn-IN',
    'Odia (India): or-IN',
    'Punjabi (India): pa-IN',
    'Malayalam (India): ml-IN',
    'Assamese (India): as-IN',
    'Maithili (India): mai-IN',
    'Santali (India): sat-IN',
    'Nepali (India): ne-IN',
    'Konkani (India): kok-IN',
    'Bodo (India): brx-IN',
    'Dogri (India): doi-IN',
    'Manipuri (India): mni-IN',
    'Sindhi (India): sd-IN'
]

