import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

print("Male:", voices[0].name)
print("Female:", voices[1].name)

engine.setProperty("voice", voices[0].id)
engine.say("Hello, I am Alex, the technical interviewer.")
engine.runAndWait()

engine.setProperty("voice", voices[1].id)
engine.say("Hello, I am Sarah, the HR interviewer.")
engine.runAndWait()