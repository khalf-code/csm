from fastapi import FastAPI
from pydantic import BaseModel
from run_csm import generate_conversation

app = FastAPI()

class Utterance(BaseModel):
    text: str
    speaker_id: int

@app.post("/generate")
def generate_audio(conversation: list[Utterance]):
    try:
        formatted = [{"text": u.text, "speaker_id": u.speaker_id} for u in conversation]
        audio_path = generate_conversation(formatted)
        return {"message": "Audio généré", "file": audio_path}
    except Exception as e:
        return {"error": str(e)}
