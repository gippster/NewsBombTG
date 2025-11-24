from gtts import gTTS


def get_tts(text: str):
    gtts = gTTS(text, lang='ru')
    gtts.save('tts_google.mp3')

