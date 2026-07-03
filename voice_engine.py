import asyncio
import edge_tts
import uuid
import os

# ----------------------------------------
# AI VOICE MAP
# ----------------------------------------

VOICE_MAP = {

    "Sarah": "en-US-JennyNeural",      # Female

    "Alex": "en-US-GuyNeural",         # Male

    "Michael": "en-US-EricNeural"      # Male

}


# ----------------------------------------
# CREATE VOICE
# ----------------------------------------

async def speak(text, person):

    voice = VOICE_MAP.get(
        person,
        "en-US-GuyNeural"
    )

    filename = f"voice_{uuid.uuid4().hex}.mp3"

    communicate = edge_tts.Communicate(
        text=text,
        voice=voice,
        rate="+0%",
        pitch="+0Hz"
    )

    await communicate.save(filename)

    return filename


# ----------------------------------------
# GENERATE VOICE
# ----------------------------------------

def generate_voice(text, person):

    try:

        voice_file = asyncio.run(
            speak(
                text,
                person
            )
        )

        return voice_file

    except Exception as e:

        print("Voice Error:", e)

        return None