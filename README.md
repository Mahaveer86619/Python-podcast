# AI-Powered Podcast Generator

This project is a full-stack application (Python backend, Flutter frontend) that automates the creation of engaging podcasts from user-uploaded PDF documents.  It leverages the power of AI to transform written material into natural-sounding conversations, complete with realistic voiceovers and a simulated podcast format.

## Project Overview

This application simplifies the podcast creation process by automating several key steps:

1.  **PDF Upload:** Users upload their source material in PDF format through the Flutter mobile app.
2.  **Content Processing:** The Python backend extracts the text content from the uploaded PDF.
3.  **AI-Driven Conversation Generation:** The extracted text is then used to generate a natural-sounding conversation using the Gemini API.  This conversation is designed to mimic the flow and style of a live podcast, complete with back-and-forth dialogue.
4.  **Voice Selection:** Users can choose from a selection of AI-generated voices for both the "host" and the "expert" participating in the simulated podcast.  This allows for customization and adds a layer of personality to the generated content.
5.  **Text-to-Speech Conversion:** The generated conversation script is then converted into high-quality audio using Deepgram's text-to-speech API. This ensures that the podcast sounds natural and engaging.
6.  **Podcast Assembly:**  FFmpeg is used to process and combine the audio output into a standard MP3 file, the common format for podcasts.
7.  **Download:**  Users can then download the generated MP3 podcast directly from the Flutter app.

## Features

*   **Automated Podcast Creation:**  Streamlines the entire podcast production process, from PDF upload to final MP3 download.
*   **AI-Powered Conversation Generation:**  Uses the Gemini API to create realistic and engaging dialogues based on the uploaded content.
*   **Voice Customization:**  Offers a choice of AI voices for both the host and expert, allowing for personalized podcast creation.
*   **High-Quality Audio:**  Leverages Deepgram's text-to-speech API for clear and natural-sounding voiceovers.
*   **Standard MP3 Output:**  Generates podcasts in the widely compatible MP3 format.
*   **User-Friendly Interface:**  The Flutter mobile app provides an intuitive interface for uploading PDFs, selecting voices, and downloading podcasts.
*   **Full-Stack Architecture:**  Built using a robust Python backend and a cross-platform Flutter frontend.

## Technologies Used

*   **Backend (Python):**
    *   Gemini API (`google-generativeai`)
    *   Deepgram API (`deepgram`)
    *   FFmpeg
    *   `PyPDF2` (or similar PDF processing library)
    *   `pydub` (or similar audio processing library, if used)
    *   Other relevant Python libraries
*   **Frontend (Flutter):**
    *   Flutter framework
    *   Relevant Flutter packages (e.g., for networking, file handling, audio playback, etc.)

## Setup and Installation (Example)

**Python Backend:**

1.  Clone the repository: `git clone https://github.com/Mahaveer86619/Python-podcast`
2.  Create a virtual environment: `python3 -m venv venv`
3.  Activate the environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
4.  Install dependencies: `pip install -r requirements.txt`
5.  Configure API keys and other settings in `app.py` (or your main Python file).
6.  Run the server: `python app.py`

**Flutter Frontend:**

1.  Clone the repository: `git clone https://github.com/Mahaveer86619/AI-podcast`
2.  Install Flutter dependencies: `flutter pub get`
3.  Connect the Flutter app to the Python backend (configure API endpoints).
4.  Run the app: `flutter run`

## Usage

1.  Launch the Flutter app.
2.  Upload a PDF file.
3.  Select the desired voices for the host and expert, from deepgram documentation.
4.  Generate the podcast.
5.  Download the MP3 file.

## Demo

A video demonstrating the application's functionality and a sample podcast output are available in the following Google Drive folder: [Link to Google Drive Folder](https://drive.google.com/drive/folders/1ZBMkVY_jQElIPTCiTUZZoGWpkVByySZA?usp=sharing)

