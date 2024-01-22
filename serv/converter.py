import requests

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()


output = query("segment-audio.mp3")


"""
curl https://api-inference.huggingface.co/models/openai/whisper-large \
	-X POST \
	--data-binary '@segment-audio.mp3' \
	-H "Authorization: Bearer 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"
"""


from huggingsound import SpeechRecognitionModel

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-japanese")
audio_paths = ["segment-audio.mp3"]

transcriptions = model.transcribe(audio_paths)