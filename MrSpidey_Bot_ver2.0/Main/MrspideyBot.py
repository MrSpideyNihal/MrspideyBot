import datetime
import speech_recognition as sr
import webbrowser
import pygame
import subprocess
import keyboard 
import os
import sys
import wave
from define import *
from setting import *

pygame.init()

class VoiceAssistant:
    def __init__(self):
        self.Bot_content = ""
        self.User_content = ""
        self.query = ""
        self.results = ""
        self.font = pygame.font.Font('data\\font.ttf', 20)
        self.window = pygame.display.set_mode((800, 480))
        self.Mic_img = mic_img
        self.setting_img = Setting_img
        self.Stop_image = stop_image
        self.image_mic = self.Mic_img.get_rect(topleft=(10, 82))
        self.image_setting = self.setting_img.get_rect(topleft=(10, 200))

    def display_label(self, surface, text, font, color, x, y):
        label = font.render(text, True, color)
        surface.blit(label, (x, y))

    def DrawAll(self):
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        self.window.fill(BLUE)
        self.window.blit(self.Mic_img, (10, 82))
        self.window.blit(self.setting_img, (10, 200))
        # self.window.blit(self.Stop_image, (32, 330))
        pygame.draw.rect(self.window, ORANGE, (120, 80, 650, 320))
        pygame.draw.rect(self.window, ORANGE, (10, 20, 280, 40))
        self.display_label(self.window, "User:", self.font, BLACK, 122, 100)
        self.display_label(self.window, self.User_content, self.font, BLACK, 200, 100)
        self.display_label(self.window, "Bot :", self.font, BLACK, 122, 150)
        self.display_label(self.window, "Status :", self.font, BLACK, 15, 30)
        self.display_label(self.window, current_time, self.font, BLACK, 650, 30)
        self.display_label(self.window, self.results[0:55], self.font, BLACK, 200, 150)
        self.display_label(self.window, self.results[55:105], self.font, BLACK, 122, 200)
        self.display_label(self.window, self.results[105:160], self.font, BLACK, 123, 250)
        self.display_label(self.window, self.results[160:220], self.font, BLACK, 123, 300)
        self.display_label(self.window, self.results[220:280], self.font, BLACK, 123, 350)
        pygame.display.flip()

    def getLang(self):
        data = open('data\\language.txt', 'r')
        lang_content = data.read()
        return lang_content

    def Checkfile(self):
        myfile = open('data\\voice.txt', 'r')
        content = myfile.read()
        if content == 'male':
            return 0
        elif content == 'female':
            return 1
        else:
            return 0

    def speak(self, audio):
        value = self.Checkfile()
        engine.setProperty('voice',voices[value].id)
        engine.setProperty('rate', 160)
        engine.save_to_file(audio, "temp_audio.wav")
        engine.runAndWait()
        pygame.mixer.init()
        pygame.mixer.music.load("temp_audio.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            if keyboard.is_pressed('q'):
                pygame.mixer.music.stop()
                break
        pygame.mixer.quit()
        os.remove("temp_audio.wav")

    def wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            self.speak("Good Morning")
        elif hour >= 12 and hour < 18:
            self.speak("Good Afternoon")
        else:
            self.speak("Good Evening")
        self.speak(" MR spidey bot version 0.0.1")

    def takeCommand(self):
        self.display_label(self.window, "Listing...", self.font, BLACK, 130, 30)
        pygame.display.flip()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listing...")
            r.pause_thresold = 1
            audio = r.listen(source)
        try:
            self.DrawAll()
            print("Recognizing......")
            self.display_label(self.window, "Recognizing..", self.font, BLACK, 130, 30)
            pygame.display.flip()
            self.query = r.recognize_google(audio, language=self.getLang())
            print(f"User said : {self.query}\n")
        except Exception as e:
            print("Cant hear say it again!")
            self.speak("Cant hear say it again!")
            return "none"
        return self.query

    def search_and_open(self):
        with open('data\\addresses.txt', 'r') as file:
            data = file.read()
        records = data.split('\n\n')
        data_dict = {}
        for record in records:
            lines = record.strip().split('\n')
            if len(lines) >= 2:
                title_line = lines[0].split(': ')
                address_line = lines[1].split(': ')
                if len(title_line) == 2 and len(address_line) == 2:
                    title = title_line[1].strip()
                    address = address_line[1].strip()
                    data_dict[title] = address
        user_title = self.query
        if user_title in data_dict:
            app_path = data_dict[user_title]
            try:
                subprocess.run([app_path])
            except FileNotFoundError:
                print("File not found or path is incorrect.")
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Title not found in the database.")

    def Start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if self.image_mic.collidepoint(mouse_pos):
                        print("Image clicked!")
                        self.query = self.takeCommand().lower()
                        self.User_content = self.query
                        self.DrawAll()
                        if 'your name' in self.query or 'introduce yourself' in self.query or 'who are you' in self.query or 'about you' in self.query:
                            self.results = "Iam MR spidey bot"
                            self.Bot_content = self.results
                            self.DrawAll()
                            print(self.results)
                            self.speak(self.results)
                        elif 'open youtube' in self.query:
                            webbrowser.open("youtube.com")
                            self.results = "Opening youtube.com"
                            self.Bot_content = self.results
                            self.DrawAll()
                            print(self.results)
                            self.speak(self.results)
                        elif 'what can you do' == self.query:
                            self.results = "I can do many things! I can help you with coding, provide recipes, and more. Just ask, and if I can help, I will. If not, I'll let you know."
                            self.Bot_content = self.results
                            self.DrawAll()
                            print(self.results)
                            self.speak(self.results)

                        elif 'open gmail' in self.query:
                            webbrowser.open("Gmail.com")
                            self.results = "Opening Gmail.com"
                            self.Bot_content = self.results
                            self.DrawAll()
                            print(self.results)
                            self.speak(self.results)
                        elif 'your creator' in self.query:
                            self.results = "Nihal Rodge is My creator"
                            self.Bot_content = self.results
                            self.DrawAll()
                            print(self.results)
                            self.speak(self.results)
                        elif 'exit' in self.query or 'quit' in self.query or 'band kro' in self.query:
                            self.speak("Quitting")
                            print("Quiting....")
                            self.results = "Quiting...."
                            self.Bot_content = self.results
                            running = False
                        
                        elif 'space fighter' in self.query:
                            self.speak("Starting game")
                            running = True
                            main()
                        else:
                            if 'none' != self.query:
                                if 'open' in self.query:
                                    self.search_and_open()
                                else:
                                    user_message = {"role": "user", "content": self.query}
                                    messages = [user_message]
                                    model = "gpt-3.5-turbo"
                                    response = client.chat.completions.create(model=model, messages=messages)
                                    self.results = response.choices[0].message.content
                                    if 'OpenAI' in self.results:
                                        self.results = "I Don't like to response question like this !"
                                        self.DrawAll()
                                        self.speak(self.results)
                                    else:
                                        self.DrawAll()
                                        self.speak(self.results)
                    if self.image_setting.collidepoint(mouse_pos):
                               Setting(self.query, self.results)
            self.DrawAll()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    assistant = VoiceAssistant()
    with open("data\\startup.txt", "r") as file:
        status = file.read().strip()
        if status == "Checked":
            assistant.wishme()
    assistant.Start()
    print("User content:", assistant.User_content)
    print("Bot content:", assistant.Bot_content)
