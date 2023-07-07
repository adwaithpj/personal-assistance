
import speech_recognition as sr
import datetime

import requests

def get_bard_response(speech):
  """Gets the Bard's response to the given speech."""
  url = "https://bard.ai/api/v1/generate"
  data = {"prompt": speech}
  response = requests.post(url, json=data)
  return response.json()["text"]

def main():
  """Runs the speech recognition and Bard interaction loop."""
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

  try:
    speech = recognizer.recognize_google(audio)
    print("You said: " + speech)
    bard_response = get_bard_response(speech)
    print("Bard says: " + bard_response)
  except:
    print("Sorry, I didn't understand that.")

if __name__ == "__main__":
  main()
