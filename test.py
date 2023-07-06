from flask import Flask, render_template, request
import pygame
import random

app = Flask(__name__)

# Initialize pygame
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

# List of MOODS
mood_list = ["Happy","Depression", "Alone", "Love", "Beast Mood"]

# List of songs
happy_list = ["Sodakku-Mela-Sodakku-MassTamilan.com.mp3", "Mersalayitten.mp3", "Yaaraiyum-Ivlo-Azhaga-MassTamilan.io.mp3",
              "Aalaporan-Thamizhan-MassTamilan.com.mp3", "Marana-Mass-MassTamilan.org.mp3"]
depression_list = ["Poi-Vazhva.mp3", "Kanave-Kanave-MassTamilan.com.mp3", "Yean-Ennai-Pirindhaai-MassTamilan.org.mp3",
                   "Ennodu-Nee-Irundhal.mp3", "Yennai-Maatrum-Kadhale.mp3"]
alone_list = ["En-Iniya-Thanimaye-MassTamilan.io.mp3", "Enakenna-Yaarum-Illaye-(Zingaroe-Remix)-MassTamilan.com.mp3",
              "Idhuvum-Kadandhu-Pogum-(The-Healing-Song)-MassTamilan.fm.mp3", "Kadhal-Valarthen.mp3", "Othayilae.mp3"]
love_list = ["Rowdy-Baby-MassTamilan.org.mp3", "Otha-Sollaala.mp3", "Idhazhin-Oram.mp3", "Vilambara-Idaiveli-MassTamilan.com.mp3",
             "Yaanji-MassTamilan.com.mp3"]
beast_list = ["Vaathi-Raid-MassTamilan.io.mp3", "Danga-Maari-Oodhari.mp3", "Mersalayitten.mp3", "Vilayadu-Mangatha.mp3",
              "Guleba-Sokama-Sokama-MassTamilan.com.mp3"]

@app.route('/')
def index():
    return render_template('D:\Programs\Python\Project\index.html', mood_list=mood_list)

@app.route('/play_song', methods=['POST'])
def play_song():
    mood_number = int(request.form['mood_number'])
    if 1 <= mood_number <= len(mood_list):
        selected_song = get_random_song(mood_number)
        pygame.mixer.music.load(selected_song)
        pygame.mixer.music.play()
        return "Playing song: " + selected_song
    else:
        return "Invalid mood number"

def get_random_song(mood_number):
    if mood_number == 1:
        return random.choice(happy_list)
    elif mood_number == 2:
        return random.choice(depression_list)
    elif mood_number == 3:
        return random.choice(alone_list)
    elif mood_number == 4:
        return random.choice(love_list)
    elif mood_number == 5:
        return random.choice(beast_list)

if __name__ == '__main__':
    app.run(debug=True)
