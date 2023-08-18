import speech_recognition as sr
from pydub import AudioSegment
import os


def ogg2wav(ogg_file_name: str) -> str:
    wave_file_name = ogg_file_name.replace('.ogg', '.wav')
    segment = AudioSegment.from_ogg(ogg_file_name)
    segment.export(wave_file_name, format='wav')
    return wave_file_name


def ogg2text(ogg_path: str) -> str:
    wave_path = ogg2wav(ogg_path)
    r = sr.Recognizer()
    with sr.AudioFile(wave_path) as source:
        audio = r.record(source)
        text = r.recognize_google(audio_data=audio, language='ru-Ru')
    os.remove(wave_path)
    os.remove(ogg_path)
    return text
