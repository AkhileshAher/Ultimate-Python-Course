import pyttsx3

names = [
    "StupidProgramm1", "AayushGarg15", "Yuniek", "NiteshUpadhyay2", "RAMESHKUMAR69",
    "AshishKushwaha4", "AshokBhatt", "MILLANDREME", "ValorantAccoun4", "Sanjeevthakur8",
    # Add the rest of the names from your list here...
]

# Initialize the text-to-speech engine
engine = pyttsx3.init()

for name in names:
    message = f"Shoutout to {name}"
    print(message)  # Optional: To see the names being processed
    engine.say(message)
    engine.runAndWait()     # Run the engine to speak out all names


