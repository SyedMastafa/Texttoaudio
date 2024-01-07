from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

def text_to_speech(text, language='en', output_file='output.mp3'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(output_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form['text']
    text_to_speech(text)
    return render_template('index.html', audio_generated=True)

@app.route('/download')
def download():
    return send_file('output.mp3', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

