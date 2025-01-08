import os
from flask import Flask, request, jsonify, send_file, Response
from src.chat_generator import generate_podcast_script
from src.tts_handler import TTSHandler

app = Flask(__name__)

# Ensure the assets directory exists
ASSETS_DIR = 'assets'
PDF_DIR = os.path.join(ASSETS_DIR, 'pdfs')
AUDIO_DIR = os.path.join(ASSETS_DIR, 'audios')

os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)

tts_handler = TTSHandler()

@app.route('/upload', methods=['POST'])
def upload_pdf():
    # Get the uploaded PDF file from the request
    file = request.files.get('pdf_file')
    
    if not file:
        return jsonify({"error": "No PDF file provided"}), 400
    
    # Step 1: Save the file locally in the assets folder
    file_path = os.path.join(PDF_DIR, file.filename)
    file.save(file_path)
    
    # Step 2: Generate the conversation script using Gemini AI
    conversation = generate_podcast_script(file_path)

    if not conversation:
        return jsonify({"error": "Failed to generate conversation"}), 500
    
    # Return the conversation as a JSON response
    return jsonify({"conversation": conversation}), 200

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    data = request.get_json()
    conversation = data.get('conversation')
    host_voice = data.get('host_voice')
    expert_voice = data.get('expert_voice')

    if not conversation or not host_voice or not expert_voice:
        return jsonify({"error": "Invalid input data"}), 400

    audio_files = []
    for i, message in enumerate(conversation):
        voice_id = host_voice if message['speaker'] == 'Host' else expert_voice
        output_filename = os.path.join(AUDIO_DIR, f"message_{i}.mp3")
        audio_path = tts_handler.generate_audio(message['text'], voice_id, output_filename)
        if audio_path:
            audio_files.append(audio_path)

    combined_audio_path = os.path.join(AUDIO_DIR, "combined_podcast.mp3")
    combined_audio = tts_handler.combine_audio(audio_files, combined_audio_path)

    if not combined_audio:
        return jsonify({"error": "Failed to combine audio"}), 500

    audio_file = os.path.join(AUDIO_DIR, "combined_podcast.mp3")
    if not os.path.exists(audio_file):
        return jsonify({"error": "Audio file not found"}), 404

    return send_file(audio_file, as_attachment=True)


@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test successful."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
