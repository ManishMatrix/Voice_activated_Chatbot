# 🎙️ VoiceGPT Assistant

This Python-based voice assistant listens to your speech, transcribes it, sends the text to OpenAI's GPT-3 model, and then reads the generated response out loud using text-to-speech.

## 📌 Features

- 🧠 Uses **OpenAI GPT-3 (text-davinci-003)** for intelligent text generation  
- 🗣️ Converts **speech to text** using Google's Speech Recognition API  
- 🔊 Converts **text to speech** using `pyttsx3`  
- 🎧 Continuously listens for the wake word `"hello"` to start interaction  
- ❌ Say `"stop"` to end the assistant session  

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/voicegpt-assistant.git
cd voicegpt-assistant
2. Install dependencies
pip install openai pyttsx3 SpeechRecognition
You also need to install PyAudio:
pip install pipwin
pipwin install pyaudio

🔐 OpenAI API Key
Add your OpenAI API key in the script (SOURCE_CODE.py):
openai.api_key = "your-api-key-here"

🚀 Usage
Run the script:
Say "hello" to activate the assistant.
Ask any question.
Say "stop" to end the session.

🧠 Example Interaction
You: hello  
Assistant: How can I help you?  
You: What is the capital of France?  
Assistant: The capital of France is Paris.  


🤝 Contributions
Pull requests and stars are welcome!
