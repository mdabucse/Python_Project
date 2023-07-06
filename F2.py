from flask import Flask, render_template, request, jsonify
import pygame
import random

app = Flask(__name__)

# Initialize pygame
pygame.init()

#Set the frequency and size of the audio
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)

# List of MOODS
mood_list = ["Happy", "Depression", "Alone", "Love", "Beast Mood"]

# List of songs
happy_list = ["Sodakku-Mela-Sodakku-MassTamilan.com.mp3", "Mersalayitten.mp3", "Yaaraiyum-Ivlo-Azhaga-MassTamilan.io.mp3",
              "Aalaporan-Thamizhan-MassTamilan.com.mp3", "Marana-Mass-MassTamilan.org.mp3"]
depression_list = ["Poi-Vazhva.mp3", "Kanave-Kanave-MassTamilan.com.mp3", "Yean-Ennai-Pirindhaai-MassTamilan.org.mp3",
                   "Ennodu-Nee-Irundhal.mp3", "Yennai-Maatrum-Kadhale.mp3"]
alone_list = ["En-Iniya-Thanimaye-MassTamilan.io.mp3", "Enakenna-Yaarum-Illaye-(Zingaroe-Remix)-MassTamilan.com.mp3",
              "Idhuvum-Kadandhu-Pogum-(The-Healing-Song)-MassTamilan.fm.mp3", "Kadhal-Valarthen.mp3", "Othayilae.mp3"]
love_list = ["Rowdy-Baby-MassTamilan.org.mp3", "Otha-Sollaala.mp3", "Idhazhin-Oram.mp3",
             "Vilambara-Idaiveli-MassTamilan.com.mp3", "Yaanji-MassTamilan.com.mp3"]
beast_list = ["Vaathi-Raid-MassTamilan.io.mp3", "Danga-Maari-Oodhari.mp3", "Mersalayitten.mp3", "Vilayadu-Mangatha.mp3",
              "Guleba-Sokama-Sokama-MassTamilan.com.mp3"]

# Endpoint to play the selected song
@app.route('/play-song', methods=['POST'])
def play_song():
    data = request.get_json()
    mood_number = int(data['moodNumber'])
    
    # Load the selected song based on the mood number
    if mood_number == 1:
        selected_song = random.choice(happy_list)
    elif mood_number == 2:
        selected_song = random.choice(depression_list)
    elif mood_number == 3:
        selected_song = random.choice(alone_list)
    elif mood_number == 4:
        selected_song = random.choice(love_list)
    elif mood_number == 5:
        selected_song = random.choice(beast_list)
    else:
        return jsonify({'success': False})
    
    # Play the selected song
    pygame.mixer.music.load(selected_song)
    pygame.mixer.music.play()
    
    return jsonify({'success': True})

# Endpoint to stop the currently playing song
@app.route('/stop-song', methods=['POST'])
def stop_song():
    pygame.mixer.music.stop()
    
    return jsonify({'success': True})

# Serve the HTML file
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
