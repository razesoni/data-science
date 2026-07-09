from openai import OpenAI

client = OpenAI(api_key="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")

audio_file = open("audios/02_Exercise 1 Pure HTML Media Player.mp3", "rb")

translation = client.audio.translations.create(
    model="whisper-1", 
    file=audio_file,
)

print(translation.text)