import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Function to record audio and convert it to text
def record_audio_and_recognize():
  """Records audio from the microphone and returns the recognized text."""
  with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

  try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    return text
  except sr.UnknownValueError:
    print("Sorry, I could not understand audio")
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
  return None

# Get user input to start recording
user_input = input("Ready to record? (y/n): ")

if user_input.lower() == "y":
  recognized_text = record_audio_and_recognize()
  # You can do something with the recognized text here, like printing it or storing it in a variable.
  if recognized_text:
    print(f"Here's the recognized text: {recognized_text}")
else:
  print("Exiting...")
