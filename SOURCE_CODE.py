import openai
import pyttsx3
import speech_recognition as sr
import time
 # Set your OpenAI API key 7 openai.api_key=""
openai.api_key="you api key"

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def audiototext(filename):
    recognizer= sr.Recognizer()
    with sr.AudioFile(filename) as source: 
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('Skipping unknown error')

def generate_response(prompt): 
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"] [0] ["text"]

def speak_text(text):
    engine.say(text) 
    engine.runAndWait()

def main():
    while True:
        print("Speak 'helloo' to start")
        with sr.Microphone() as source:
            recognizer =sr.Recognizer()
            audio =recognizer.listen(source)
        try:
            transcription= recognizer.recognize_google(audio)
            if transcription.lower()=="hello":
            #Record audio
                filename ="input.wav"
                print("How can I help you?")
                with sr.Microphone() as source:
                    recognizer=sr.Recognizer()
                    source.pause_threshold = 1
                    audio= recognizer.listen(source, phrase_time_limit=None, timeout=None) 
                    with open(filename, "wb") as f:
                        f.write(audio.get_wav_data())
                #Transcribe audio to text
                text = audiototext(filename)
                if text:
                    print(f"You said: {text}")
                    if text.lower() == "stop":
                        break
                # Generate response using GPT-3 
                    response = generate_response(text)
                    print(f"GPT-3 says: {response}")
                    #Read response using text-to-speech
                    speak_text(response)
        except Exception as e:
            print("An error occurred: {}".format(e))

if __name__=="__main__":
    main()