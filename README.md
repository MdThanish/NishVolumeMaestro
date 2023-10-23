# NishVolumeMaestro

# 🎙️ Voice-Controlled Volume Adjustment Project

## Introduction

Welcome to the Voice-Controlled Volume Adjustment Project (Nish Volume Maestro)! This Python script empowers you, Mohamed Thanish of the mystical realm of 2023, with the magic of voice. It allows you to effortlessly control the volume of your Windows-based computer or laptop. By harnessing the capabilities of cutting-edge libraries like SpeechRecognition and pyttsx3, this program transforms your voice commands into seamless volume adjustments.

## Contact

💌 If you seek guidance, have questions, or wish to delve deeper into the arcane arts, reach out to the enchanter behind the code, Mohamed Thanish, via [ mohamedthanish14@gmail.com ]or [LinkedIn]( https://www.linkedin.com/in/mohamed-thanish-m-b82053218/ ).

![its me ](https://media.licdn.com/dms/image/C4D03AQGKFO-u-lClJA/profile-displayphoto-shrink_800_800/0/1661606445764?e=1703721600&v=beta&t=HWx7xigPN5AlHGp5plWPxV_iV3uRJqgI1QwOTghPJmw)


## Code Flow

1. **Import Libraries**:
   - Our enchanting journey begins by importing the essential libraries:
     - `speech_recognition`: It breathes life into voice recognition.
     - `pyttsx3`: The sorcerer behind text-to-speech feedback.
     - `ctypes` and `comtypes`: The mystical gateways to Windows audio settings.
     - `pycaw`: The key to audio manipulation.

2. **Initialize Recognizer and Text-to-Speech Engine**:
   - We conjure the recognizer using `sr.Recognizer()`.
   - The text-to-speech engine awakens with `pyttsx3.init()`.

3. **Get Default Audio Playback Device**:
   - Our quest for the perfect audio device begins with `AudioUtilities.GetSpeakers()`.
   - With a wave of the wand, we activate the audio endpoint volume interface.

4. **Volume Control Functions**:
   - Our spellbook includes `set_volume(level)` to command the system volume.
   - `get_current_volume()` unveils the current volume level.

5. **Volume Range Settings**:
   - Customize your magic with minimum and maximum volume levels (`min_volume` and `max_volume`).

6. **Welcome Message**:
   - Let your ears feast upon the melodious welcome message as we unveil the program's potential through the voice of the text-to-speech engine.

7. **Listen for Voice Commands**:
   - We enter the enchanted forest of voice commands, ever-ready to heed your words through the microphone.

8. **Voice Command Handling**:
   - "increase volume": Share your desired volume level, and we shall raise it, announcing the outcome.
   - "decrease volume": Request your preferred volume level, and we shall lower it, revealing the results.
   - "mute": Silence shall descend upon the audio realm, and we shall proclaim it.
   - "unmute": We lift the silence with precision, and the volume shall resound at its previous level.
   - "current volume": Seek to know the current volume, and we shall reveal its secret.
   - "exit": When it's time to part ways, a courteous exit is granted.

9. **Exception Handling**:
   - In the event of mysterious voice phenomena or communication breakdowns (`sr.UnknownValueError`), our enchantments remain resilient.
   - Should the winds of error (`sr.RequestError`) blow, rest assured, we shall inform you.

10. **Voice Feedback**:
    - Our voice shall be your loyal companion, guiding you through this mystical journey, narrating every action and safeguarding against unseen obstacles.

11. **Copyright and License**:

    Copyright 2023 Mohamed Thanish

    This enchanting code is shared under the benevolent terms of the **Magician's License**, a truly open-source incantation. As a magician of code, you are encouraged to weave your own spells upon this code for your unique purposes, just as you have witnessed here.

    By using this code, you acknowledge and agree to the following mystical principles:

    - You are free to share and adapt this code for any purpose, whether magical or mundane.
    - Attribution is appreciated but not required. Credit is a token of respect among wizards.
    - The code comes as-is, without any warranties. Use it wisely and responsibly, as magic can be unpredictable.

    [License Details]

🪄 **MIT License**

Copyright (c) 2023 Mohamed Thanish

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

