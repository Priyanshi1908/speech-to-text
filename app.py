from flask import Flask, request, jsonify, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # The HTML will be updated.

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    recognizer = sr.Recognizer()
    audio_file = request.files['audio']

    try:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return jsonify({"transcription": text})  # Respond with JSON
    except sr.UnknownValueError:
        return jsonify({"error": "Sorry, could not understand the audio."})
    except sr.RequestError:
        return jsonify({"error": "Request error; please check your internet connection."})

if __name__ == '__main__':
    app.run(debug=True)
