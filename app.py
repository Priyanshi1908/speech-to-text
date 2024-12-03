from flask import Flask, request, jsonify, render_template
import speech_recognition as sr
import os

app = Flask(__name__)

@app.route('/')
def index():
    # The HTML will be rendered from the templates directory
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    recognizer = sr.Recognizer()
    audio_file = request.files['audio']

    try:
        # Process the audio file
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        return jsonify({"transcription": text})  # Respond with JSON
    except sr.UnknownValueError:
        return jsonify({"error": "Sorry, could not understand the audio."})
    except sr.RequestError:
        return jsonify({"error": "Request error; please check your internet connection."})

if __name__ == '__main__':
    # Use the PORT environment variable for deployment, default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
