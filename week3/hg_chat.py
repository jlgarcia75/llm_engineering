"""# Required Python packages
gradio==3.39.0
SpeechRecognition==3.10.0
gTTS==2.3.2
pydub==0.25.1  # For audio processing (optional)

# Install with:
# pip install gradio SpeechRecognition gTTS pydub
Note:

For audio processing, you might need to install additional system dependencies:
On Linux: sudo apt-get install portaudio19-dev python3-pyaudio
On macOS: brew install portaudio
On Windows: Download PyAudio wheel from here
How to Run

Save the code to a file (e.g., chatbot.py)
Install the required packages
Run the script: python chatbot.py
Access the interface at http://localhost:7860

"""

import os
import time

import gradio as gr
import speech_recognition as sr
from gtts import gTTS

# Initialize recognizer
recognizer = sr.Recognizer()


def process_input(text_input, audio_input):
    combined_input = ""

    # Process text input if provided
    if text_input:
        combined_input += f"[Text] {text_input}\n"

    # Process audio input if provided
    if audio_input:
        try:
            with sr.AudioFile(audio_input) as source:
                audio_data = recognizer.record(source)
                audio_text = recognizer.recognize_google(audio_data)
                combined_input += f"[Audio] {audio_text}"
        except Exception as e:
            combined_input += f"[Audio Error] {str(e)}"

    # Generate response (replace with your actual chatbot logic)
    if not combined_input:
        response = "Please provide either text or audio input."
    else:
        response = (
            f"I received your input:\n{combined_input}\n\nThis is a simulated response."
        )

    # Convert response to speech
    tts = gTTS(text=response, lang="en")
    audio_file = "response.mp3"
    tts.save(audio_file)

    return response, audio_file


# Create Gradio interface
with gr.Blocks(title="Multimodal Chatbot") as demo:
    gr.Markdown("# 🤖 Audio-Text Chatbot")
    gr.Markdown("Enter text or upload an audio file to chat with the bot.")

    with gr.Row():
        text_input = gr.Textbox(
            label="Text Input", placeholder="Type your message here..."
        )
        audio_input = gr.Audio(label="Audio Input", source="upload", type="filepath")

    submit_btn = gr.Button("Submit", variant="primary")

    with gr.Row():
        text_output = gr.Textbox(label="Chatbot Response", interactive=False)
        audio_output = gr.Audio(label="Spoken Response", interactive=False)

    submit_btn.click(
        fn=process_input,
        inputs=[text_input, audio_input],
        outputs=[text_output, audio_output],
    )

if __name__ == "__main__":
    demo.launch()
