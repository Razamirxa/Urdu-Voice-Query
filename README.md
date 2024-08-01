# Urdu-Voice-Query
Speech-to-Text and Text-to-Speech Assistant in Urdu

## Overview

Urdu Voice Query is a powerful voice assistant application built with Streamlit. It allows users to record their voice in Urdu, transcribe the spoken content to text, process the text using a generative AI model, and respond with a spoken response in Urdu. The application uses Google Generative AI, Google Text-to-Speech (gTTS), and other libraries to achieve this functionality.

## Features

- **Speech-to-Text**: Converts spoken Urdu input into text using `speech_to_text`.
- **Generative AI Response**: Processes the transcribed text to generate a response in Urdu using Google Generative AI.
- **Text-to-Speech**: Converts the AI-generated text response back to speech in Urdu using gTTS.
- **Streamlit Interface**: Provides an interactive and user-friendly web interface.

## Prerequisites

- Python 3.8 or higher
- An API key for Google Generative AI
- `ffmpeg` installed on your system (for audio processing)


2. **Use the interface**:
    - Open your web browser and go to `http://localhost:8501`.
    - Click the record button to record your voice in Urdu.
    - Wait for the speech-to-text conversion.
    - The assistant will respond with a text message in Urdu.
    - The response will be converted to speech and played back.

