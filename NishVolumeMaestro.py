import speech_recognition as sr
import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize the voice recognizer
recognizer = sr.Recognizer()

# Initialize text-to-speech engine for voice feedback
engine = pyttsx3.init()

# Get the default audio playback device
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

# Initialize the audio endpoint volume interface
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Define a function to set the system volume
def set_volume(level):
    volume.SetMasterVolumeLevelScalar(level, None)

# Define a function to get the current volume level
def get_current_volume():
    return int(volume.GetMasterVolumeLevelScalar() * 100)

# Define volume range settings
min_volume = 20  # Minimum volume level (adjust as needed)
max_volume = 80  # Maximum volume level (adjust as needed)

# Say welcome message
engine.say("Welcome to NishVolumeMaestro.")
engine.say("Control your PC or laptop volume using your voice.")
engine.runAndWait()

# Listen for voice commands
with sr.Microphone() as source:
    engine.say("Listening for volume control commands...")
    engine.runAndWait()

    recognizer.adjust_for_ambient_noise(source)

    while True:
        try:
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio).lower()

            if "increase volume" in command:
                engine.say("Sure, please specify the desired volume level.")
                engine.runAndWait()
                audio = recognizer.listen(source)
                level_command = recognizer.recognize_google(audio).lower()
                try:
                    level = int(level_command)
                    new_volume = min(get_current_volume() + level, max_volume)
                    set_volume(new_volume / 100.0)
                    engine.say(f"Volume increased to {new_volume}%")
                except ValueError:
                    engine.say("Invalid level. Volume not changed.")
            elif "decrease volume" in command:
                engine.say("Sure, please specify the desired volume level.")
                engine.runAndWait()
                audio = recognizer.listen(source)
                level_command = recognizer.recognize_google(audio).lower()
                try:
                    level = int(level_command)
                    new_volume = max(get_current_volume() - level, min_volume)
                    set_volume(new_volume / 100.0)
                    engine.say(f"Volume decreased to {new_volume}%")
                except ValueError:
                    engine.say("Invalid level. Volume not changed.")
            elif "mute" in command:
                set_volume(0.0)  # Mute the volume
                engine.say("Volume muted")
            elif "unmute" in command:
                set_volume(1.0)  # Unmute the volume
                engine.say(f"Volume unmuted to {get_current_volume()}%")
            elif "current volume" in command:
                current_vol = get_current_volume()
                engine.say(f"Current volume is {current_vol}%")
            elif "exit" in command:
                engine.say("Exiting the program...")
                engine.runAndWait()
                break
            else:
                engine.say("Command not recognized")
            engine.runAndWait()
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            engine.say(f"Error: {e}")
        finally:
            engine.runAndWait()
